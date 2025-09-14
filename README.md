# Flask Bootstrap App

This is a simple Flask application that utilizes Bootstrap 5 to create a beautiful user interface. The application serves as a starting point for building web applications with Flask and Bootstrap.

## Project Structure

```
flask-bootstrap-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── css
│           └── style.css
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-bootstrap-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:
```
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Features

- Home page with a responsive layout using Bootstrap 5.
- Custom CSS styles for enhanced appearance.
- Easy to extend and modify for additional features.

## License

This project is licensed under the MIT License.