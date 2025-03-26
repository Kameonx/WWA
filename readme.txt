# Whiteboard Web App

A web-based collaborative whiteboard that allows you to organize ideas with sticky notes, images, and GIFs in a private session environment.

---

## About This App

This application provides a flexible whiteboard space where you can add, move, and resize various elements. All data is stored locally in your browser, ensuring your information persists across sessions while maintaining privacy. The app features private session management so multiple users can have separate whiteboards without seeing each other's content.

## Using Whiteboard Web App

🐍 Run the app locally using Flask: https://kameon3.pythonanywhere.com

1. Download and extract the contents of the repository.
2. Install the required dependencies with `pip install -r requirements.txt`
3. Run the application with `python app.py`
4. Open your browser and navigate to `http://127.0.0.1:5000/`
5. Enter a session name to create or join a private whiteboard.

## Features

* **Magnets**: Add containers that can hold images or GIFs
* **Notes**: Add sticky notes with editable text content
* **Image Upload**: Upload images from your device to magnets
* **GIF Search**: Search and add Tenor GIFs with real-time results
* **Dark Mode**: Toggle between light and dark themes
* **Private Sessions**: Create separate whiteboard sessions with unique names
* **Persistence**: All content is saved automatically to local storage
* **Drag & Drop**: Easily position elements anywhere on the whiteboard
* **Resize**: Adjust the size of magnets and notes as needed
* **Dot Grid Background**: Visual reference grid for alignment

## How It Works

The application uses HTML5, CSS3, and JavaScript for the frontend functionality, with Flask providing the backend server. Data is stored in the browser's localStorage, ensuring your information persists between sessions without the need for a database. The Tenor API integration allows for searching and embedding GIFs directly into your whiteboard elements.

## Technical Details

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python with Flask
* **Storage**: Browser localStorage
* **API Integration**: Tenor GIF API
* **Design**: Responsive layout with dark/light mode support

---

Feedback always welcome!

Email: Kameon@live.com

Created using VS Code, Python, and Flask. 2023.

Thank you,

-Kameon