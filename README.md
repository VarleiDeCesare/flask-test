# Flask Destinations CRUD API

A simple REST API built with Flask and SQLAlchemy for managing travel destinations. This project demonstrates basic CRUD operations with SQLite database.

## Features

- ✅ Create new destinations
- ✅ Read all destinations or by ID
- ✅ Update existing destinations
- ✅ Delete destinations
- ✅ SQLite database integration
- ✅ JSON responses

## Tech Stack

- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database

## Project Structure

```
flask-destinations-api/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/destinations` | Get all destinations |
| GET | `/destinations/<id>` | Get destination by ID |
| POST | `/destinations` | Create new destination |
| PUT | `/destinations/<id>` | Update destination |
| DELETE | `/destinations/<id>` | Delete destination |

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd project_name
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv api_env
   ```

3. **Activate virtual environment**
   
   **On macOS/Linux:**
   ```bash
   source api_env/bin/activate
   ```
   
   **On Windows:**
   ```bash
   api_env\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   flask run
   ```
   
   Or alternatively:
   ```bash
   python app.py
   ```

   Debug Mode:
   ```bash
   flask run --debug
   ```

6. **Access the API**
   
   The server will start at `http://localhost:5000`


### New features to implement

1. **Implement data validation on POST HTTP verb**
2. **Change SQLITE to postgres or Mysql using Docker compose to handle**
3. **Deploy the application on AWS or equivalent**