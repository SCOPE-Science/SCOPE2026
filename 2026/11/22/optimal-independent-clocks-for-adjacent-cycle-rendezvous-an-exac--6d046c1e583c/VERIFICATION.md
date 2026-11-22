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

The analytical proof in `RESULT.md` establishes the full-domain formulas and their parameter boundary conditions. `CHECK.py` separately constructs the exact killed Markov chain of the relative walk, solves linear equations over rational numbers, and compares its mean with the spectral and hyperbolic identities for a finite list of sizes and movement probabilities. It also performs optimizer asymptotic checks. Run `python CHECK.py` with SymPy and SciPy installed. The successful run reported `PASS 193 independent checks`.

Only the finite instances are computationally checked. The universal strict convexity, arbitrary-size trigonometric summation, large-size first-order correction and Wald stopping-time step are mathematically proven, not formally certified. The source comparisons involve the 2003 complete relevant chapter, an accessible 2014 preprint, the motivating 2026 source and the 2022 article; the 1995 original could not be obtained and may contain stronger priority information. Independent audit: not performed.
