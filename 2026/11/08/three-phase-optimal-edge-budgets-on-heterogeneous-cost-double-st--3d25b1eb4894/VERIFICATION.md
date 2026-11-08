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

The derivation constructs a Euclidean supporting configuration in each of three price regimes, proves the associated Rayleigh upper bound, and matches it with explicit positive conductances and a first positive weighted-path quotient eigenvector. Uniqueness is established through equality of the Rayleigh certificate and leaf-wise eigenvector equations. The proof covers all integers \(a,b\ge2\) and all positive real prices and budgets.

The included `verify.py` was run with Python 3 and SymPy. It passed 368 exact-rational test cases covering each regime, both boundary cases, asymmetric leaf counts up to 100, exact supporting variances, budgets, eigenvector equations, all principal minors of a four-by-four quotient spectral positivity matrix, and pendant eigenvalue inequalities. This finite verification supplements but does not prove the continuous-parameter statement. Independent review has not been performed.
