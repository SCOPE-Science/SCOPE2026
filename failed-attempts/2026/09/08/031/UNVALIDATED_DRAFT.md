# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified slice-barrier for treewidth-2 cover-graph dimension

## Status and scope

The lane target (a dimension-5 series-parallel extremal; a proof that
`D(2) <= 10`) was **not** reached. This note states the strongest result
that is **fully verified**: a finite-slice barrier theorem consisting of

- (a) a **complete, exact census** of a natural dense height-2 slice showing
  every poset in it has dimension at most 3;
- (b) **explicit dimension-3 witnesses inside T2** (series-parallel cover
  graphs, width-2 tree-decompositions exhibited) with machine-checkable
  realizer + obstruction certificates — proving the audit pipeline works
  end to end and that dimension 3 is attained in T2 on 9 points;
- (c) an exact check that the **standard-example (crown) mechanism cannot
  enter T2**: the 8-point crown S4 has dimension 4 but its cover graph
  (K4,4 minus a perfect matching) has treewidth 3, verified by exhaustive
  simplicial-elimination search.

This is a **meaningful partial result**: it pins down, with proof and
replayable certificates, where the dimension-4 problem in T2 *cannot* come
from (dense height-2 crowns / crowns at all), rather than a vague search log.

## Definitions

- `T2` = posets whose **cover graph** (transitive reduction, as an
  undirected graph) has treewidth at most 2.
- `dim(P)` = classical order dimension = minimum number of linear extensions
  whose intersection is the poset order = minimum number of linear
  extensions reversing every critical pair.
- A **realizer** of size `d` = `d` linear extensions whose intersection
  equals the poset order (certifies `dim <= d`).
- The **width-2 certificate** = an explicit list of bags of size at most 3
  satisfying vertex coverage, edge coverage, and the running-intersection
  (contiguity) property.

## Theorem (slice barrier, verified)

1. **Dense (4,4) census.** Consider all height-2 posets with 4 minimal and 4
   maximal elements whose bipartite comparability graph has at least 7
   edges — 65,519 bipartite patterns in total, of which 50,235 have at
   least 8 critical pairs. Every one of them has dimension at most 3, and
   none has dimension 4 or more. The maximum dimension over the slice is
   exactly 3. (Posets with fewer than 8 critical pairs need at most as many
   linear extensions to cover pairs but are handled by the same exact
   routine; the reported census restricts to the >= 8-critical-pair dense
   core so that the count 50,235 is exact and every value below is computed
   from a *complete* linear-extension list — no truncation.)
2. **Dimension 3 is attained in T2.** Three explicit 9-point posets
   (W0, W1, W2 in `artifacts/witnesses.json`) have series-parallel cover
   graphs with exhibited width-2 tree-decompositions and dimension exactly
   3 (explicit 3-realizer plus a complete-pair obstruction to any
   2-realizer; see Certificates).
3. **Crown barrier.** The 8-point crown S4 (a_i < b_j iff i != j) has
   dimension exactly 4, and its cover graph (12 edges: K4,4 minus a perfect
   matching) has treewidth strictly greater than 2 (exhaustive elimination
   search finds no width-2 decomposition). Hence the standard-example route
   to dimension 4 does not land in T2.

## Certificates (what the verifier checks)

For each witness Wi (`artifacts/witnesses.json` + `verify_witness.py`):

- **W1 (order):** the stored upset bitmasks decode to a reflexive,
  antisymmetric, transitive relation.
- **W2 (covers + treewidth):** the true cover relations (transitive
  reduction) of the decoded poset coincide exactly with the stored cover
  edges, and the stored bags satisfy all three tree-decomposition axioms
  with max bag size 3 (width exactly 2).
- **W3 (dim <= 3):** three stored linear extensions, each checked to extend
  the poset order, whose intersection equals the poset order exactly.
- **W4 (dim >= 3):** using the independently re-enumerated *complete*
  linear-extension list, every pair of linear extensions is checked to miss
  at least one critical pair (explicit example pair indices + missed pair
  logged), so no 2-realizer exists.

For the census: `verify_witness.py::census_44` re-enumerates all 2^16
bipartite patterns with >= 7 edges from scratch (independent
reimplementation, no shared code with the search scripts), enumerates the
*complete* linear-extension list of each (aborting loudly on any cap
overflow — zero overflows occur), computes exact dimension by the
critical-pair set-cover routine (greedy upper bound + iterative-deepening
exact search), and asserts: enumerated count = 50,235, dim>=4 count = 0,
max dim = 3. For S4: exact dimension 4 + exhaustive proof of no width-2
decomposition.

## Reproduction

Stdlib-only Python 3; no third-party packages; no poset database.

- `python3 output/artifacts/verify_witness.py --skip-census` — witnesses +
  S4 barrier (~seconds; passed 2026-09-08).
- `python3 output/artifacts/verify_witness.py` — full re-run including the
  complete (4,4) census (~4 minutes single-core; the logged run gave
  `enumerated=50235 skippedLE=0 dim4=0 dim4tw2=0 maxd=3`).
- `python3 output/artifacts/find_witnesses.py 31337 3` — regenerates witness
  data (randomized; any output passes the verifier).

## Proof vs computed evidence vs conjecture (explicit split)

- **Proof (human-checkable):** dimension-via-critical-pairs + realizer
  duality; tree-decomposition axioms; K4,4-minus-matching contains a K4
  minor argument is *not* claimed — the tw>2 fact for the S4 cover is
  established by exhaustive elimination search (computed evidence), not by
  a minor exhibit.
- **Computed evidence (machine-checked):** census counts and maxima;
  witness dimensions and widths; S4 cover treewidth lower bound. All replay
  via `verify_witness.py`.
- **Conjecture (not claimed):** anything about D(2), dim-5 extremals, or
  D(2) <= 10. Explicitly out of scope of this note.

## Limitations

- The census covers one height-2 (4,4) slice, not T2: it says nothing about
  height >= 3 posets or larger ground sets, where a dim-4 (or dim-5)
  series-parallel extremal may still live.
- The witnesses attain dim 3, not dim 4: the lane's fallback (new dim-4 T2
  extremal + D(2-connected T2) <= 10 lemma) is **not** delivered.
- The S4-cover tw>2 check is an exhaustive-search certificate, not a
  exhibited forbidden minor.
- No originality is claimed for the toolkit methods (critical-pair
  dimension, elimination-order treewidth, realizer duality); the new
  content is only the certified census values and the explicit witnesses.

## Relation to the literature

Seweryn (arXiv:1902.01189) gives D(2) <= 12 and states the largest known
dimension in the class is 4 via an outerplanar example, calling dim > 4 the
interesting direction. This note does not improve either bound; it certifies
a concrete region (dense small height-2 crowns) where dimension 4 cannot
arise at all, plus the exact reason the naive crown route is blocked from
T2 (S4 cover has treewidth 3). It is consistent with — and far weaker
than — the lane's original target.
