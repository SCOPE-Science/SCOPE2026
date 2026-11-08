# Self-review

## Correctness — PASS

The graph is uniquely determined up to isomorphism by \((a,b,t)\). The proof distinguishes the two white part sizes, first rules out any side with three white vertices, then classifies exactly the four surviving cases via intersections with the deleted matching. In the two-plus-two case it establishes an explicit first legal force when the matched-index sets are different, reducing to an already proved case. The equality obstruction is computed without overlap. Every zero-forcing set dominates because a white vertex has at least \(a-3\) or \(b-3\) adjacent initially black vertices, both positive. The full polynomial follows by counting complement choices, and the nonzero lowest-degree coefficients are established constructively at \(t=0,1\), and \(t\ge2\). The independently constructed adjacency-based checker exhaustively corroborates all coefficients across 50 graph profiles. The all-order statement is proved symbolically, not inferred from the finite tests.

## Originality — PASS, provisional historical priority

The 2018 zero-forcing-polynomial paper gives the undeleted complete-multipartite case (Proposition 4), so the \(t=0\) specialization is prior art. The 2024 dom-forcing preprint and the 2026 study give the undeleted scalar dom-forcing number, not the full matching-deletion class. A search of mathematical research records found nearby results for complete multipartite forcing sets and matching-deleted bicliques, but the matching-deleted work concerns different invariants (non-CIS pairs and geodesic subpaths) and does not imply the forcing-process classification or polynomial here. No accessible source asserting a stronger matching-deletion zero-forcing theorem was found. Searches do not establish absolute novelty; historical priority remains uncertain, and search-result summaries cannot rule out inaccessible full texts.

## Mathematical value — PASS

The result is a complete infinite-family counting theorem for two related graph processes under a natural sparse perturbation. The first two edge deletions produce sharp changes in the minimum initial number of black vertices, and the formula counts every optimiser, not just the minimum. The full coefficient data separates the t=0, t=1 and t≥2 regimes and includes the two-step phenomenon invisible from the complete-bipartite case. The same theorem establishes a nontrivial structural strengthening: every forcing set is dominating throughout this family, while a concrete smaller-part graph shows that this does not extend automatically to all bicliques.

## Closest literature and limitations

Primary full texts: Boyer et al., arXiv:1801.08910, Proposition 4; Susanth et al., arXiv:2411.00580, Theorem 3.8; Jiang and Wan, doi:10.3934/math.2026802, Section 5. The \(t=0\) formula is known; only the matching-deletion classification is offered as new. All mathematical claims require \(a,b\ge4\); nothing is asserted for arbitrary deleted-edge patterns. Independent mathematical audit and exhaustive priority determination remain outstanding.

Self-review: passed. Independent audit: not yet performed.
