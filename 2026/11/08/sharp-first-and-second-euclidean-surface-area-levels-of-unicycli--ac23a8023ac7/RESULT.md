# Sharp first and second Euclidean surface-area levels of unicyclic graphical zonotopes

## Finding

**Theorem (two sharp surface-area levels).** For each integer \(n\geq5\), among all connected simple unicyclic graphs \(G\) with \(n\) vertices, put
\[
Z_G=\sum_{\{u,v\}\in E(G)}\left[-\frac{e_u-e_v}{2},\frac{e_u-e_v}{2}\right]
\subset \left\{x\in\mathbb R^n:\sum_i x_i=0\right\},
\qquad A(G)=\mathcal H^{n-2}(\partial Z_G).
\]
The unique surface-area minimizer up to graph isomorphism is the triangle with all \(n-3\) extra vertices attached as leaves to one triangle vertex. The unique second minimizer, meaning the next *distinct* area value, is the triangle with \(n-4\) leaves on one triangle vertex and one leaf on a second triangle vertex. Their exact respective areas are
\[
A_1(n)=(6n-14)\sqrt{n-1}+2\sqrt{2(n-2)},
\qquad A_2(n)=(6n-16)\sqrt{n-1}+2\sqrt{2(n-2)}+2\sqrt{3(n-3)}.
\]
Thus every unicyclic \(G\) except the first graph has \(A(G)\ge A_2(n)\), with equality precisely for the specified second graph, and the sharp positive gap is
\[
\boxed{A_2(n)-A_1(n)=2\left(\sqrt{3(n-3)}-\sqrt{n-1}\right)>0.}
\]
For completeness, in order \(n=4\) the only two types are a triangle with one attached leaf, of area \(10\sqrt3+4\), and the four-cycle, of area \(8\sqrt3+8\), the latter having larger area by \(4-2\sqrt3\).

**All-unicyclic surface formula.** Let \(C\) be the unique cycle of \(G\), of length \(\ell\), and let \(B\) be its set of bridge edges. For a bridge \(e\), let \(s_e\) be the number of vertices in the component detached from \(C\) by removing \(e\). For two distinct cycle edges \(e,f\), let \(s_{ef}\) be either resulting component size after their deletion. Then, for every \(n\ge3\),
\[
\boxed{A(G)=2\ell\sum_{e\in B}\sqrt{s_e(n-s_e)}
+2\sum_{\{e,f\}\subset E(C)}\sqrt{s_{ef}(n-s_{ef})}.}
\]
This is independent of all choices of which component to count.

## Assumptions and scope

Graphs are finite, connected, loopless, simple, and have exactly one cycle. The geometric realization and the Euclidean scalar product are the *canonical coordinate ones*, not arbitrary affine images. The intrinsic dimension of \(Z_G\) is \(n-1\), and \(A(G)\) is its \((n-2)\)-dimensional boundary measure, counting each geometric facet once. A graph isomorphism acts by an orthogonal coordinate permutation, so area is isomorphism-invariant. All stated inequalities concern integers \(n\ge5\), except the separately stated \(n=4\) comparison.

## Proof

**1. The facet-to-cut identity.** Let \(H\) be any connected graph on \(k\) labeled vertices and \(Z_H\) its graphical zonotope. Its intrinsic \((k-1)\)-volume is \(\sqrt{k}\,\tau(H)\), where \(\tau(H)\) is its number of spanning trees (and for \(k=1\), the zero-dimensional volume and \(\tau(H)\) are both one). Indeed, the standard zonotope volume decomposition sums the absolute determinants of all \((k-1)\)-element generator sets. A nonzero summand occurs precisely at a spanning tree. Each tree incidence matrix has squared Gram determinant \(k\), by the matrix-tree identity applied to an incidence basis; therefore each nonzero summand is \(\sqrt k\).

