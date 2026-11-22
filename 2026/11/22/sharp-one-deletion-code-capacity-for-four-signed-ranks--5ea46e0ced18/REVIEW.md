# Scientific review: four signed ranks under one deletion

## Correctness — PASS

The source space has \(384\) signed four-permutations and \(48\) signed three-permutations. The proof defines an explicit nonnegative integer output weight with \(12\) zeros, \(32\) ones and \(4\) twos; its total is \(40\). The sign-pattern analysis supplies at least two total weight units for the complete distinct deletion deck of every source. Therefore the universal bound is \(20\). Ten explicitly listed tuples and their negatives form a twenty-word code. The attached independent inverse-insertion and direct-deletion check verifies the channel incidence on all \(384\) sources and certifies the \(46\) pairwise distinct outputs of this code.

The proof covers all signed sources at exactly four ranks; it does not extrapolate to higher ranks. The independent inverse construction is a computational cross-check, not an external mathematical audit.

## Originality — PASS, qualified

Gabrys and collaborators (2014, DOI: 10.1109/ISIT.2014.6875337) treat the unsigned rank-standardized channel. Their consecutive-run equivalence is acknowledged, and their broad asymptotic code result neither contains independent orientation signs nor fixes the signed four-rank capacity. Galvão, Lee and Dias (2015, DOI: 10.1186/s13015-015-0040-x) define signed permutations and study sorting by reversals/transpositions, not deletion-code capacity. Searches for type-B signed-permutation deletion codes, orientation-preserving rank-standardized deletion, and exact twenty-word codebooks did not locate an equivalent classification. A related published result on signed-successions encodes *ternary sparse-word* codes; another treats full-systematic *unsigned* permutation codes. Neither implies a bound on the present signed deletion incidence graph. Some corresponding repository full texts were not retrievable; historical priority remains qualified.

## Mathematical value — PASS

This exact value settles a natural zero-error coding invariant for ordered symbols with independent orientation attributes, where the unobservable deleted symbol loses both rank and orientation and all remaining ranks are renormalized. The matching half-integral output certificate and sign-symmetric code make the finite answer structurally interpretable and reusable as a benchmark for signed-rank deletion channels. The result is not a general signed-permutation coding theorem, not a new genome-sorting algorithm, and not a complete enumeration of optimizers.

## Closest literature and limitations

The unsigned channel's standard definition and consecutive-run lemma are covered by the 2014 ISIT paper. The 2015 molecular-biology paper supplies the signed-permutation representation but analyzes different edits. An exact-day public antecedent for the signed setting is 25 March 2015; the 2014 conference result is older by year but does not provide a verified first-online day. A stronger equivalent result in unindexed historical literature is possible; none was established by the inspected sources. The present certificate makes no independent-validation or priority-guarantee claim.

Self-review: passed. Independent audit: not yet performed.
