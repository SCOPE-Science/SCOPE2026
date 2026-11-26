---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For n≥4, zero through three forward moves cannot reach the same column. In row i, a walk with k jumps contributes the product of the first k rates; the stays are distributed over the k+1 visited vertices, contributing the complete homogeneous polynomial in the negative rates. The quadratic diagonal is strictly positive; the one-hop entry changes sign at 2/(r_i+r_{i+1}). In the cubic, the diagonal is strictly decreasing in r_i h to and beyond its unique zero ρ, the one-hop bracket has discriminant −(5a²+2ab+5b²)/12 for a=r_i,b=r_{i+1}, and the two-hop constraint is h≤3/(r_i+r_{i+1}+r_{i+2}). The last hop is positive. Thus the horizons are exact, with no later reentry and row sums one. The inequalities M<A<C≤A+M<2A and ρ>3/2 give strict bounds. On the alternating and adjacent-fast four-cycles the triple constraint is active as the slow rates tend to zero, yielding the two distinct endpoints of the range. On the single-fast-state family the two constraint ratios cross 1 at R=1 and R=ρ/(2−ρ), respectively, giving precisely the stated ties and strict inequalities. An independent rational bisection gives ρ≈1.596071637983321523 and switch ≈3.951373035591441433. The prose's last printed digit in ρ is a rounding slip; the defining cubic, frozen check output and exact comparisons determine the result.

## originality

PASS

The exact quadratic horizon has stronger local coverage, and both the walk-expansion technique and the general principle of finding a positivity threshold are known. The distinct contribution is the sharp two-sided RK3/RK2 comparison for every positive rate profile, including both sharpness configurations and the contrast switch. The checked general step-size constructions do not yield this optimized comparison; related exact results change the order, graph, or wraparound regime.

## value

PASS

The largest completed positive step is a natural constraint on integration of a transition network. A strict sharp range showing that the higher-order method can win or lose, with a cheap local decision rule and a one-site contrast switch, is more informative than positivity of one method or examples at selected rates. The different spatial arrangements of fast rates explain the two limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
