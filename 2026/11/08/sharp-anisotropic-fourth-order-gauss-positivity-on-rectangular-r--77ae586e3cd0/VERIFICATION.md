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

# Reproducibility and limits

The proof is analytic. Python 3 code in `verify.py` requires only the standard library and may be run with `python verify.py`. It computes the weighted Kronecker-sum Laplacian, constructs the degree-two Padé numerator and denominator as exact rational matrices, inverts the denominator by exact Gauss–Jordan elimination, and compares all computed entries against the four-eigenspace projector formula. It also tests the quartic coefficient identities for exact rational parameters and verifies representative positive and eventual-negative configurations, including \(K_2\square K_5\). The package replay output was `VERIFY_OK 2135`.

The all-real-parameter assertion does not follow from these finite tests: it follows from the symbolic identities, positivity of each coefficient in the feasible cases, and the leading-term sign obstruction outside the feasible interval. The classification is of the **completed endpoint**, not of intermediate stage states. No assertion is made about arbitrary individual edge weights or about the number of finite positivity windows in excluded parameter regions.

This document records checks on the mathematical derivation and its reproducibility only. No independent mathematical audit has been performed.
