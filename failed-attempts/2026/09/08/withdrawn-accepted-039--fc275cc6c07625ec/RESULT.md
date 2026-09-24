# Complete LIS-length distribution for stack-sortable (231-avoiding) permutations at n = 9, 10

## Context

Gross counts of 231-avoiding (Knuth stack-sortable) permutations are the
Catalan numbers, but refined statistics under pattern restriction —
longest increasing subsequence (LIS) length and RSK shape — are the
recognized frontier (Stanley survey program; Deutsch–Hildebrand–Wilf
limiting laws; Mansour–Yıldırım averages; permuton LIS scaling). Prior
work gives asymptotics, averages, descent/peak distributions, or
unique-LIS enumeration, but no source publishes the LIS-keyed finite
histogram for the full 231 class. This record certifies the exact
per-LIS-value census at the two largest lengths admitting exhaustive
generation with per-object tableau-log replay (n = 9, 10).

## Definitions

- `Av_n(231)`: permutations of `{1,…,n}` with no indices `i<j<k` whose
  values are order-isomorphic to `(2,3,1)`.
- `LIS(π)`: length of the longest strictly increasing subsequence,
  computed by patience piles and independently by Robinson–Schensted
  row-insertion first-row length (equal by Schensted's theorem; both
  recomputed per object).
- Narayana number: `N(n,k) = C(n,k)·C(n,k−1)/n` for `1 ≤ k ≤ n`.
- Dyck map: `D(∅) = ""`, and for `π = L ⌢ (n) ⌢ R` with `R_std` the
  standardization of `R`, `D(π) = "U" ⌢ D(R_std) ⌢ "D" ⌢ D(L)`;
  a peak is an adjacent `"UD"`.

## Result

For `n = 9`, the LIS-length distribution over `Av_9(231)` is exactly

| LIS | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-----|---|---|---|---|---|---|---|---|---|
| count | 1 | 36 | 336 | 1176 | 1764 | 1176 | 336 | 36 | 1 |

summing to `C_9 = 4862`. For `n = 10`, over `Av_10(231)` it is exactly

| LIS | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|----|
| count | 1 | 45 | 540 | 2520 | 5292 | 5292 | 2520 | 540 | 45 | 1 |

summing to `C_10 = 16796`. Both rows equal the Narayana closed form
`N(n,k)`. The recursive map `D` is bijective `Av_n(231) → Dyck_n` with
`LIS(π) = #peaks(D(π))` for every object with `1 ≤ n ≤ 10`. At n = 9, 10
the unique maximal-LIS witness (`LIS = n`) and the unique minimal-descent
witness (`des = 0`) are both the identity `(1,2,…,n)`; RS row insertion
on the identity never bumps, ending in the single row `[1,…,n]`.

## Proof / evidence

Exhaustive finite proof (not asymptotic argument):

1. **Generation.** `gen231` implements the Catalan decomposition
   `π = L ⌢ (n) ⌢ R` with `set(L) = {1,…,k−1}`,
   `set(R) = {k,…,n−1}`. Every generated object passes a brute-force
   triple `avoids231` check (soundness); totals equal Catalan
   `C_9 = 4862`, `C_10 = 16796` (completeness given `|Av_n(231)| = C_n`).
   Independent brute force over all `n!` permutations for `n ≤ 7`
   (plus `n = 8`, 40320 perms) confirms Catalan counts.
2. **Dual LIS.** Patience piles (`bisect_left`) and RS first-row length
   (`bisect_right` row insertion) are asserted equal on every one of the
   `4862 + 16796` objects; independent auditor re-run confirms agreement
   everywhere, row sums, and equality to `N(n,k)`.
3. **Dyck-peak transport.** Standalone audit on every object for
   `1 ≤ n ≤ 10` checks decomposition value sets, Dyck validity
   (`len 2n`, never negative, balanced), `LIS == peaks`, image
   distinctness with count `== C_n` (hence bijection onto `Dyck_n`
   in-window), transported histogram `== Narayana`, and
   `des+1` histogram `== Narayana` (finite observation). Extremal
   uniqueness (`LIS = n` count 1, `des = 0` count 1) certified by
   exhaustive count; any perm with `LIS = n` or `des = 0` is the
   identity, verified per object.
4. **Closed form.** `comb(n,k)*comb(n,k-1)//n` reproduces both rows.

General-`n` `LIS = Narayana` is a verified-to-10 conjecture, explicitly
not proved; the induction sketch in the draft is not a general proof.

## Limitations

- Finite window only: full dual census at n = 9, 10; bijection audit at
  n ≤ 10; brute force at n ≤ 8. No asymptotics or general-n proof.
- Bare integer rows are classical Narayana (OEIS A001263); novelty is
  the LIS-keyed replayable certificate for `Av(231)`, not the sequence.
- RSK shape beyond the first row is not tabulated.
- Completeness relies on the classical `|Av_n(231)| = C_n` enumeration;
  certificate trusts CPython stdlib implementations.

## Reproducibility

From `output/artifacts/`:

    python3 output/artifacts/census.py            # n=9,10 census (rewrites distribution.json)
    python3 output/artifacts/verify_small.py      # brute-force n<=7
    python3 output/artifacts/verify_bijection.py  # bijection + Narayana + uniqueness, n=1..10

Expected: `n=9 total=4862 …`, `n=10 total=16796 …`,
`ALL SMALL-N BRUTE-FORCE CHECKS PASS`,
`ALL BIJECTION + NARAYANA CHECKS PASS (n=1..10)`.

## References

- E. Deutsch, A. Hildebrand, H. Wilf, Longest increasing subsequences in
  pattern-restricted permutations, arXiv:math/0304126 (limiting laws).
- M. Bóna, C. DeJonge, Pattern avoiding permutations and involutions
  with a unique longest increasing subsequence, arXiv:2003.10640.
- T. Mansour, G. Yıldırım, Permutations avoiding 312 and another
  pattern, Chebyshev polynomials and longest increasing subsequences,
  arXiv:1808.05430.
- M. Bukata et al., Distributions of Statistics over Pattern-Avoiding
  Permutations, arXiv:1812.07112 (ascents/descents/peaks, not LIS).
- M. Hyatt, J. Remmel, The classification of 231-avoiding permutations
  by descents and maximum drop, arXiv:1208.1052 (descent Narayana).
- S. Kitaev, P. Zhang, Non-overlapping descents and ascents in
  stack-sortable permutations, arXiv:2310.17236 (descent Narayana).
- Y. Zhuang, Eulerian polynomials and descent statistics,
  arXiv:1610.07218 (peak/descent over 231, not LIS).
- C. Stump, On bijections between 231-avoiding permutations and Dyck
  paths, arXiv:0803.3706 (maj statistics, not LIS=peaks).
- OEIS A001263 (Narayana triangle); OEIS A000108 (Catalan numbers).
