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
# Verification notes

The accompanying `VERIFY_NUMERIC.py` is standalone and requires Python 3, SciPy and NumPy. It integrates \(\dot{\log x}=-y\), \(\dot y=e^{\log x}-1\) rather than relying on the Lambert branch for its trajectory values. It independently uses the conserved-energy endpoint root as a check, detects the first positive observable-speed crossing, compares with the analytic two-term law, checks the first boundary-layer correction, and checks the Gaussian initial-distance inversion. It runs 24 parameter combinations plus one separate direct physical-time quadrature.

Command: `python VERIFY_NUMERIC.py`

Observed output: `VERIFY_OK ODE_first_exits=24 root_conditions=24 Gaussian_log_inverse=24 independent_time_quadrature=1`

The proof's infinite-parameter statements rely on exact energy conservation, monotonicity, and controlled boundary-layer asymptotics, not the finite numerical tests. Machine precision limits the checks for very small initial data; integrating the logarithm of the initial coordinate avoids underflow. The related 2022 source could not be fully inspected, and no independent review has been carried out.
