---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

The analytical proof in `RESULT.md` uses an exact entropy identity and the invariant subset of its zero-dissipation set, then a stable linear ratio equation along each approaching positive trajectory. This verifies the convergence and asymptotic amplitudes at the nonhyperbolic boundary, without assuming the initial state lies on a center manifold.

The accompanying `check.py` requires Python 3.10+, NumPy, SciPy, and SymPy. It checks the transfer identity and critical curvature algebra symbolically, constructs rational equilibria and illustrates the model at five exchange rates. For \(\alpha_i=1,\ (k_1,k_2,k_3)=(1,2,3),\ R_0=5,\ \gamma=2\), the two stationary thresholds are \(2/3\) and \(3\); substitution into the critical coefficient gives biomass amplitudes \(7/81\) and \(3/7\). The finite integrations illustrate, but do not certify, the infinite-time conclusions.
