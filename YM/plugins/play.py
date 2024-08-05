# app.py

from flask import Flask, request, jsonify
from play import play_music

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play():
    url = request.json.get('url')
    if url:
        try:
            play_music(url)
            return jsonify({ 'success': True })
        except Exception as e:
            return jsonify({ 'success': False, 'error': str(e) })
    return jsonify({ 'success': False, 'error': 'Please enter a URL.' })

if __name__ == '__main__':
    app.run(debug=True)
