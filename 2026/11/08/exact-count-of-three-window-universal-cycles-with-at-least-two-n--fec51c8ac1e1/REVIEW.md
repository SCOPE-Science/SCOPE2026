# Scientific review

## Correctness — PASS

The theorem specifies ordered length-three windows with at least two nonzero positions, counts rotations but not relabelings/reversals, and includes all integer alphabet sizes \(q\ge3\). The proof constructs a balanced strongly connected restricted de Bruijn graph, factors its entire Laplacian characteristic polynomial by an explicit invariant quotient, obtains the common rooted in-arborescence count from the directed matrix-tree theorem, and applies the directed BEST theorem with one distinguished edge to prevent any rotation normalization error. Direct exact enumeration at \(q=2,3\) and exact cofactors at \(q=2\) through \(6\) independently corroborate the formula. The infinite formula relies on the symbolic proof rather than the finite checks.

## Originality — PASS on available comparisons, residual risk noted

Mitchell–Wild (arXiv:2607.22350, first public 2026-07-24) directly motivates adjacent Hamming-weight-layer universal cycles, but its accessible abstract states a construction/existence result rather than a count. Its full manuscript was unavailable through the attempted public and institutional routes; the source is a material residual priority risk. Sawada–Williams–Wong (2013) construct binary weight-range cycles. Sawada–Williams (2021) prove a different fixed-content *shorthand* construction; its public full text was inspected. Chen–Kitaev–Sun (2020) study removing at most two specified words or binary short cases, a different forbidden-set scale. Chang–Wang–Xue (2025) enumerate cycles of \(k\)-permutations, where triples contain three *distinct* symbols, rather than the present family allowing repetitions. Exact statements and reductions were compared; none of the accessible claims implies the present nonbinary exact \(q\)-parameter formula. The result is not a novelty certificate against unindexed papers or the inaccessible full preprint.

## Value — PASS

For every alphabet size, this supplies the complete design-space cardinality of a natural restricted-window universal-sequence family, refining existence to a nontrivial exact answer. Its factorized arborescence number and explicit degree decomposition give reusable structural data for random generation and sequence counts. This is the smallest nonbinary dense-weight instance not equivalent to the binary upper/lower-weight symmetry; the theorem resolves that entire alphabet-size parameter family rather than a selected numerical case.

## Limitations

Only three-letter windows with weights two or three are counted, and the cycles are identified only up to rotation. The manuscript of the closest 2026 source could not be fully read, leaving historical-priority risk; no independent review is claimed. Classical matrix-tree and BEST theorems are cited rather than presented as new results.

Self-review: passed. Independent audit: not yet performed.
