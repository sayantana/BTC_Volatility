# BTC_Volatility

This is a project which calculate the daily Bitcoin price volatility and store into postgres database.

We have used BRIN indexes for the tables as mostly it will be querying within range.

To run this project.

1. checkout the project
2. ```cd BTC_Volatility```
3. docker-compose up --build
4. Once it finishes and prints the following Extract Transform and Load is completed
5. In pgadmin or similar tool access the databases.
    - db user name: postgres
    - db pass: postgres
    - db name: database
    - host: 0.0.0.0
    - port: 5432
