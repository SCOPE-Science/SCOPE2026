# Independent mathematical audit

## correctness

PASS

Independently reconstructed the deterministic normalization: decompose one endpoint's per-edge payoff into a constant, two centered one-coordinate terms and a row/column-centered interaction. The opponent has the complementary payoff. The slope in each player's own priority is 1/K after averaging over a neighbor, independent of tie orientation, so the potential gradient energy is c_K sum d_i². The opposite-signed interactions have cancelling profile divergence and are orthogonal to gradients; across distinct neighbors their mixed products average to zero. For each endpoint interaction the squared matrix norm is (K²-1)/12 (subtract the two main-effect variances from the Bernoulli variance); summing unilateral differences gives c_K per incidence. Thus R=X/(2X+Y) under unordered equal-weight moves; doubling all moves would cancel in the ratio. Counting edges and wedges gives the listed expectations and covariances. In particular writing each edge indicator as p+epsilon makes the centered Y equal to 2q p sum epsilon plus twice the centered quadratic wedge sum; the latter is orthogonal to the linear sum and has variance 4H[p(1-p)]² including the factor of two. This independently gives the sparse covariance and, by the displayed gradient, variance 2(1+lambda)/(2+lambda)^4. Connected edge-sharing cumulant patterns have v<=e+1 and O(n^v p^e) contribution, hence after scaling only the covariance survives; exact p=lambda/n gives O(1) bias in the means. At n²p bounded the wedge expectation vanishes and the Poisson edge law gives the Bernoulli mixture. When n²p diverges with np small the wedge-to-edge ratio vanishes by concentration and Markov; when np tends to a finite positive constant both statistics concentrate on scale n; and when np diverges relative variances vanish. The no-edge convention and boundedness justify the stated limits. Frozen VERIFICATION.md and verify.py were inspected, not executed; `OPENBLAS_NUM_THREADS=1 python3 /workspace/reproductions/frozen_checks.py 5` independently checks both absolute finite energies at K=2,3,4 with cyclic edgewise ties.

## originality

PASS

Pass for the combined stochastic ratio laws and explicit fluctuation coefficient, not the exact finite-game formula, the thresholds for raw graph edge and wedge counts, or a new CLT method. The assigned record itself is the exact Resultary hit; the strongest distinct hits concern degree-score third cumulants and fixed-edge isolate–motif covariance. Classical subgraph methods provide the tools to derive the stated result, but the available statements do not themselves give the normalized priority-game ratio regimes and law. Closest full-text access limits are recorded rather than treated as evidence of absence.

## value

PASS

The stochastic ratio measures a specific obstruction to a potential approximation, and the zero-denominator convention makes its first-contact limit genuinely different from the positive-mean-degree fluctuation analysis. The two scaling windows and exact Gaussian variance turn a pointwise identity into quantitative distributional predictions. The second window is when wedges become appreciable relative to edges, not the first appearance of any wedge, and the claim concerns incentive error rather than safety or welfare.

The dated certificate retains the supplied scientific assessment, sources and limitations.
