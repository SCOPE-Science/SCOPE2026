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

# Mathematical verification

The complete proof is in `RESULT.md`. The standalone standard-library `verify.py` checks all finite contexts needed for the obstruction and inverse lemmas; computes the six-by-six bivariate determinant by exact polynomial permutation expansion; and independently reconstructs every cyclic output and the explicit two-step antecedent for rings of lengths 1 through 13. Fixed-density transfer and double-binomial coefficient computations agree through length 15, and exact recurrences agree through length 23. The local truth-table lemmas are exhaustive over their precisely bounded input windows. The all-length conclusion follows from the local proof and the exact transfer identity, not from finite experimental agreement. The eigenvalue ordering follows from the factored exact characteristic polynomial and isolated roots.

To reproduce, execute `python3 verify.py` in the directory containing the files. Expected success marker: `VERIFY_OK`. The program is complete, standalone, deterministic, and uses only Python's standard library. Its checks are same-study verification, not an independent audit or certification.
