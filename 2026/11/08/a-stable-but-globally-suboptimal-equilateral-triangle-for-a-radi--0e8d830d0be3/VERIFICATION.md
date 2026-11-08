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

# Reproducibility

Install `mpmath>=1.3,<2` (see `requirements.txt`) and run `python3 check.py`. The script reproduces two independent numerical approaches: monotone one-dimensional sector sum intervals and direct two-dimensional Cartesian quadrature. For the rigorous comparison it certifies the lower bound of the difference by evaluating a finite 4096-term sum with directed interval arithmetic. The geometric derivation of those finite enclosures, the all-exponent local Hessian inequality, and the continuity argument are in `RESULT.md`.

The interval calculation in the supplied environment returned a certified lower bound \(0.00011172321630575\ldots>0\), and an upper bound \(-0.03744802929406\ldots<0\) for the local Hessian-sign expression at \(p=7/4\). The direct 2D Cartesian midpoint integration returned approximate regular/comparator weighted areas of \(0.3737899773\) and \(0.3742713329\), agreeing in sign and scale with the sharper radial-sector quadrature. Computations were run on the standalone checker and repeated after writing the source artifact. Their finite precision and the dependency on `mpmath.iv` are explicit; no formal, third-party, or independent audit has been performed.
