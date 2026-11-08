# Self-review

## Correctness — PASS

For the original 2024 **neighbor-valued** median definition, the two equal-weight center neighbors are both admissible discrete medians, and the specified nearest-neighbor rule selects the nearer leaf, choosing the smaller leaf at equality. The leaves maintain their order, with exact half-separation \(d_t=(1-s)^t d_0\). The derived normalized map \(T_s(w)=[(1-2s)w+s\sigma(w)]/(1-s)\) follows by substitution. Consensus follows from a scalar forced-contraction inequality and absolutely summable mean increments. The switching dichotomy follows from explicit one-sided branches and the repelling fixed points for \(s>2/3\); finite exceptional preimage sets give a countable union. At \(s=3/4\) the two affine branches each cover the whole interval and have slope of magnitude two, yielding exactly equal length-k cylinder probabilities. Exact-rational checks in `verify.py` cover the critical identities and boundary cases. No finite computation is used as proof of the infinite statement.

## Originality — PASS, best-knowledge

The original 2024 source's model and its numerical/mean-field analysis were compared against the precise conclusion about *median-neighbor identity*, not merely consensus. A critical definition distinction was independently checked: the source's 2025 revision permits any real weighted-median minimizer and projects the center into the leaf interval, so the two versions cannot be treated interchangeably. Mei et al.'s different asynchronous median dynamics concern state convergence rather than the original synchronous nearest-neighbor sequence. Searches for the normalized map, the threshold \(2/3\), iid fair itinerary and model aliases did not locate an implication or covering theorem. The piecewise-affine full-shift fact is classical and explicitly not claimed as a general mathematical novelty. Risk: an independent unpublished or unindexed derivation, or a source not fully accessible, may already obtain the model-specific theorem.

## Value — PASS

The sharp boundary separates finite eventual stabilization of the **actual social influence choice** from indefinite influence switching on the smallest connected graph where a choice is possible, despite consensus in both regimes. The special parameter \(s=3/4\) realizes a full Bernoulli symbolic process from deterministic dynamics and one random initial condition. This reconciles apparently erratic decisions with convergent scalar opinions and illustrates structural sensitivity to the later revision of the median definition. The result is motivated by an expressly social-network update model and does not depend on arbitrary external numerical slices.

## Limits and closest literature

This result is not a general convergence theorem for arbitrary graphs and does not apply to arXiv:2406.17552v3's real-minimizer definition. Only the 2024 discrete-neighbor variant, a three-node path and equal center weights are treated. The classical full-branch affine map is standard; the contribution is its exact realization and parameter threshold for the specified influence mechanism. An independent literature-priority audit is absent.

Self-review: passed. Independent audit: not yet performed.
