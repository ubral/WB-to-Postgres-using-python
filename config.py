# Import the psycopg2 library, which is used to connect to PostgreSQL databases
import psycopg2

# Define the database URI as a string
DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost:5432/DataAnalysis'

#In the database URI, postgresql+psycopg2 specifies that the database is using the PostgreSQL driver with psycopg2 as the Python adapter.
# Postgres is the username for accessing the database, password is the password, localhost is the hostname,
# 5432 is the port number for the database server, and DataAnalysis is the name of the database being accessed.