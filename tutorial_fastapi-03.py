from fastapi import FastAPI
app = FastAPI()
students={
    1: {"name": "John", "age": 20},
    2: {"name": "Jane", "age": 22},
    3: {"name": "Doe", "age": 21}
}
@app.get("/students/{student_id}")
def get_students(student_id: int):
    if student_id in students:
        return students[student_id]
    return {"error": "Student not found"}
#this shows not required query parameter
@app.get("/get-student")
def get_student(name : str = None):
    for student in students.values():
        if student["name"] == name:
            return student
    return {"error": "Student not found"}
