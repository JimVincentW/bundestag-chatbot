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
        # ... other questions ...
    ],
    "Gesetzesentwurf": [
        "Was ist das Hauptziel des Gesetzesentwurfs?",
        "Wer hat den Gesetzesentwurf eingereicht?",
        # ... other questions ...
    ],
    # ... other document types ...
}

class LegislativeDocumentProcessor:

    def __init__(self, document):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.document = document

    def ModelA(self, content):
        instructions = {
            "role": "referent",
            "team_role": "teamleiter",
            "action": "zusammenfassen",
            "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
            "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
            "special_instruction": ["CreateOpenBookMemory", "Structurise"]
        }

        model = ChatOpenAI(
            temperature=0,
            openai_api_key=self.api_key,
            model="gpt-3.5-turbo-0613"
        )

        prompt = f"""
        Du bist {instructions["role"]} und sollst {instructions["action"]}s Dokumente des Bundestags {instructions["action"]}.
        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][3]}: {content}.

        Du arbeitest als Teil eines Teams.
        Deine Rolle ist {instructions["team_role"]}.

        Bitte fasse auch für das dynamische OpenBookMemory zusammen.
        """

        response = model.generate(prompt)
        # Extract and return the summary from the response (assumes summary is in the response)
        return response

sample_document = {
    "type": "Vorgang",
    "id": 300955,
    "intiative": ["gruene", "spd", "fdp"],
    "important_files": [
        "BT-Drucksache 20/7356",
        "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"
    ],
    "content": """This is a sample content of the Vorgang document that we'd like to summarize. It contains details about various legislative proceedings and other information relevant to the Bundestag."""
}

processor = LegislativeDocumentProcessor(sample_document)
summary = processor.ModelA(sample_document["content"])
print(summary)