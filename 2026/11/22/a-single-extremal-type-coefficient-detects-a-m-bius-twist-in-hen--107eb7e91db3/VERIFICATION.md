---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For n≥4 both explicit seam choices give simple triangle-free cubic graphs. A pairwise intersecting triple of edges is a star or triangle, and four pairwise intersecting edges are impossible here. Thus L(G) is K₄-free and its triangles are exactly the three-edge stars. A neighborhood of a distinct new vertex is legal precisely when it omits at least one edge of each star. Universal finite extension and homogeneity realize each choice over the named parameters (arbitrarily many new mutually nonadjacent copies are possible), and quantifier elimination identifies the choice with a unique complete nonalgebraic type. Thus its nonneighbor set is an edge cover with the same weights. In the transfer, a chosen rung contributes v_i with no conditions; an absent rung requires both incoming/outgoing bit ORs to be true. Rail weights occur exactly once because they are counted at their outgoing column. The twisted seam swaps the final/initial bit pair, giving tr(BJ) instead of tr(B). Simultaneous row exchange commutes with each local matrix. Directly subtracting columns 01 and 10 gives (0,−u_i,u_i,0)ᵀ: all rung contributions cancel and the off-diagonal cover indicators give the indicated signs. Over the rational polynomial ring the invariant symmetric block cancels in the trace difference, and the antisymmetric line contributes 2 times the product of −u_i. This is therefore an identity over the integers as stated. The minimum cover degree is n and is attained by the all-rung matching; the only different coefficient is supported there. Reversal of degree by 3n gives the neighbor spectrum. The sign switches correctly with parity and no identification of individual types is needed.

## originality

PASS

The supported distinct part is the fully site-inhomogeneous twist cancellation with arbitrary rung and paired-rail activities, transferred to the complete one-type inventory. Do not assign novelty to the generic Henson extension principle, perfect-matching difference, finite census cases, or the all-homogeneous recurrence specialization. The arXiv identifier 1312.7506 is correct but the frozen reference uses a descriptive rather than canonical title; the source inspection gives the actual title.

## value

PASS

The stronger weighted invariant separates seam sensitivity from bulk type counts on two natural cubic ladder families. Arbitrary rung perturbations and independent columnwise rail-pair perturbations do not introduce any further difference: the twist only couples to one antisymmetric transfer mode. That is a useful complete enumeration statement, not a relabeling of the already-known two-unit perfect-matching difference or a finite table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
