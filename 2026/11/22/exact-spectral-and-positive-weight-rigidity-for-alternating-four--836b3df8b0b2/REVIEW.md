# Scientific review

## Correctness

PASS. The explicitly normalized Fourier matrix decomposes after parity Fourier transforms into two-by-two blocks with trace \(2\) and determinant modulus \(|\cos(N\delta/2)|\), yielding the full Gram spectrum and boundary. A transitive rotation/reflection action averages arbitrary positive weights to uniform while preserving eigenvalue bounds; strict convexity follows from the invertible Vandermonde moment map. The determinant is a product of weights and the unnormalized result reduces to a strictly convex one-variable quadratic. The included checker supplies 846 supplementary finite assertions, not an infinite certificate.

## Originality

PASS relative to inspected sources and available search results. The most relevant recent work, Wind-Andersen (arXiv:2611.02379), treats first-order compensation, explicitly setting aside the exact fixed-imperfect-node and spectral objectives. Austin–Trefethen (2017) and Yu–Townsend (2022) establish more general interpolation/stability estimates and do not supply these exact globally weight-optimal constants on a periodic even grid. A related polyphase paper (Ghosh–Mulleti–Seelamantula, arXiv:2610.36142) provides a broad reconstruction framework; its available abstract does not assert the present simultaneous positive-weight optima. An older equivalent two-coset/polyphase calculation is a genuine residual priority risk. A negative search is not proof of uniqueness.

## Value

PASS. This complete natural periodic-timing-jitter model has a sharp worst-case sampling condition number, exact mean-square Gram defect, volume loss, best positive compensation, and precisely quadratic collapse at node collision. It proves uniform stability even for displacement fractions beyond the usual uniform Kadec sufficient range and shows that no nonuniform positive reweighting can improve either spectral extreme. The restrictions to two interlaced cosets and critical sampling are scientifically material.

## Limits

No arbitrary-jitter extension or uniqueness assertion for condition-number minimizers is proved. The proof is analytic and self-contained; numerical checks are supplementary. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
