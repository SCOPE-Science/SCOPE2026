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

# Verification and reproducibility

Run `python3 verify_star.py` in a directory containing this file and the script. Only the Python standard library is required. An actual execution produced:

`PASS exact-state and survival checks: 6048`

The script independently enumerates infected-state masks and uses exact rational first-step recursions for the Laplace transform of first detection, for all tested \(1\le m\le7\), every \(1\le k\le m\), three positive rational values of \(\alpha\), four selections of \(\beta\) (one designed to hit the exact equality threshold), and three positive rational transform arguments. It tests both hub-monitoring and leaf-only layouts and their signed transform difference. Numerical survival checks at three positive times supplement, but do not replace, exact arithmetic.

The all-parameter proof is analytical: conditioning on the initial seed gives the three mixture components, and a positive exponential convolution fixes the sign of the survival difference for every positive time. Finite tests do not prove the theorem for untested sizes or rates. Source comparison and historical priority are not mechanically certified.
