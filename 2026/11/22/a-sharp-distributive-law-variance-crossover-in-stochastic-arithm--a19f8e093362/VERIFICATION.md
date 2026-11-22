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

## Reproducible checks

The proof is analytical and uses the two-sided stationary conditional-Poisson construction for unit-death queues, the exact covariances of independent Poisson immigration–death sources, and elementary Laplace integrals. The standalone `verify.py` (Python 3 standard library) checks exact rational expressions and sign classification for 216 positive parameter triples, plus explicit boundary and paired-regime examples. Its expected output states 1,086 passed rational checks and equality at a positive triple.

The finite tests do not establish the all-positive-real-parameter theorem. The argument does not address alternative architectures, unequal death rates, transient data, integrated autocovariance readout, or the historical-priority uncertainty from restricted full text.
