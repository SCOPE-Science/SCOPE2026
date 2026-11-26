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

For r>0 and 0<β≤1/2 at unit translation spacing, the zero-offset Ron–Shen duality relation requires sum over integer shifts of g_r h equal to β almost everywhere (conjugation is immaterial with this real g_r and real right side). For arbitrary Bessel duals it involves only h on [−1,1]. Conversely every bounded fiber solution supported there is Bessel and obeys all duality relations: for a nonzero offset the displacement is at least 1/β≥2 and the closed supports have at most a null intersection. At β=1/2 this still holds. Besselness follows by applying Fourier-series Parseval at period 1/β to each translated bounded window (support length at most that period) and summing the finitely overlapping unit shifts. Folding the two half periods gives a>b>0 with a=(1−x)^r, b=x^r. The cap is feasible exactly when T(a+b)≥β almost everywhere, which reduces by continuity and concavity/convexity to the stated inclusive T_min. For s=|U|, the complex fiber objective is at least s+|β−as|/b. This is strictly decreasing before β/a and increasing after it. The unique minimizer s=min(T,β/a) is positive, equality fixes U to that positive real value, and the resulting V is nonnegative and at most T. Any nonzero part outside [−1,1] strictly raises L1; the equal-weight fiber is null. Both sites are forced when aT<β; otherwise the minimizer uses just the stronger site. Counting those fibers gives the exact support bound and simultaneous attainment, including T=T_max. Integrating the optimizer on the two regions gives the claimed Pareto integral and its saturated value. Differentiation has no moving-boundary term since the pieces meet; the remaining integral is negative and strictly increases as the positive lower limit u rises. For r=1 the formula at t=1+ε simplifies to F1/β=2+2ε log(2ε)+(2−2ε)log(1+ε)−2ε, so its quadratic correction is −3ε². For 0<r<1 the slope increment is asymptotic to 2u^(1−r)/(1−r), u~ε/r, yielding the stated fractional coefficient after integrating in T. For r>1 the first feasible u is positive, giving a finite slope. The uploaded checker was inspected, not run: its loops specify 45+6 curve comparisons, while VERIFICATION.md records 46 and RESULT.md says 51. This documentation discrepancy is not used in establishing the result.

## originality

PASS

Credit unrestricted minimum-L1/support theory and its immediate saturated-cap specialization to Díaz Martín et al. The supported distinct claim is the binding-cap norm and support law with one common optimizer, including the boundary expansions. General numerical convex optimization and a box-window norm/support tradeoff are precedents, but neither inspected statement supplies this finite-cap analytic classification. Access to decisive theorem passages was limited, as described below.

## value

PASS

A hard peak bound on a synthesis dual is a concrete constraint for bounding synthesis amplitudes under coefficient perturbations. The result determines exactly when it is feasible, what extra L1 cost and support it imposes, and that a single unique L1 optimizer achieves minimum support as well. The difference between a finite slope and a logarithmic cusp explains sensitivity near the least feasible cap. These are specific design quantities for the binding region, not a restatement of the unrestricted L1 theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
