# Self-review

## Correctness — PASS

The asserted equivalence, structural criterion and count have common hypotheses: a finite star with one center and \(k\ge1\) leaves, \(1\le n\le k+1\) labeled agents, identical nonnegative additive vertex utilities, and complete nonempty connected bundles. Every legal allocation consists of one center bundle and singleton-leaf bundles. The exact local paired maximin share isolates one leaf from the pooled induced star. A PMMS violation exists exactly if a larger-valued leaf is held at the center, a smaller-valued leaf lies outside, and the center bundle has strictly more value than that held leaf. Nonnegative additivity reduces the only exceptional equality to a zero-valued center with at most one positive held leaf. This yields the sorted-threshold binomial count or the exceptional zero/one-positive count without double counting, including empty and all-leaf center subsets. A violating pair can exchange leaves and strictly improve the global leximin vector. All nonviolating allocations have the same sorted utility vector, so PMMS equals leximin for this family. Finite exact checks separately enumerate the legal two-way partitions and the global leximin optimum: 83,309 settings and 1,391,766 center-subset choices, with no discrepancies. The proof, rather than the experiments, establishes the unbounded-real-value theorem.

## Originality — PASS, subject to bibliographic uncertainty

Hummel and Igarashi (2024, arXiv:2401.14825, Theorem 6.1) establish the general direction leximin implies local PMMS for identical valuations and prove tree-based existence and algorithms. Their inspected full text does not give the converse for stars, every local PMMS allocation, the all-parameter multinomial/binomial census, or the zero-hub jump. The 2017 *Fair Division of a Graph* treatment of connected allocation and stars addresses proportionality and other guarantees rather than this local PMMS optimizer classification. Unconstrained PMMS studies concern different feasible partitions. Relevant exact claim, alias, implication, and broader-coverage searches in published mathematical records and open scientific literature identified no dominating theorem. An unindexed or otherwise inaccessible equivalent may still exist; failure to find one is not a uniqueness proof.

## Value — PASS

The result closes a natural all-solutions question left open by an existence result: it characterizes every locally PMMS allocation for all common additive nonnegative weights, calculates its exact census and prevalence among all connected allocations, proves an equivalence of local PMMS and global leximin that is special to the star structure, and identifies a discontinuity at precisely zero center value. The zero-center exception makes a sorted-only heuristic incomplete and the full classification nontrivial. Counting and sampling fair connected allocations and understanding when local/global welfare orderings coincide are natural questions in graph-constrained fair division. The result is not asserted to extend to other graphs or heterogeneous valuations.

## Closest work and limits

- H. Hummel and A. Igarashi, *Keeping the Harmony Between Neighbors: Local Fairness in Graph Fair Division*, arXiv:2401.14825 (2024), Sections 3 and 6, especially Theorem 6.1. Inspected full preprint, including its star discussions and tree construction.
- S. Bouveret et al., *Fair Division of a Graph*, arXiv:1705.10239 (2017), inspected preprint; establishes background connected graph allocations and star algorithms for different fairness goals.
- G. Amanatidis et al., *Comparing Approximate Relaxations of Envy-Freeness*, arXiv:1806.03114, inspected abstract/background only; unconstrained PMMS is not itself a covering result.
- Residual risk: possible unindexed equivalent PMMS star classification; no independent audit. Direct enumerations do not certify all real-valued instances.

Self-review: passed. Independent audit: not yet performed.
