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

The proof derives the exact operator norm for all \(0<p<1\), \(0\le\rho<1\), using a basis-of-jumps reduction, orthogonal centred Bernoulli monomials and an explicitly convex comparison polynomial. It proves the global optimizer cases and all equality functions. This is an analytical universal proof; exact-rational finite checks alone would not establish the continuum claim.

Use `python3 check.py` from this directory. The checker uses only the Python standard library. Its rational transition calculations compare independently computed state-space residual norms with the stated three Fourier formulas. It also tests the polynomial difference, spin-complement reflection, exact rational signs of a two-switch witness and the numerical critical-point location. The resulting count is printed at completion. Verification is same-model only; no independent audit has been performed.

The algebraic critical point is defined uniquely by the equation \(B(p,\rho)=\partial_\rho B(p,\rho)=0\) in the proved range; the printed decimal is approximate. The source comparison cannot rule out all unindexed or inaccessible historical work.
