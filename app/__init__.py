
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomstuff'

app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '	2dc3f9dbdd07a4'

app.config['MAIL_PASSWORD'] = 'a1a2f3634e8d92'

mail = Mail(app)

from app import views