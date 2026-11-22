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

Geodesic triple criterion shows a face is wholly in one part or selects at most one vertex from each part, hence join B=D1*...*Dr with separate filled part simplices attached along their discrete vertices. Cofibration homotopy pushouts append a_i−1 one-cells per part, and join of discrete spaces produces Π(a_i−1) spheres S^(r−1). Relative chain LES for (GP,B) identifies H1 as ⊕I_i for r>=3 while join orientation swaps two reduced degree-zero factors by −1, giving the full part-permutation twist. r=2 requires separate pair with the two disjoint shore simplices, giving augmentation kernel on cross edges and sign on shore exchanges. Independently enumerated all faces for size profiles (2,2,2), (1,3,2), (2,3), obtaining 30,29,17 faces including empty. Finite checks do not prove integral or all-rank cases.

## originality

PASS

Rather 2026 exactly proves the general-position FACE characterization and counting polynomial, which is expressly excluded from the novelty assertion. The topological homotopy and integral full-automorphism module are additional. The highly relevant Resultary clique-bouquet geodesic-avoidance complex instead has one central cone, first Betti N−1 rather than Σ(a_i−1)=N−r and no equivalent integral action; multipartite induced-forest results use different face predicates.

## value

PASS

A natural geodesic complex gains a complete integrally equivariant classification, detecting mixed-dimensional topology, essential sign twists under equal-part permutation, and the r=2 lattice that does not generally split integrally. These are useful structural invariants not encoded in the previously known scalar face polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
