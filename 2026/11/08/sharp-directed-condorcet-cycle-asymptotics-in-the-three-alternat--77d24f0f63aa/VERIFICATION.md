---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Execute `python verify_mallows.py` with Python 3; no third-party dependencies are needed. This checks coefficient identities and exact rational finite-electorate values, including an independent brute-force path for the smallest odd sizes. The observed result is `PASS: 171 exact coefficient / rational / exhaustive checks`.

The key noncomputational steps are: (i) binomial identification of the distant pairwise reversal; (ii) an explicitly normalized change of measure giving the positive tilted adjacent margin; (iii) an exponential bound for simultaneous reversals of both adjacent comparisons; and (iv) a binomial local approximation and geometric summation giving the full constant. The finite checker neither proves nor substitutes for the large-electorate analysis. The proof uses standard Hoeffding and Stirling estimates for fixed \(0<\phi<1\); it is not uniform as \(\phi\uparrow1\).
