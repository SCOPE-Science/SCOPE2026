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

# Reproducible checks and analytic limits

Run `python3 verify.py` with Python 3 standard library; no network access or external data is needed. The recorded execution printed `CHECK_OK 452 assertions`, and displayed the limiting value `1.140093467050976`.

The checker constructs the unique inside-the-unit-circle root of the quartic denominator and calculates the exact residue expression for lattice coefficients. Its truncated absolute mass has an explicit geometric tail bound. At seven smoothing strengths (from \(10^{-4}\) through \(10^8\)) it tests the unit row sum and positivity of the central coefficient. It independently reconstructs finite-cycle kernels by discrete Fourier sums for six cycle lengths and compares them against periodized lattice coefficients; it also verifies norm dominance and large-smoothing convergence in tested dimensions.

The analytic justification does not rely on these finite tests. Fourier \(L^1\) convergence proves local scaled-kernel convergence; a uniform derivative \(L^2\) estimate proves tightness of the absolute mass. Summing the negative intervals of the limiting continuum Green kernel gives an exact closed constant. Fourier periodization handles the large-cycle limit and finite-dimensional spectral convergence handles the strong-smoothing limit on a fixed cycle. Neither the checker nor the analytic argument establishes historical novelty, nor does the checker certify the infinite-parameter theorem by enumeration.
