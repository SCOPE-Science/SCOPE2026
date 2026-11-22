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

Run `python verify.py` with Python 3, NumPy and SciPy. The extracted file contains every required mathematical input and no external data dependencies.

Observed on the packaged source before embedding: `VERIFY_OK 2596` (2,596 assertions). Exact `fractions.Fraction` tests cover the dimension-37 witness, sampled row sums and its Ritz quotient; independent numerical QR pivot checks cover nine sizes; extensive direct vector-product tests compare the sampled quotient to the closed form, sharp endpoints and strict sign threshold. An analytic proof covers all parameters and sizes; the finite checks are not exhaustive verification.

The main limitation is that no matrix family outside the specified rank-one construction is covered. Independent mathematical validation has not been performed.
