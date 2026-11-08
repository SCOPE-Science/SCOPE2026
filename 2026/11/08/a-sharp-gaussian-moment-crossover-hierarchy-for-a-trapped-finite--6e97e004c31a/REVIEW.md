# Scientific review: Gaussian-moment crossing hierarchy

## Correctness

**PASS.** The stated Markov generator identities are valid for bounded stationary polynomials on \([-1,1]\). They reconstruct the previously known exact even-moment product without reliance on a plotted density. Each factor of the variance-normalized product is strictly decreasing in the tumble-exit rate; the divergent small-rate limit and subunit large-rate limit prove exactly one root. The gamma-ratio and Stirling expansions at the singular scale \(T=c/n\) are uniform on compact positive ranges of \(c\), yielding the first-order boundary and the logarithmic correction with a controlled remainder. The standalone checker passes 206 finite diagnostic assertions; these are not substitutes for the analytic all-order proof.

## Originality

**PASS, with residual priority risk.** The 2024 Sun–Ye–Podgornik article already derives the full stationary hypergeometric characteristic function, the exact moment recurrence, and the unnormalized large-order support-edge scaling. None of those facts is presented as new. Its inspected introduction, moment, boundary-asymptotic, stationary-density and conclusion sections do not present the new all-even-order Gaussian-normalized crossing classification or the singular rate–order law with logarithmic term. The 2019 Basu–Majumdar–Rosso–Sabhapandit–Schehr paper concerns a special equal-switching-rate submodel and shape transitions, not the varying-rate crossing hierarchy. A known same-model stationary second/fourth/sixth-moment identifiability result addresses different inverse-data questions, not this comparison across all orders. Semantic literature and research-record comparisons found no stronger or equivalent statement; an unindexed equivalent or a pre-existing asymptotic consequence remains possible.

## Mathematical value

**PASS.** The question distinguishes two physically meaningful regimes of a trapped active particle relative to a passive Gaussian control at exactly matched stationary variance. The theorem gives a complete *unique threshold for every even moment*, rather than just one kurtosis sign check, and identifies the singular joint high-order/long-tumble scaling with a sharp constant and a nontrivial logarithmic correction. It clarifies why fixed positive tumble-exit rates eventually give a Gaussian moment deficit although small exit rates produce large standardized moments at each fixed order. No tail ordering, estimation guarantee or general multidimensional extension is inferred.

## Closest sources and limitations

The underlying stationary law and raw moments are prior work: https://arxiv.org/abs/2409.00578 (first posted September 1, 2024). The equal-rate three-state shape classification is https://arxiv.org/abs/1910.10083 (first posted October 22, 2019). The exact moment recurrence already implies the raw-data statements, so publication priority must be evaluated for the *derived crossing and singular asymptotic theorem*, not for the model or moment formula. Remaining limits are exact stationary sampling, positive fixed running rate and one-dimensional zero-temperature dynamics; a separately indexed theorem could cover the same asymptotic comparison.

Self-review: passed. Independent audit: not yet performed.
