---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Using exactly the supplied 11-vertex 18-edge Herschel adjacency, independently computed all 11-by-11 shortest-path distances, yielding diameter four, triangle-free graph and scale-1 cycle rank 18-11+1=8. The complete 2^11 nonempty subset enumeration gives scale counts 11,29,178,1535,2047 at integer distances 0..4 and scale-two f=(11,42,69,46,9,1). Independent replay of pivots (9,4,0,10,3,7,2,1,8,5,6) yields 88 pairs and critical 0/3-cells; all 526 covers topologically sort, proving X2≃S3 integrally. An independent exhaustive free-face procedure legally performs 767 elementary simplicial collapses of X3 to vertex {0}; at scale four the full simplex is contractible. All 12 S3×C2 graph automorphisms were constructed and the signed simplex Lefschetz traces agree with sgn(S3)⊗epsilon(C2). Rank-one integral top homology forces degrees ±1; the all-field reduced barcode consists of ten [0,1) in H0, eight [1,2) in H1 and one [2,3) in H3.

## originality

PASS

Targeted searches for Herschel graph Rips, Herschel distance-two clique complex and its sign character found no earlier equivalent result besides the exact assigned record. Older Herschel independence/matching/cut classifications concern different simplex predicates; other named graph Rips classifications have different metrics/graphs and no universal implication. Adamaszek (arXiv:1104.0433), inspected primary PDF, analyzes powers and clique complexes under girth/forbidden-cycle restrictions and named families; Herschel has four-cycles (e.g. 0-5-1-6-0), failing relevant girth restrictions. Its general graph-power perspective does not determine this 11-vertex finite computation or its orientation. Best-of-knowledge with unindexed risk.

## value

PASS

The smallest non-Hamiltonian polyhedral graph is a natural graph-metric test case. Its shift from a wedge of eight loops to an integral three-sphere at r=2, collapse at r=3, and nontrivial full symmetry orientation are motivated exact filtration invariants, useful for graph-power and persistent equivariant topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
