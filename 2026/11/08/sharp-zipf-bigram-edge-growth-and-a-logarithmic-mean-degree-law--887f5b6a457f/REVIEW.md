# Scientific review: Sharp Zipf bigram edge growth and a logarithmic mean-degree law

## Correctness — PASS

The exact infinite Zipf normalization and the distinction between ordered and unordered edges are specified. Nonloop ordered-pair occurrence indicators are 1-dependent and mutually exclusive at neighboring indices; Stein–Chen gives an aggregate bounded Poisson-occupancy error. A Dirichlet divisor count and an explicitly integrated kernel give both the leading term and the secondary coefficient, with a controlled square-root divisor remainder. Unordered-pair overlaps give a separate \(O_a(n^\gamma)\) aggregate error. The self-bounding deletion inequality yields a rigorous variance bound and the strong law; ordinary heavy-tail occupancy gives the vertex denominator. A standalone checker passed 17,939 exact-rational finite assertions, including complete enumerations, but the infinite arguments are proved analytically in RESULT.md.

## Originality — PASS (best-knowledge, subject to priority verification)

Xie and Zhou, *Universal Exponent-Two Degree Laws in Range-Renewal Networks*, arXiv:2609.05290 (2026), prove fixed-degree/iterated-tail results without an asymptotic total-edge count; Chen, Xie and Ying, arXiv:1305.1829, likewise do not supply uniform growing-degree sums. Archibald et al., arXiv:1806.04962, and Louchard, Schachinger and Ward, arXiv:2203.14773, inspect the same adjacent-pair observable but for a geometric rather than power-law distribution. Full primary statements and accessible text were examined. Public mathematical-record searches for range-renewal, ordered adjacent bigrams, Zipf edge counts, and their leading coefficients did not return a covering statement. The nearest published records discuss finite-alphabet substring counts or different graph/urn objects. A more general unpublished or unlocated infinite-alphabet word-pattern theorem could overlap; no uniqueness is asserted from unsuccessful searches alone. Exact queries, IDs, implications and inspections are documented in AUDIT.json.

## Mathematical value — PASS

Total distinct edges and logarithmically diverging mean degrees are natural finite-time network descriptors not settled by a fixed-degree power-law tail. The orientation merger changes the leading constant by a nontrivial factor \(2^{\gamma-1}\). The exact secondary term for directed edges distinguishes power-law product-frequency collisions and permits finite-size estimation; its divisor-method derivation supports related statistics. The result is not merely a renamed coupon-occupancy limit because the adjacent pairs overlap, and controlling that dependence is necessary.

## Scope and limitations

Only \(a>1\) and the exact normalized infinite Zipf alphabet are covered. The undirected second-order constant, CLT and general slowly varying tails are not proved. Finite numerical/finite-state checks do not replace proof and no independent assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
