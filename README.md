# azure-openai-chat
Sample Project for Azure Open AI Chat

# Test Environment Setup
1. (Recommended) Create a virtual environment
2. Install the required packages within the virtual environment

   `pip install --no-cache -r requirements.txt`

# Update Environment Variables
1. Copy `.env.example` to `.env`
2. Add API key, endpoint, version, and model for Azure Open AI in `.env`

# Test the Standalone Application (`app.py`)
1. Modify `app.py` as needed (e.g., system role and query).
2. Run `app.py`.

   `python app.py`

# Test the API Service (`api.py`)
1. Run `api.py`

   `python api.py`
2. Open a web browser and navigate to [http://127.0.0.1:8080/?role=travel professional&q=introdce to Ilan city in Taiwan](http://127.0.0.1:8080/?role=travel%20professional&q=introdce%20to%20Ilan%20city%20in%20Taiwan)

# Test the Web Application (`web.py`)
1. Run `web.py`

   `python web.py`
2. Open a web browser and navigate to http://127.0.0.1:8081

# Exercises
1. Deploy `web.py` to an Azure Virtual Machine.
2. Deploy `web.py` to Azure Container Instances.
3. Deploy `api.py` to Azure Functions.