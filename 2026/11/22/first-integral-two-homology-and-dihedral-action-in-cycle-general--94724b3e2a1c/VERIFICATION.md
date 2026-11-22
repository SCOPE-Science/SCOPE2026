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
Run `python3 verify.py` and `python3 verify_equiv.py` in this directory. They use standard-library Python only, and both returned PASS for the exact source files. The first enumerates every labelled triple and four-set of the cycle orders in scope, reconstructs all signed boundary matrices, and performs integer unimodular unit-pivot reductions with zero residual blocks. The second obtains the integral two-cycle basis for the nine-cycle from exact rational row reduction, verifies integer coefficients, recomputes rotation/reflection matrices and the Lefschetz trace, and checks the finite-group invariant dimensions.

## What the checks establish
They prove the finite homology table, lack of integral torsion, primitive boundary images, group-action matrices and stated rational quotient homology. The finite computations are exhaustive for orders three through twelve, but do not prove any all-order formula or homotopy-equivalence assertion. Independent external validation was not performed.
