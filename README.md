# Qna-Chatbot
Question Answering Chatbot using your PDFs


# PDF Helper Bot

A generative AI web application that can answer questions by referring to custom PDFs uploaded.

This is a web application is using a FAISS as a vectorsotre and answers questions about multiple PDFs uploaded to it at the beginning if the session.


![Logo](https://github.com/emarco177/documentation-helper/blob/main/static/pdf-helper.gif)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/gowriks12/Qna-Chatbot.git
```

Go to the project directory

```bash
  cd Qna-Chatbot
```

Install dependencies 

```bash
  conda env create -n <new env name> -f spec.yaml
```

This command will create a new conda environment with all the dependencies installed


Start the flask server

```bash
  streamlit run main.py
```

In the web application window, upload PDFs click "OK" and wait for it to process. Once it is completed, type your questions and ask away.
