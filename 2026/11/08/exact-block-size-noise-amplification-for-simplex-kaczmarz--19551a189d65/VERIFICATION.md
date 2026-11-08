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

The theorem was checked by reconstructing the Gram eigenvalues, the subset Gram inverse, the shift norm, the permutation-averaged projectors and the recurrences. The calculation is analytic and covers all integers \(d\ge2\), every \(1\le k\le d\), all fixed responses and all deterministic starts. SymPy-based exact rational subset enumeration in `verify_simplex.py` passed for \(d=2,\ldots,7\) at every block size. These finite checks cannot establish the general theorem without its written proof. The all-subset model differs from sampling blocks of a fixed paving; and the reported noise floor does not apply to extended residual-correction methods. No independent audit was performed.
