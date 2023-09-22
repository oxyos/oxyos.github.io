from flask_frozen import Freezer
from app import app
import sys

freezer = Freezer(app)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building static site")
        freezer.freeze()
    else:
        print("Starting Flask server")
        app.run()
