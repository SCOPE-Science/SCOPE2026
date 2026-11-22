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

The exact-arithmetic standalone `verify_picard.py` reconstructs 48 explicit projective lines, their intersection form, four Galois-character projectors and four subgroup orbit-sum forms. Rational Gaussian elimination (standard-library `fractions.Fraction`) yields the full rank 20, character dimensions 9, 7, 2, 2, and arithmetic Picard ranks 9, 16, 11, 11, 20. The nonidentity Galois trace is 2, 12, 2 at exponents 3, 5, 7.

A separate symbolic determinant calculation in the cyclotomic ring with \(\zeta_8^4=-1\) verified the 1128 pairwise incidence decisions used by the standalone combinatorial verifier. Both scripts use exact algebra rather than finite-field sampling or probabilistic rank approximations. Only the standalone verifier is included; its original source and method suffice to reproduce all accepted numerical evidence.

The proof also depends on standard intersection theory for distinct lines on smooth quartics, the K3 Picard upper bound 20 in characteristic zero, and Galois descent up to torsion. These are not numerical assertions. No independent mathematical audit has been performed.
