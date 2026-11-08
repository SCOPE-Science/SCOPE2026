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

Run `python3 check.py` with Python 3.10 or later. Expected terminal output:

`PASS: exact multiplex updates, geometric waiting-time convolutions, and binomial tails.`

The verifier uses only Python's standard library and exact `fractions.Fraction` arithmetic. It tests two and three agents, depths one through five, homogeneous and heterogeneous influence probabilities, different row-stochastic internal matrices, and times zero through fifteen. All tested equalities are exact rational equalities, without numerical tolerances.

The infinite-depth central-limit and bottleneck assertions follow from the independent-geometric representation and classical limit theorems, not from finite tests. The spectral characteristic polynomial is proved analytically by block triangularity. The verification does not constitute an independent audit.
