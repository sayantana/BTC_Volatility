FROM postgres:latest
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=database
COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql
