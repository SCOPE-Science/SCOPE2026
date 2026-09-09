# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Shortening shadow-gap table for the extremal Type-II [72,36,16] enumerator

## Claim
From the unique putative extremal Type-II weight enumerator W72* (length 72),
shortening at fixed coordinate 1 admits **exactly one** MacWilliams-compatible
distribution, a [71,35,16] code with dual distance 15, tabulated below in exact
rational arithmetic. The puncture-excess gap value on this residual cell is
**g = 2^35 = 34359738368**, an explicit nonnegative integer combination of
punctured/shortened weight-distribution coefficients (not the Conway-Sloane
shadow enumerator of the shortened code). Independent replay reproduces the table and g
bit-for-bit (`python3 verify.py` -> `VERIFY_OK`).

## Parent enumerator (recomputed from the Gleason basis)
`f = x^8+14x^4y^4+y^8`, `g = x^24+759x^16y^8+2576x^12y^12+759x^8y^16+y^24`;
`W72* = c0 f^9 + c1 f^6 g + c2 f^3 g^2 + c3 g^3` with
`c = (-1081/3087, -989/4116, 3151/2058, 733/12348)`, fixed by
`A0 = 1, A4 = A8 = A12 = 0`. Nonzero coefficients:

| w | A_w |
|---|---|
| 0, 72 | 1 |
| 16, 56 | 249849 |
| 20, 52 | 18106704 |
| 24, 48 | 462962955 |
| 28, 44 | 4397342400 |
| 32, 40 | 16602715899 |
| 36 | 25756721120 |

Sum `2^36`; MacWilliams self-dual; support `0 mod 4`, so the exact-`Z[i]`
shadow computation gives self-shadow `S = A`
(`s1_gleason.py`, `s3b_shadow_exact.py`).

## Shortened table (the complete MacWilliams-compatible list: one cell)
`t_w = w A_w / 72` is the UNIQUE solution of the 68 nontrivial MacWilliams
equations in 5 unknowns (rank 5, consistent; `s2b_shorten.py`).
Shortened [71,35] `A'_w = A_w - t_w`; punctured dual [71,36]
`B'_j = (A_j - t_j) + t_{j+1}`; MacWilliams residual exactly 0.

| w | A'_w |
|---|---|
| 0 | 1 |
| 16 | 194327 |
| 20 | 13077064 |
| 24 | 308641970 |
| 28 | 2687264800 |
| 32 | 9223731055 |
| 36 | 12878360560 |
| 40 | 7378984844 |
| 44 | 1710077600 |
| 48 | 154320985 |
| 52 | 5029640 |
| 56 | 55522 |

Min distance 16 (>= 15 as required); dual distance 15; sums `2^35`, `2^36`.
(`s2b_shorten.py`, `f2_table.py`.)

## Shadow-gap value g (puncture excess B' - A', not the Conway-Sloane shadow
enumerator of the shortened code)
Coset excess `Q = B' - A'` lives on odd weights
`{15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 71}` with values
`55522, 5029640, 154320985, 1710077600, 7378984844, 12878360560, 9223731055,`
`2687264800, 308641970, 13077064, 194327, 1` (all `3 mod 4` plus `71`).
**Lemma.** For any genuine binary Type-II parent, `A_odd = 0`, so
`t_odd = 0` by `0 <= t <= A` and complement symmetry; then for the
shortened/punctured pair `Q_j = B'_j - A'_j` satisfies `Q_even = t_odd = 0`
and `Q_odd = B'_odd >= 0` because `A'_odd = 0`; hence `Q >= 0` and
`g := sum_{j = 3 mod 4} Q_j >= 0`. On the putative extremal cell
**`g = 34359738368 = 2^35`** with `g_{1 mod 4} = 0`. (`f1_gap.py`.)
Since `g > 0` is satisfied, no exclusion is claimed.

## Consistency context (why this is a baseline, not an exclusion)
The cell survives every enumerator-level test applied: self-shadow,
Assmus–Mattson 5-design lambdas integral (e.g. `lambda_5(16) = 78`),
pair/triple/quad/quint balanced moments integral, k-point MacWilliams systems
unique-and-balanced for k = 1..5, extremal-72 theta kissing number 6218175600
reproduced, Jacobi polarized identity exact. First rank drop at k = 6
(nullity 1–5, still consistent; an integral admissible 6-point cell is exhibited
in `s23_cell.json`). Full target exclusion is therefore NOT claimed; the table
plus `g` is logged as the citable obstruction baseline per the fallback.

## Replay
`cd output/artifacts && python3 verify.py` reruns all scripts and asserts every
identity above, ending in `VERIFY_OK`. Hashes in `SHA256SUMS`.
Standard library only (`fractions`, `math`, `json`, `subprocess`).
