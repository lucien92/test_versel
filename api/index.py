from flask import Flask, render_template
from flask import Flask, render_template, request, redirect
from flask import url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def survey():
    if request.method == 'POST':
        result = request.form['number'] #permet de récupérer le résultat du formulaire
        return redirect(url_for('result', variable=result)) #rédirige vers une autre page en faisant passer une variable

    # don't need to test request.method == 'GET'
    return render_template('form.html')



@app.route('/result/<variable>') #attention il faut bien mettre à la fin du chemin <variabnle> pour que la fonction result puisse récupérer le nom de la variable mis dans le redirect
def result(variable): #opn reprend le nom de la variable qui a été définie dans la fonction survey
     contenance = variable
     #result_final = algo(contenance) #OK ça devrait être bon, à tester en attendant et en améliorant le rendu de la page
     
     return render_template('result.html', result=contenance) #voir comment utiliser une variable dans le result.html