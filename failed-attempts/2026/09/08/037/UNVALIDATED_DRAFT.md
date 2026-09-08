# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified symmetry-reduced Wilf census for unordered length-4 pattern pairs

**Scope.** The 24 patterns of length 4 form 7 classes under the trivial
Wilf-symmetries (reverse, complement, inverse, acting diagonally on pairs);
the C(24,2) = 276 unordered *distinct* pairs form **56 orbits**. Each table
row is the lex-minimum representative of its orbit (verified by
`output/artifacts/symmetry.py`: 56 classes, 276 pairs covered, every rep the
lex-minimum of its orbit). Loop pairs (P, P) are excluded throughout.

**Method.** Exact prefix-backtracking counter
(`output/artifacts/enumerator.c`, compiled as `output/artifacts/enum2`):
patterns are 6-bit pairwise-comparison signatures (an order-isomorphism
invariant); a prefix is pruned when any quadruple using the newest position
matches a forbidden signature. Determinism confirmed by reruns; an
independent stdlib-only backtracker using a direct relative-order test
(`output/artifacts/verify.py`) agrees on all n ≤ 8 slices and spot checks
(e.g. Av₈(1234,4321) = 1764, Av₈(1234,1324) = 8864 under both programs).
Per-row replay: `./output/artifacts/enum2 N a1 a2 a3 a4 b1 b2 b3 b4`, or
`bash output/artifacts/worker.sh N "a|b"`; full proofs in
`output/artifacts/CENSUS_NOTE.md`.

## Proven theorems

**Theorem 1 (Erdős–Szekeres finiteness).** Avₙ(1234,4321) = ∅ for n ≥ 10
(Erdős–Szekeres with r = s = 4); at n = 9 it has exactly 1764 = 42² =
(f^{(3,3,3)})² members (RSK + hook-length formula: hooks 5,4,3,4,3,2,3,2,1,
product 8640, 9!/8640 = 42; census total 1764 forces every member to have
shape (3,3,3)). Enumerator confirms 0 at n = 10, 11, 12.

**Theorem 2 (Catalan separation).** Every other rep contains a length-3
subpattern 123, 132, or 321 (machine-checked: 0 of 56 reps lack one), so
Avₙ(q) ⊆ Avₙ(P) and |Sₙ(P)| ≥ Cₙ = (1/(n+1))·C(2n,n). At n = 12 this gives
the proved disjoint interval {0} vs [208012, ∞) (C₁₂ = 2704156/13 = 208012;
census minimum over nontrivial classes is 100728 for (1234,3421)).

## Certified counts |Sₙ(P)| (format P|Q|n9|n10|n11|n12)

