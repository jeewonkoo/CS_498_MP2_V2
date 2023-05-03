from flask import Flask, request, jsonify

app = Flask(__name__)
seed = 0
# @app.route('/')
# def hello_world():
#    return 'Hello World'

@app.route('/', methods=['POST', 'GET'])
def update_seed_value():
    # if request.method == 'POST':
    #     # string = bytes(your_str, 'utf-8')
    #     seed["num"] = request.json["num"]
    # else:
    #     return bytes(seed["num"], 'utf-8')
    global seed
    if request.method == 'POST':
        seed = int(request.json.get('num'))
        print(f'POST: {seed}')
        return jsonify(success=True)
    else:
        print(f'GET: {seed}')
        return str(seed)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)