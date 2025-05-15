from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
from automation_playwright import run_automation  # Ensure this is correctly imported

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "API is running. Use /run_automation to start automation."}), 200

@app.route('/run_automation', methods=['POST'])
def run_automation_endpoint():
    try:
        data = request.json
        username = data.get('username')
        material = data.get('material')
        speed = data.get('speed')
        position_type = data.get('position_type')
        positions = data.get('positions')
        
        # Pozisyonları tuple formatına dönüştür
        P1 = (
            float(positions["P1"]["x"]),
            float(positions["P1"]["y"]),
            float(positions["P1"]["z"]),
            float(positions["P1"].get("r", 0))  # R ekseni varsa ekle, yoksa 0
        )
        P2 = (
            float(positions["P2"]["x"]),
            float(positions["P2"]["y"]),
            float(positions["P2"]["z"]),
            float(positions["P2"].get("r", 0))
        ) if position_type == "Up, Down, Forward" else None
        P3 = (
            float(positions["P3"]["x"]),
            float(positions["P3"]["y"]),
            float(positions["P3"]["z"]),
            float(positions["P3"].get("r", 0))
        )
        
        num_iterations = data.get('iterations', 10)

       
        run_automation(username, material, speed, position_type, P1, P2, P3, num_iterations)

        return jsonify({"status": "success", "message": "Automation started successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
