---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Fresh Fraction arithmetic reproduces denominator positivity with minimum approximately \(0.8848140675\), alternating signs on all 11 ordered nodes, and minimum error magnitude approximately \(0.0290874739\). If a competing type-\((4,4)\) rational had uniform error below \(0.025\), the cross-multiplied difference numerator (degree at most 8) would change sign across at least 9 consecutive intervals, forcing more real zeros than its degree; this independently reconstructs the lower-bound proof rather than relying on the saved verifier.

## originality

PASS

No searched source states this two-cusp type-\((4,4)\) threshold or a stronger result that mechanically implies it.

## value

FAIL

The surviving statement is a one-off inequality against the externally chosen cutoff \(0.02\) for one low type and one shifted two-cusp function. The record does not establish an exact minimax value, a structural family, a sharp degree boundary, or an externally motivated use for precisely this cutoff. Under the stated value bar, correctness and novelty of this finite certificate alone do not make the narrow threshold decision mathematically worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
