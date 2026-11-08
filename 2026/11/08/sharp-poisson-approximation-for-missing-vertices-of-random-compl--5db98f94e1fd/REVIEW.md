# Mathematical review

## Correctness (C): PASS

The exact coefficient decomposition counts subtrees by deleted vertices and includes all singleton boundary cases. The balanced logarithmic expansion is uniform for deleted-vertex counts at most a small power of the order, and the binomial second-moment identity cancels the order-one-over-size term against the prelimit Poisson parameter. For arbitrary proportional imbalanced sequences the first-order two-deletion residual has an explicit strictly negative limit. Leaf-extension double counting and a factorial tail make these local coefficient expansions into total-variation upper bounds; a Lipschitz three-mass witness yields the matching lower bounds. All quantifiers, normalizations and excluded extreme-imbalance cases are stated in the main result. The standalone checker passes 310 finite and asymptotic comparisons. This is an analytic proof, not an inference from tests.

## Originality (O): PASS, qualified

Chin et al. (2018), Proposition 3.1, already prove the exact complete-bipartite subtree polynomial; Theorem 3.4 treats the leading balanced spanning probability. Wagner (2019) provides dense-graph subtree-counting techniques; Wagner and Wang (2026), Theorem 2, provide a general but substantially coarser Poisson approximation. None of the inspected material gives the sharp balance-sensitive rates or signed residual, and published mathematical-record searches yielded only distinct graph-polynomial and spanning-tree results. This original claim is precisely the asymptotic refinement, not the exact enumerator or a first Poisson limit. Unindexed equivalent analyses remain a priority risk.

## Value (V): PASS

The balanced versus fixed-proportion unbalanced dichotomy supplies an order-of-magnitude improvement in total-variation approximation and a computable signed certificate of its cause. It quantifies when a natural Poisson approximation is unusually accurate and identifies the precise symmetry responsible, strengthening a known dense-graph convergence theorem in a canonical nontrivial example. Neither a mere small-parameter experiment nor a repackaging of the original counting polynomial is asserted.

## Limitations

Only proportional part sizes are treated; no claim covers extreme imbalance, the critical near-balanced transition, or other graph families. The comparison uses the exact finite-size mean intensity \(\theta=R_1\). The stated mathematical evidence has not been independently audited; historical priority is qualified.

Self-review: passed. Independent audit: not yet performed.
