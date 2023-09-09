import os
from langchain.chat_models import ChatOpenAI
import fitz


instruction_templates = {
    "summary": "Summarize the content and provide the main points.",
    "analysis": "Analyze the content critically, looking for rhetorical devices, tone, and any potential bias.",
    "context": "How does this content relate to existing knowledge or legislation?",
    "QA": "Are there any inconsistencies or inaccuracies in the summary and analysis?",
    "presentation": "Present the summarized and analyzed data in an easily digestible format."
}

document_questions = {
    "Vorgang": [
        "Was ist der Hauptzweck dieses Vorgangs?",
        "Welche Parteien oder Organisationen sind an diesem Vorgang beteiligt?",
        "Was sind die Schlüsseldaten im Zusammenhang mit diesem Vorgang?",
        "Welche Schritte wurden bisher in diesem Vorgang unternommen?",
        "Welche rechtlichen oder politischen Auswirkungen hat dieser Vorgang?",
        "Welche Behauptungen, Formulierungen und rhetorischen Stilmittel sollten aus einer kritischen Perspektive beachtet werden?"
        ],
    "Gesetzesentwurf": [
            "Was ist das Hauptziel des Gesetzesentwurfs?",
            "Wer hat den Gesetzesentwurf eingereicht?",
            "Welche Änderungen werden durch den Gesetzesentwurf vorgeschlagen?",
            "Wie wirkt sich der Gesetzesentwurf auf bestehende Gesetze aus?",
            "Gibt es Kontroversen oder Meinungsverschiedenheiten in Bezug auf den Gesetzesentwurf?",
            "Was für einen Ton hat das Dokument?", 
            "Was für sprachliche und rhetorische Mittel werden verwendet?"
        ],
    "Antrag": [
        "Was ist der Hauptzweck des Antrags?",
        "Wer hat den Antrag gestellt?",
        "Welche Maßnahmen oder Entscheidungen werden im Antrag vorgeschlagen?",
        "Welche Argumente werden im Antrag vorgebracht?",
        "Was sind die potenziellen Auswirkungen des Antrags?",
        "Welche Behauptungen, Formulierungen und rhetorischen Stilmittel sollten aus einer kritischen Perspektive beachtet werden?"
    ],
     "Unterrichtung": [
            "Welche Informationen werden in der Unterrichtung mitgeteilt?",
            "Wer ist der Absender der Unterrichtung?",
            "An wen ist die Unterrichtung gerichtet?",
            "Was sind die Schlüsselpunkte der Unterrichtung?",
            "Welche Handlungen oder Entscheidungen werden in der Unterrichtung empfohlen?",
            "Was für einen Ton hat das Dokument?", 
            "Was für sprachliche und rhetorische Mittel werden verwendet?"
        ],
    "Stellungnahme": [
        "Wer hat die Stellungnahme abgegeben?",
        "Auf welches Thema oder welche Angelegenheit bezieht sich die Stellungnahme?",
        "Was sind die Hauptpunkte der Stellungnahme?",
        "Gibt es Meinungsverschiedenheiten oder Kontroversen in der Stellungnahme?",
        "Welche Handlungen oder Entscheidungen werden in der Stellungnahme empfohlen?",
        "Was für einen Ton hat das Dokument?", 
        "Was für sprachliche und rhetorische Mittel werden verwendet?"
    ],
    "Beschlussempfehlung": [
        "Was ist der Hauptzweck der Beschlussempfehlung?",
        "Wer hat die Beschlussempfehlung abgegeben?",
        "Welche Entscheidungen oder Maßnahmen werden in der Beschlussempfehlung vorgeschlagen?",
        "Was sind die Gründe für die in der Beschlussempfehlung vorgeschlagenen Maßnahmen?",
        "Welche Auswirkungen könnten die vorgeschlagenen Maßnahmen haben?"
    ],
    "Bericht": [
        "Was ist das Hauptthema des Berichts?",
        "Wer hat den Bericht verfasst?",
        "Welche Schlüsselinformationen enthält der Bericht?",
        "Welche Schlussfolgerungen werden im Bericht gezogen?",
        "Welche Empfehlungen werden im Bericht gegeben?"
    ],
    "Kleine": [
            "Was ist das Hauptthema des Berichts?",
            "Wer hat den Bericht verfasst?",
            "Welche Schlüsselinformationen enthält der Bericht?",
            "Welche Schlussfolgerungen werden im Bericht gezogen?",
            "Welche Empfehlungen werden im Bericht gegeben?",
            "Was für einen Ton hat das Dokument?", 
            "Was für sprachliche und rhetorische Mittel werden verwendet?"
        ]
}

class LegislativeDocumentProcessor:
    def __init__(self, document, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.document = document

    def _build_prompt(self, content):
        instructions = {
            "role": "referent",
            "team_role": "teamleiter",
            "action": "zusammenfassen",
            "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
            "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
            "special_instruction": ["CreateOpenBookMemory", "Structurise"]
        }

        return f"""
        
        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][3]}: {content}.
        Du arbeitest als Teil eines Teams.
        Deine Rolle ist {instructions["team_role"]}.
        Bitte fasse auch für das dynamische OpenBookMemory zusammen.
        """
    
    messages = [
        ("system", f"Du bist {instructions['role']}"),
        ("human", f"""Du arbeitest in einem Teil und deine Rolle ist {instructions['team_role']}.
        Der name des aktuellen Dokuments ist {self.document["title"]}.
        Du bist außerdem dafür verantwortlich den ersten Eintrag für das "OpenBookMemory" zu schreiben. 
        Aufgrund dieser Arbeitsvorlage werden deine Teammitglieder die Arbeit fortsetzen. 
         """),
        ("ai", "Alles klar, was steht in dem Dokument?"),
        ("human", "Das Dokument: {document}")
    ]


    def process_document(self, content):
        model = ChatOpenAI(
            temperature=0,
            openai_api_key=self.api_key,
            model="gpt-3.5-turbo-0613"
        )
        prompt = self._build_prompt(content)
        response = model.generate(prompt)
        return response

# Test
sample_document = {
    "title": "Gesetz zur Änderung des Lobbyregister- und des Lobbyistenverhaltensgesetzes",
    "type": "Vorgang",
    "id": 300955,
    "intiative": ["gruene", "spd", "fdp"],
    "important_files": [
        "BT-Drucksache 20/7356",
        "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"
    ],
    "content": "..."
}

processor = LegislativeDocumentProcessor(sample_document)
summary = processor.process_document(sample_document["content"])
print(summary)

