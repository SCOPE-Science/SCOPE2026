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

# Verification notes

The complete proof of the essential endpoints is the positive-probability constant-symbol block argument in `RESULT.md`; it is not inferred from numerical endpoint sampling. The pullback exists because all affine contraction factors are strictly between zero and one. The exact moment recurrence uses independence between the present iid symbol and the past-measurable stationary coordinate.

Run `python check.py` with standard-library Python 3. It enumerates every type history of lengths one through eight at four rational perturbation strengths, verifying 2,040 finite states and 64 exact mean/variance equalities, and it checks endpoint contraction estimates. Exhaustive finite-word checks do not establish the infinite product-space result; the analytical argument does.

No independent mathematical audit or external validation has been performed. The result does not establish any claim for all random interval-map realizations or for general correlated environmental processes.
