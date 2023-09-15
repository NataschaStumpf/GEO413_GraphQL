# GEO413_GraphQL

Dieses Projekt basiert auf einem ursprünglichen Repository von [Shadid12](https://github.com/Shadid12) und wurde modifiziert.

Der ursprüngliche Code, auf dem dieses Projekt basiert, finden Sie [hier](Link zum ursprünglichen Repository](https://github.com/Shadid12/flask-graphql).

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

## Referenzen ##

Haque, S. (2023): Using GraphQL with Python – A Complete Guide - Apollo GraphQL Blog. Online verfügbar unter https://www.apollographql.com/blog/graphql/python/complete-api-guide/, zuletzt aktualisiert am 14.09.2023, zuletzt geprüft am 14.09.2023.
