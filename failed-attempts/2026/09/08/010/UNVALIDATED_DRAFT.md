# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact symmetric-group orbit census of monotone Boolean functions on B4 with width and self-dual witnesses, and certified replay to D5 = 7581

## Objects and conventions (self-contained)

Identify a monotone Boolean function (MBF) on `n` variables with its set of minimal
true points, i.e. an **antichain** in the Boolean lattice `B_n = {0,...,2^n - 1}`
where elements are subsets of an `n`-set written as bitmasks and `a <= b` iff
`(a & b) == a`. The empty antichain is the constant-1 function (truth all ones
except with the convention used here: truth bit `x` is 1 iff some `a` in the
antichain satisfies `a <= x`; the empty family gives truth 0); the singleton
`{0}` is constant-0's complement. Every truth table arises from exactly one
antichain (its minimal ones), so counting antichains counts MBFs (Dedekind numbers).
`S_n` acts by permuting the `n` coordinates (bits of each mask). The **canonical
representative** of an orbit is the lexicographically least sorted tuple among its
24 (resp. 120) permuted images. **Width** = antichain cardinality. **Rank profile**
= histogram of popcounts in the antichain. Duality: `f^d(x) = NOT f(NOT x)`;
on minimal antichains it is computed via truth tables and re-minimization.

## Theorem (machine-checked)

1. **B4 census.** `|MBF_4| = 168` antichains, verified by two independent
   enumerations (exhaustive `2^16` subset scan and comparability-graph
   independent-set branch-and-bound) with identical sets.
2. **S4-orbits.** The 168 antichains form exactly **30** `S_4`-orbits under the
   lex-min canonical hash. Orbit-size multiset:
   `[1,1,1,1,1,1,3,3,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,12,12,12,12,12,12,12]`,
   i.e. histogram `{1:6, 3:2, 4:9, 6:6, 12:7}`; sizes sum to 168 and each
   divides 24. Full table of 30 canonical representatives with orbit size,
   width, rank profile, truth value, and self-dual flag is in `artifacts/b4_orbits.csv`.
3. **Burnside cross-check (B4).** Fixed-point counts by `S_4` cycle type:
   `(1^4):168 x1; (1^2 2):50 x6; (1 3):15 x8; (2^2):28 x3; (4):8 x6`.
   Sum `168 + 6*50 + 8*15 + 3*28 + 6*8 = 720 = 24 * 30`. Fix counts are constant
   on each conjugacy class (checked per element, not assumed).
4. **Width.** Over all 168: `{0:1, 1:16, 2:55, 3:64, 4:25, 5:6, 6:1}`; over the
   30 representatives: `{0:1, 1:5, 2:7, 3:9, 4:6, 5:1, 6:1}`. The bound
   `C(4,2) = 6` is sharp with **unique** extremal witness, the full rank-2 layer
   `(3,5,6,9,10,12)`.
5. **Duality (B4).** Exactly **12** self-dual antichains:
   `(1,),(2,),(4,),(8,),(3,5,6),(3,9,10),(5,9,12),(6,10,12),(7,9,10,12),
   (5,6,11,12),(3,6,10,13),(3,5,9,14)`,
   spanning exactly 3 orbits with representatives `(1,)`, `(3,5,6)`,
   `(3,5,9,14)`. Explicit fixed witness: the 2-of-3 majority `(3,5,6)`
   (truth 59624). Explicit separating pair: `A = (1,2)` with
   `A^d = (3,)`; their canonical representatives `(1,2)` and `(3,)` lie in
   distinct orbits (sizes 6 and 6). Duality preserves orbit sizes (all 168 checked).
6. **Dedekind recursion.** Pairs `(f0,f1)` of MBF_3 truth tables with
   `f0 <= f1` number exactly 168 (= D4); pairs of MBF_4 truth tables with
   `f0 <= f1` number exactly **7581** (= D5). This certifies D5 by recursion
   from the certified D4 table, independent of the direct B5 enumeration.
7. **B5 replay (certified, not just lower bound).** Direct independent-set
   enumeration gives **7581** antichains; `S_5`-orbit partition gives **210**
   orbits with histogram
   `{1:7, 5:14, 10:28, 12:2, 15:14, 20:21, 30:43, 60:74, 120:7}`,
   summing to 7581 with every size dividing 120. Burnside by class:
   `1*7581 + 10*887 + 20*105 + 15*309 + 30*35 + 20*35 + 24*11 = 25200 = 120*210`,
   unanimous per class. Width histogram:
   `{0:1, 1:32, 2:285, 3:1090, 4:2020, 5:2146, 6:1380, 7:490, 8:115, 9:20, 10:2}`.
   Exactly **two** width-10 extremal witnesses: the rank-2 layer
   `(3,5,6,9,10,12,17,18,20,24)` and the rank-3 layer
   `(7,11,13,14,19,21,22,25,26,28)` (each `S_5`-fixed as a set, orbit size 1).
   Exactly **81** self-dual B5 antichains, width histogram
   `{1:5, 3:10, 4:20, 5:35, 7:10, 10:1}`; the rank-3 middle layer is self-dual,
   the rank-2 layer is not. Nontrivial separating pair `A=(1,2)`, `A^d=(3,)`
   persists at n=5 in distinct orbits.

## Evidence (reproducible, stdlib-only)

- `artifacts/census.py` — enumeration, truth/antichain conversion, duality.
- `artifacts/orbits.py` — permutations, canonical hash, orbit partition, profiles.
- `artifacts/generate.py` — builds `b4_orbits.csv`, `b4_orbits.json`,
  `b5_summary.json`, `certificate.json` (SHA-256 + timings).
- `artifacts/replay.py` — independent verifier: re-enumerates from scratch,
  re-partitions orbits, re-checks Burnside/duality/extrema, replays checksums;
  passes in ~8 s (see `certificate.json` for per-stage timings).
- `artifacts/certificate.json` — SHA-256 checksums and wall-clock log.

## Originality and limitations (honest)

- The numbers `D4 = 168`, `D5 = 7581` and the orbit counts 30/210 are classical
  (not claimed as new). The contribution is the **explicit, replayable
  canonical-representative tables with width/rank-profile distributions,
  Burnside fixed-point tables, self-dual enumeration with fixed witness and
  separating pair, and the push-button replay certificate** — none of which
  appears in the retrieved sources (Burnside-count-only and heavy-computation
  references listed in the topic brief).
- Scope is `n = 4` (full orbit table) and `n = 5` (full count + orbit census +
  witnesses); nothing is claimed for `n >= 6`.
- Enumeration programs are deterministic and cross-checked by two methods plus
  Burnside and Dedekind-recursion identities, but correctness ultimately rests
  on the (short, auditable, stdlib-only) code in `artifacts/`.
