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

# Reproduction and scope

Run `python check_star_inverse.py` from the folder containing this document and the checker. It uses Python 3, NumPy, SymPy and SciPy. The recorded reproducibility marker `RARE_HUB_INVERSE_AND_SLOW_LIMIT_OK` was obtained using the script packaged alongside this proof.

The checker performs exact rational symbolic verification of the Schur-complement determinant formula for four spokes and numerical recovery of two-, three-, and four-spoke interaction rates, including repeated values. It also checks numerical strict interlacing and convergence to the analytic effective semigroup at a sequence of hub masses. The results do not prove the statements for infinitely many parameters; the mathematical proof in RESULT.md supplies those arguments.

The inverse formula assumes the full noiseless nonzero spectrum, a known positive central mass and equal known peripheral masses. Numerical root extraction at repeated coefficients can lose precision. The slow limiting formula fixes the interaction rates before taking the mass to zero. No independent audit has been performed.
