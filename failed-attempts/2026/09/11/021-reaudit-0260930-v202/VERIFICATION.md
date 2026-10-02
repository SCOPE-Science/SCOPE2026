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

Fresh monotone-triangle enumeration independently produced 218348 order-7 ASMs, 2630 diagonally symmetric ASMs and exactly 116 nonzero joint cells. The independently regenerated inversion and minus-one marginals match the committed table, including the unique maximum-minus-one cell. The committed generalized Pfaffian polynomial has total coefficient sum 2630 and projects to the same joint table under the stated statistic relations. The finite census is therefore correct.

## originality

FAIL

Originality fails because the central joint table is mechanically implied by the published generalized DSASM generating function. The checked paper defines the relevant inversion/statistic refinement and Theorem 20 gives a Pfaffian formula for the generalized generating function at the specialization used here; evaluating it at order 7 and projecting variables is a finite specialization, even if the 116-cell table is not printed.

## value

FAIL

As a numerical benchmark the table is reproducible, but under the required value bar it is a known-formula recomputation: the exact coefficients are mechanically obtainable from the published all-order generalized generating function. The classical Pfaffian reduction lemma is also expressly pre-existing. No separate structural theorem, unexpected boundary, or mathematically motivated unknown invariant survives beyond evaluating the known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
