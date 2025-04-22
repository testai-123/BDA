
#Map function
def mapper(A, B):
    mapped_values = []
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    for i in range(rows_A):  
        for k in range(cols_A):  
            for j in range(cols_B): 
                mapped_values.append(((i, j), A[i][k] * B[k][j]))

    return mapped_values

# Shuffle
def shuffle(mapped_values):
    shuffled_data = {}

    for key, value in mapped_values:
        if key in shuffled_data:
            shuffled_data[key].append(value)
        else:
            shuffled_data[key] = [value]

    return shuffled_data

# Reduce Function
def reducer(shuffled_data):
    result_matrix = {}
    
    for key, values in shuffled_data.items():
        result_matrix[key] = sum(values)  # Summing up all values at (i, j) position

    return result_matrix



if __name__=='__main__':
    # crete 2 matrices
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    # Applying MapReduce
    mapped_results = mapper(A, B)
    shuffled_results = shuffle(mapped_results)
    final_result = reducer(shuffled_results)

    # Converting dictionary output to matrix format
    rows_A, cols_B = len(A), len(B[0])
    result_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for (i, j), value in final_result.items():
        result_matrix[i][j] = value

    # Displaying the result
    for row in result_matrix:
        print(row)
