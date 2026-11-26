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

With v,a,d>0, the rate polynomial is positive at 0 and negative at d, so the two positive rates straddle d. The off-diagonals of the unperturbed propagator are a f/k and d f/k, k=r−s. The first builds the surface load from the air-only pulse and the second propagates the removed load to the air objective over the remaining time. This yields the exact positive-factor gain qQad f(τ)L(T−τ)/k², with zero gain at both endpoints. The logarithmic derivative g=f′/f strictly decreases. To check h=f/L decreases, f′L−f²<0 is immediate when f′<=0; otherwise the strict log-tangent bound for f on (0,t) gives L<f²/f′. The stationarity expression g(τ)−h(T−τ) is therefore strictly decreasing in τ and increasing in T. The unique interior root lies below the surface peak t0, increases with T, and converges to t0 as h tends to zero. For short horizons, writing x=τ/T and multiplying the root equation by T gives 1/x−2/(1−x)−(r+s)T/6+O(T²) near x=1/3. The first two terms have a simple zero there with derivative −27/2, giving the stated −(r+s)T²/81 coefficient in τ. At large T, h(u) is asymptotic to sr exp(−su)/k and g′(t0)=−sr, which gives the stated exponential peak approach. An independent augmented-matrix-exponential computation reproduced the example optimizer 1.954697195671885 h, baseline burden 1.455061340406646, and reduction 0.235189905679788.

## originality

PASS

The physical two-state exchange model and cleaning of surface reservoirs are prior. The supported distinct contribution is the evaluated one-wipe, source-free finite-horizon timing theorem, including uniqueness, spectral dependence, horizon monotonicity and its two endpoint laws. The strongest overlapping scalar window result uses different dynamics and cannot be specialized to this two-mode jump.

## value

PASS

An explicit timing criterion distinguishes maximizing removed surface burden from minimizing cumulative air exposure. The optimum is strictly earlier than the burden peak and can be selected from the two air-decay rates without identifying the individual transfer rates or removal fraction. The horizon dependence gives actionable limiting intuition and an exact test case for richer compartment models; this is a meaningful structural result within the stated idealization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
