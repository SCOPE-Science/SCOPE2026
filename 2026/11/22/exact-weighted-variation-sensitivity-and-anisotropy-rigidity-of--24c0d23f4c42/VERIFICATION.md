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

# Reproduction

Run `python verify.py` using Python 3. The checker uses exact rational arithmetic and no external dependencies. It verifies an exact sharpness construction on 900 randomly chosen positive-weight, strictly increasing grids, 900 random two-input inequalities, and the explicitly stated gain-five example. The expected final line is `ALL_GCM_WEIGHTED_VARIATION_CHECKS_PASS`.

# Analytical limits

The theorem for all finite knot sets and positive weights is established by the hull-chord Jacobian calculation, finite piecewise-affine line-segment integration, and a strict-contact quadratic construction. Finite tests do not prove a statement about every real input. The proof does not classify non-nodal or higher-dimensional convexification. Historical-priority search is incomplete; no independent audit has been performed.
