# Mathematical review: universal ternary profiles of nested equivalences

## Correctness — PASS
The full type enumeration follows from the ultrametric triangle inequality on the least equivalence-coincidence level. All equality patterns and ultrametric three-point configurations are explicitly realized. The ternary-comb witness contains \(2K+3\) points and realizes every type. Each of the \(K+1\) merge levels must contain a node branching into at least three child classes, giving the lower bound through the leaf-count identity. Equality forces exactly one ternary branch at each level; the mixed \((i,j,j)\) triple types force these branches to lie on one chain, proving uniqueness. The verifier reproduced all type signatures through nine merger levels and all small hierarchical partition systems specified in the result.

## Originality — PASS within examined sources
Fiuk–Kieroński–Michielini (2025), sections 1–2 and relevant hierarchy definitions, and Fiuk (2026), including its atomic-types section 5.1 and appendix, were read in HTML. They study finite satisfiability and logical complexity over nested relations; neither inspected source asserts an exact single-model realization of every pure three-variable quantifier-free profile or uniqueness at a linear minimum. Published comparison claims on equivalence-relation rank-three theories, guarded fragments, and metric profile reconstruction concern distinct invariants. Searches for three-point ultrametric universality, ternary combs, tuple types, and equivalent definitions did not locate a covering statement. The full material for certain related published repository records and the 2015 broad metric-universality paper was not available; this is an explicit historical-priority risk, not evidence of absence.

## Value — PASS
Finite-model and database hierarchies are usually specified by increasingly coarse equality tests. The result gives a single optimal universal witness for every satisfiable pure existential three-variable Boolean condition in all \(K\)-level hierarchies, counts the entire local test space, and proves that the extremal finite design is rigid. The all-level exact resource bound and uniqueness go beyond a sample census, with potential use in local consistency testing and test-fixture construction. It does not claim general finite-model properties for formulas with quantifier alternations or additional predicates.

## Sources and limitations
- O. Fiuk, E. Kieroński, V. Michielini, *Two-Variable Logic for Hierarchically Partitioned and Ordered Data*, arXiv:2512.09508v1, https://arxiv.org/html/2512.09508.
- O. Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072v1, https://arxiv.org/html/2605.15072v1.
- V. Bilet et al., *Minimal universal metric spaces*, arXiv:1503.00667, https://arxiv.org/abs/1503.00667 (broad universality in a different setting; detailed full-text comparison remains limited).

The independent mathematical audit and external priority review have not been conducted. The exhaustive computation checks only the small cases stated above. The theorem holds only for the pure nested-equivalence signature with equality and three variables.

Self-review: passed. Independent audit: not yet performed.
