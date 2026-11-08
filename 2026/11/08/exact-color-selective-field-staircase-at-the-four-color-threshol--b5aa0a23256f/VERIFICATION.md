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

# Reproduction

Compile and execute the two embedded independent C++17 programs (`ico_q4_check_a.cpp`, `ico_q4_check_b.cpp`) with `g++ -O3 -std=c++17`. Both are self-contained and assert all thirteen constrained minimizing penalties and counts. The first visits every spin vector recursively using thirty explicitly listed edges; the second enumerates all two-bit packed configurations using a geometric two-pentagon graph description. Both report PASS on all \(16,777,216\) assignments. These programs were compiled and executed against the actual package-source bytes before embedding.

The graph descriptions were independently checked to be isomorphic. Finite exhaustive enumeration is exhaustive here because there are exactly \(4^{12}\) labeled states; it is not a proof about any other graph order. Intersections of the thirteen lines were checked with exact rational arithmetic; numerical approximation is not used.
