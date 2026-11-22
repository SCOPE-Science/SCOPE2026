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

# Reproducing the exact finite census

All paths below are relative to the directory holding this document. The graph is defined by `adjacency.txt`, whose line \(i+1\) lists the five neighbors of vertex \(i\). Every input is a twelve-digit ternary word, encoded as \(\sum_{i=0}^{11}3^i x_i\).

Run the following commands in that directory:

```sh
c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
./verify_direct > direct_replay.txt
cmp direct_replay.txt direct_output.txt
python3 verify_vector.py > vector_replay.txt
cmp vector_replay.txt vector_output.txt
python3 verify_symmetry.py > symmetry_replay.txt
cmp symmetry_replay.txt symmetry_output.txt
```

The vectorized independent checker requires NumPy and Python 3; the direct C++ verifier and symmetry verifier require only their respective language standard libraries. The C++ program writes `orbit_roots.csv`; the Python vector checker writes `vector_roots.csv` and independently compares every canonical root and individual basin to the direct list. The symmetry checker verifies every listed adjacency-preserving permutation and their group closure, then rewrites `orbit_classes.csv`. The displayed reference outputs were obtained by actually executing the programs in the package.

The direct program exhausts all \(531441\) states through a finite functional graph, while the vector verifier checks \(F^{11}=F^8\) for each state through direct iterate arrays, and explicitly confirms failure of \(F^{10}=F^7\). The local three-phase activation condition is independently enumerated; all \(600\) recurring nonconstant states satisfy full phase rotation, and no omitted periodic cases remain because the global iterate identity has been checked on the full state space.

The one-step transition code is given in full. The counting result does not extrapolate from simulation samples to an infinite family. The source comparison addresses available indexed and full-text works, but absence of a matching result in searches does not constitute an absolute novelty proof.
