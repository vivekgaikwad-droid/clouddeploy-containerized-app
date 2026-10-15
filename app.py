
from flask import Flask, jsonify
from datetime import datetime, timezone
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CloudDeploy | Experiment 5</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #101827;
                color: #f8fafc;
                display: grid;
                place-items: center;
                min-height: 100vh;
            }
            main {
                max-width: 650px;
                margin: 24px;
                padding: 36px;
                background: #1e293b;
                border-radius: 18px;
                box-shadow: 0 15px 45px #0005;
            }
            .tag { color: #67e8f9; font-weight: bold; }
            h1 { font-size: 2.2rem; }
            p { color: #cbd5e1; line-height: 1.7; }
            .status {
                background: #064e3b;
                padding: 14px;
                border-radius: 10px;
                color: #a7f3d0;
            }
            a { color: #67e8f9; }
        </style>
    </head>
    <body>
        <main>
            <span class="tag">AWS CLOUD COMPUTING PROJECT</span>
            <h1>CloudDeploy</h1>
            <p>Experiment 5: Design and Deploy a Containerized Application in AWS.</p>
            <div class="status">Application is running successfully.</div>
            <p>This Flask application is packaged in a Docker container
            for consistent deployment across environments.</p>
            <p>Container hostname: <strong>""" + socket.gethostname() + """</strong></p>
            <p><a href="/health">Check application health →</a></p>
        </main>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudDeploy",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
