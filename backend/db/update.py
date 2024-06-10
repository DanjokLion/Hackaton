from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

engine = create_engine('')
Session = sessionmaker(bind=engine)
session = Session()

def update_data():
    while True:
        new_data = fetch_new_data()
        
        update_database(new_data)
        
        update_dashboard()
        
        time.sleep(28_800)  # обновление раз в 8 часов

def fetch_new_data():
    pass

def update_database(new_data):
    pass

def update_dashboard():
    pass

update_data()
