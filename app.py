from models import *
from flask import Flask, render_template, make_response, request


app = Flask(__name__)

@app.route('/getbyid', methods=['GET'])
def get_by_id():

    id = request.args.get('id', type=int)

    if id and id > -1:
        try:
            name = Data.get_by_id(id).name
            age = Data.get_by_id(id).age
        except:
            return make_response('<h2>Ошибка 404 <br> Не найдено :(</h2>', 404)
        return render_template('index.html', id=id, name=name, age=age)
    return make_response('<h2>Ошибка 404 <br> Не найдено :(</h2>', 404)
    
if __name__ == '__main__':
    app.run(debug=True)
