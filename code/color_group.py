import numpy as np


def find_color_group(matrix):
    color_group = {}
    for i in range(0, len(matrix)):
        if not np.all(matrix[i, :] == -100):
            clr_gr = f'color_{i + 1}'
            to_vertex = matrix[i]
            color_group[clr_gr] = [i]
            while 0 in to_vertex:
                ind = np.where(to_vertex == 0)[0][0]
                if np.all(matrix[ind, :] == -100):
                    matrix[i][ind] = 1
                    continue
                to_vertex_2 = matrix[ind]
                new_to_vertex = np.array([1 if to_vertex[j] + to_vertex_2[j] >= 1 else 0 for j in range(len(matrix))])
                matrix[i] = new_to_vertex
                matrix[ind, :] = -100
                to_vertex = matrix[i]
                color_group[clr_gr].append(ind)
            matrix[i, :] = -100
        else:
            continue
    return color_group


mtr = [[1, 1, 1, 0, 0, 0, 1],
       [1, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 1, 1],
       [0, 1, 1, 1, 1, 0, 1],
       [0, 0, 0, 1, 1, 1, 0],
       [0, 0, 1, 0, 1, 1, 0],
       [1, 0, 1, 1, 0, 0, 1]]

mtr_2 = np.array([[1, 0, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 0, 0, 0],
                  [1, 0, 1, 1, 0, 1, 0, 0],
                  [1, 1, 0, 1, 0, 0, 1, 0],
                  [1, 1, 1, 0, 0, 0, 0, 1]])
# print(find_color_group(mtr_2))
