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

# Verification record

The proof's essential identities are equations (1)--(9) of `RESULT.md`. They were reconstructed by deriving the coefficient moment generating function through Parseval, checking positivity and location of the maximum of the radial rational modulus, evaluating \(F'(0)=U\) and \(F'''(0)/6=U(U^2-1)/48\), and checking both Chernoff signs explicitly. The logarithmic integral error is bounded by integrating a short arc and does not assume a Gaussian saddle approximation. The lower bound is genuinely infinite-dimensional because it holds for the complete coefficient distribution, not truncated Taylor data.

Run `python3 verify_coefficients.py` for supplementary standard-library exact rational checks of the cubic expansion and initial Taylor coefficients. The checker reports 96 exact identities. These sample identities are not a substitute for analytic quantifiers. The normalization is \(\|z^n\|_\theta^2=\exp(n^\theta)\), and the final asymptotic is for the logarithm of the *norm ratio*, not its square. The formula concerns fixed parameters \(0<\lambda<1\) and \(2/3<\theta<1\). No external verification or independent audit has occurred.
