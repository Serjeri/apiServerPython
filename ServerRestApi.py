# написать rest api сервес по бронированию комнат
# Делается

from flask import Flask, jsonify, request
app = Flask(__name__)


rooms = [
    {
        'id': 1,
        'room': 'atelier',
        'quantity': 10
    },
    {
        'id': 2,
        'room': 'one-room_apartment',
        'quantity': 3
    },
    {
        'id': 3,
        'room': 'two-room_apartment',
        'quantity': 5
    }
]

@app.route('/rooms', methods=['GET'])
def get_list():
    return jsonify(rooms)

@app.route('/rooms/<int:room_name>', methods=['PUT'])
def update_room(room_name):
    item = next((x for x in rooms if x ['room'] == room_name), None)
    params = request.json
    item.update(params)
    return item

@app.route('/rooms/<int:room_name>', methods=['DELETE'])
def delete_room(room_name):
    id_room, _ = next((x for x in enumerate(rooms) if x[1] ['room'] == room_name), (None,None))
    rooms.pop(id_room)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)


