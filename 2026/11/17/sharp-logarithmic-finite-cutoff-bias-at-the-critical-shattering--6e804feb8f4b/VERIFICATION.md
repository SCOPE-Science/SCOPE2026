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

# Verification

The scientific proof is contained in `RESULT.md`. Reproduce the included finite numerical checks with `python3 check.py` using only Python's standard library. They check coefficient recurrences, formal generating identities at interior arguments, positivity and slow convergence of second-moment partial sums. They do not certify infinite limiting statements.

The analytic checks include: exact differentiation of the source generating equation, the sign and boundary behavior of the derivative deficit, the reciprocal differential inequality at the marginal parameter, and an elementary two-scale sandwich with nonnegative coefficients. The source model, date, exact normalization, scope of stationarity and distinct fragmentation operators are identified in `RESULT.md`.

The analytical limit uses existence of the mass-conserving stationary critical sequence, with an endpoint derivation from the source's supercritical stationary family. The statement does not include pointwise cluster-size asymptotics or transient kinetics. Search-based priority assessment is not independent validation.
