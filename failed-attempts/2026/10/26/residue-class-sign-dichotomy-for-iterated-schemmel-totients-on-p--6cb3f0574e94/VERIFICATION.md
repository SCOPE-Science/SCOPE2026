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

If t=p−m is coprime to P_m and L_m(t)≤2m, each positive local factor q^(b−1)(q−m) is at most 2m. Therefore every q is at most 3m, each exponent is bounded by e_q, and t divides T_m. When t>B_m this is impossible. For a prime p>m, gcd(p,t)=1; the first iterate is p^(a−1)t and the second is L_m(t) for a=1 or p^(a−2)tL_m(t) for a≥2. A prime q≤m dividing t kills the next iterate and proves strict deficiency. Otherwise t>m and L_m(t)>2m give strict two-iterate abundance: t+L_m(t)>p at a=1, and tL_m(t)>mp for a≥2. Among reduced p modulo P_m, a q dividing m imposes no exclusion and each other q excludes one of q−1 options; CRT and the prime number theorem in fixed progressions therefore give both asserted asymptotics uniformly in the sense of a single finite set of exceptional base primes. At m=4, with t>4 and avoiding 2 and 3, the only t with L_4(t)≤8 are 5,7,11,25,35,55, by enumerating the products of local factors 1,5,3,7 from the permitted prime powers. Only 25 and 55 give primes p≥13. Their chains are 25→5→1 and 55→7→3→0, yielding D_4(29)=31 and D_4(59)=65; at a≥2 their products tL_4(t) are 125>116 and 385>236. Bases 2 and 3 vanish, 5 gives a geometric sum strictly below 5^a, 7 gives 3·7^(a−1), and 11 gives 10 at a=1 and 98·11^(a−2) at a≥2. All remaining p≡1 mod 3 have a vanishing second iterate. Frozen verify.py and VERIFICATION.md were inspected; the reported exact finite comparisons were not rerun and are not a substitute for the analytic uniform proof.

## originality

FAIL

The distinct indexed finding f611bc4e0ee8 states the same uniform eventual sign criterion, the same prime-density product, and the same complete m=4 classification (it also classifies m=2). The different cutoff is real, but the other proof already gives an explicit sufficient cutoff in terms of its displayed rational constant c_m. The frozen replacement bound is neither sharp nor a demonstrated overall improvement and does not salvage the principal claims. The coverage is established by matching passages, not by inferring priority from dates.

## value

FAIL

A complete classification and exact density for these arithmetic functions are naturally motivated, but in this submission those results are already covered. The remaining cutoff is only a sufficient, unoptimized replacement for a prior explicit threshold; it is weaker already at m=6 and no different useful regime, optimality, or systematic quantitative improvement is established. No independently valuable surviving claim is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
