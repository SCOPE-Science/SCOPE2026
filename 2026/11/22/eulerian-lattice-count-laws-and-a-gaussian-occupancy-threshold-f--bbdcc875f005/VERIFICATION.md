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

# Reproducible mathematical checks

Run `python3 verify_eulerian.py` with Python 3.10 or later and no third-party dependencies. The script computes exact integer Eulerian rows, rational atom probabilities, finite-law support, the geometric mean, direct independent integer-point enumeration for 300 deterministic pseudorandom translated frusta, and numerical critical-window comparisons. It exits with a nonzero status on any failed comparison. The critical-window test is only numerical corroboration: the proof invokes the central limit theorem and uniform integrability. A direct sum-of-uniforms representation establishes the critical mean and variance scaling analytically. All computations described here apply only to the displayed parameters and do not amount to exhaustive infinite certification.
