# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified orbit census for the sparse slice of rank-4 paving matroids on 9 elements

## Abstract
We certify a closed S9-orbit census of a natural slice of the rank-4 paving
stratum on ground set [9]: all paving matroids with at most two large
hyperplanes (size >= 4). There are exactly **18** S9-orbits in this slice
(1 + 5 + 12), each with an explicit lexicographically least block
representative, orbit size / stabilizer order, full Tutte polynomial (two
pivot orders), and an explicit U(2,5)-minor certificate. As a global theorem
over the *whole* paving (4,9) stratum (not just the slice) we prove no member
is binary, by the checked fact that every 9-subset of F2^4\{0} contains a
dependent triple. Every member of the slice in fact has a U(2,5) minor, hence
is neither binary nor ternary; we separately exhibit an explicit ternary
paving (4,9) matroid (a 9-subset of an elliptic quadric in PG(3,3)) with 18
large blocks, proving the ternary stratum is nonempty and lies outside the
slice. Census script and independent verifier use only the Python standard
library and agree on all 348 checks.

## 1. Objects and slice
Work on ground set [9] = {0,...,8}. A rank-4 paving matroid is encoded by its
family B of large blocks (hyperplanes of size >= 4): every 3-subset lies in at
most one block, and the bases are all 4-sets except those contained in a
block. Small hyperplanes are then exactly the triples contained in no block.
The slice is: number of large blocks k <= 2.

**Theorem 1 (slice census).** Up to S9 there are exactly 18 paving (4,9)
matroids with k <= 2: k=0: U(4,9) (1 orbit); k=1: single block of size
4,5,6,7,8 (5 orbits); k=2: block sizes (a,b) with intersection t, a<=b,
t<=2, a+b-t<=9, giving exactly the 12 triples
(4,4)x{0,1,2}, (4,5)x{0,1,2}, (4,6)x{1,2}, (4,7)x{2}, (5,5)x{1,2}, (5,6)x{2}.
Distinct triples give non-isomorphic matroids (large-hyperplane sizes and
intersection are isomorphism invariants), and within each triple the
representative below is the lexicographically least sorted block list, so each
orbit appears exactly once.

Orbit table (blocks B; nb = #bases = T(1,1); orb/stab; Tutte evals; U(2,5)
minor via contract C, keep E, delete D):

| name | blocks | nb | orbit | stab | T(1,1) | T(2,1) | T(1,2) | C | E |
|---|---|---|---|---|---|---|---|---|---|
| U49 | [] | 126 | 1 | 362880 | 126 | 256 | 382 | [0,1] | [2,3,4,5,6] |
| k1-4 | [[0,1,2,3]] | 125 | 126 | 2880 | 125 | 255 | 381 | [0,1] | [2,4,5,6,7] |
| k1-5 | [[0,1,2,3,4]] | 121 | 126 | 2880 | 121 | 251 | 376 | [0,1] | [2,5,6,7,8] |
| k1-6 | [[0,1,2,3,4,5]] | 111 | 84 | 4320 | 111 | 241 | 360 | [0,6] | [1,2,3,4,5] |
| k1-7 | [[0,1,2,3,4,5,6]] | 91 | 36 | 10080 | 91 | 221 | 318 | [0,7] | [1,2,3,4,5] |
| k1-8 | [[0,1,2,3,4,5,6,7]] | 56 | 9 | 40320 | 56 | 186 | 219 | [0,8] | [1,2,3,4,5] |
| k2-4-4-t0 | [[0,1,2,3],[4,5,6,7]] | 124 | 315 | 1152 | 124 | 254 | 380 | [0,1] | [2,4,5,6,7] |
| k2-4-4-t1 | [[0,1,2,3],[0,4,5,6]] | 124 | 2520 | 144 | 124 | 254 | 380 | [0,1] | [2,4,5,6,7] |
| k2-4-4-t2 | [[0,1,2,3],[0,1,4,5]] | 124 | 3780 | 96 | 124 | 254 | 380 | [0,1] | [2,4,6,7,8] |
| k2-4-5-t0 | [[0,1,2,3],[4,5,6,7,8]] | 120 | 126 | 2880 | 120 | 250 | 375 | [0,1] | [2,4,5,6,7] |
| k2-4-5-t1 | [[0,1,2,3],[0,4,5,6,7]] | 120 | 2520 | 144 | 120 | 250 | 375 | [0,1] | [2,4,5,6,7] |
| k2-4-5-t2 | [[0,1,2,3],[0,1,4,5,6]] | 120 | 7560 | 48 | 120 | 250 | 375 | [0,2] | [1,4,5,6,7] |
| k2-4-6-t1 | [[0,1,2,3],[0,4,5,6,7,8]] | 110 | 504 | 720 | 110 | 240 | 359 | [0,1] | [2,4,5,6,7] |
| k2-4-6-t2 | [[0,1,2,3],[0,1,4,5,6,7]] | 110 | 3780 | 96 | 110 | 240 | 359 | [0,2] | [1,4,5,6,7] |
| k2-4-7-t2 | [[0,1,2,3],[0,1,4,5,6,7,8]] | 90 | 756 | 480 | 90 | 220 | 317 | [0,2] | [1,4,5,6,7] |
| k2-5-5-t1 | [[0,1,2,3,4],[0,5,6,7,8]] | 116 | 315 | 1152 | 116 | 246 | 370 | [0,1] | [2,5,6,7,8] |
| k2-5-5-t2 | [[0,1,2,3,4],[0,1,5,6,7]] | 116 | 2520 | 144 | 116 | 246 | 370 | [0,2] | [1,5,6,7,8] |
| k2-5-6-t2 | [[0,1,2,3,4],[0,1,5,6,7,8]] | 106 | 1260 | 288 | 106 | 236 | 354 | [0,2] | [1,5,6,7,8] |

