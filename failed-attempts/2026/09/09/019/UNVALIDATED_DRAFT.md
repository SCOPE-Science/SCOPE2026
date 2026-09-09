# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Transverse systole crossover and separating-systole gap on a Bolza-symmetric twist arc in genus 2

## Theorem (tracked-family crossover; fallback-level partial result)
Fix the separating length `l0 = 2 arcosh(1 + sqrt(2))` and the arc
`tau in [-T, T]`, `T = 1/4`. Define `S = diag(E, E^-1)` with `E = exp(l0/2)`,
`Tw(tau) = diag(e^{tau/2}, e^{-tau/2})`, and the committed generators

- `X_A = [[1, 1/2], [-1, 1/2]]`, `Y_A = [[-1/2, -2], [1, 2]]`,
- `X_B = [[1, 1], [-1/2, 1/2]]`, `Y_B = [[-1/2, -1], [2, 2]]`,

with `A(tau) = X_A Tw(tau) Y_A Tw(tau)^{-1}`,
`B(tau) = X_B Tw(tau) Y_B Tw(tau)^{-1}`.
Put `l_A(tau) = 2 arcosh(tr A(tau)/2)`, `l_B(tau) = 2 arcosh(tr B(tau)/2)`,
`D(tau) = l_A(tau) - l_B(tau)`, `m(tau) = min(l_A(tau), l_B(tau))`. Then:

1. **Closed-form traces.** `tr_A(tau) = 1/2 + 2 e^tau + (1/2) e^{-tau}`,
   `tr_B(tau) = 1/2 + (1/2) e^tau + 2 e^{-tau}`, so
   `tr_B(tau) = tr_A(-tau)` and `D` is odd with `D(0) = 0` exactly.
2. **Unique transverse crossing.** `D` has exactly one zero `tau* = 0` on
   `[-T, T]`, enclosed in `[-0.01, 0.01]` (width `0.02`):
   `D(-0.01) in [-0.0268321359591406, -0.0268321359590413] < 0`,
   `D(0.01) in [0.0268321359590406, 0.0268321359591402] > 0`, and
   `D'(tau) >= 1.298 > 0` throughout, with
   `l_A'(tau) in [0.649, 2.404]`, `l_B'(tau) = -l_A'(-tau)`.
3. **Tracked systole intervals (width << 0.05).** At `tau = -T`, `0`, `+T`:
   `m(-T) = l_A(-T)`, `m(0) = l_A(0) = l_B(0)`,
   `m(+T) = l_B(+T)` (intervals below, widths ~1e-12), with disjoint
   leadership margins at the endpoints:
   - `l_A(-T)` vs `l_B(-T)` disjoint, `A` wins;
   - `l_B(T)` vs `l_A(T)` disjoint, `B` wins;
   - centre `l* = 2 arcosh(3/2) in [1.924847300238390, 1.924847300238441]`.
4. **Separating gap.** `l0 in [3.057129494723162, 3.057220511037126]`, so
   `l0 - m(tau) >= 1.132 > 0.05` for every `tau` on the arc
   (`m(tau) <= l(0)` by monotonicity + exact `D(0) = 0`).
5. **Derivative cross-check.** Exact-rational finite differences of the traces
   at step `h = 1/1000` agree with `d tr_A(0) = 3/2`, `d tr_B(0) = -3/2`
   (hence `D'_tr(0) = 3`) to better than `1e-6`.
6. **McShane-type spot check.** Summands `2/(1 + e^{l/2})` over the Dehn
   orbits `A_k = X_A S^k Y_A S^{-k}`, `B_k = X_B S^k Y_B S^{-k}`,
   `|k| <= 6`, are enclosed at `tau in {-T, 0, T}`; the geometric tail is
   certified `< 5.5e-9 < 1e-6`.

## What is proved vs what is not
- **Proved:** everything above, replayable from the committed rational
  matrices by `output/artifacts/verify_crossover.py` (stdlib only).
- **Computed evidence (not a theorem):** the McShane-type partial sums are
  reported as enclosed values with a certified tail, not as a proof of the
  full McShane–Mirzakhani identity residual (which would need the entire
  simple-length spectrum).
- **Explicit limitation:** minimality is certified *among the two tracked
  Dehn families* only — not over all simple closed geodesics. Global word
  exclusion was deliberately avoided (it is the failure mode of the blocked
  2D attempts). The separating gap is therefore stated against the tracked
  systole `m(tau)`. No claim is made about spine strata beyond this arc.

## Proof sketch
All generators have `det = 1` exactly over `Fraction`s; base words are
`alpha = X_A Y_A = [[0,-1],[1,3]]`, `beta = X_B Y_B = [[3/2,1],[5/4,3/2]]`,
both of trace `3`. Expanding `X Tw Y Tw^{-1}` with `Tw = diag(t, t^-1)`
gives `tr = X00 Y00 + X11 Y11 + (X10 Y01) z + (X01 Y10)/z`, `z = t^2`,
yielding the closed forms (coefficients `(1/2, 2, 1/2)` and mirror).
Trace `>= 2.699 > 2` on the arc, so both words are hyperbolic throughout.
Since every term of `tr_A''(tau)` is a positive interval, `tr_A'` is strictly
increasing; combining the tight endpoint trace-derivative intervals with the
denominator interval `sqrt((tr/2)^2 - 1)` gives `l_A' >= 0.649`,
`D' >= 1.298`, hence at most one zero; the endpoint sign reversal gives at
least one, inside `[-0.01, 0.01]`. Monotonicity plus oddness identifies the
winner on each side, giving the systole intervals. The Bolza length uses the
integer-verified `sqrt(2) in [1.4142, 1.4143]` (`14142^2 < 2*10^8 < 14143^2`).
Interval arithmetic is outward-rounded (`math.nextafter` padding plus a
generous libm allowance); all margins exceed interval widths by many orders
of magnitude. Exact facts used: mirror symmetry, `tr(0) = 3`,
`l* = 2 arcosh(3/2)`, `l_A'(0) = 3/sqrt(5)`, `D'(0) = 6/sqrt(5)`.

## Reproduction
Run `python3 output/artifacts/verify_crossover.py` (stdlib only). On success
it prints `VERIFY_OK` and writes `output/artifacts/certified_values.json`.
