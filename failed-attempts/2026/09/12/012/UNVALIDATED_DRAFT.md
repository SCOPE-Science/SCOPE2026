# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Wilf-collapse pocket: Av(1342,1423) and Av(1342,1432) coincide to n = 14

## Claim

Let A = Av(1342, 1423) and B = Av(1342, 1432) (classical patterns, one-line notation).
Then |A_n| = |B_n| for every 0 <= n <= 14, with values

| n   | 0 | 1 | 2 | 3 | 4  | 5  | 6   | 7    | 8    | 9     | 10     | 11      | 12      | 13       | 14        |
|-----|---|---|---|---|----|----|-----|------|------|-------|--------|---------|---------|----------|-----------|
| cnt | 1 | 1 | 2 | 6 | 22 | 90 | 394 | 1806 | 8558 | 41586 | 206098 | 1037718 | 5293446 | 27297738 | 142078746 |

Moreover (structural collapse data, exact to n = 9):

- The one-sided difference sets are exactly balanced at every level:
  |A_n \ B_n| = |B_n \ A_n|, namely 0,0,0,0,1,10,72,459,2760,16074 for n = 0..9.
  Hence neither class contains the other, yet their totals agree.
- The append-child-count profiles match as multisets at every level n <= 9:
  for each k, the number of perms in A_n with exactly k class-preserving appends
  equals the corresponding number in B_n.
- Two-sided minimal witnesses exist at every level 8 <= n <= 14 (listed in
  `artifacts/census_n14.txt` and verified below); e.g. at n = 8,
  (8,7,5,4,1,6,3,2) is in A \ B and (8,7,5,4,1,6,2,3) is in B \ A.

In particular the admitted tiny-instance anchor (agreement to n = 9 with two-sided
witnesses) is extended to n = 14, and the target inequality gr(A) < gr(B) has no
finite-count support through length 14: both classes reach 142078746 together.

## Why this refutes the target direction (evidence, not proof of equality)

The target claims gr(A) < gr(B). The census shows the two enumerations tracking
each other exactly through 14 terms with balanced differences — the signature of a
Wilf-collapse pocket rather than a separation. No claim about the limiting growth
rates themselves is made; equality of rates is conjectured but NOT proved.

## Method (replayable)

1. `artifacts/census.c` — OpenMP DFS over the shared Av(1342) append tree with an
   incremental O(n^2) detector for patterns 1342/1423/1432 created through the last
   element, carrying 1423/1432 containment flags. Compile
   `gcc -O2 -fopenmp -o census_bin artifacts/census.c`, run `./census_bin 14 7`.
   Output archived in `artifacts/census_n14.txt` (counts + witnesses).
2. `artifacts/naive.c` — independent validator: full-permutation DFS with naive
   O(n^4) direct 4-tuple pattern tests (no shared code, no incremental detector,
   no flags). Agrees with engine n = 0..10.
3. `artifacts/crosscheck.py` — independent itertools brute force n <= 9 plus
   verification of every witness in `census_n14.txt` (membership in exactly one
   class + minimality: parent avoids both patterns). All pass.
4. Detector correctness: incremental `endings()` checked against brute-force
   occurrence-through-last on 5000 random (perm, gap) pairs — 0 mismatches.
5. Symmetry exclusion: `artifacts/symcheck.py` verifies no dihedral map sends the
   basis {1342,1423} to {1342,1432}; the collapse is therefore not a trivial symmetry.

## Conjectures and uncertainty (explicitly NOT claimed)

- Wilf-equivalence A ~ B (equal counts for all n) is suggested by exact balance,
  matching profiles, and append-tree AHU-label agreement to depth 6, but no bijection
  is exhibited and several natural candidates were refuted (swap-last-two,
  reverse-descending-runs, frame-wise child coincidence, order-isomorphism). Stated
  as conjecture only.
- Growth-rate equality gr(A) = gr(B) is likewise conjectured, not proved.

## Artifacts

- `artifacts/census.c`, `artifacts/naive.c`, `artifacts/crosscheck.py`,
  `artifacts/symcheck.py`, `artifacts/diffdist.py`, `artifacts/census_n14.txt`
