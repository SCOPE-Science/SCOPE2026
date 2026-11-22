---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The zero-diagonal permutation polytope is a Birkhoff face, so an edge corresponds to a single relative k-cycle, k>=2, and Frobenius squared length equals 2k. For fixed support S the simultaneous fixed-point prohibitions for pi and pi∘tau form a forbidden 2k-cycle together with n-k isolated rook cells. Inclusion-exclusion with c_{k,t}=2k/(2k-t) binom(2k-t,t) counts allowed derangements, and ordered endpoints are divided by exactly two. For fixed deficit j=n-k, forbidden hits converge in factorial moments to Poisson(2), giving a_n,n-j/n!→e^-2, while factorial tails justify summing over j. The separate two-derangement agreement count tends to Poisson(1), and countable-state truncation gives total variation. Independently enumerated each unordered vertex pair and checked exact rook-polynomial E_n,k classes for n=3,4,5,6, obtaining total edges 1,30,706,20770. The asymptotics are proved by bounds, not by enumeration.

## originality

PASS

The single alternating-cycle adjacency criterion and rook count of a generic cycle are classical; the claimed new results are their combination with two derangement constraints to obtain every length multiplicity, followed by distribution and total-variation asymptotics.

## value

PASS

The one-skeleton metric length census of the natural crown-graph perfect-matching face is an exact enumerative invariant, and the limit contrast is mathematically striking: almost every random vertex pair is nonadjacent (probability ~e/n) while its distance deficit is asymptotically indistinguishable in total variation from a random edge deficit. Both the full finite distribution and this natural comparison can support graph-polytope metric and sampling research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
