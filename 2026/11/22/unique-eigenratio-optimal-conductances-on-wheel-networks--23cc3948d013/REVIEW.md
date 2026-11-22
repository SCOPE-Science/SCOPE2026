# Scientific review: unique eigenratio-optimal wheel conductances

## Correctness — PASS

The unrestricted claim follows from three exact Rayleigh comparisons: the hub-against-rim mode, the first rim Fourier pair, and the largest rim Fourier mode. These prove an explicit lower bound on the entire eigenratio for **every** nonnegative independent edge allocation. That bound is minimized at precisely one mean rim-to-spoke ratio, and the usual wheel Fourier spectrum shows attainment. Equality in the first-frequency bound forces cosine and sine eigenvectors. Their complex combination imposes common rim conductance by the imaginary part of its eigenvector equation and common spoke conductance by its real part. The total budget then fixes a unique global optimizer. Boundary graph size \(m=3\), odd/even highest Fourier modes, zero rim edges, arbitrary budget scaling and connectedness were checked separately. The deterministic standalone verifier reports 3910 finite supporting checks, including exact symbolic characteristic-polynomial checks; these are supplementary to the infinite-family analytic proof.

## Originality — PASS on inspected evidence, qualified

The earlier complete wheel connectivity-design theorem at the cited public full-text URL solves maximization of \(\lambda_2\), provides the wheel spectrum, and establishes Fourier-mode rigidity. Those pieces **are prior work**. Kempton, Herrmann and di Bernardo's arXiv:1505.07279 is a general Laplacian eigenratio framework; because the objective is scale-free, its per-node upper caps cover the same allowable conductance rays as a global positive budget, which is acknowledged explicitly. Their inspected text does not provide this exact wheel allocation or unique nonsymmetric certificate. Boyd et al.'s 2009 wheel solution minimizes stochastic-chain SLEM and differs in the six-rim optimal ratio. The distinct resistance, spectral-width (2011 full preprint) and eigenvalue-design literature was compared by objective and implication. The novelty claimed is solely the sharp eigenratio wheel formula, unrestricted uniqueness, and quantitative asymptotic incompatibility with fastest absolute decay; unindexed equivalent literature and potential unindexed equivalent literature remains a priority risk.

## Value — PASS

The eigenratio is a standard spectral conditioning and synchronization measure; wheels have a naturally tunable hub-versus-ring architecture. An exact all-size support-and-weight classification is useful in assessing such designs. The exact discrepancy shows that reducing a *relative* eigenvalue spread can require funding nearly all edges on the slow rim and dramatically sacrificing absolute convergence rate. For large wheels the eigenratio gain is additive \(\pi^2+o(1)\), but the absolute spectral gap falls to asymptotic fraction \(4/m\) of its maximum. This structural distinction survives the whole infinite family and is not a routine value-free numerical instance.

## Limits and adjacent literature

The proof is for nonnegative symmetric combinatorial Laplacians with uniform vertex masses, equal conductance prices, total budget and connected wheels. It does not address stochastic positivity, heterogeneous costs, arbitrary graph structures, or minimum absolute-rate constraints. Prior general wheel Fourier and spectral-optimization tools are fully acknowledged, and the published closest same-graph spectral-gap theorem was read rather than treated as a disjoint result solely by name. Some equivalent publication may remain undiscovered; self-review does not establish independent validation.

Self-review: passed. Independent audit: not yet performed.
