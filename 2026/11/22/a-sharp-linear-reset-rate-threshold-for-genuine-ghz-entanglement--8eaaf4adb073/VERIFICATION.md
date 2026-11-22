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

# Reproduction
Execute `python checker.py` with SymPy and mpmath. The supplied source computes exact stationary diagonal components for \(3\le n\le8\) at four rational reset-to-noise ratios, verifies their population normalization and stationary master equations, and compares the GM concurrence expression with independent age quadrature and numeric thresholds. These are finite tests only; the existence, uniqueness, and two-term large-size law are analytically established in `RESULT.md`.

The phase-space dimension grows exponentially with \(n\), but exact Hamming-weight symmetry collapses the needed stationary computation to \(n+1\) scalar populations. The protocol considers ideal full entangled-state restoration and Markov local depolarization. A self-review was passed; independent audit and external experimental confirmation are not performed.
