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

The proof establishes an all-parameter theorem. The standalone `check_gini_pcenter.py` is a finite corroborating checker. It uses exact rational cut enumeration for linearized maps, plus numerical root-finding for selected genuinely nonlinear maps; root-finding is not a proof of the asserted global bounds or asymptotic sharpness. Its expected final line is `ALL_P_CENTER_GINI_CHECKS_PASS`.

Analytical checks: (i) the center is uniquely defined by a strictly convex energy; (ii) the cut formula has no hidden normalization and exactly preserves the coefficient of the added center; (iii) at \(p>2\) each Jacobian weight is at most one half by the balance equation and a concave-power inequality; (iv) the sharp superquadratic derivative at a two-extreme configuration exists and has weights one half; (v) at \(1<p<2\) the constructed perturbation satisfies \(h-c_h=o(h)\); (vi) integration of the Jacobian bound is justified by sup-norm Lipschitz regularity and approximation of exceptional line segments.

Known limits: the checker only examines small finite dimensions and selected exponents; no external independent audit has been performed.
