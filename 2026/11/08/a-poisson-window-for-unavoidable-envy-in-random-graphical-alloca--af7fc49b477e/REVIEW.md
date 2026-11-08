# Self-review

## Correctness — PASS

The lower bound counts goods versus required positively valued recipients inside each nontrivial tree component, and applies even to arbitrary non-endpoint assignments. The upper bound orients a tree outward and a cyclic component around a chosen cycle and then outward; simplicity forces any other individual's bundle to carry at most one good valued by a given agent. Every assigned item contributes the maximum possible unit to welfare. For random graphs the factorial-moment formula for isolated edges uses exactly \(2r(n-r-1)\) forbidden edges. Trees of order at least three are uniformly ruled out by fixed-order estimates, a geometric estimate over intermediate orders and a binomial Chernoff bound for orders above half the vertices. Therefore the limiting mean is \(e^{-c}/4\), including its constant. A Python verifier tests all small simple graphs, and is not substituted for a proof of the limit.

## Originality — PASS, with specified residual risk

Misra–Sethia (arXiv:2410.14272), accessible in full, already prove the binary graphical EF existence criterion: do **not** credit that criterion or the orientation construction as a new result. Their inspected statement and proof do not count the **minimum number** of envious agents or derive its random-graph Poisson window. Manurangsi (arXiv:2610.34434, first public 2026-10-25), motivates random envy-freeness but considers an independent-permutation valuation model, not random graphs. Prior work by Bénadè and colleagues (arXiv:2307.09648) likewise uses stochastic valuations rather than the graph model. Classical random-graph isolated-tree counts cover probabilistic ingredients, so the narrower originality claim is the sharp fair-division deficit law combining the exact optimization identity with the graph component window. Named-equivalence and broader-implication searches identified no matching claim in the available literature and public research records. Risks: the recent motivating paper could not be read in full; the precise combination may have appeared in unindexed literature, and the underlying probabilistic techniques are standard.

## Value — PASS

The deterministic EF existence criterion does not quantify how many agents must be envious when EF fails. The optimal envy-deficit \(T(G)\) gives an interpretable exact measure of fairness shortfall for every realized graph, without welfare sacrifice. Its critical-window Poisson law identifies a finite nonzero probability of a perfectly fair optimal market while the market graph is still sparse and generally disconnected. The constant \(e^{-c}/4\) and the complete limiting distribution give a usable robustness benchmark, rather than an isolated small numerical construction.

## Scientific and reproducibility limits

The interpretation assumes binary symmetric unit endpoint values, a simple graph, fully allocated indivisible goods, strict unweighted envy and optimization over complete allocations. No conclusion is drawn for weighted, parallel-edge, general, or endogenous allocation models. The probability claim relies on \(G(n,p)\) independently present edges; the proof, not the checker, handles asymptotic limits. The full text of the recent motivating 2026 article could not be inspected, so that overlap risk remains explicit.

Self-review: passed. Independent audit: not yet performed.
