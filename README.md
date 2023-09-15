# GEO413_GraphQL

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

3. 
   
```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
```
## Referenzen ##
