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

Analytical checks: expand the Gaussian characteristic functions exactly to degree four; compare both quadratic and quartic homogeneous polynomials; recover the isotropic scalar from the smallest eigenvalue of \(Q\) when \(d\ge2\); deduce the rank-one tensor and its kernel; obtain the variance-difference square from a unit kernel vector. Check sufficiency by explicit construction. The parameter conditions require \(s>0\), \(z\ge0\), \(z<s^2\), and \(T\succeq0\) of rank at most one. Both one-dimensional triples are strictly admissible and exactly collide through quartic order.

`CHECK.py` tests the polynomial identity and the one-dimensional example using exact rational arithmetic. It is an independent finite arithmetic cross-check only; it does not constitute an all-dimensional certificate or an independent mathematical review.

Limitations: the data are formal derivatives at frequency zero, not finitely sampled noisy measurements; only two unit-mass isotropic Gaussian components are covered. Literature comparisons have explicit abstract/full-text coverage limits in `AUDIT.json`.
