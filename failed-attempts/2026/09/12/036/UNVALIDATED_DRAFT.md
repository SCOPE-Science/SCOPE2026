# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Maximal Pasch-free 48-block partial STS on 19 points with certified non-completion

## Claim (TARGET route)

There exists a Pasch-free partial Steiner triple system `P` on point set
`[19] = {0,...,18}` with exactly 48 blocks such that

- (maximality) no triple outside `P` can be added without repeating a pair
  or creating a Pasch — in fact the stronger statement holds: no triple at
  all can be added without repeating a pair (linear-maximality), because the
  leave graph (27 uncovered pairs) is triangle-free; and
- (non-completability) no Steiner triple system `STS(19)` on `[19]`
  contains all blocks of `P`.

## Witness

The 48 blocks (normalized, sorted), produced by seeded randomized greedy
search (seed 285), stored machine-readably in
`output/artifacts/witness_blocks.json`:

```
(0,1,10) (0,2,14) (0,4,6) (0,5,13) (0,8,15) (0,9,12) (0,16,18)
(1,2,3) (1,4,18) (1,6,17) (1,7,9) (1,11,15) (1,12,16) (1,13,14)
(2,4,16) (2,5,10) (2,7,17) (2,8,9) (2,12,13) (2,15,18)
(3,4,14) (3,5,7) (3,6,9) (3,8,12) (3,10,15) (3,11,16) (3,17,18)
(4,5,15) (4,7,13) (4,8,11) (4,10,12)
(5,8,18) (5,9,16) (5,14,17)
(6,8,14) (6,11,12) (6,13,18)
(7,8,16) (7,10,18) (7,11,14) (7,12,15)
(8,10,13)
(9,10,11) (9,15,17)
(10,16,17)
(11,13,17)
(12,14,18)
(13,15,16)
```

The leave graph (27 uncovered pairs), stored in
`output/artifacts/leave_edges.json`:

```
(0,3) (0,7) (0,11) (0,17) (1,5) (1,8) (2,6) (2,11) (3,13) (4,9) (4,17)
(5,6) (5,11) (5,12) (6,7) (6,10) (6,15) (6,16) (8,17) (9,13) (9,14)
(9,18) (10,14) (11,18) (12,17) (14,15) (14,16)
```

Leave degree sequence: `4,2,2,2,2,4,6,2,4,4,2,4,2,2,4,2,2,4,2`
(sum 54 = 2·27).

## Verification (replayable, stdlib only)

Run `python3 output/artifacts/verify.py` (prints `VERIFY_OK`). It checks:

- **V1.** 48 distinct normalized triples on `{0,...,18}` covering every point.
- **V2.** Pair-disjointness: the 48 blocks cover exactly 144 distinct pairs,
  so `P` is a genuine partial Steiner triple system.
- **V3.** Pasch-freedom: an exhaustive census over all C(48,4) = 194580
  4-subsets of blocks finds 0 Pasches, where a Pasch is defined as 4 blocks
  on exactly 6 points with every point of degree 2.
- **V4.** Leave: exactly 171 − 144 = 27 uncovered pairs, and an exhaustive
  census finds 0 triangles in the leave graph.

## Proof of maximality and non-completability (deterministic lemma)

**Lemma.** Let `P` be a partial STS on 19 points with `b` blocks and a
triangle-free leave graph. Then no triple outside `P` can be added without
repeating an already-covered pair, and if additionally `b = 48` then no
`STS(19)` on the same point set contains `P`.

*Proof.* A triple addable without repeating a pair has all three of its
pairs uncovered, i.e. it is a triangle of the leave graph. Since the leave
is triangle-free, no such triple exists — this is linear-maximality, which
implies the target's Pasch-tolerant maximality. For `b = 48`, a full
`STS(19)` has 57 blocks, so any extension of `P` would add exactly 9 blocks
whose 27 pairs partition the 27 leave pairs; each added block would be a
leave triangle, contradicting triangle-freeness. ∎

Hence no SAT solver or unsatisfiability certificate is needed: the
completion verdict is decided by the deterministic leave-triangle census
(V4) plus this lemma. The audit plan's proposed SAT encoding would
re-derive the same verdict; the leave argument above is strictly stronger
(it rules out even adding a single triple).

## Remarks on generation and novelty

- The witness was found by randomized greedy search over the 969 triples on
  19 points (random permutation order, seed 285; add a triple iff it is
  pair-disjoint from all accepted triples and creates no Pasch). The scan
  script is `output/scratch/search1.py`. Greedy Pasch-free partials
  routinely reach 43–51 blocks; seeds 11, 94, 285, 298 of the first 300 all
  gave 48-block witnesses with triangle-free leave (seed 285 used here).
- No prior table or paper located during admission exhibits a maximal
  Pasch-free 48-block partial on 19 points with an `STS(19)`-completion
  verdict; Lindner/Doyen–Wilson-type theorems embed into much larger orders
  and do not decide this same-order tier.

## Limitations

- The claim is existential (one witness), not a classification: it does not
  say how many such partials exist, nor whether every 48-block maximal
  Pasch-free partial is incompletable.
- Pasch-freedom is certified by exhaustive census (exact for this instance),
  and non-completability by the leave lemma; no general same-order
  completion theorem is proved or claimed.
- Verification was run with CPython 3.12 stdlib only
  (`itertools`, `json`, `collections`); the census takes seconds.
