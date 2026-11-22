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

# Reproducibility and limits

The exact probability is a one-dimensional integral of explicitly stated elementary functions. Recompute \(r_k^2\), \(q_k^2\), \(h_k\) and integrate \(F_k(t)\) for any \(k\ge1\) using standard numerical quadrature. The algebraic identity \(r_k^2q_k^2-h_k^2=k^2\) and the Kruskal lemma provide a hand-checkable analytic certificate. The threshold \(k=\sqrt3\) follows from the maximal value of \(|\sin2t|\), not numerical search.

The included `CHECK.py` computes all six distances for each sampled antipodal quadruple and builds its minimum spanning tree independently, comparing the observed diagonal property to the stated inequality for several aspect ratios. The random generator seed is explicit and numerical tolerances intentionally exceed Monte Carlo sampling error. The checker also tests near-circle coefficients and phase monotonicity. Its finite samples cannot prove the analytic assertions, which are supplied in the result. Public literature priority remains provisional; no independent audit has occurred.
