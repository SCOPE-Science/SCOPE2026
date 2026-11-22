# Path-complement characteristic models of conjunctive tree Horn closures

## Finding

Let \(T=(V,E)\) be any finite rooted tree with \(n=|V|\ge1\). For each nonleaf vertex \(v\), introduce **one** definite Horn implication with the entire set \(\operatorname{ch}(v)\) of its immediate children as its premise and \(v\) as its conclusion:
\[
\Sigma_T=\{\operatorname{ch}(v)\to v:v\text{ is not a leaf}\}.
\]
Thus this is a conjunctive rule, not a separate implication from each child. Let \(\mathcal C_T\) be the family of \(\Sigma_T\)-closed sets, and let \(\operatorname{MI}(T)\) be the proper meet-irreducible members of \(\mathcal C_T\), equivalently its Horn characteristic models. For a vertex \(u\) and a leaf \(\ell\) below it, let \([u,\ell]\) be the vertex set of their unique directed descendant path.

**Theorem.** For every such tree,
\[
\operatorname{MI}(T)=\bigl\{V\setminus[u,\ell]:\ell\text{ a leaf},\ u\text{ an ancestor of }\ell\text{ (including itself)}\bigr\},
\]
with no repetitions. In particular, the complete deficit-size polynomial (deficit = number of omitted vertices) is
\[
Q_T(z)=\sum_{M\in\operatorname{MI}(T)}z^{n-|M|}
=\sum_{\ell\text{ leaf}}\sum_{j=1}^{\operatorname{depth}(\ell)+1}z^j.
\]
Therefore its coefficient \(a_j=[z^j]Q_T(z)\) equals the number of leaves of depth at least \(j-1\). The coefficient sequence is nonincreasing, and the exact number of leaves of depth \(d\) is \(a_{d+1}-a_{d+2}\), with missing coefficients taken as zero.

Writing \(c(T)=|\operatorname{MI}(T)|\), one has the sharp bounds
\[
n\le c(T)=\sum_{\ell\text{ leaf}}(\operatorname{depth}(\ell)+1)
\le \left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\]
For \(n\ge2\), equality in the lower bound holds exactly for rooted paths. Equality in the upper bound holds exactly for rooted **brooms** whose internal vertices form one chain and whose leaves are all attached to its deepest vertex, with the number of leaves maximizing \(L(n-L+1)\) over integers \(1\le L\le n-1\) (namely either nearest integer to \((n+1)/2\) allowed by that range). The one-vertex tree meets both bounds.

## Assumptions and scope

The ground set is the actual set of tree vertices; all vertices are distinct and the root is distinguished. No additional Horn rules or nullary implications are allowed. For a leaf there is no rule with that vertex as conclusion. The rule for each nonleaf has exactly one conclusion and may have a premise of arbitrary positive size. The dependency digraph is acyclic; each vertex belongs to at most one premise (that of its parent) and occurs as a conclusion in at most one rule, so occurrence-degree is at most two. A proper meet-irreducible of a finite closure system is a closed set other than the whole ground set that cannot be expressed as the intersection of two strictly larger closed sets.

The theorem concerns **all** finite rooted trees and all nonnegative deficit sizes, not just trees of bounded degree or selected depths. It does not concern arbitrary acyclic Horn bases, even those with bounded occurrence-degree.

## Proof

**1. Closure as a condition on omissions.** For \(X\subseteq V\), put \(O=V\setminus X\). The set \(X\) is closed if and only if every omitted nonleaf vertex has at least one omitted child. Indeed, the rule \(\operatorname{ch}(v)\to v\) fails precisely when \(v\notin X\) while all children of \(v\) lie in \(X\). This characterization uses the *entire* child set as the premise.

**2. Every omitted vertex starts an omitted path.** If a closed \(X\) omits a vertex \(u\), then \(u\in O\). Follow an omitted child whenever the current omitted vertex is not a leaf; finiteness produces a leaf \(\ell\) with \([u,\ell]\subseteq O\). Thus \(X\subseteq V\setminus[u,\ell]\). Conversely, for every ancestor-to-leaf path \([u,\ell]\), the set \(V\setminus[u,\ell]\) is closed: every omitted internal vertex has the next path vertex as an omitted child. Moreover, among closed sets still omitting \(u\), no set strictly contains \(V\setminus[u,\ell]\), since such a set would omit a proper subset of this single path while still omitting \(u\), and could no longer reach any missing leaf from \(u\). Hence these complements are exactly the inclusion-maximal closed sets omitting \(u\). Two distinct downward paths from \(u\) cannot be nested because each ends at a leaf.

**3. Meet-irreducibles are maximal omitters.** In any finite closure system, each inclusion-maximal closed set omitting a fixed element is meet-irreducible: if it were an intersection of two strictly larger closed sets, both would contain the omitted element. Conversely, a proper meet-irreducible has exactly one cover in the finite inclusion lattice. If two covers existed, their intersection would equal the element, contradicting meet-irreducibility. Choose an element \(u\) added by the unique cover; every strictly larger closed set must contain the cover and thus must contain \(u\). It is therefore maximal closed among sets omitting \(u\). Applying Step 2 gives precisely the listed path complements. Distinct ancestor-to-leaf paths have distinct vertex sets (their topmost and bottommost vertices identify them), so the representation has no duplicates.

