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

# Verification instructions and boundaries

Run `python3 check.py` using only the Python standard library. The checker constructs every size-zero-through-three matching of the complete three-by-\(n\) bipartite graph, encodes its edge incidence vector, then computes an exact integer Walsh--Hadamard transform. This transform is independent of the seven-moment formula that it checks against on every frequency through \(n=6\). The expected zero counts are \(3,0,72,0,2730,0\), with least positive magnitudes \(2,1,2,1,2,1\). For \(7\le n\le12\), it exhaustively processes all sign-column multisets up to column permutation, comparing independent three-row matching dynamic programming with the seven-moment identity. It checks the two sign-block identities and explicit base-witness extension through \(n=200\). The run finishes with `THREE_ROW_MATCHING_WALSH_EXACT_PASS`.

The proof of the statement for all lengths is mathematical, not inferred from finite enumeration. No external mathematical auditing or independent validation has been performed. The exact zero multiplicity at arbitrary odd lengths and the endpoint inverse norm are not asserted.
