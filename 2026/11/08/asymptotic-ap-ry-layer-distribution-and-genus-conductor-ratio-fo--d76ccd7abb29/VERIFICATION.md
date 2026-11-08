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

The attached standard-library Python script `artifacts/verify.py` exhaustively compared Apéry representatives computed by independent shortest-path search with minimum-square-summand counts and the closed three-branch height formula for 111 parameter values, including every integer from 3 through 100 and thirteen larger values through 2000. It checked 12,875 nonzero residue classes, their exact genera, the predicted Apéry heights outside the explicitly constructed exceptional set, and the elementary Frobenius upper bound. The expected terminal print is `VERIFY_OK` with totals.

These finite checks are not a substitute for proving the all-parameter formulas or the asymptotic density theorem. The latter rests on Lagrange's and Legendre's theorems, Landau's two-square density bound, and the explicit counting argument given in the result. There has been no independent mathematical audit or certification.
