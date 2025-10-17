# Cloud Migration Demo Application

A simple Python Flask web application that displays hardware ID and current UTC time, storing records in a local SQLite database.

## Files Structure
```
migration-demo/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
└── demo.db               # SQLite database (created automatically)
```

## Installation

1. **Install Python 3.6+**
   Make sure Python 3.6 or higher is installed on your system.

2. **Create project directory**
   ```bash
   mkdir migration-demo
   cd migration-demo
   ```

3. **Save the files**
   Copy app.py, requirements.txt, and templates/index.html to your project directory.

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install Flask directly:
   ```bash
   pip install Flask
   ```

## Running the Application

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open in browser**
   Go to: http://localhost:5000

3. **Using the application**
   - The page displays current hardware ID and UTC time
   - Click "Save to Database" to store current info
   - Click "Refresh Records" to see saved records
   - Time updates automatically every 5 seconds

## Features

- **Hardware ID**: Uses system MAC address as unique identifier
- **UTC Time**: Real-time UTC timestamp
- **SQLite Database**: Stores records locally in demo.db file
- **Simple Interface**: Clean web interface for demonstrations

## For Cloud Migration Demo

This application is perfect for demonstrating:
- Application state before migration
- Continuous operation during migration
- Data persistence after migration
- Hardware identification across cloud environments

## Stopping the Application

Press `Ctrl+C` in the terminal to stop the Flask server.

## Database

The SQLite database (demo.db) is created automatically and stores:
- Unique record ID
- Hardware ID
- UTC timestamp
- Save timestamp

To reset the demo, simply delete the demo.db file.
