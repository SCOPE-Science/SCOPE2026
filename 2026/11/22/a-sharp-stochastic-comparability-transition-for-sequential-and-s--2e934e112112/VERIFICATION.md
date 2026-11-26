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

Conditioning on the first arrival gives the wheel's greedy mixture with hub weight 1/(n+1) and rim size 1+R_(n−3). Uniform maximal sets instead weight the hub by 1/(M_n+1), where M_n counts maximal rim sets. The cyclic gaps between selected vertices are 2 or 3, which proves the marked-gap enumeration and the transfer matrix A(z) with rows (0,1,0), (z,0,1), (z,0,0). The trace of A(z)^n counts weighted labeled configurations. At z=1 its recurrence M_n=M_(n−2)+M_(n−3) and startup counts 10,12,17 at n=8,9,10 give M_n>n thereafter, excluding greedy stochastic dominance at the singleton CDF. Conversely the greedy mean is strictly higher. For the infinite tail, the path first-arrival recurrence gives the generating function (1−exp(−2z))/(2(1−z)^2); its factorial remainder gives E S_n>0.43n for n≥20. For the static law the matrix trace is the sum of nth powers of the three roots of λ³−zλ−z. At z=1 their modulus ratios and the log derivative λ²/(3λ²−1) give E T_n<0.42n for n≥20. Thus the wheel mean gap is greater than 0.01n−0.43 for n≥44. I independently checked n=8,…,43 using exact fractions: iterate B=I,E=0 by (B,E)→(BA,EA+BA') at z=1 to get static wheel mean (1+tr E)/(1+tr B), and compute the sequential mean with P_0=0, P_m=1+(2/m)∑_(j=0)^(m−2)P_j and (1+n(1+P_(n−3)))/(n+1). All 36 gaps are positive; the minimum is 799/24570 at n=12. A higher mean excludes the reverse stochastic direction. Small wheel supports collapse as stated, with equality at n=3,5,7 and strict greedy dominance at n=4,6; for n=6 the two size-(1,2,3) vectors are (1/7,2/7,4/7) and (1/6,1/2,1/3). At n=8 the displayed CDF crossing follows from the exact rim size laws, with both directions strict. The uploaded verifier was inspected, not executed.

## originality

PASS

Sequential and uniform-static parking, cycle dominance, the greedy wheel mixture and earlier connected incomparable examples are established. The supported distinct result is the complete first-order comparison on wheels, in particular the persistent incomparability threshold rather than the existence of incomparability on some graph.

## value

PASS

The wheel is a natural way to test whether a universal vertex preserves a known rim order. The classification identifies where that order persists, where the occupancy laws coincide, and where the hub reverses only the low tail despite a larger mean. Persistence for every larger wheel is stronger than a lone counterexample. The result says nothing about the maximum-degree-three conjecture, since hub degree grows with n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
