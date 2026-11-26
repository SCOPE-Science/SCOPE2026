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

I reconstructed all sixteen complexes from the induced retained grid vertices. In the independent generator, the least available grid vertex is either unmatched or matched to one available neighbor; this gives every matching once. The two grid reflections give exactly (r,c) with r=0,1 and 0<=c<ceil(n/2). On the nonempty face posets I reconstructed the specified coreduction pairing and independently certified acyclicity by retirement times: a directed Hasse cycle would have to alternate up and down, since upward matched edges are disjoint and on a cycle the number of up and down steps is equal. After each upward matched edge, every available unmatched downward edge goes to a strictly earlier retired face. That precludes a cycle. Each case has one critical 0-cell and exactly the reported number of critical cells in one dimension d>=2. Forman's CW model then has only the point and d-cells, each attached to the point, proving the claimed wedge over the integers, not just mod-two homology. All table entries and totals 87,378 nonempty faces, 419,433 covers, and 43,636 pairs agreed; the unpunctured width-four comparison gives 9 spheres of dimension three.

## originality

PASS

The exact claim is a full width-4–6 graph-vertex-deletion profile. The closest inspected results classify the unmodified graphs, graph-edge deletions, or links associated with deleting two adjacent endpoints. None supplies the sixteen sphere-wedge types of this different operation.

## value

PASS

Graph-vertex deletion is the first site-defect operation, genuinely different from the studied edge defect. The natural thin-grid family now has comparable exact types at three successive widths, including a dimension drop at the middle-row width-four endpoint and five distinct multiplicities at width six. These give useful base cases for deletion, links and connectivity calculations. The actual homotopy type, not just a field Betti table, is determined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
