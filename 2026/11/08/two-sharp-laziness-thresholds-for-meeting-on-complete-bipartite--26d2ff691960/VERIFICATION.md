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

# Verification and reproducibility

Run `python3 verify_meeting.py` with Python 3.9 or later. No third-party packages, input datasets, compiled extensions, or network access are required.

The checker directly builds the individual-walker lazy transition matrix on each \(K_{a,b}\), forms the synchronous two-particle dynamics on unordered distinct vertex pairs by combining both possible label assignments, treats diagonal meetings as absorbing, and solves the full rational absorbing-time system using exact Gauss–Jordan elimination. This is independent of the three-class reduction used in the mathematical proof. The tested graphs have \(1\le a,b\le4\) except \(K_{1,1}\), and five exact rational holding probabilities are used for each. Further tests check the rational difference identities and the threshold-sign boundaries for part sizes up to \(100\). The extracted checker printed `VERIFY_OK 31129 exact assertions` on replay.

**Scope of verification:** These are finite exact computations, not a proof of statements for arbitrarily large graphs. The all-size conclusion is provided by the explicit first-step recurrences, rational elimination, positivity of denominators, strict monotonicity of the comparison polynomials, and exact endpoint evaluations in `RESULT.md`.

**Unperformed:** No independent external mathematical audit, experimental confidence interval, or historical-priority certification is claimed.
