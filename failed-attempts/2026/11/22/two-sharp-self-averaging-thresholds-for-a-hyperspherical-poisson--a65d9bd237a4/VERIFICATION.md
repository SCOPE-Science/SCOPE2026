---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The normalized spherical Poisson kernel has mean one; its second moment follows from convolution at coincident directions, giving (1+ρ²)/(1−ρ²)^(d−1). Distinct correlations are pairwise independent, including pairs sharing a label by rotational invariance conditional on that label. The angular density has rate I(s)=−(1/2)log(1−s²); a fixed bin with rate below 2α has exponentially many pairs with relative count concentrated by the variance bound, and a bin above 2α is empty with high probability by a union bound. These facts, finite-bin upper and lower bounds, and exclusion of near-endpoint tails give the constrained maximum of fρ−I over I≤2α. The identity (1+ρ²−2ρs)−(1−s²)=(s−ρ)² and the derivative show that the maximum is at min(ρ,tα), giving the stated log limit, including equality. For α>α_P, under the Poisson tilt the law concentrates at ρ. The truncated second-moment exponent at b=ρ is I(ρ) because 2fρ−I is increasing up to ρ; continuity gives a cutoff b>ρ with rate below 2α. The truncated average concentrates by Chebyshev and the discarded mean tends to zero, so A_d tends to one. Pairwise independence gives the exact variance and its stated constant and exponent, including at α_V. At α_P no ordinary probability limit is asserted. Fresh polar-angle quadrature corroborated both one-pair moments for d=2,3,8 and two values of ρ; replay `python3 /workspace/branches/independent_certificates.py 5`. The limit is proved by the rate and concentration arguments, not the quadrature.

## originality

FAIL

The combined diagram is correct but mechanically obtainable from existing results and their proofs. Ding–Markatou–Saraceno give the exact same off-diagonal variance, including the expression from which α_V follows immediately. Jana–Rao give the entropy-truncated empirical large-deviation principle and the resulting free-energy calculation for independent arrays; their inspected proof uses only a union bound and a pair-count variance bound, so carries over unchanged once one conditions on a shared direction to see pairwise independence. This yields the full log-rate, not just the extremal correlation. The strict probability cutoff follows from the established importance-sampling truncation proof of Chatterjee–Diaconis with the same pairwise-independence observation and the kernel tilt. These antecedents do not state the specific sphere statistic diagram verbatim; the finding is a combination and evaluation of their existing mechanisms requiring no additional dependence estimates.

## value

FAIL

It is useful to recognize that a variance diagnostic can misrepresent accuracy at this natural spherical null. But as a standalone research finding, the frozen result evaluates already available free-energy and importance-sampling cutoff arguments on the published kernel and substitutes into its known variance, with no additional dependence bound or critical-boundary law. The striking variance-versus-probability contrast is an instance of the already established importance-sampling distinction. This is an informative worked application, not a distinct exact research contribution under the scientific-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
