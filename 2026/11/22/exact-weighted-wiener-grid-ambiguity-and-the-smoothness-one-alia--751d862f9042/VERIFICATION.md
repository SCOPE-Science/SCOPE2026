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

Absolute coefficient summability justifies finite-group Fourier inversion at the sampling nodes. The translate only changes coefficient phases; invisibility is exactly a zero sum in each annihilator class. For a class with total coefficient mass L, zero sum gives each magnitude at most L/2. If u and v are the two lowest weights, at most L/2 mass can benefit from the smallest weight u, so class cost is at least (u+v)L/2 and squared L2 mass is at most L^2/2. Equality in the latter requires exactly two equal nonzero magnitudes, and then the former requires exactly a pair of least total weight, with opposite adjusted phases. Across classes the sum of squared costs is at most the square of total cost, strictly so for multiple active classes. Proper weights ensure an attained minimum; a pair witness of cost one proves sharpness. For a differing coordinate of a rectangular-grid alias pair, |k_j|+|ell_j| >= |k_j-ell_j| >= m_j, so one can choose nonnegative integers a and m_j-a no larger than those magnitudes. Strictly increasing factors force equality only when the pair already straddles zero at separation m_j, and every transverse coordinate vanishes on both frequencies. Concavity, linearity, or convexity of the one-coordinate cost gives exactly the listed endpoints, all integers, or the central integer(s), respectively, with the lists coinciding when m=1. Rescaling differences by two proves the diameter and ± extremizers give the recovery lower bound. The one-dimensional constants follow from F_m directly. Moeller's Theorem 7.4 with d=1, theta=1 and q=2 has r>0 and gives the asserted log-power upper bound for arbitrary optimized locations, hence the fixed-grid loss lower bound of order m^(1/2)/(log m)^(3r+3/2).

## originality

PASS

On the inspected evidence the fixed-grid sharp nullspace radius and full extremizer and transition description are distinct from optimized sampling-width bounds, sparse-grid approximation estimates and mode transitions in other spaces. Fourier inversion and elementary discrete convexity are credited ingredients, and the faster optimized-sampling bound is prior work, not claimed here.

## value

PASS

The zero-fiber radius is a canonical, algorithm-independent limitation of prescribed grids. The exact sharp constant at every size and the rigidity of its two-frequency witnesses identify which information the design loses, including the change from endpoint to centered aliasing and its coordinatewise role in anisotropy. The exact finite subgroup version and quantitative comparison with optimized point sampling give practical meaning to the invariant beyond a routine aliasing computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
