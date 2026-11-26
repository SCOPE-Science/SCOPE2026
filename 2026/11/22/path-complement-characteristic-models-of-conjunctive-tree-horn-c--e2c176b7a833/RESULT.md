# Sharp characteristic-model counts for conjunctive tree Horn closures

## Finding

Let \(T\) be a finite rooted tree on \(n\ge 1\) vertices, with \(L\) leaves. At each nonleaf \(v\), impose the one definite Horn implication \(\operatorname{ch}(v)\to v\), with the entire child set as its premise. Let \(c(T)\) be the number of proper meet-irreducible closed sets (the Horn characteristic models). Then
\[
n\le c(T)\le L(n-L+1)\le \left\lfloor (n+1)^2/4\right\rfloor.
\]
The lower bound is attained exactly by rooted paths. For each feasible pair \((n,L)\) with \(n\ge 2\), the middle bound is attained exactly by brooms: the internal vertices form a chain starting at the root, and every leaf is attached to its last vertex. In particular the upper bound for fixed \(n\) is attained exactly by brooms with \(L\) nearest to \((n+1)/2\) among the integers \(1\le L\le n-1\). The one-vertex tree attains both bounds.

This gives a sharp bound on the number of models in the characteristic representation, not just an enumeration algorithm. The argument uses a path-complement description that also follows by specializing general acyclic Horn decomposition results, as explained below.

## Assumptions and scope

The ground set \(V\) consists of the actual tree vertices. The only implications are \(\operatorname{ch}(v)\to v\) for nonleaves \(v\). In particular, there is no rule for a leaf, there are no nullary premises, and an all-children premise is not replaced by one implication per child. Unary internal vertices are allowed. The dependency digraph is acyclic; a vertex appears in at most one premise and as the conclusion of at most one rule. A proper meet-irreducible is a closed set other than \(V\) that cannot be expressed as the intersection of two strictly larger closed sets.

## Structural input and proof

**Closed sets and paths.** Write \([u,\ell]\) for the vertex set of the directed path from a vertex \(u\) to a descendant leaf \(\ell\), allowing \(u=\ell\). The complement \(O=V\setminus X\) of a closed set has the following property: each nonleaf in \(O\) has at least one child in \(O\). This property is also sufficient for closure of \(X\), because it excludes exactly the cases in which some omitted vertex has its entire premise present.

If a closed set omits \(u\), the property allows us to follow omitted children from \(u\) until a leaf is reached. Thus it is contained in the complement of a path \([u,\ell]\). Conversely the complement of such a path is closed, and no strictly larger closed set can still omit \(u\): within that path the successive omitted children are uniquely forced. The path complements are therefore exactly the maximal closed sets omitting \(u\).

In any finite closure system, a maximal closed set omitting some \(u\) is proper meet-irreducible, because every strictly larger closed set contains \(u\). Conversely every proper meet-irreducible has a unique cover in the inclusion lattice: two distinct covers have intersection equal to the set, and at least one cover exists because the set is proper. Any element added by the unique cover belongs to every strictly larger closed set. Thus the meet-irreducibles are precisely the path complements \(V\setminus[u,\ell]\) for all descendant leaves \(\ell\) and their ancestors \(u\). Different paths give different complements, since their vertex sets determine their first and last vertices.

**Deficit sizes.** The deficit of a model \(M\) is \(n-|M|\). A leaf \(\ell\) at depth \(d\) accounts for one path of each size from 1 to \(d+1\), so
\[
Q_T(z):=\sum_{M\text{ proper meet-irreducible}}z^{n-|M|}
=\sum_{\ell\text{ leaf}}\sum_{j=1}^{\operatorname{depth}(\ell)+1}z^j.
\]
In particular \(a_0=[z^0]Q_T(z)=0\). For \(j\ge 1\), the coefficient \(a_j=[z^j]Q_T(z)\) is the number of leaves of depth at least \(j-1\); the sequence \(a_1,a_2,\ldots\) is nonincreasing. The number of leaves at depth \(d\ge 0\) is \(a_{d+1}-a_{d+2}\), taking coefficients beyond the degree to be zero.

