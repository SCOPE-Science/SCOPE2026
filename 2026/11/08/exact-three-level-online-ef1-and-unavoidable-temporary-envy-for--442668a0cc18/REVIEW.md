# Review of exact online EF1 at the three-agent surplus boundary

## Correctness

**PASS.** The terminal EF1 shape reduction is logically forced by positivity and exactly four goods among three agents; with a \((2,1,1)\) shape it reduces to comparison of one singleton to the smaller of the two goods in the doubled bundle, preserving the entire result under independent strictly increasing recodings of each agent's finite levels. The game recursion uses the correct quantifier order: the adversary picks a value triple, the allocator sees it and then chooses the recipient. The separate Python ordinal checker and C++ cardinal checker independently return the four asserted win/loss values and include the entire adaptive decision tree by complete finite recursion. No finite test is substituted for an infinite unrestricted claim: the infinitely many positive real ratios are covered by the proved exact ordinal reduction. Source paths and instructions for replay are embedded.

## Originality

**PASS, with residual literature risk.** Neoh–Teh (2026, arXiv:2610.34625v1) give approximate EF1 bounds with predictions for three agents and a negative exactness regime for at least five agents, but not an exact three-agent/four-good personalized three-tier cutoff. Wang–Wei (2025, arXiv:2505.24321v2) prove tri-valued impossibility under a requirement of fairness at every arrival, which does not imply failure of final-only fairness; indeed here a successful algorithm must sometimes violate EF1 after the second arrival. Elkind et al. (2024, arXiv:2410.14593v1) study temporal EF1 and two global item types, not this domain. A previously known two-agent/three-good ordinal-cutoff result does not imply the three-agent guarantee or first-two assignment separation. Matching statements, not merely keywords, were compared. Equivalent unindexed exhaustive game analyses remain possible.

## Value

**PASS.** For a canonical smallest-surplus three-agent market, the result completely classifies the precise value-alphabet boundary at which a deterministic online final-EF1 policy exists, despite known general temporal impossibility phenomena. The structural result shows why neither predetermined second-good occupancy pattern is sufficient and proves temporary fairness violations are sometimes necessary to preserve eventual fairness. This addresses an intrinsic distinction between online horizon fairness and terminal fairness rather than a purely arbitrary enumeration. The algorithm is finite and not claimed efficient.

## Literature and limitations

The exact two-agent small-market result is known, so no novelty is asserted for that smaller case. Published full-text inspections cover the motivating 2026 paper, the 2025 temporally constrained impossibility paper, and the 2024 two-type temporal fairness paper. The current exact cutoff depends on a known four-good horizon and strictly positive additive values and does not extrapolate to larger market sizes. Independently commissioned validation would be needed before publication.

Self-review: passed. Independent audit: not yet performed.
