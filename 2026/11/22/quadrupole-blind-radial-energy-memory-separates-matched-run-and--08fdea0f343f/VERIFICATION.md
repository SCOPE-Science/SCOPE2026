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

Use the stationary bounded convolution |Y|≤1 in dimensionless time, P=Y·n and Q=|Y|². The first-harmonic semigroup and orientation autonomy give E[P_τ|Y₀,n₀]=M+e^(−(1+α)τ)(P₀−M): in the convolution each n_s·n_τ has conditional mean e^(−α(τ−s)). Since Q'=−2Q+2P and stationarity gives E(QP)=E(Q²) from the time derivative of Q², the two covariance initial conditions both equal V. Solving C'+2C=2V e^(−(1+α)τ) gives H_α, including the resonance (1+2τ)e^(−2τ); its curvature at zero is −2(1+α). For amplitude, the angular action on P² at fixed Y is −θ(P²−Q/3); the position drift supplies −2P²+2P. The drift and the dipolar action on QP give −(3+α)QP+Q+2P². Their stationary balances yield M=(1+α)^−1, E P²=(2+θ/3)M/(2+θ), and E Q²=(M+2E P²)/(3+α). Subtracting M² gives the stated V and differentiating gives the strict negative θ derivative. Solving S=(18+5θ)/(2+θ) gives exactly the stated inverse for 5<S<9. Substituting θ=α and θ=3α gives the ratio, positive gap and limits; in particular V_RTP=5/72 and V_ABP=1/40 at α=1, while the common lag-0.96 kernel is 0.4280923294. These are conclusions about stationary radial squared displacement, not the full position process.

## originality

PASS

The same-day Poisson-redraw paper exactly covers the normalized kernel and variance in the audited theorem's isotropic RTP subset, with the same closure proof. The ABP kernel also follows from previously published arbitrary-initial second moments and stationarity, and separate stationary fourth moments are known. The distinct submitted result is the general two-eigenrate theorem for non-redraw as well as redraw orientations: the exact quadrupolar amplitude dependence with its inverse together with the common dipolar all-lag curve and the resulting matched comparison. No novelty credit is assigned to either named model's standalone formulas, the closure method, or the RTP kernel. The exact partial equivalence is not dismissed based on its date.

## value

PASS

Radial energy is a natural directly defined observable in an isotropic harmonic trap. The result pinpoints which angular information its normalized curve necessarily loses, and identifies a calibrated fourth moment that recovers it when two eigenrates are present. Equal measured all-lag shape can coexist with parametrically different variances, with an exact quantified gap under matched orientation persistence. This supports model discrimination and inverse interpretation beyond computing a familiar moment in a single propulsion model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
