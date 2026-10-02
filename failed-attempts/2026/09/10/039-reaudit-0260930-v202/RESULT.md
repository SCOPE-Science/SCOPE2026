# Uniform Steklov gap bound in a symmetric three-boundary-component circular-pants cell

## Context

Steklov isoperimetric inequalities bound the normalized first-nonzero Steklov
eigenvalue `S(Ω) = σ₁(Ω)·L(∂Ω)` in terms of topology. The Weinstock inequality
settles the simply-connected planar case (`S ≤ 2π`, sharp for the disk).
Fraser–Schoen and Girouard–Polterovich proved the general orientable-surface
bound `σ₁·L ≤ 2π(γ+l)` (genus `γ`, `l` boundary components), hence the lane
baseline `B₀ = 6π` at `(γ,l,k) = (0,3,1)`. This general bound is not expected
sharp except at `(0,1)` and decides no fixed conformal-modulus subcell.
The exact gap for planar triply-connected domains in a fixed modulus cell is
undecided by the general bounds.

## Definitions

- `M = { Ω_r : r ∈ [0.20, 0.35] }` with
  `Ω_r = { |z| < 1 } ∖ ( { |z−0.5| ≤ r } ∪ { |z+0.5| ≤ r } )`
  (unit disk minus two closed equal disks with fixed symmetric centers `±0.5`).
- `L(r) = L(∂Ω_r)`, `S(Ω_r) = σ₁(Ω_r)·L(∂Ω_r)`.
- `B₀ = 6π`: instantiated Girouard–Polterovich Thm 1.2 /
  Fraser–Schoen bound at genus `0`, `b = l = 3`, `k = 1`.
- Steklov variational principle on Lipschitz domains:
  `σ₁(Ω) = inf { ∫_Ω|∇v|² / ∫_{∂Ω}v² ds : 0≠v∈H¹(Ω), ∫_{∂Ω}v ds = 0 }`.

## Result

**Theorem.** For every `r ∈ [0.20, 0.35]`,

```
sup_{Ω_r ∈ M} σ₁(Ω_r)·L(∂Ω_r) ≤ 161π/76 ≈ 6.655 ≤ B₀ − 0.10.
```

In fact `B₀ − 161π/76 − 0.10 = 295π/76 − 1/10 ≥ 295·3/76 − 1/10 > 11`
(using only `π > 3`), so the margin over the required `B₀ − 0.10` exceeds 11.

## Proof / Evidence

This is proof (closed forms plus exact rational monotonicity), not numerical
evidence.

1. **Geometry.** For `r ≤ 0.35`, `0.5+r ≤ 0.85 < 1` and `2r ≤ 0.7 < 1`,
   so each `Ω_r` is a bounded connected Lipschitz domain with three boundary
   components. `L(r) = 2π + 2πr + 2πr = 2π(1+2r)`.

2. **Admissible trial.** `u(x,y) = x` satisfies `u ∈ H¹(Ω_r)`, `|∇u|² = 1`,
   and `∫_{∂Ω_r} u ds = 0` exactly: the outer circle contributes `0` by odd
   symmetry and the inner circles contribute `2πr·(±0.5)`, summing to `0`
   by the `±0.5` symmetry. Hence `u` is admissible and
   `σ₁(Ω_r) ≤ D(r)/N(r)` with `D = ∫|∇u|²`, `N = ∫_{∂Ω}u² ds`.

3. **Closed forms.** `D(r) = area(Ω_r) = π(1−2r²)`. On the outer circle
   `∫₀^{2π} cos²θ dθ = π`; on inner circle at center `c = ±0.5`,
   `∫₀^{2π}(c+r cosθ)²r dθ = 2πrc² + πr³`. Summing both centers:
   `N(r) = π(1+r+2r³)`. Therefore
   `S(r) ≤ F(r) := 2π(1+2r)(1−2r²)/(1+r+2r³)`.

4. **Uniform monotonicity.** Write `F = 2π·A/B` with `A = (1+2r)(1−2r²)`,
   `B = 1+r+2r³ > 0`. Then `sign(f′) = sign(N_f := A′B − AB′)` with
   `A′ = 2−4r−12r²`, `B′ = 1+6r²`, and exact expansion (the `r⁵` terms
   `−24r⁵+24r⁵` cancel) gives `N_f(r) = 1−4r−20r²−16r³+4r⁴`.
   `N_f(1/5) = −451/625 < 0` exactly, and
   `N_f′(r) = −4−40r−48r²+16r³` satisfies
   `sup_{[0.2,0.35]} N_f′ ≤ −4−40(0.2)−48(0.2)²+16(0.35)³ = −13.234 < 0`,
   so `N_f` is strictly decreasing hence negative on the whole interval.
   Thus `F` is strictly decreasing and
   `sup_M S ≤ F(0.2) = 161π/76` (with `A(1/5) = 161/125`,
   `B(1/5) = 152/125`).

Method note: the lane text suggested an annular-log trial plus capacity
quotient plus symmetrization; the certificate above is the classical
Weinstock coordinate-trial leg (the symmetric centers make the boundary mean
of `x` vanish exactly), which already beats `B₀ − 0.10` by ~12 units, so no
logarithmic refinement was needed.

## Limitations

- Upper bound only; far from sharp; no extremal identification.
- Uses the lane-admitted baseline datum `B₀ = 6π` at `(γ=0,b=3,k=1)` rather
  than re-proving Girouard–Polterovich / Fraser–Schoen.
- Applies only to the named symmetric cell (fixed centers `±0.5`,
  `r ∈ [0.20, 0.35]`); not a general `(γ,b)` theorem.
- Must not be read as sharp or as resolving the full `b = 3` extremal problem.

## Reproducibility

Run `python3 output/artifacts/replay.py` (stdlib only: `fractions` exact
rational arithmetic plus a float cross-check). It asserts the polynomial
identity for `N_f` with exact `r⁵` cancellation, `N_f(1/5) = −451/625`,
`sup N_f′ < 0`, `f(0.2) = 161/152`, margin `≥ 11`, and a float grid check
that `max F = F(0.2)` with `B₀ − F(0.2) > 12.0`; prints `VERIFY_OK`.
Independently re-executed during audit: `VERIFY_OK`.

## References

- A. Girouard, I. Polterovich, Upper bounds for Steklov eigenvalues on
  surfaces, arXiv:1202.5108 (Thm 1.2: `σ_k L ≤ 2π(γ+l)k`; Thm 1.4).
  https://arxiv.org/html/1202.5108v1
- A. Fraser, R. Schoen, The first Steklov eigenvalue, conformal geometry,
  and minimal surfaces, Adv. Math. 226 (2011).
  https://geometrysummer.math.uconn.edu/wp-content/uploads/sites/2312/2018/07/FS1.pdf
- R. Weinstock, Inequalities for a classical eigenvalue problem,
  J. Rational Mech. Anal. 3 (1954).
- J. Hersch, L. Payne, M. Schiffer, Some inequalities for Stekloff
  eigenvalues, Arch. Rational Mech. Anal. 57 (1975).
- F. Oudet, C.-Y. Kao, B. Osting, Computation of free boundary minimal
  surfaces via extremal Steklov eigenvalue problems, ESAIM COCV 2021.
  https://www.numdam.org/articles/10.1051/cocv/2021033/
- B. Colbois, A. Girouard, C. Gordon, D. Sher, Some recent developments on
  the Steklov eigenvalue problem, arXiv:2212.12528.
