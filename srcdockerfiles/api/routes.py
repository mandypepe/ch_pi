from flask import jsonify,request
from services.auth_guard import auth_guard
def init(app):

    @app.route('/Devops', methods=['POST'])
    @auth_guard()
    def protected_route():
        message= request.json.get('message')
        to = request.json.get('to')
        from_r=request.json.get('from')
        timeToLifeSec= request.json.get('timeToLifeSec')
        if not message or not to or not from_r or not timeToLifeSec :
            return jsonify({"message": " Data missing", "status": 400}), 400
        return jsonify({"message": f'Hello {to} your message will be send', "status": 200}), 200

    @app.route('/', methods=['GET'])
    def init_route():
        return jsonify({"message": f'Ave Imperator, morituri te salutant', "status": 200}), 200