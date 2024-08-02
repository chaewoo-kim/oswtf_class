from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os

from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine
from models import ClassInfo, ClassStudent
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 수동 실행
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "../frontend/build/static")), name="static")


# 접근 허락할 URL
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class AddStudent(BaseModel):
    student_id: str
    class_id1: str
    class_id2: str
    class_id3: str
    class_id4: str
    class_id5: str
    class_id6: str
    class_id7: str
    class_id8: str


class ClassInfo(BaseModel):
    class_id: str
    lecture_id: str
    class_name: str
    

@app.get("/")
async def home():
    path_to_index = os.path.join(os.getcwd(), "..", "frontend", "build", "index.html")

    return FileResponse(path_to_index)


@app.get("/init")
async def home(db: Session = Depends(get_db)):
    classLists = db.query(models.ClassInfo).all()
    
    return [{"class_id" : classList.class_id, "lecture_id" : classList.lecture_id, "class_name" : classList.class_name} for classList in classLists]


@app.post("/student_join/studentInfo", response_model=schemas.StudentInfo)
async def student_join(studentInfo: schemas.StudentInfoAdd, db: Session = Depends(get_db)):
    db_student = await crud.student_add(db=db, studentInfo=studentInfo)

    print(type(db_student))

    path_to_index = os.path.join(os.getcwd(), "..", "frontend", "build", "index.html")

    return FileResponse(path_to_index)


@app.post("/create_class/classInfo", response_model=schemas.ClassInfo)
async def create_class(classInfo: schemas.ClassInfoCreate, db: Session = Depends(get_db)):
    crud.create_class(db=db, classInfo=classInfo)
    
    path_to_index = os.path.join(os.getcwd(), "..", "frontend", "build", "index.html")

    return FileResponse(path_to_index)





@app.get("/manifest.json")
async def get_manifest():
    path_to_manifest = os.path.join(os.getcwd(), "..", "frontend", "build", "manifest.json")

    return FileResponse(path_to_manifest)

@app.get("/logo192.png")
async def get_logo192():
    return

@app.get("/logo512.png")
async def get_logo512():
    return

@app.get("/favicon.ico")
async def get_favicon():
    return

@app.get("/logo192.png")
async def get_logo():
    path_to_logo = os.path.join(os.getcwd(), "..", "frontend", "build", "logo192.png")
    return FileResponse(path_to_logo)