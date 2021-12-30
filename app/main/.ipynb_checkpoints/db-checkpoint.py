from sqlalchemy import create_engine

def initialize():
    engine = create_engine('postgresql://postgres:postgres@db:5432/database')
    return engine