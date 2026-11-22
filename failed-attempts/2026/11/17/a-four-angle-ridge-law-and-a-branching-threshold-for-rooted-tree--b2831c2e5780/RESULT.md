# A four-angle ridge law and a branching threshold for rooted-tree order polytopes

## Finding

Let \(T\) be an arbitrary finite rooted tree with \(n\ge 2\) vertices, unique root \(r\), and parent-before-child order. Write \(d_v\) for the number of children of vertex \(v\), \(L\) for the number of leaves, and \(U\) for the number of leaves whose parent has exactly one child. Put \(W=\sum_{v\in T}\binom{d_v}{2}\).

In the canonical Euclidean order polytope \(\mathcal O(T)\), every two facets meet in a ridge except the \(L-U\) pairs consisting of the upper-coordinate facet at a leaf and the cover facet joining that leaf to its parent when the parent has at least two children. These missing pairs form a matching in the facet-adjacency graph. Consequently the facet-adjacency graph is a complete graph on \(n+L\) vertices with a matching of size \(L-U\) removed, and there are
\[
R(T)=\binom{n+L}{2}-L+U
\]
ridges.

The complete **interior Euclidean ridge-dihedral-angle distribution**, omitting classes of zero multiplicity, is
\[
\begin{array}{c|c}
\text{angle}&\text{multiplicity}\\\hline
\pi/4& d_r+U\\
\pi/3&n-1-d_r\\
\pi/2&\binom{n+L-1}{2}-W\\
2\pi/3&W
\end{array}
\]
Thus the spectrum has at most four angle values and depends only on rooted offspring counts plus the number of unary-parent leaves.

For any sequence of rooted trees with \(n\to\infty\), a uniformly sampled ridge has asymptotically right angle **if and only if** the maximum number of children at any vertex satisfies \(\Delta(T)=o(n)\). Here right-angle convergence means the fraction of ridges with angle \(\pi/2\) tends to one; no probability space over trees is imposed.

## Assumptions and scope

The graph \(T\) is a finite connected acyclic undirected simple graph, with a distinguished root and each edge oriented away from the root. Vertices carry their standard mutually orthogonal unit coordinate vectors in \(\mathbb R^n\); no intrinsic affine renormalization, edge weighting or alternative marking is used. The order polytope is
\[
\mathcal O(T)=\left\{x\in[0,1]^n: x_{p(v)}\le x_v\ \text{for every nonroot }v\right\}.
\]
A ridge is a codimension-two nonempty face; a ridge angle is the interior angle between its two incident facet halfspaces. In dimension two this is the usual polygon interior corner angle. A singleton tree is excluded, because there are no ridges. All sums over vertices and leaf counts refer to the given rooted tree, not to an unlabeled equivalence class.

## Proof

**1. Facets and dimension.** The irredundant outward facet inequalities are
\[
-x_r\le0,\qquad x_\ell\le1\quad(\ell\text{ a leaf}),\qquad x_{p(v)}-x_v\le0\quad(v\ne r).
\]
All other box inequalities follow by transitivity along a rooted path. Every displayed inequality defines a facet: choose all vertex heights strictly increasing from root to leaves within \((0,1)\), then independently set either the root to zero, one chosen leaf to one, or exactly the endpoints of a chosen cover edge equal in \((0,1)\), maintaining all other strict inequalities. An everywhere strict assignment exists, so the dimension is \(n\). There are \(1+L+(n-1)=n+L\) facets.

**2. Exact pairwise intersections.** A pair of distinct cover constraints can be imposed as equality by contracting their two underlying tree edges. Contracting edges in a tree cannot create a directed cycle. Assign all resulting contracted vertices strictly increasing heights in \((0,1)\). Only the selected covers are equalities. For a pair involving the root lower facet, set its contracted root block to zero and all other blocks to heights strictly between zero and one. For two distinct leaf upper facets, set those leaves to one and all other points to heights less than one, respecting their parent order. For a leaf upper facet and a cover not incident to that leaf, impose the selected cover equality and set the leaf to one; no other inequality is forced to equality, since the selected leaf has no descendants and the selected cover's contracted component is disjoint from it. For a leaf upper facet and its *own* cover \(p(\ell)\lessdot\ell\), the equality forces \(x_{p(\ell)}=x_\ell=1\). If \(d_{p(\ell)}=1\), no additional facet is forced to equality, so the intersection is a ridge. If \(d_{p(\ell)}\ge2\), every sibling \(s\) satisfies \(1=x_{p(\ell)}\le x_s\le1\); hence further independent facet equalities occur, so this intersection is not a ridge. Thus precisely \(L-U\) facet pairs are nonadjacent and all other pairs yield codimension two. The excluded pairs are disjoint as pairs of labeled facets, establishing the matching assertion and ridge count.

