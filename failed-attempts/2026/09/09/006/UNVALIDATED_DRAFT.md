# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified minimal growth rate in a rank-3/4 Coxeter window

## Claim (headline theorem)

Fix the following 7 connected Coxeter systems (matrices in `series.json`;
labels: `A=[3,3,4]`, `B=[3,3,5]`, `C=[3,4,4]`, `D=[3,3,∞]`, `E=[2,4,∞]`,
`F`=rank-4 (`[3,3,4]` triangle + pendant `m=3`), `G`=rank-4 path `[3,4,∞]`).
Each is infinite, non-spherical, and non-affine (every member contains a
hyperbolic-triangle or infinity-edge parabolic; no affine diagram contains one).

Let `a_n` = number of words of length `n` and `ω = limsup a_n^{1/n}` (growth
rate). Then, with the certified intervals below,

- `ω(A) ∈ [1.40126836, 1.40127916]`,
- `ω(E) ∈ [1.46557123, 1.46557279]`,
- `ω(B) ∈ [1.50613567, 1.50614643]`,
- `ω(C) ∈ [1.58234718, 1.58235381]`,
- `ω(D) ∈ [1.61803398, 1.61803522]`,
- `ω(G) ∈ [1.66040772, 1.66041023]`,
- `ω(F) ∈ [1.74243322, 1.74243756]`,

so `A` (triangle `[3,3,4]`) is the unique minimal-growth system in this window,
separated from the runner-up by the certified gap
`ω(E)_lo − ω(A)_hi = 0.064292… > 0`, and from every other member by a larger
positive gap. Each interval has width at most `1.1×10⁻⁵`.

## Method (proof sketch)

1. **Exact Steinberg series.** For each system enumerate all spherical subsets
   `T` (finite-parabolic test: infinity edges excluded; pairs `I₂(m)`; triples
   by the `A₃/B₃/H₃` path criterion `(3,3)/(3,4)/(3,5)`; all other triples and
   4-sets infinite). Form `g(t) = Σ_T (−1)^|T| t^{ℓ_T}/W_T(t) = 1/W(t)` with
   classical finite-type denominators and longest-element shifts `ℓ_T`, reduce
   the common factor, and obtain `W(t) = N(t)/Q(t)` with `N(0) = Q(0) = 1`.
   Sanity: `g(0) = 1`, series coefficients nonnegatively integral, exponential
   (`a₁₄ > 50`), and the construction reproduces the known series of `C₂³` and
   of the infinite dihedral group.
2. **Smallest-pole lower bounds.** `Q`'s smallest positive zero `r ∈ [a,b]` is
   isolated by scanning plus exact Sturm counts (`0` roots in `(0,a]`, exactly
   `1` in `[a,b]`, bisection to width `10⁻¹²`). Since `r` is a pole,
   `R ≤ b` and `ω ≥ 1/b`.
3. **Convergence-radius upper bounds.** For rational `ρ`, the number of zeros
   of `Q` in `|z| < ρ` is computed by a rigorous argument-principle winding
   count: `512–4096` midpoint boxes on the circle with second-order radius
   `M₂(dθ/2)²/2`, each box proved to avoid `0`, consecutive angular steps
   proved unambiguous, total slack `< π`. Count `0` certifies `R > ρ`, i.e.
   `ω < 1/ρ`. Bisection gives `ρ` within `10⁻⁹` of `R`.
4. **BFS cross-check.** Exact Tits reflection representation over `ℚ`/`ℚ(√2)`
   (`B(eᵢ,eⱼ) = −cos(π/m)`, `−1` for `m = ∞`); Cayley-sphere counts from the
   identity agree with all series coefficients to length `12`.
5. **Ordering.** Interval arithmetic gives the minimum and all gaps; the
   smallest gap (`0.064292…`) is certified positive as a difference of exact
   fractions.

## Evidence summary

- `output/artifacts/series.json`: exact `W` numerators/denominators, Sturm
  brackets, exact series `a₀…a₁₄`, spherical-subset tables per system.
- `output/artifacts/omega.json`: certified `R`/`ω` brackets, ordering, gap data.
- `output/artifacts/compute_series.py`, `certify_radii.py`, `bfs_check.py`:
  replay scripts (stdlib + sympy); `verify.py`: independent replay printing
  `VERIFY_OK` (rebuilds series/polys, rechecks Sturm counts, rechecks winding
  exclusion at fresh arc counts, rechecks all gaps).

## Per-system table (exact, abbreviated)

| sys | W denominator `Q` | `a₁₂` | `ω` interval |
|-----|-------------------|-------|--------------|
| A | `1−t²−t³−t⁴+t⁶` | 240 | [1.40126836, 1.40127916] |
| E | `1−t−t³` | 249 | [1.46557123, 1.46557279] |
| B | `1−t−t³−t⁵+t⁶` | 444 | [1.50613567, 1.50614643] |
| C | `1−t²−2t³−t⁴+t⁶` | 726 | [1.58234718, 1.58235381] |
| D | `1−t−t²` | 754 | [1.61803398, 1.61803522] |
| G | `1−t−t³−t⁴−t⁶` | 1777 | [1.66040772, 1.66041023] |
| F | `1−t−t²−t⁴+t⁸` | 3711 | [1.74243322, 1.74243756] |

## Limitations / uncertainty

- Scope is the committed 7-system window (minimal-growth claim is relative to
  it, not global). Originality vs. the Terragni minimal-hyperbolic dataset and
  the Floyd/Kellerhals/Bredon minima rests on the admission triage, not on a
  fresh literature search in this pass.
- The winding-count upper bounds use floating-point midpoints with rigorous
  second-order remainder radii plus explicit slack accounting (not pure
  interval arithmetic); the logical certificate is machine-checkable via
  `verify.py` with independent arc counts.
- BFS checks spheres only to length `12` (audit-plan minimum); series extend
  exactly to `a₁₄`.
