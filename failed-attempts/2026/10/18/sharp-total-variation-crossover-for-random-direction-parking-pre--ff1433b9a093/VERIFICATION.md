---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The asserted limits concern the last preferred spot conditional on success, with half-L1 total variation. Independently, fix all direction choices and park on a circle of n+1 spots: rotation puts the final vacancy at the sentinel in exactly one of n+1 translates. Cutting at the sentinel gives the weighted line normalization (n+1)^(n-1). With j the hole before the last arrival, neither preferences nor searches can cross that hole during successful prefix parking, so the two sides factor with the binomial interleaving count. The last preference left of the hole succeeds with probability p, and right of it with probability 1-p; this gives the sign and normalization of (1). Stirling applied to the Borel factorization gives the n^(-5/2) interior scale and an O(1/(n j^(3/2))) bound at the left boundary. The signed cumulative weight is anchored at the midpoint and its increment is b_j+b_(j+1); the limiting derivative is twice the interior density. The n-scaled absolute mass includes one unit at the two endpoints together and the interior integral of |1+t f|. Pairing reflected positions reduces that integral to the integral on [0,1] of max(1,a z/sqrt(1-z²)), with a=8|t|/sqrt(2π); splitting at z=(1+a²)^(-1/2) yields sqrt(1+a²). The same integrable endpoint bound gives the fixed-bias norm limit; the unbiased terms are O(1/n) there. This includes p=0,1 and any sequence with the stated finite scaled limit.

## originality

FAIL

The classical primary source does not state the sharp constants or joint limit, but a distinct indexed finding covers the whole submitted asymptotic claim, including every fixed biased p as a special case of a stronger sequence statement. Another distinct indexed finding contains the identical critical profile. This is a statement-level coverage verdict, not a finding about chronological priority, authorship, or dependence.

## value

PASS

The asymptotic question is mathematically substantive: the unbiased boundary mass and the bulk bias compete at one scale. Their combination produces a curved profile, not a replacement of order notation by arbitrary constants. This value of the mathematical result does not make an additional duplicate finding valuable as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
