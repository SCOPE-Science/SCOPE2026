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

The signed Lamperti transform defines the nonsticking branch and turns the motion into constant speeds ±v. The law regenerates at a complete reset; solving the two-state Fourier resolvent gives stationary characteristic function r(r+2ν)/(r(r+2ν)+v²k²), hence the Laplace scale used in the variance. Reflection symmetry gives mean zero and eliminates all paths with a reset from the stationary covariance, so C(t)=exp(−rt)H(t) for the no-reset correlation H. Stationarity of g² gives H'(0+)=rC(0)/2. For the second derivative, differentiate H'(t)=v E[g(Y_0)Σ_t g'(Y_t)] in the unreset dynamics. Zero flips give the drift term v² E[g g'']; the probabilities of zero and one flip give −2ν H'(0+) and two or more flips contribute o(t) to H'(t). For 1<p<2 the unreset drift difference quotient after multiplication by g(Y_0) is controlled by a constant times |Y_0|^(2p−2) on |Y_0|>2vt; on the shrinking inner region it is O(t^(2p−2)). This justifies the singular-origin boundary limit with the Laplace tails. More generally the integral of g'' against the shifted initial density weighted by g is continuous near zero lag, by local integrability of g'' and the bounded weighted density with exponential tails. Product differentiation cancels the two reset terms of second order, giving C''(0+)/C(0)=(p−1)r(r+2ν)/(2(2p−1))−rν=r(αr−4ν)/(2(α+2)). At α=0, g is linear and the drift term is zero. The two derivatives determine positive r and ν in sequence for known α, then the stationary variance determines a unique positive v. This is a population inverse, not estimation under noise. The supplied checker was inspected, not executed.

## originality

PASS

The underlying heterogeneous telegraph model, stationary marginal, and homogeneous reset-covariance boundary are prior. The supported distinct claim is the normalized right curvature of the nonlinear physical position, its reset-to-flip threshold, and the resulting exact inverse with known exponent. The slope by itself is a stationary reset balance identity, not the distinct contribution.

## value

PASS

The physical-coordinate nonlinearity changes the sign of initial curvature while leaving the first normalized slope unchanged and negative. The explicit threshold separates these two effects and permits the tumbling rate and speed scale to be distinguished from the reset rate using only short-lag population data and the stationary variance. No inverse robustness or applicability outside the model is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
