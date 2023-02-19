# Import the necessary libraries and modules from SQLAlchemy
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the database URI from a configuration file
from config import DATABASE_URI

# Create an engine object to connect to the database
engine = create_engine(DATABASE_URI)

# Define a session object using the engine object
Session = sessionmaker(bind=engine)
