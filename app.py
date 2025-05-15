import sys
import os
from flask import Flask, request, jsonify
from agent.First_agent import run_agent,run_agent_transcribe # Ensure this is the correct path and file

# Ensure parent path is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

@app.route("/create-course", methods=["POST"])
def course_creation():
    data = request.get_json()

    course_name = data.get("course_name")
    level = data.get("level")
    expected_outcomes = data.get("expected_outcomes")

    if not course_name or not level or not expected_outcomes:
        return jsonify({"error": "Missing one or more required fields"}), 400

    try:
        result = run_agent(course_name, level, expected_outcomes)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/transcribe-video', methods=['POST'])
def analyze_video():
    data = request.get_json()
    youtube_url = data.get('youtube_url')

    if not youtube_url:
        return jsonify({'error': 'YouTube URL is required'}), 400

    response = run_agent_transcribe(youtube_url)

    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True)
