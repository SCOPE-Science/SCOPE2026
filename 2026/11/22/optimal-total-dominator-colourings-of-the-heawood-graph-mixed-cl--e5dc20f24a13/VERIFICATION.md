---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and evidence boundaries

The included `global_checker.cpp` enumerates all proper partitions of the fourteen labelled Fano-incidence vertices for each \(1\le k\le8\), tests total-dominator validity for each, constructs every one-vertex recolouring edge among optima, and computes all connected components and vertex degrees. It uses only C++17 standard libraries.

The included `side_checker.py` is independent of the C++ partition enumerator: it enumerates seven-element side partitions, matches nonincident colour blocks, verifies that every opposite-side vertex is witnessed by an unmerged block, reconstructs optima, and computes the recolouring graph. It also verifies the geometric correspondence between the \(21\) isolated states and the \(21\) incident Fano point–line flags. It uses only the Python 3 standard library.

Run from the directory containing both files:

```bash
g++ -std=c++17 -O2 -Wall -Wextra global_checker.cpp -o global_checker
./global_checker
python3 side_checker.py
```

Actual executions of these files yielded `PASS`. Both independently produced \(2751\) optimal partitions, \(2401\) with no mixed class, \(322\) with one, \(28\) with two, exactly \(11{,}662\) recolouring edges, \(21\) isolates, and components of sizes \(966\) and \(1764\). The shared degree histogram is \(0:21,\ 2:56,\ 5:224,\ 6:476,\ 7:168,\ 10:1806\). No external software, datasets, or private package references are required.

These are *complete finite* verification procedures, not probabilistic experiments or evidence of an infinite generalization. Unindexed scientific priority and independent scholarly audit have not been resolved.
