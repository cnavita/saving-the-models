from flask import Flask, render_template, request
import joblib

# create instance of an app
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route('/')
def root1():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact', methods = ['POST'])
def contact():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    pred = model.predict([[int(preg), int(plas), int(pres), int(skin), int(test), int(mass), int(pedi), int(age)]])

    if pred[0] == 1:
        output = 'diabetic'

    else:
        output = 'diabetic'

    return render_template('contact.html' , predicted_text = f'the person is {output}')


#run the app
if __name__ == '__main__':
    app.run(debug=True) # debug = true will keep runing the program in server implicitly
