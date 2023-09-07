import requests

BASE_URL = "https://search.dip.bundestag.de/api/v1/"
API_KEY = "rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF"  # replace with your actual API key
RESOURCE_TYPE = "dokument"  # to fetch documents related to a Vorgang

def get_documents(vorgang_id):
    documents = []
    params = {
        "f.vorgang": vorgang_id,
        "apikey": API_KEY
    }

    while True:
        response = requests.get(f"{BASE_URL}{RESOURCE_TYPE}", params=params)
        data = response.json()

        if "documents" in data:
            documents.extend(data["documents"])

        # If there's no cursor or it's the same as the previous one, break
        if not data.get("cursor") or data.get("cursor") == params.get("cursor"):
            break

        # Update the cursor for the next iteration
        params["cursor"] = data["cursor"]

    return documents

if __name__ == "__main__":
    vorgang_id = "300955"  # replace with the ID of your desired Vorgang
    all_documents = get_documents(vorgang_id)

    # Print or process the documents as you wish
    for doc in all_documents:
        print(doc)


# curl "https://search.dip.bundestag.de/api/v1/dokument?f.vorgang=300955&apikey=YOUR_API_KEY"
 