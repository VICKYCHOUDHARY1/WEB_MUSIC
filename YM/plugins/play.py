from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    track_id = data.get('track_id')
    return jsonify({'status': 'success', 'message': f'Playing track {track_id}'})

@app.route('/pause', methods=['POST'])
def pause():
    return jsonify({'status': 'success', 'message': 'Paused'})

@app.route('/next', methods=['POST'])
def next_track():
    return jsonify({'status': 'success', 'message': 'Next track'})

@app.route('/prev', methods=['POST'])
def prev_track():
    return jsonify({'status': 'success', 'message': 'Previous track'})
