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

# Verification of the rooted-resultant formula

Run `python verify.py` in the directory containing `verify.py`, with Python 3, SymPy, NumPy and SciPy. No input files, network, external proofs or environment variables are needed.

The checker constructs each weighted path Laplacian and its \(n\)-column Krylov matrix from definitions. It verifies the squared rooted-resultant identity by exact rational matrices for three weight patterns at every vertex for \(2\le n\le8\). It separately verifies the already-established coprimality/unimodularity classification for all vertices of unit paths of sizes \(2\) through \(12\), strictly as a regression check. It also proves five parametric symbolic factor identities for a mirror-symmetric five-site weighted path and three exact phase comparisons. The positive finite-horizon Gramian determinant is separately calculated by 80-point Gauss–Legendre quadrature on a heterogeneous four-site path and compared to the exact spectral coefficient, and six stable-path resolvents are checked exactly. Total: **200** checks, all passing in the extracted package.

The proof in `RESULT.md` covers all positive real conductances, all path sizes, all valid observation horizons and the distinct zero/nonzero cases. Neither finite checking nor quadrature certifies the infinite claim by itself. The Cauchy determinant formula requires strictly positive damping; no infinite-horizon claim is made without it. The reviewed result has not received independent mathematical validation.
