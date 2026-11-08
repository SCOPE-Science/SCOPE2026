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

# Verification

`CHECKER.py` needs only Python 3's standard library. Run `python3 CHECKER.py` from this package directory. The script derives the complete allowed triple set directly from the two-nonzero condition, reconstructs the graph, checks indegree/outdegree balance, and computes exact integer Laplacian minors using Bareiss elimination for alphabet sizes \(q=2,3,4,5,6\). It compares these with the all-alphabet arborescence formula and the BEST factorial count.

Independently, dynamic programming over the used-edge bitmask counts every Euler circuit with distinguished edge `(1,1,1)` first for \(q=2,3\). This method does not use a spanning-tree theorem, determinant, or the closed formula. It produces \(1\) and \(1728\) respectively. The proof of the entire infinite family is given in RESULT.md by an invariant-subspace factorization of the Laplacian. Finite replay is corroboration, not a proof for larger alphabets.

All computations are over exact integers, without floating point or heuristic search. The public certificate does not purport to have been independently audited.
