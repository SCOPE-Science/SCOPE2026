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

# Verification record

Run `python3 verify.py` using Python 3 without external packages. The recorded replay succeeded: `PASS: 116 exact-rational and numerical checks`.

The checker independently enumerates conditional emission paths in two- and three-state hidden Markov examples and confirms their matrix-transform polynomial identity using exact fractions. It checks exact finite resolvent remainders, compares Poissonized random-walk first-passage survival with separately integrated killed-semigroup spectral formulas for five starting positions, and numerically checks the small-parameter Perron-eigenvalue slope in three heavy-tail examples.

The asymptotic Perron-projector bounds, Potter domination, and mean-finiteness equivalence are proved analytically in RESULT.md, not certified by finite sample arithmetic. The proof assumes a fixed primitive finite-state environment, positive finite conditional rates, and fixed starting site. The displayed sharp survival equivalent requires a regularly varying stationary Laplace deficit. Independent validation has not been performed.
