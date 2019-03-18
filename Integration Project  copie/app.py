
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route("/")
def root(): 
    query = """
        SELECT Incidenct_Code, Creation_DateTime
        FROM mytable 
        """

    posts = db.engine.execute(query)

    return render_template("Homepage.html", posts=posts)


if __name__ == '__main__':
     app.run(debug=True)
