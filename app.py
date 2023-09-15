# Importieren der erforderlichen Module und Klassen
from api import app, db  # Importieren der Flask-Anwendung und der SQLAlchemy-Datenbankinstanz
from ariadne import (
    load_schema_from_path,  # Laden des GraphQL-Schemas aus einer Datei
    make_executable_schema,  # Erstellen des ausführbaren GraphQL-Schemas
    graphql_sync,  # Synchrones Ausführen von GraphQL-Abfragen
    snake_case_fallback_resolvers,  # Fallback-Resolver für snake_case-Felder
    ObjectType,  # Importieren des ObjectType zur Definition von GraphQL-Typen
)
from flask import request, jsonify  # Importieren von Flask-Modulen für HTTP-Anforderungen und JSON-Antworten
from ariadne.explorer import ExplorerPlayground  # Importieren des GraphQL-Explorers (Playground)
#  from api.queries import list_resolver, get_resolver
#  from api.mutations import create_post_resolver

# Konfigurieren des GraphQL-Playground-Titels
PLAYGROUND_HTML = ExplorerPlayground(title="Cool API").html(None)

query = ObjectType("Query")
mutation = ObjectType("Mutation")

#  query.set_field("listPosts", list_resolver)
#  query.set_field("getPost", get_resolver)

#  mutation.set_field("createPost", create_post_resolver)

# Laden des GraphQL-Schemas aus einer Datei
type_devs = load_schema_from_path("schema.graphql")

# Erstellen eines ausführbaren GraphQL-Schemas mit snake_case-Fallback-Resolvers
schema = make_executable_schema(
    type_devs, query, mutation, snake_case_fallback_resolvers
)


# Endpoint für den GraphQL-Playground (GET-Anfrage)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200  # HTML-Seite des GraphQL-Explorers anzeigen


# Endpoint für den GraphQL-Server (POST-Anfrage)
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()  # JSON-Daten aus der POST-Anfrage abrufen
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400  # Statuscode basierend auf dem Erfolg der Abfrage festlegen
    return jsonify(result), status_code  # JSON-Antwort mit dem Abfrageergebnis und dem Statuscode senden