def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    triangle = []  # Initialize the triangle as an empty list

    for i in range(n):
        row = []  # Initialize the current row as an empty list

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # The first and last elements are always 1
            else:
                # Calculate the value based on the values in the previous row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)

        triangle.append(row)  # Add the current row to the triangle

    return triangle
