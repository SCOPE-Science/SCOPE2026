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

Run `python verify.py` with Python 3. The included script needs no external packages. Its rational calculations exactly check the two finite graphs' matrices, leading principal minors, graph Poisson solutions, resistance energies, and strict location of the near-critical multiplier coefficient.

The infinite-parameter statement is proved symbolically in `RESULT.md`: diagonalize the connected Laplacian and perturb the positive isolated rank-one eigenvalue. The local edge derivative is the usual inverse-operator derivative on the mean-zero space. Neither the finite checks nor numerical approximation are taken as substitutes for this all-graph reasoning.

The local-source birth matrix and equal-capacity assumptions are essential when interpreting the chosen kernel from the source article. The result excludes the degenerate equality \(\eta=Q_G\) and does not cover demographic noise, changing graph size in the limit, or source birth depending on graph degree.