(D = complement of C union E in each row; full D, Tutte polynomials, and
small-hyperplane counts are in `artifacts/orbit_table.jsonl`.)

## 2. Proofs
**Lemma (matroid validity).** Each row's family B has pairwise intersections
<= 2 and yields a rank-4 matroid: checked basis exchange on all pairs plus
rank 4. The large hyperplanes recovered as closures equal exactly the listed
blocks, so the encoding is faithful. (Both scripts check this.)

**Orbit counts.** For each row, the S9-image set of its block family is
enumerated over all 9! permutations: reported orbit size = image-set size,
stabilizer = 362880/orbit size (exact divisibility asserted), representative
is the least image, and image sets of distinct rows are pairwise disjoint.
Sizes/blocks/intersections separate the (a,b,t) triples: e.g. the three
(4,4,t) rows have the same Tutte triple (124,254,380) but orbit sizes
315/2520/3780, so Tutte collisions are resolved by the orbit invariant. The
(a,b,t) enumeration above is complete: a,b>=4, t<=2, a+b-t<=9, a<=b leaves
exactly these 12 triples (verified in the worklog).

**Tutte values.** Memoized deletion-contraction computed under two pivot
rules (greatest-first, least-first) agrees on the full polynomial per row;
T(1,1)=#bases, T(2,1)=130+#bases (since every subset of size <=3 is
independent, proved from the block axiom: blocks have size >=4 so no
3-circuit exists; hence exactly C(9,0)+...+C(9,3)=130 independent sets of
rank<4... precisely the deletion-contraction-free identity checked
directly), and T(1,2)=#spanning sets counted directly.

**Theorem 2 (no binary paving (4,9)).** A binary paving (4,9) matroid would
give 9 distinct nonzero vectors of F2^4 with all triples independent.
Exhaustion over all C(15,9)=5005 nine-subsets shows every one contains a
dependent triple (a^b^c=0); hence no rank-4 paving matroid on 9 elements is
binary. This is a statement about the whole stratum, proved in ~seconds.

**Theorem 3 (slice is doubly nonrepresentable; ternary stratum nonempty).**
U(2,5) is not representable over GF(2) or GF(3): exhaustion over normalized
[I2|A] matrices (2^6=64 over GF(2), 3^6=729 over GF(3)) shows some pair of
the 5 columns is always proportional. Each of the 18 rows carries an explicit
(C,E,D) with M/C restricted to E equal to U(2,5) (all 10 pairs independent,
all 10 triples dependent of rank 2 in the contraction; replayed in the
verifier), so every slice member is neither binary nor ternary. Conversely
the 9 columns
(0,0,1,1),(0,0,1,2),(0,1,0,1),(0,1,0,2),(1,0,0,1),(1,0,0,2),
(1,1,1,0),(1,1,2,0),(1,2,1,0)
in PG(3,3) (an elliptic-quadric zero set minus one point) have rank 4 with
all C(9,3)=84 triples independent, hence form a ternary paving (4,9)
matroid; its 18 rank-3 4-sets are listed in `run_meta.json`, so it lies
outside the slice. Thus the GF(3) stratum of paving (4,9) is nonempty while
the entire k<=2 slice is non-ternary.

## 3. Reproduction
```
python3 output/artifacts/census.py    # ~8 s; writes orbit_table.jsonl, run_meta.json
python3 output/artifacts/verify.py    # independent replay; exit 0; 348 checks
```
sha256(orbit_table.jsonl) = 400bb25946809af3ec3e441b65bedb8c3528a82a3099828c027441abfec421be.
Dependencies: CPython 3 stdlib only. Deterministic (no randomness, no seeds).

## 4. Scope, limits, and what is NOT claimed
- We do NOT claim the full paving (4,9) orbit count N^pav(4,9); the full
  stratum (with arbitrarily many large blocks / non-sparse-paving families)
  is not enumerated here. The 18 orbits are exactly the k<=2 slice, proved
  complete within that slice.
- The excluded minor used is U(2,5) (a forbidden minor for both GF(2) and
  GF(3)), not F7/Vamos/P8; those do not occur as minors of this slice in the
  searched contraction pairs (the U(2,5) certificate was found first and
  suffices for both fields).
- Orbit enumeration is brute force over S9 (362880 permutations x 18 rows),
  not nauty/bliss canonical labeling; it is exact but does not scale to much
  larger ground sets.
- Prior art: Mayhew-Royle catalogues all 9-element matroids; the delta here
  is the per-orbit Tutte + U(2,5)-witness package with a two-program replay
  for this slice, plus the global no-binary theorem and the explicit ternary
  witness. We do not correct or extend their total counts.
