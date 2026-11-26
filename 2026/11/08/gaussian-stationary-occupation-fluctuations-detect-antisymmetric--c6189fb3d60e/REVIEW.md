# Independent mathematical audit

## correctness

PASS

For the column generator the imbalance is s=B1 with s_i=Σ_{j≠i}(X_{ij}−X_{ji}), giving δ=s/(μn²)+Bδ/(μn). Each independent centered edge matrix is supported on a two-coordinate subspace; both Bernstein variance operators are bounded by a constant times Σ_{i<j}(E_ii+E_jj)=(n−1)I times that constant. Thus ||B||=O_P(√(n log n)), ||s||=O_P(n), and the remainder has ℓ² norm O_P(n^(−3/2)√log n). Exchangeability and a permutation-invariant truncation of this norm give o_P(n^(−3/2)) per fixed vertex; the norm bound alone would not do that. Removing the finitely many internal pairs separates the sums at finitely many vertices for the joint CLT; two-coordinate asymptotic independence then gives the empirical law. For the squared sum, conditioning on the single shared pair gives Cov(s_i²,s_j²)=Var((X_ij−X_ji)²), while each Var(s_i²)=O(n²). This gives L² concentration of n^(−2)Σs_i², and the remainder is negligible after n² scaling of ||δ||². At v=0 symmetrization is exact because X=X' almost surely. For the two-point example μ=2 and v is respectively 0, 2, 4, as claimed. The uploaded verifier was inspected, not executed; numerical finite instances are not needed to establish the bounds or limits.

## originality

PASS

The checked prior work gives closely related models and first-order estimates, but does not give or dominate this joint pair-correlation-sensitive second-order law. This is a bounded comparison, not certification of priority.

## value

PASS

Equal marginals and an identical uniform first-order limit can hide three different disorder responses. Identifying a pair-antisymmetry invariant that controls both local fluctuations and global susceptibility distinguishes these ensembles, rather than just refining an error bound by a constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
