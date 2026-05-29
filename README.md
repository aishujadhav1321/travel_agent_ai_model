# Travel Assistant AI

## Overview

Travel Assistant AI is a FastAPI + LangChain based AI project that provides travel recommendations using Google Gemini API.

## Features

* Travel destination recommendations
* AI-powered responses
* FastAPI backend
* Swagger API documentation
* Gemini AI integration

## Technologies Used

* Python
* FastAPI
* LangChain
* Google Gemini API
* Uvicorn

## Run Project

```bash
python -m uvicorn app:app --reload
```

## API Endpoint

```bash
POST /travel-assistant
```

## Example Request

```json
{
  "query": "Best places to visit in Goa"
}
```

## Example Response

```json
{
  "response": "Baga Beach, Calangute Beach, Fort Aguada..."
}
```

## Swagger UI

```text
http://127.0.0.1:8000/docs
```
