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

The binary determinant is one exactly on two distinct nonzero column symbols. Rank two requires at least two occupied nonzero symbol classes, so the zero concept is excluded, but the empty query support is shattered. The non-isolated complete bipartite or tripartite graph determines its partition up to color permutations, consistently giving 35, 155 and 651 concepts. Fixing the two terminals to different nonzero symbols realizes all four traces at each remaining vertex of K_{2,n−2} independently. The fresh enumeration tests each support's trace count, maximality by its one-edge extensions, and canonical orbit under all vertex permutations. It reproduces all polynomial coefficients, facet-size distributions (8,3), (15,12,10), (96,70,180,15) and the labeled orbits. The explicit edge lists confirm the graph descriptions: for example the seven-edge representative has paths 0–4–1, 0–5–1, 0–3–2–1. The exact augmented boundary ranks reproduce the nonzero reduced Betti numbers β₂=7 at n=4, β₃=5 and β₄=1 at n=5, and β₄=111 and β₅=24 at n=6. The table has 3, 4 and 6 distinct facet orbits on masks of lengths 6, 10 and 15, respectively. Maximum support size and nonpurity follow from these data; only the constructive lower bound extends to general n.

## originality

PASS

The classical Plücker representation and plane count are not novelty claims. The exact finite shattering complexes under pair-coordinate queries, including the orbit and reduced homology data, were not found as an independently stated or implied result in the inspected sources. The nearest Grassmann, finite-linear-action and coloring competitors change the Boolean query class in decisive ways.

## value

PASS

Binary two-plane coordinates provide a canonical finite Boolean class, and n=4 is the first ambient size with four-index Plücker constraints. The next two orders give a meaningful comparison of this same complex: the maximum faces have a uniform bipartite shape, but inclusion-maximal faces can have smaller sizes and different types. The exact reduced homology detects structure not recoverable from VC dimension or the number of concepts alone. These are reusable low-order benchmarks for structural questions, not an all-order pattern inferred from three cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
