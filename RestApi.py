from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

rooms = {
    1: {
        "room": "studioApartment",
        "Quantity": 7
    },
    2: {
        "room": "studioApartment",
        "Quantity": 5
    },
    3: {
        "room": "studioApartment",
        "Quantity": 10
    }
}

@app.route('/rooms', methods=['GET'])
def get_room():
    return jsonify(rooms)

@app.route('/rooms', methods=['POST'])
def create_room():
    rooms[len( rooms ) + 1] = request.json
    return jsonify(rooms)

@app.route('/rooms/<int:id>', methods=['PUT'])
def update_room(id):
    rooms.get(id).update(request.json)
    return jsonify(rooms)

@app.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    rooms.pop(id)
    return jsonify(rooms)


if __name__ == '__main__':
    app.run(debug=True)