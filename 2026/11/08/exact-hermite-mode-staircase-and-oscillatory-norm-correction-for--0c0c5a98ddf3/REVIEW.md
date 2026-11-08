# Scientific review

## Correctness — PASS

The Gaussian window is unit normalized, and the annular region has Euclidean area \(L\). The established Daubechies spectral formula gives \(\lambda_n=\int_s^{s+L}u^ne^{-u}/n!\,du\), whose sum over \(n\ge0\) is \(L\). The exact adjacent-difference identity proves the global unimodal ordering, not merely local extremality: it is positive exactly for \(n+1<\rho(s,L)\), zero exactly at equality, and negative thereafter. This establishes all maximizing indices, endpoint cases and multiplicities. Strict monotonicity of \(\rho\) establishes every and only every switch, while differentiating the exact difference at equality proves the cusp jump. A uniform-in-bounded-index-offset Stirling expansion yields the displayed next-order coefficient and bounded remainder; monotone unbounded \(\rho\) realizes its full cluster interval. The shipped standalone numerical checker corroborates 1,320 specific assertions but does not certify the infinite claims.

## Originality — PASS, provisional

Knutsen (arXiv:1907.00848v1, Section 3.1, full paper inspected) treats the *same unit-area ring* and establishes the Hermite integral, two possible leading indices and leading-order norm bounds with error \(O(R^{-3})\). Those results are credited as prior work, not repackaged as new. The present combined claim resolves the competing mode exactly for every ring, classifies all transition radii/eigenspaces and positive cusp jumps, and computes the oscillatory coefficient at the order left undetermined by Knutsen's estimate. Galbis' arXiv:2102.02031 establishes universal radial-symbol norm bounds; Marceca–Romero arXiv:2104.06150 concerns spectral counting deviations; Nicola–Tilli arXiv:2207.08624 concerns optimal global symbol constraints. The inspected portions and relevant statements of those full texts do not establish or imply this simultaneous exact ring-mode and oscillatory-correction law. The related mixed-Poisson-distribution representation makes earlier equivalent probabilistic results a real unresolved priority risk; absence of a search hit is not a uniqueness proof. Independent literature verification is still warranted.

## Mathematical value — PASS

Ring phase-space localization is a canonical fixed-area Gaussian STFT benchmark, singled out in the primary literature because all Hermite orders can be optimal. Distinguishing which order wins, classifying every signal that maximizes concentration at every radius, and finding all norm kinks make the operator norm *exactly* computable and describe its mode-changing geometry. The explicit, nonconstant next-order term additionally identifies a genuine asymptotic obstruction to replacing the published \(O(R^{-3})\) norm error by a constant multiple of \(R^{-3}\). These are global structural and sharp asymptotic facts rather than merely finite calculations. They do not establish new general results for arbitrary domains or non-Gaussian windows.

## Sources and residual risks

Primary: Knutsen, arXiv:1907.00848v1, Sections 2.3, 3.1 and Proposition 3.1 (2019-07-01). Related: Galbis, arXiv:2102.02031v1 (2021-02-03); Marceca–Romero, arXiv:2104.06150v1 (2021-04-13); Nicola–Tilli, arXiv:2207.08624v1 (2022-07-18). Daubechies' foundational 1988 result is acknowledged through the reproduced spectral theorem; no unverified priority assertion is made for it. A specialist literature review could find equivalent mixed-Poisson or incomplete-gamma mode results. The asymptotic claim requires fixed \(L\).

Self-review: passed. Independent audit: not yet performed.
