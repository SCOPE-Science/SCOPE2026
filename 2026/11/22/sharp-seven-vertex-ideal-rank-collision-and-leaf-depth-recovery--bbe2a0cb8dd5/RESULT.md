# Sharp seven-vertex ideal-rank collision and leaf-depth recovery from graded one-types of rooted trees

## Finding

Let \(T\) be any finite nonempty rooted tree, oriented as a finite strict partial order with the root least and ancestor below descendant. Embed its vertices as individually named parameters in the countable universal homogeneous strict partial order \(\mathbb P\). For each complete nonalgebraic one-point type \(\tau\) over these parameters, let \(L_\tau=\{a\in T:a<x\}\) and \(U_\tau=\{a\in T:x<a\}\). Define

\[
E_T(u,v)=\sum_{\tau\in S_1^{\mathrm{na}}(T)}u^{|L_\tau|}v^{|U_\tau|}.
\]

For every integer \(d\ge0\),

\[
\boxed{[u^d v]E_T(u,v)=\#\{\ell\in\operatorname{Leaf}(T):\operatorname{depth}(\ell)\ge d\}.}
\]

Thus the number of leaves at depth exactly \(d\) is \([u^dv]E_T-[u^{d+1}v]E_T\). In particular the sum of leaf depths (the Sackin index) is \(\sum_{d\ge1}[u^dv]E_T(u,v)\).

The marginal \(I_T(u)=E_T(u,0)\) is the rank polynomial of the distributive lattice of order ideals of \(T\). The first collision of this rank polynomial among nonisomorphic finite rooted trees occurs at **seven vertices**. There is exactly one colliding unordered pair of rooted isomorphism classes through this size. Both have

\[
I_T(u)=1+u+2u^2+3u^3+4u^4+4u^5+3u^6+u^7,
\]

but their respective leaf-depth multisets are \(\{1,2,4\}\) and \(\{2,3,3\}\). Their mixed coefficients \([u^2v]E_T\) are \(2\) and \(3\). No collision occurs through six vertices.

## Assumptions and scope

The ambient structure is the countable Fraïssé limit of all finite strict partial orders; every finite consistent strict-poset one-point extension is realized and any two such extensions have the same complete type exactly when their comparisons to all the named parameters agree. New elements are distinct from all named parameters. The parameter order is a **rooted-tree poset** with an undirected Hasse diagram that is a tree and a unique least element. Every child set is unordered; no plane ordering is assumed. Depth counts edges from the root, which has depth zero. The claim concerns the **graded** type count, not probabilities of sampling vertices of the ambient countable structure.

## Proof

**One-point type classification.** For any finite parameter poset \(P\), a prospective new point \(x\) determines the lower set \(L=\{a\in P:a<x\}\) and upper set \(U=\{a\in P:x<a\}\). Necessarily \(L\) is an order ideal, \(U\) is an order filter, \(L\cap U=\varnothing\), and every element of \(L\) lies strictly below every element of \(U\). Conversely, precisely these four conditions make the stipulated comparisons transitive; declaring all remaining named points incomparable with \(x\) defines a finite strict partial order. Homogeneity and the extension property provide a unique complete nonalgebraic type for each admissible pair. Consequently

\[
E_P(u,v)=\sum_{\substack{L\text{ ideal},\,U\text{ filter}\\L\cap U=\varnothing,\,L<U}}u^{|L|}v^{|U|}.
\]

**Leaf-depth extraction.** To contribute to \([v^1]\), the filter \(U\) must be a singleton \(\{\ell\}\). Such a singleton is an order filter if and only if \(\ell\) is a maximal parameter: in a rooted tree, a leaf. As every vertex of \(L\) must be strictly below \(\ell\), \(L\) is an ideal contained in the strict ancestor chain of \(\ell\). The ideals of a chain of length \(\operatorname{depth}(\ell)\) are exactly its initial segments, so for each \(0\le d\le\operatorname{depth}(\ell)\), this leaf contributes exactly one admissible pair \((L,\{\ell\})\) with \(|L|=d\). Summing over leaves proves the coefficient formula for **all** finite rooted trees, independently of any enumeration. Taking adjacent differences gives exact leaf-depth multiplicities; summing the tails for \(d\ge1\) gives their total depth.

**Ideal-rank marginal and seven-vertex cutoff.** Setting \(v=0\) forces \(U=\varnothing\), leaving arbitrary ideals \(L\), so \(I_T(u)=\sum_{L\text{ ideal}}u^{|L|}\). If the root has child-rooted trees \(T_1,\ldots,T_m\), then every nonempty ideal contains the root and chooses an ideal independently in each child subtree. Therefore

\[
\boxed{I_T(u)=1+u\prod_{j=1}^m I_{T_j}(u).}
\]

The finite cutoff is certified by the supplied `verify.py`, whose canonical rooted-tree generator is complete by induction: every rooted tree has a unique nondecreasing multiset of child rooted trees with total size one less than the parent, and the generator enumerates **every** such multiset once. It enumerates respectively \(1,1,2,4,9,20,48\) rooted isomorphism classes of sizes one through seven. For each class the recurrence gives an exact integer rank polynomial. Exact comparison of all resulting coefficient vectors shows no collisions for sizes at most six, and precisely one unordered pair among 48 seven-vertex classes.

A canonical child-multiset encoding uses `()` for a leaf and a tuple of child encodings otherwise. The two exceptional rooted trees are

```
A = ((), ((), (((),),)))
B = (((),), (((), ()),))
```

Their parent-index arrays, listed in depth-first vertex order with root parent \(-1\), are respectively `[-1,0,0,2,2,4,5]` and `[-1,0,1,0,3,4,4]`. Direct application of the recurrence gives the displayed common rank polynomial. The leaves have depths \(1,2,4\) for \(A\) and \(2,3,3\) for \(B\), whence the already proved extraction identity gives \([u^2v]E_A=2\) and \([u^2v]E_B=3\).

## Verification

Run `python3 verify.py` using Python 3.9 or newer; no external libraries are required. The program regenerates **all** canonical rooted-tree shapes of orders one through seven, computes their ideal-rank polynomials recursively, and separately enumerates every subset pair \((L,U)\) for each shape and tests the downset, upset, disjointness, and comparability conditions. It independently checks the ideal marginals and all leaf-depth coefficients. The completed run reports 85 complete extension-diagram comparisons, the unique seven-vertex collision, and the claimed mixed coefficients. Replayed textual output appears in `verification_output.txt`. The finite exhaustive classification depends on the explicit complete generator and arithmetic code, not merely on a partial sample. The all-size coefficient formula is proved symbolically above rather than inferred from finite tests.

## Relationship to prior work

The order-ideal rank polynomial and its Whitney-number interpretation, along with general algorithms to compute it, are established background: see Wild (arXiv:1208.2180, Sections 1 and 6). The rooted-tree polynomial in Misanantenaina--Wagner (arXiv:1803.09623, Sections 1 and 2) is a **different** polynomial involving maximal antichains and cutsets; its tree-characterization results do not directly identify the graded logical-type coefficients considered here. Previous general finite-poset one-type counting results provide orbit-type context, including exact ungraded counts for tree-cover posets and enumeration of the graded polynomial on small posets. The present claim is limited to the leaf-depth extraction in *all* finite rooted trees and the sharp first failure of reconstruction from the ideal-rank marginal, with a unique small obstruction.

## Limitations

The coefficient identity reconstructs leaf depths, **not** an entire rooted tree from the graded type polynomial. The seven-vertex statement classifies collisions only up to seven vertices; it does not classify every larger collision or assert that the full graded spectrum distinguishes all rooted trees. A finite exhaustive script underpins the minimal-collision classification; its enumeration is complete only through size seven. Historical priority is a residual risk, particularly if a previous tree-invariant comparison has an unrecognized equivalent formulation. Independent mathematical audit has not been performed.

## References

- Marcel Wild, *Output-polynomial enumeration of all fixed-cardinality ideals of a poset, respectively all fixed-cardinality subtrees of a tree*, arXiv:1208.2180 (first posted 2012-08-10), https://arxiv.org/abs/1208.2180 . Especially Sections 1 and 6 (Whitney numbers and rank polynomial of the ideal lattice).
- V. R. Misanantenaina and S. Wagner, *A Tutte-like polynomial for rooted trees and specific posets*, arXiv:1803.09623 (first posted 2018-03-26), https://arxiv.org/abs/1803.09623 . Sections 1--2 (different rooted-tree polynomials and tree-characterization questions).
