# Scientific review: six-point self-disjoint finite Fourier supports

## Correctness — PASS
The universal construction follows from a factorization of the two vertical polynomial slices of a six-supported signal, and the final support point cancels exactly because \(t^2=-3\). For \(p=7\), the equivalence of self-disjoint support and a singular principal Fourier minor is exact. Translation reduces the exhaustive lower-bound problem to \(213053\) subsets containing the origin. `CHECK.cpp` confirms, in a certified prime field admitting a primitive seventh root, that each of those principal minors has nonzero reduction. A complex-zero cyclotomic determinant would have zero reduction, hence no smaller support is possible. The finite calculation is a proof certificate for one specific field, not a claim of exhaustive computation for all primes.

## Originality — PASS relative to checked evidence
Zhou (arXiv:2608.06335, Section 2.3) explicitly describes the two-dimensional \(p\equiv3\pmod4\) minimum as difficult and constructs supports of size \(2p-2\), without the six-site pattern or a sharp result at seven. The closest published four-point result, *Sharp four-point self-disjoint Fourier supports on \(\mathbb F_p^2\) for \(p\equiv3\pmod8\)* (2026), is disjoint in prime congruence from the present \(p\equiv7\pmod{24}\) class. Caragea–Lee's cyclic principal-minor statements are not equivalent to the two-dimensional elementary-Abelian character-table problem. Targeted searches for a six-site construction, minimum \(\sigma_7=6\), and smaller singular principal minors in \(\mathbb F_7^2\) found no direct covering assertion. A mathematical search result's absence is not a proof of global novelty: an unindexed earlier calculation remains a residual risk.

## Value — PASS
The natural self-disjoint Fourier-support invariant is directly connected to singular principal character-table minors and was explicitly left undetermined in the prime-square, anisotropic case. The six-site construction gives a constant upper bound on an infinite previously untreated congruence class, improving the \(2p-2\) construction, and the exact minimality at its first prime identifies the first sharp boundary for that class. This provides a motivated exact invariant, not a selected numerical statistic without structural context.

## Scope and residual risks
The sharp equality is claimed only for \(p=7\); larger primes are covered by the upper bound only. The exact finite exclusion uses a reproducible C++ integer certificate, not an independently validated formal proof system. Independent audit has not been performed. Older unindexed mathematical arguments or alternate formulations may still cover the construction or minimality.

Self-review: passed. Independent audit: not yet performed.
