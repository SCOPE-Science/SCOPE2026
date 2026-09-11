# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of Schmidt-winning on the rational line L0: the fiber is empty

**Target.** Decide whether `Bad(1/2,1/2) ∩ L0` with `L0 = {(x, x/2+1/3)}` is
`1/2`-Schmidt-winning in the line topology.

**Result.** The target claim is **false**, proved in the strong sense: the fiber
`Bad(1/2,1/2) ∩ L0` is **empty**, so no Alice strategy can force the limit
point into it. The empty set is not Schmidt-winning (Bob's first ball already
witnesses failure; equivalently, there is no point of the target set for the
intersection point to belong to).

## 1. Definitions (standard simultaneous normalization)

Write `||·||` for distance to the nearest integer. Under the standard
simultaneous sup-norm normalization used in the Davenport/An–Beresnevich–Velani
program,
`(x,y) ∈ Bad(1/2,1/2)` iff there exists `c > 0` such that for all integers
`q ≥ 1` and all integers `p, r`:
`max(|qx − p|, |qy − r|) ≥ c/q^{1/2}`,
i.e. `max(||qx||, ||qy||) ≥ c/q^{1/2}` for all `q ≥ 1`.
(Any equivalent normalization with the same exponent changes only the constant
`c` and leaves the argument intact; see §4.)

Parametrize `L0` by `t = x`, so points are `(t, t/2 + 1/3)`. Suppose for
contradiction that some `t ∈ ℝ` has `(t, t/2+1/3) ∈ Bad(1/2,1/2)` with constant
`c > 0`. Then for every `q ≥ 1`:
`max(||qt||, ||q(t/2+1/3)||) ≥ c/q^{1/2}`.  ...(★)

## 2. Resonant subsequence q = 6m collapses both errors to ||3mt||

Fix `m ≥ 1` and set `q = 6m`. Put `u = 3t`, so `3mt = mu`. Then:
- `qt = 6mt = 2mu`, hence `||qt|| = ||2mu||`.
- `q(t/2+1/3) = 3mt + q/3 = mu + 2m`, and `2m` is an integer, so
  `||q(t/2+1/3)|| = ||mu||` **exactly**.

Consequently at every `q = 6m`:
`max(||qt||, ||q(t/2+1/3)||) = max(||2mu||, ||mu||)`.  ...(1)

## 3. Doubling bound and Dirichlet finish the proof

For any `θ`, `max(||2θ||, ||θ||) ≤ 2||θ||`. Indeed, writing
`θ = n + δ` with `|δ| = ||θ|| ≤ 1/2`, `2θ = 2n + 2δ`, so
`||2θ|| ≤ |2δ| = 2||θ||` (if `|2δ| > 1/2` then `1 − |2δ| < |2δ|`, only
strengthening the inequality). Hence from (1):
`max(||qt||, ||q(t/2+1/3)||) ≤ 2||mu||` at `q = 6m`.  ...(2)

By Dirichlet's approximation theorem, for the fixed real `u = 3t` there are
infinitely many `m ≥ 1` with `||mu|| < 1/m`. For any such `m`, (2) gives
`max(||qt||, ||q(t/2+1/3)||) < 2/m` at `q = 6m`. The putative Bad constant `c`
requires, via (★), `≥ c/√(6m)` at the same `q`. But
`2/m < c/√(6m) ⟺ √(6m)·2 < c·m ⟺ m > 24/c²`
(dividing by `m > 0`: `2/m vs c/√(6m)` ⟺ `2√(6m) < cm` ⟺ `m > 24/c²`).
Since Dirichlet supplies infinitely many `m` with `||mu|| < 1/m`, all
sufficiently large ones exceed `24/c²` and violate (★). Contradiction.

Therefore **no** `t ∈ ℝ` satisfies (★) for any `c > 0`:
`Bad(1/2,1/2) ∩ L0 = ∅`.

## 4. From empty fiber to non-winning (game conclusion)

Schmidt's `(α,β)`-game (here `α = 1/2`, Bob starts with any ball, nested balls
with radii shrinking by `α`, `β` factors) is won by Alice iff the intersection
point lies in the target set. With target `S = Bad(1/2,1/2) ∩ L0 = ∅`, every
complete play has its limit outside `S`, so Alice has no winning strategy:
`S` is **not** `1/2`-Schmidt-winning (indeed not `α`-winning for any
`α, β ∈ (0,1)`). The target claim — existence of an Alice strategy with all
limit points in `Bad(1/2,1/2)` at uniform `c > 0` — is rigorously false.

*Normalization robustness.* The only properties of the exponent/constant used
are: the Bad exponent is `1/2 < 1` (so `1/m = o(1/√m)` defeats any fixed `c`),
and the resonant shift `q/3` is integral along `q = 6m`. Any equivalent norm
on the `(p,r)`-lattice (e.g. max vs Euclidean, shifted exponent conventions)
changes at most the threshold constant, not the conclusion. The fiber is empty
under every standard normalization.

## 5. Reproducible evidence

`output/artifacts/verify_fiber_empty.py` (stdlib only) replays:
- exact-rational resonant identity `||q(t/2+1/3)|| = ||3mt||` for `q = 6m`
  on sample slopes (exact `Fraction` arithmetic);
- exact doubling bound `max(||2θ||,||θ||) ≤ 2||θ||` on a 2000-point grid;
- the threshold implication `m > 24/c² ⟹ 2/m < c/√(6m)`;
- end-to-end explicit violation denominators `m` (e.g. `c = 0.5 → m = 12`,
  fiber max `≈ 0.05888 < 0.5/√72 ≈ 0.05893`; `c = 0.1` at `t = √2 → m = 136`,
  `t = π → m = 113`), run via `python3 output/artifacts/verify_fiber_empty.py`
  → `VERIFY_OK`.

## 6. Scope, originality, limitations

- The argument exploits the specific rational slope `1/2` and intercept `1/3`
  (`q = 6m` clears both denominators); it classifies the named line `L0` and
  does not claim anything about Diophantine or other rational lines.
- No literature search found this two-line empty-fiber certificate recorded for
  `y = x/2 + 1/3`; the admission review confirms the slice is in the explicitly
  excluded boundary of An–Beresnevich–Velani, so the negative resolution is
  original either as a winning-failure certificate or, more strongly, as an
  emptiness proof.
- Limitation: disproof is for the standard simultaneous-weight `(1/2,1/2)` Bad
  set; dual/multiplicative or Hausdorff-measure refinements are out of scope
  and untouched.
