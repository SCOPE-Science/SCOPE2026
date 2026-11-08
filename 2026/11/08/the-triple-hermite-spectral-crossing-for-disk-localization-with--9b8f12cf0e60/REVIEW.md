# Self-review

## Correctness — PASS
The standard radial Hermite/Laguerre overlap formula, verified against Keller–Luef's polyanalytic basis formulas, gives exact normalized radial densities. Incomplete-gamma integration gives the finite polynomial \(Q_n(A)\) and a factored difference \(-e^{-A}A^{n-1}(A-n+1)(A-n)/n!\) for every \(n\ge1\). The sign pattern yields one and only one possible secondary peak. The explicit nonnegative expression for \(Q_{m+1}-Q_0\) dominates it and proves the global norm and all top eigenspaces. No numerical extrapolation is used. The standalone package checker recomputes finite cases independently.

## Originality — PASS, provisional historical priority
Inspected Keller–Luef's full publicly accessible 2021 version, especially the displaced-Hermite/Laguerre basis in Section 3.1 and localization framework in Section 3.2. These give foundational tools but not the stated sharp disk norm transition or the infinite arithmetic pattern of simultaneous adjacent spectral collisions. Inspected Knutsen's full 2020 article, including Section 3.2, which uses the Gaussian window and analyzes norm on periodic annular supports instead. Published mathematical-record searches for first-Hermite disk crossings, triple degeneracy and Laguerre radial norms returned no covering result. Prior related recorded findings concerning periodic Hermite radial masks are different operators and masks, and imply neither the fixed-disk transition nor its complete adjacent ordering. Residual risk: older or difficult-to-index specialist work may have made the same observation.

## Value — PASS
This is a natural complete classification of the maximizing signal for the smallest non-Gaussian Hermite localization window on the canonical circular aperture, with an exactly located three-dimensional exceptional top eigenspace and an infinite staircase of three-level adjacent degeneracies at integer areas. Both the optimizer switch and the otherwise hidden secondary local peak are structural, not selected numerical examples or a mere restatement of eigenvalue integrals.

## Scientific limits
Other window orders and noncircular masks are excluded. Equality of nonadjacent suboptimal modes is not characterized. Historical priority remains provisional pending wider specialist review.

Self-review: passed. Independent audit: not yet performed.
