# Review of sine-weight variation stability for sorting

## Correctness
**PASS.** The exact two-input weighted-variation operator norm is a maximum-cardinality-cut formula, not a single-input quotient. Sorting is piecewise an arbitrary coordinate permutation, the weighted first-difference norm reduces each permutation to finite step columns, and every derivative can be attained inside a strict sorting chamber. The sine weights saturate a central maximal cut for every cardinality. A nonnegative central-cut matrix provides a direct comparison proof of the all-weight lower bound and a full-support central row proves unique weight optimality. The standard-library exact-rational checker exercises all finite fixed-cardinality cut cases through length eleven, thousands of rational test cases and an actual attaining two-input pair. The analytical proof covers all finite dimensions; numeric trigonometric tests are only corroboration.

## Originality
**PASS, subject to historical priority risk.** Chong's 1975 Theorem 2.1 and Duff's classical rearrangement theory concern reduction of one signal's variation. The published exact weighted-path sorting result likewise computes the single-input ratio (a minimizing cut denominator), not this two-input maximizing-cut numerator. An inspected finite-star two-point sorting theorem controls quadratic Sobolev energy, not weighted path \(\ell^1\) differences; an unrelated three-point median sine optimization cannot imply this result. Direct published-finding corpus searches for permutations, weighted two-input BV, maximum cuts, sine weights and cotangent/cosecant constants found no implying coverage. A relevant Duff (1967) full text was inaccessible, and unindexed priority risk remains.

## Value
**PASS.** This is a complete and sharp stability classification for a natural nonlinear map, including the optimal choice of all positive spatial edge weights, a rigidity statement and explicit parity-dependent constant. The theorem quantifies why rearrangement's one-input variation reduction does not control perturbation sensitivity and how much an optimally chosen path metric mitigates that instability; the improvement is asymptotically from \(n\) to \(2n/\pi\), not a small isolated gain.

## Closest literature and limitations
K.-M. Chong, *Variation reducing properties of decreasing rearrangements* (1975), https://doi.org/10.4153/CJM-1975-040-2; D. Anevski and A.-L. Fougères (2007), https://arxiv.org/abs/0710.4617; S. Bankevich and A. Nazarov (2014), https://arxiv.org/abs/1402.3006. Closest published records: *Isoperimetric sharp constants for sorting in convex weighted-path energies* (single-input) and *Sharp two-point stability of sorting in finite-star Sobolev norms* (star quadratic metric). No continuous, weighted higher-dimensional or infinite sequence claim is established. Independently unverified historical priority remains possible.

Self-review: passed. Independent audit: not yet performed.
