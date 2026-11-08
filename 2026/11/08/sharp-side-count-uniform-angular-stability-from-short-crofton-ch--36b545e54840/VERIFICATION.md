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
The accompanying `verify.py` is a self-contained numerical test using NumPy. Run `python verify.py` in a Python environment with NumPy installed.

The checker (i) simulates invariant lines by uniform normal angle and signed offset conditioned on hitting each polygon; (ii) compares four empirical short-chord CDF values to the analytic linear formula, within six empirical standard errors plus an explicit tolerance; (iii) tests the vertex-wedge angular integrals against the exact coefficient by quadrature; (iv) checks the strictly convex angle coefficient's second derivative over a dense mesh; and (v) constructs four genuinely closed convex equilateral polygons with alternating exterior turns and observes their sharpness quotients decreasing towards \(1/6\).

The exact theorem does not depend on the finite Monte Carlo runs. Analytic checks critical to infinite validity are in the proof: finite-edge separation, exact normal/offset Jacobian, the strict differential inequality, and the explicit sharpness construction. No independent audit was performed.
