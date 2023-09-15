# curl "https://search.dip.bundestag.de/api/v1/dokument?f.vorgang=300955&apikey=YOUR_API_KEY"
 
import requests

BASE_URL = "https://search.dip.bundestag.de/api/v1/"
API_KEY = "rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF"  # Make sure to replace with your actual API key and keep it safe!
RESOURCE_TYPE = "dokument"

def get_documents(vorgang_id):
    documents = []
    params = {
        "f.vorgang": vorgang_id,
        "apikey": API_KEY
    }

    while True:
        response = requests.get(f"{BASE_URL}{RESOURCE_TYPE}", params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}. Message: {response.text}")
            break
        
        data = response.json()

        if "documents" in data:
            documents.extend(data["documents"])

        if not data.get("cursor") or data.get("cursor") == params.get("cursor"):
            break

        params["cursor"] = data["cursor"]

    return documents

if __name__ == "__main__":
    vorgang_id = "300955"
    all_documents = get_documents(vorgang_id)

    for doc in all_documents:
        print(doc)

    print(f"Found {len(all_documents)} documents for Vorgang {vorgang_id}")
