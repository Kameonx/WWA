# Whiteboard Web App

A web-based collaborative whiteboard that allows you to organize ideas with sticky notes, images, and GIFs in a shared session environment.

---

## About This App

This application provides a flexible whiteboard space where you can add, move, and resize various elements. Data is stored on the server, enabling real-time collaboration between multiple users on different devices. The app features session management so multiple teams can have separate whiteboards without seeing each other's content.

## Using Whiteboard Web App

You can access the app in two ways:

### Option 1: Use the Hosted Version
🌐 Access the online version at: https://kameon3.pythonanywhere.com

### Option 2: Run Locally
🐍 Run on your own computer:

1. Download and extract the contents of the repository.
2. Install the required dependencies with `pip install -r requirements.txt`
3. Run the application with `python app.py`
4. Open your browser and navigate to `http://127.0.0.1:5000/`
5. Enter a session name to create or join a collaborative whiteboard.
6. Share this session name with others to collaborate in real-time!

## Features

* **Real-time Collaboration**: Multiple users can view and edit the same whiteboard across different devices
* **Magnets**: Add containers that can hold images or GIFs
* **Notes**: Add sticky notes with editable text content
* **Image Upload**: Upload images from your device to magnets
* **GIF Search**: Search and add Tenor GIFs with real-time results
* **Dark Mode**: Toggle between light and dark themes
* **Session Management**: Create separate whiteboard sessions with unique names
* **Persistence**: All content is saved automatically to the server
* **Mobile Support**: Full touch support for mobile devices
* **Drag & Drop**: Easily position elements anywhere on the whiteboard
* **Resize**: Adjust the size of magnets and notes as needed
* **Dot Grid Background**: Visual reference grid for alignment

## How It Works

The application uses HTML5, CSS3, and JavaScript for the frontend functionality, with Flask providing the backend server. Data is stored on the server with client synchronization, enabling real-time collaboration across multiple devices. The Tenor API integration allows for searching and embedding GIFs directly into your whiteboard elements.

## Technical Details

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python with Flask
* **Storage**: Server-side with client synchronization
* **API Integration**: Tenor GIF API
* **Design**: Responsive layout with dark/light mode support
* **Mobile-Optimized**: Touch events for better mobile experience

---

Feedback always welcome!

Email: Kameon@live.com

Created using VS Code, Python, and Flask. 2023.

Thank you,

-Kameon