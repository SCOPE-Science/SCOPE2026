# Replayable linear-extension census of all unlabelled posets to n = 8, with extremal sorting probabilities and a 1/3-balanced witness

## Context

Exact small-n linear-extension counts `e(P)` and incomparable-pair sorting
probabilities `Pr[x precedes y]` are standard ground truth for the Kahn–Saks
1/3–2/3 conjecture program (every non-chain poset has a pair with sorting
probability in `[1/3,2/3]`), sorting under partial information, and
linear-extension estimators. The FindStat Posets collection databases
unlabelled posets only to size 7, and its linear-extension / balance
statistics are sparse samples; bare unlabelled counts to `n = 16` are known
(OEIS A000112, Brinkmann–McKay) but carry no per-poset `e(P)` table.

## Definitions

- Unlabelled poset representative: Chapel Hill Atlas standard child form.
  Element `k`'s list is the set of elements it covers (lower covers),
  naturally labelled; `n#id` is the line number in `stdpstsN`.
- `e(P)`: number of linear extensions of `P`.
- For an incomparable pair `{x,y}`, `e_{x<y}` (`e_{y<x}`) is `e` of `P` with
  `x<y` (`y<x`) imposed; `Pr[x < y] = e_{x<y}/e(P)`.
- `delta(P) = max_{incomparable {x,y}} min(Pr, 1-Pr)`.
- Atlas IDs below refer to the seeded standard-form order, used only as IDs;
  every integer was recomputed from the stored cover pairs alone.

## Result

**Theorem (finite certified census, conditional on Atlas seed completeness).**
For one standard-form representative per unlabelled-poset class with
`|P| <= 8` (19,449 classes: 1, 2, 5, 16, 63, 318, 2045, 16999 for
`n = 1..8`), the value `e(P)` in `artifacts/census_all.csv` equals the exact
number of linear extensions of `P`. Dual ideal-DP paths agree on all classes;
all 485 forest values agree with the hook-length formula; for every
incomparable pair the augmented counts satisfy `e_{x<y} + e_{y<x} = e(P)`
(250,688 pairs in total). Every non-chain class (19,441) has a pair with
sorting probability in `[1/3,2/3]`, and `1/3` is best possible per `n >= 3`.

Per-`n` aggregates (recomputed):

