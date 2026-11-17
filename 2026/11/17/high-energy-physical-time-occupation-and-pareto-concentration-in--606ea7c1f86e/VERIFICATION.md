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

The coordinate conjugacy and invariant are checked by symbolic differentiation in `verify_lva.py`, and the two-branch exact period integral is evaluated numerically for sample energies. The required infinite-level statements follow instead from the explicit inverse-branch integral bounds proved in RESULT.md, including both turning-point singularities and the normalization in physical time.

The source's center existence and time-changed Lotka--Volterra reduction are independently read from Banaji--Boros--Hofbauer, Section 5.2. The new limit is fixed-parameter, not uniform near the vertical-Hopf parameter boundary. The standalone checks do not certify originality or mathematical independence. No independent audit was performed.

The standalone run on the packaged source reported `LIFTED_CENTER_SYMBOLIC_AND_FINITE_PERIOD_CHECK_OK`. For \((a,b,d)=(1,2,3)\), finite-energy physical periods at \(h=10,30,60\) were approximately \(2.962106821\), \(6.557906736\), and \(11.752051372\), with period-to-energy ratios converging toward the analytical coefficient \(1/6\). The reported finite values are only diagnostics.
