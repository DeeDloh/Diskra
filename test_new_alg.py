matrix = [[1, 1, 1, 0, 0, 0, 1],
          [1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 1, 0],
          [0, 0, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 0, 0, 1]]

color_group = {}

for i in range(0, len(matrix)):
    if matrix[i] is not None:
        clr_gr = f'color_{i}'
        to_vertex = matrix[i]
        color_group[clr_gr] = [i]
        while 0 in to_vertex:
            ind = to_vertex.index(0)
            if matrix[ind] is None:
                matrix[i][ind] = 1
                continue
            to_vertex_2 = matrix[ind]
            new_to_vertex = [1 if (k := to_vertex[j] + to_vertex_2[j]) >= 1 else 0 for j in range(len(matrix))]
            matrix[i] = new_to_vertex
            matrix[ind] = None
            to_vertex = matrix[i]
            color_group[clr_gr].append(ind)
        matrix[i] = None
    else:
        continue

print(color_group)