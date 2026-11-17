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

The exact analytic proof is given in `RESULT.md` and independently checked against the direct directional-flux integral and simulation in `check_crossing_density.py`. Run `python check_crossing_density.py` with dependencies in `requirements.txt` installed.

In the executed checker, 2,400 midpoint angular grid values were used to test the sine-kernel Fourier identity at planar radial positions 0, 0.4, 1, 2. The radial normalization integral was evaluated up to radius 10,000 and compared with the closed \(1-8/\pi^2\) mass. Six-hundred-thousand independent hemispherical endpoint quadruples yielded crossing fraction 0.18871166666666667 versus exact 0.1894305308612978. The observed/truth crossing-radius subprobabilities were: radius 0.25: 0.011960/0.011919540; 0.5: 0.040358333/0.040502018; 1: 0.099986667/0.100763035; 2: 0.158113333/0.158551180; 4: 0.181835/0.182455686. All predeclared error thresholds passed.

Successful message: `HEMISPHERE_GEODESIC_CROSSING_LOCATION_LAW_OK 600000 tuples`.

Finite sampling cannot prove a continuum density and numerical quadrature cannot certify a global analytic Fourier identity. Those are established by the direct calculations in the mathematical proof. No external mathematical or historical audit was undertaken.
