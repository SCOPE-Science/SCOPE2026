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

# Computation and reproducibility

The graph consists of three row labels and six cyclic columns, encoded by bit index \(3c+r\). `verify_python.py` and `verify_cpp.cpp` are complete standalone sources using only a standard Python 3 environment or an ordinary C++17 compiler, respectively. Execute them using the commands recorded in `RESULT.md`.

Both programs check each of \(2^{18}\) labelled vertex subsets using exact open-neighborhood nonemptiness and distinctness of the signatures of vertices outside the selected set. Their independent graph implementations agree on all cardinality counts, budget component partitions for capacities six through eighteen, and the budget-nine all-optima shortest-path profile.

The reference stdout files `output_python.txt` and `output_cpp.txt` were produced by running the included source code. `witness_transition.txt` gives an additional explicit length-twelve path in hexadecimal mask notation. The witness demonstrates existence only: exhaustive checks underpin the complete graph and metric claims. The established scalar domination number is not asserted as new. Nothing here verifies an infinite family or constitutes an independent scholarly audit.
