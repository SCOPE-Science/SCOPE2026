---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Reconstructed f=(x-a)^2+(y-b)^2-r^2 and g=x^2+y^2-1 and X=(1+kappa*x)*xy*(g J grad f - f J grad g)+epsilon*f*g*(x,0). Exact symbolic polynomial expansions for arbitrary parameters independently give df(X)=f[(1+kappa*x)4xy(bx-ay)+2epsilon*x(x-a)g] and dg(X)=g[(1+kappa*x)4xy(bx-ay)+2epsilon*x^2 f]; both coordinate axes are invariant and the second component has a nonzero degree-five term. On f=0 the angular speed 2xyg(1+kappa*x) is strictly positive by a,b>r and sqrt(a^2+b^2)-r>1; hence a regular finite-time periodic orbit exists. The cofactor contribution from g is a closed-orbit total derivative; pairing theta with pi-theta makes the remaining log multiplier -2epsilon*kappa*r^2 times a strictly positive integral, without sign ambiguity or numerical inference. Three independently selected admissible parameter tuples passed direct original-vs-paired quadrature. Degree <5 lower bound relies on the specific published Jana-Sarkar degree 3/4 exclusion and classical low-degree Kolmogorov facts; the code alone does not prove impossibility.

## originality

PASS

PASS within inspected primary and published mathematical sources. Jana-Sarkar establishes precisely the no-go up to degree four, not the all-parameter quintic attracting construction. The 2025 Gasull-Santana lower-bound/prescribed-curve framework has general Kolmogorov constructions, but its inspected published statements do not enforce simultaneous invariant singular unit circle, invariant axes, and a separate positive circular attractor at degree five. Broad inverse algebraic-cycle constructions have uninspected historical specializations; priority risk is explicitly retained and is not asserted absent merely from a negative query.

## value

PASS

PASS: the natural threshold immediately above a strong cubic/quartic impossibility theorem is attained by an explicit constrained and biologically interpretable construction. The sign-definite transverse exponent certifies an open parameter family of actual isolated attracting cycles rather than relying on invariant curve membership or numerical evidence. No global basin, uniqueness or other-cycle claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
