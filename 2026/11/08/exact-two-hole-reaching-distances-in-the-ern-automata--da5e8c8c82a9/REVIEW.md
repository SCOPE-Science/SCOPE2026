# Scientific review

## Correctness — PASS

The claim specifies the exact binary automaton, word order, all integers \(n\ge4\), all unordered pairs and equality of the reached image. Construction gives a word of each claimed length. The potential proof checks every permitted letter transition on rank at least \(n-2\), then uses monotonicity of image rank to exclude lower-rank shortcuts. The histogram partitions all \(\binom n2\) pairs. The independent BFS implementation in `checker.py` agrees on 451 pair instances and checks 23,014 potential transitions. This does not replace the universal proof.

## Originality — PASS under documented comparisons

The result is **not** claimed to be the first sharp \(2n\) worst-case result; both that maximum and its unique extremal pair are covered by the earlier public all-\(k\) avoidance record, and two-merge existence within \(2n\) is covered by a more general cyclic-defect-one record. The 2021 primary paper's four-state example is likewise covered. The new assertion is the entire labeled pairwise shortest-reachability formula, plus the exact distance histogram, which are not stated or logically supplied by those prior maxima or existence bounds without a separate optimization argument. Earlier general reachability bounds and the single-step inverse-extension rule similarly do not fix these geodesic distances. Priority remains provisional because a differently indexed older exact classification might exist.

## Value — PASS

The first nontrivial prescribed-image rank requires separating **which** pair of states is absent, not merely achieving rank loss two. The classification gives every pair's exact reaching threshold, a sharp formula for all multiplicities, and a complete interval of attainable lengths. It distinguishes adjacency/boundary geometry and offers a quantitative benchmark for synchronization and subset-reachability studies. This is a natural, all-parameter structural classification, not an arbitrary finite slice or minor numerical bound.

## Boundaries

No new claim is made for the already-known maximum, existence of short two-merge words, or minimal rank-two-deficiency length in isolation. The full work applies to the labeled standard Černý automaton with exactly two missing states, with no general bound asserted. Historical-priority risk remains in older transformation-monoid literature. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
