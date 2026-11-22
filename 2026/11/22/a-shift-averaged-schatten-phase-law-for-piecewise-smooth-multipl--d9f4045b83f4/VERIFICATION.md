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

The attached `verify.py` uses Python 3 with NumPy and SciPy. It checks the pairwise equality of singular values for complex random finite cell matrices, the exact finite-grid sawtooth second-Schatten formula, numerical quadrature of the three asymptotic regimes on a piecewise-smooth symbol, and smooth periodic symbol convergence. All checks are finite and do not certify the infinite-dimensional limit.

The exact critical constants in the proof derive from centered linear variance on a length-\(h\) cell, giving \(h^2/12\), and from \(B(3/2,3/2)=\pi/8\), doubled because each cell has two singular values. For the periodic sawtooth the exact shift-averaged squared Hilbert–Schmidt mass is \(1/3-1/(6N)\), independently checkable from the crossing-cell variance formula.

The argument explicitly requires finitely many breakpoints with piecewise \(C^1\) extensions. It establishes no deterministic phase-independent trace law and no general \(BV\) extension. The literature comparisons are evidence of a novelty assessment, not a proof of absolute priority. Independent expert validation is not performed.
