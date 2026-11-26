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

The displayed C is the cumulative candidate; its survival term is exp(−x−y−t) with x=−log(1−u), y=−log(1−v), t=φx^a y^b. The exponential correction is bounded by (1−u)(1−v), giving continuity even at the unit sides; the other sides are grounded and both margins are uniform. The interior mixed derivative has sign of H=(x+at)(y+bt)−ab t, by the chain rule. A negative interior value violates two-increasingness on a small rectangle; a nonnegative interior derivative extends the rectangle inequalities to the boundary by continuity. If a<1, fix 0<y<b; x^(−a)H→φa y^b(y−b)<0 for every positive φ, and the same argument with coordinates exchanged excludes b<1. For a,b≥1 and φ>0, set r=x/(at), s=y/(bt), m=a+b−1. The inverse is t=(φa^a b^b r^a s^b)^(−1/m), x=art, y=bst, onto the whole positive quadrant. The sign restriction becomes φ≤(1+r)^m(1+s)^m/(a^a b^b r^a s^b) for every r,s>0. Each one-variable minimum is global, at r=a/(b−1) and s=b/(a−1) when the denominators are positive and at the corresponding infinity limit otherwise. Multiplication yields exactly Φ. Equality is allowed whether or not the infimum is attained; any strict violation admits finite positive r,s with negative density. At φ=0 the candidate is uv without exponent restrictions. I checked Φ(1,3)=1/4 and verified by exact fractions H(4/9,4/9)=0 at (a,b,φ)=(2,2,729/256) versus −37232/4782969 at φ=3. A half-power witness gives H=−4573/8000000 at (a,b,φ,x,y)=(1/2,1,1/2,1/10000,1/2).

## originality

PASS

Neither the candidate family nor the classical a=b=1 Gumbel–Barnett bound is new. The inspected material supports as distinct the sharp all-positive-real-exponent iff classification, particularly the exclusion of every subunit exponent at positive coupling and the nontrivial asymmetric positive domain. The closest broader two-function paper remains a specific limited-access priority risk.

## value

PASS

The candidate was introduced as a model for bivariate failures. Nonnegative rectangle probabilities are a prerequisite before fitting or interpreting it. The complete classification corrects a use of subunit exponents, supplies sharp admissible couplings for genuine asymmetric cases, and distinguishes a forbidden parameter region from a merely small dependence regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
