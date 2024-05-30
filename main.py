# Import
from flask import Flask, render_template, request
import datetime


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')
# Druga strona
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Trzecia strona
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Obliczenia
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Strona z formularzem
@app.route('/form')
def form():
    return render_template('form.html')

# Obsługa wysyłania formularza
@app.route('/submit', methods=['POST'])
def submit_form():

    today = datetime.datetime.now()
    name = request.form['name']
    email = request.form['email']
    data = request.form['data']
    adres = request.form['adres']
    
    context = {
        'name': name,
        'email': email,
        'data': data,
        'adres': adres,
    }
    with open('form.txt', 'a',) as f:
        f.write(str(today.strftime("%D %H:%M:%S")) + "\n" + "Name: " + name + '\n' + "E-mail: " + email + '\n' + "Data: " + data + '\n' + "Adres: " + adres + '\n\n')
    return render_template('form_result.html', **context)

app.run(debug=True)
