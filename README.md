# Spotify API OAuth2 Authentication with Flask
## Overview
This project demonstrates how to integrate Spotify authentication using OAuth2 with a Python Flask application. The application allows users to log in with their Spotify account, obtain authorization tokens, and access their playlists.

## Prerequisites
Before running the project, make sure you have the following:

1. Python 3 installed 
2. Required Python libraries: *requests*, *urllib.parse*, *flask*
3. Spotify Developer Account: Obtain your *CLIENT_ID* and *CLIENT_SECRET* from the Spotify Developer Dashboard.

## Getting Started
1. Clone the repository:  
`git clone https://github.com/your-username/spotify-oauth2-flask.git`

2. Install the required dependencies:  
`pip3 install -r requirements.txt`

3. Set up environment variables:  
- **CLIENT_ID:** Your Spotify Developer Dashboard client ID
- **CLIENT_SECRET:** Your Spotify Developer Dashboard client secret

4. Run the Flask application:  
`python3 app.py`

5. Open your web browser and navigate to `http://localhost:5000`

## Project Structure
- **app.py:** Flask application containing routes for authentication and accessing Spotify playlists.
- **requirements.txt:** List of Python dependencies.


## Usage
1. Visit the application at `http://localhost:5000`
2. Click on *"Login with Spotify"* to initiate the Spotify authentication process.
3. Grant necessary permissions, and you will be redirected back to the application.
4. Access your Spotify playlists at `http://localhost:5000/playlists`
5. To refresh the access token, visit `http://localhost:5000/refresh-token`

## Important Notes
- The application uses Flask for handling routes and requests.
- OAuth2 authorization code flow is implemented for obtaining access and refresh tokens.
- Tokens are stored in Flask session for subsequent API requests.
- The application checks token expiration and refreshes them when necessary.
  
## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.

License
This project is licensed under the **MIT License**.
