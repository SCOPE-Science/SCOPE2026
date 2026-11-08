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

# Reproduction of the mathematical calculation

The companion standalone `verify.py` requires Python and SymPy. Run `python verify.py` after extracting both files into the same directory. A successful run prints `VERIFY_OK` and the exact values of \(D_c\), the cubic coefficient \(C\), and the coefficient of the invader cutoff \(a_c\). The checker's symbolic operations recompute the Fourier-symbol normalization, the quadratic constant and second-harmonic equations, the cubic fundamental-mode solvability equation, and the second-order invasion eigenvalue coefficient. Each identity is asserted rather than accepted by proximity of floating-point values. A finite Fourier-mode sign scan is only a diagnostic: the paper's proof covers all Fourier modes by their residue classes and monotonicity.

The mathematical proof in `RESULT.md` separately establishes the infinite-dimensional hypotheses: the spectral gap at the critical resident mode, the reduced branch and signed cubic coefficient, positive resident existence, simplicity and sign derivatives of the periodic elliptic principal eigenvalue, the monotone frontier, its zero- and infinite-diffusion limits, and the perturbation expansion. These are **not** computationally certified by the script. Numerical collocation of a non-infinitesimal pattern was performed as a consistency check and not used to justify the theorem or its error bounds.

Exact scientific limits: the proof addresses a sufficiently small positive resident pattern and the spectral growth of a rare competing population. No nonlinear coexistence, global attractor classification, or stochastic model conclusion is verified. Independent audit is not performed.