**3. Euclidean angles.** The outward normals are \(-e_r\), \(e_\ell\), and \((e_{p(v)}-e_v)/\sqrt2\). At a ridge shared by two facets with outward unit normals \(a,b\), the interior dihedral angle is \(\pi-\arccos(a\cdot b)\). A root-lower/incident-cover pair or an upper-leaf/own-cover pair has normal product \(-1/\sqrt2\), and gives \(\pi/4\); the latter is present only for a unary parent. A consecutive pair of cover edges has normal product \(-1/2\), giving \(\pi/3\); these pairs are indexed uniquely by a nonroot vertex \(v\) and one of its \(d_v\) children, whence total \(\sum_{v\ne r}d_v=n-1-d_r\). Two cover edges sharing a parent have normal product \(+1/2\), giving \(2\pi/3\), with \(W=\sum_v\binom{d_v}{2}\) such pairs. Every other ridge pair has orthogonal normals, giving \(\pi/2\). Its multiplicity is the total \(R(T)\) minus the other three counts, simplifying to \(\binom{n+L-1}{2}-W\). This accounts for every ridge exactly once.

**4. Sharp right-angle concentration.** The total number of nonright ridges is
\[
(d_r+U)+(n-1-d_r)+W=n-1+U+W.
\]
Since \(0\le U\le n\) and \(W\le\Delta(T)(n-1)/2\), if \(\Delta(T)=o(n)\) the nonright count is \(o(n^2)\), whereas \(R(T)\ge\binom{n+1}{2}-n=\Theta(n^2)\). Conversely, if \(\Delta(T)/n\not\to0\), then along a subsequence \(\Delta(T)\ge\varepsilon n\); one vertex contributes \(W\ge\binom{\varepsilon n}{2}\), while \(R(T)\le\binom{2n}{2}\). Therefore the nonright fraction cannot tend to zero. This proves the equivalence.

## Verification

The included `VERIFY.py` enumerates all free trees on \(2\le n\le9\), applies every possible root, lists every order-preserving Boolean vertex, and independently determines the affine dimension of every pairwise facet intersection. A pair is counted only when that dimension is exactly \(n-2\). It then computes actual outward-normal cosines and compares the resulting full angle count with the four displayed formulas. The enumeration covers 748 rooted instances (including root placements for isomorphic rooted trees, which are permitted repetitions), with per-size counts \(2,3,8,15,36,77,184,423\). This is a finite check, not the reason the theorem holds for all dimensions; the preceding argument proves the universal assertions. The script requires Python 3, NumPy and NetworkX.

## Relationship to prior work

Stanley's foundational facet description and connected-partition description of order-polytope faces are already known. Ahmad, Fourier and Joswig (arXiv:2309.01626, first public 2023-09-04), especially Theorem 2.1 and preliminary facets discussion, explicitly restate the general partition/face theorem; it provides strong *combinatorial* prior coverage and can be specialized to obtain the adjacency condition, so adjacency by itself is **not** asserted to be novel. Their principal theorems concern monotone face vectors of maximal ranked posets, not the Euclidean metric-angle distribution of arbitrary rooted trees. Garver, Grosser, Matherne and Morales (arXiv:2001.08822, first public 2020-01-23) study rooted-tree and mobile posets through linear-extension enumeration and hook products, not Euclidean ridge angles. Fang, Fourier, Litza and Pegel (arXiv:1712.01037, first public 2017-12-04) investigate marked-poset interpolation and combinatorial types, with publicly accessible abstract; full-text metric overlap cannot be excluded solely from the abstract.

The proposed contribution is the **complete explicit Euclidean ridge-angle multiplicities together with the exact maximum-branching/right-angle concentration criterion**. Neither a general face-partition theorem nor face-vector data alone specifies Euclidean angles without further use of the canonical normal realization. These results follow from the stated independent local-normal and facet-adjacency analysis. Literature priority remains provisional pending broader human review.

## Limitations

The scope is unweighted, rooted-tree order polytopes in the standard Euclidean metric; it does not extend automatically to arbitrary posets, general graphical root polytopes, arbitrary diagonal scalings, or other affine realizations. Results apply to the multiset of ridge angles, not ridge volumes or the complete face lattice. The combinatorial adjacency part follows from known general poset face theory; only the consolidated metric spectrum and sharp angular concentration law are proposed as new. Finite enumerations cannot establish infinite-dimensional correctness, and a mathematically equivalent result outside the inspected literature remains possible. No independent external mathematical audit has been carried out.

## References

1. R. P. Stanley, “Two Poset Polytopes,” *Discrete & Computational Geometry* 1 (1986), 9–23; foundational facets and face structure.
2. I. Ahmad, G. Fourier and M. Joswig, “Order and chain polytopes of maximal ranked posets,” arXiv:2309.01626 (initial posting 2023-09-04); especially §2, Theorem 2.1 and Proposition 2.3.
3. A. Garver, S. Grosser, J. P. Matherne and A. H. Morales, “Counting linear extensions of posets with determinants of hook lengths,” arXiv:2001.08822 (initial posting 2020-01-23); Introduction §1.1 and discussion of rooted-tree posets.
4. X. Fang, G. Fourier, J.-P. Litza and C. Pegel, “A Continuous Family of Marked Poset Polytopes,” arXiv:1712.01037 (initial posting 2017-12-04).
