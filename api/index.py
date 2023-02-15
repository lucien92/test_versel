from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def survey():
    # if request.method == 'POST':
    #     result = request.form['number'] #permet de récupérer le résultat du formulaire
    #     return redirect(url_for('result', variable=result)) #rédirige vers une autre page en faisant passer une variable

    # don't need to test request.method == 'GET'
    return render_template('form.html')

# @app.route('/')
# def hello():
#     return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)