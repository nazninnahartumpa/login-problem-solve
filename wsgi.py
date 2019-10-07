"""App entry point."""
from application import create_app
import os

app = create_app()
app.secret_key = os.getenv('SECRET_KEY')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
