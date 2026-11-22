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

# Reproducibility and checks

The companion `verify_depth.py` is standalone, requires Python 3 and only the standard library, and reproduces the finite tests with `python3 verify_depth.py`.

- Independently enumerate entire recursive-tree parent assignments and the backwards Markov-chain distribution for every size from two to nine and three rational polynomial exponents.
- Enumerate individual ancestry paths to check the pathwise potential identity and nonnegative correction exactly using rational arithmetic.
- Propagate depth means and variances by a separate finite recurrence for 3000 vertices, as diagnostics rather than asymptotic certificates.
- Recorded outcome: 973 passed finite assertions and diagnostics, with no failures.

The infinite results require the proof's state-dependent deterministic logarithmic-error estimate, bounded-increment martingale central limit theorem and martingale isometry. Exhaustive finite tests cannot prove those limits. Independent audit has not been performed.
