from resact1 import label_all, generate_graph, rotation_distance_matrix     
import tracemalloc
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def sizeof_object(obj):
    return sys.getsizeof(obj)

def benchmark_memory(n):
    result = {"n": n}

    tracemalloc.start()

    # 1. trees
    trees = label_all(n)
    snap1 = tracemalloc.take_snapshot()
    result["num_trees"] = len(trees)
    result["mem_trees_bytes"] = sum(stat.size for stat in snap1.statistics("filename"))

    # 2. graph
    G = generate_graph(trees)
    snap2 = tracemalloc.take_snapshot()
    result["mem_graph_bytes"] = sum(stat.size for stat in snap2.statistics("filename"))

    # 3. distance matrix
    dist, _ = rotation_distance_matrix(G)
    snap3 = tracemalloc.take_snapshot()
    result["mem_distance_matrix_bytes"] = sum(stat.size for stat in snap3.statistics("filename"))

    tracemalloc.stop()
    return result


def run_memory_benchmarks(n_values, csv_file="../Results/memory_benchmark.csv"):
    rows = []
    for n in n_values:
        print(f"Profiling memory for n={n}")
        rows.append(benchmark_memory(n))

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved memory results to {csv_file}")

    return rows

if __name__ == "__main__":
    rows = run_memory_benchmarks(range(3, 9))

    labels = ["Tree Generation", "Graph Construction", "Distance Matrix"]

    n_values = []
    gen_mem = []
    graph_mem = []
    matrix_mem = []
    total_mems = []
    for row in rows:
        n_values.append(int(row["n"]))
        gen_mem.append(float(row["mem_trees_bytes"]))
        graph_mem.append(float(row["mem_graph_bytes"]))
        matrix_mem.append(float(row["mem_distance_matrix_bytes"]))
        total_mem = (
            float(row["mem_trees_bytes"])
            + float(row["mem_graph_bytes"])
            + float(row["mem_distance_matrix_bytes"])
        )
        total_mems.append(float(total_mem))
    
plt.figure(figsize=(6, 4))
plt.plot(n_values, gen_mem, "-o", label="Tree Generation")
plt.plot(n_values, graph_mem, "-o", label="Graph Construction")
plt.plot(n_values, matrix_mem, "-o", label="Distance Matrix")
plt.plot(n_values, total_mems, "-o", label="Total Memory", linewidth=2, color="black")

plt.xlabel("n")
plt.ylabel("Memory (bytes)")
plt.title("Memory usage vs n")
plt.legend()
plt.tight_layout()
plt.savefig("../Results/memory_plot.png", dpi=300)
plt.show()