| n | classes | max e(P) (witness) | min e(P) | sum e(P) | forests | most lopsided min Pr | min_P delta(P) |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 (1#1) | 1 | 1 | 1 | — | — |
| 2 | 2 | 2 (2#1 antichain) | 1 (2#2 chain) | 3 | 2 | 1/2 (2#1, (1,2): 1–1) | 1/2 |
| 3 | 5 | 6 (3#1) | 1 (3#5) | 14 | 4 | 1/3 (3#2, (1,2): 2–1) | 1/3 |
| 4 | 16 | 24 (4#1) | 1 (4#16) | 96 | 9 | 1/6 (4#6, (1,4): 5–1 of 6) | 1/3 (4#9) |
| 5 | 63 | 120 (5#1) | 1 (5#63) | 895 | 20 | 1/10 (5#10, (1,5): 18–2 of 20) | 1/3 |
| 6 | 318 | 720 (6#1) | 1 (6#318) | 11751 | 48 | 1/20 (6#38, (1,6): 76–4 of 80) | 1/3 |
| 7 | 2045 | 5040 (7#1) | 1 (7#2045) | 214708 | 115 | 1/35 (7#59, (1,7): 408–12 of 420) | 1/3 (7#1650) |
| 8 | 16999 | 40320 (8#1) | 1 (8#16999) | 5594463 | 286 | 1/70 (8#558, (1,8): 2484–36 of 2520) | 1/3 (8#14584) |

The maximum is `n!` at Atlas id 1 (antichain) and the minimum is 1 at the
last id (chain) for every `n` — re-derived, not assumed.

### Certified 1/3-balanced witness

Poset **8#14584**, child form `{{},{},{1},{2,3},{4},{4},{5},{6,7}}`
(cover pairs 1→3, 2→4, 3→4, 4→5, 4→6, 5→7, 6→8, 7→8): `e = 9`, 13 ideals,
4 incomparable pairs, and every pair splits 6–3:
(1,2), (2,3), (5,6), (6,7), each `6/9` vs `3/9`.
Hence pair `(1,2)` has `Pr[1 < 2] = 2/3 ∈ [1/3,2/3]` and `delta(P) = 1/3`
exactly — the minimum over all of `n = 8`. The 7-element induced subposet on
`{1..7}` is Atlas 7#1650 with identical `e = 9` and splits.

### Extremal lopsided pair at n = 8

Poset **8#558**, `{{},{},{},{},{1},{1},{1},{2,3,4}}`, `e = 2520`:
pair `(1,8)` splits 2484–36, i.e. `min Pr = 36/2520 = 1/70`, the global
minimum over all 228,009 incomparable pairs at `n = 8`.

## Proof / evidence

Computed evidence with replay (not a general theorem about the 1/3–2/3
conjecture, which remains open in general):

- Path A: bottom-up DP over order ideals, `dp[∅] = 1`, `e(P) = dp[full]`.
- Path B (independent): top-down recursion removing minimal elements of the
  remaining upset, memoised. Asserted equal on all 19,449 classes.
- Forest cross-check: if each label occurs in at most one cover list,
  `e(P) = n!/∏ h_v` with subtree sizes `h_v`; asserted equal on all 485
  forest classes.
- Sorting probabilities: for every incomparable `{x,y}`, add `x<y`
  (resp. `y<x`), reclose transitively, rerun ideal DP; asserted
  `e_{x<y} + e_{y<x} = e(P)` on all 250,688 pairs.
- Independent verifier `artifacts/verify.py` (upset-recursion replay from
  stored childform strings, forest recheck, witness and pair-sample
  rechecks): `VERIFY_OK rows=19449 forests_rechecked=485`, `WITNESS_OK` for
  both headline posets with exact splits, `PAIR_SAMPLE_OK pairs=100`
  (plus an earlier 300-pair sample during the run).
- Brute-force permutation recounts on sampled classes and standard-form
  spot checks (minimum over all natural labellings equals stored form)
  agree; per-`n` seed counts match A000112 and stored forms are unique
  per `n`.

Replay: `python3 artifacts/verify.py artifacts/census_all.csv --pairs 100`.

## Limitations

- Representatives are seeded Atlas standard forms; non-isomorphism /
  completeness of the seeds is inherited (spot-verified, not exhaustively
  re-proved at `n = 8`). The completeness half of the census is therefore
  conditional on Atlas correctness.
- The full 250,688-row pair table is not stored; per-class `e(P)`, per-`n`
  extrema, and exact witness splits are stored, and any pair is
  recomputable with the committed scripts.

## Reproducibility

- `artifacts/census_all.csv`: per-class `(n, id, childform, e, nideals,
  nincomp_pairs, is_forest)` for all 19,449 classes.
- `artifacts/per_n_extrema.json`: per-`n` maxima/minima, forest/chain
  counts, most-lopsided pair and min-delta witness per `n`.
- `artifacts/witness_8_14584.json`, `artifacts/extremal_lopsided_8_558.json`:
  exact splits for headline posets.
- `artifacts/census.py`, `artifacts/verify.py`: census pipeline and
  independent replay verifier (stdlib-only).

## References

- OEIS A000112 — Number of partially ordered sets with n unlabeled elements.
  https://oeis.org/A000112
- Brinkmann–McKay, Counting unlabelled topologies and transitive relations,
  J. Integer Seq. 8 (2005) Art. 05.2.1.
  https://cs.uwaterloo.ca/journals/JIS/VOL8/McKay/mckay170.html
- FindStat — Posets collection (unlabelled posets to size 7, canonical
  cover-relation encoding). https://www.findstat.org/CollectionsDatabase/Posets/
- FindStat St000100 — Number of linear extensions of a poset.
  https://www.findstat.org/StatisticsDatabase/St000100/
- FindStat St000848 — Balance-related statistic (1/3–2/3 motivation).
  https://www.findstat.org/StatisticsDatabase/St000848/
- Chapel Hill Poset Atlas (Gann–Proctor) — poset lists to m = 9.
  https://lists-of-posets.math.unc.edu/
