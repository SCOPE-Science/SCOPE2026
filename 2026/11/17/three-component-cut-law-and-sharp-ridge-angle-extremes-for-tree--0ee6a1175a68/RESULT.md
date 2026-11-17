# Three-component cut law and sharp ridge-angle extremes for tree graphical zonotopes

## Finding
Let \(T=(V,E)\) be any simple tree with \(n=|V|\ge3\). Its canonical graphical zonotope is \(Z_T=\sum_{\{u,v\}\in E}[e_u,e_v]\), equipped with the Euclidean metric induced from \(\mathbb R^V\) on its affine hull. For two distinct edges \(e,f\), deleting both leaves three connected components: the outer component attached to \(e\), the middle component between the cuts, and the outer component attached to \(f\). Write their positive vertex counts as \(a,b,c\), respectively, with \(a+b+c=n\), and define
\[
q(e,f)=\sqrt{\frac{ac}{(a+b)(b+c)}}.
\]
The pair \(\{e,f\}\) indexes exactly four ridges of \(Z_T\); their **interior dihedral angles**, counted with multiplicity, are
\[
\boxed{\arccos q(e,f),\ \arccos q(e,f),\ \pi-\arccos q(e,f),\ \pi-\arccos q(e,f).}
\]
Consequently the full ridge-angle multiset is given by all unordered pairs of tree edges, has \(2(n-1)(n-2)\) entries, is evenly split between strictly acute and strictly obtuse angles, contains no right angles, and has average \(\pi/2\).

Define \(\alpha(T)\) to be the smallest interior acute ridge angle, put \(\ell=\lfloor(n-1)/2\rfloor\), \(h=\lceil(n-1)/2\rceil\), and \(Q_n=\sqrt{\ell h/((\ell+1)(h+1))}\). Then
\[
\boxed{\arccos Q_n\ \le\ \alpha(T)\ \le\ \arccos\frac1{n-1}.}
\]
The lower equality holds precisely when some vertex of degree two separates the tree, on deletion, into components of sizes \(\ell\) and \(h\). The upper equality holds precisely when \(T\) is a star. Both bounds are attained by trees at every \(n\ge3\); the path attains the lower bound. When \(n=3\), the star and path are the same tree and both bounds equal \(\pi/3\).

## Assumptions and scope
Every edge has unit generator weight. Angles are intrinsic to the \((n-1)\)-dimensional affine span, not angles between arbitrary ambient hyperplanes and not normal-cone solid angles. A ridge means a codimension-two face, including vertices of a two-dimensional zonotope. All multiplicities count actual distinct ridges. No unweighted-graph assumption beyond simplicity, connectedness and acyclicity is hidden; all graphs in the theorem are trees.

## Proof
**1. Independent generators.** Orient the tree edges arbitrarily and put \(b_e=e_u-e_v\) for the corresponding oriented root vectors. A linear relation among the \(b_e\) has zero coefficient at any leaf edge, by taking the leaf coordinate, and successive leaf deletion forces every coefficient to vanish. Thus the centered zonotope \(Z_T-t=\sum_{e\in E}[-b_e/2,b_e/2]\), for a suitable translation \(t\), is an invertible linear image of the \((n-1)\)-cube in \(H=\{x:\sum_vx_v=0\}\).

**2. Exact facet normals.** For an edge \(e\), let \(A_e\) be either component of \(T-e\), and set \(u_e=\mathbf1_{A_e}-(|A_e|/n)\mathbf1\in H\). Its inner product with the root \(b_f\) is zero for every \(f\ne e\), since no such edge crosses the cut; its inner product with \(b_e\) is \(1\) or \(-1\). Accordingly, \(u_e\) is a dual facet normal, up to sign. Fix two edges \(e,f\). Choose \(A_e=A\) and \(A_f=C\) as the disjoint outer components of \(T-\{e,f\}\), of sizes \(a,c\); their complement, the middle component, has size \(b\). Direct inner products give
\[
\langle u_e,u_f\rangle=-\frac{ac}{n},\quad
\|u_e\|^2=\frac{a(b+c)}n,\quad
\|u_f\|^2=\frac{c(a+b)}n.
\]
Hence the two normalized dual normals have signed cosine \(-q(e,f)\). Every pair of cube coordinates has exactly four codimension-two coordinate faces, determined by the two independent endpoint choices. The corresponding outward unit normals have signed cosine \(+q(e,f)\) in two cases and \(-q(e,f)\) in the other two cases. Since the interior dihedral angle is \(\pi-\arccos\) of the outward-normal dot product, the four angles are exactly as stated. Positivity of \(a,b,c\) implies \(0<q(e,f)<1\). The count and acute/obtuse split follow by summing over \(\binom{n-1}{2}\) edge pairs; supplementary pairing gives mean \(\pi/2\).

