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

The signed harmonic rule gives a cell's two normalized slopes in [0,3] when its secant is nonzero, and gives two zero slopes when the secant is zero. The four corner derivative polynomials on [0,3]^2 are nonnegative, so the cell preserves variation. For a perturbation of one secant, the same corner test applies to the central response; its variation is exactly the cell length times the absolute secant change. Each outer cell contributes its length times the absolute knot-slope response times 8/27, twice the absolute extremum of its Hermite shape function. The respective harmonic partial-derivative bounds are 3(l+r)/(r+2l) and 3(l+r)/(2r+l); changing sign gives no extra mass because the piecewise selector is continuous and absolutely continuous on each coordinate line. Weighting by the neighboring cell lengths gives precisely Phi on both sides. Finite telescoping and cellwise convergence (with Fatou for the variation sum) give the global bound for summable differences. The one-secant witness with both neighbors equal to 1, as that secant goes from zero to epsilon, simultaneously approaches both derivative bounds. This also proves infinite coefficient if the neighbor ratios are unbounded. For finite K, isolate one nonzero secant difference first: integrating its strict derivative bounds gives a strictly sub-K contribution, and the global bound on the remaining, possibly infinite, differences preserves that one strict deficit. This fills in the infinite-difference nonattainment step; inputs differing only by a constant are outside the quotient. Phi(1)=2 and the (2,1,3) factor is 377/105, not Steffen's 107/27. Targeted rational check: python3 /workspace/reviews/evidence/reproduce.py, output 1. The uploaded finite checker was inspected, not executed. The result concerns the fixed-grid interior rule, not finite-endpoint PCHIP.

## originality

PASS

The formula for the selector and one-input monotonicity are known, as are the uniform-grid coefficient and near-flat mechanism. The supported distinct claim is the exact length-weighted BV coefficient for the nonuniform Brodlie rule, including the simultaneous sharp limits of the two knot responses and nonattainment. The closest distinct same-day PCHIP finding optimizes a pointwise ordinate sup-norm, not BV. The nonuniform Steffen result does not transfer the harmonic derivative bounds or the strictness.

## value

PASS

On a standard nonuniform interpolation rule, this separates shape preservation from perturbation stability, identifies exactly when the latter is finite, and quantifies the worst amplifying mesh configuration. The nonlinear coefficient and strict nonattainment are practically and mathematically distinct from the known equal-mesh value and Steffen law. The individual three-length evaluation illustrates that distinction rather than serving as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
