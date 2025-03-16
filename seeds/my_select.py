from sqlalchemy import func

from conf.db import session
from conf.models import Student, Grade, Subject, Teacher, Group


def select_01():
    students_with_avg_grade = (
        session.query(
            Student.id,
            Student.name,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )
    return students_with_avg_grade

def select_02():
    student_with_max_grade = (
        session.query(
            Student.name.label("student_name"),
            Subject.name.label("subject_name"),
            Grade.grade.label("max_grade")
        )
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Student, Student.id == Grade.student_id)
        .filter(Grade.subject_id == 1)
        .order_by(Grade.grade.desc())
    )


    return student_with_max_grade.first()
def select_03():
    avg_grade = (
            session.query(func.avg(Grade.grade).label("avg_grade"))
            .join(Student, Student.id == Grade.student_id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Grade.subject_id == 1)
            .filter(Student.group_id == 1)
            .scalar()
        )
    return f"Average grade for group 1 in subject 1 is: {round(avg_grade)}"

def select_04():
    avg_grade = (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .scalar()
    )
    return f"Average grade for all students in all subjects is: {round(avg_grade)}"

def select_05():
    courses = (
        session.query(Subject.name)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.id == 3)
        .all()
    )
    return courses

def select_06():
    return session.query(Group).filter(Group.id == 2).first()

def select_07():
    grades = (
        session.query(Student.name, Grade.grade)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Student.group_id == 2)
        .filter(Grade.subject_id == 1)
        .all()
    )
    return grades

def select_08():
    avg_grade = (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.id == 1)
        .scalar()
    )
    return avg_grade

def select_09():
    courses = (
        session.query(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == 2)
        .all()
    )

def select_10():
    courses = (
        session.query(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .join(Student, Student.id == Grade.student_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Student.id == 4)
        .filter(Teacher.id == 4)
        .all()
    )
    return courses

if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03())
    print(select_04())
    print(select_05())
    print(select_06())
    print(select_07())
    print(select_08())
    print(select_09())
    print(select_10())