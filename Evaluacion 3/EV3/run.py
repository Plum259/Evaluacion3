from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio1.html', methods=['GET','POST'])
def Ejercicio1():
    if request.method == 'POST':
        Nota1 = int(request.form['Nota1'])
        Nota2 = int(request.form['Nota2'])
        Nota3 = int(request.form['Nota3'])
        Asistencia = int(request.form['Asistencia'])
        resul = round((Nota1+Nota2+Nota3)/3)
        aprueba = "REPROBADO"
        if resul >= 40 and Asistencia >= 75:
            aprueba="APROBADO"
        return render_template('Ejercicio1.html', resultado=resul, aprueba=aprueba)
    return render_template('Ejercicio1.html')
@app.route('/Ejercicio2.html', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method == 'POST':
        Nombre1 = str(request.form['Nombre2'])
        Nombre2 = str(request.form['Nombre2'])
        Nombre3 = str(request.form['Nombre3'])
        nombres = [Nombre1, Nombre2, Nombre3]
        nombrelarg = max(nombres, key=len)
        caracteres = len(nombrelarg)
        return render_template('Ejercicio2.html', var=nombrelarg, caracteres=caracteres)
    return render_template('Ejercicio2.html')
if __name__ == '__main__':
    app.run(debug=True)
