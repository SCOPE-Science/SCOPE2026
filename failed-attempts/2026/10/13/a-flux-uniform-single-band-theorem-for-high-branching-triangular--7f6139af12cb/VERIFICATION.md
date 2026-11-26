---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The magnetic Schur complement across the other two vertices has numerator 2(y+c) and denominator y²−1; the uniform regular incidence tree gives y=z−(m−1)h. Its upper-half-plane branch has Im y>0 and G=(m−1)/(my−z). Independently recomputing both discriminants gives exactly the frozen formulas. For |c|<1 the quartic discriminant is negative and D(0)<0, hence exactly two simple real zeros; between them, the unique real cubic root is in (−1,1) with positive y-derivative of the cubic. Its derivative as a function of energy is negative, ruling it out as the upper-half-plane branch, so the density is strictly positive there. Where the cubic roots are distinct and real, the resolvent has real boundary values except at possible isolated poles. Ordinary edges follow from the simple discriminant zeros: the double root is not ±1, so the E-partial does not vanish and the inverse has a square-root term. To check that G does not turn it into an inverse square root, write E=H(y)=y+2(m−1)(y+c)/(y²−1). If my−E=0 then y³−3y−2c=0, and substitution gives H′(y)=3−2m≠0, impossible at the double root. Also the derivative of G in y is nonzero there. At c=1 the physical quadratic has edges 1±sqrt(8(m−1)); G=(y−1)/((y−2)(y+1)), with regular edges except y=−1 at m=3. Its expansion gives the coefficient sqrt(2)/(3π); sign reversal handles c=−1. The algebraic resolvent has possible singular support only at finitely many real exceptional points, and the free-power atom threshold excludes all atoms since the largest input atom is at most 2/3 and m≥3. The trace is faithful, or equivalently all site diagonal spectral measures agree, so this gives full spectral support and pure absolute continuity of the operator, not just a single component of its spectral measure.

## originality

FAIL

The all-flux structural claim, not just the credited symmetric slice, is a direct corollary of Huang's free-power support and density theorem applied to the exact triangle law. Its Nevanlinna integral reduces to a two-term function whose level set has one component by an elementary inequality. The endpoint-flux laws, including the exceptional coefficient, are direct instances of the published free-binomial density. For generic flux the specific quartic is the routine discriminant elimination of the known subordination map, and the ordinary edge expansion follows from the map's simple critical points and a nonvanishing Cauchy denominator. No retrieved source is asserted to print this exact quartic in magnetic notation. The decision rests on the mathematical implication covering the physical conclusions, not on the literature access gaps.

## value

FAIL

The graph formulation is a useful exposition, but the claimed band, its spectral type, and the critical singularity are obtained directly from the prior general criterion and exact free-binomial law. The extra quartic presentation is the discriminant of the cleared universal map, not an independent new spectral invariant or previously unresolved transition. The threshold and edge profile would have clear scientific value if they were not mechanically implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