**4. Complete size polynomial and inversion.** Fix a leaf \(\ell\) of depth \(d\). It has exactly one ancestor at each distance \(0,1,\ldots,d\); the corresponding omitted paths have \(1,2,\ldots,d+1\) vertices. Summing over leaves proves the stated polynomial. Thus \(a_j\) counts leaves with depth at least \(j-1\), implying monotonicity and the difference formula. Equivalently, exchanging the order of summation shows \(c(T)\) is the sum over vertices of the number of descendant leaves.

**5. Sharp extremal counts.** Every vertex has at least one descendant leaf; hence the last expression is at least \(n\). If an internal vertex has two child subtrees containing leaves, it contributes at least two, making the inequality strict. Thus equality requires exactly one descendant leaf at every vertex, which is precisely the rooted-path case.

Let \(L\) be the number of leaves and \(K=n-L\) the number of internal vertices. A root-to-leaf path contains at most \(K\) internal vertices, so \(\operatorname{depth}(\ell)+1\le K+1\) for every leaf and
\[
c(T)\le L(K+1)=L(n-L+1)\le\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\]
The last inequality is completion of the square over integer \(L\). Equality in the first inequality requires *every* internal vertex to lie on *every* root-to-leaf path. Hence the internal vertices form a common chain and all leaves attach to its deepest vertex; these and only these trees are brooms (including stars and one-edge trees). Such a broom has \(L\) leaves each at depth \(K\), and therefore attains \(L(K+1)\). Optimizing \(L\) proves attainability and the equality description. The \(n=1\) case is immediate. \(\square\)

## Verification

A stand-alone checker, `verify.py`, enumerates every labelled unrooted tree on \(n\le7\) vertices via Prüfer codes, roots it at vertex zero, constructs its Horn closed sets directly, finds their meet-irreducibles by counting covers in the closed-set lattice, and independently constructs the proposed path complements. It also verifies both sharp inequalities. The actual run returned `VERIFY_OK tree_instances=18249 subset_tests=2238526 maximizers=66`, with 18,249 rooted-labelled instances and 2,238,526 raw candidate subsets. These finite tests check implementation and small cases; the universal result is Steps 1–5, not an inference from the tests.

The spectrum and models can be produced directly in polynomial time: a depth-first traversal computes all leaf depths in \(O(n)\) operations; enumerating the \(c(T)\) path complements as explicit \(n\)-bit characteristic vectors uses \(O(nc(T))\) time and \(O(n)\) working space (excluding output).

## Relationship to prior work

Babin's 2026 closure-representation complexity theorem establishes coNP-completeness of equivalence testing for general acyclic definite-Horn systems with small premises; its general maximal-omitter lemma is used here as standard background, not asserted to be new. Defrain, Ohana and Vilmin (2025) establish incremental-polynomial enumeration of meet-irreducibles for acyclic bases of bounded conclusion-degree, a class containing these tree systems. Those general results do not state the path-complement classification, the entire deficit polynomial and its inversion to leaf-depth counts, or the sharp \(\lfloor(n+1)^2/4\rfloor\) extremum for this concrete family. Nourine and Vilmin (2023) prove a recursive acyclic-split decomposition theorem for general implication bases. Their decomposition tree is a tree *of partitions of a basis*, not the dependency tree used here; their general recurrence can help compute characteristic models, but Sections 3–4 do not state the leaf-depth polynomial or its sharp tree extremum. A specialization of their theorem may nevertheless provide an alternate derivation, and is acknowledged as a historical-scope risk.

Thus the contribution is an exact structural and extremal description in a canonical natural subclass, not a claim that generic Horn model enumeration is newly tractable.

## Limitations

The result relies on the one conjunctive premise per internal vertex and on the dependency graph being a rooted tree. Adding rules, adding shared children (a DAG), or replacing an all-children premise by separate child implications can invalidate the path-complement classification. No explicit formula is claimed for general acyclic convex geometries. The proof has not received independent validation; a prior equivalent specialization of a more general decomposition theorem cannot be ruled out by finite literature searches.

## References

1. M. Babin, *Completeness of Canonical Closure Representations Is coNP-Complete*, preprint first posted 20 July 2026, https://arxiv.org/abs/2607.18534.
2. O. Defrain, A. Ohana, S. Vilmin, *Enumerating the Irreducible Closed Sets of an Acyclic Implicational Base of Bounded Degree*, ISAAC 2025, DOI 10.4230/LIPIcs.ISAAC.2025.24; open HTML https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.24/LIPIcs.ISAAC.2025.24.html.
3. L. Nourine, S. Vilmin, *Hierarchical decompositions of implicational bases for the enumeration of meet-irreducible elements*, Theoretical Computer Science 969 (2023), 114030, open preprint https://arxiv.org/abs/2202.05536.
