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

The exact finite checker is `verify.py`, requiring only Python's standard library. Running `python verify.py` enumerated every permutation for each order 2 through 9 and passed 292 integer/rational assertions: one for every ordered pair of record indices in every size, plus a separate aggregate-covariance check at each size. The checks were recomputed using the embedded checker after extraction from the packaged finding.

The general proof is combinatorial and independent of the finite enumeration. It conditions on the unordered prefix-value set, uses conditional symmetry of the prefix ordering, and identifies the exceptional equal-index set. The asymptotic follows from a binomial-reciprocal bound and the classical harmonic variance of record counts. No independent external verification has been performed.
