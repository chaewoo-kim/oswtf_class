from sqlalchemy import String, Column
from database import Base

class ClassInfo(Base):
    __tablename__ = "class"

    class_id = Column(String, primary_key=True)
    lecture_id = Column(String)
    class_name = Column(String)

class ClassStudent(Base):
    __tablename__ = "class_std"

    student_id = Column(String, primary_key=True)
    class_id1 = Column(String)
    class_id2 = Column(String)
    class_id3 = Column(String)
    class_id4 = Column(String)
    class_id5 = Column(String)
    class_id6 = Column(String)
    class_id7 = Column(String)
    class_id8 = Column(String)
