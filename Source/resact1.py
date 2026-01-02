import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generate_trees(n):
    if n==0:
        return [None]
        
    shapes = []

    for left_count in range(n):
        right_count = n - 1 - left_count

        left_shapes = generate_trees(left_count)
        right_shapes = generate_trees(right_count)

        for L in left_shapes:
            for R in right_shapes:
                shapes.append((L,R))

    return shapes

def label_inorder(shape, start):
    if shape is None:
        return None, start 
        
    left, right = shape
    left_label, next_label = label_inorder(left, start)

    root_label = next_label
    next_label += 1

    right_label, next_label = label_inorder(right, next_label)

    return (root_label, left_label, right_label), next_label

def label_all(n):
    shapes = generate_trees(n)
    Labelled = []

    for shape in shapes:
        Label, nxt = label_inorder(shape,1)
        Labelled.append(Label)

    return Labelled

def left_rotate(tree):
    if tree is None:
        raise ValueError("NO TREE")
    label, l, r = tree
    if r is None:
        raise ValueError("NO RIGHT")
    right, B, C = r
    return (right, (label, l, B), C)

def right_rotate(tree):
    if tree is None:
        raise ValueError("NO TREE")
    label, l, r = tree
    if l is None:
        raise ValueError("NO LEFT")
    left, B, C = l
    return (left, B, (label, C, r))

def single_rotation_anywhere(tree):
    if tree is None:
        return []
    
    neighbours = set()
    label, L, R = tree

    if R is not None:
        neighbours.add(left_rotate(tree))
    
    if L is not None:
        neighbours.add(right_rotate(tree))

    if L is not None:
        left_variants = single_rotation_anywhere(L)
        for newL in left_variants:
            neighbours.add((label, newL, R))
    
    if R is not None:
        right_variants = single_rotation_anywhere(R)
        for newR in right_variants:
            neighbours.add((label, L, newR))

    neighbours.discard(tree)
    return list(neighbours)

def generate_graph(tree):
    G = nx.Graph()
    for t in tree:
        G.add_node(t)

    for t in tree:
        neighbours = single_rotation_anywhere(t)
        for nb in neighbours:
            if nb in G:
                G.add_edge(t, nb)
    return G


def draw_rotation_graph(G, figsize=(7, 7)):
    nodes = list(G.nodes())
    n = len(nodes)
    plt.figure(figsize=figsize)

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=1600, node_color="lightblue")
    nx.draw_networkx_edges(G, pos)

    labels = {node: str(node) for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=7)
    plt.title(f"Rotation Graph with {n} nodes", fontsize=14)
    plt.axis("off")
    plt.savefig("../Results/rotation_graph.png", dpi=300)
    plt.show()


def rotation_distance(treeA, treeB, G):
    return nx.shortest_path_length(G, source=treeA, target=treeB)

def rotation_distance_matrix(G):
    nodes = list(G.nodes())
    n = len(nodes)
    dist = np.zeros((n, n), dtype=int)

    for i, t in enumerate(nodes):
        lengths = nx.single_source_shortest_path_length(G, t)
        for j, other in enumerate(nodes):
            dist[i][j] = lengths[other]
    return dist, nodes

