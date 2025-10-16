# HNG Backend Stage 0 Task

A FastAPI application that serves personal information and random cat facts.

## Features

- Personal profile endpoint with name, email, and technology stack
- Random cat facts integration
- UTC timestamp display
- RESTful API design

## API Endpoints

- `GET /` - Welcome message with basic information
- `GET /me` - Personal profile with random cat fact and current UTC time

## Prerequisites

- Python 3.7 or higher
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/zinsu-moni/Hng_TASK_1.git
cd Hng_TASK_1
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Method 1: Using Uvicorn directly
```bash
uvicorn main:app --reload
```

### Method 2: Using Python module
```bash
python -m uvicorn main:app --reload
```

The application will start on `http://localhost:8000`

## Usage

Once the server is running, you can access:

- **Welcome endpoint**: `http://localhost:8000/`
- **Profile endpoint**: `http://localhost:8000/me`

### Example Response

**GET /me**
```json
{
  "status": "success",
  "email": "zinsusezonsu@gmail.com",
  "name": "Zinsu Sezonsu",
  "Stack": "FastApi",
  "fact": "A cat's hearing is better than a dog's.",
  "timestaps": "2025-10-16 14:30:45"
}
```

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Requests**: HTTP library for making API calls to cat facts service

## Environment Variables

No environment variables are required for basic functionality.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is part of the HNG Backend Track Stage 0 task.

## Contact

- **Name**: Zinsu Sezonsu
- **Email**: zinsusezonsu@gmail.com
- **GitHub**: [@zinsu-moni](https://github.com/zinsu-moni)

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 8000 is busy, specify a different port:
   ```bash
   uvicorn main:app --reload --port 8001
   ```

2. **Module not found errors**: Ensure you've activated your virtual environment and installed dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Cat fact API timeout**: The application handles API timeouts gracefully and will return an appropriate message.

## Development

To run in development mode with auto-reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

This makes the application accessible from other devices on your network.