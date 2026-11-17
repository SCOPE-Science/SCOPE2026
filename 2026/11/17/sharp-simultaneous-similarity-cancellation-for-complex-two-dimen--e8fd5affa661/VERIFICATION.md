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

The proof in `RESULT.md` establishes the assertions for all finite multiplicities and arbitrary index sets without numerical extrapolation. Critical checks are the cyclic centralizer identity, the inverse-block existence argument, the exact Kronecker condition-number product, and the two-dimensional nilpotent/involution canonical intertwiners.

Run `python verify.py` using Python 3 and NumPy to execute 79 finite exact-rational and numerical illustrations. The script is not an exhaustive check and does not replace the mathematical proof. No independent external audit has been performed.
