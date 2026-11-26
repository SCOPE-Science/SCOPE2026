---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both classifications are correct for the stated tensor product and all integer r≥3. In diameter two the only forbidden triple is an induced two-edge path. If a valid set repeats a row, any outside point must use one of the columns of that pair. An outside point then excludes a third point in the repeated row and excludes a second outside row. The column case is symmetric; with neither repetition the set is a partial permutation. This independently recovers the coefficient formula including the 3/4-point rectangles. The initial segment through b_4 or b_5 is unimodal: the last early differences switch from negative to positive at r=9 for width four, and at r=6 and r=10 for width five. The tail junction differences are 4(r−39) binom(r,4)/5−6 binom(r,2)−r and 5(r−155) binom(r,5)/6−r, respectively. Each is negative up to its junction cutoff and positive from the next integer: at and above 40 use binom(r,4)/binom(r,2)≥38·37/12, and at and above 156 use binom(r,5)≥2r. The following pure-binomial slope is positive exactly from r=12 or r=14, respectively. Equality at r=11 or 13 creates no rise, and absent tail terms do not create a peak. Independent shortest-path subset enumeration on the five packaged graph sizes and exact coefficient checks for both widths through r=500 agree; the inequalities, not the finite replay, prove the unbounded cases.

## originality

FAIL

The two advertised sharp windows do not constitute a distinct finding. The distinct same-day Resultary record 725a303a7d95 already states precisely the width-four window for the identical adjacency and weak unimodality definition, even allowing r=1,2. This is exact coverage, not a determination of priority between the two same-day records. The earlier Resultary theorem ff0919bdb467 specializes at a=5 to the entire nonunimodal window 14≤r≤155 and sharp re-entry at 156. Only the finite unimodal range 3≤r≤13 at width five lies outside those two cited covers, and it is directly checked from Rather's previously known coefficient formula. The originally advertised novelty of both windows is therefore not established.

## value

FAIL

The re-entrant boundaries would meaningfully address the published parameter question if distinct. As submitted, the two advertised contributions are covered and the only uncovered piece identified is a direct eleven-case substitution in the established coefficients. That residual check does not supply a separate motivated structural result or useful new boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
