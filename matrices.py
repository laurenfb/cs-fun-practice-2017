matrix = [
    ['1', '1', '1', '1', '1',],
    ['1', '1', '1', '1', '1',],
    ['1', '1', '0', '0', '0',],
    ['1', '1', '0', '0', '0',],
    ['1', '1', '1', '1', '1',],
]

# top left = 2,2
# top right = 2,5
# bottom right = 3,5

def find_corners(matrix):
    top_left = find_top_left(matrix)
    top_right = find_top_right(matrix, top_left)
    bottom_right = get_bottom_right(matrix, top_left, top_right)
    return top_left, bottom_right

def find_top_left(matrix):
    for row_index, row in enumerate(matrix):
        for char_index, char in enumerate(row):
            if char == '0':
                return [row_index, char_index]

def find_top_right(matrix, top_left):
    top_right = [top_left[0], None]
    top_of_image = matrix[top_left[0]]
    index_in_question = top_left[1]
    while index_in_question < len(top_of_image): # check for off-by-one
        if top_of_image[index_in_question] == '1':
            top_right[1] = index_in_question -1
            return top_right
        index_in_question += 1
    top_right[1] = index_in_question
    return top_right

def get_bottom_right(matrix, top_left, top_right):
    bottom_right = [None, top_right[1]]
    for row_index, row in enumerate(matrix):
        if row_index >= top_left[0]:
            if row[top_left[1]] == '1':
                bottom_right[0] = row_index - 1
                return bottom_right


print(find_corners(matrix))
