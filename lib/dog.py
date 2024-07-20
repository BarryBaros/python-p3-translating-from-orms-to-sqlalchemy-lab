#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

if __name__ == '__main__':
    # Create an SQLite database and the Dog table
    engine = create_engine('sqlite:///dogs.db')
    create_table(Base, engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example usage
    fido = Dog(name="Fido", breed="Labrador")
    save(session, fido)

    # Retrieve all dogs
    all_dogs = get_all(session)
    print("All dogs:", all_dogs)

    # Find dog by name
    dog_by_name = find_by_name(session, "Fido")
    print("Dog by name:", dog_by_name)

    # Find dog by ID
    dog_by_id = find_by_id(session, fido.id)
    print("Dog by ID:", dog_by_id)

    # Find dog by name and breed
    dog_by_name_and_breed = find_by_name_and_breed(session, "Fido", "Labrador")
    print("Dog by name and breed:", dog_by_name_and_breed)

    # Update dog's breed
    update_breed(session, dog_by_id, "Golden Retriever")
    updated_dog = find_by_id(session, fido.id)
    print("Updated dog:", updated_dog)
