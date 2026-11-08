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

# Verification scope

The exact proof is in `RESULT.md`. The `verify.py` script provides independent finite-size corroboration, not a proof beyond the tested sizes. Running `python3 verify.py` with Python 3 and NumPy returned:

`PASS: 40 ring/flux cases; all matrix and capture checks passed`

For each \(3\le n\le10\) at \(\Phi\in\{0,\pi/2,\pi,3\pi/2,\pi/3\}\), the script checks Hermitian idempotence of the displayed projector, commutation with the coherent dynamics (indeed annihilation at zero energy), zero amplitude at every detected double-occupation site, bosonic exchange symmetry, exact localized-pair survival formulas, and all diagonal initial states. It independently diagonalizes the coherent two-boson Hamiltonian and calculates the collision-map nullity on each numerically degenerate eigenspace; it separately computes the count of loss-free real eigenvalues of the finite non-Hermitian generator with explicitly unequal positive rates.

Floating-point spectral grouping is performed with tolerance \(10^{-8}\); it is not an exhaustive symbolic certificate. The infinite-domain proof instead rests on the exact trigonometric equality criterion, unique resonant center-of-mass sector, its collision rank one and finite-dimensional dissipative spectral decomposition. No independent external audit or experimental confirmation was performed.
