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

For b>=0 the denominator is positive and the margins are uniform. Continuous mixed-density nonnegativity is equivalent to two-increasingness; a negative boundary density also gives a negative interior rectangle by continuity. For C=xy g(t), t=(1-x)(1-y), differentiation gives g-hg'+xy t g'', where h=x+y-3xy. For OR3 the resulting numerator is affine in s=(1-x)+(1-y) at fixed t, with attainable endpoints 2sqrt(t) and 1+t. On the positive side the axis endpoint is positive, leaving exactly the displayed diagonal test. On the negative side put k=-a and w=kt. At (0,1) one needs k<=b+1; under this bound P=k/(1+b exp(w))<=1 and Pw<=1, the latter by exp(w)>=1+w and w<=b+1. For z>=b the numerator divided by (b+z)^2 is at least 1-P, and for z<b it is at least 1-P+Pxy(1-w), nonnegative by the two bounds. This includes b=0 and equality at the frontier. The valid (2,1) witness follows from 1-exp(-2v^2)<=2v^2<=2v. At (21,20) and x=y=2/3, the witness is the quadratic (3600-3560z+205z^2)/9 with z=exp(7/3); exact Taylor bounds give 10<z<11, and convexity with negative endpoint values certifies failure.

## originality

PASS

The supported distinct result is the evaluated sharp negative frontier for OR3 for all b>=0 and its certified contrast with the positive side. The original expression, density, published sufficient rectangle and b=0 exponential special case are prior. The one-dimensional test is a family-specific formulation of a general affine-endpoint calculation, not credited as a new universal transform characterization. The closest accessible statements do not cover the family-specific sharp inequalities or directly imply the asymmetric boundary behavior.

## value

PASS

The exact sharp negative interval resolves an actual domain question for an existing copula family. The positive diagonal criterion reduces continuum checking to one variable and identifies what the corner bound misses: two exact examples on a=b+1 distinguish a valid extension from a genuine interior obstruction. This matters for selecting legal parameters, not merely comparing pointwise bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
