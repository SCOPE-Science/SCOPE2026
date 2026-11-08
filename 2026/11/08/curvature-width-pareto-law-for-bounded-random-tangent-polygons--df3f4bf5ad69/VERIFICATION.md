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

The analytic argument proceeds by angular gap decomposition, a uniform single-near-semicircle area asymptotic, a bound ruling out multiple near-singular gaps at first order, and integration of the exact adjacent-normal intensity. It is not a numerical or external certification.

Run `python verify_tangent_tail.py` from this package with NumPy/SciPy installed. The independent numerical checks include finite-angle tangent-line intersections for a circle, an ellipse, and a noncircular constant-width body, exact special-case comparisons for circles and the constant-width Fourier family, numerical evaluation of the general coefficient for several sample sizes, and direct simulations of tangent polygons. The code reports `VERIFY_OK` when all assertions pass.

The near-gap tests used \(\delta=0.008,0.002,0.0005\) and showed \(\delta A\) approaching the predicted \(w^2/2\). The numerical evaluation for a unit circle and \(n=3\) gave \(C_3\approx3.8197186343\); for an ellipse of semiaxes \(1.5,0.8\) it gave \(C_3\approx4.7828171247\). For \(h=1+0.06\cos(3\theta)\), the exact value is \(C_3\approx3.4331164110\) with \(p_3\approx0.2461092665\). The simulation drew 350,000 triplets per shape; finite-threshold errors are not assumed to vanish at a specified rate. No independent audit has been performed.
