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

# Verification details

Execute `python3 verify_kmp.py` from this package using Python 3 standard library. The program directly integrates the strictly positive spectral measure after the change of variables \(\lambda=4\sin^2\theta\), checks five resolvent values, and verifies both exact spectral moment sum rules. It also implements a separate event-driven simulation of local KMP bond exchange with 20,000 independent realizations at each of three observation times.

Analytic verification consists of the explicitly derived martingale bracket, three half-line pair-moment equations, the physical decaying resolvent branch, and contour inversion of its sole branch cut. A finite sample cannot establish these identities for all times. The simulation produces stochastic tolerances and does not establish asymptotic convergence, uniqueness, novelty, or independent audit.

A unit-rate microscopic bond generator yields deterministic diffusivity \(1/2\). For comparison with the diffusivity-one continuum convention in the source, double the bond event rate, i.e. substitute \(2t\) for \(t\).
