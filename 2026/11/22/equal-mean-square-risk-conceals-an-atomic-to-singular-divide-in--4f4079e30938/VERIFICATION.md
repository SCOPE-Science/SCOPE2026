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

# Reproducible verification

Run `python3 verify.py` using a Python 3 standard-library environment from the directory containing this document. The exact-rational checker enumerates all orders of three balanced labeled datasets on four or six points, checks the epoch-noise moments and geometric finite-epoch variance identities, and verifies the three-partition distribution and exact first-level IFS gaps. In the current source package it returned `VERIFY_OK 236`.

The checker verifies finite formulas on enumerated rational inputs. It does **not** establish the all-parameters moment theorem, infinite stationary series, uniqueness of stationary distributions, self-similar Hausdorff/measure dimensions, non-atomicity, singularity, or literature priority. Those assertions rest respectively on the symbolic exchangeability calculation, contractive affine recursion, IFS separation/entropy argument, and ternary digit-frequency argument given in `RESULT.md`.

The model is scalar, equal-curvature, and has independent epoch orders. Statements concerning singularity at the critical step exclude the exact-local-solve parameter; independent mathematical audit has not been performed.
