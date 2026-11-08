# Review of the stationary bipartite noisy-voter crossover

## Correctness (PASS)

The claim is confined to simultaneous independent updates, not conventional random-sequential voter moves. Strict positivity of the transition matrix at nonzero noise proves unique stationarity. Because each new part depends only on the opposite *old* part and independent local randomness, cross-part independence is preserved at each finite step and in the stationary weak limit. This establishes independence of entire part configurations rather than only their first two moments.

On a complete bipartite graph, each fresh part count is conditionally binomial given the opposite previous count. Composing two steps yields an exact scalar transition with drift \(-(1-q^2)(u-1/2)\) and conditional variance \(\mu(1-\mu)/a+q^2(1-a^{-1})r(1-r)/b\). The uniform third-moment bound makes the stationary diffusion-generator limit valid. The polynomial moment recursion uniquely identifies \(\operatorname{Beta}(2\lambda,2\lambda)\) on \([0,1]\). Exact same-part two-spin recurrences establish both boundary regimes without assuming a fixed part-size ratio. Finite independent exact-rational checks replay all identities; they do not serve as an infinite proof.

## Originality (PASS, qualified)

The closest same-update treatment is Benjamini–Helman Tov–Zhukovskii (arXiv:2207.01224), especially Section 6 of the full text. It computes a *single-vertex temporal repetition statistic* on \(K_{n,m}\); the inspected results do not give the stationary same-time factorization of all vertex spins across the bipartition, nor a joint fraction limit or sharp three-phase noise scaling. General voter stationary results by Pymar–Rivera (arXiv:2112.01478) and Ben-Ari et al. (arXiv:2004.10187) operate with asynchronous updates, and Mori et al. (arXiv:1810.05643) examine an interacting, non-product multivariate Beta model. published-finding corpus semantic searches using synchronized voter, stationary independence, and Beta-limit formulations found no directly covering published finding. This is best-knowledge originality, not a guarantee that every older paper has been located; the exact independence observation is structurally simple and may have been implicit elsewhere.

## Value (PASS)

The theorem isolates an overlooked dynamical distinction: in the synchronous bipartite model, two repeatedly interacting classes are independent *at the same stationary time*. At vanishing noise, the independent endpoint limits mean disagreeing whole-class consensuses occur with probability tending to \(1/2\), unlike joint consensus behavior commonly associated with asynchronous updates. The critical scaling depends only on the sum of reciprocal part sizes and remains valid with arbitrarily unbalanced diverging populations. The complete three-regime classification and joint non-Gaussian law provide a concrete reference for parallel-update interacting-particle systems.

## Scope, closest sources and risks

The exact factorization applies to any finite loopless bipartite graph without isolated vertices, but the explicit crossover requires complete bipartite sampling. Other update conventions, self-loops, temporal correlations, convergence rates, and exactly zero reset noise are outside scope. Historical-priority risk persists because the broad interacting-particle literature cannot be exhaustively audited by a limited source search. The full same-process paper has been read in its relevant sections; neither similarity of models nor absence from search results was treated as sufficient novelty evidence. The asymptotic proof and its exact finite identities are independently reconstructible from the manuscript.

Self-review: passed. Independent audit: not yet performed.
