from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        i = 0
        texto = request.form['usuario']
        texto_guardar = {f"{texto}{i}": texto}
        with open("datos.json", "a") as archivo:
            json.dump(texto_guardar, archivo)
            i += 1
      
    return '''
        <form method="post">
            <input type="text" name="usuario">
            <input type="text" name="contraseña">
            <input type="submit">
        </form>
    '''


if __name__ == "main":
    app.run()

app.run(host='0.0.0.0', port=8080, debug=True)