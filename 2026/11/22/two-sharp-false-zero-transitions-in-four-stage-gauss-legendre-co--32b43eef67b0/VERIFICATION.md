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

Constructed P independently as ∑_{j=0}^4 (−1)^j x^(4−j)L4^(j)(t) from the collocation residual. P(x,0)>0, and Gaussian quadrature applied to the difference V of two candidate polynomials gives V(1)^2/2+x∑ b_i V(c_i)^2=0, proving uniqueness (at x=0 use V′≡0). The endpoint numerator has the stated strictly positive sum-of-squares identity. For x>0, the derivative of e^(xt)Y_x is a positive multiplier of L4, so only node sign changes can change the interval root count. Any zero at a node is exactly double, since the derivative of L4 is nonzero there. The resultant of L4 and P−x⁴L4 in t, made monic in x, was independently computed as F(x²); exact Sturm variations at 0,26,27,104,105,+∞ are 4,4,3,3,2,2, and the roots are simple. The resultant as a product of node values excludes simultaneous contacts. Rational interval evaluation in the isolated Gauss nodes gives sign patterns ++++, +++−, +−+− at x=1,6,12. Thus between the two parameter contacts the fourth node alone is negative, and after the second the second node is negative too. Strict monotonicity on each nodal span and positive endpoints give all claimed zero counts, the c4 then c2 contacts, and nonnegativity precisely on [0,x1] (strict positivity only for x<x1). Replay `python3 /workspace/branches/independent_certificates.py 2`; the exact certificates and argument, not sample-based extrapolation, cover the continuum.

## originality

PASS

The supported distinct finding is the full-step scalar sign and root classification for the raw four-stage Gauss collocation polynomial. Endpoint Padé positivity, generic SSP barriers and event bifurcations in other interpolants or Markov stage maps are known but not equivalent. The most plausible inaccessible spline dense-output source remains an explicit priority risk.

## value

PASS

A classical stiff scalar test exposes a meaningful failure of numerical event detection: a method whose end value never becomes negative can introduce two false event pairs inside a single raw step. The exact thresholds, nodal locations and distinction between nonnegativity and strict positivity make this a usable diagnostic for the natural unmodified method, not a mere recomputation of Padé endpoint positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
