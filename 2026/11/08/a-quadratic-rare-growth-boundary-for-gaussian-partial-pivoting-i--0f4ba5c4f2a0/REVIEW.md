# Scientific review

## Correctness — PASS
The single-step pivot formula produces a Schur complement of magnitude \(D+qB\) under precisely half of the independent sign configurations, and row-order multiplicity cancels that half. An explicit Gaussian integral yields the full upper-tail law. The two near-maximal comparison branches give two triangles of area \(1/2\), and the remaining boundary where the first-column pivot dominates contributes only \(O(\varepsilon^3)\). Direct integration gives \(1/(2\pi^2)\) for normal and \(1/32\) for Laplace entries. The standalone executable verifies deterministic algebra and finite Gaussian comparisons; these are supporting checks, not replacements for the infinite-limit proof.

## Originality — PASS, with residual priority uncertainty
The original October 2026 works on Gaussian elimination growth analyze large-dimension tail bounds and the last Schur entry, rather than a sharp full-tail probability for the independent-entry two-dimensional model. The exact random-butterfly distribution of Peca-Medlin and Trogdon belongs to a different ensemble. Direct query comparisons and accessible primary-paper text reveal no equivalent sharp coefficient. However, a potentially relevant unpublished 1988 Macleod distribution report could not be read, and the complete Driscoll–Maki paper was inaccessible. No claim of proven uniqueness or first discovery is made.

## Value — PASS
The probability law treats the canonical smallest nontrivial partial-pivoting system, giving a fully reproducible rare-event benchmark at the exact Wilkinson upper endpoint and distinguishing universal quadratic decay from its distribution-specific coefficient. It gives a calibration target for numerical rare-tail simulations and a baseline for extending such questions to larger systems without asserting those extensions have been solved. The result is substantially different from a textbook maximal-growth inequality, which gives no probability or coefficient.

Self-review: passed. Independent audit: not yet performed.
