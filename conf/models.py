from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = 'students'  # Додано __tablename__

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))  # Виправлено назву таблиці
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subjects = relationship("Subject", back_populates="teacher")  # Виправлено ім'я (було subject)

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="subjects")  # Виправлено ім'я
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'  # Додано __tablename__

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    grade = Column(Integer, nullable=False)
    date_received = Column(DateTime, default=datetime.utcnow)  # Виправлено виклик функції

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
