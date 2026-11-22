# Review of the sparse curling-transform fiber theorem

## Correctness (C): PASS

The central suffix-power lemma reduces every possible mixed-letter suffix repetition to a square with period equal to the distance between the two ones. Its two boundary inequalities recover the displayed three-gap transform exactly. The subsequent explicit inversion proof separates all possible first-gap categories, then the only plausible middle-gap collision, and handles all short-length exceptions. These are statements for all nonnegative gap lengths, not extrapolations from computation. Independent direct enumeration checked all \(10{,}660\) weight-two binary sources of lengths \(2\) through \(40\), and an independent inverse-image computation checked every length through \(100\). The attached programs and captured results are reproducible using Python 3 without dependencies. Finite tests are corroborative, not the infinite argument.

## Originality (O): PASS, within bounded source access

The motivating Caveney–Dong–Shallit 2026 paper studies avoidance thresholds and morphic sources paired with their curling transforms; this result instead classifies the entire inverse map on the weight-two source stratum. Chaffin–Linderman–Sloane–Wilks 2012/2013 enumerate words by a single final curling number, which cannot imply a complete **ordered** prefix-transform fiber description. OEIS A216955 likewise tabulates final-curling counts. The closest indexed related result concerns two transform outputs for ternary extremal repetition-avoidance sources rather than a universal all-length fixed-weight binary inversion theorem. Exact and alias searches found no dominating claim. The motivating paper's later full-text sections were unavailable on re-open, and unindexed equivalents remain a residual priority risk; lack of matches is not a proof of global novelty.

## Value (V): PASS

A full prefix curling-number trace is a natural observation map in suffix-repetition analysis; determining whether it reconstructs the source is an inverse problem distinct from computing its final statistic. Weight two is the first nontrivial fixed-weight binary family in which suffix squares can contain both symbols. The theorem gives all inverse fibers, not just an upper bound or one example. Unexpectedly only two ambiguities survive for every sufficiently long length, yielding exact decoder success and conditional entropy. This is a complete motivated classification, not an arbitrary finite table.

## Limitations

The theorem concerns only exact Hamming weight two, the fully ordered prefix trace, and labeled binary sources. It makes no prediction for higher weights or for a truncated observation. Verification is computational only over the reported finite ranges. Priority is not certified against unindexed or inaccessible literature. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
