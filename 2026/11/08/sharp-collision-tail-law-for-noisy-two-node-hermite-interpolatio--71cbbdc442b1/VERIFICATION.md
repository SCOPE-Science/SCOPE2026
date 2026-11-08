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

Run `python verification/check_hermite_tail.py` from the research-package root with Python 3 and no third-party libraries. An actual execution passed 281 counted checks.

The checker performs exact-rational Gaussian elimination for square two-node confluent Vandermonde systems, verifies each prescribed derivative against the solution for Hermite multiplicities \(m=1,\dots,6\), and checks scaled squared \(L^2\) error norms at knot gaps \(1/10,1/100,1/1000,1/10000\). It also constructs the right-endpoint value-cardinal coefficient for \(m=1,\dots,8\) and tests its leading coefficient and endpoint derivatives, and evaluates the reciprocal-spacing normalization formula at three subcritical rational exponents.

These tests are exact for rational arithmetic inputs, while their convergence-threshold comparisons use a finite floating-point tolerance for the ratio of exact rational values. The all-orders theorem, tail integration, and sharp moment boundary are proved analytically in `RESULT.md`, not certified by this finite checker. No independent audit was performed.
