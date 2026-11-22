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

The exact independent executable check is `check.py`, run with Python 3 without optional dependencies. It enumerates every Dyck path for semilengths 1 through 7, computes both coordinate-wise empirical means and all ordered-pair Hamming distances, and asserts equality with the closed forms using rational arithmetic. Successful run: `CATALAN_VERTEX_INERTIA_EXACT_PASS n=1..7`.

The script separately displays three floating-point comparisons to the theorem's sharp large-size expansion; these are diagnostic only. Its finite checks do not constitute proof of the all-size identity or asymptotic formula. Those follow from the bivariate generating-function differentiation and the standard elliptic singularity expansion in `RESULT.md`. No external or independent audit has been performed.
