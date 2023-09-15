import os
from langchain.chat_models import ChatOpenAI
import fitz

import os
from langchain.chat_models import ChatOpenAI
import fitz

sample_document = {
    "type": "Vorgang",
    "id": 300955,
    "intiative": ["gruene", "spd", "fdp"],
    "important_files": [
        "BT-Drucksache 20/7356",
        "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"
    ],
    "content": "Just some random text for now."
}

class TeamLeiter:

    def __init__(self, document):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
        self.document = document
        self.model = ChatOpenAI(
            temperature=0,
            openai_api_key=self.api_key,
            model="gpt-3.5-turbo-0613"
        )

    def Referent_Leiter(self, content, id, type, title):
        instructions = {
            "role": "referent", #optionds: referent, journalist,
            "document_type": "VorgangsDokument", 
            "team_role": "teamleiter",
            "action": "zusammenfassen",
            "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
            "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
            "special_instruction": ["CreateOpenBookMemory", "Structurise"]
        }

        referenten_model = ChatOpenAI(
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo-0613"
        )


        ## Referent der neue ein Team leitet, schreibt Zusammenfassung in OpenBookMemory

        prompt = f"""
        Du bist {instructions["role"]} und 
        sollst {instructions["document_type"]}s Dokumente des Bundestags {instructions["action"]}.
        
        Du arbeitest als Teil eines Teams.
        Deine Rolle ist {instructions["team_role"]}.

        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][3]}: {content}.
        
        Bitte fasse auch für das dynamische OpenBookMemory zusammen.
        Für das Memory reicht es aus, wenn du die wichtigsten Punkte zusammenfasst.

        Damit dein Ergebnis rausgelesen werden kann, verwende bitte folgende Struktur:
        Dokumentnummer: {self.document["id"]}
        Dokumenttyp: {self.document["type"]}
        Dokumenttitel: {self.document["title"]}
        Zusammenfassung:
        Memory:
        """
        
        
        input = str(prompt)
        output = referenten_model(prompt)

        return input, output
    

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







def JournalistLeiter(self, content, OpenBookMemory):
    instructions = {
        "role": "journalist", #optionds: referent, journalist, 
        "document_type": "Pleanrsprotokolle",
        "team_role" : "teamleiter",
        "action": "berichten",
        "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
        "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
        "special_instruction": ["CreateOpenBookMemory", "Structurise"],
        "memory" : OpenBookMemory
    }

    model = ChatOpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo-0613"
    )

    prompt = f"""
    Du bist {instructions["role"]} und sollst über {instructions["document_type"]}s 
    Dokumente des Bundestags {instructions["action"]}.
    Dafür hast du folgendes Dokument zur Verfügung:
    {instructions["input"][3]}: {content}.
    

    """
    
    responste = model(prompt)
    return response, OpenBookMemory


processor = TeamLeiter(sample_document)
summary = processor.Referent_Leiter(sample_document["content"])
print(summary)


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
        if not self.api_key:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
        self.document = document
        self.model = ChatOpenAI(
            temperature=0,
            openai_api_key=self.api_key,
            model="gpt-3.5-turbo-0613"
        )


    def ModelA(self, content):
        instructions = {
            "role": "referent", #optionds: referent, journalist, 
            "team_role": "teamleiter",
            "action": "zusammenfassen",
            "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
            "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
            "special_instruction": ["CreateOpenBookMemory", "Structurise"]
        }

        model = ChatOpenAI(
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo-0613"
        )


        ## Referent der neue ein Team leitet, schreibt Zusammenfassung in OpenBookMemory

        prompt = f"""
        Du bist {instructions["role"]} und sollst {instructions["action"]}s Dokumente des Bundestags {instructions["action"]}.
        
        Du arbeitest als Teil eines Teams.
        Deine Rolle ist {instructions["team_role"]}.

        Du wirst den ersten Teil des Dokumentes lesen, es kann sein, dass der 

        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][3]}: {content}.
        
        Bitte fasse auch für das dynamische OpenBookMemory zusammen.
        Für das Memory reicht es aus, wenn du die wichtigsten Punkte zusammenfasst.

        Damit dein Ergebnis rausgelesen werden kann, verwende bitte folgende Struktur:
        Dokumentnummer: {self.document["id"]}
        Dokumenttyp: {self.document["type"]}
        Dokumenttitel: {self.document["title"]}
        Zusammenfassung:
        Memory:
        Deine Antwort hat bitte als letzten Teile

        """
        
        response = model(prompt)


        
        #  Parse respone's lines after intro strings with pydantic

        
      
        # Write lines after Zusammenfassung into text file
        with open("OpenBookMemory.txt", 'r') as file:
            lines = file.readlines()    


        # Write lines after ObenBookMemory into text file
        with open("OpenBookMemory.txt", 'r') as file:
            lines = file.readlines()

        # Write lines into OpenBookMemory
        OpenBookMemory = []
        for line in lines:
            OpenBookMemory.append(line)

    
        return response, OpenBookMemory
            
                
    



        
    def ModelB(self, content, OpenBookMemory):
        instructions = {
            "role": "journalist", #optionds: referent, journalist, 
            "document_type": "Pleanrsprotokolle,"
            "team_role": "teamleiter",
            "action": "berichten",
            "input": ["Titel", "Struturzeilen", "Keywords", "Text"],
            "output": ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"],
            "special_instruction": ["CreateOpenBookMemory", "Structurise"]
            "memory" : OpenBookMemory
        }

        model = ChatOpenAI(
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo-0613"
        )

        prompt = f"""
        Du bist {instructions["role"]} und sollst über {instructions["document_type"]}s 
        Dokumente des Bundestags {instructions["action"]}.
        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][3]}: {content}.
        """
        
        OpenBookMemory = []

        messages = [
        ("system", "Du bist juristischer Referent des Bundestages."),
        ("human", "Bitte beantworte diesen Fragenkatalog zu dem angehängten Dokument in angemessener Knappheit. Um die Fragen zu beantworten arbeite bitte in Stichpunkten."),
        ("ai", "Alles klar, was sind die Fragen?"),
        ("human", "Die Fragen: {questions}. \n\nSei bitte so konkret wie möglich. Bei der Kritischen Perspektive zu der Rhetorik und benutzten sprachlichen Stilmitteln bitte die Begriffe und die Kritikpunkte daran kurz aufschreiben. "),
        ("ai", "Okay, was ist das Dokument?"),
        ("human", "Das Dokument: {document}")
        ]


        response = model(prompt)
        return response, OpenBookMemory

sample_document = {
    "type": "Vorgang",
    "id": 300955,
    "intiative": ["gruene", "spd", "fdp"],
    "important_files": [
        "BT-Drucksache 20/7356",
        "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"
    ],
    "content": "Just some random text for now."
}


processor = LegislativeDocumentProcessor(sample_document)
summary = processor.ModelA(sample_document["content"])
print(summary)
Ä