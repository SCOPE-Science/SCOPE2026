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

The field equation gives exactly the four open Cartesian neighbors. Distinct leaves must have distinct Boolean concepts and hence distinct centers, so depth three requires at least eight centers and depth four is impossible on eight. Each root branch on eight needs four centers, forcing the root's full four-neighbor set inside the same E. On each four-center branch the next query must split two against two, and each pair can be separated precisely when its two centers have different adjacency to some query in E. The published rooted reduction tests exactly binomial(20,3)=1140 candidates at a fixed root; translating then gives the rooted pairs. The independent replay scanned all 1,081,575 eight-sets directly, without the fixed-root translation reduction, finding 84 at the origin, 2,050 total and 2,100 rooted pairs (2,000 one-root sets and 50 two-root sets). It tested all static traces on triples and pairs as needed, yielding VC dimension exactly two on every winning set. An elementary ambient upper bound also holds: a shattered triple would share a common neighbor; three of the four neighbors of one vertex include an opposite pair, whose only common neighbor is that vertex, ruling out the trace consisting of that pair alone. The replay verified the exact representatives of the 200-map symmetry group (9 orbits of size 200, 2 of 100, 1 of 50) and all eight length-three paths of the supplied witness. Both queries and leaves are inside E throughout.

## originality

PASS

The static predicate and the general binary-tree cardinality bound are known; the distinct contribution is the exact self-restricted online minimizer classification in the pentagonal torus, including root multiplicities and the symmetry quotient. The closest same-predicate paper treats static VC and leaves small supports outside its size guarantees. The inspected online analogues are for other graph families or have ambient queries. No independent matching census was established; this is a bounded comparison, not a claim of absolute priority.

## value

PASS

The support size eight is forced by the leaf bound rather than chosen for computational convenience. Attainment in this symmetric degree-four graph is not automatic once queries and centers must share the support. The census identifies every minimal-size support achieving an adaptive depth not available statically, and the orbit and root counts distinguish essentially different witnesses and quantify where adaptation can start. This is a precise baseline for studying how graph symmetries and locality constrain online learning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
