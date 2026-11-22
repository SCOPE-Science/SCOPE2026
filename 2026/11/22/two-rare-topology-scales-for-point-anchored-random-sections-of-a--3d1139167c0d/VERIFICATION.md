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
# Analytic and numerical verification

The claimed results are established by a direct proof in `RESULT.md`: (i) toroidal Jacobian for uniform volume-point anchoring; (ii) exact section topology classifier; (iii) square-root angular boundary-layer limit with a tilt-integrable majorant; (iv) an exact semicircle/arcsine integral yielding the annulus coefficient. Finite computer experiments alone cannot prove either asymptotic limit.

Run `python3 check_torus_area.py` with Python 3, NumPy and SciPy. The script checks 130 independent angular discretizations against exact conditional arcsine-CDF predictions and uses deterministic Gaussian quadrature to evaluate four increasing major radii. With the packaged implementation, the observed scaled disk probabilities at radii \(5,20,80,320\) were approximately \(1.054344295,1.045220482,1.038786341,1.036698474\), converging toward \(1.0359209536249055\). Corresponding scaled annulus probabilities were approximately \(0.180755848,0.180165497,0.180135938,0.180132289\), converging toward \(0.1801265486974894\). Numerical quadrature is corroboration and is not a certified error-bound argument.

All topology equalities are up to planar-section tangencies and limiting transition planes, which form null events. The theorem does not claim independent external audit or formal computer certification.
