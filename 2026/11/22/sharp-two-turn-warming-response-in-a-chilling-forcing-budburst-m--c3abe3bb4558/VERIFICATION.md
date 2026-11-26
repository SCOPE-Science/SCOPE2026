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

On the post-threshold spring ramp, H>0 fixes the positive square-root branch and gives the unique budburst date. For w<c put x=c−w, v=b exp(−x²/2), R=xv/√(2(h+v)). Then B′=−1+R, while B′=−1 at and beyond c (the one-sided limits agree because R(0)=0). With s=v/(h+v), (log R)_x=1/x−x(1−s/2), and s_x=−xs(1−s). Hence x²(1−s/2) increases strictly from zero to infinity; R has a unique strict peak and vanishes at both ends of x>0. Solving R=1 and R_x=0 gives v²−v−2h=0, v=y, x_c²=1+1/y, and b_c=y exp[(1+1/y)/2]. This explicit pair exists, and pointwise strict increase of R in b classifies max R below, at, or above one on the three ranges. At equality B′ vanishes only at w=c−x_c and B‴=R_xx<0 there; B″ changes sign and B is still strictly decreasing. Above equality the two x-roots are crossed in decreasing x, making the first w-turn a minimum and the second a maximum. Differentiation confirms d(log b_c)/dy=(2y−1)/(2y²)>0 and the auxiliary limits e and √(2eh). At the critical point g=log R has g_b=y/[b_c(y+1)] and g_xx=−(2y−1)/y. Rescale x−x_c by √(b−b_c); the limiting quadratic has two simple roots, yielding the stated γ and O(b−b_c) error. The finite tapered-winter integral equals x²/2 on 0≤w≤c, and c>x_+ puts both turns strictly inside it. None of this uses field validation or a rerun of the bundled checker.

## originality

PASS

The supported distinction is a global phase diagram for the specified combination of quadratic cold exposure, offset uniform warming, and quadratic accumulated spring forcing. The empirical exponential requirement, competing signs of chilling and forcing, and the generic square-root exponent are background. The nearest available primary statements concern model formulation, qualitative advance or delay, or empirical comparisons; none supplies the exact threshold or complete two-turn classification on the stated surrogate. The exact catalogue hit is the assigned record itself.

## value

PASS

The motivated question is whether a warming-driven advance can give way to a temporary delay and then return to advance when chilling and forcing compete. For this specified model, a numerical curve could suggest the shape but cannot certify either that no third turn is possible or exactly when the delay window first opens. The global threshold and the model-specific onset size make the switch interpretable, and the construction allows both extrema within one finite winter interval. This is useful as an exact model benchmark, not a forecast or measured tipping point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
