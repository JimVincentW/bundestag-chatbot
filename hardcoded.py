import os
import sys
import fitz
import langchain
from langchain.chat_models import ChatOpenAI

type = "Vorgang"
id = 300955
intiative = ["gruene", "spd", "fdp")]
important_files = ["BT-Drucksache 20/7356", "1. Beratung BT-Plenarprotokoll 20/113, S. 13947C-13959B"]
important_item_1 = important_files[0]
important_item_2 = important_files[1]



#Model A 
# Purpose: Summarize, suggest Topics, extract Keywords
# Input: Text Headline & Bold Statement
# Output: Keywords, Topics, Summary
# Value Add: Pointing to the important sections of the Document, Starting OpenBookMemory


instruction_overhead_chain_1 = [
    "role" : "referent",
    "team_role" : "teamleiter",
    "action" : "zusammenfassen", 
    "type" : "Vorgang",
    "input" : ["Titel", "Struturzeilen", "Keywords", "Text"],
    "output" : ["Keywords", "Topics", "Summary", "Important Sections", "OpenBookMemory"]
    "special_instruction" : "CreateOpenBookMemory", "Structurise"
]

MODEL_A = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo-0613")

A_Template = f"""
Du bist {instruction_overhead_chain_1["role"]} und sollst {instruction_overhead_chain_1["type"]}s Dokumente des Bundestags {instruction_overhead_chain_1["action"]}.
Dafür hast du folgendes Dokument zur Verfügung:
{instruction_overhead_chain_1["input"][0]}: {important_item_1}.

Du arbeitst als Teil eines Teams.
Deine Rolle ist {instruction_overhead_chain_1["team_role"]}.



"""
