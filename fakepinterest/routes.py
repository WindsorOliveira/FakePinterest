#Onde cria as rotas do sites
from flask import render_template, url_for
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario
from flask_login import  login_required
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(usename=formcriarconta.username.data,
                          email=formcriarconta.email.data, senha=senha)

        database.session.add(usuario)
        database.session.commit()
    return render_template("criarconta.html", form=formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)