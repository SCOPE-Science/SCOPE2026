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

Reconstructed the calculation independently by conditioning on the stationary reset age T~Exp(r) and on the angular path. With I_c and I_s the integrals of cos(2Θ) and sin(2Θ) over that age, the conditional position is Gaussian with Σ_xx=2D̄T+2δI_c, Σ_yy=2D̄T−2δI_c, Σ_xy=2δI_s. The stationary angular correlations are (1/2)exp(−ω|u−v|), ω=4q, so E I_c²=E I_s²=1/[r(r+ω)] after the age average. Gaussian fourth moments give V=4D̄² Var(T)+4δ²(2E I_s²−E I_c²)=4D̄²/r²+4δ²/[r(r+ω)]. The age integral similarly gives E[X_0² cos(2Θ_0)]=δ/(r+ω). The future initial y² term survives with probability e^(−rt); instantaneous future y variance at time s survives with probability e^(−r(t−s)), with mean angular harmonic e^(−ωs)cos(2Θ_0). Taking covariance gives e^(−rt)[V−A∫_0^t e^((r−ω)s)ds], A=2δ²/(r+ω). The backward construction yields stationarity and finite moments; uniqueness follows from the unique uniform angular invariant law and loss of initial position at the first reset. For nonzero δ, the bracket is strictly decreasing; for r<ω its limit is V−A/(ω−r), and negativity is equivalent to (2+3b²)(r/ω)²−2b²(r/ω)−2>0. At equality the tail is exactly V e^(−ωt); for r≥ω the bracket is unbounded below, with crossing V/A at resonance. The quadratic root lies in ((1+√11)/5,1), decreases in b² (since the root exceeds 2/3), and has the stated endpoint limits. The log root gives r t_*→log(3+2/b²); when δ=0 the covariance is V e^(−rt). A boundary replay is D̄=ω=1, r=9/10, b²=38/63, which gives V=400/63 and A=40/63, hence the strictly positive critical tail. Reviewed the supplied scripts and their recorded outputs as diagnostic evidence only; did not execute them.

## originality

PASS

The equal-time moments and much of the conditional second-moment propagator are known. The supportable increment is the stationary nonzero-lag orthogonal square covariance and its exact sign classification under retained orientation. No inspected source supplies the same stationary mixed fourth-order temporal law or a result covering the sign threshold. This is a best-of-knowledge assessment, not certification of priority.

## value

PASS

A rotationally invariant stationary position marginal and positive simultaneous squared-coordinate covariance conceal a strictly negative delayed covariance above a quantitative threshold. The transition picks out retained orientational memory rather than signed coordinate correlation; the exact anisotropy-dependent boundary and the single crossing make this a usable temporal diagnostic. No statistical inference rate or other reset protocol is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
