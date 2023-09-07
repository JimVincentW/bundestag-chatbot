import os
from langchain.chat_models import ChatOpenAI

class LegislativeDocumentProcessor:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.document = {
            "type": "Vorgang",
            "id": 300955,
            "intiative": ["gruene", "spd", "fdp"],
            "important_files": [
                "BT-Drucksache 20/7356",
                "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"
            ]
        }
    

    def ModelA(self):
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
        Du bist {instructions["role"]} und sollst {instructions["type"]}s Dokumente des Bundestags {instructions["action"]}.
        Dafür hast du folgendes Dokument zur Verfügung:
        {instructions["input"][0]}: {self.document["important_files"][0]}.

        Du arbeitest als Teil eines Teams.
        Deine Rolle ist {instructions["team_role"]}.

        Bitte fasse auch für das dynamische OpenBookMemory zusammen.
        """

        response = model.generate(prompt)
        # Process the response as needed
        # Update OpenBookMemory, etc.
        return response

    # Models B, C, D, E can be similarly defined

processor = LegislativeDocumentProcessor()
processor.ModelA()
