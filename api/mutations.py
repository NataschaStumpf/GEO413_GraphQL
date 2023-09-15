from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post


# Diese Funktion dient dazu, einen Beitrag in der Datenbank zu erstellen.
# Sie verwendet den convert_kwargs_to_snake_case-Dekorator, um die Argumente im snake_case-Format zu konvertieren.
@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        # Das heutige Datum wird ermittelt.
        today = date.today()

        # Ein neuer Beitrag wird erstellt, wobei das Datum im Format "Mon-Tag-Jahr" gespeichert wird.
        post = Post(
            title=title, description=description, created_at=today.strftime("%b-%d-%Y")
        )

        # Der Beitrag wird der Datenbank hinzugefügt und die Änderungen werden gespeichert.
        db.session.add(post)
        db.session.commit()

        # Ein Erfolgs-Payload wird erstellt, der den neuen Beitrag enthält.
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # Fehler bei falschem Datumsformat
        # Im Falle eines Fehlers wird ein Fehler-Payload erstellt.
        payload = {
            "success": False,
            "errors": [f"Falsches Datumsformat angegeben. Das Datum sollte im Format tt-mm-jjjj sein."]
        }

    # Der Payload wird zurückgegeben, um das Ergebnis der Funktion zu übermitteln.
    return payload