**3. Sharp bounds and equality.** Write
\[
q(e,f)^2=\frac{a}{n-a}\frac{c}{n-c}.
\]
For fixed \(n\), each factor is strictly increasing in its outer-component size. Because \(a,c\ge1\), this implies \(q(e,f)\ge1/(n-1)\), with equality exactly when \(a=c=1\). In a star every edge pair has this property. In any nonstar tree, a path of length at least three has adjacent initial edges \(e,f\) whose two outer components have sizes \(1\) and at least \(2\); hence some pair has strictly larger \(q\). This proves the star characterization of the upper bound on \(\alpha(T)\).

For the other bound, among positive integer triples of a fixed sum \(n\), if \(b>1\), replacing \((a,b,c)\) with \((a+1,b-1,c)\) strictly increases \(a/(a+b)\) and \(c/(b+c)\). Hence a maximizing triple must have \(b=1\). For \(b=1\), the squared cosine is \(f(a)f(c)\), where \(f(t)=t/(t+1)\) and \(a+c=n-1\). The function \(\log f(t)=\log t-\log(t+1)\) is strictly concave for \(t>0\); therefore this product is uniquely maximized, up to swapping, at \((a,c)=(\ell,h)\). Thus \(q(e,f)\le Q_n\), with equality precisely for a singleton middle component and balanced outer components. The singleton is a degree-two vertex incident to both deleted edges and no others, yielding exactly the stated equality criterion. A path with its middle vertex chosen appropriately attains the lower bound.

## Verification
Run `python check_tree_angles.py` using Python's standard library. The checker enumerates all 1,440 labeled trees on 3 through 6 vertices via Prüfer sequences, examines every pair of edges, computes the three connected components by deletion, checks the exact rational squared cosine against directly constructed dual-normal inner products and generator-annihilation conditions, and checks both equality characterizations. It also examines 60 deterministically sampled trees of orders 7, 8, 12, 20 and 50. The recorded result is `TREE_ZONOTOPE_DIHEDRAL_PASS exact_labelled_trees=1440 star_cases=18 balanced_degree2_cases=795 sampled_large_trees=60`. This is finite corroboration; the proof above treats all tree orders.

## Relationship to prior work
Padrol, Pilaud and Poullot develop the canonical graphical-zonotope realization, its fan and its deformation cone, rather than metric dihedral-angle spectra. The standard dual-normal formula for a parallelotope is classical and is used here, not claimed as new. Existing work on Euclidean surface areas and intrinsic volumes of tree graphical zonotopes examines different invariants and does not by itself supply the three-component per-ridge angle law or its sharp degree-two and star equality classifications. The statement's priority is provisional pending broader bibliographic review.

## Limitations
The formula applies to the canonical unit-root Euclidean embedding of trees. Arbitrary edge reweighting changes the normalized facet normals, and graphs with cycles need not give parallelotopes, so neither generalization is asserted. The paper comparison includes a fully read primary HTML article and targeted database/literature searches; additional unindexed equivalent work could exist. The checker is not an infinite proof.

## References
1. Arnau Padrol, Vincent Pilaud and Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first submitted November 24, 2021, https://arxiv.org/abs/2111.12422 and https://arxiv.org/html/2111.12422v2.
2. Günter M. Ziegler, *Lectures on Polytopes*, Springer, 1995. Standard background on zonotopes, facets and face lattices; no specific tree-angle theorem is attributed to this reference.
