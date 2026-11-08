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

The analytic proof decomposes the weighted rook Hamiltonian into four tensor eigenspaces and combines the two middle sectors only at the exact spectral collision. The general capture lemma is proved on the finite-dimensional bright/dark decomposition, so neither the infinity-time limit nor the loss-rate independence is inferred from enumeration.

Reproduce the independent finite checks with `python checker.py` (SymPy, NumPy, and SciPy). The checker forms the full labeled adjacency independently of the tensor spectral formulas, computes the exact Krylov orthoprojector for all \(m,n\in\{2,3,4,5\}\) and both coupling regimes, and tests every site orbit. It also evaluates the non-Hermitian matrix exponential at late times for selected sizes and compares it to the analytical capture value. The completed run reported 246 exact assertions and 32 dynamical comparisons.

Finite computations do not independently prove all sizes or all continuous parameter values. Quantified numerical tolerance for the dynamical comparisons is \(10^{-8}\). The singular jump concerns the infinite-time limit only, and no claim of independent validation or external certification is made.
