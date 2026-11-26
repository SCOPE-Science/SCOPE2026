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

Expanding rank ≥3 from the empty mark requires an anchor u with both an edge and a nonedge partner of marked rank ≥1. In the triangle-free age a marked edge requires 00,10,01; a marked nonedge requires all four exterior traces. Conversely let a,b,c,d witness u-only, v-only, both and neither at a full nonedge uv. At the edge uc, a,v,b supply the three requisite traces: ac and bc are prohibited by triangles, and b is not adjacent to u. Thus one full nonedge suffices, including in a countable host. The witnesses force six distinct vertices and the four edges of a path on five of them. Equality in the edge bound leaves exactly that path plus isolates. On those six vertices only ab,ad,bd,cd are optional and only the triple ab,ad,bd is forbidden; there are 14 anchored templates. Independent exhaustive enumeration over all 32,768 labelled graphs, using neighborhood set differences/intersections and separately the edge/nonedge rank-one anchor test, gives 5,789 triangle-free graphs, the same 2,292 qualified by both criteria and nine orbits. Orbit sizes, stabilizers, canonical masks and CSV edge lists all agree. Since graphs below order six cannot qualify, the nine equal-order shapes are exactly the minimal induced obstructions within the age. Rank ≥1 is nonemptiness. Rank ≥2 is the existence of a vertex with a neighbor and a distinct nonneighbor, equivalent here to having an edge and a third vertex by triangle-freeness.

## originality

PASS

The supported contribution is the exterior-trace criterion for the full triangle-free age, the sharp extremum on that whole class, and its complete nine-element obstruction basis and census. Closely matched unrestricted-rank results use a different extension class; the linear-forest result does overlap with the extremum and criterion on a strict subclass, and that overlap is credited.

## value

PASS

The exact exterior-trace condition turns a recursive rank question into a local test that works even for countable hosts. It gives a small complete forbidden induced basis and explains why the triangle-free age has a strictly smaller onset than unrestricted graph rank. The exact finite census supports this classification rather than posing an arbitrary isolated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
