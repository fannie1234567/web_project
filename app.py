#https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name} 5!"

@app.route("/fannie")
def hello_world_fannie():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name} fannie!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))