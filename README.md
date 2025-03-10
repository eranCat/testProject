# Time API

A modern, lightweight FastAPI application that provides time-related information through RESTful endpoints. This service offers current time retrieval with timezone information, making it useful for applications that need to synchronize time data or display timezone-aware timestamps.

## Features

- Real-time timestamp retrieval
- Timezone information
- JSON response format
- OpenAPI documentation
- Docker support

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
