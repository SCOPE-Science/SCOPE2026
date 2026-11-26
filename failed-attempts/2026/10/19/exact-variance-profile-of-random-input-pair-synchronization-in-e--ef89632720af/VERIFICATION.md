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

Repeated independent trials of a fixed reset word give a geometric tail, ensuring finite moments and uniqueness of the transient-chain equations. Before reaching the boundary j=n−1, a rotation advances the pair and a merge leaves it unchanged; this produces a drop of 2 in both mean and variance per advancement. At the boundary reached from {0,d}, let L=n−1−d; the successors are {0,L+1} and {0,L}, with the latter absorbed for L=0. For the mean the boundary equation is F_d=2L+1+(F_(L+1)+F_L)/2. For variance the law of total variance gives G_d=2L+(G_(L+1)+G_L)/2+(F_(L+1)−F_L)²/4. Direct symbolic substitution gives zero polynomial residuals, and F_0=G_0=0. The strictly concave quadratic F_d has vertex n(n−1)/(2n−1), whose closest integer is floor(n/2) for both parities; the term −2i makes i=0 unique. At this gap the mean and variance have leading terms n³ and 2n⁶/3, giving the stated coefficient of variation, not a distributional limit. An independently written exact-rational replay (`python3 reproductions/2.py --max-n 8`) matched all 83 pair states for n=3,…,8; the frozen verifier was inspected, not run. The recurrence identities, not the finite replay, establish the claim for every n.

## originality

FAIL

An indexed result gives the complete conditional first- and second-moment solution for the identical chain after cyclic relabeling, so the variance of every starting pair is already determined explicitly by subtracting the square of the conditional mean. Another indexed record gives the odd-diameter variance and the same limiting coefficient of variation directly. This is present mathematical coverage; the later catalog dates do not establish prior conception, historical priority, or derivation direction.

## value

FAIL

An all-pair variance would answer a natural quantitative question beyond mean synchronization, and the single quartic representation is convenient. But the exact invariant is already mechanically available from the complete conditional moment solution, and the stated fluctuation limit is also explicitly available for the odd diameter. The simplification provides no distinct invariant, distributional conclusion, or new regime in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