A facet normal \(a\) of \(Z_G\) must satisfy \(\langle a,e_u-e_v\rangle=0\) on precisely those edge generators spanning a codimension-one subspace. Thus the zero-slope subgraph has exactly two connected components, \(G[S]\) and \(G[V\setminus S]\), for a nonempty proper set \(S\). Equivalently, the crossing edge set is an inclusion-minimal bond. Conversely every bond supplies two opposite supporting facets. The facet is, up to translation, the orthogonal Minkowski product of \(Z_{G[S]}\) and \(Z_{G[V\setminus S]}\) in disjoint coordinate subspaces. By the previous volume identity, the area of each such facet is
\[
\sqrt{|S|(n-|S|)}\,\tau(G[S])\tau(G[V\setminus S]).
\]
Summing the two opposite facets over unordered connected bipartitions gives the exact general identity
\[
A(G)=2\!\sum_{\substack{\{S,V\setminus S\}\\G[S],G[V\setminus S]\ \mathrm{connected}}}
\sqrt{|S|(n-|S|)}\,\tau(G[S])\tau(G[V\setminus S]).
\tag{1}
\]
There is no multiplicity from different bond edges: each unordered bipartition contributes one antipodal facet pair.

**2. Specialization to one cycle.** In a connected unicyclic graph every minimal edge cut is either one bridge or two distinct edges on the unique cycle. After deletion of a bridge, exactly one side retains the cycle (with spanning-tree count \(\ell\)), while the other side is a tree (count one). Deletion of any two cycle edges yields two trees (counts one). Substituting these cases into (1) proves the boxed all-unicyclic formula and its normalization.

**3. Cycles of length at least four are never among the first two.** Put \(F_j=\sqrt{j(n-j)}\), so \(F_j\ge F_1=\sqrt{n-1}\) for every \(1\le j<n\). For cycle length \(\ell\ge4\), there are exactly \(n-\ell\) bridge terms with coefficient \(2\ell\) and \(\binom\ell2\) two-cycle-edge terms with coefficient two. Therefore
\[
A(G)\ge \ell(2n-\ell-1)F_1\ge 4(2n-5)F_1.
\tag{2}
\]
The second inequality follows because \(\ell\mapsto \ell(2n-\ell-1)\) is concave and its values at \(\ell=4\) and \(\ell=n\) satisfy \(n(n-1)-4(2n-5)=(n-4)(n-5)\ge0\). Subtracting the proposed second value from the right side of (2) gives
\[
(2n-4)F_1-2(F_2+F_3)>0
\]
for every \(n\ge5\): use \(F_1\ge2\), \(F_j\le n/2\), and \(2(2n-4)>2n\). Thus any graph among the first two must have a triangle cycle.

**4. Triangle cases and non-leaf penalties.** Suppose \(C\) is a triangle, and let \(w_1,w_2,w_3\ge1\) be the numbers of vertices in the three trees rooted at its vertices, including the roots, so \(w_1+w_2+w_3=n\). Deleting two triangle edges isolates one rooted tree, and the cycle contribution is exactly \(2\sum_{i=1}^3F_{w_i}\). The bridge contribution is \(6\sum_{e\in B}F_{s_e}\). Since \(j\mapsto F_j=\sqrt{j(n-j)}\) is strictly concave on \((0,n)\), the most majorizing triple \((n-2,1,1)\) uniquely minimizes the cycle sum; hence
\[
\sum_iF_{w_i}\ge F_{n-2}+2F_1=F_2+2F_1.
\tag{3}
\]
There are \(n-3\) bridges and every one contributes at least \(F_1\), with equality only when its detached component is one leaf. In particular, if any bridge is not incident to a detached leaf, its detached component has \(2\le s_e\le n-3\), and its contribution exceeds the baseline \(F_1\) by at least \(F_2-F_1\). Such a graph has
\[
A(G)\ge A_1(n)+6(F_2-F_1)>A_1(n)+2(F_3-F_1)=A_2(n).
\tag{4}
\]
The strict middle inequality follows from strict concavity, \(F_3-F_1<2(F_2-F_1)\) for \(n\ge5\). Consequently **both** first area levels are attained among graphs whose noncycle vertices are all individual leaves.

