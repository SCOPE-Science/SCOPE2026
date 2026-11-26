---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Positive Beatty complementarity gives r(n)=floor(n/β) minus the number of positive upper summands below n with upper complement, where β=φ². Put j=m+1, t=F_{j-2}, and ε=φ^{-(j-2)}. Binet gives tβ=F_j+ε for odd j and F_j−ε for even j; tε<1 and ε<=φ^{-3}. A sum of two upper terms has value floor((k+l)β) or one less. For odd j, totals k+l<t give sums at most F_j−3 and totals k+l>=t give at least F_j−1. For even j only k+l=t could yield F_j−2, and it would require a carry, hence 0<e=ceil(kβ)−kβ<ε for 0<k<t. The integer t ceil(kβ)−kF_j=te−kε would have absolute value <1 and hence be zero, contradicting gcd(t,F_j)=1 and 0<k<t. Thus r(F_j−2)=floor((F_j−2)/β)=t−1. The estimate floor((F_j−3)/β)<=t−2 applies to all earlier points of the block. At F_j−1 the cited mixed complement theorem gives zero, verified in Shallit Theorem 5. For j=5 the target equals the left endpoint F_4 and t−1=1, so the same uniqueness argument applies. The frozen script was inspected, not run. A fresh exact audit reproduced its finite checks through F_17, and the separate 24-case replay `/workspace/reproductions/4.py` is used below with the published recognizer. Neither bounded count on its own proves the infinite result. The upper-sum exclusion is a separate fact used to attain the maximum.

## originality

FAIL

No inspected source explicitly phrases the mixed Fibonacci-block extremum. Nevertheless it is a mechanical corollary of the exact 12-state upper-sumset recognizer in Shallit Theorem 8 plus the earlier endpoint theorem, not merely something a general counting algorithm might help investigate. The decisive implication is given below, including a complete finite test of the only regular word families needed. This conclusion does not rely on the inaccessible Kawsumarng full text or same-day dating.

## value

FAIL

Exact extrema on natural Fibonacci blocks are a sensible invariant, and the elementary exclusion proof is transparent. But the stated fact is mechanically obtainable from the two published sumset descriptions via a fixed two-suffix state test and elementary floor bounds. The paper does not establish a stronger structural tool or an additional unknown exact invariant that survives this coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
