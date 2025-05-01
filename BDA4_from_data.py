import pandas as pd 

df = pd.read_csv('grade.csv')


def mapper(row):
    return (row['Name'], row['Marks'])

def reducer(mapped_data):

    scores = {}

    for student, marks in mapped_data:
        if student in scores:
            scores[student].append(marks)

        else:
            scores[student] = [marks]

    graded_students = {}

    for student, marks_list in scores.items():

        avg = sum(marks_list)/len(marks_list)

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
        
        graded_students[student] = (round(avg,2), grade)

    return graded_students 


mapped_results = list(df.apply(mapper, axis=1))

fin = reducer(mapped_results)

for student, (avg,grade) in fin.items():
    print(f'{student} -> Average: {avg}, Grade: {grade}')
