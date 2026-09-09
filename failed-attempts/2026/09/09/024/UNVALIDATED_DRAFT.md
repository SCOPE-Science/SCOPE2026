# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified exact-rational SRG feasibility census, 51 ≤ v ≤ 100

## Result

Let a *count solution* be an integer quadruple `(v,k,λ,μ)` with
`51 ≤ v ≤ 100` satisfying the SRG count equation
`k(k−λ−1) = (v−k−1)μ`. There are exactly **10098** such quadruples.

**Theorem (verified census).** Of the 10098 count solutions:

- **277** have feasible spectra (266 integral type, 11 conference type);
- **9821** are excluded by exact spectrum arithmetic, each with a logged
  reason (`nonintegral-multiplicity`, `conference-numerator-nonzero`,
  `half-integer-eigenvalue`, `eigenvalue-sign`, `nonpositive-multiplicity`,
  `D<=0`);
- of the 277, exactly **15** integral quadruples fail a Krein inequality
  (`q_11^1 < 0` or `q_22^2 < 0` in every case) and exactly **18** fail the
  absolute bound; no conference quadruple fails either test;
- **106** primitive quadruples pass *both* the Krein and absolute-bound
  tests (all 11 conference survivors are primitive and pass);
- the four catalogue open cases checked —
  `(69,20,7,5)`, `(85,30,11,10)`, `(99,14,1,2)`, `(100,33,8,12)` —
  all **survive** both tests, so no elimination is claimed for any of them.

All Krein numbers `q_ij^k` were computed in exact `Q(√D)` pair arithmetic
with the correct relation-valency weights `(1,k,v−k−1)`, and every integral
case was additionally cross-checked by an independent plain-`Fraction`
computation from the restricted eigenvalues; all 266 agree, and all
`√D`-leftover parts vanish (277/277). Krein entries `q_11^0 = f` and
`q_22^0 = g` reproduce the multiplicities exactly (internal consistency
check). The absolute-bound data `f(f+3)/2`, `g(g+3)/2` are exact integers;
no bound is tight in the window (0 tight cases).

## Headline tuple (69,20,7,5): exact data, no elimination

For `(v,k,λ,μ) = (69,20,7,5)`: `t = 2`, `D = 64`, `r = 5`, `s = −3`,
`f = 23`, `g = 45`. Exact Krein numbers of interest:

| coefficient | value |
|---|---|
| `q_11^1` | 299/32 |
| `q_11^2` | 207/32 |
| `q_12^1` | 405/32 |
| `q_12^2` | 529/32 |
| `q_22^1` | 1035/32 |
| `q_22^2` | 879/32 |

all strictly positive. Absolute bounds: `f(f+3)/2 = 299 ≥ 69`,
`g(g+3)/2 = 1080 ≥ 69`, non-binding. Hence the Bose–Mesner/Krein/absolute
machinery used here does **not** obstruct `(69,20,7,5)`; existence remains
open. The topic's headline elimination attempt therefore YIELDS NO WITNESS,
and this report claims only the census (fallback) theorem above.

## Method (reproducible)

`output/artifacts/srg_ledger.py` (stdlib only, deterministic):

1. Enumerate all integer `(v,k,λ,μ)` satisfying the count equation
   (triple loop over `v`, `k`, `μ`, divisibility-determined `λ`).
2. Classify spectra exactly: discriminant `D = (λ−μ)² + 4(k−μ)`;
   integral case (perfect-square `D`, evenness, integral positive
   multiplicities, sign pattern `r > 0 > s`) vs. conference case
   (odd `v`, vanishing numerator `2k + (v−1)(λ−μ) = 0`) vs. excluded.
3. Compute all 27 Krein numbers via `Q(√D)` pair arithmetic from the dual
   eigenmatrix `Q` with weights `(1,k,v−k−1)`; evaluate at `√D = d` when
   `D = d²`, else require vanishing `√D`-part. Cross-check every integral
   case with an independent `Fraction` computation from `(r,s,f,g)`.
4. Absolute bound `v ≤ f(f+3)/2`, `v ≤ g(g+3)/2` for primitive graphs
   (`μ ∉ {0,k}`); flag TIGHT/FAIL; imprimitive rows marked NA.
5. Emit `ledger.json` (all rows) and `replay.log` (every exclusion plus
   totals) deterministically (`sort_keys=True`).

`output/artifacts/verify.py` re-executes the generator in a fresh temp
directory and byte-compares both outputs → `VERIFY_OK`.

## Eliminated / obstructed rows (machine-checked)

Krein-FAIL (15, all integral): `(55,48,42,40)`, `(56,22,3,12)`,
`(56,33,22,15)`, `(56,40,30,24)`, `(63,22,1,11)`, `(63,40,28,20)`,
`(64,21,0,10)`, `(64,42,30,22)`, `(64,54,46,42)`, `(78,70,63,60)`,
`(81,64,52,44)`, `(81,70,61,56)`, `(100,78,63,52)`, `(100,81,66,63)`,
`(100,88,78,72)`.

Absolute-bound-FAIL (18): `(56,22,3,12)`, `(56,33,22,15)`,
`(56,40,30,24)`, `(63,22,1,11)`, `(63,40,28,20)`, `(64,21,0,10)`,
`(64,30,18,10)`, `(64,33,12,22)`, `(64,42,30,22)`, `(64,54,46,42)`,
`(81,40,25,14)`, `(81,40,13,26)`, `(81,64,52,44)`, `(81,70,61,56)`,
`(100,33,18,7)`, `(100,66,39,52)`, `(100,78,63,52)`, `(100,88,78,72)`.

## Limitations / what is NOT claimed

- No nonexistence proof for `(69,20,7,5)` or any other open tuple.
- The census covers only classical feasibility (count equation, integral/
  conference spectrum, Krein, absolute bound); it does not implement
  clique bounds, Terwilliger/polynomial constraints, or structural searches.
- Conference-type rows verify Krein/absolute data formally; geometric
  realizability is a separate question.
- Catalogue comparison (e.g. Brouwer table agreement) was not re-fetched in
  this session and is not part of the claim.

## Artifacts

- `output/artifacts/srg_ledger.py` — generator (stdlib only).
- `output/artifacts/ledger.json` — full 10098-row ledger.
- `output/artifacts/replay.log` — exclusion + totals log.
- `output/artifacts/verify.py` — independent byte-replay check (`VERIFY_OK`).
