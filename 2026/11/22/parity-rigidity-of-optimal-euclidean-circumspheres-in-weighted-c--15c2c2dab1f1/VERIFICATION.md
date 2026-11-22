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

The proof relies on the central-symmetry ball certificate, exact signed-cycle quadratic identity, parity constraint on neighboring sign products, Cauchy--Schwarz equality classification, and the discrete Fourier eigenvalues of the cyclic shift quadratic form. All hold for the stated positive weights and every integer cycle size at least four.

A standalone standard-library script, `check_weighted_cycle.py`, checked the squared-radius formula and the farthest sign patterns in 3,360 finite integer-weight cases (all weights in {1,2,3} up to cycle size seven, and additional deterministic cases through size eleven). It also checked exact sample equalities and inequalities for fixed total weight. The observed output was `WEIGHTED_CYCLE_OUTER_EXACT_PASS 3360`.

Finite enumeration cannot establish the all-dimensional proof or rule out unknown earlier publications. The all-dimensional proof is given in `RESULT.md`. Independent audit is not performed.
