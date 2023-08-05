#Onde cria os formulários do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confir = SubmitField("Login")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Nome", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(8, 15)])
    confir_senha = PasswordField("Confirmar senha", validators=[DataRequired(), EqualTo("Senha")])
    botao_confir = SubmitField("Cadastrar")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")