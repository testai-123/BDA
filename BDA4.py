# Sample data: (Student Name, Marks)
data = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 67),
    ("David", 73),
    ("Eva", 58),
    ("Frank", 80)
]

# Map Function: emits (name, grade)
def mapper(record):
    name, marks = record
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return (name, grade)

# Reduce Function: just passes along the mapped result (no aggregation needed here)
def reducer(mapped_data):
    return dict(mapped_data)

# Run Map
mapped_results = list(map(mapper, data))

# Run Reduce
final_results = reducer(mapped_results)

# Output
for student, grade in final_results.items():
    print(f"{student}: {grade}")
