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

# Reproducibility and limits

Run `python3 CHECKER.py` with standard Python 3. It constructs each finite semigroup for \(2\le r\le10\) with \(m=r+2\), checks all its elements and minimal generators in a complete range below the conductor plus multiplicity, and compares every genus-conditioned mean and the closed unconditional mean against exhaustive enumeration. Success produces `SHORT_CONDUCTOR_EMBEDDING_OK`.

The checker does not establish the infinite limit; the proof uses a matching factorization, a summable Bernoulli tail, a total-variation coupling, and the binomial central limit theorem. The original first public source date is the initial submission of arXiv:2611.11559v1 (2026-11-08). Independent mathematical validation has not been performed.
