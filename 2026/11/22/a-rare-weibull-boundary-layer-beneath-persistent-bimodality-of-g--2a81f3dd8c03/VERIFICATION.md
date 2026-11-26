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

Taking the CDF power gives the location change with the stated minus sign and mass exp(-c_n). For a scaled negative excursion t, the ratio of the two CDFs gives the exact conditional survival exp[-c_n*expm1(t^p/c_n)]. The single exponential coupling realizes these conditional laws (not the original nested maxima); c*log(1+E/c) has positive derivative for E>0 and tends to E. On either branch put v=|x|^p/sigma. The density is proportional to v^k y exp(-y), where y=c_n exp(v) on the negative branch and y=c_n exp(-v) on the positive branch. The log scores k/v+1-y and k/v+y-1 both strictly decrease from positive infinity and each crosses zero once. The density vanishes at zero and at both tails, so these are strict distinct local maxima at every n. At the negative root t=c_n*v solves t exp(t/c_n)=k+t/c_n, giving t=k+O(1/c_n) and y=c_n+k+O(1/c_n); substituting preserves the exp(-k) height factor. At the positive root v=L-log(1-k/v), L=log c_n, which gives v=L+k/L+O(L^-2) and y tending to 1. Restoring units gives the two stated positions and heights; their ratio forces eventual unique positive global dominance. The ordinary unconditioned normalization follows by expanding the inverse signed power of b_n+sigma*G on its eventually positive branch. Independent high-precision finite checks corroborated the two location and height scales.

## originality

PASS

The signed-power Gumbel family, underlying mode equation and closure from max-stability are prior ingredients. The assessed addition is the combined rare conditional law and quantitative description of both peaks across block sizes. Comparison with the exact underlying model and the related published block-maxima limit found no covering statement of the conditional boundary layer together with the sharp peak asymptotics. Conditioning and stationary-point analysis are standard methods, not asserted as new.

## value

PASS

Bimodality is a defining feature of the model, so comparing its persistence under the standard block-maximum operation with the actual branch mass is natural. A zero-density valley preserves two strict local modes while the secondary peak and branch probability collapse on explicit different scales. The conditional law describes the fluctuations within that shrinking branch and the peak constants distinguish this from merely restating closure or the ordinary Gumbel limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
