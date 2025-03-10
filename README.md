# Time API

A simple FastAPI application that provides time-related endpoints.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
```bash
uvicorn src.main:app --reload
```

### Using Docker
```bash
docker build -t time-api .
docker run -p 8000:8000 time-api
```

## API Endpoints

- `GET /`: Hello World message
- `GET /time`: Current time and timezone
- `GET /docs`: API documentation (Swagger UI)
