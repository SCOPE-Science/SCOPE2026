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

# Verification of the double-vacancy separation theorem

The mathematical proof is in `RESULT.md`. It uses a half-line Kolmogorov equation, an exact decomposition of the two-vacancy event into independent mark events, and the positive Taylor coefficients of \(2(\cosh\gamma+2-3\sinh\gamma/\gamma)\). All theorem parameters lie in \(0<p<1\), with terminal time \(1\).

Run `python checker.py` in the directory containing this file. The script uses only the Python standard library. It independently enumerates all site arrival orders and proposed colors on finite paths of sizes five, six, and seven; compares exact rational vacancy and color-pattern probabilities to finite one-sided recurrences; and verifies rank-one conditional joint distributions of whole left and right finite terminal configurations. It also checks positive Taylor coefficients and the limiting factor \(1/5\). The completed run reported `PASSED 180 exact finite-state and analytic coefficient checks`.

These finite enumerations are consistency checks, not an exhaustive proof of the infinite-line statement. Infinite-volume existence, the conditional factorization, and strict attenuation are established analytically. The floating-point decimal values are reproducible evaluations rather than formally certified rounding intervals. Independent audit is not yet performed.
