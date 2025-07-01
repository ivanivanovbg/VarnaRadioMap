# VarnaRadioMap

**VarnaRadioMap** is a web-based application that displays marine radio navigation warnings and allows users to upload and visualize maritime routes. It is focused on the region around Varna, Bulgaria, and supports interactive map-based exploration of navigational warnings.

## 🌐 Live Demo

http://185.177.57.26:3000

## ✨ Features

- 📡 Fetch and display current NAVWARNs (navigational warnings)
- 🗺 Upload GPX/CSV-like maritime routes and visualize them on a map
- 🧭 Built-in route conversion and map overlay
- ⚡ FastAPI back-end with React + Leaflet front-end (not included in this repo)

## 🧰 Tech Stack

- **Backend:** FastAPI, BeautifulSoup4, Pydantic, LXML
- **Frontend:** React with Leaflet for interactive maps
- **Deployment:** Uvicorn ASGI server

## 🚀 API Endpoints

### `GET /navwarnings/`
Returns a list of current NAVTEX-like navigation warnings.

### `POST /routes/`
Accepts a route file upload (CSV/GPX) and returns geo-coordinates for frontend rendering.

## 📦 Installation

### Backend Setup

```bash
# Clone the repo
git clone https://github.com/ivanivanovbg/VarnaRadioMap
cd VarnaRadioMap

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
