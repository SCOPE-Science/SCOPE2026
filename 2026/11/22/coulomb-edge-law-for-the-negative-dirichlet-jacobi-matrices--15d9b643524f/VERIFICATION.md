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

The analytic argument uses constant-hopping spectra, finite-rank interlacing, a dyadic boundary-layer bound, an interior Riemann-integral limit, and monotone inversion. The exact constant comes from \(\pi^{-1}\int_0^s\sqrt{s/x-1}\,dx=s/2\). These steps prove the infinite statement for each fixed \(s>0\); the numerical checks are not extrapolated to a proof.

The bundled `check.py` requires Python, NumPy and SciPy. Run `python check.py`; at packaging time it passed 23 finite checks, including exact block eigenvalue formulas, three independent integral evaluations, and twelve finite-Jacobi threshold counts. For the finite threshold counts, the truncation includes the estimated forbidden tail and observed discrepancies are explicitly nonzero. No exact infinite-dimensional eigenvalue computation was claimed.

Limits: no independent mathematical audit, no finite-level eigenvalue formula, no uniformity in \(s\), no determination of the spectral norm, and residual literature-priority risk from potentially dominating generic semiclassical asymptotic theorems.
