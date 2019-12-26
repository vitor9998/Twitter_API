from flask import Flask
from tuapi import Lista, Tweets



app = Flask(__name__)
app.register_blueprint(Lista)




try:
    app.run(debug=True)
except Exception as ex:
    print(f'''Erro ao levantar a aplicação.
Exception: {str(ex)}''')