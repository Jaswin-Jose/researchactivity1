from resact1 import label_all, generate_graph, rotation_distance_matrix, draw_rotation_graph

tree = label_all(3)
G3 = generate_graph(tree)
dist_matrix, nodes = rotation_distance_matrix(G3)

print("Distance matrix:")
print(dist_matrix)

draw_rotation_graph(G3)
