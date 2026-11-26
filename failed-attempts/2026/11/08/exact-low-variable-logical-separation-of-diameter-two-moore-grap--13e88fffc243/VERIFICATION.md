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

In the ordinary two-pebble game, one stationary vertex needs only equality, a distinct neighbor, and a distinct nonneighbor, all available. With two distinct stationary vertices, subtracting the endpoints and taking the neighborhood intersection (0 for an edge and 1 for a nonedge) gives the four extension counts in the proof. Their supports are identical for all degrees at least three. A lifted third pebble leaves precisely those two anchors, so the response extends the partial isomorphism after every move, without a quantifier-rank bound. C5 has no independent triple; three neighbors of a vertex give one in every higher-degree graph. In the four-variable formula the common-neighbor and domination clauses reuse the fourth name in disjoint scopes. A centered independent triple has 3d−2 neighbors in its union, leaving d(d−3) vertices outside the triple with no neighbor in it. This is zero exactly at d=3 in the range d≥3. The upper and lower width bounds follow, with degree 57 strictly conditional.

## originality

FAIL

The earlier Moore-graph rank-four record 06adb273d86e already gives both separating sentences, the same centered-triple count, and the complete one- and two-anchor adjacency/equality extension data. Its rank-four equivalence theorem alone is not the same as unrestricted-rank three-variable equivalence. But the exact pair-extension paragraphs in its proof already supply the repeatable invariant for the ordinary three-pebble game. The standard game theorem converts that invariant directly to the asserted unrestricted-depth lower bounds. Thus the full width classification is mechanically implied by the earlier proof data and existing finite-variable logic, rather than merely resembling a result with different quantifiers.

## value

FAIL

C5, Petersen and Hoffman–Singleton are natural logical benchmarks, but the asserted sharp widths add only a direct reusable-pebble reading of published extension data plus the same published separators. Neither the finite replay nor recasting the proof as an unbounded-round strategy yields a further independent invariant under this scope. In particular, the record does not analyze the four-variable comparison of degrees 7 and 57.

The dated certificate retains the supplied scientific assessment, sources and limitations.
