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

From the extracted package directory run `python verify_spectral.py` with NumPy, SciPy and SymPy installed. The script constructs the positive symmetric Bessel kernel via a scaled modified Bessel function, checks its Gram series and exact Feller branching Laplace composition, and uses independent Gaussian-quadrature matrices to inspect the short- and long-time principal eigenvalues.

The supplied run completed **89 deterministic assertions** successfully. In particular, \(j_{1,1}^2/4=3.670492660530974\ldots\), while \(t[1-\Lambda(t)]\) at \(t=25,75,200,500\) was approximately \(2.94222,3.27065,3.43564,3.52636\); these are consistency checks for convergence, not an estimate used to prove it. The script does not claim exhaustive verification of an infinite-dimensional eigenvalue problem.

The proof of the exact radius requires the positivity of the actual source projection onto the top eigenfunction. The proof of its long-time coefficient requires the Hilbert–Schmidt convergence of the sampled-killed branching semigroup to the continuously killed semigroup, followed by the Dirichlet \(J_1\) eigenvalue calculation. Those analytical arguments are detailed in `RESULT.md` and are not replaced by the finite test grid.

The exact numerical grids and code are contained in `verify_spectral.py`. The solver evaluates the symmetrized kernel directly, rather than relying on a value copied from a previous calculation. No independent audit is asserted.