| P | Q | n=9 | n=10 | n=11 | n=12 |
|---|---|---|---|---|---|
| 1,2,3,4 | 1,2,4,3 | 41586 | 206098 | 1037718 | 5293446 |
| 1,2,3,4 | 1,3,2,4 | 44074 | 224352 | 1163724 | 6129840 |
| 1,2,3,4 | 1,3,4,2 | 34875 | 162560 | 766124 | 3644066 |
| 1,2,3,4 | 1,4,3,2 | 21846 | 87382 | 349526 | 1398102 |
| 1,2,3,4 | 2,1,4,3 | 21846 | 87382 | 349526 | 1398102 |
| 1,2,3,4 | 2,3,4,1 | 29375 | 123996 | 518971 | 2155145 |
| 1,2,3,4 | 2,4,1,3 | 19190 | 72482 | 272530 | 1021734 |
| 1,2,3,4 | 2,4,3,1 | 13185 | 40619 | 120636 | 348197 |
| 1,2,3,4 | 3,4,1,2 | 14443 | 45770 | 138988 | 407134 |
| 1,2,3,4 | 3,4,2,1 | 8797 | 21478 | 48206 | 100728 |
| 1,2,3,4 | 4,2,3,1 | 12934 | 37088 | 98115 | 241269 |
| 1,2,3,4 | 4,3,2,1 | 1764 | 0 | 0 | 0 |
| 1,2,4,3 | 1,3,2,4 | 41586 | 206098 | 1037718 | 5293446 |
| 1,2,4,3 | 1,3,4,2 | 41586 | 206098 | 1037718 | 5293446 |
| 1,2,4,3 | 1,4,3,2 | 37663 | 182936 | 904302 | 4535994 |
| 1,2,4,3 | 2,1,3,4 | 25252 | 105632 | 442916 | 1860498 |
| 1,2,4,3 | 2,1,4,3 | 41586 | 206098 | 1037718 | 5293446 |
| 1,2,4,3 | 2,3,1,4 | 30468 | 137229 | 625573 | 2881230 |
| 1,2,4,3 | 2,3,4,1 | 28269 | 122752 | 537708 | 2375500 |
| 1,2,4,3 | 2,4,1,3 | 29943 | 132958 | 595227 | 2683373 |
| 1,2,4,3 | 2,4,3,1 | 25721 | 105485 | 430767 | 1752945 |
| 1,2,4,3 | 3,2,1,4 | 19770 | 76466 | 295810 | 1144530 |
| 1,2,4,3 | 3,2,4,1 | 18228 | 66640 | 240550 | 859295 |
| 1,2,4,3 | 3,4,1,2 | 17760 | 63594 | 223488 | 772841 |
| 1,2,4,3 | 3,4,2,1 | 13726 | 43134 | 130302 | 380414 |
| 1,2,4,3 | 4,2,3,1 | 16016 | 53579 | 172663 | 537957 |
| 1,3,2,4 | 1,3,4,2 | 41586 | 206098 | 1037718 | 5293446 |
| 1,3,2,4 | 1,4,3,2 | 34676 | 160808 | 752608 | 3548325 |
| 1,3,2,4 | 2,1,4,3 | 28696 | 124310 | 540040 | 2350820 |
| 1,3,2,4 | 2,3,4,1 | 23156 | 92416 | 367007 | 1451780 |
| 1,3,2,4 | 2,4,1,3 | 28696 | 124310 | 540040 | 2350820 |
| 1,3,2,4 | 2,4,3,1 | 25842 | 106327 | 435965 | 1782733 |
| 1,3,2,4 | 3,4,1,2 | 16766 | 58656 | 201106 | 677767 |
| 1,3,2,4 | 4,2,3,1 | 17234 | 61242 | 214594 | 744594 |
| 1,3,4,2 | 1,4,2,3 | 41586 | 206098 | 1037718 | 5293446 |
| 1,3,4,2 | 1,4,3,2 | 41586 | 206098 | 1037718 | 5293446 |
| 1,3,4,2 | 2,1,4,3 | 31192 | 141656 | 651136 | 3023840 |
| 1,3,4,2 | 2,3,1,4 | 28696 | 124310 | 540040 | 2350820 |
| 1,3,4,2 | 2,3,4,1 | 41586 | 206098 | 1037718 | 5293446 |
| 1,3,4,2 | 2,4,1,3 | 33977 | 156727 | 730619 | 3436710 |
| 1,3,4,2 | 2,4,3,1 | 28696 | 124310 | 540040 | 2350820 |
| 1,3,4,2 | 3,1,2,4 | 25252 | 105632 | 442916 | 1860498 |
| 1,3,4,2 | 3,1,4,2 | 41586 | 206098 | 1037718 | 5293446 |
| 1,3,4,2 | 3,2,1,4 | 18164 | 67234 | 247786 | 911120 |
| 1,3,4,2 | 3,2,4,1 | 28696 | 124310 | 540040 | 2350820 |
| 1,3,4,2 | 3,4,1,2 | 29396 | 129996 | 580276 | 2611290 |
| 1,3,4,2 | 4,1,2,3 | 24019 | 98677 | 406291 | 1676009 |
| 1,3,4,2 | 4,2,1,3 | 19718 | 76066 | 293398 | 1131794 |
| 1,4,3,2 | 2,1,4,3 | 36572 | 175277 | 853410 | 4209376 |
| 1,4,3,2 | 2,3,4,1 | 21846 | 87382 | 349526 | 1398102 |
| 1,4,3,2 | 2,4,1,3 | 31192 | 141656 | 651136 | 3023840 |
| 1,4,3,2 | 3,2,1,4 | 20462 | 77988 | 296787 | 1130969 |
| 1,4,3,2 | 3,4,1,2 | 21846 | 87382 | 349526 | 1398102 |
| 2,1,4,3 | 2,4,1,3 | 43193 | 218704 | 1129944 | 5937728 |
| 2,1,4,3 | 3,4,1,2 | 20518 | 79932 | 311028 | 1209916 |
| 2,4,1,3 | 3,1,4,2 | 41586 | 206098 | 1037718 | 5293446 |

Cross-checks against the failed-attempt archive (independent programs):
FAIL-022's separating vectors reappear exactly — (1234,1342): n=9: 34875,
n=10: 162560; (1324,1432): n=9: 34676, n=10: 160808. FAIL-036's n=9
equality (1342,2143) = (3142,2341) at 29943 involves ordered/specific
labellings outside the unordered-canonical frame used here (e.g. the ordered
pair (1342,2143) is symmetric to canonical rep (1432,2413) = 31192 at n=9,
not to rep (1243,2413) = 29943), so it is neither confirmed nor contradicted
by this table; those attempts proved single-pair slices, while this census
covers all 56 unordered classes at n = 9–12 with the two theorems above.

## Empirical Wilf-grouping at n = 12 (conjecture, NOT proved)

Only 38 distinct values among 56 classes at every n = 9–12, with 5 stable
multi-member groups (same membership at all four n). At n = 12:

- 5293446 × 10: (1234,1243), (1243,1324), (1243,1342), (1243,2143),
  (1324,1342), (1342,1423), (1342,1432), (1342,2341), (1342,3142), (2413,3142)
- 1398102 × 4: (1234,1432), (1234,2143), (1432,2341), (1432,3412)
- 1860498 × 2: (1243,2134), (1342,3124)
- 2350820 × 5: (1324,2143), (1324,2413), (1342,2314), (1342,2431), (1342,3241)
- 3023840 × 2: (1342,2143), (1432,2413)

No bijection is claimed; proving any of these collapses is left open.

## Limitations

- Enumeration is exact but machine-certified (no hand proof of individual
  table entries beyond the two theorems); n = 12 rows took ~1–18 s each in C.
- The lex-min rep convention and symmetry script pin the 56-class partition;
  any Wilf-equivalence beyond trivial symmetries is conjectural.
- Loop pairs (P,P) and ordered pairs are not tabulated (diagonal action covers
  unordered distinct pairs only).
