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

The all-integer homotopy claim rests on the written face-poset fiber decomposition, the classification of cyclic binary words with no isolated allowed subdivision vertex, and the acyclic patchwork theorem. The fiber matching leaves exactly one \((n-1)\)-cell for odd \(n\) and three for even \(n\), plus one ordinary critical zero-cell; this excludes any unproved inference from finitely many computed examples.

For finite reproducibility, run `python3 gear_verifier.py` with Python 3.10 or later and compare its standard output with `expected_output.json` as bytes. The program reconstructs the graph, enumerates all faces, checks pair validity and involutivity, checks every directed cover relation for acyclicity for \(3\le n\le9\), and independently reduces mod-two simplicial boundaries for \(3\le n\le7\). Exact counts include 59,699 augmented faces and 407,762 oriented Hasse incidences at \(n=9\). The finite check is a corroborating test, not an infinite proof. No external validation or independent audit is claimed.
