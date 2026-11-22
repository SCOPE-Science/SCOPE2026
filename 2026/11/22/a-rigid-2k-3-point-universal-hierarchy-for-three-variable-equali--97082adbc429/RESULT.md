# A rigid \(2K+3\)-point universal hierarchy for three-variable equality profiles

## Finding
For every integer \(K\geq0\), consider all nonempty finite structures in the pure signature consisting of equality and \(K\) named equivalence relations \(E_1\subseteq\cdots\subseteq E_K\). An *ordered three-variable quantifier-free type* is a complete consistent assignment of truth values to all equality and \(E_i\) atoms on the ordered variables \((x,y,z)\), allowing repeated elements. The number of types realized in some such structure is exactly
\[
T_K=1+4(K+1)+3\binom{K+1}{2}.
\]
A single structure realizes every type if and only if it contains a representative of every such ordered triple profile. The least possible size of such a universal structure is exactly
\[
U_K=2K+3.
\]
Moreover, the minimum-size universal structure is unique up to isomorphism. It is the *ternary comb*: three leaves share the first-level class; at each successive level, two new singleton branches join the existing cluster. Equivalently, its rooted hierarchy of equivalence classes has one ternary branch at each of the \(K+1\) merge levels, with all those branch vertices on one ancestor chain and no other non-unary branching.

As a consequence, for any quantifier-free formula \(\theta(x,y,z)\) in this pure signature, the existential sentence \(\exists x\exists y\exists z\,\theta(x,y,z)\) is satisfiable in some nested-equivalence structure if and only if it holds in the unique \((2K+3)\)-element ternary comb. This consequence does **not** extend to arbitrary quantifier prefixes or to additional unconstrained relation symbols.

## Assumptions and scope
The universe is finite and nonempty. Every \(E_i\) is reflexive, symmetric and transitive, and \(E_i\subseteq E_{i+1}\); equality has its usual interpretation. No strict containment is required. There are no colors, constants, orders, or additional symbols. Put \(h=K+1\), \(E_0=\Delta\) (identity), and \(E_h=X\times X\), the total equivalence. For distinct \(a,b\), define their *merger level*
\[
\ell(a,b)=\min\{j\in\{1,\ldots,h\}:a\,E_j\,b\},
\]
and set \(\ell(a,a)=0\). For \(K=0\), \(h=1\) and all distinct points have merger level one. All comparisons are made in the stated signature; the added \(E_0,E_h\) are definitions, not extra named predicates.

## Proof
**(1) The complete type classification.** Nested equivalences imply the strong triangle inequality
\[
\ell(a,c)\leq\max\{\ell(a,b),\ell(b,c)\}.
\]
Consequently, among three distinct points the maximum merger level occurs at least twice. Every ordered three-point type is therefore exactly one of: (i) all coordinates equal (one type); (ii) exactly one of the three pairs of coordinates equal, with the unequal coordinate at one of \(h\) positive merger levels (\(3h\) types); (iii) three distinct equilateral points at one positive level (\(h\) types); or (iv) three distinct points with one specified closer pair at level \(i\), and the other two pairs at level \(j>i\) (\(3\binom h2\) types). These categories are pairwise distinct, exhaust all possible complete atomic profiles, and all are feasible in finite hierarchies by constructing a three-point ultrametric with the indicated levels. Thus their sum gives \(T_K\).

**(2) A universal construction.** Label the \(2h+1\) points \(0,1,\ldots,2h\). Put \(\ell(a,a)=0\), and for distinct \(a,b\) define
\[
\ell(a,b)=\max\left\{1,\left\lfloor\frac{\max\{a,b\}-1}{2}\right\rfloor+1\right\}.
\]
At level one, \(0,1,2\) form one equivalence class. For each \(j=2,\ldots,h\), adjoin the two points \(2j-1,2j\) to the previous nontrivial class at level \(j\). Define \(E_i\) by \(\ell(a,b)\leq i\) for \(1\leq i\leq K\). These are nested equivalences because the construction is a rooted class tree. An equilateral type at level \(j\) occurs on the two newly attached points and any older point (using the initial three for \(j=1\)). For any \(i<j\), choose a pair merging at \(i\) inside the old cluster and a new point attaching at \(j\); permutations of the three coordinate positions realize the three closer-pair orientations. Every equality pattern and every positive level is realized as well. Hence the construction realizes all \(T_K\) types.

