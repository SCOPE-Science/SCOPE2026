# Scientific review

## Correctness — PASS

The only external mathematical premises are the exact two-sided-exponential bounds in Faulhuber–Shafkulovska, Section 8, equation (8.2), and that paper's global uniqueness/local strict convexity results, Section 8. The proof explicitly normalizes by the redundancy and expands both hyperbolic factors with first and second derivative control in the moving strip \(\eta=2\log n+O(1)\). The derivative roots \(\log 6\), \(\log 3\), \(\log 4\) are bracketed inside the known global-optimizer localization interval; nonzero curvature yields the \(O((\log n)^2/n^2)\) root error. Uniform expansion at fixed additive offsets yields three convex scaled loss profiles and the two strictly positive regret limits. The checker passed 76 finite high-precision assertions, including independent truncated Zak-multiplier comparisons; numerical tests are not substituted for asymptotic proof.

## Originality — PASS, provisional

The closest paper, Faulhuber–Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, gives exact source functions, unique optimizers, and order/localization results; inspected Sections 2.4 and 8, including 8.5, do not state their sharp additive logarithmic offsets or the compact-uniform scaled regret profiles. Its formulas make the new conclusion derivable with a further singular-limit analysis, which the present proof supplies; established uniqueness is explicitly credited. Kloos–Stöckler, arXiv:1311.7359, focuses on frame sets and the approach to critical density, not integer density tending to infinity; its relevant Sections 4–5 were inspected. Gaussian lattice results, arXiv:1601.02972, concern a different window (abstract-level comparison only). Earlier work by Janssen, *Some Weyl–Heisenberg frame bound calculations* (1996), supplies sharp-bound calculations cited by the principal paper; the original full text was not inspected. An equivalent expansion in older harmonic-analysis or asymptotic-optimization literature remains a residual priority risk, and unsuccessful searches alone are not proof of novelty.

## Mathematical value — PASS

The three conflicting global design objectives for a fixed natural exponential Gabor window have different logarithmic lattice corrections even though they share the same leading high-density scale. The theorem resolves their exact asymptotic geometry and computes strictly positive, sharp normalized performance penalties for choosing the best-conditioned rather than individually tightest spectral bounds. This supplies a quantitative Pareto statement not given by knowing only the existence, ordering, and uniqueness of three optimizers. It is not a finite-\(n\) optimality table or a general-window universality claim.

## Limitations and closest sources

All asymptotics hold as integer redundancy grows, with bounded additive perturbations and a fixed two-sided exponential window. They rely on primary source equations and convexity; they do not concern nonrectangular lattices or all density ratios. Published historical priority is provisional pending additional specialist assessment. Principal source: https://arxiv.org/html/2204.02917v2 ; earlier exponential-window analysis: https://arxiv.org/abs/1311.7359 ; Gaussian comparison: https://arxiv.org/abs/1601.02972 .

Self-review: passed. Independent audit: not yet performed.
