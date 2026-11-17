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

# Reproducible checks and analytical limits

Run `python3 verify_quadratic_bv.py` from the complete accompanying package using Python 3 and no third-party dependencies. The standard-library exact rational checker independently computes Gram inverses in the monomial basis and compares 464 cases with the derived jump formula, checks the first ten sharp rational coefficients, tests the all-input bound on rational vectors, and verifies six continuum jump moment identities. Its floating-point diagnostics compare the claimed asymptotic value and maximizing jump fractions for four sample dimensions. Expected final line: `ALL_QUADRATIC_BV_CHECKS_PASS`.

The proof of the all-dimensional norm relies on the jump-basis decomposition and the orthogonal polynomial identity, not finite tests. The limit and maximizing-jump localization rely on explicit continuum total variation, derivative-root analysis, and a uniform step-moment convergence argument. Exact symbolic identities in the proof have been reconstructed; no automated or independent proof certification has been performed. Historical novelty is provisional and the included comparisons have explicit scope limits.
