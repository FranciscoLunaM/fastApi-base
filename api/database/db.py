import os
from sqlmodel import create_engine,Session
from dotenv import load_dotenv
load_dotenv('../.env')

username=os.getenv("DATABASE_USERNAME")
password=os.getenv("DATABASE_PASSWORD")
host=os.getenv("DATABASE_HOST")
port=os.getenv("DATABASE_PORT")
database=os.getenv("DATABASE_NAME")

#engine=create_engine("postgresql://username:password@ip:port/dbname", echo=True, connect_args=connect_args)



engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}", echo=True)
print("Database connection established.")
def get_session():
    with Session(engine) as session:
        yield session