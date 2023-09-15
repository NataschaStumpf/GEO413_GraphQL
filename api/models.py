from app import db  # Importieren der SQLAlchemy-Datenbankinstanz aus Ihrer Flask-App


# Definieren einer Datenbanktabelle für Posts
class Post(db.Model):
    # Option, um eine vorhandene Tabelle zu erweitern, falls sie bereits existiert
    __table_args__ = {'extend_existing': True}

    # Definieren von Spalten in der Datenbanktabelle
    id = db.Column(db.Integer, primary_key=True)  # Eine eindeutige ID für jeden Beitrag
    title = db.Column(db.String)  # Der Titel des Beitrags als Zeichenkette
    description = db.Column(db.String)  # Eine Beschreibung des Beitrags als Zeichenkette
    created_at = db.Column(db.Date)  # Das Erstellungsdatum des Beitrags als Datum

    # Eine Methode, um die Daten des Beitrags in ein Wörterbuch umzuwandeln
    def to_dict(self):
        return {
            "id": self.id,  # Die ID des Beitrags
            "title": self.title,  # Der Titel des Beitrags
            "description": self.description,  # Die Beschreibung des Beitrags
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))  # Das formatierte Erstellungsdatum
        }
