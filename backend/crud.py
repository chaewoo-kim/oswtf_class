from sqlalchemy.orm import Session
import models, schemas
from fastapi import Request


async def get_class_info(db: Session, class_id: str):
    return db.query(models.ClassInfo).filter(models.ClassInfo.class_id == class_id).first()

def create_class(db: Session, classInfo: schemas.ClassInfoCreate):
    db_class = models.ClassInfo(class_id=classInfo.class_id, lecture_id=classInfo.lecture_id, class_name=classInfo.class_name)
    
    db.add(db_class)
    db.commit()
    db.refresh(db_class)

    return db_class

async def student_add(db: Session, studentInfo: schemas.StudentInfoAdd):
    db_student = models.ClassStudent(student_id=studentInfo.student_id,
                                     class_id1=studentInfo.class_id1,
                                     class_id2=studentInfo.class_id2,
                                     class_id3=studentInfo.class_id3,
                                     class_id4=studentInfo.class_id4,
                                     class_id5=studentInfo.class_id5,
                                     class_id6=studentInfo.class_id6,
                                     class_id7=studentInfo.class_id7,
                                     class_id8=studentInfo.class_id8,)
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

# async def student_delete(request: Request, db: Session, targetInfo: schemas.ClassInfoDelete):
#     data = await request.json()

#     targetInfo.class_id = data['target_id']

#     db_target = db.query(models.ClassStudent).filter(models.ClassStudent.map((item, index) => (
#         if item == targetInfo.class_id:
            
#     )))