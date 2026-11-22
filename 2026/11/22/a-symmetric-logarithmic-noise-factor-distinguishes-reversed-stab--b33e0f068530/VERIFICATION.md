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

# Reproducibility and proof checks

The mathematical proof is given in `RESULT.md`. The critical global assertion is the positivity of the four-term reciprocal-exponential difference, proved analytically through the strict convexity of its logarithmic-scale representation. A separate Lévy-integrability estimate establishes existence of the symmetric infinitely divisible noise. The gamma reflection formula proves that its characteristic function equals the quotient of the two logarithmic-clock characteristic functions; the factorization and Jensen inequality are then standard.

The included `checker.py` is a finite numerical consistency test. Run `python checker.py` after installing `mpmath`. With `mpmath` configured at 42 decimal digits it reported `PASS 750 finite diagnostic comparisons`. It tests complex Mellin ratios, positivity on grids, local log-cumulants, and Lévy–Khintchine numerical quadratures across several stability parameters. It does not certify all real parameter values and is **not a substitute** for the proof.

Boundary conditions: both indices lie strictly between zero and one, time is positive, clocks are independent, and the stable Laplace exponents have unit scale. This is strictly a marginal law, not a pathwise process factorization. The ordinary first moment of the original stable clock is infinite, and no ordinary convex ordering of the unlogged clock is claimed. External independent assessment has not been performed.
