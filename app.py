from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/QuienesSomos')
def about():
    return render_template('QuienesSomos.html')

@app.route('/Servicios')
def services():
    return render_template('Servicios.html')  

@app.route('/servicio/<service_name>') 
def service(service_name):
    return render_template('service_detail.html', service_name=service_name)

@app.route('/noticias')
def news():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Recibe los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí podrías procesar y almacenar los datos
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
