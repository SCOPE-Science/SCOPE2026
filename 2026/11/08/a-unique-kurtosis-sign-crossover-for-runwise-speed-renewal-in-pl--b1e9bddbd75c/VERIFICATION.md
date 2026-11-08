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

The analytical result is supported by an ordered four-time cumulant decomposition and a strict stochastic-order comparison for the ratio of two positive integrals. These are the essential infinite-domain proof steps; finite checks cannot replace them.

The standalone `verify_kurtosis.py` checks the cumulant and variance against a separately integrated six-variable moment system for speed laws \(R\in\{0,1\}\) at several rates and times. It also checks numerical threshold ordering and a sign change. The actual run passed 395 deterministic checks, including 252 independent ODE/moment comparison tests. Reproduce with `python verify_kurtosis.py` with Python, NumPy and SciPy installed. The checker is a reproducibility aid, not a formal proof or an independent audit.

Boundaries: the speed law requires a finite fourth moment and a strictly positive second moment. The model renews heading and speed together, with stationary initial velocity. External publication priority has not been certified.
