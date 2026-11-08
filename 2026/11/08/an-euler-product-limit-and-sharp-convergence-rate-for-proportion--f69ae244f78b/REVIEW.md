# Scientific assessment

## Correctness (PASS)

The mathematical claim has a self-contained proof that reduces the collector to independent geometric failure counts, bounds its hypergeometric failure parameters by \(q_N^m\), and couples the entire count sequence. The resulting sum of differences of geometric means bounds total variation by \(q_N/[N(1-q_N)^5]\). The \(q\)-binomial coefficient recurrence establishes the exact limiting mass function without relying on a numerical product. A pointwise product expansion and a summable bound prove the positive order-\(N^{-1}\) no-delay correction and therefore the sharpness of the total-variation rate along fixed rational-ratio subsequences. The extracted standalone checker gave 598 passed finite assertions, including exact rational brute-force enumeration. The proof, rather than the checker, supports the infinite conclusions.

## Originality (PASS, best-knowledge)

The main 2026 source gives exact phase-geometric decomposition and fixed-offer-size Gumbel results, but not the proportional-offer tight Euler law, its uniform total-variation comparison, or its sharp no-delay correction. Xu and Tang (2011) analyze the same least-collected policy, with exact mean and fixed-offer-size asymptotics; Berend and Sher (2026) consider a different retain-all policy. Known \(q\)-series identities themselves are credited. Published mathematical-record comparisons and scientific-source searches did not identify a covering theorem for this complete combination. This assessment is provisional: more general stochastic-approximation or \(q\)-probability results might give the same theorem as a special case.

## Mathematical value (PASS)

The offer fraction is a natural scaling parameter, not an arbitrary finite slice. For fixed \(d\) the model has a Gumbel-scale completion time, while for \(d_N/N\to\theta>0\), the process finishes only a tight number of rounds after the deterministic minimum. The theorem identifies the complete limiting probability law, moments and generating function, controls finite-size error uniformly across the entire distribution, and proves that the rate is optimal. These results are relevant when each round offers a macroscopic fraction of all opportunities but a scheduler is able to act on only one.

## Sources and residual limitations

Directly inspected source material: Doumas–Spektor (arXiv:2607.01463, full public text, equations (74)–(75), Theorem 20 and expansion proofs); Xu–Tang (2011, author-hosted full PDF, introductory formulation, Section 5, Theorem 4); Berend–Sher (arXiv:2605.06953, full arXiv HTML, Sections 2–3). Classical geometric and Euler identities are prior knowledge. Historical-priority uncertainty remains; endpoints of the offer-fraction regime and multicopy targets are not treated.

Self-review: passed. Independent audit: not yet performed.
