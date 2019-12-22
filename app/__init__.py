from flask import Flask
from config import Config
# from Flask_boostrap import Bootstrap
app= Flask(__name__)
# bootstrap = Bootstrap(app)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)

from app import routes