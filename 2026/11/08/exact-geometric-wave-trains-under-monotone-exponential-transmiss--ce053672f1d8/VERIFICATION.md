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

The transformation, energy conservation, strict convexity of positive level sets, uniqueness of stationary-line energy minima, transversality away from threshold, and exact geometric peak decay are shown by explicit algebra in `RESULT.md`. The finite checker in `check.py` is standalone and uses only the Python standard library. Its fourth-order Runge–Kutta calculations test the rational example, monitor the first integral and record consecutive prevalence/incidence peaks; it is not a proof for all time.

The wave theorem assumes \(0<a<\gamma\), positive initial susceptible/infective counts and deterministic closed SIR dynamics. The exact two-knot statement concerns the representation of \(\log\beta\) on a finite interval, not an empirical model-selection guarantee. Independent external audit has not been performed.
