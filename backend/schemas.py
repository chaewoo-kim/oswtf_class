from pydantic import BaseModel

class ClassInfoBase(BaseModel):
    class_id: str
    

class ClassInfoCreate(ClassInfoBase):
    lecture_id: str
    class_name: str

class ClassInfo(ClassInfoBase):
    lecture_id: str
    class_name: str

    class Config:
        orm_mode = True

class ClassInfoDelete(ClassInfoBase):
    pass


class StudentInfoBase(BaseModel):
    student_id: str
    class_id1: str
    class_id2: str
    class_id3: str
    class_id4: str
    class_id5: str
    class_id6: str
    class_id7: str
    class_id8: str

class StudentInfoAdd(StudentInfoBase):
    pass

class StudentInfo(StudentInfoBase):


    class Config:
        orm_mode = True