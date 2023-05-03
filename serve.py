from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        # start a separate process to run stress_cpu.py
        subprocess.Popen(['python', 'stress_cpu.py'])
        return 'Started CPU stress test!'
    elif request.method == 'GET':
        # return the private IP address of the EC2 instance
        return 'Private IP address: ' + socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)
