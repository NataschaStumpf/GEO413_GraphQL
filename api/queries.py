from api.models import Post  # Importieren des Post-Modells aus Ihrem Projekt
from ariadne import convert_kwargs_to_snake_case


# Ein Resolver, der eine Liste aller Posts zurückgibt
def list_resolver(obj, info):
    try:
        # Die Abfrage aller Posts aus der Datenbank und Umwandlung in ein Dictionary-Format
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)  # Ausgabe der Posts (kann für Debugging-Zwecke nützlich sein)

        # Erstellung eines Payloads für eine erfolgreiche Abfrage
        payload = {
            "success": True,  # Erfolgsstatus auf True setzen
            "posts": posts  # Die Liste der Posts im Payload
        }
    except Exception as error:
        # Erstellung eines Payloads für den Fehlerfall
        payload = {
            "success": False,  # Erfolgsstatus auf False setzen
            "errors": [str(error)]  # Fehlermeldung hinzufügen
        }
    return payload  # Rückgabe des Payloads als Ergebnis der GraphQL-Abfrage


@convert_kwargs_to_snake_case  # Decorator zur Umwandlung der Argumente in Snake Case
def get_resolver(obj, info, id):
    # Versuchen, den Post mit der angegebenen ID aus der Datenbank abzurufen
    try:
        # Versuchen, den Post mit der angegebenen ID aus der Datenbank abzurufen
        post = Post.query.get(id)

        # Payload für eine erfolgreiche Abfrage erstellen
        payload = {
            "success": True,  # Erfolgsstatus auf True setzen
            "post": post.to_dict()  # Den einzelnen Post im Payload zurückgeben
        }
    except AttributeError:  # Wenn der Post nicht gefunden wurde
        payload = {
            "success": False,  # Erfolgsstatus auf False setzen
            "errors": ["Post item matching {id} not found"]  # Fehlermeldung hinzufügen
        }
    return payload  # Rückgabe des Payloads als Ergebnis der GraphQL-Abfrage
