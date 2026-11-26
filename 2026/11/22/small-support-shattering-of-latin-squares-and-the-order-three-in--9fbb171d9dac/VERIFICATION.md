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

For all n>=2, compatibility is necessary by the all-positive trace. For a compatible k-support, all specified cells are distinct. Insert positives, then insert an alternative symbol at each negative cell: at most k-1 earlier entries ban symbols in the relevant row or column and the query bans at most one more. For k<=n-1 a choice always remains. The resulting k-entry partial Latin square satisfies Smetaniuk's completion theorem (Evans conjecture), so realizes the trace. A compatible full row has an impossible pattern of n-1 positives and one negative, proving sharpness as an existential obstruction. For n=3 there are 6 first rows and two derangements for the second row, with the third forced. Each point occurs four times. Two compatible points occur together twice when they share one coordinate, and once when they share none, by normalizing labels and checking these row choices. On a shattered triple the seven nonempty traces exhaust its twelve positive incidences, so each occurs once; all three pairs must share a coordinate and these equalities cannot all lie in one fibre, which would give two all-positive traces. Conversely the normalized Latin triangle {(0,0,0),(0,1,1),(1,0,1)} has one all-positive trace, and its pair and singleton incidence counts give all other traces. There are 24 such triangles through a point, and every edge sharing a coordinate lies in one. No size-four support fits 16 traces into 12 squares. An independently written enumeration of the 12 squares, all supports through size four, maximal edges, and binary incidence columns was run; replay: python3 /workspace/branches/01c403cf-fb9f-414f-ba95-94fbc1a9fafc/latin_independent.py. It returns (1,27,270,216,0), 108 maximal edges, 216 triangles, rank(partial_2)=133 and a connected one-skeleton. Thus rank(partial_1)=26, giving reduced Betti numbers 111 and 83 over F2 and zero in other degrees. No integral homology claim is established or asserted. Both frozen checkers were inspected, not executed.

## originality

PASS

Credit the uniform sharp signed-trace criterion and the exact Latin-square shattering complex, not the completion theorem, the concept class, or the ternary triangle boundary calculation as a freestanding new invariant. The strongest indexed overlap, the antipodal-sphere complex, has exactly the same triangles and boundary rank, as follows from comparing the two concepts mathematically. It does not give the Latin-square shattering theorem or its specific edge and facet classifications. The original finding is the classification for the Latin-square concept class; the homology figures are valid consequences with the overlap credited, not the basis for the originality pass.

## value

PASS

The uniform sharp cutoff distinguishes when arbitrary negative prescriptions are as feasible as positive partial completion. The exact first nontrivial boundary describes which compatible triples survive and which lower-dimensional facets cannot extend. This provides a useful finite model for the established shattering class; the transferred boundary rank by itself is not the value justification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
