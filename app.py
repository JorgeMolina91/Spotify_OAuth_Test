import requests
import urllib.parse

from flask import Flask, redirect, request, jsonify, session
from datetime import datetime



app = Flask(__name__)
app.secret_key = '03678-6y745t-7245gfskiysrt6-765sfky5'

load_dotenv()
CLIENT_ID = 'CLIENT_ID' # This CLIENT_ID is getted from the Spotify dashboard settings
CLIENT_SECRET = 'CLIENT_SECRET'# This CLIENT_SECRET is getted from the Spotify dashboard settings
REDIRECT_URI = 'http://localhost:5000/callback' # This URI is the one I put on the Spotify dashboard

AUTH_URL = 'https://accounts.spotify.com/authorize' # This is the URL from which I'll get and refresh the authorization token
TOKEN_URL = 'https://accounts.spotify.com/api/token' 
API_BAE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "Greetings! 😁 <a href='/login'>Login with Spotify</a>"


@app.route('/login')
def login():
    scope = 'user-read-private user-read-email'

    params = { 
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True # This one is for the user to login everytime 
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)


@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({'error':request.args['error']})
        

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    
        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect('/playlists')


@app.route('/playlists')
def get_playlists():
    if 'access_token' not in session:
        redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    response = requests.get(API_BAE_URL + 'me/playlists', headers=headers)
    playlists = response.json()

    return jsonify(playlists)


@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/playlists')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    