**Sharp counts.** Counting paths by their first vertex gives \(c(T)=Q_T(1)=\sum_{u\in V} \#\{\ell:\ell\text{ is a descendant leaf of }u\}\). Each summand is at least one. A vertex with two children has at least two descendant leaves; if there is no such vertex then the tree is a rooted path. This proves the exact lower bound and its equality cases.

There are \(n-L\) internal vertices. Each root-to-leaf path uses only internal vertices until its final vertex, so every leaf has depth at most \(n-L\). Summing depth plus one over all leaves gives \(c(T)\le L(n-L+1)\). Equality requires every root-to-leaf path to use every internal vertex. They must therefore all follow one chain of internal vertices and branch only at its last vertex; conversely each such broom attains the bound. For each feasible pair \((n,L)\), \(n\ge2\), the broom with \(n-L\) internal vertices and \(L\) leaves exists. Completing the square in \(L\) gives the maximum \(\lfloor(n+1)^2/4\rfloor\), with equality at the integer or integers nearest to \((n+1)/2\) within the feasible range. For \(n=1\) the sole proper meet-irreducible is the empty set, so \(c(T)=1\). \(\square\)

## Verification

The standalone Python checker `verify.py` enumerates labelled trees on up to seven vertices by Prüfer codes (rooting at vertex zero), builds the closed sets directly from the implications, computes the meet-irreducibles by their covers, and compares with the path description and sharp inequalities. The recorded run returned `VERIFY_OK tree_instances=18249 subset_tests=2238526 maximizers=66`. These finite checks do not replace the general proof. A traversal and a leaf-depth histogram yield the coefficients in \(O(n)\) operations. Explicit enumeration of all characteristic vectors takes \(O(nc(T))\) time and \(O(n)\) working space, excluding output.

## Relationship to prior work

Babin [1, Lemma 2.3] gives the general maximal-omitter characterization. Defrain–Ohana–Vilmin [2, full arXiv version, Lemma 5.1] express an attached irreducible using a minimal transversal of the premises concluding the omitted vertex and attached irreducibles for elements of that transversal. Here there is a single premise for a nonleaf, so its minimal transversals are singleton children; the candidates specialize to the omitted-path recursion. Nourine–Vilmin [3, Theorem 5] give an acyclic-split recurrence. Splitting off the deepest leaves gives a Boolean factor and a smaller tree. On lifting a path complement from that smaller tree, an omitted path that ends at a newly exposed leaf must extend into exactly one removed child in a maximal extension; other paths are unchanged, and the Boolean factor supplies singleton removed leaves. This also yields the path description by induction and hence the deficit polynomial by counting path lengths.

The extremal count concerns fixed total vertex number with unary internal vertices allowed. Since \(c(T)=L+\sum_\ell\operatorname{depth}(\ell)\), it is related to the Sackin index (total external path length). Fischer [4, §4.1, Theorems 4–5 and Remark 6] optimizes that index at fixed leaf number without nonroot unary vertices; those hypotheses and extremizers are different. The bounds here optimize the size of the characteristic representation over the tree Horn family with a fixed total size (or fixed total size and leaf count), not the complexity of general Horn model enumeration.

## Limitations

The theorem requires an actual rooted tree and one conjunctive premise per internal vertex. Extra implications, shared children, or separate implications from each child can invalidate the path description. No bound of this form is asserted for arbitrary acyclic Horn bases, and no claim of exhaustive historical priority is made.

## References

1. M. Babin, *Completeness of Canonical Closure Representations Is coNP-Complete*, arXiv:2607.18534, https://arxiv.org/abs/2607.18534.
2. O. Defrain, A. Ohana, S. Vilmin, *Enumerating the Irreducible Closed Sets of an Acyclic Implicational Base of Bounded Degree*, ISAAC 2025, DOI 10.4230/LIPIcs.ISAAC.2025.24; full preprint https://arxiv.org/abs/2506.24052.
3. L. Nourine and S. Vilmin, *Hierarchical decompositions of implicational bases for the enumeration of meet-irreducible elements*, Theoretical Computer Science 969 (2023), 114030; https://arxiv.org/abs/2202.05536.
4. M. Fischer, *Extremal Values of the Sackin Tree Balance Index*, https://doi.org/10.1007/s00026-021-00539-2.
