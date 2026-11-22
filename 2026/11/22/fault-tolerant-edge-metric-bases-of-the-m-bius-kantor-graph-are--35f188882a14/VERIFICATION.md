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

# Reproducibility and verification

The standalone executable sources `check_py.py` and `check_cpp.cpp` in this package construct the Möbius–Kantor graph by the given complete edge list. They do not read external files or rely on network access.

Run `python3 check_py.py` and, independently, `g++ -std=c++17 -O2 check_cpp.cpp -o check_cpp && ./check_cpp`.

Both programs must report \(24\) graph edges, \(368\) ordinary edge-resolving four-sets, zero fault-tolerant four-sets, \(16\) fault-tolerant five-sets, and equality between these five-sets and the distinct distance-three spheres. The Python program also tests the ordinary three-set boundary and directly tests every one-vertex deletion from each candidate. C++ builds witness masks for all \(\binom{24}{2}=276\) edge pairs and enforces two-witness coverage. Both check \(64\), \(8\), \(48\) unordered optimal-pair intersections of sizes zero, two, three, respectively, and reconfiguration edge counts \((0,48,56,56,120)\) for replacement limits \(1\) through \(5\). Python independently computes connected-component sizes at each limit.

The exhaustive search is finite: \(\binom{16}{4}=1820\) four-subsets and \(\binom{16}{5}=4368\) five-subsets. The no-four-set result extends to all smaller fault-tolerant candidates by monotonicity of two-witness coverage. For ordinary edge metric dimension, the Python checker excludes all \(\binom{16}{3}=560\) triples, and a valid four-set exists. None of these experiments claims an infinite-family theorem.

Results were checked by reading and executing the actual delivered source texts after JSONL extraction; tool environment and compiler versions are not logically part of the proof.
