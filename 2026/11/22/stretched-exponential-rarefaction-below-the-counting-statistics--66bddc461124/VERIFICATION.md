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

For a one-sided +L barrier, reflection gives single survival erf(sqrt(c/t)), c=L²/(4D); independence and renewal occupation give age density S_1(t)^N/μ_N, killed product law given age, and binomial count given age. The survival integral is finite iff N>2 by t^(−N/2) at infinity. In u=t log(N)/c, Mills' estimate gives −log S_N=(1+o(1))sqrt(u/(π log N)) N^(1−1/u) locally uniformly, and μ_N∼c/log N by the step at u=1 plus the uniform age-tail bound at RESULT.md lines 59–65. For U fixed, the reflected image integral is O(N^(−1/U)/sqrt(log N)) uniformly on u≤U since 2sqrt(log(N)/u)−ell/sqrt(u)≥sqrt(log(N)/u) eventually; the survival normalization has the same error. Taking δ=N^(−β), 0<β<1/(2uκ), choose U>uκ with 1/U>β. This makes the error o(δ), so young ages up to uκ−δ have success-count lower tail bounded by exp(−const Nδ²), whereas the window [uκ+δ,uκ+2δ] has the desired count with probability 1−o(1), including integer rounding. The two bounding survival exponents agree to relative o(1) because δ log N→0, and the logarithms of the mixing density normalization and window width are negligible. A fixed younger age gap incurs a cost exp(−const N); a fixed older gap raises the stretched-exponential power, so dividing by the sharp rare-event estimate proves conditional localization. The assumptions exclude a crossover near the hard edge, not a uniform rare-event law.

## originality

PASS

Credit the finite-population subedge logarithmic equivalent and its selected age under one-sided collective resets, not the exact stationary mixture or limiting hard edge. The closest related indexed statements concern different observables and do not supply equivalent coverage. The primary paper's passage-level comparison remains access-limited.

## value

PASS

The zero below the limiting support hides a continuum of stretched-exponential powers and the mechanism producing a rare low count. Resolving the coefficient as well as the unusually old selected age distinguishes the result from typical-age binomial fluctuations and from a hard-edge statement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
