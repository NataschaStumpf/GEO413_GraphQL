# GEO413_GraphQL

![GitHub contributors](https://img.shields.io/github/contributors/Shadid12/GEO413_GraphQL)
![GitHub last commit](https://img.shields.io/github/last-commit/Shadid12/GEO413_GraphQL)

Dieses Projekt basiert auf einem ursprünglichen Repository von [Shadid12](https://github.com/Shadid12) und wurde modifiziert.

**Ursprüngliches Repository:** [Shadid12/flask-graphql](https://github.com/Shadid12/flask-graphql)

## Zielsetzung

- Einrichten eines Python-Webservers mit Flask.
- Verwendung der Ariadne-Bibliothek zur Implementierung von GraphQL.
- Zusammenstellung eines GraphQL-Schemas.
- Ausführung von Abfragen und Mutationen gegen eine Python GraphQL API.

## Anforderungen

- Python 3.9.13
- Erforderliche Python-Pakete: `flask`, `flask-sqlalchemy`, `flask-cors`, `ariadne`

## Vorbereitung

1. Erstellen und aktivieren Sie die Conda-Umgebung:

   ```shell
   conda env create -f GEO413_GraphQL.yml
   conda activate GEO413_GraphQL
   ```
2. Legen Sie eine Datenbank an (hier PostgreSQL)
   
4. Passen Sie 'api/__init__.py' an, indem Sie 'YourUserName', 'YourPassword', 'YourHostname', und 'YourDatabaseName' ersetzen:

```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
```

4. Erstellen Sie einen GraphQL-Client (hier Apollo Explorer):

- Endpoint: http://localhost:5000/graphql

5. Führen Sie Flask aus:
   
```
conda activate GEO413_GraphQL
set FLASK_APP=app.py
flask run
```

## Referenzen ##

## Referenzen

- [Apollo Explorer](https://www.apollographql.com/docs/graphos/explorer/): The GraphOS Studio Explorer (zuletzt aktualisiert am 14.09.2023).
- [Ariadne](https://ariadnegraphql.org/): Python GraphQL Schema-first (zuletzt aktualisiert am 11.09.2023).
- [Flask](https://flask.palletsprojects.com/en/2.3.x/): Welcome to Flask — Flask Documentation (2.3.x) (zuletzt aktualisiert am 21.06.2023).
- [GraphQL](https://graphql.org/): GraphQL | A query language for your API (zuletzt aktualisiert am 12.09.2023).
- Haque, S. (2023): [Using GraphQL with Python – A Complete Guide - Apollo GraphQL Blog](https://www.apollographql.com/blog/graphql/python/complete-api-guide/) (zuletzt aktualisiert am 14.09.2023).



