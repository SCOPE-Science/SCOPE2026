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

# Verification and limits

The theorem is proved analytically in RESULT.md. The only nonstandard sign-count step uses the exact derivative representation \(\Delta_a'(t)\) and strict convexity of \(K(y)\) for every \(y>0\), with all expectations finite for those positive arguments. Endpoint signs use a positive mass of diffusivities larger than the mean, Jensen's inequality, and Fatou's lemma for divergent inverse half-moments. The time bracket follows from direct curvature calculation.

Run the included standalone \(\texttt{checker.py}\) using \(\texttt{python checker.py}\). It checks exact symbolic derivative identities and independently evaluates four specified positive diffusivity distributions (three discrete and one continuous with divergent negative half-moment). It checks the signs, bounded-support brackets, two extrema, and crossover times to high precision. The checker depends on Python with SymPy and mpmath. Its diagnostics are finite tests, not a substitute for the infinite-dimensional analytic proof.

Prior literature already contains the Brownian survival kernel, arbitrary diffusivity mixture, and an implicit typical-crossover criterion. This package does not assert that the earlier methods were new. The exact contribution is the all-distributions shape and uniqueness theorem. A related book chapter could not be read in full; priority limitations persist. Independent verification remains not performed.
