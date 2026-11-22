# Review: second-order coherence on weighted sunlets

## Correctness — PASS

The spectral blocks of the weighted sunlet Laplacian yield exact identities for both inverse moments. Strict matrix trace convexity on the mean-zero positive-definite subspace, injective edge-weight parametrization, and averaging under dihedral automorphisms prove unrestricted global uniqueness. The derivative of the exact one-variable F2 objective is the cubic P_n with exactly one positive zero. For every n>=3, the verified positive polynomial T(n-3) proves P_n(t_1)<0, hence t_2>t_1. Leading orders of the cubic give t_2/n -> c, while the first-order square-root allocation gives t_1/sqrt(n) -> 1/sqrt(6); direct expansion yields absolute regret asymptotic to (sqrt(6)/90)n^(11/2). Independently executed check_sunlet.py passed 1009 finite numerical and algebraic diagnostics; those checks are not infinite proofs.

## Originality — PASS on inspected evidence, with qualification

Primary coherence work establishes the squared-reciprocal Laplacian metric but not sunlet conductance optimization. Effective-resistance design optimizes a different first inverse moment. The weighted corona paper supplies spectral characteristic polynomials and first-order coherence, not the optimized second inverse moment. Two retrieved complete sunlet and one-leaf corona results maximize the smallest positive Laplacian eigenvalue: their statements and proofs use eigenvalue min-max/SDP, whereas the new theorem minimizes the full inverse-square spectral sum and has a distinct cubic stationary equation. published-finding corpus semantic search with aliases for biharmonic index, spectral zeta, edge allocation, and source objects returned no implication-covering claim among the inspected closest results. Searches do not certify universal novelty; unindexed equivalent work remains a residual priority risk.

The closest primary sources and mathematically comparable findings are:

- Patterson and Bamieh (2013), arxiv:1310.2592v1, Section II-B: second-order coherence is a squared-inverse spectral sum, but no sunlet conductance budget optimum.
- Ghosh, Boyd and Saberi (2008), *Minimizing Effective Resistance of a Graph*: first-order inverse-trace conductance allocation, not the second-order objective.
- Du, Zhu, Gao and Li (2022), *Consensus analysis of the weighted corona networks*: weighted corona identities and first-order coherence, not second-order design.
- *Unique price-optimal fastest mixing on sunlet networks* (2026), full RESULT.md inspected: optimizes the Fiedler eigenvalue under prices, not the full inverse-square trace.
- *Exact price-optimal continuous-time mixing on transitive one-leaf coronas and rigid cyclic sunlets* (2026), full RESULT.md inspected: same difference in objective.

An unindexed equivalent optimization remains a publication-priority risk. The inspected literature and bounded semantic searches establish only a qualified originality assessment.

## Value — PASS

This is an infinite natural family of two-class unicyclic networks: the precise second-order optimal budget and support are determined against arbitrary asymmetric edge allocation, with a strict all-size structural mismatch from the classical first-order objective. The discrepancy changes the power-law scaling of pendant conductance from n^(-3/2) to n^(-2), and entails a sharp diverging absolute second-order regret. The relative regret tends to zero; no constant-factor penalty is claimed. The result supplies a reproducible spectral-network design benchmark beyond an unmotivated numerical instance.

## Scientific limits and verification

The proof requires connected support, symmetric undirected weighted Laplacians, one pendant per cycle vertex, uniform edge prices, and a unit total conductance budget. The absolute regret grows at the specified rate, but the relative regret vanishes. The executable checker was run and passed 1009 finite diagnostics; it is not an exhaustive infinity check. No external mathematical certification is claimed.

Self-review: passed. Independent audit: not yet performed.
