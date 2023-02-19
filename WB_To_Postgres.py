# Import necessary libraries and modules
import wbgapi as wb
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

# Import the 'engine' and 'Session' objects from the 'crud' module
from crud import engine, Session

# Start a new session
s = Session()

# Declare a base class for our database schema
Base = declarative_base()

# Retrieve a list of all World Bank data series containing the word 'military'
df = wb.series.list(q='military')

# Iterate over each data series and download its data
for id in df:
    # Extract the ID and title of the data series
    id_title = id['id']
    series_name = id['value']

    # Print a message to indicate which data series is being downloaded
    print('Downloading data for ', series_name)

    # Download the data for the current series and reformat it as a 'melted' dataframe
    df = wb.data.DataFrame(id_title, mrv=50, numericTimeKeys=True)
    df = df.rename_axis('Country').reset_index()
    df = pd.melt(df, id_vars=['Country', ], var_name='Year', value_name=series_name)

    # Define a new class for our database table with the same name as the data series. Source tutorial had name of the class Book because it was for a library. Feel free to use whatever name you want.
    class Book(Base):
        __tablename__ = series_name
        id = Column(Integer, primary_key=True)
        Country = Column(String)
        Year = Column(Integer)
        Value = Column(Float)

    # Print a message to indicate that the table for the current series is being created
    print('Loading table', series_name)

    # Create the table in the database
    Base.metadata.create_all(engine)

    # Insert each row of data from the dataframe into the database
    for index in df.index:
        Cntry = (df['Country'][index])
        Values = (df[series_name][index])
        yr =  (df['Year'][index])
        book = Book(
            Country=Cntry,
            Value=Values,
            Year=yr,
        )
        s.add(book)
        s.commit()
