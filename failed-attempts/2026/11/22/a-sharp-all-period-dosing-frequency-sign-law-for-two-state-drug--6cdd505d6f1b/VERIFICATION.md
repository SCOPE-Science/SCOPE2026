---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a traceless strictly positive-off-diagonal real 2×2 generator part, its square is (d²+pq)I. The centered propagator product has determinant one and half-trace C=cosh(uT)cosh(vT)+h sinh(uT)sinh(vT), with u=aφ, v=b(1−φ). Strict positivity gives a simple pair of positive eigenvalues, and h>−1 follows from ab>|d_A d_B| and the positive off-diagonal cross-terms. Writing C as the affine combination of cosh(T√x) at x=(u+v)² and x=(u−v)² with weight (1+h)/2 shows strict Jensen for h<1 and strict secant extrapolation for h>1; the averaged eigenvalue uses that same affine combination in x before applying cosh. Thus the exact sign and equality case hold. Computing the T⁴ discrepancy between C and cosh(qT) gives (1−h²)u²v²T⁴/6; dividing by the leading arcosh derivative denominator qT and by T yields the stated quadratic correction. The coefficient of the fastest cosh is positive, so the long-period limit is the duty-weighted average of the phase exponents. The witness gives a²=5/4, b²=7 and ab h=3; its two endpoint exponents have opposite signs by the stated rational square comparisons. For the other sign one can take equal positive switching rates with dose-dependent sensitive growth and fixed tolerant growth: the symmetric traceless parts are nonparallel, giving h<1. The saturating-law witness lies in the frozen assumptions, which do not require the tolerant growth rate to exceed the active one under the selected dose.

## originality

FAIL

The main all-period sign law is a direct corollary of an older arbitrary-2×2 trace identity after substituting the two phase exponentials and taking the dyadic fast-period limit. The distinct four-pulse catalogue result gives the explicit spectral substitution and shift-based reversal mechanism in a related two-phenotype class. The mathematics therefore overlaps beyond matching terminology or a numerical parameter; no within-day priority is inferred. The exact frozen numbers and its convex proof are not a new independent sign theorem.

## value

PASS

Whether the sign of net growth survives taking the infinitely rapid approximation at fixed generators and treatment fraction is a meaningful stability question. The exact example translates the sign comparison into opposite qualitative forecasts in a specified rate model, not merely a small numerical change. Scientific motivation and explanatory use are real even though the law is covered and the particular parameters do not constitute a separately validated new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
