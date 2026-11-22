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

# Reproducibility

Run `python checker.py` with Python 3 standard library. The code computes rational cell transition matrices, verifies stochasticity, centrosymmetry, right and left affine-mode identities, signed second-eigenvector structure, and rational leading coefficients for degrees one through eight. It evaluates finite-step optimality from all grid-step candidates using bisection of a strictly monotone polynomial and exact polynomial antiderivatives represented numerically. Tests cover iterations 1, 2, 3, 5, 8, 13, and 42; the output reports a counted tally of 584 finite benchmark units. It reproduces \(A_1=1/2\), \(A_2=3/8\), \(A_3=17/42\), \(A_4=115/304\), and \(A_5=413/1060\).

These computations are not exhaustive over all degrees or iterations and do not substitute for the proof. The general statements follow from derivative-measure reduction, positivity and spectrum of the explicitly defined matrix and the Perron argument in RESULT.md. No external mathematical audit has been performed.
