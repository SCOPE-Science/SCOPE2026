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

# Reproducibility and mathematical limits

Run `python3 checker.py` with the Python standard library. The checker uses `fractions.Fraction` for exact algebraic identities (positive diagonals, shift identities, top norms, and finite telescoping), and `math` only for selected continuum level counts and moment quadrature. A successful run prints `ANNULUS_MONOMIAL_SPECTRAL_CHECKS_OK 2508`.

Analytical completeness depends on the basis identity, rational factorization, lattice count, layer cake and integrable tails, all explicitly proved in `RESULT.md`. No finite check proves the infinite-dimensional assertions. The result does not cover nonscalar symbols, alternative boundary weights, or a general varying-symbol trace theorem.
