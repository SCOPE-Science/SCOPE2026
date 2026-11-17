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
# Verification of the finite-round threshold theorem

Run `python check.py` in a Python 3 environment with `sympy` and `mpmath` installed. The program contains the full tested algebra and deterministic recurrences and requires no external files. Its successful output begins:

```
VERIFY_OK exact_center_taylor=2 exact_normal_form_identity=1 unique_transition_examples=4 critical_decay_examples=2 bifurcating_endemic_branches=2
```

The exact symbolic checks establish the first two Taylor coefficients of the competing-risks incidence map and the algebraic equality between the direct center-manifold coefficient and \(v^2D(p)/(p^2u^2)\). The finite numeric checks verify the sign change for sampled parameter pairs, two critical trajectories of 180,000 rounds, and two small endemic branches from the full three-dimensional fixed-point equations. Numerically observed \(n a_n\) values were approximately \(0.441367\) and \(0.249759\), compared with analytical coefficients \(0.441933\) and \(0.249980\), respectively.

Infinite convergence, existence of a smooth center manifold, uniqueness of the parameter sign transition for all positive \(\nu,\tau\), and local stability are established by the analytic proof in `RESULT.md`; finite sampling alone cannot establish these assertions. No independent scientific audit has been carried out.
