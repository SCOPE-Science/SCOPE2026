---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=3 iid points on S¹ with f_eta(theta)=(1+eta cos(theta))/(2pi), eta in [0,1), minimal enclosing radius <1 iff a unique circular gap exceeds pi. A uniquely defined complementary arc anchor theta has mass density n f_eta(theta) p_eta(theta)^{n-1} with p_eta=(1-b sin theta)/2, b=2eta/pi. Expanding even sine powers and integrating f cos-derivative gives exactly the finite P(E) polynomial. The end slack S has conditional survival (1-q_eta(theta,s)/p_eta(theta))^{n-1}, with q_eta integral over the far endpoint sector; differentiating yields a joint density. Fixed eta>0 Laplace expansion at theta=-pi/2 gives stated sqrt(n) Gaussian anchor, p_*^{n-1} probability and independent rate-1 exponential slack on n/(pi+2eta) scale. For eta=lambda/n, uniform p expansion gives exp[-(2lambda/pi)sin theta], normalizer I0(2lambda/pi), and independent exponential slack. Joint density convergence plus unit limiting mass triggers Scheffe total-variation convergence. Geometric diameter-chord formula R=cos(S/2), C=sin(S/2)e^{i(theta+pi/2-S/2)} gives weak center/radius limits. Numerical checker source inspected; finite polynomial/quadrature and conditional simulations are not proofs of asymptotic TV. All claims restrict to fixed eta>0 or fixed lambda, not other varying rates.

## originality

PASS

Wendel 1962 proves the distribution-free semicircle probability for centrally symmetric laws; the assigned eta=0 case is already known. The complete 2026/10/25 marked Wendel theorem treats centrally symmetric boundary density and hull-to-center clearance; its assumptions exclude eta>0 cosine modulation and its variable is Euclidean hull distance, not minimum enclosing disk center. The 2026/11/8 three-point symmetry stability theorem treats n=3 probability deficit, not the n→infinity anisotropic conditioned marks and 1/n orientation transition. The new fixed-anisotropy Gaussian localization versus weak-anisotropy von Mises crossover with independent slack and TV joint law survives these comparisons.

## value

PASS

The conditional shape of a rare center-exclusion/minimum-enclosing-disk event is a natural stochastic-geometry invariant. This result provides an explicit exact finite probability and, beyond classical symmetric Wendel counts, a sharp crossover at eta∼1/n in conditional center direction, with nontrivial normal/Bessel/von-Mises and exponential marks and observable radius/center scalings. These are motivated asymptotic regimes, not arbitrary parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
