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

# Reproducibility and evidence boundaries

The complete proof is in `RESULT.md`. The standalone code `verify_cumulant.py` can be run with Python 3 plus SymPy, NumPy and SciPy; it requires no external datasets.

Actual checks performed:

- Exact symbolic equality between the characteristic polynomial of the independently assembled four-state tilted generator and the displayed closed polynomial.
- Exact symbolic agreement of the fourth-order eigenvalue coefficient and the angular cumulant formula.
- Exact rational checks of axial and diagonal fourth-cumulant rates in the \((a,b,h,v)=(5,1,0,1)\) example.
- Direct finite-time, twenty-component moment-chain matrix exponentiation for five parameter/angle combinations; compared large-time rates with independently derived formulas, including both signs and nonzero half-turn rates.
- Direct evaluation of the fixed-chirality reentrant sign sequence at \(q=0,1/8,1/2\).

The matrix-exponential checks are finite-time diagnostics, not an exhaustive search over parameters or an infinite-time proof. Infinite-time existence, spectral dominance, all parameter inequalities and the unique maximum of the chirality threshold are established analytically. Independent scientific audit has not been performed.
