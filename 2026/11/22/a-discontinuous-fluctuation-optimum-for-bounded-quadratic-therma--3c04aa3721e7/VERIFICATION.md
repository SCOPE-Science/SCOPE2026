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

Verified for the stated dimensionless cosine cycle and the continuous hard-truncated quadratic. Reflection reduces to m≤1/2, and direct integration for A≤m gives m(1−m)−A²/2. When only the lower cutoff is crossed, the integral over [0,α(m/A)] has no first-derivative boundary term since g(0)=0; integration gives F'=[(1−m)s−Aα]/π, with sign K(m/A)−m/(1−m). For A>1−m the arcsine integral differentiates to a strictly negative integral. At the two junctions F' is continuous: the clipped g is Lipschitz and differentiation under phase averaging uses a bounded integrand except on a zero-measure set of phases hitting the cutoffs. In particular F'(m)=−m and at A=1−m the formula from the lower-only region gives (1−m)(s−α)/π<0 for m<1/2. For m=1/2 the quadratic and full-support regions alone give strict descent. Direct differentiation gives K'=P/(sα²), P'=−4tα, and K vanishes at both ends, with a unique nondegenerate maximum at t_*. The two roots below the fold are both admissible: for k=m/(1−m)<K(t_*), k<t_* and K(k)<k, forcing the smaller root above k. Since t=m/A decreases with A, the larger root is the minimum and smaller root the maximum. At the fold, K''(t_*)<0 and the prefactor of K−k in F' is positive, so F' has a double zero and F'''<0 there: the horizontal inflection is not a local extremum. At a stationary point the height ratio reduces to R(t), with derivative the stated strictly positive factor times −P. On (0,t_*) it decreases from infinity to below one (use P(1/2)>0 and R(1/2)<1), so exactly one positive-branch value ties A=0. The monotone pieces and strict tail descent complete the global classification and the discontinuous one-sided amplitude limit. Bisection independent of the frozen checker gives c_fold≈0.17846502362118932, c_switch≈0.13773027340449354, A_jump≈0.43089218157395015. A direct uniform-phase midpoint sum for m=0.1 at A≈0.4971478159410423 gives F≈0.11280709248223, consistent with the reported value. Read all frozen support including check.py without executing it; the analytic sign and comparison argument, not the finite check, supplies the universal result. This is stationary optimization, not physiological hysteresis or field validation.

## originality

PASS

Rate averaging and mean/variance effects are established. The inspected older mathematical model varies the mean for asymmetric thermal curves, and the closest indexed exact models either vary the waveform or start with a mean outside the viability interval. The fixed-interior-mean amplitude switch and separate fold are not supplied by those statements. This is a bounded best-of-knowledge finding; it does not certify priority against general convolution work.

## value

PASS

Clipping a rate at viability limits is a motivated benchmark. The exact result quantifies when initially harmful fluctuations become globally beneficial at larger scales, and when a newly available positive local optimum is still inferior. Distinguishing the global tie from the interior fold matters for interpreting local optimizers and is not an untruncated Jensen calculation or an arbitrary numerical example. No empirical universality or dynamical hysteresis is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
