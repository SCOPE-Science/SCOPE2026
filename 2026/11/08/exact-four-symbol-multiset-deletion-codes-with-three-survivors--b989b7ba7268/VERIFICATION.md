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

# Reproducing the exact computations

Save `checker.py` alongside this file and run `python3 checker.py` using a Python interpreter with integer `bit_count()` support (Python 3.10 or later). No third-party modules or external input are required.

Expected finite impossibility results: at \(n=4,5,6,7,8\), the targets \(12,7,6,6,6\) are absent from the pairwise-compatible graphs, with exhaustive recursion node counts \(7056,13027,14895,16825,19450\). The checker prints all five and finally reports `PASS: all finite exhaustive upper bounds and witnesses verified`.

The graph's vertex set is the complete set of four-compositions of \(n\), and two vertices are joined iff their coordinatewise minimum sum is at most two. Inductively, its recursive search enumerates every possible increasing-index clique, with only the obvious eligible-candidate cardinality bound as pruning. The script separately constructs each offered lower-bound code and compares its three-survivor descendant sets directly; this guards the equivalence used in graph generation. The unbounded case \(n\geq9\) is proved mathematically by assigning each codeword a nonempty set of coordinates of size at least three; no finite search is used for that argument.

These are reproducible finite calculations and a mathematical proof; they do not constitute independent external validation or an assessment of definitive publication priority.
