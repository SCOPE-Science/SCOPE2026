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

The defining integer sum of termwise parities is exactly the transform of (1,1,0) in Rampersad–Wiebe, journal Theorem 15 (arXiv v1 Theorem 18), so the support rejects precisely runs of length 2 mod 3, with the empty product accepted. Fixed-width binary order is increasing integer order; leading zeros in the initial state do not matter. From unfinished-run residues 0,1,2, reading zero resets states 0/1 and rejects 2, while a one advances cyclically, with final acceptance in 0/1. This proves the three prefix decompositions including A₀=B₀={0}, C₀ empty. The top accepted integer of A_m is 2^m−1 except when m≡2 mod 3, when clearing the last bit gives the maximum 2^m−2. The first element of B_m is zero, and the first of C_m is 2^{m−1} for m≥1. Consequently the only inter-block gaps are u_L=1+1_{L≡0 mod 3} for A_L and v_L=2^{L−2}+1+1_{L≡0 mod 3} for B_L, the latter only for L≥2. For L≥3 elimination gives the three preceding A-multisets plus u_L and v_{L−1}, with initial A-multisets empty, one gap 1, and two gaps 1. At L=3 both impulses are gap 2; thereafter the second impulse is exactly g_{L−3}. This proves all three generating functions, strict first appearance at depth j+3 for g_j, and exclusion of every other gap. The size series is (1+z)/D. In |z|≤q the triangle inequality on z+z²+z³, including its equality case, rules out any root of D but q; D′(q)<0. Taking ratios of simple-pole coefficients therefore gives the displayed fixed-gap limiting shares. Summing their numerators, including the geometric tail, gives 1+q at z=q using D(q)=0. Since q>1/2, summing g_jπ(g_j) diverges. The limit is for initial dyadic blocks, not arbitrary cutoffs. A separately written check verified exact binomial sums at n=0,…,300 (each 0 or 1) and all 121,395 adjacent pairs across L=1,…,18, with largest gap 32,769; those checks corroborate but do not replace the recurrence and pole proofs.

## originality

PASS

The ordered all-depth gap law, permitted-distance spectrum, and limiting dyadic probabilities for the fixed support are the distinct contributions. Both the exact binomial sequence and its support were already published; the older Fibonacci run transform has the identical odd support. The nearest general Baum–Sweet gap spectra use a different language and do not cover this one.

## value

PASS

The gap statistic is a natural geometric refinement of a published automatic support: it gives all possible distances, their multiplicities at every dyadic depth and a normalized limiting law with infinite mean. Membership and one-point support size do not answer those questions. The lacunary gap sizes and explicit asymptotic frequencies explain a nontrivial distinction between typical gaps and mean spacing without claiming a new underlying sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
