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

The exact `verify.py` uses Python 3 standard library `fractions.Fraction`. It verifies the Walsh–Parseval identity, the primal \(\ell_1\) constraint, complementary slackness, active-subgradient stationarity, and exact squared residual distances. It exhaustively enumerates truth tables in Boolean dimensions 2, 3, and 4 (16, 256, and 65,536 inputs). Farthest squared distances are respectively \(1/4\), \(9/16\), and \(9/4\); the even-dimensional bent multiplicities are 8 and 896. Quadratic bent witnesses in even dimensions 2, 4, 6, and 8 satisfy exact saturation and full-facet support. An independent numerical SLSQP optimization, carried out separately on 21 input instances in dimensions 4, 8, and 16, agreed within \(3.9\times10^{-13}\) squared-distance units; that numerical test is corroborative and not part of the self-contained exact checker.

Reproduce the exact checks using `python verify.py`. The finite checks do not prove the all-dimensional theorem; steps 1–5 of RESULT.md provide its proof. No independent audit or outside mathematical certification was performed. Publication priority is provisional.
