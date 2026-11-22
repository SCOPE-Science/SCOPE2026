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

The package contains a standalone Python 3 script, `checker.py`, requiring only the standard library. Invoke `python3 checker.py` to reproduce 506 successful assertions. It uses rational interval enclosures for \(\pi\), \(e^{2\pi\lambda}\), and the two stated strict sign claims. In particular, it proves \(K(0.18008)<0<K(0.18009)\), and confirms that the log-likelihood-ratio slope at zero is positive for the exact pair \((0.10,0.11)\). A seeded set of floating-point identities is diagnostic, not a global proof.

The mathematical proof is in RESULT.md. Its global parts require no numerical test: the derivative of \(K\) is strictly positive on \((0,\infty)\), and the terminal mixed partial is strictly negative for every admissible parameter. Normalization and positivity follow independently from wrapping the source density. Therefore finite sampling, numerical grids or solver convergence are not used to claim an infinite quantifier.

No independent mathematical audit has been conducted. The theorem does not claim to resolve inference in the location-unknown or freely rotated family, or uniqueness in the entire mathematical literature.
