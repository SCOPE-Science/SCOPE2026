# Review of the radius-four flag-rank sphere formula

## Correctness

PASS. The definition of every cut submatrix is explicit. Inactive cuts force all crossing entries to vanish, so active cuts factor into consecutive principal blocks. Weight four permits only four active rank-one cuts or a consecutive triple with ranks one, two, one. The four consecutive rank-one block counts follow from exact rank-one \(2\times2\) matrix classifications and the central-rectangle decomposition; the triple exception is \(q^2\lvert\mathrm{GL}_2(\mathbb F_q)\rvert\). Composition and placement counts give the stated expression with no asymptotic step. Independent exhaustive enumerations over four small finite fields agree, but are not substituted for the proof.

## Originality

PASS against the inspected scientific sources, with the residual risk noted below. The closest primary source, Alfarano–Mushrraf–Zullo, arXiv:2606.12934v1 (Section 3 and Conclusion), establishes explicit sphere volumes only through radius three and specifically leaves larger radii open. The earlier Alfarano–Neri–Zullo arXiv:2303.16653v1 discusses the metric and optimal-distance codes rather than radius-four volumes. The Fourier–Nebe source introduces the ambient metric. No matching or stronger radius-four formula was found in the checked published records or targeted literature searches; the searched ranges are not a uniqueness proof.

## Value

PASS. This closes the first omitted exact sphere-volume case in a recently studied coding metric for all prime powers and arbitrary dimensions \(n\ge4\), rather than evaluating an arbitrary isolated instance. The formula determines the missing radius-four term in the sphere-packing bound for minimum distance nine and sharply identifies the degree-seven large-field leading term at fixed dimension. The argument also identifies the structural source of the correction term: one middle cut of rank two.

## Closest literature and limitations

The main prior paper computes radii zero through three, while its fixed-radius general estimate does not imply the exact radius-four coefficient. Its 2026 conclusion explicitly identifies arbitrary-radius enumeration as an outstanding direction. The dimension-three count is not treated as novel. No statement is made about radius five or greater, perfect-code existence, or definitive priority across all unindexed sources.

Self-review: passed. Independent audit: not yet performed.
