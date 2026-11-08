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

Run `python check_affine_simplex_section.py` with Python 3, NumPy and SciPy. The included checker was executed successfully and returned `AFFINE_SIMPLEX_SECTION_FACE_VECTOR_CHECKS_PASSED`.

The program numerically integrates the positive exact Gaussian spacing kernels for \(n=3,4,6,8\), verifies normalization, left/right symmetry, the independent edge-count expectation and all crossed-face combinatorial identities. For each small \(n\), it draws 140,000 Gaussian normal vectors and applies the **directional-width/centered-norm** weight corresponding to the invariant Crofton hyperplane distribution, before comparing the empirical side-split probabilities with the quadrature formula. Dimensions \(300,1200,4800\) are checked for convergence in mean empirical residual toward the fixed-rank exponent profile for \(j=0,1,2\).

The exact finite results rest on face-lattice combinatorics and Gaussian radial independence; the limit rests on Gaussian extreme-value concentration, the width-tilt \(L^1\) lemma and binomial tail bracketing. Numerical data do not prove the infinite limit or establish historical novelty. Random seeds are fixed for reproducibility. No independent mathematical audit has been performed.
