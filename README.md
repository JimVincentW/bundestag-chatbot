This project is a first version to use large language models (LLMs) for assisting in the review of parliamentary documents.

As this is an early stage of the project, the scope is limited to the review of parliamentary processes ("Vorgänge") and their most important Documents ("wichtige Drucksachen") in the German Bundestag.

Since I have no Database to work on, I use the dip.bundestag.de website to scrape for the data (Additions using the DIP API are highly welcome). Links can be put in the console when running the script.

This project works with langchain to set up prompt templates, a catalogue of questions and an automated review process.

! Important ! 
The project makes use of OpenAIs GPT-4 Model. If you do not have acess to this model, use the GPT-3.5 models instead. Change the line of the main script to do so.
To see which models your orgaisation is allowed to use, run the oai_models.py script.

# Setup

### 1. Clone the repository:
```bash
git clone https://github.com/JimVincentW/bt-reviewer.git
```

### 2. Install the required packages:

```bash 
pip install -r requirements.txt
```

### 3. Export the OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="<key>"  
```

### 4. Run the script:

```bash
python main.py
```

Enter link of dip.bundestag.de process ("Vorgang")
e.g.:
```bash
https://dip.bundestag.de/vorgang/planungsstand-des-ausbaus-der-lehrter-bahn/302931?f.wahlperiode=20&f.typ=Vorgang&start=25&rows=25&pos=38
```


### With Docker:
To enter the OpenAI API key, export it as an environment variable in your terminal or set it in the .env file in the root directory of the project.

```bash
export OPENAI_API_KEY="<key>"  
```

```bash
docker-compose build
docker-compose up -d
docker exec -it bt-reviewer /bin/sh  
```

Then, inside the container, run the script:
```bash
python main.py
```
Enter link of dip.bundestag.de process ("Vorgang")
e.g.:
```bash
https://dip.bundestag.de/vorgang/planungsstand-des-ausbaus-der-lehrter-bahn/302931?f.wahlperiode=20&f.typ=Vorgang&start=25&rows=25&pos=38
```


This way, the OpenAI API key will be set as an environment variable in the Docker container, and your Python script can use it to make requests to the OpenAI API.


Result in console and results.txt:

###Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)

