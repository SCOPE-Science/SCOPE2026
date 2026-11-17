---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For p in (0,1)\{1/2}, reflection reduces to P=(1+delta)/2>Q. Inspected exact images of dyadic cells L_j,R_j; each opposite-half jump renews a geometric depth J with Pr(J=j)=2^(-j-1). Left depth hitting from j is (Q/P)^(j+1), hence theta=(1-delta)/(1+3delta) and geometric N with mean (1-delta)/(4delta). First-step right downward-passage equation g=z(P+Qg^2), right exit b=Pz/(1-Qzg), and fresh depth average F=b/(2-g) imply E[z^S]=(1-theta)F/(1-theta F). Differentiation gives E S=(1+3delta)/(2delta^2). Expanding g at z=exp(-s delta^2) yields the continuous-at-zero Laplace limit 2/(1+sqrt(1+2s)); geometric transform yields delta N=>Exp(rate 4). Right excursions terminate, return count is almost surely finite, left depth thereafter has SLLN drift delta, so log2 distance-to-favored-endpoint rate delta. Validity of exact counts explicitly requires uniform initial point in disfavored half, while a.c. initial data suffice only for almost-sure endpoint statement. This is analytic infinite-time proof; no finite experiments are used as its substitute.

## originality

PASS

Prior Hata–Yano work proves symmetric p=1/2 arcsine/Darling–Kac limits; the inspected primary sections do not establish the off-critical geometric count, exact residence pgf or two bias crossovers. The nearby published generalized Hata–Yano and Pelikan findings address different maps/parameters and statistics. No dominating implication was identified, subject to literature coverage limits.

## value

PASS

The exact renewal law and two mathematically different critical scales distinguish recurrence number from occupation duration in a canonical random interval map, directly extending the critical case. The computable p-dependent finite-time invariant and endpoint escape rate address natural dynamical questions beyond a routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
