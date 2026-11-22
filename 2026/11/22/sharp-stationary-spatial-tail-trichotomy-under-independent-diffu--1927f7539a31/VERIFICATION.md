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

# Reproducible verification

Run `python verify_reset_edge.py` with Python 3, NumPy and SciPy. The script computes the stationary characteristic function from a real renewal integral and independently from the positive spectral measure. All 12 comparisons on the grid \(r\in\{1,2,3\}\), \(k\in\{0,0.2,1,2\}\) (for \(W(d)=\tfrac32\sqrt{1-d}\), \(\lambda=1\)) agree to the script's explicit tolerance. The script checks normalization and a subcritical spectral residue, positivity of stationary densities and representative three-regime tail ratios, the supercritical boundary exponential moment, and four edge-coefficient tests for \(\nu\in\{1/4,3/4\}\). The checker exited successfully with `PASS` when executed from its content. Finite quadrature and selected asymptotic ratios do not constitute general proofs; the analytic proof is in `RESULT.md`.

The critical denominator has a nonstandard branch singularity. Its proof-critical evaluation is the explicit Cauchy-transform expansion in `RESULT.md`, not a numerical extrapolation. The isolated pole and spectral continuum are both retained; omission of either would invalidate the corresponding regime. Source access and scholarly priority remain distinct from mathematical correctness, and independent validation has not been performed.
