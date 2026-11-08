# Mathematical assessment

## Correctness — PASS

The global statement concerns *all* feasible symmetric stochastic kernels, not only orbit-invariant ones: convex averaging over the stabilizer of the exceptional vertex is valid for centered spectral norm. Internal sum-zero eigenvalues can be made exactly zero for every feasible pair of interblock weights, so the three-state quotient is both a lower bound and attainable. An exact missing-column norm bound proves the first phase. For larger missing stars, a fixed-off-diagonal two-by-two spectral-norm lemma and concavity of the restricted smallest Laplacian eigenvalue yield the other two phases. A block-constant Rayleigh vector gives a sharp dual spectral-gap bound in the last phase. Substitution proves the kernels are nonnegative and have their claimed spectrum. Rational verification covers 1,462 parameter combinations, including all phase transitions, but is not substituted for the universal proof.

Risk: errors in the two-dimensional quotient or its minimization would affect the conclusion; both were independently reconstructed algebraically and checked using exact arithmetic. The theorem does not establish uniqueness of arbitrary minimizers.

## Originality — PASS on inspected evidence

The general fastest-mixing SDP formulation of Boyd, Diaconis and Xiao (2004) includes convexity and symmetry reduction and explicitly solves the complete bipartite example. The symmetry paper of Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955v1, 2007) treats edge-transitive, distance-transitive, and several other structured families, with a detailed two-cliques-with-a-bridge example. The present complete graph with multiple missing edges incident to one distinguished vertex is not edge-transitive when both neighbor classes are nonempty, and the full three-phase formula does not follow from the quoted evaluated formulas. The more general SDP *algorithm* can solve individual instances, but without the new symbolic optimization does not supply this explicit classification. Previously available single-missing-edge and missing-neighbor inequalities are excluded from the novelty assertion.

Risks: an unindexed specialist paper may contain an equivalent threshold-graph instance or an implicit parameter formula. Search failure is not a proof of novelty; the available exact-source comparison supports a qualified originality assessment, not independent publication-priority certification.

## Mathematical value — PASS

The object is a minimal controlled departure from a complete mixing network, and deletion of an incident star distinguishes concentrated damage from matching-edge deletions. The result completely determines the best achievable uniform-stationary asymptotic mixing rate and provides feasible optimal transition probabilities for *every* star size. The two distinct transitions distinguish attainability of the universal missing-column bound, saturation of a row capacity, and a subsequent switch from balanced to one-sided spectral control. This is a natural exact graph-design classification rather than an arbitrary numerical slice or a routine parameter substitution.

## Sources and limitations

Primary literature inspected in relevant full-text sections: S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review (2004), https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf; and S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007), https://arxiv.org/pdf/0709.0955. Related exact results for complete-graph matching deletions were compared at statement/implication level and were found to cover only the distinct one-missing-edge boundary, not the claimed family with at least two incident missing edges.

No independent mathematical audit or exhaustive literature certification has been performed.

Self-review: passed. Independent audit: not yet performed.
