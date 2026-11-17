---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The source pencil maps t to parameter kappa(t)=t^-3-t^4, giving the known collision polynomial after factoring kappa(x)-kappa(y) by y-x. Substituting y=sx shows B birational to t^7=-(s²+s+1)/(s³(s+1)(s²+1)). At characteristics away from 2,3,7, the rational function has seven distinct branch places with valuations (1,1,-3,-1,-1,-1,4); gcd(valuation,7)=1, so the degree-seven geometric Kummer extension is connected and totally ramified at seven places. Riemann–Hurwitz gives g=15. Degree-nine plane arithmetic genus28 yields delta sum13 and Weil plus delta bounds gives #B(Fq)>=q+1-30sqrt(q)-13. For gcd(7,q-1)=1, seventh powering permutes Fq^×, giving exactly one H point over every rational s, including ramified rational fibers; #H=q+1. Ordered distinct collision pair ratios s cannot have s³=1 or s⁴=1; inclusion–exclusion gives q-gcd(3,q-1)-gcd(4,q-1). Independent polynomial factorization/algebra and brute-force prime q=5,11,13,17,19,23,31,37,41 corroborate only finite cases.

## originality

PASS

Asgarli–Ghioca previously defined this exact collision curve and established geometric irreducibility and a weaker Hasse–Weil estimate using the plane arithmetic genus. It also established the source N_k root criterion. These are expressly prior work. The surviving theorem evaluates its normalization genus15 and Kummer model, improves error to 30sqrt(q)+13, and computes an exact second factorial moment for an arithmetic regime; the inspected independent published singularity-classification result gives only the first moment and node-splitting classification, not these collision-pair counts. Original 2023 primary full Section 2 unavailable (arxiv/open access and authorized institutional blocked), so historical priority is qualified not fabricated.

## value

PASS

The degree-nine collision curve is an established controlling object for rational smoothness questions; its exact normalization genus and second singularity moment are natural invariants needed for refined point-count and incidence estimates. The improved Weil coefficient and exact collision moment provide specific arithmetic information beyond existence bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
