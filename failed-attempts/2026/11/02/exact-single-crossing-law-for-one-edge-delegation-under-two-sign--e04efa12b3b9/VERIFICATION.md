---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditional on state s, only disagreeing donor/recipient votes can change the weighted majority. A creation of correctness requires (X,Y,S)=(0,1,h−1); a loss requires (1,0,h). Independence and the two equal adjacent binomial coefficients yield the stated Aₛrₛ^(h−1) factor; the odds comparison follows by dividing by positive denominators. Averaging uses fixed prior weights. Dividing the result by the positive binomial coefficient and the larger base to the power h−1 gives a constant plus one monotone exponential. This proves the sign law, including equal bases, zero coefficients and an integer transition with a zero. The quoted witness gains and inequalities check by exact rational evaluation; in both witnesses vₛ>uₛ>1/2. A separate ballot enumeration agrees in 108 exact statewise comparisons for h=1–4 (/workspace/branches/frozen_math_replay.py, argument 3); the uploaded script was inspected, not executed. The theorem is for a fixed edge chosen before the signal and fixed parameters as population size varies.

## originality

FAIL

Resultary 6a41be4f4ced explicitly states the identical two-state one-edge formula, statewise odds test and single crossing in electorate size, including its equal-base and dominant-base cases. It also gives a strict-better-recipient harmful-to-helpful example and a real crossing location. The frozen helpful-to-harmful witness is a different example, but the possibility follows routinely from the identical two-exponential formula and the attainable signs of its coefficients; it is not a new crossing law. The Gilbert et al. literature comparison verifies framework overlap independently, but the direct determination here is the equivalent indexed finding. No claim about authorship or historical provenance follows from the comparison.

## value

FAIL

The one-edge gain law is useful, but its submitted incremental content is an additional numerical reversal witness in the same class. The known law gives the opposite direction at once by the coefficient signs and prior choice; the new numbers do not establish a separate boundary, regime, or independent invariant. No genuinely valuable repaired remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
