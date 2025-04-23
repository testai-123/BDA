from collections import defaultdict

# Sample data: (Student Name, Subject, Marks)
data = [
    ("Alice", "Math", 85),
    ("Alice", "English", 92),
    ("Bob", "Math", 76),
    ("Bob", "English", 88),
    ("Charlie", "Math", 67),
    ("Charlie", "Science", 59),
    ("David", "Math", 73),
    ("Eva", "English", 58),
    ("Frank", "Science", 80)
]

# Map Function: emits (student_name, marks)
def mapper(record):
    name, subject, marks = record
    return (name, marks)

# Reduce Function: calculates average and assigns grade
def reducer(mapped_data):
    scores = defaultdict(list)
    
    for student, marks in mapped_data:
        scores[student].append(marks)

    graded_students = {}
    for student, marks_list in scores.items():
        avg = sum(marks_list) / len(marks_list)
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'
        graded_students[student] = (round(avg, 2), grade)
    
    return graded_students

# Map Step
mapped_results = list(map(mapper, data))

# Reduce Step
final_results = reducer(mapped_results)

# Output
for student, (avg, grade) in final_results.items():
    print(f"{student} -> Average: {avg}, Grade: {grade}")
