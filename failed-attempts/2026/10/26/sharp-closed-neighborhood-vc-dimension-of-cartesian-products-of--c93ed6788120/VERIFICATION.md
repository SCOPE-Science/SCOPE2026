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

Shattering four points would put all four in one radius-one ball. A coordinate line has only full-line, singleton or empty intersections with such balls, so a shattered four-set must use more than one line through the all-positive center. There are then three arms across at least two coordinates. If two share a line, their common centers lie on that line and only the all-positive center also reaches the third. If three use different coordinates, the first two have exactly two common centers, and the third excludes the double-change center. Thus the three-arm proper trace is impossible. The binary-cube triple realizes all eight traces, including the empty one via a triple-coordinate change; fixing other coordinates preserves all distances. In a rectangle all-positive triples lie in a row/column cross; a collinear triple loses pair traces and an L loses the corner singleton. The remaining shape occupies two rows and three columns (up to transpose), so the empty trace forces one spare row and column. The explicit witnesses work at 3x4 and above, and the same-row pair works outside 2x2 whenever the formula needs dimension two. The one-coordinate and 2x2 degeneracies follow from constant and co-singleton concepts respectively.

## originality

FAIL

The distinct catalogue result 'Exact online neighborhood dimensions of mixed-alphabet Hamming graphs' tabulates the very same static closed-neighborhood VC dimension for every admissible product. The entries are there as established context, not the online theorem's novelty claim. The same two-coordinate classification is also contained in the stronger catalogue theorem on rectangular rook graph shattered supports. There is no distinct uncovered parameter case or quantitative invariant in the frozen finding. This establishes catalogue coverage at review time, not who obtained or published the result first.

## value

FAIL

The distinction between open and closed shattering and the rectangular cutoff are meaningful combinatorial facts. But this submittted exact classification supplies the already tabulated closed invariant, with no new parameter regime, strengthened theorem or separately motivated structural result beyond that classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
