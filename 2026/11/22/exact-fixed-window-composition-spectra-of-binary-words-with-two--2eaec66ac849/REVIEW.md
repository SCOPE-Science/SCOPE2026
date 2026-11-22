# Scientific review: fixed-window two-marker composition profiles

## Correctness — PASS
The binary weight-two word is uniquely specified by ordered positions \(i<j\). The set of length-\(h\) window starts covering each one is an integer interval \(A_i\). The two observed statistics \(T=N_1+2N_2\), \(U=N_2\) are exactly \(T=|A_i|+|A_j|\), \(U=|A_i\cap A_j|\). For \(n\ge3h-1\) the possible incidence lengths are \(\min(i,h,n-i+1)\), allowing a disjoint exhaustive enumeration of endpoints, central positions, and fixed distances. The proof establishes the region, each fiber formula, sharp boundary, singleton characterization and collision expansion. The standalone checker independently compared complete fibers in 696 parameter cases and 26,850 literal window observations, but is not substituted for the infinite argument.

## Originality — PASS, with residual priority risk
The 2022 primary paper of Ye and Elishco introduces truncated composition-multiset reconstruction and treats fixed-length read submultisets for code constructions (Section VIII), not complete weight-two single-layer output regions and fibers. The closest published two-marker note counts **all** read lengths through a cutoff and gives stronger wordwise observations, but does not state or directly imply the quantitative single-layer fiber census; discarding lower-length layers merges fibers, requiring the distinct interval-overlap counting performed here. Published width-three results are not all-width, weight-two fixed-layer fiber classifications. Semantic literature and publicly indexed research searches found no identical statement. General historical-priority risk and derivability from broader generating identities remain.

## Value — PASS
A natural sparse-fragment reconstruction channel has a complete two-parameter feasible-output region and every inverse-fiber size; these directly determine exact restricted zero-error code size, sharp saturation threshold, unique decodability, and fixed-width collision asymptotics. This is an informative exact invariant, not a one-parameter numerical curiosity.

## Limitations
The exact classification assumes a known number of two ones, known \(n,h\), noiseless noncyclic overlapping windows, and count-preserving readout. The result says nothing about positive-distance error correction or higher marker weights. A finite checker is corroboration only. An independent scientific validation has not been performed.

## Primary comparisons
- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (first public 2022-08-31), especially Section VIII.
- *A sharp \(3r-1\) saturation law for two-marker length-limited composition decks*, published research note, full RESULT.md comparison.
- *Interval-support characterization for binary three-window composition multispectra and the sharp four-window obstruction*, published research note, full RESULT.md comparison.

Self-review: passed. Independent audit: not yet performed.
