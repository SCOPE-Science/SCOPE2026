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

# Reproducible checks

Run `python3 verify.py` with Python 3. This uses only the standard library. The program generates every proper four-colouring for \(1\le t\le5\), reconstructs adjacency by checking single-vertex recolourings against all triangle edges, confirms the exact vertex and edge counts and hub-change count, and checks reverse adjacency. Breadth-first search from all representatives under an explicit subgroup of graph automorphisms tests connectivity and diameter; the symmetry reduction is valid because colour relabelling and petal permutation preserve the graph metric. A separate direct shortest-path test confirms the explicit extremal witnesses. The small local gateway cases are checked exhaustively for all 12 ordered distinct hub-colour pairs.

The recorded output shows the predicted diameters \(4,7,10,13,16\) at \(t=1,2,3,4,5\). The proof in `RESULT.md` establishes the theorem for every positive integer \(t\); finite tests cannot establish infinite behavior. Only self-review has been performed. The source files provide no external certification.
