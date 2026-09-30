# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

The Polya finite-dimensional distribution in Yu-Alajaji-Gharesifard is exactly the Beta mixture of iid Bernoulli sequences with parameters
\(a=R/\Delta\) and \(b=B/\Delta\). After self-loop deletion, \(Z_1\) has no effect on off-diagonal edges, and conditional on the Beta variable \(\Theta=p\), the graph is the independent random-addition threshold model \(T_{n,p}\) of Diaconis-Holmes-Janson. Their Theorem 6.5 therefore applies conditionally and gives the stated almost-sure random graph limit.

The displayed degree-limit density was checked against Theorem 6.5. Its first moment is \(p\), so the limiting edge density equals the mixing variable. The general subgraph polynomial follows by ordering the images of an injective homomorphism by birth time; each vertex with an earlier neighbor must be dominant, and no other creation bit is required. The clique and three-vertex-path specializations follow directly.

For the edge count, \(E_n=\sum_{t=2}^n(t-1)Z_t\) is exact for the loop-deleted graph. Conditional expectation and variance are \(\Theta W_n\) and \(\Theta(1-\Theta)Q_n\). The Beta moments give the stated total-variance formula. The conditional triangular-array CLT satisfies Lindeberg because \(\max_j j/\sqrt{Q_n}\to0\); bounded conditional expectations then give stable convergence jointly with \(\Theta\).

No contradiction was found in the boundary regimes: \(R,B,\Delta>0\) implies \(0<\Theta<1\) almost surely, and the fixed-\(p\) formulas have the correct complete/empty limits as \(p\to1/0\).

## Originality

**PASS, to the best of our knowledge.**

The full searchable version of Yu-Alajaji-Gharesifard was inspected around its model definition, Polya law, stated contributions, and cited random-threshold literature. Its stated results are exact degree distributions, decay centrality, Laplacian spectrum/eigenbasis, and consensus dynamics. Searches in that text for `graphon`, `edge density`, `central limit`, `clique`, and `triangle` did not locate the results proved here.

Diaconis-Holmes-Janson Theorem 6.5 gives the deterministic graph limit for iid dominant/isolated additions with a fixed parameter \(p\), including the explicit degree-limit law \(\mu_p\). It does not treat Polya reinforcement. Diaconis-Janson develops general connections between exchangeability and graph limits, including de Finetti-type mixture ideas, but does not specialize them to the 2026 Polya threshold model or derive the edge variance and stable two-scale fluctuation statement here.

External searches using combinations of `Polya threshold graph`, `graphon`, `graph limit`, `subgraph density`, `clique density`, `edge density`, `central limit`, `Beta mixture`, `reinforced threshold graph`, and `exchangeable threshold graph` did not locate a prior statement of the explicit Beta-random limit \(\Gamma_{\mu_\Theta}\), the motif polynomial \(P_H(\Theta)\), or the exact edge-variance/stable-CLT package for this model.

No inaccessible paper was identified whose title or abstract specifically indicates these Polya-threshold asymptotics. Residual originality risk remains from older exchangeable-graph, urn, or threshold-graph literature under different terminology. In particular, the graph-limit component is a short consequence of two known ingredients once the Beta mixture is recognized; originality is claimed for the explicit synthesis and its global-statistic consequences, not for de Finetti theory or fixed-\(p\) threshold graph limits themselves.

## Value

**PASS.**

The result supplies the large-\(n\) probabilistic description missing from the model paper: reinforcement does not wash out, but survives as a nondegenerate Beta-random graphon. This immediately yields all fixed motif-density limits, including a simple clique law and random transitivity limit. The exact edge variance and stable CLT separate order-\(n^2\) environmental fluctuations from order-\(n^{3/2}\) conditional sampling noise, giving a concrete mechanism for the non-ergodicity of the graph sequence rather than only of the underlying urn draws.

## Sources inspected

- Yu, Alajaji, Gharesifard, *Polya Thresholds Graphs*, arXiv:2603.18452 (2026), including the searchable full text around Sections 1-3 and the Polya finite-dimensional law.
- Diaconis, Holmes, Janson, *Threshold Graph Limits and Random Threshold Graphs*, Internet Mathematics 5(3), especially Section 6.3 and Theorem 6.5.
- Diaconis, Janson, *Graph limits and exchangeable random graphs*, for the general exchangeability/graph-limit relationship.

## Scientific limitations retained

The result is restricted to the classical constant-reinforcement two-color model, removes self-loops before applying simple-graph limit theory, provides no cut-distance rate, and proves a stable CLT only for the global edge count. The possibility that a generic older theorem can be specialized to recover some statements remains a residual originality risk.
