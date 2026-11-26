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

The stated symmetric adjacency has 18 edges and exactly degree-four vertices 2, 4, 11. Both listed permutations preserve its edges and induce generators of S₃ on those vertices; permuting coordinates conjugates the corresponding updates. In an independent exact program I encoded states as subsets of the vertex set. Each unbiased even site has a self-loop and uses strict majority; each biased site uses threshold two on four open neighbors; at degree three use threshold two. Recurrence was computed independently of the frozen scripts: start from all roots of F_B²(x)=x, distinguish fixed roots from two-cycle pairs, and grow successive disjoint preimage layers. A state appears at its true first-entry time, and inherits its attracting orbit from its successor. All 2,048 starting states were assigned at every one of the eight policies, excluding longer periods directly. The exact tables agree with all stored fixed- and two-cycle basin histograms and entry-time/period distributions. For k=0,1,2,3 respectively the combined unanimous basins are 1002, 852, 795, 763; unanimous-one basins are 501, 567, 624, 672; two-cycle counts are 61, 48, 44, 55; the sharp maximum times are 6, 6, 6, 4. For the all-biased case, the labelled integer trajectory 37→26→549→1050→869→1178→869 witnesses first entry at four. The same reproduction prints witnesses for each other policy. The frozen builder compares aggregate censuses, not paired state-by-state arrays as one verification sentence suggests, but the proof and frozen aggregate claims are confirmed by the independent full partition.

## originality

PASS

The full incumbent-tie census is already covered and only the comparison baseline. The general eventual-period bound of two is also covered by a threshold-network theorem. The supported distinct result is the complete nonempty localized intervention census, including the opposite unanimity trends, nonmonotone two-cycle count, and sharp policy-dependent entrance cutoffs.

## value

PASS

The graph is a natural fixed benchmark whose only tie-capable sites form a single symmetric three-vertex orbit. The intervention isolates the effect of tie policy rather than changing edges. The full exact partition shows how support for one unanimous outcome can increase while the total probability of consensus under uniform initial conditions decreases, and identifies how recurrent alternatives and the time cutoffs change. These are meaningful unknown finite quantities beyond the incumbent-tie table and beyond the period-two theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
