# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified 2x2-slice equilibria in 4x4 {0,1,2,3} bimatrix games: M22(4,3) >= 8

## 1. Problem and result

Let `A,B in {0,1,2,3\}^{4x4}`. For supports `I,J` with `|I|=|J|=k` call `(x,y)`
an **isolated square-support Nash equilibrium** if

- (indifference) `A[I,J] y = v·1`, `sum y = 1`; `B[I,J]^T x = w·1`, `sum x = 1`;
- (uniqueness) the `(k+1)x(k+1)` extended systems `[[A[I,J],-1],[1^T,0]]`,
  `[[B[I,J]^T,-1],[1^T,0]]` have nonzero determinant;
- (full mixing) `x>0`, `y>0` strictly;
- (strict best response) every `i' not in I` has `A[i',J]·y < v` strictly and
  every `j' not in J` has `x·B[I,j'] < w` strictly.

Equalities are classified degenerate and excluded. For `k=1` this is a strict
pure equilibrium. Let `N22(A,B)` be the number with `k=2` (36 candidate pairs)
and `M22(4,3) = max N22` over all `{0,1,2,3\}` games. Trivial slice cap is 36;
continuum (real-payoff, nondegenerate 4x4) cap is 15 total equilibria
(von Stengel 1999; Ickstadt–Theobald–von Stengel 2025).

**Theorem (certified lower-bound catalog).** There exists an explicit
`(A*,B*) in {0,1,2,3\}^{4x4}` with `N22(A*,B*) = 8`. Hence `M22(4,3) >= 8`.
The full 69-pair square-support census is: 1 pure + 8 with `k=2` + 0 with
`k=3` + 0 with `k=4` (9 isolated total), each certified by exact-rational
mixtures, expected payoffs, best-response slacks, and determinants. A second
independent witness with the same counts exists, and a further game attains
13 isolated total (4 pure + 6 2x2 + 3 3x3), near the continuum cap 15.

This exceeds the pre-registered fallback bar (`>=6`) and is proved by exact
`Fraction` arithmetic with no floating point, rerunnable in milliseconds.
No claim of a matching global upper bound (`M22 = 8`) is made; the upper bound
remains open between 8 and 36 (15 under the continuum-total cap).

## 2. Witness matrices

Primary witness (integers published):

```
A* = [[3,3,0,0],
      [1,2,2,2],
      [2,0,2,2],
      [1,0,3,3]]
B* = [[2,2,1,3],
      [0,2,3,0],
      [2,0,3,0],
      [1,1,0,2]]
```

Secondary witness (independent discovery, symmetric variant, same census shape):

```
A2 = [[0,0,3,3],[0,2,2,2],[2,1,2,2],[3,3,1,1]]
B2 = [[1,1,0,2],[0,2,3,0],[2,0,3,0],[1,1,0,2]]
```

Bonus near-continuum-total game (N22=6, total 13):

```
A3 = [[2,0,2,1],[2,1,1,3],[0,2,1,2],[3,1,0,0]]
B3 = [[1,0,2,1],[0,2,1,3],[1,3,2,1],[3,1,0,1]]
```

## 3. Complete verified census of (A*,B*)

Enumerator: all 69 square pairs; `k>1` solved by exact Gaussian elimination
over `Fraction`; `k=1` by direct strict comparison. Table (0-indexed):

| # | I | J | k | x | y | v | w | detM | detN | min row slack | min col slack |
|---|---|---|---|---|---|---|---|------|------|---------------|---------------|
| 1 | [3] | [3] | 1 | [1] | [1] | 3 | 2 | 1 | 1 | 1 | 1 |
| 2 | [0,1] | [1,2] | 2 | [1/2,1/2] | [2/3,1/3] | 2 | 2 | 3 | 2 | 1 | 1/2 |
| 3 | [0,1] | [1,3] | 2 | [2/3,1/3] | [2/3,1/3] | 2 | 2 | 3 | -3 | 4/3 | 1/3 |
| 4 | [0,2] | [0,2] | 2 | [1/2,1/2] | [2/3,1/3] | 2 | 2 | 3 | 2 | 1/3 | 1/2 |
| 5 | [0,2] | [0,3] | 2 | [2/3,1/3] | [2/3,1/3] | 2 | 2 | 3 | -3 | 1/3 | 1/3 |
| 6 | [1,3] | [1,2] | 2 | [1/2,1/2] | [1/3,2/3] | 2 | 3/2 | 3 | -2 | 2/3 | 1/2 |
| 7 | [1,3] | [1,3] | 2 | [1/3,2/3] | [1/3,2/3] | 2 | 4/3 | 3 | 3 | 2/3 | 1/3 |
| 8 | [2,3] | [0,2] | 2 | [1/2,1/2] | [1/2,1/2] | 2 | 3/2 | 2 | -2 | 1/2 | 1/2 |
| 9 | [2,3] | [0,3] | 2 | [1/3,2/3] | [1/2,1/2] | 2 | 4/3 | 2 | 3 | 1/2 | 1/3 |

