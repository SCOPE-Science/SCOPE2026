# Review of the logarithmic-square spectral-edge theorem

## Correctness — PASS
The coefficient action of the compact product is exact: \(e_{pk}\mapsto\rho^{(p+q)k}e_{qk}\). The operator decomposes into weighted arithmetic paths. A small-edge truncation and coprime divisibility bound force every surviving path to have at most \(\log(1/\varepsilon)/\log q+O(\log\log(1/\varepsilon))\) edges. Matching almost-unit weighted paths in arbitrarily many distinct coprime components deliver a min-max lower bound for each fixed eigenvalue index. These bounds give the same limit \(\pi^2(\log q)^2\). The trace-class, nonconstant-mode, and logarithmic normalization requirements are explicitly handled. A standard-library diagnostic checks 7,818 finite assertions but does not stand in for the proof.

## Originality — PASS, qualified
Full relevant mathematical sections of Clifford, Dabkowski and Wiggins (2021) were compared: that work already treats the same operators and establishes the weighted path/numerical-range framework, but not the displayed sharp approach-rate or fixed-eigenvalue-rank statement. Leng and Zhao (2026) give composition-product Schatten criteria, not this spectrum. The closest published undamped finite-degree cutoff theorem supplies the **same** logarithmic-square numerical-radius coefficient for a different cutoff and is expressly credited. The present sharp radial compactification and fixed-rank condensation require a separate edge truncation and min-max comparison, and were not found in the inspected statements. A previously proved more general spectral approximation theorem could subsume this and remains a nonzero priority risk.

## Mathematical value — PASS
As compact monomial cross-products approach a noncompact boundary product, understanding the precise degeneration of the numerical-radius and more than just the first spectral mode is a natural spectral problem. The fixed-rank universality establishes that arbitrarily many eigenvalues crowd against the same edge at the sharp logarithmic-square scale; the effective rate depends on the larger arithmetic degree and not the smaller coprime degree. This separates radial compactification from finite polynomial cutoffs and supplies a quantitative boundary theorem rather than a parameter-renaming exercise.

## Remaining limitations
No rank-uniform limit, second-order asymptotic or general-symbol theorem is claimed. Known weighted-chain descriptions and finite-cutoff cosine estimates are explicitly credited. Independent verification and comprehensive historical priority checking have not occurred.

Self-review: passed. Independent audit: not yet performed.
