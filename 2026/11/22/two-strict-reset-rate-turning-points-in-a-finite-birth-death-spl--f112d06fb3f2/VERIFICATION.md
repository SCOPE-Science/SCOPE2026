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

# Reproducibility and verification limits

The standalone `verify.py` uses only `fractions.Fraction` and `math.comb` from the Python standard library. Command: `python3 verify.py`.

It reconstructs both tridiagonal continuants and the boundary path-weight prefactor directly from the ten rational transition probabilities. It expands the exact derivative numerator and the transformed polynomial, confirms their coefficient-sign pattern and four rational derivative brackets, and solves both boundary-discounted first-passage systems at six rational parameter choices using exact Gaussian elimination. The observed result was `PASS 32 exact rational assertions; two strict interior extrema certified by Descartes and sign brackets`.

The proof of the infinite claim (there are exactly two roots in the entire interval) comes from Descartes' rule applied to the explicit fourth-degree polynomial, plus two rational sign-change brackets. The checker corroborates its inputs but finite test values alone cannot establish an interval-wide theorem. No independent mathematical audit or external certification has been performed. The model assumes a fresh independent reset decision after each nonabsorbing walk step; no general reset protocol or unknown minimum state count is covered.
