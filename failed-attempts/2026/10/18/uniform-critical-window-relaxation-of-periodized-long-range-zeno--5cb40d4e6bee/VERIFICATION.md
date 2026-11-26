---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Every signed lift in the defining rate sum contributes to the eigenvalue 2κF_p(2πm/N); lifts divisible by N contribute zero. The nearest-neighbor term makes all modes except m=0 positive. Differentiation and the Laplace/geometric summation are justified by absolute summability of r^(1−p) for p>2, and the resulting integrand has the sign of sin θ. Reflection and strict increase on (0,π) give exactly the stated minimizers, including N=3. At p=3 the twice-differentiated cosine series converges locally uniformly off multiples of 2π by Dirichlet's test; the logarithmic identity gives −log θ+O(θ²) near zero. Integrating twice from zero with F₃(0)=F₃'(0)=0 gives (θ²/2)log(1/θ)+3θ²/4+O(θ⁴). For ε=z/log N and θ=2π/N, the Taylor error for r≤N is bounded by Cκθ⁴ times the sum of r^(1−ε), and the r>N contribution by 4κ times the tail of r^(−3−ε). Both are O_K(κN^(−2)) because N^(−ε)=e^(−z) is bounded on K. The remaining decreasing sum differs from its integral by O(1), and that integral is log N times Φ(z) with continuous value at zero. Reciprocals give the stated spectral times; a squared deviation has rate twice the gap as a worst-case rate or when a gap mode is present, and can decay faster for other initial data. This is not a finite-dephasing quantum statement. The frozen checker was inspected, not executed.

## originality

FAIL

The classical polylogarithm results cover the claimed new normalization and window by direct specialization of the exact ring symbol, and also give the gap-mode inequality. This is positive implication evidence, not a failure to find the exact title or formula. In particular Catalano et al. already state the normalized critical log and constant terms in supplement Eq. (S30). The frozen truncated-moment proof is valid, but the resulting spectral claim does not have an uncovered component under the stated implication standard.

## value

PASS

As a statement about this specified rate generator, the asymptotic gives a physically interpretable normalization and predicts the change of relaxation across a size-dependent range of exponents. It cleanly separates gap time from squared-deviation time and finite rate-periodization from quantum or open-boundary dynamics. This usefulness does not make a direct implication of classical formulas an independent original finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
