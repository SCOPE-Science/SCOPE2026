---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Franklin graph is the twelve-vertex [5,-5]^6 cubic graph with 18 edges. The total 4-cut face predicate is: complement contains an independent 4-set. Fresh independent enumeration finds exactly 45 independent 4-sets and 2,533 augmented faces with f-vector (1,12,66,220,495,792,638,264,45). The record greedy vertex order yields 1,245 matched face pairs and 43 unmatched 4-dimensional faces, and a complete directed Hasse topological sort verifies acyclicity; after empty-face removal Forman gives a wedge of 43 S4. Independently enumerated all 48 graph automorphisms and signed invariant-face Lefschetz sums, reproducing the rational character trace multiset (43:1,5:3,-1:9,-7:6,-5:6,1:23) and zero invariant rank. Purity dimension 7 with H4 !=0 precludes pure shellability.

## originality

PASS

Best-knowledge: the inspected total-cut primary literature gives general definitions and chordal/cycle/grid, multipartite, path and Cartesian graph families, not the Franklin graph with the exact four-cut parameter. Resultary semantic searches returned Franklin ordinary matching, two-independence, domination and Rips results, but not an earlier four-cut homotopy/48-element character. Different Franklin graph complexes cannot imply this exact invariant merely through shared graph symmetry.

## value

PASS

The Franklin graph is a standard symmetric cubic graph and total four-cut complexes are a natural member of the graph-cut filtration. The exact integral homotopy 43 S4, strict non-shellability in a pure 7-dimensional complex, and full 48-element rational symmetry character provide precise, nontrivial invariants of a canonical finite object that are not mechanically implied by prior k=2 or nearby-graph calculations. Such exact equivariant data are independently useful without an infinite graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