Full per-equilibrium data (all slacks, mixtures) is in
`artifacts/census_champion.json`. Every mixture is strictly positive with
denominator 2 or 3; every outside slack is `>=1/3` (strictly positive);
every `(k+1)`-determinant is `±2` or `±3` (nonzero). All other 60 square
pairs fail at least one of: singular (`det=0`), non-positive mixing, or
non-strict best response — checked exhaustively. Hence `N22=8` exactly for
this game, and `M22(4,3) >= 8`.

Structural note (integer obstruction, not a proof): with entries in
`{-3..3}` differences, 2x2 determinants `D=A11-A12-A21+A22` lie in
`{-6..6}\{0}`; here only `±2,±3` occur, giving small-denominator mixtures
`1/2,1/3,2/3` and uniform row value `v=2` across all eight 2x2 equilibria.
Coexistence of eight pairs requires compatible global best-response
coupling — the witness arranges it with slacks exactly `1/3`–`4/3`.

## 4. Methods and reproducibility

- **Exact census** (`artifacts/census.py`): `Fraction`-only, no float.
  Single-game full 69-pair census runs in ~3 ms (well under 5 s).
  Independent verifier `artifacts/verify_champion.py` re-asserts `N22==8`,
  strict positivity/slacks, nonzero dets, `Fraction` types.
- **Fast screen** (`count_N22_fast`): integer-only 2x2 formulas
  (`nA*DA>0`, `(v_num-u_num)*DA>0`), proved equal to exact census on
  1000 random games.
- **Heuristic maximality search**: uniform random sampling plus single-payoff
  hill-climbing (96 single-entry neighbours per game), fixed seeds.
  Archived: `uniform_search_log.txt` (100k uniform, seed 777, hist
  `{0:87185,1:12135,2:630,3:48,4:2}`, best 4, total 101056 incl. hill steps)
  and `iterated_search_log.txt` (sideways-accepting walks seeds
  100,101,102,201,205, total 516218 games, global best 8 found independently
  twice). Extended campaigns (uniform 300k, basin-hopping 665k, neighbourhood
  exhaustions) total >2.8M games with no 9 found. Scripts archived alongside logs.
- **Local optimality**: both 8-champions are 1- and 2-step optimal
  (all 96 neighbours and all 9216 two-step neighbours have `N22<=8`).

## 5. Limitations and what is NOT claimed

- **No global upper bound.** Search saturation and 2-step optimality are
  evidence, not proof. Exhaustion over `4^32 ≈ 1.8e19` games is infeasible;
  index/parity + determinant pruning toward a matching `M22=8` certificate
  is left open. Honest interval: `8 <= M22(4,3) <= 36` (and `<=15` if the
  continuum-total cap is applied to the 2x2 slice, which is valid since
  `N22 <= total`).
- **Scope**: only square fully-mixed isolated equilibria counted; unequal
  supports and weakly-mixed/degenerate ties excluded by definition.
- **Originality**: continuum 4x4 max 15 is known; novelty is the bounded-integer
  slice obstruction and the certified `{0..3\}` witness/census benchmark, not a
  general equilibrium-computation method.

## 6. Reproduce

```
python3 artifacts/verify_champion.py
# -> census: 9 isolated ... N22=8 ... VERIFY OK in ~3 ms
python3 artifacts/uniform_search_script.py   # 100k, fixed seed 777
python3 artifacts/iterated_search_script.py  # 516k, fixed seeds, best 8
```

## References
- von Stengel (1999), New maximal numbers of equilibria in bimatrix games, DCG.
- Ickstadt–Theobald–von Stengel (2025), stable-set bound, max 31 for n=5 / 15 for n=4.
- von Stengel (2021), Finding Nash equilibria of two-player games (methods reference).
