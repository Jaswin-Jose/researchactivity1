from resact1 import label_all, generate_graph, rotation_distance_matrix
import csv
import time
import matplotlib.pyplot as plt

def benchmarking(n):
    result = {}
    result["n"] = n

    t0 = time.perf_counter()
    trees = label_all(n)
    t1 = time.perf_counter()
    result["num_trees"] = len(trees)
    result["time_generating_all_trees"] = t1-t0

    t2 = time.perf_counter()
    G = generate_graph(trees)
    t3 = time.perf_counter()
    result["time_build_graph"] = t3-t2

    t4 = time.perf_counter()
    _ = rotation_distance_matrix(G)
    t5 = time.perf_counter()
    result["time_matrix"] = t5-t4

    return result


def run_time_benchmarks(n_values, csv_file="../Results/time_benchmark.csv"):
    rows = []
    for n in n_values:
        print(f"Timing n={n}")
        rows.append(benchmarking(n))

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved time results to {csv_file}")

    return rows
if __name__ == "__main__":
    rows =run_time_benchmarks(range(3, 9))

    labels = ["Tree Generation", "Graph Construction", "Distance Matrix"]

    n_values = []
    gen_times = []
    graph_times = []
    matrix_times = []
    total_times = []
    for row in rows:
        n_values.append(int(row["n"]))
        gen_times.append(float(row["time_generating_all_trees"]))
        graph_times.append(float(row["time_build_graph"]))
        matrix_times.append(float(row["time_matrix"]))
        total_time = (
            float(row["time_generating_all_trees"])
            + float(row["time_build_graph"])
            + float(row["time_matrix"])
        )
        total_times.append(float(total_time))
    
plt.figure(figsize=(6, 4))
plt.plot(n_values, gen_times, "-o", label="Tree Generation")
plt.plot(n_values, graph_times, "-o", label="Graph Construction")
plt.plot(n_values, matrix_times, "-o", label="Distance Matrix")
plt.plot(n_values, total_times, "-o", label="Total Time", linewidth=2, color="black")

plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Runtime vs n")
plt.legend()
plt.tight_layout()
plt.savefig("../Results/runtime_plot.png", dpi=300)
plt.show()