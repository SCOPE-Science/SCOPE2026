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

The analytic proof in `RESULT.md` is the primary evidence. The standalone `verify_two_cycle.py` reconstructs all nonstandard algebraic identities using exact symbolic arithmetic, including the scalar two-cycle polynomial, normalized commuting-Jacobian product, the two complex transverse eigenvalues and the rational stability witnesses.

Run `python verify_two_cycle.py` with Python 3 and SymPy. A successful execution prints `SYNC_LOTKA_VOL_TWOCYCLE_IDENTITIES_OK` and returns code zero. Finite rational checks demonstrate strict examples; the complete parameter classification is proved separately by the convex quadratic and monotone competition coordinate, not inferred from sampling.

The polynomial map does not preserve the entire nonnegative orthant for arbitrary initial conditions. The proof concerns positive periodic states and their local Floquet spectra. Neutral multipliers at the two reentrance thresholds do not by themselves classify the nonlinear bifurcations. A potentially relevant earlier 1987 cyclic three-dimensional Lotka–Volterra article was inaccessible in full and is an explicit scientific-priority risk. Independent audit has not been performed.
