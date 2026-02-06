from resact1 import label_all, generate_graph, rotation_distance_matrix
import csv

def diameter(n):
    result = {}
    result["n"] = n
    tree = label_all(n)
    G3 = generate_graph(tree)
    dist_matrix, _ = rotation_distance_matrix(G3)
    result["rotation_diameter"] = dist_matrix.max()
    return result

def run_time_benchmarks(n_values, csv_file="../Results/rotation_diameter.csv"):
    rows = []
    for n in n_values:
        rows.append(diameter(n))

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved time results to {csv_file}")

    return rows
if __name__ == "__main__":
    rows =run_time_benchmarks(range(3, 9))