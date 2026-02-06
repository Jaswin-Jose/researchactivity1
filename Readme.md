# Research Activity 1
---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/Jaswin-Jose/researchactivity1.git
cd researchactivity1
```
2. Create Virtual Environment
```bash
python -m venv venv
```
Activate environment:

Linux / macOs
```bash
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
---
## Usage

### Generate Rotation Graph and Compute Distances

To generate a rotation graph for n=3 nodes:

```bash
cd Source
python Outputs.py
```

This will:
- Generate all binary trees with 3 nodes
- Create the rotation graph and distance matrix
- Calculate and print the rotation diameter
- Save a visualization to `Results/rotation_graph.png`

### Time Benchmarking

To benchmark runtime performance for different tree sizes (n=3 to 8):

```bash
cd Source
python time.py
```

Outputs:
- `Results/time_benchmark.csv` - Raw timing data
- `Results/runtime_plot.png` - Performance visualization

### Memory Benchmarking

To benchmark memory usage for different tree sizes:

```bash
cd Source
python memory.py
```

Outputs:
- `Results/memory_benchmark.csv` - Memory usage data
- `Results/memory_plot.png` - Memory consumption visualization

### Rotation Diameter Analysis

To compute rotation diameters for trees of different sizes:

```bash
cd Source
python Rotationdiameter.py
```

Output:
- `Results/rotation_diameter.csv` - Diameter values for each n
