from flask import Flask, render_template, url_for


from config import config

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/login")  
def login():
    return render_template("auth/login.html") 
 

@app.route("/registro")
def registro():
    return render_template("auth/registro.html") 

@app.route("/programarCita")
def programarCita():
    return render_template("blog/programarCita.html") 
        
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()    




    