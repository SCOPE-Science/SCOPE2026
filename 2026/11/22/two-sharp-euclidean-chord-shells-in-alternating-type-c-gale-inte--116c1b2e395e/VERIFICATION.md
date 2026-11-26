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

In the native 0/1 embedding, reversing a vertex and coding 0 as +1 converts every suffix constraint into the lower barrier −1 (parity makes the even-time bound 0). Reflection of the walk started at height 1 telescopes to C(2r,r)+C(2r,r+1)=C(2r+1,r); zero and the unit vectors witness full dimension. Distance squared equals Hamming distance at the vertices. At full distance the heights are opposite and forced to zero at all even times: each block has two orientations, and division by two gives the complementary matching. Any nonvertex is excluded as a diameter endpoint by the strict convexity of squared distance, with the other endpoint fixed. A sole agreement on bit 1 would force both heights to −1, precluding a subsequent step, and the last step cannot be such an agreement from opposite odd heights. An agreement on bit 0 leaves first-coordinate walk states −1 through 3; on states 0,2 the two-step transition has row sum 3. The odd agreement times give 2(3^r−2^r) ordered pairs in total and even times give the same, so the unordered result is 2(3^r−2^r). No claim of a gap between lengths of arbitrary segments in the continuous polytope is made by the vertex-shell result. Fresh exact enumeration at r=1,…,6 reproduced the counts and endpoint patterns; replay `python3 /workspace/branches/independent_certificates.py 1`. The enumeration corroborates, not replaces, the all-r argument.

## originality

PASS

The bounded comparison supports the distinct two-shell enumeration on the specified alternating Gale interval. The reflection-based vertex count and general Gale description are not novel. The closest distinct paired-transfer and alternating-spectrum records have substantive, demonstrated scope differences, not just different titles or publication dates.

## value

PASS

The alternating pattern gives a uniform natural family with the simplest periodic Gale boundary. The ambient diameter alone would miss the exponentially larger penultimate shell and the complete matching/isolated-vertex structure at the diameter. The explicit shell ratio and classification give useful extremal metric information for this family; it is not just a routine tally of vertices or another presentation of the linked-snake result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
