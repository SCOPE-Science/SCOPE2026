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

The exact finite identities were checked with the provided `checker.py`, executed from the delivered package contents. All 134 reported checks passed. The script enumerates onto words and possible fresh draws for small cases and independently compares exact Stirling-number expressions; the larger finite cases test convergence diagnostics only.

The infinite-n proof rests on the conditional surjection law, the span-one local central limit theorem for zero-truncated Poisson sums at a fixed parameter, and the union-bound exclusion of repeated colors and short-time rescues. Numerical checks alone do not establish the limit. No independent validation has been performed.
