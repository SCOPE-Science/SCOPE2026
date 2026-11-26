---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A concurrent triple of lines leaves the other three points of the fourth line through the concurrency point. A nonconcurrent triple leaves a four-arc: a collinear triple in the complement would force the three hypothesis lines to meet its carrier at the fourth point. Conversely, each collinear triple determines its three concurrent lines, and each arc has exactly 13−6−4=3 exterior lines whose union covers its entire nine-point complement. These complements are an antichain and every shattered set must be contained in one, by the empty trace. Each maximal candidate is itself shattered: for an arc, its secants and tangents realize traces by at most two lines and can be padded with distinct exterior lines; for a collinear triple, use separate off-carrier lines for proper nonempty traces and the carrier for the full trace, padding by unused lines through the fourth point. All noncollinear triples extend by choosing a point off their three secants; all smaller sets extend to triples. The 715 four-sets include exactly 13·(4·9+1)=481 nonarcs, counted uniquely by their carrier, hence 234 arcs. Independently built the plane from a 3×3 affine grid and its four ideal points, exhausted all 8192 supports for each of the exact-two and exact-three families, and verified the complement–facet bijection. Exact two has 702 shattered four-sets (every four-set except a whole line), and no larger ones. Here ‘noncollinear four-set’ means not wholly collinear, not no collinear triple. Frozen scripts and logs were inspected but not executed.

## originality

PASS

Pass for the exact-three-distinct-line support classification and nonpure complement–facet duality, not for the standard projective arc and collinear-triple counts. The 702 four-set number is shared with nearby older or same-day families and not the basis for originality.

## value

PASS

The exact static shattering complex distinguishes two maximal support geometries in a canonical finite plane. The complement bijection is a useful explicit structural description of the concepts as well as of the traces, and the lost 468 four-faces demonstrate that exact distinct-line budgets can alter the support complex even without changing VC dimension. This is more than a recomputation of arc counts or a dimension bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
