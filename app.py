from flask import Flask, request, render_template, send_from_directory
from main_page.views import main_blueprint


app = Flask(__name__)






app.register_blueprint(main_blueprint)



if __name__ == "__main__":
    app.run(debug=True)
