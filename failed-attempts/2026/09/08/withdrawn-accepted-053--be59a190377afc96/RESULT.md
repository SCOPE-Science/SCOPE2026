# Whole-period Goldbach-comet band separation with Hardy–Littlewood residual envelope beyond the Stein bound

## Context

The Hardy–Littlewood prediction (1923, conjecture A) modulates unordered Goldbach
counts by a singular series through the odd divisors of n. Raw Goldbach tables
exist below 200000 (Stein & Stein 1965), raw sequences to ~20000 (OEIS
A002375/A002372), minimal-partition verifications to 4e18 (Oliveira e Silva),
and qualitative comet/fractal band plots (MathWorld to n=2000; Liang et al.
nlin/0601024). None certifies exact whole-period mod-30 band means, ordering
gaps, or a uniform normalized residual envelope over a disjoint full-period
interval beyond the Stein bound.

## Definitions

- Scope: even n with 210000 ≤ n < 252000 (half-open): 21000 evens,
  42000/210 = 200 full periods mod 210, hence 1400 values in each of the 15
  even residue classes mod 30.
- Twin-prime constant C2 = 0.6601618158468695 (float64 headline;
  Decimal-60 cross-check against 0.6601618158468695739278122243).
- S(n) = product over odd p|n of (p−1)/(p−2) (empty product = 1 for powers of 2).
- H(n) = C2·n/(log n)²·S(n), natural log: unordered-count Hardy–Littlewood
  main-term prediction, compared to unordered G(n).
- G(n) = #{p ≤ n/2 : p prime, n−p prime} (unordered Goldbach decompositions).
- rho(n) = G(n)/H(n).
- For c ∈ {0,2,…,28}: Ḡ_c = mean of G over band c; μ_c = mean of rho over band c.
- E = max_n |rho(n)−1|.

## Result

Lemma (sieve correctness): a byte-array Eratosthenes sieve to 252000 yields
pi(252000) = 22203; an independently coded odd-only segmented sieve on
[210000,252000] returns the same 3396 in-scope primes; deterministic
Miller–Rabin (bases 2,7,61, valid below 2³²) agrees on a seeded 2000-sample
(0 mismatches).

Theorem (exact G-band tier separation, proved by exact integer/rational
arithmetic): the 15 band sums are exact integers

4748970, 1770618, 1790339, 3570483, 1766583, 2383891, 3555482, 1776489,
1789521, 3556878, 2365554, 1786228, 3565034, 1783145, 1789793

for c = 0,2,…,28; dividing by 1400 gives exact means (e.g. Ḡ_0 = 474897/140,
Ḡ_8 = 252369/200). Full strict ordering:

8 < 2 < 14 < 26 < 22 < 16 < 28 < 4 < 20 < 10 < 12 < 18 < 24 < 6 < 0,

minimum adjacent gap 34/175 ≈ 0.1943 (bands 16–28). Tier gaps:

- {0} vs {6,12,18,24}: 1178487/1400 ≈ 841.776;
- {6,12,18,24} vs {10,20}: 1171591/1400 ≈ 836.851;
- {10,20} vs plain {2,4,8,14,16,22,26,28}: 115043/280 ≈ 410.868.

The tier grouping is the singular-series prediction (S = 8/3, 2, 4/3, 1);
within-tier fine order is an exact census fact over this window, not a
universal law.

Benchmark (computed evidence under stated H, float64 with Decimal-60
cross-check to <3e-15, identical ordering): rho band means

c=0: 1.1947685126, 2: 1.1878888761, 4: 1.2011131873, 6: 1.1979029159,
8: 1.1852876220, 10: 1.1996681890, 12: 1.1926451535, 14: 1.1920960384,
16: 1.2006066181, 18: 1.1931113777, 20: 1.1904014300, 22: 1.1983001928,
24: 1.1960224539, 26: 1.1962110015, 28: 1.2007077421,

ordered 8<2<20<14<12<18<0<24<26<6<22<10<16<28<4>, minimum separation
δ ≈ 1.0112407508e-04. Uniform envelope E = 0.2599740089406617 at n = 215596
(G = 1189, H = 943.6702595156436, rho = 1.2599740089406617); minimum rho =
1.1322050475194423 at n = 236108; mean rho = 1.195115420728894; band-mean
spread 0.01582557; per-band residual variances 8.0e-05 to 2.7e-04;
min G = 1062, max G = 4738.

## Proof / Evidence

- Lemma: direct computation; replay script asserts all three checks.
- Theorem: exact band sums from exhaustive enumeration; adjacent differences
  are positive rationals verified by exact Fraction arithmetic; tier gaps are
  extrema differences. Auditor independently re-enumerated all 21000 G(n) and
  reproduced all sums, order, gaps, and tier gaps exactly.
- Benchmark: H/S/rho recomputed in float64 and Decimal-60; float-vs-exact-S
  <2e-15; band-mean agreement <3e-15 with identical ordering; margin 9 orders
  below δ. Auditor recomputed H/rho spot values and audited the full rho table
  (E, mean, spread, extrema, per-band counts/means).
- Residual decomposition: with consistent unordered H, mean rho ≈ 1.195;
  classical (log n)(log n−2) refinement would raise H by ≈1.19 here and move
  mean rho to ≈1.00; remaining structural signal is tier separation, spread,
  and variances.

## Limitations

- Half-open [210000,252000) keeps every band at exactly 1400 values; n=252000
  excluded; no claim outside window, about odd n, or about HL conjecture truth.
- Fine rho ordering/gap δ is a census measurement under H = C2·n/(log n)²·S,
  not a theorem about neighboring windows; denominator choice shifts mean rho
  substantially.
- Within-tier fine G order is window-specific census fact; only tier
  separation is claimed as structural singular-series confirmation.

## Reproducibility

Run `python3 output/artifacts/replay.py` (stdlib only, ~1–3 min): re-sieves,
re-enumerates all G(n), recomputes S/H/rho in float64 and Decimal-60, asserts
segmented-sieve match, Miller–Rabin agreement, S agreement, band-mean
agreement with identical ordering, and rewrites certified_summary.json,
G_table.json, rho_table.json.

## References

- Stein & Stein, Tables of binary decompositions 0<2n<200000 (Math. Comp. 19,
  1965; report LA-3106). https://api.crossref.org/works/10.2307/2003363
- OEIS A002375 (unordered Goldbach decompositions). https://oeis.org/A002375
- OEIS A002372 (ordered decompositions, cites LA-3106). https://oeis.org/A002372
- Oliveira e Silva, Goldbach conjecture verification (to 4e18).
  https://sweet.ua.pt/tos/goldbach.html
- Deshouillers–te Riele–Saouter, New experimental results concerning the
  Goldbach conjecture (ANTS 1998). https://ir.cwi.nl/pub/1222
- MathWorld, Goldbach Partition (comet plot to n=2000).
  https://mathworld.wolfram.com/GoldbachPartition.html
- Liang et al., Fractal in the statistics of Goldbach partition,
  arXiv:nlin/0601024. https://arxiv.org/abs/nlin/0601024
