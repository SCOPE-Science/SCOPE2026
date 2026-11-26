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

Take the universal homogeneous limit of the finite I_3-free oriented digraphs, as specified in the assumptions. Its strong amalgamation is obtained by inserting arcs between the two new sides, so no independent triple can span both. Each admissible finite diagram is realized, and homogeneity identifies diagrams with complete types over pointwise named parameters. The nonarcs among new vertices form a triangle-free graph H. For any named base vertex, its nonneighbors must form an independent set in H, with two orientations for each remaining pair. A triple with at least two base vertices already has a tournament arc, so there are no other restrictions and the product W(H)^n is exact, even at n=0. Counts on no edges, one edge, adjacent edge pairs and disjoint edge pairs give the four bases. A triangle-free graph with at least three edges contains a three-edge star, path, path plus edge, or matching; all four have weights strictly below the two-disjoint-edge bound at the same arity. Every extra edge strictly lowers W. Dividing by the edgeless term as leading denominator gives the rare-nonarc exponent, since (8/9)^2<22/27; dividing the multiple-nonarc mass by the single-nonarc leading term gives the 11/12 conditional rate. For r=2 the conditional event is exact, not an asymptotic claim. All growth comparisons are at fixed r.

## originality

PASS

The supported distinct finding is the exact all-arity fixed-tournament-base spectrum together with its successive weight layers and local nonarc probabilities. This uses known structural facts and the standard hard-core polynomial; the prior global enumeration even contains the eight-choice local mechanism for a specified nonarc pair.

## value

PASS

A pointwise named tournament is a natural finite base because no forbidden independent triple can contain two base points. The exact ordered extension spectrum is an intrinsic orbit-count statistic. The hard-core reduction separates base size from new arity, and its sharp hierarchy explains quantitatively why a nonarc is rare and usually unique when present, facts not supplied by an unconditioned bitournament asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
