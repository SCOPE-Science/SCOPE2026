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

For a unit step on the input path only the windows straddling its edge can respond. A single affected window is at the output boundary. When there are two, their derivatives are u=∂c D(a,b,c) and v=−∂b D(b,c,d). Hölder bounds each by M=2^(1/p). If b<c and u<0, put s=c−b and t=a−c. The numerator in |u| is t^(p−1)−s^(p−1), and the denominator is at least (2t^p)^((p−1)/p). This gives |u|≤M/2, with the reflected estimate for v; b=c gives magnitude M/2 for nonconstant crossing triples. Thus opposite signs force one smaller amplitude. Counting adjacent differences with zero, one, or two flanking zeros gives 3M/2, 5M/2, 3M at lengths 4, 5, ≥6, respectively. The 1-norm of the coefficients in the unit-step decomposition is exactly input TV. To justify line integration at constant triples one may approximate the initial endpoint by data with no constant triples, so the segment meets nondifferentiability in finitely many parameters, and pass to the limit by continuity. With (a,b,c,d)=(1,0,ε,ε), the derivative tends to (−M/2,M), and finite differences tending to this derivative prove the sharp supremum for fixed p. At the endpoints the statistic is range or twice range, and the two crossing range derivatives have the same weak sign. An actual small positive step at that same baseline leaves the first range fixed and increases the second by the step size, even though c=d; no strict ordering of the two tied entries is needed. The n=3 output TV is identically zero, so the endpoint discontinuities are for n≥4 only. The proof establishes the continuum; the frozen NumPy tests were inspected, not rerun.

## originality

PASS

Pass for the continuum sharp law and its endpoint discontinuities, with exact prior coverage credited for the quadratic slice and the long-path Gini endpoint. The strongest other matched three-site p-family is a different filter. There is no priority claim from same-day publication dates.

## value

PASS

A sliding local dispersion filter is a natural use of both Gini-type and quadratic scale statistics. The exact length cutoffs and strict drops at both limiting exponents show that pointwise approximation by very small or very large finite powers cannot be used to infer worst-case stability of the limiting filter. The crossing-window estimate identifies why adding independent worst-case responses would overestimate the gain; the explicit baselines give practical tests. This value does not depend on treating the known quadratic or Gini slices as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
