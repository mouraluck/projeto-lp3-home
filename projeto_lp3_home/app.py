from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista_produtos = [
    {"nome": "AmbientChá", "desc": "Este chá é milagroso"},
    {"nome": "CanabCreme", "desc": "Este creme é milagroso"},
    {"nome": "VerdeGel", "desc": "Este gel é milagroso"},
    ]
    return render_template('index.html', produtos=lista_produtos)

@app.route('/carrinho')
def carrinho():
    return render_template('../static/assets/html/carrinho.html')