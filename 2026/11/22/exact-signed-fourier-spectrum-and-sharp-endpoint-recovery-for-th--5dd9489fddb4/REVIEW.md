# Scientific review of the order-three Aztec-diamond spectrum

## Correctness — PASS

The cell coordinates produce exactly 24 vertices and 36 edges; the least-unmatched-cell recursion exhaustively produces 64 perfect matchings. Vertex sign switching preserves signed sums up to a global sign and exactly reduces the 36 signs to 13 gauge coordinates. For each of the 8192 normalized signings, the enumerated matching sum equals an independently built 12-by-12 exact Kasteleyn determinant. The normalized signed histogram has 4,781 zeros and 3,411 nonzero values, with minimum nonzero absolute value 8 and maximum 64. Gauge sign symmetrization gives the full spectrum and rank. Exact integer Walsh inversion of the nonzero-frequency indicator gives total absolute kernel numerator 164,610 over denominator 8,192. Averaging a competing projection over translations proves minimality among all projections, not only translation-invariant ones. These arguments cover the finite domain completely; no inference from limited samples is made.

## Originality — PASS under bounded primary comparison

The 1991 Elkies–Kuperberg–Larsen–Propp theorem supplies 64 tilings and orientation/rank generating functions, not the independent edge-sign spectrum. Chhita–Young study selected structured weight families. Barkley–Liu prove unsigned two-adic matching divisibility using channel spaces; a later exact all-order signed-divisibility theorem proves a common divisor, but expressly leaves complete spectra and projection norms undetermined. The complete normalized sign distribution, its 4,781 zero gauge classes, full rank, and evaluated sharp endpoint norm are not direct consequences of those published statements. Searches also included signed-Kasteleyn, gauge-equivalent and Fourier-recovery terminology and precise numerical invariants. Historical coverage is not exhaustive: a preexisting unindexed order-three evaluation or a specialized arbitrary-weight tabulation remains possible.

## Mathematical value — PASS

The order-three Aztec diamond is the first modest-sized member with a 24-cell tiling ensemble and 13 genuinely independent sign coordinates, making it a natural exact finite benchmark beyond the standard unsigned tiling count. Only about 41.6 percent of Fourier modes survive, and the best possible endpoint projection amplifies by \(82305/4096\), even though its surviving Hilbert condition number is merely 8. This distinction gives a precise example of endpoint-versus-Hilbert stability for a canonical planar dimer model. The claim is a finite complete spectrum and natural optimal-recovery invariant; no unsupported general-size theorem is asserted.

## Sources, boundary and residual risks

The relevant archival sources and closest contemporary signed-divisibility calculation are cited and distinguished in `RESULT.md`. The reproducible complete integer certificate is `verify.py`. General Kasteleyn determinant machinery can compute individual signed sums, but a generic computational representation is not an evaluated spectral distribution or sharp projection constant. This is a bounded historical comparison and a self-review, not an independent audit or a guarantee of priority.

Self-review: passed. Independent audit: not yet performed.
