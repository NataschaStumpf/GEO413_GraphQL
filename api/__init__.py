# Import Flask Bibliotheken
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Erstellen einer Flask-App-Instanz
app = Flask(__name__)
# Aktivieren von Cross-Origin Resource Sharing (CORS) für die App
CORS(app)

# Konfigurieren der PostgreSQL-Datenbankverbindung
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
# Deaktivieren der Verfolgung von Änderungen in der Datenbank
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Erstellen der SQLAlchemy-Datenbankinstanz und Verknüpfen mit der Flask-App
db = SQLAlchemy(app)

# Eine einfache Route für die Startseite der API
@app.route('/')
def hello():
    return 'My First API !!!'