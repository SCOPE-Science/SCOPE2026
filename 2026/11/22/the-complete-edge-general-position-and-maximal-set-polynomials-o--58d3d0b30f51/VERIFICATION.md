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

The test is on subsets of the 32 distinguished edges, not on orbits. In an independent exact replay, a triple was forbidden precisely when some ordering and orientation of its three edges made 3 plus the two inter-edge Hamming distances equal the Hamming distance from the initial endpoint to the final endpoint. Equality is sufficient by concatenating shortest connecting segments and necessary by taking the corresponding subpaths of a witness geodesic. This reproduced 576 forbidden triples, including triples with an intervening non-selected edge. The cardinality-layer replay generated each candidate from its subset omitting the largest edge, and, above size 3, admitted it exactly when all immediate subsets were legal. A forbidden triple in such a candidate would survive some one-edge removal. Marking all parents of admitted children then identified exactly the nonfacets. This reproduced all 17 face coefficients, all facet coefficients, totals 610955 and 4686, and the six size-16 masks as precisely the two-coordinate-class unions. No larger layer exists. Additionally, transitivity gives 24 incidences per edge across the 192 undirected antipodal geodesics, so a legal 16-set must meet each in two. Comparing paths swapping two adjacent flips in a square, using both starting corners, forces opposite-edge indicators equal. Thus coordinate classes are constant, independently explaining the equality cases.

## originality

PASS

Pass for the complete labelled face/facet census, not for the classical maximum or as a priority claim for maximum-set rigidity. A distinct same-day catalogue statement would already cover the six maximum sets by specialization, if confirmed as catalogued. None of the examined statements enumerates nonmaximum feasible sets or facets by cardinality. The judgment is best of current knowledge, not historical priority certification.

## value

PASS

Q4 is the first cube with nonconsecutive triples on a geodesic. Its full face and facet counts quantify saturation beyond the known largest size: minimal facets of size six and gaps in the possible maximal cardinalities show precisely how nonpure this complex is. The finite exact polynomials are independently useful benchmarks for more general edge-geodesic and saturation enumerations; the claim is not merely the known upper bound in new notation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
