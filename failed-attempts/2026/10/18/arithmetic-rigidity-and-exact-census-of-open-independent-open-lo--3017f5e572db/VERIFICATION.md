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

Open domination plus open independence forces each selected vertex to have one selected neighbor, and distinct matching components share neither row nor column. Two empty lines on the same side duplicate signatures; an empty row in the presence of a horizontal edge gives the singleton of that edge's endpoint twice (and dually for columns). This forces the three occupancy regimes. Conversely a mixed-board unselected signature has horizontal/vertical counts (3,0), (2,2), (1,1) or (0,3); the pure triple contains a unique matched pair and a singleton, and in mixed signatures the vertex types identify which pieces encode row and column. All are nonempty, injective and nonsingleton, whereas the selected signatures are distinct singletons. In a pure case the optional empty column (row) produces distinct pairs. The mixed allocation has m!n! ordered choices and symmetry factor 2^(h+v)h!v!; the pure allocation has n!/2^m or its transpose, including the choice of the optional empty line. The square-board specialization and exclusion of m=1 or n=1 are consistent.

## originality

FAIL

The full finding is already covered in the compared published catalogue: the distinct rectangular-rook record gives an equivalent iff theorem and the same counts and sizes, not just the same graph family. The complete-multipartite record also gives a direct stronger coverage relation and explicitly identifies the bipartite classification as previously established. The FAIL is for lack of a distinct scientific claim relative to the compared corpus. The matching entries carry later archive dates; the comparison is not a finding of earlier independent discovery, copying, or lack of priority for the assigned record at its own release. The earlier primary sources inspected do not establish that historical proposition.

## value

PASS

As a mathematical result, the full classification of a natural all-vertex open-code notion on a canonical product is useful. The general selected-edge necessity does not prove sufficiency in graphs with triangles and four-cycles; here the signature profiles resolve that obstacle and give both the existence obstruction and the exact labeled family. This judges the substance of the theorem, not distinctness from the equivalent coverage recorded under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
