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

The analytic argument establishes the exact KKT sign/support cells and Jacobian, their strict local realizability, and the global maximum as a finite set of row sums. It then proves the exchange-based sorted-prefix support rule, the normalized weight envelope via a two-dimensional top-eigenvalue bound, and the equality and infimum classifications. This proof is not a machine-certified derivation.

Run `python3 verify.py` in the same directory with standard Python 3.10 or newer; the expected final line is `PASS: 464 finite exact-rational/analytic-envelope assertions`. The check covers 216 exact-rational weight/scale instances across dimensions 2 through 7 (all active masks), their exact finite KKT witnesses, and normalized envelope examples through dimension 9. Finite samples do not prove universal quantifiers. Numerical floating-point envelope comparisons use tolerance `1e-12` and are only auxiliary.

The references supply the underlying proximal construction and generalized Jacobian; they do not independently certify novelty or the newly asserted optimization. Independent audit has not been performed.
