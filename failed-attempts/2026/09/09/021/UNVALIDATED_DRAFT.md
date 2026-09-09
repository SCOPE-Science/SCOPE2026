# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Intercalate-free Latin squares of order 8: twelve certified isotopy classes in three paratopy blocks

## Definitions
Order-8 Latin square over symbols {0,...,7}. An *intercalate* (N2 configuration) is a pair of
distinct rows r1<r2 and columns c1<c2 with L[r1][c1]=L[r2][c2]=a, L[r1][c2]=L[r2][c1]=b, a!=b.
*N2-free* means zero intercalates over all C(8,2)^2 = 784 row/column pairs. Isotopy = row/column/
symbol permutations; paratopy adds the 6 permutations of the (row, column, symbol) roles
(conjugates). Autotopism group = isotopy stabilizer; its order is computed exactly.

## Theorem (verified partial classification; replayable)
There exist at least 12 pairwise non-isotopic N2-free Latin squares of order 8, falling into
exactly 3 pairwise non-paratopic blocks with the following verified invariants:

| block | # isotopy classes (lower bound) | transversals/class | autotopism order/class |
|-------|---------------------------------|--------------------|------------------------|
| A     | 5                               | 48                 | 2                      |
| B     | 5                               | 56                 | 4                      |
| C     | 2                               | 66                 | 1                      |

Representatives (rows as symbol strings; first row normalized to identity):

- A1 (seed 1): 01234567 / 74163502 / 67052134 / 36147250 / 12763045 / 40375621 / 25601473 / 53420716
- A2 (seed 2): 01234567 / 74152036 / 46073152 / 32650741 / 57426310 / 65107423 / 13765204 / 20341675
- A3 (seed 4): 01234567 / 72345016 / 16527340 / 35170624 / 67012453 / 54706231 / 43651702 / 20463175
- A4 (seed 19): 01234567 / 24715630 / 47306152 / 53471206 / 76520341 / 60152473 / 32647015 / 15063724
- A5 (seed 27): 01234567 / 57623140 / 62051734 / 43572601 / 30467215 / 14705326 / 76310452 / 25146073
- B1 (seed 3): 01234567 / 17340256 / 43605712 / 54162370 / 65721034 / 70456123 / 26573401 / 32017645
- B2 (seed 8): 01234567 / 13647250 / 45061723 / 37152406 / 24506371 / 56720134 / 62473015 / 70315642
- B3 (seed 10): 01234567 / 35146270 / 54603712 / 13470625 / 46752031 / 62017453 / 27361504 / 70523416
- B4 (seed 15): 01234567 / 62401753 / 23760145 / 30175624 / 17652430 / 45016372 / 74523016 / 56347021
- B5 (seed 58): 01234567 / 23467015 / 15723640 / 47601253 / 56170324 / 72045136 / 60352471 / 34516702
- C1 (seed 6): 01234567 / 17053246 / 53726104 / 74605312 / 46572031 / 20167453 / 65341720 / 32410675
- C2 (seed 12): 01234567 / 14702356 / 62057413 / 57341602 / 36170245 / 70561324 / 25416730 / 43620571

Full grids for all 12 (incl. B5) are in `output/artifacts/class_table.json`.

## Evidence
1. Each rep is Latin and N2=0 by exhaustive 784-pair scan; per-pair logs for leaders A1/B1/C1
   (`n2log_A/B/C.txt`, 784 lines each, zero HITs). Checker re-verifies N2=0 for all 12.
2. Pairwise non-isotopy within/across blocks: exact `iso_count` (row-0-forced: 8 row images x
   40320 column perms, symbol perm forced) returns 0 for every cross-class pair among the 12
   (all 66 pairs tested; same-transversal prefilter is necessary-condition only).
3. Autotopism orders recomputed by the same exact counter: 2 (block A), 4 (block B), 1 (block C).
4. Paratopy: sum over 6 conjugates of iso_count. Within-block bridges positive (A-pairs: 2;
   B-pairs: 4; C-pair: 3 = 1+1+1 across three distinct conjugates), so each block is one
   paratopy class; leader cross-pairs A1-B1, A1-C1, B1-C1 all score 0, so the 3 blocks are
   pairwise non-paratopic.
5. Independent replay: `output/artifacts/verify.py` (stdlib only) re-derives every number from
   the stored grids and prints VERIFY_OK (run: `python3 verify.py` in artifacts dir).

## Method note (generation, not a census)
Randomized exact-cover DFS row-by-row with first row fixed and early intercalate pruning
produced 57 N2-free squares (seeds 1..59); exact isotopy partition of those 57 gives the 12
classes above. No exhaustive upper bound is claimed.

## Limitations / what is NOT claimed
- Not a full isotopy census of N2-free order-8 squares; counts 5/5/2 are lower bounds.
- No claim identifying these 3 paratopy blocks with McKay's 3 N2-free main classes (that
  identification was not verified); the blocks are proved distinct from each other only.
- Originality: new verified witness set and stratification; the order-8 N2-free isotopy count
  itself remains open.
