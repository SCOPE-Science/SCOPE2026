# Scientific review: congruence entropy on rooted trees

## Correctness — PASS

The claim concerns every congruence on the graph inverse semigroup of each finite outward rooted tree, and all complete \(b\)-ary trees with integer \(b\ge2\). Wang's congruence-triple correspondence (arXiv:1806.10721, Theorem 1.4) has a unique pair \((H,W)\) in this acyclic case. A root split produces the exact bivariate polynomial without overcounting. The complete-branching recurrences follow by specialization; a convergent geometric series of logarithmic increments proves the two growth constants. The strict lower bound on their difference is explicit and positive for every admissible \(b\). The tail estimates yield the stronger \(o(1)\) error in the exponential exponent, rather than only a sublinear bound.

The standalone verifier checks complete bivariate polynomials against independently enumerated Wang pairs for rooted binary trees through height three and ternary trees through height two. It additionally counts congruences by exhaustive semigroup multiplication on small graphs, rather than relying solely on the Wang correspondence. The finite checks support, but do not replace, the proof of infinite-height results.

## Originality — PASS relative to inspected literature

Wang (2018) already classifies every graph inverse semigroup congruence; Mesyan–Mitchell (2014) already characterize the role of non-Rees congruences; Luo–Wang–Wei (2023) and Anagnostopoulou-Merkouri–Mesyan–Mitchell (2021/2024) study lattice properties. The present statement is *not* a claim to a new congruence classification. Its contribution is the explicit full bivariate recursive enumerator and the sharp, strictly positive exponential Rees-scarcity rate for infinite complete-tree families. Those formulas and entropy limits were not found in the inspected pertinent statements or searched mathematical records.

This originality judgment has a residual risk: the recurrence is a nontrivial enumerative specialization of an established correspondence and might occur as an unpublished or unlocated consequence in the literature. A published broader counting theorem could supersede the claim.

## Mathematical value — PASS

The number of distinct congruences and the number of Rees congruences are canonical invariants of a semigroup, rather than an artificially sliced statistic. On an entire infinite family of exponentially growing finite semigroups, the exact counts lead to a quantitative structural statement: Rees congruences form an exponentially vanishing fraction of all congruences in the underlying number of graph vertices. The exact bivariate polynomial also makes the distribution by hereditary-set size and non-Rees selections computable for arbitrary rooted outward trees. The explicit strictly positive entropy gap is not supplied by qualitative prior characterizations of congruence lattices.

## Scope and closest literature

The inference depends on finite acyclic outward trees, not arbitrary directed graphs with cycles or arbitrary tree orientations. The comparison with Wang's theorem is especially close: it supplies the entire admissibility model, while the branching partition functions and entropy bounds are derived here. The quantitative asymptotic is for fixed \(b\ge2\); no uniform-in-branching assertion is made.

Self-review: passed. Independent audit: not yet performed.
