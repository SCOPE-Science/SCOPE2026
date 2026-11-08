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
The proof reduces boundary-normal counting to the meridian astroid and evaluates its intersection volume with the spheroid. Cross-section integration and exact polynomial factorization establish the closed form, not statistical fitting.

Run `python check.py` from a Python environment with NumPy and SciPy. The checker uses explicit random seed 602714, tests eight aspect ratios against numerical quadrature and volume-uniform Monte Carlo, tests meridian normal stationarity roots at 1,440 sampled points, and verifies the slender asymptotic coefficient numerically at four scales. A successful run prints `SPHEROID_NORMAL_COUNT_VOLUME_LAW_OK` with sample counts. Finite tests do not certify the global claims, which rely on the proof. The axis and caustic are zero-volume exceptional sets.
