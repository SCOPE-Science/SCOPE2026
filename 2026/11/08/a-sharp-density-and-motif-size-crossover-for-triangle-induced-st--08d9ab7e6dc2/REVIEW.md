# Scientific review

## Correctness — PASS
The claim is precise for all integers \(r\ge3\), \(n\ge r+1\), and \(0<p<1\). Joint indicator moments split into independent overlaps of at most one shared vertex, a two-vertex overlap with two compatible centers and \(r-1\) incompatible centers, and an always incompatible three-vertex overlap. The exact counts give the displayed polynomial and a strictly decreasing linear sign factor. At the smallest order there is no possible positive-overlap contribution; at all larger orders the unique threshold is interior and its monotonicity follows algebraically. The Python checker separately computes exact rational moments and enumerates all labeled graphs in bounded sizes, and passes 3213 assertions. Infinite-size statements are proven analytically; finite enumeration is not mistaken for proof.

## Originality — PASS (qualified)
Schbath–Lacroix–Sagot (2008) establish overlap methods for variance of coloured connected motifs, and Ellis–Ferry (2010) treat non-induced single-graph counts. Martorana et al. (2020) provide generic induced-motif and pair-covariance machinery that can specialize to this example but do not state the all-r sharp critical surface or its joint scaling regime. A previously analyzed r=2 triangle/open-triad covariance is explicitly excluded. The all-r sign/monotonicity assertion is not found in the inspected material; prior general methods may yield it after a specialization, and older unindexed tables may already contain it.

## Value — PASS
Counts of triangles and induced stars represent competing closure and open-neighborhood structure in random graphs. An all-r classification identifies the exact density at which they become anticorrelated, and its dependence on graph size and motif size. The changing scales between fixed r and linear r/n distinguish this theorem from a one-off small-motif covariance evaluation.

## Scientific limits
Only the independent-edge homogeneous model is covered. The result does not claim exact correlations, a limit law, applications to conditioned graphs, or historical uniqueness. The generic-overlap-priority risk is substantive.

Self-review: passed. Independent audit: not yet performed.
