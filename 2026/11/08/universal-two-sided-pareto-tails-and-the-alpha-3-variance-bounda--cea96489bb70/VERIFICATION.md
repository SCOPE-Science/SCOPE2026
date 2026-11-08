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

# Verification and reproducibility

The standalone file `verify_stationary_tails.py` runs using Python with NumPy and SciPy. The final package checker was executed and returned `PASS: 90 numerical assertions`, with tests covering: equilibrium-age normalization; independent numerical quadrature versus the exact Mellin gamma expression; positive- and negative-position tail expansions across four Pareto exponents; convergence to the first directional skew coefficient; stationary age-square moment when the third reset-time moment is finite; the critical truncated logarithmic coefficient; and the elementary free quantum-walk ballistic second-moment identity.

The proof in `RESULT.md` independently establishes the non-lattice Markov-renewal stationary mixture, the classical Weber--Schafheitlin Bessel Mellin identity's applicability, the super-algebraically small short-age correction, the complement-shift cancellation in gamma-ratio asymptotics, the two-sided expansion, and the exact infinite-lattice moment thresholds. No finite simulation or checker timeout is presented as proof of an infinite assertion.

The computation requires no external dataset, uploaded code, or downloaded paper. To reproduce: `python verify_stationary_tails.py` after installing `numpy` and `scipy`. Expected output includes four exponent-specific summaries and the final PASS count.

Limitations: tests use a few explicit positive parameters and do not numerically certify all quantifiers; the mathematical statements rely on the analytic proof. No independent audit or external validation has been conducted.
