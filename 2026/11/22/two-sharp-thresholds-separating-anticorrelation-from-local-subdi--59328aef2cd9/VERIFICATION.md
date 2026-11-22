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

# Reproducibility and limits

The mathematical statement and complete sign/uniqueness argument are in `RESULT.md`. Use the accompanying `verify.py` from the same extracted directory. Requirements are Python with NumPy, SciPy, SymPy, and mpmath. The command `python verify.py` must terminate successfully and print a `PASS` assertion count; this run observed `PASS: 847 independent and algebraic checks`.

The checks independently compute the stationary OU covariance using a continuous Lyapunov solver, compare the matrix-exponential velocity covariance with its exact two-exponential form across five rate pairs and seven relative diffusivities, check positive stationary MSD and running diffusivity, evaluate the signed-first-moment identity, verify the derivative of its sign function, bracket the unique crossings, and test the sharp exponential critical prefactor using high precision. SymPy checks key algebraic simplifications exactly. Finite sample assertions, numerical roots, and displayed figures are *not* exhaustive proofs over the continuum of time or parameters; global validity rests on the closed-form sign proof in `RESULT.md`.

Prior formulas for the full autocorrelation and MSD are correctly credited. No separate independent scientific review has been undertaken. No claim is made for unavailable parameter regimes or fitting-based anomalous exponents.
