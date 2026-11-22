---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

At t=0 all mixed faces are crossing edges between two full shore simplices, yielding ab−1 circles. For t>=1 direct induced-degree case split gives two shore simplices, hub cone u*(simplex B0 * discrete B1), mixed edges and unique triangles (u,x,z) for x∈A\{u}, z∈faulted B0. Each edge {x,z} has only that triangle coface, giving (a−1)t legal elementary collapses. The remainder is a contractible connected core (gluing along nonempty contractible intersections) plus precisely (a−1)(b−t) extra one-cells, with integral cycle basis c_{x,y}. These cycles existed in earlier stages and the new triangles kill only specified basis elements, proving split surjection and primitive kernels. Independently direct induced-degree enumeration for (a,b)=(3,4),(4,4) at all 0<=t<=b recovered the explicit face families. Mod-2 tests do not replace CW proof.

## originality

PASS

Carnero Bravo 2023 proves the intact biclique Ind_2 homotopy, a credited boundary case. Published 2026-11-17 matching-deletion persistence treats t pairwise disjoint missing edges and can create S2 at t>=3; for this hub-clustered deletion no S2 appears and the ranks differ. Other star-deficient biclique robust clique complexes use k>=4 and do not imply the k=2 dissociation conclusion. The complete clustered-fault integral homotopy/persistence statement is not known from inspected prior work.

## value

PASS

Comparing clustered versus disjoint edge faults in a natural higher-independence invariant identifies sharp destruction of all cycles without higher-dimensional births, gives explicit integral filtration maps and symmetric-group lattices, and resolves a motivated fault-shape dependence rather than an arbitrary tiny case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
