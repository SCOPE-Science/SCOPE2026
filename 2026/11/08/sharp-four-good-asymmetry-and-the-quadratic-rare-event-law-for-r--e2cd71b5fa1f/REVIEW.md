# Scientific assessment

## Correctness — PASS

For agent-dependent, per-good independent Bernoulli utilities, realized EF1 reduces exactly to a binomial comparison with a one-unit margin; independence across agents factors its probability. The four-good binomial probabilities are explicit polynomials. The \(1:3\) score decreases strictly with the singleton agent's parameter, and its comparison with the \(2:2\) score is equivalent to the displayed exact threshold. A derivative with an elementary positive polynomial proves that the critical curve is monotone and has one crossing of \(1/16\). Direct analysis of the \(0:3\) versus \(1:2\) probabilities rules out earlier unbalanced optimizers. For arbitrary fixed \(m\), the only second-order EF1 failures have two successes in the opposing bundle; their coefficients give a strictly convex integer quadratic, proving the rare-event rule with its tie limitation. The standalone program passed 330 exact-rational and small-parameter consistency checks. The proof, not the finite program, establishes all-parameter statements.

## Originality — PASS, qualified

Igarashi and Oh's *Fair Division of Lotteries* (arXiv:2610.34906v1; first posted October 26, 2026) studies the same independent utility-realization model, but Theorems 4.2 and 4.5 concern ex-post **EF**, not EF1; their common-distribution hypotheses also exclude two different per-agent success parameters. The paper explicitly names EF1 as a future direction. The present results therefore do not follow by weakening their conclusions: an EF-probability maximizer need not maximize an EF1 probability, and their symmetric-distribution balancing argument cannot establish this heterogeneous phase diagram.

Aloisio et al. (2024) optimize expected maximum envy for precommitted allocations, not the probability of EF1. The full text could not be inspected from the available repository path, leaving residual priority uncertainty. Babaioff and Grofman (2026) analyze randomization *over allocations* with fixed valuations, distinct from random valuations under a fixed precommitted allocation. Existing calculations for shared binary good values, and for independent common-rate binary values under equal-size partitions, do not imply the new two-rate unequal-allocation optimization. Specific semantic research-record queries produced related Bernoulli inequalities and assignment-lottery results but no claim with these objects, event and parameters. This is a best-knowledge originality judgment, not an exhaustive proof of priority.

## Mathematical value — PASS

The natural question is whether a precommitted ex-ante equal, therefore envy-free, allocation maximizes the chance of satisfying the indivisible-goods relaxation EF1 after independent valuations are observed. The result resolves the complete first failure at four goods, not merely one counterexample: it locates all strict and tied parameter regions, including a nonmonotone interval in the high success rate. The separate arbitrary-fixed-\(m\) limit identifies a new squared-rate risk allocation principle and explains why a one-good shift emerges at the exact rate ratio \(\sqrt2\) for four goods. Such exact thresholds are useful for the design of nonadaptive lottery-good allocations when agents' valuation frequencies differ. The theorem is deliberately limited to two agents, binary utilities, full independence and fixed population in the rare-value limit; it is not promoted as a general optimal algorithm for other distributions.

## Closest literature and limitations

- A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1, https://arxiv.org/abs/2610.34906 — closest model, but exact EF rather than EF1 and common marginal laws in the optimum theorem; main sections and conclusion inspected.
- A. Aloisio et al., *Approximately Fair Allocation of Indivisible Items with Random Valuations* (2024), https://iris.gssi.it/handle/20.500.12571/30247 — precommitment and random utilities, but expected maximum envy; repository abstract inspected, full text not obtained.
- M. Babaioff and Y. Grofman, *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization*, arXiv:2601.16579v1, https://arxiv.org/abs/2601.16579 — fairness of lotteries over allocations, not independent Bernoulli valuations of a fixed allocation; main results inspected.

Residual risk remains for unindexed earlier exact probability calculations. At leading-order ties in the rare-value limit, the theorem identifies two surviving candidates but does not assert a finite-rate choice between them.

Self-review: passed. Independent audit: not yet performed.
