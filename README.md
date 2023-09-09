
🚧 Under construction 🚧s

This project is a second version to use large language models (LLMs) for assisting in the review of parliamentary documents.

This is an variant project "bt-reviewer". Here the main focus of presenting documents of the german parliamentary processes is by dynamically injecting knowledge into LLM Chains with the goal of finally producing well informed Chatbots.

The retrieval of information is done by either:
1. direct instructions for automated information retrieval

2. by using a chatbot which autonomously retrieves information from the database

So far only the first option is under development. 
The choice of database type(s) is not yet decided.

Solutions involing modern Vector-Databases are likely, although hybrid approaches are also possible.

This project works with langchain to set up prompt templates, a catalogue of questions and isntructions as well as a automated review process.

Scope for v1:
- Setting up one Pipeline for each process


# Model Usage
The project makes use of OpenAIs GPT-4 Model. If you do not have acess to this model, use the GPT-3.5 models instead. Change the line of the main script to do so.
To see which models your orgaisation is allowed to use, run the oai_models.py script.

# Setup

### 1. Clone the repository:
```bash
git clone https://github.com/JimVincentW/bundestag-chatbot.git
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

### With Docker:
To enter the OpenAI API key, export it as an environment variable in your terminal or set it in the .env file in the root directory of the project.

```bash
export OPENAI_API_KEY="<key>"  
```

```bash
docker-compose build
docker-compose up -d
docker exec -it bundestag-chatbot /bin/sh  
```

Then, inside the container, run the script:
```bash
python main.py
```

This way, the OpenAI API key will be set as an environment variable in the Docker container, and your Python script can use it to make requests to the OpenAI API.



###Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)

