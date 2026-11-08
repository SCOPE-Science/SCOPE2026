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

The theorem's covariance is derived from conditional expectations given an individual source vertex, separately for the two sides of the biclique. Strict concavity, rational supporting tangents for the finite small cases, and a monotone rational witness establish the global sign classification without appeal to finite enumeration.

Run `python3 check.py` alongside this file. The standalone checker exhaustively enumerates every orientation for \(2\le b\le7\) and nine rational probabilities, using exact integer and rational arithmetic. It independently computes source counts and directed two-step-path counts for each orientation, then checks the moment identity. Additional checks verify the rational small-case certificates and positive witness. The script reports 645 assertions/checks.

The finite checker does not prove results for all \(b\). Exact analytic differentiation and endpoint arguments are essential, and the roots are not asserted to be rational. Prior-work inspection was limited to the identified primary articles and searches; absence of an explicit competing statement is not a proof of historical novelty. Independent audit: not performed.
