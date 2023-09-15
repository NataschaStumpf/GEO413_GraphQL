# GEO413_GraphQL

Dieses Projekt basiert auf einem ursprünglichen Repository von [Shadid12](https://github.com/Shadid12) und wurde modifiziert.

Der ursprüngliche Code, auf dem dieses Projekt basiert, finden Sie [hier](https://github.com/Shadid12/flask-graphql).

## Zielsetzung ##

- Einrichten eines Python-Webservers mit Flask
- Ariadne-Bibliothek zur Implementierung von GraphQL
- GraphQL-Schema zusammenstellen
- Abfragen und Mutationen gegen eine Python GraphQL API ausführen

## Anforderungen ##

- Python 3.9.13 
- Python-Pakete: `flask`, `flask-sqlalchemy`, `flask-cors`, `ariadne`

## Vorbereitung ##

1. Erstellen und aktivieren Sie die Conda-Umgebung

```
conda env create -f GEO413_GraphQL.yml
conda activate GEO413_GraphQL
```
2. Datenbank anlegen (hier PostgreSQL)

3. api/__init__.py anpassen: YourUserName, YourPassword, YourHostname, YourDatabaseName

```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
```

4. Graph erstellen (hier Apollo Explorer)

Endpoint: http://localhost:5000/graphql

5. Flask run
   
```
conda activate GEO413_GraphQL
cd \
set FLASK_APP=app.py
echo %FLASK_APP%
flask run
```

## Referenzen ##

Apollo Explorer (2023): The GraphOS Studio Explorer. Online verfügbar unter https://www.apollographql.com/docs/graphos/explorer/, zuletzt aktualisiert am 14.09.2023, zuletzt geprüft am 14.09.2023.

Ariadne (2023): Ariadne · Python GraphQL Schema-first. Online verfügbar unter https://ariadnegraphql.org/, zuletzt aktualisiert am 11.09.2023, zuletzt geprüft am 14.09.2023.
Flask (2023): Welcome to Flask — Flask Documentation (2.3.x). Online verfügbar unter https://flask.palletsprojects.com/en/2.3.x/, zuletzt aktualisiert am 21.06.2023, zuletzt geprüft am 14.09.2023.

GraphQL (2023): GraphQL | A query language for your API. Online verfügbar unter https://graphql.org/, zuletzt aktualisiert am 12.09.2023, zuletzt geprüft am 12.09.2023.

Haque, S. (2023): Using GraphQL with Python – A Complete Guide - Apollo GraphQL Blog. Online verfügbar unter https://www.apollographql.com/blog/graphql/python/complete-api-guide/, zuletzt aktualisiert am 14.09.2023, zuletzt geprüft am 14.09.2023.
![image](https://github.com/NataschaStumpf/GEO413_GraphQL/assets/73939232/07a4d4bb-41a1-42ac-b1d5-a850aadc161d)

