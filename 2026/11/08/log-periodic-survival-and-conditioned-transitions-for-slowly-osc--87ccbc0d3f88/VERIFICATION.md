---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Perron conjugation gives F_n=Q+ε_nA, ε_n=f(log n)/n. Bounded f,f' give ε_{n+1}−ε_n=O(n⁻²) and s_{n+1}/s_n=1−κε_n+O(n⁻²), with s_n the inverse stated envelope. Substituting Φ_n=s_n(1+ε_n u) cancels the first-order defect by the centered Poisson equation. Positive products propagate componentwise relative errors against Φ_n, bounded by exp(CΣ_{k≥n}k⁻²); summing the propagated residuals makes the backward products Cauchy and gives the positive h_n with h_n/s_n=1+O(n⁻¹). Writing h_n=(πh_n)(1+w_n), the centered equation for w_n−ε_nu iterates under the stable restriction of Q with O(n⁻²) forcing; the convergent geometric sum is O(n⁻²). The scalar ratio a_n/a_{n+1}=1+κε_n+O(n⁻²) then yields the displayed Doob derivative, whose rows sum to zero. For fixed initial time, the normalized rows of the forward F-product approach π at O(n⁻¹) by the strict-positive stochastic contraction and O(n⁻¹) forcing. Testing against Φ_n and 1/R gives c_{m,x}=R(x)h_m(x)π(1/R)>0 and the claimed relative error with exponent n−m. Ratios for fixed prefixes give the harmonic Doob law. A shift of log n not a period of the mean-zero primitive gives a nonconstant multiplicative ratio if κ≠0; integer phase subsequences exist. In the witness, all live entries stay positive and the maximum row sum is 7/8. Independent characteristic-polynomial and eigenvector differentiation gives λ'/λ=1/12 and the rational response [[1/9,−1/9],[1/18,−1/18]] (python -B /workspace/independent_checks.py 5); the sine multipliers at their extrema have ratio e^(1/6). The finite arithmetic corroborates the witness, not the asymptotic estimates.

## originality

PASS

Limited to the log-periodic endpoint envelope with its error, the oscillatory Doob response through first order with O(n⁻²) error, and their simultaneous nonscalar witness. The constant-profile law and existence of an inhomogeneous Q-process are already covered. General product theory presents material risk for the survival portion considered by itself, but no inspected result establishes both stated quantitative conclusions in this regime.

## value

PASS

In a natural finite-state killed-chain setting, this exhibits a non-regularly-varying survival factor even though the kernels converge to a strictly positive limit, with quantified tracking of the instantaneous Perron transform by the actual infinite-horizon conditioned transitions. The nonscalar two-state witness realizes the survival modulation and a nonzero response simultaneously; multiplying a fixed kernel by alternating scalar masses would give only the former. The combined formula and rates make the distinction useful beyond a proof of existence of the conditioned process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
