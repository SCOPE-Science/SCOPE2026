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

On the complete host, any clique containing an edge must vary that edge's unique coordinate, since two different changed coordinates would give nonadjacent placements. Fix the other k-1 tokens. If f sites are full, all n-f admissible settings form the unique maximal fibre of each of its edges. There are no singleton facets: a site with spare capacity can receive a token from elsewhere, or if all tokens occupy that site they can move to an empty one. The conditions 0≤k-1-sf≤(n-f)(s-1) and 0≤f≤n-2 give exactly L≤f≤U; each intermediate occupancy total is realizable. Choosing the moving token and saturated sites and counting the remaining labelled assignments by factorial denominators gives M_f. Placements give V, and each j-clique with j≥2 contributes in only one fibre, proving the full polynomial. Occupancy vectors can be reconciled by surplus-to-deficit moves. Labels can then be permuted by transpositions using a vacant slot at an endpoint or via a third site. The purported simultaneous deformation retraction is valid: on the barycentric subdivision of each facet, fix the original vertices and send every positive-dimensional face barycentre to the facet barycentre. The image of each chain simplex lies in one arm of the star, and the straight-line homotopy stays in the facet and fixes the star. Distinct facets meet at most at vertices, so these homotopies glue. The connected incidence graph has V+ΣM_f nodes and Σ(n-f)M_f edges, giving the claimed integral circle wedge. Purity is L=U: the two endpoints agree at k≤s and k=ns-1, and n=2 forces both to zero. In the remaining n≥3 range, if L=0 then floor((k-1)/s)≥1; if L>0 then L≤n-3 and k-1-s(L+1)=(s-1)(n-L)-s≥0, so U≥L+1. Inspected the finite NetworkX and coefficient checker verify_supertoken.py; the reported 45 instances were not rerun and the checker is not a homology proof. The excluded fully occupied graph is indeed discrete.

## originality

PASS

The model, common-coordinate lemma, largest clique and connectivity have clear prior coverage. The supported distinct claim is the full capacity-dependent facet spectrum, the simultaneous sharp purity boundary, and the explicit rank of the integral circle wedge. The gluing mechanism and unrestricted Hamming structure are standard and are not separate novelty claims.

## value

PASS

The maximal fibres measure all complete one-token reassignment opportunities, not just the largest one. Their exact multiplicities simultaneously resolve the pure and mixed-dimensional regimes and determine how many independent loops survive filling every clique. This separates two natural boundary regimes from the entire intermediate occupancy range and gives an all-parameter invariant of a previously defined graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
