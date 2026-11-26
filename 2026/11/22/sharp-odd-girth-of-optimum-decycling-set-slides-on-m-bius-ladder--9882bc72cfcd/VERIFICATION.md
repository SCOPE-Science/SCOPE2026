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

For n=2m the surviving-forest edge count gives 2|S|>=n+1+e(S), so m+1 is the lower bound and a set of that size can contain at most one selected edge. Adjacent empty columns leave a square. Conversely, at size m+1 the number of empty columns is m-1 plus the number of doubles. A double cuts the strip and the no-adjacent-empties condition leaves at most one edge across each internal cut, ruling out cycles. Without doubles there are exactly two singleton-to-singleton boundaries. Any cycle must cross every boundary, since removing an uncrossed boundary again makes a strip with at most one edge per internal cut. Its use of both singleton-to-singleton boundaries would force two corresponding selected edges, including at a twisted boundary, a contradiction. In the forward wave the selected a-indices are an even prefix and an odd suffix, with at most one ordinary selected edge where they meet; the b token and the twisted seam create no extra edge. The reverse wave has an odd prefix and even suffix and the same bound. At the all-a transition only the internal 0–1 edge is selected; the subsequent double is isolated from other selections. The holes are separated in these waves and at the transitions. The forward and reverse waves are distinguished by the selected b vertex, with column-index sum strictly decreasing within each; the all-a state and double state are separate and the initial state is distinct from reverse intermediates because it contains a_0. This includes n=4 with empty wave ranges. Therefore the n+1 slides are legal, minimum, and form a simple cycle. Any closed slide walk induces a balanced directed edge multiset on the host, so an odd walk contains an odd host cycle no longer than the walk. In the even host an odd closed walk uses an odd number of antipodal jumps and needs at least n unit steps modulo 2n. For odd n every host edge reverses residue parity, so the parity of the number of selected even vertices bipartitions the slide graph. Independent leaf-peeling enumeration and all-root BFS reproduce odd girths infinity,5,infinity,7,infinity,9,infinity for n=3 through 9, not used as an infinite proof.

## originality

PASS

The distinct result is attainment of the host odd-girth bound under minimum feedback-set feasibility, uniformly for every even Möbius ladder. Bipartiteness in the odd case and the host obstruction are generic, not independent novelty. No inspected match supplies the feasible attaining cycle or an equivalent theorem. Exact-family feedback-number and FVS reconfiguration full-text access limits make the verdict best-of-knowledge.

## value

PASS

On a canonical infinite cubic ladder family, odd girth measures the shortest parity-breaking closed relocation with every intermediate placement optimum. A host obstruction need not be sharp after restricting feasible states. The all-even-order attaining construction proves that optimal decycling does not raise the parity-breaking length here, a structural result useful in comparing local configuration graphs to their hosts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
