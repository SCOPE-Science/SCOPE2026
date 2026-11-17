---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Eliminating velocity gives AR(2) with b=(1+a)^-2 and phi=[2(1+a)+a²(1-t)]/(1+a)², Gaussian innovation variance a³σ²/(1+a)^4. Jury conditions reduce exactly to Δ_t(a)>0 and t>0. The Yule–Walker covariance gives V_t=σ²(a²+2a+2)/(t(a+2)Δ_t). Independent symbolic derivative and factorization confirm F_t=B(a)[t-T(a)] and T'(a)=8(a+2)(a²-2a-2)(a²+2a+2)/[a²(a³+4a²+10a+8)²]. Thus T minimizes at a=1+√3, tc=(4+12√3)/13; each domain piece has claimed zero, one, or two extrema. Exact rational evaluation independently reproduces eleven-dimensional J'(1)=-10881433/143273691, J'(4)=40729/114967512, J'(20)=-2559661/557646408. This ensures total-error nonmonotonicity but not uniqueness of aggregate extrema.

## originality

PASS

Leplat et al. NAG-GS already gives the scheme, quadratic Schur boundary and Lyapunov framework, and Mohammadi–Razaviyayn–Jovanović provides broad two-step moment/noise formulas. Those underpin the calculation, but the exact stationary-noise turning-point threshold for the specific fixed-damping step path and fully stable 11-mode reversal are not stated or mechanically forced by the published optimal tradeoff statements inspected. Resultary queries for tc and the specific semiimplicit noise law found the assigned record only. Historical parameter-equivalence remains a risk.

## value

PASS

The threshold near 1.9065 separates monotone noise response from two extrema even when deterministic stability permits every step; the 11-mode exact witness shows the effect persists in an actual SPD problem rather than an isolated modal curve. This is a motivated counterexample to choosing step size solely by deterministic stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
