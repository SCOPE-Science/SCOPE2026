---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Gaussian polar decomposition separates chi-square squared radii from independent uniform directions. Every normalized factor has second-moment identity; conditioning out removed radial variables makes additional normalization an exact conditional expectation, so convex order and unbiasedness follow for arbitrary nonzero real PSD H. A product-state maximizer has positive spherical-neighborhood measure. AM–GM bounds a probe by (c rho/r^r)(sum squared radii)^r and the sum over m samples by one chi-square sum, giving the upper logarithmic t^{1/r} rate. Requiring one sample’s r independent chi-square radii to exceed a balanced threshold near the maximizing directions gives the matching lower rate; r=0 bounded, r=1 positive exponential moment below its sharp strict threshold, r>=2 none. No critical equality MGF claim. Independent rational chi-square calculations corroborated E Z^2 64/32/16 for H=I4 and the Bell projector product-state radius 1/2. Tail proof is analytic.

## originality

PASS

PASS best of knowledge: Bujanović–Kressner and Meyer–Avron give rank-one Gaussian probe bounds and Gaussian versus all-spherical endpoint variance analyses. The fully inspected Meyer–Avron paper treats full product distributions and variance/sampling complexity; it does not state the arbitrary intermediate-subset convex-order family or exact matrix-dependent t^{1/r} logarithmic constant and exponential-moment ladder. Generic homogeneous Gaussian-chaos large-deviation theory can imply related exponents and may implicitly cover sharp coefficients after optimization; the risk is documented. The joint conditional-design theorem survives bounded comparisons.

## value

PASS

PASS: Heavy-tail obstruction is an actual problem of Kronecker trace estimation. The claim gives a quantitative design rule, precise tail constants via the product numerical radius, strict monotone convex-loss comparison, and the exact number of radial normalizations needed to gain exponential moments. It is a motivated invariant beyond known endpoint variance reductions; hard computation of rho is disclosed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
