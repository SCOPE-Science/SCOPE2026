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

# Verification of the asymptotic optimal corner cut

The analytic statement is reconstructed in `RESULT.md`: (i) exact projected-edge correlations, (ii) exact first variation, (iii) triangle sine rule for fixed removed area, (iv) strict reflection comparison, and (v) strict monotonicity of the entire derivative numerator after division by \(\theta^2\). The sign certificate bounds the tenth derivative uniformly and proves a negative **continuous** upper bound for every \(0<\theta<\pi/6\); it is not a finite-grid inference.

Run `python verify.py` with Python 3 and SymPy. The included script checks the trigonometric simplification of \(F\), the seven displayed exact Maclaurin coefficients, the rational bounds used in the strict sign proof, the derivative-amplitude estimate, the root endpoint signs and a numerical root bracket. Its final four quadrature checks separately integrate actual polygonal widths and compare finite differences with the analytic first-order coefficient; these do not substitute for the proof. The script in this package was executed successfully and printed its PASS message.

Numerical approximations to the maximizing angle, cut ratio and decrease are illustrative. The theorem's exact content is the uniquely specified real root and its defining expression. No independent mathematical audit has been performed, no all-cut finite-size minimization is claimed, and no comprehensive global priority certification is asserted.
