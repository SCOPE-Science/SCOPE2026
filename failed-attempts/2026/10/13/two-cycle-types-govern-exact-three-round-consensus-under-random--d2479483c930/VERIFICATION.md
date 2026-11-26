---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Each round at most doubles row support, so three rounds are necessary. A second-layer support of size two, caused by a shared edge, cannot participate in success: even the union with a size-four support is too small. Otherwise each second-layer row has four coefficients 1/4, and the last layer succeeds exactly by pairing complementary supports. Contracting the four first-layer pairs gives a loopless 2-regular multigraph. The doubled-pair case has 3 partitions times 2² ways to attach endpoints; the simple-cycle case has 3 cycles times 2⁴ ways, giving 12 and 48, leaving 45 overlaps among 105 matchings. The respective complement graphs on original vertices are K4,4 and a disjoint pair of K2,2, giving 24 and 4 final matching choices. Thus 480 of 11025 pairs complete any fixed first matching, and the quotient is 32/735. Reviewed the frozen verification notes and integer path-count verify.py; the support argument covers the full finite sample space without a new execution.

## originality

FAIL

A distinct indexed Resultary finding classifying shortest eight-agent consensus edge topologies explicitly enumerates the same reduced three-perfect-matching sample space: fixed first matching, 12 and 48 admissible second matchings by cycle type, complementary four-element supports as the exact completion criterion, and 480 ordered completions. Its enumeration and complement test cover the probability and mechanically give the per-type refinements. That record is later-dated: this is evidence of equivalent indexed coverage, not evidence of chronological priority over the frozen record.

## value

FAIL

For shortest schedules under the natural uniform law, the conditional probability and sixfold contrast would be meaningful exact facts. With the complete matching-layer census and complementary-support test already indexed, the remaining probability normalization and two small factorial counts add no independently useful unknown invariant. The analytic exposition is valid, but uses the same support classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
