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

For the undivided S(m,n), Kummer gives the two self-addition carry totals minus the mixed-addition carry total. There are r input digits plus no further nonzero outgoing carries after the zero padding since all three incoming carries are at most one. For p=2h+1 the reachable class-zero incoming states are 000,011,101. From 000 the class-zero destinations count (h+1)²+2·h(h+1)/2=L: add the both-low square and the two mixed triangles where the mixed sum produces a carry. From 011 they count h(h+1)+h(h+1)/2+(h+1)(h+2)/2=L, because the high thresholds are h+1 and h, and the mixed carry threshold is 2h. Swapping digits gives 101. Neither a both-low mixed carry nor a missing both-high mixed carry occurs in these three rows, so the increments stay in {0,1}; complementing all bits and digits interchanges class zero and class one and verifies the other three rows. Hence the lumping is independent of the microscopic state and its weighted matrix is K(t)=[[L,Bt],[B,Lt]]. Its trace, determinant and initial terms give the exact rational generating function, including r=0. All transition entries are positive, so each intermediate valuation occurs and the all-zero and all-one paths count L^r and BL^(r−1). For Y_i=(−1)^(X_i), the eigenvalue 1/p gives E Y_i=p^(−i) and E Y_iY_j=p^(−|i−j|). Summing gives the stated mean and variance, including zero mean and variance at r=0. The two-state matrix is irreducible and aperiodic; its stationary sign covariances p^(−|i−j|) give the positive occupation-time asymptotic variance (p+1)/(4(p−1)). The finite-state additive-functional CLT applies from state zero. Dividing the quotient by 2 does not change any valuation for odd p.

## originality

PASS

The transition matrix, occupation histogram and probabilistic consequences are already those of Holte's ordinary two-summand carry chain. The supported distinct arithmetic claim is that the super Catalan quotient, a signed combination of three correlated carry counts, has exactly that process law on every square block. The inspected primary and indexed statements do not supply this quotient-specific identification or its weighted transfer. This is not a novelty claim for the ordinary carry chain, its moments or its CLT, nor a demonstration of historical priority.

## value

PASS

The two-index quotient combines carries that are correlated and subtracts the mixed stream; neither the usual Kummer law for one binomial coefficient nor independent convolution of factor histograms predicts its values. The exact uniform reduction to an ordinary two-state process supplies the full distribution and extremal counts for every block and gives an identifiable arithmetic interpretation of a familiar probability law. That reduction is substantive; the standard moments and limit law alone would not be a separate scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
