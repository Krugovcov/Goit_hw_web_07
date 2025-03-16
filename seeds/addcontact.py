import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from conf.db import session
from conf.models import Student, Group, Subject, Teacher, Grade

fake = Faker("uk-UA")

def insert_groups():
    for _ in range(3):
        group = Group(name=fake.word())
        session.add(group)
    session.commit()

def insert_teachers():
    for _ in range(random.randint(3, 5)):
        teacher = Teacher(name=fake.name())
        session.add(teacher)
    session.commit()

def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(random.randint(5, 8)):
        subject = Subject(name=fake.word(), teacher=random.choice(teachers))
        session.add(subject)
    session.commit()

def insert_students():
    groups = session.query(Group).all()
    for _ in range(random.randint(30, 50)):
        student = Student(
            name=fake.name(),
            group=random.choice(groups)
        )
        session.add(student)
    session.commit()

def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(10, 20)):
                grade = Grade(student=student, subject=subject, grade=random.randint(60, 100))
                session.add(grade)
    session.commit()

def seed_database():
    try:
        insert_groups()
        insert_teachers()
        insert_subjects()
        insert_students()
        insert_grades()
        print("Database seeded successfully!")
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()