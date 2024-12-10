# DC Sentiment Analysis Tool (AI-powered)
The DC Sentiment Analysis Tool is a full-stack application that predicts the sentiment of user-inputted text (Positive, Negative, or Neutral) using OpenAI's AI models. The backend is built with Flask, while the frontend leverages React, Redux, and Axios to provide an intuitive user interface.

Basically, the tool receives a text input from the user and predicts whether the sentiment of the text is Positive, Negative, or Neutral.

# Features
**AI-Powered Sentiment Analysis:** Predicts the sentiment of input text in real-time.
**Full-Stack Architecture:** Backend API built with Flask and a responsive frontend using React.
**RESTful API:** Clean and reusable API endpoints for text sentiment analysis.
**Environment Variable Support:** Store sensitive information like API keys securely.

## Prerequisites

Python 3.6 or higher       
Node.js and npm (or Yarn)      
OpenAI account with a valid API key      
Basic knowledge of React, Axios, and Flask      

# Backend Setup

1. Navigate to the backend directory:

```
cd backend
```
2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Set up environment variables:

* Create a `.env` file in the `backend/` folder:
```
OPENAI_API_KEY=your_openai_api_key
```

5. Start the Flask server:

```
python app.py
```

# Frontend Setup

1. Navigate to the frontend directory:

```
cd frontend
```

2. Install dependencies:

```
npm install
```

3. Update API URL:

* In `src/App.js`, ensure the base URL matches your backend's URL.

4. Start the React development server:

```
npm start
```

# API Endpoints
## Backend Endpoint
`POST /analyze`
* Description: Accepts a piece of text and returns the sentiment.
* Request:
  * Method: `POST`
  * Content-Type: `application/json`
  * Body:
``` 
{
    "text": "Your input text here"
}
```
  * Response:
``` 
{
    "sentiment": "Positive" | "Negative" | "Neutral"
}
``` 


## Usage 

* Open the React frontend in your browser (usually http://localhost:3000).
* Enter text into the input field and submit it.
* View the DC sentiment analysis results displayed on the page.

## Example
1.  Positive 
<img width="731" alt="image" src="https://github.com/user-attachments/assets/a7d65006-296a-484d-9c79-fe00b16ec81e">

2.  Negative 
<img width="747" alt="image" src="https://github.com/user-attachments/assets/5fb5fb65-899b-4cee-b3e8-7661375c1bf8">
