# Scientific review: two-threshold stochastic Hodge error

## Correctness — PASS

The domain is the linear rank-order priority game on the independent-edge random graph \(G(n,p_n)\), with equally weighted unilateral changes and deterministic tie protocols. Proposition 2 of Lin et al. provides the exact graphwise ratio of harmonic and total squared incentive energy, \(R=X/(2X+Y)\). The result proves all claimed regimes by exact edge/wedge moments and concentration, plus an explicit connected-diagram cumulant argument for the nontrivial joint central limit theorem at \(p_n=\lambda/n\). Matrix multiplication gives the positive variance \(2(1+\lambda)/(\lambda+2)^4\). The supplied executable independently checks all finite-graph moment identities and game-flow projections, including graphs with cycles. These finite checks are not substituted for the stochastic limit proofs. The zero-edge convention and Gaussian centering restriction are stated.

## Originality — PASS, with residual risk

The October 5, 2026 Lin–Lan–Nguyen–Kawahara source proves the deterministic finite-graph Hodge decomposition and its degree-count identity. It does not assert the stochastic network limit, the Bernoulli first-edge window, the fixed-degree Gaussian variance or the combined density classification. Ruciński's 1988 small-subgraph limit theory supplies classical probabilistic context but not a priority-game energy ratio, and Sturm–Wemheuer's 2024 abstract concerns broad weighted sparse-graph normal approximations without the ratio-specific constant. Direct source/claim/equivalence searches and comparisons with accessible prior research records did not reveal an equivalent statement or a stronger result implying the full combined finding. The fixed-graph energy identity is credited, not presented as new. Generic subgraph count results can be combined with it to derive some implications, so novelty priority could be challenged by an unindexed derivation; no assertion of exhaustive literature coverage is made.

## Mathematical value — PASS

The mathematical question is the stochastic cost of replacing decentralized priority incentives by a common potential when interaction networks are uncertain. The three macroscopic phases are separated by two natural random-graph scales: the first contact and the emergence of adjacent contacts. The exact positive Gaussian variance supplies risk and uncertainty information missing from a pointwise deterministic bound, independent of priority cardinality or tie orientation. The result is a complete asymptotic law for the canonical Erdős–Rényi network model and not an arbitrary small parameter census. It does not assert safety or welfare effects outside the formal incentive-error metric.

## Closest literature and limits

- Lin, Lan, Nguyen and Kawahara, *Priority Coordination Games: Hodge Decomposition and a Sharp Design Limit*, arXiv:2610.05832v1, Proposition 2, Remark 1, Corollary 1. The structural energy identity is prior work.
- Ruciński, *When Are Small Subgraphs of a Random Graph Normally Distributed?*, *Probability Theory and Related Fields* 78 (1988), 1–10. Classical subgraph counting and limit distributions.
- Sturm and Wemheuer, *A Central Limit Theorem for Functions on Weighted Sparse Inhomogeneous Random Graphs*, arXiv:2404.12740. General stochastic-graph central-limit methodology; only abstract-level comparison established.

The Gaussian law assumes exact \(p_n=\lambda/n\); the weak laws allow the indicated broader sequences. The definition on empty graphs is conventional, and independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