**(3) Sharp lower bound.** Represent an arbitrary hierarchy by the rooted tree of nonempty classes at each level \(E_0,E_1,\ldots,E_h\), with the \(n\) singleton classes as leaves and the unique total class as root. A node at level \(j\) has one child for each constituent \(E_{j-1}\)-class. To realize the equilateral three-point type at merger level \(j\), some node at that level must have **at least three children**. This is necessary at every \(j\in\{1,\ldots,h\}\). For any finite rooted tree with \(n\) leaves,
\[
n=1+\sum_{v\text{ internal}}(\deg^+(v)-1).
\]
There are therefore at least \(h\) distinct internal nodes each contributing at least two to the sum, giving \(n\geq1+2h=2K+3\). This argument applies even if some named equivalences coincide globally, since the required equilateral types force a branching at every level in a universal structure.

**(4) Uniqueness at equality.** Suppose \(n=2h+1\). Equality in the leaf identity forces exactly one node of three children at each level \(j\), with every other internal node unary. Denote the unique branching node of level \(j\) by \(v_j\). The universal profile with one closer pair at \(i\) and the other two pairs at \(j\) requires that \(v_i\) be below \(v_j\) (a closer pair lies inside one child cluster of the branching node at level \(j\)). In particular, consecutive levels satisfy \(v_1\prec v_2\prec\cdots\prec v_h\). Every branch except the one leading to the next lower branch vertex is unary all the way to a leaf, while \(v_1\) has three leaf descendants. Thus the hierarchy tree is necessarily the ternary comb, uniquely determining all named equivalence relations up to relabeling of points.

**(5) Existential three-variable consequence.** A quantifier-free formula is constant on each complete ordered three-variable type. Every realizable type occurs on the comb; hence if an existential triple satisfies the formula in any allowed hierarchy, an equal type satisfies it in the comb. The reverse direction follows because the comb belongs to the class.

## Verification
The standalone standard-library Python program `VERIFY.py` independently constructs the comb and its complete ordered-triple profiles for \(h=1,\ldots,9\) and compares against the formula and full type list. It also exhausts all single-equivalence partitions through five elements and all two-level chains of partitions through seven elements, checking the sharp sizes and unique unlabelled extremizer. Run from a directory containing the extracted artifact using `python VERIFY.py`. The observed output is:

```text
VERIFY_OK comb_depths=9 exhaustive_nested_structures=22207 unique_K2_shape=((1,), (1,), (1, 1, 3))
```

The exhaustive computations only cover the indicated small cases. The proof, not numerical enumeration, establishes the result for all \(K\geq0\).

## Relationship to prior work
Fiuk, Kieroński, and Michielini formulate finite-model questions for nested equivalence relations and explicitly interpret them as hierarchies of leaves. Fiuk's subsequent guarded-fragment paper extends this investigation to more variables and develops atomic-type techniques, but studies a general satisfiability/complexity setting, not a smallest **single** three-point-profile-universal hierarchy. In contrast, the claim here is confined to pure nested equivalences, exactly three named variables, quantifier-free types, and simultaneous realization in one finite structure. Related classification results for equivalence structures and ultrametric profiles use similar partition-tree or isometry-type ideas, but do not in the inspected material imply the sharp universal size and its unique all-level extremizer. This is a comparison within the accessible literature, not an assertion of exhaustive historical priority.

## Limitations
The result concerns only three-variable quantifier-free types of **pure** nested equivalences. It does not give small models for general first-order, guarded, or two-variable sentences with alternating quantifiers, or for signatures carrying colors, functions or additional free relations. The uniqueness is up to isomorphism of named equivalence structures, not literal equality of labels. Finite script checks are supporting evidence, not an independent mathematical audit. Earlier related metric-universality and partition literature may contain an equivalent formulation not identified by the available searches; independent historical verification has not been performed.

## References
1. O. Fiuk, E. Kieroński and V. Michielini, *Two-Variable Logic for Hierarchically Partitioned and Ordered Data*, arXiv:2512.09508v1, first public 2025-12-10. https://arxiv.org/html/2512.09508
2. O. Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072v1, first public 2026-05-14. https://arxiv.org/html/2605.15072v1
3. V. Bilet, O. Dovgoshey, M. Kucukaslan and E. Petrov, *Minimal universal metric spaces*, arXiv:1503.00667 (2015). https://arxiv.org/abs/1503.00667
