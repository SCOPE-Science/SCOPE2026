# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Scale dichotomy for permutation-matrix microstates of the plain-lamplighter Bernoulli tuple

## Claim
Freeze `G0 = (Z/2)^{(F2)} rtimes F2`, `M0 = L^infty([0,1]^{G0}) rtimes G0`
(Bernoulli), `X = (u_a, u_b, v_e)` with `v_e` the order-2 lamp at the identity,
and the frozen scale `eps0 = 1/10`, `delta0 = 1/100`, `c1 = (ln 2)/16`.
Microstates are permutation matrices for `(u_a, u_b)` plus diagonal `+-1`
sign matrices for `v_e`; test datum D0 = 52 reduced group words of length
`<= 3` (target trace 0), `tr(V) = 0`, mixed moments `tr(U_w V) = 0` for
`|w| <= 2`, plus exact relations `V^2 = I`, unitarity, lamp commutation
(exact by construction). Then:

(a) **k = 12 certificate (VERIFY_OK).** There exists an explicit base pair
`(Pa, Pb)` (archived in `artifacts/base_k12.json`) for which every one of the
52 test words is fixed-point-free, so every group-word defect is EXACTLY 0
(`< delta0`); `tr(V) = 0` and every mixed moment is 0 for ALL `C(12,6) = 924`
balanced sign patterns (since every `|w| <= 2` word is fixed-point-free).
The 924 microstates are pairwise at distance-squared `>= 8/12 = 2/3`
(distinct balanced diagonals differ in `>= 2` coordinates, `d^2 = 4m/k`),
hence `1/10`-separated (`2/3 >> 1/100`). Since `924 >= exp(c1*144) = 512`,
the fixed-scale packing bound holds at `k = 12` for this ansatz.

(b) **k = 6 impossibility inside the ansatz.** NO pair `(Pa, Pb)` in
`S6 x S6` makes all 52 test words fixed-point-free. Proof: simultaneous
conjugation `(Pa,Pb) -> (s Pa s^{-1}, s Pb s^{-1})` preserves every fixed-point
count, so it suffices to check one `Pa` per S6 conjugacy class (11 cycle
types) times all 720 `Pb` = 7920 checks, done exhaustively. Zero pairs fully
succeed; the best total fixed-incidence count is 12 (types `(2,2,2)`,
`(2,4)`, `(6,)`). Because `delta0 = 1/100 < 1/6`, any admissible defect would
have to be exactly 0, i.e. fully fixed-point-free — impossible. Hence no
permutation-matrix `(1/100, 6)`-microstate exists for the frozen datum D0.

(c) **Counting crossover.** The balanced-sign family gives `2^{k-1}`-type
growth (`C(12,6) = 924`), which exceeds `exp(c1 k^2)` at `k = 12` but falls
below it for every `k >= 15` (`2^{k-1} < 2^{k^2/16}`). So the exhibited family
cannot supply the closed-form extension to all `k >= 6` required by the exact
fallback; that extension needs a new counting idea.

## What is NOT claimed
- No claim about the full Bernoulli-vs-profinite gap (profinite-side covering
  bound untouched).
- No claim that the exact preset fallback holds (its k=6 half fails in-ansatz;
  its all-k extension fails for this family).
- No claim that k=6 certificates with genuinely non-permutation unitaries are
  impossible — only the permutation-matrix ansatz is closed.

## Replay
- `python3 output/artifacts/verify_k12.py` -> `VERIFY_OK` (seconds, stdlib).
- k=6 no-go: `output/artifacts/proof_k6_nogo.json` (11 classes, 0/7920 zero
  pairs); regeneration loop documented in WORKLOG Step C (stdlib, ~1 min).

## Prior-work separation
Hayes 1505.06682 gives existential positivity, never explicit fixed-scale
numbers for this tuple; Popa-Vaes 1111.6951, Chifan-Ioana-Osin-Sun 2111.04708,
Ding 2404.08182 state no microstate packing numbers. The k=12 explicit
packing count and the k=6 exhaustive no-go appear in none of them and do not
follow mechanically from any existential rate.
