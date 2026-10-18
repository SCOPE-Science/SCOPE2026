---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed all 40 tetrads from exact frozen verify.py; independent Python enumerator found 11 vertices, 51 edges, 80 faces, 40 facets, missing only four edges (7,11)...(10,11), 135 graph 3-cliques and exactly 55 nonfacial cliques. Exact mod-two boundary rank 40 and graph-cycle dimension 41 gives H1(F2)=F2; all 55 nonfacial triangle cycles reduce to the nonzero class. Exact Smith normal form on integral 41-cotree-edge by 80 facial boundaries gives index 2, hence H1(Z)=Z/2. Exhaustive 6!*4!=17,280 degree-block automorphism candidates yield precisely 48 facet-preservers, vertex orbit sizes 6,4,1 and five triangle orbits 3,4,12,12,24. Since simple graph loops have at least 3 edges, all 55 are shortest. These are exact finite exhaustive checks, not extrapolation.

## originality

FAIL

REJECTED AS COVERED. The complete previously published Resultary RESULT.md for the IDENTICAL forty-facet Lutz/Walkup 11-vertex RP3 complex states exactly 55 missing triangular cycles all detect the unique nonzero mod-two H1 class and splits them under the same 48 automorphisms into orbit sizes 3,4,12,12,24. Since the independent exact integer homology calculation and known RP3 topology give H1(Z)=Z/2, each of those same 55 mod-two-nonzero triangles is necessarily the unique nonzero integral torsion class. The prior additionally proves a strictly stronger induced-subcomplex homology support theorem for all 2048 subsets. The purported novelty of integral systole census and orbit split is therefore merely a same-object corollary, no different numerical wording saves originality.

## value

FAIL

The 55-triangle count and five exact group orbits would be a natural finite combinatorial H1 systolic invariant of the canonical minimal RP3 triangulation; however the exact same natural fact and its stronger induced-subcomplex generalization are already in the previously published same-object table. A known-table recomputation and mod-two-to-integral restatement is not an independently valuable new finding. V FAIL despite exact reproducible computation and a good underlying mathematical object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
