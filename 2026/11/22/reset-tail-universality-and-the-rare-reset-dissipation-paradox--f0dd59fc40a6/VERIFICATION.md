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

The Poisson age has rate r and is independent of the previous reset location. Free-displacement characteristic function r/(r+Dk²) gives an independent unit Laplace Z times sqrt(D/r); the pre-jump marginal is stationary because the clock intensity is constant. Forward and reversed Brownian segments have symmetric free kernels; the stationary endpoint log-density ratio has mean zero, and the ratio per jump x→y is p_R(y)/p_R(x). Endpoint integrability follows from the stationary convolution: it is bounded above and bounded below by a positive constant times exp(-|x|sqrt(r/D)) by restricting the reset integral to a bounded interval, and has finite first moment. Thus the rate is r[E h(Y+TZ)−E h(Y)], T=sqrt(D/(r sigma²)). For T≥1, |h(Y+TZ)|/T^p is bounded by a constant times 1+|Y|^p+|Z|^p and converges almost surely to c|Z|^p. The Laplace moment Gamma(p+1) gives the stated coefficient, and the bounded-in-T subtraction E h(Y) is lower order for p>0. For the even powers, the gamma moment ratio enforces variance one. Binomial expansion, E Z^(2j)=(2j)!, and vanishing odd Laplace moments give all coefficients with the stated powers of D/sigma² and r. Gaussian c_1=1/2 gives D/sigma²; for m≥2 the positive j≥2 coefficients imply strict decrease, and j=m determines the leading divergence. The quartic terms follow from E Y²=1.

## originality

PASS

Supported distinct content is the rare-rate tail-index classification, with its coefficient and finite-variance super-Gaussian divergence, plus the all-even-power finite-rate polynomial and monotonicity. The stationary convolution, general path-reversal entropy functional, and already treated Gaussian and exponential cases are not credited as new.

## value

PASS

At fixed reset variance the rate can vanish, stay finite and nonzero, or diverge under the same rare-reset limit. This distinguishes models indistinguishable by variance and explains why low event frequency need not make the process close to reversible by this measure. The quartic law gives a smooth, normalized, explicit witness, and the even-power formula resolves the finite-rate direction of change rather than merely exhibiting sampled growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
