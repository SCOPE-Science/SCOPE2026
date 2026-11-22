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

# Reproducibility and mathematical verification

Run `python CHECKER.py` with Python 3 and SymPy. The program symbolically tests the integrated scalar identity, the logistic composition law, the stationary-point algebra and critical constants, and exactly checks an admissible rational parameter witness. The analytic proof in `RESULT.md` supplies the all-group-size and all-admissible-parameter quantifiers; the program is an algebraic cross-check, not an independent theorem prover.

The physically relevant exposure variable stops at the first root of \(1/p-1\) when one exists. The strict sign of the first derivative yields an exponential approach for a simple root; the strictly negative second derivative at the unique maximum yields \(t^{-2}\) at a double root. The proof does not cover initially missing strategies, finite populations, local rather than global feedback or stochastic environments. No independent scientific audit has been performed.