**5. Sharp second level and equality classification.** For an all-leaf triangle graph write \(w_i=1+a_i\), with integers \(a_i\ge0\) and \(\sum a_i=n-3\). The bridge contribution is constant: \(6(n-3)F_1\). Among the triples \((w_1,w_2,w_3)\), up to permutation, \((n-2,1,1)\) is uniquely maximal in majorization order. Among *all other* triples, \((n-3,2,1)\) majorizes every one: the largest entry of a distinct triple is at most \(n-3\), and the sum of its largest two entries is at most \(n-1\). Strict concavity of \(F\) proves that the unique first and second cycle-sum levels occur at those two triples. Substituting into the surface formula yields precisely \(A_1(n)\) and \(A_2(n)\) as stated, with equality only for the two asserted graph types. Their gap is positive because \(3(n-3)>n-1\) for \(n>4\).

For \(n=4\) there are exactly the two graph types listed: a triangle with one leaf and a four-cycle. Evaluating the all-unicyclic formula gives the stated values and difference. This completes the proof.

## Verification

The bundled standalone checker `check_unicyclic_surface.py` uses exact nonisomorphic graph generation and two *independent finite numerical area calculations*: (a) enumeration of connected graph bipartitions with spanning-tree factors from (1), (b) the special bridge/paired-cycle-edge formula. For \(4\le n\le9\), it compares every nonisomorphic unicyclic graph (counts \(2,5,13,33,89,240\)), sorts the actual areas, and checks the two values and unique graph levels. For \(4\le n\le6\), it additionally constructs the zonotope in an orthonormal basis of the intrinsic hyperplane and checks the area of its convex hull for the first four graphs by increasing area. This is finite corroboration only; the proof above covers every permitted \(n\).

Run `python check_unicyclic_surface.py` with Python 3 and the packages `networkx`, `numpy`, and `scipy` installed. A successful run prints `UNICYCLIC_GRAPHICAL_ZONOTOPE_FIRST_TWO_SURFACE_LEVELS_PASSED` followed by the enumeration data.

## Relationship to prior work

Padrol–Pilaud–Poullot develop the face and normal structure of graphical zonotopes [1], including the connected-bipartition description of facets. Joós–Lángi establish general Euclidean intrinsic-volume decompositions and investigate isoperimetric problems for abstract zonotopes [2]. These two sources supply a framework for step 1; neither contains the graph-specific sharp first/second unicyclic surface-area classification or the strict discrete second-level gap proved in steps 3–5. A general bound on abstract \((n-1)\)-dimensional zonotopes with \(n\) generators does not order the unicyclic incidence-vector realizations. A related result for **tree** graphical zonotopes concerns an edge-cut sum with different facet multiplicities and does not imply the present unicyclic ordering. Equivalences under other names for bond energies or edge-cut Euclidean norms remain a priority risk.

A motivating distinction is that every unicyclic graph on \(n\) vertices has \(n\) edge generators and hence the same first intrinsic volume/mean-width scaling, whereas the canonical surface area varies. Within the triangle-cycle subclass even intrinsic \((n-1)\)-volume is fixed at \(3\sqrt n\) because there are exactly three spanning trees; the sharp surface-area hierarchy therefore compares bodies with the same volume and generator count.

## Limitations

The theorem classifies only the two lowest distinct surface-area values, not the entire surface-area spectrum or the maximizer. It requires connected simple unicyclic graphs with canonical unit graph-root generators and the usual Euclidean metric; weighted edges, multiple cycles, or nonorthogonal affine changes are not covered. Historical priority is provisional, and independent mathematical validation has not been performed. Numerical enumeration of dimensions at most nine is not an infinite-dimensional proof.

## References

[1] A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, publicly posted 2021-11-24. https://arxiv.org/abs/2111.12422

[2] A. Joós, Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204, publicly posted 2022-06-07. https://arxiv.org/abs/2206.03204
