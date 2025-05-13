
def is_valid_matrix(matrix):
    n = len(matrix)
    required = set(range(1, n + 1))

    # Check each row
    for row in matrix:
        if set(row) != required:
            return False

    # Check each column
    for col in range(n):
        column_values = [matrix[row][col] for row in range(n)]
        if set(column_values) != required:
            return False

    return True
matrix = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
print(is_valid_matrix(matrix)) 