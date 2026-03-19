from fastapi import FastAPI
app = FastAPI()
students = {
    1: {"name": "Alice", "age": 20, "grade": "A"},
    2: {"name": "Bob", "age": 22, "grade": "B"},
    3: {"name": "Charlie", "age": 21, "grade": "A-"},
}
@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = students.get(student_id)
    if student:
        return student
    return {"error": "Student not found"}

