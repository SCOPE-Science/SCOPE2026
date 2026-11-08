# Review: Two-median conservation and exact relaxation on bipartite opinion networks

## Correctness — PASS

Define weighted medians as observed values, with strict uniqueness on both sides of each initial center. Positive affine order equivariance proves the medians along the candidate trajectories. Their derivatives exactly match every agent equation, and full initial data are recovered. Prior global Lipschitz guarantees uniqueness; the exact proof covers every finite \(m,n\), positive normalized shared row weights and real initial opinions. The nearest-observed-neighbor \(K_{2,2}\) tie boundary is verified algebraically. The standalone exact-rational checker passes 1,289 admissible finite cases and four boundary rational times; it is corroboration only.

The strict half-weight conditions guarantee a unique median at every finite time by positive affine equivariance. The differential equation is directly satisfied, including all initial values. In the tie boundary example, the median choice must be among observed neighbor opinions, not an arbitrary point of an interval; this distinction is built into the proof and verifier. The infinite family is proved analytically, not inferred from finite testing.

## Originality — PASS, with residual priority uncertainty

The v1 initiating paper introduces this ODE and proves well-posedness, stable equilibria, and convergence; its v3 revises and expands qualitative claims. Both were inspected for the initial-data-to-limit map and partwise median invariance. Earlier asynchronous and synchronous discrete-time median models have different update laws. Exact statements and implications, not merely keyword nonmatches, were compared. Searches found no preempting two-median finite-time formula; unindexed equivalence remains a risk.

The initiating definition and general convergence are prior art: [https://arxiv.org/html/2404.16318v1](https://arxiv.org/html/2404.16318v1) and its same-work [https://arxiv.org/html/2404.16318v3](https://arxiv.org/html/2404.16318v3). Comparators include asynchronous discrete-time [https://arxiv.org/abs/2212.08808](https://arxiv.org/abs/2212.08808) and synchronous-inertia [https://arxiv.org/html/2406.17552v3](https://arxiv.org/html/2406.17552v3). The first paper's convergence-to-an-unspecified-equilibrium conclusion does not logically supply the exact selected equilibrium nor the two finite-time decay rates. A published but unindexed equivalent remains possible and is not treated as a disproved possibility.

## Value — PASS

A natural two-community structure supports a conserved pairwise order-statistic sum and gives a complete consensus-selection map, which qualitative global convergence does not determine. Exact \(e^{-t}\) internal and \(e^{-2t}\) intergroup transients identify different mixing timescales; robustness to nonmedian outliers and independence from group size make the invariant socially and mathematically interpretable. A four-agent tie example isolates the assumption controlling the phase transition to possible dissensus.

## Scientific limitations

Assumptions of positive, identical cross-group weights within each group and unique initial weighted medians are material. The conclusion does not extend unchanged to arbitrary row-heterogeneous weights, nonunique initial medians, or stochastic weighted-median models. The two exponentials are separate sharp modes only when their coefficients are nonzero. Numerical and exact-rational experiments are not substitutes for the general proof. No external independent audit has taken place.

Self-review: passed. Independent audit: not yet performed.
