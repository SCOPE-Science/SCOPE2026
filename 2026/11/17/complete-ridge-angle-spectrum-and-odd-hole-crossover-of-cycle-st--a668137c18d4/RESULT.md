# Complete ridge-angle spectrum and odd-hole crossover of cycle stable-set polytopes

## Finding
Let \(n=2m+1\ge5\) be odd and let \(P_n\subset\mathbb R^n\) be the standard Euclidean stable-set polytope of the cycle \(C_n\). Every ridge is the intersection of exactly two facets. Its **entire interior dihedral-angle multiset**, counted once per ridge, is:

| Interior angle | Number of ridges for \(n=5\) | Number for odd \(n\ge7\) |
| --- | ---: | ---: |
| \(\pi/2\) | \(25\) | \(2n(n-2)\) |
| \(2\pi/3\) | \(n\) | \(n\) |
| \(\pi-\arccos\sqrt{2/n}\) | \(n\) | \(n\) |

Consequently \(P_5\) has \(35\) ridges and, for odd \(n\ge7\), \(P_n\) has exactly \(2n(n-1)\) ridges. No ridge has an acute interior dihedral angle. The largest angle is the odd-hole angle \(\pi-\arccos\sqrt{2/n}\) for \(n=5,7\), but the edge–edge angle \(2\pi/3\) for every odd \(n\ge9\). These are two distinct obtuse angle levels at every allowable order.

For a uniformly selected ridge of \(P_n\) at odd \(n\ge7\), the two obtuse levels each occur with probability \(1/[2(n-1)]\), and \(\Pr(\Theta_n=\pi/2)=(n-2)/(n-1)\). Conditional on an obtuse ridge, \(\Theta_n\) converges in distribution, through odd orders, to \(\tfrac12\delta_{\pi/2}+\tfrac12\delta_{2\pi/3}\). In particular,
\[
\mathbb E[\Theta_n-\pi/2]=\frac{\pi/6+\arcsin\sqrt{2/n}}{2(n-1)}
=\frac{\pi}{12n}+\frac{1}{\sqrt2\,n^{3/2}}+O(n^{-2}).
\]
The conditional limiting atom at \(\pi/2\) comes from angles that remain strictly obtuse at every finite order.

## Assumptions and scope
Coordinates are the orthonormal indicator-vector coordinates of \(\mathbb R^n\), not a barycentric, normalized, or polar realization. A stable set contains no adjacent cycle vertices, and \(P_n=\operatorname{conv}\{\mathbf1_S:S\text{ stable in }C_n\}\). Indices are cyclic modulo \(n\). Ridges have dimension \(n-2\). The **interior** angle at two adjacent facets with outward normals \(u,v\) is \(\pi-\arccos(\langle u,v\rangle/(\|u\|_2\|v\|_2))\). The theorem concerns exactly odd integers \(n\ge5\); no assertion for the triangle is included.

## Proof
**1. Exact facet representation.** For odd \(n=2m+1\ge5\), the irredundant inequalities for \(P_n\) are
\[
 Z_i:\ -x_i\le0,\qquad E_i:\ x_i+x_{i+1}\le1,\qquad H:\ \sum_{i=0}^{n-1}x_i\le m.
\]
For completeness, the edge relaxation \(Q=\{x\ge0:x_i+x_{i+1}\le1\}\) has only stable-set indicator vertices and one extra vertex \(h=(1/2,\ldots,1/2)\): if a vertex has a zero coordinate, deletion of that coordinate leaves path components and a totally unimodular bipartite edge system, hence an integral vertex. If no coordinate is zero, all active constraints are cycle-edge constraints, and full rank forces all \(n\) such constraints to be tight, whose unique odd-cycle solution is \(h\). At \(h\) those \(n\) edge facets have linearly independent normals. Relaxing exactly \(E_t\) leaves an edge from \(h\) to the maximal stable-set vector \(\mathbf1_{S_t}\), where \(S_t=\{t+2,t+4,\ldots,t+2m\}\pmod n\). As \(\sum h_i=m+1/2\) but \(\sum_{i\in S_t}1=m\), intersecting \(Q\) with \(H\) cuts off only \(h\) and creates no new vertices; it equals \(P_n\).

The \(n\) sets \(S_t\) are all maximal-*cardinality* stable sets. Their incidence matrix is circulant with generating polynomial \(p(z)=z^2+z^4+\cdots+z^{2m}\). At \(z=1\), \(p(1)=m\ne0\); at any other \(n\)th root of unity \(z\), \(p(z)=z^2(1-z^{2m})/(1-z^2)\ne0\). The matrix is invertible, so the \(n\) points \(\mathbf1_{S_t}\) are affinely independent and the facet \(H\) is an \((n-1)\)-simplex. Each \(Z_i\) and \(E_i\) also defines a facet: set only \(x_i=0\), respectively \(x_i+x_{i+1}=1\), with the remaining inequalities strict by choosing sufficiently small positive remaining coordinates.

**2. Complete ridge classification.** All pairs \(Z_i,Z_j\), \(i\ne j\), share a ridge: choose both coordinates zero and all other coordinates small and strictly positive. An \(E_i,Z_j\) pair shares a ridge precisely when \(j\notin\{i,i+1\}\): choose the two edge coordinates near \(1/2\), \(x_j=0\), and all remaining coordinates small positive; for incident pairs, the opposite edge endpoint becomes one and its next neighbor becomes zero, forcing a third independent facet equality.

Two neighboring edge facets \(E_i,E_{i+1}\) always share a ridge: take \(x_i=x_{i+2}=t\), \(x_{i+1}=1-t\) with \(0<t<1\) and every other coordinate sufficiently small. Two disjoint edge facets also share a ridge when \(n\ge7\): assign each selected edge endpoint sum one, strictly slacken the at most one edge linking the two pairs, and keep the other coordinates small; their total coordinate sum is then strictly less than \(m\ge3\). For \(n=5\), two disjoint edges cover four vertices and their two tight inequalities already contribute coordinate sum two, so \(H\) forces the fifth coordinate to vanish; the intersection is contained in a third independent facet and is not a ridge.

Finally, the simplex facet \(H\) meets each \(E_i\) along a ridge. Among the \(n\) maximum stable sets, exactly one has both endpoints of edge \(i,i+1\) absent, while the other \(n-1\) have exactly one present. The corresponding \(n-1\) simplex vertices span a ridge. It meets no \(Z_i\) along a ridge: the \(Z_i\)-face contains only \(m+1\) of the \(n\) vertices of \(H\), of affine dimension at most \(m<n-2\). This exhausts all facet pairs.

**3. Euclidean angles and counts.** The outward normals are \(-e_i\), \(e_i+e_{i+1}\), and \(\mathbf1\) for \(Z_i,E_i,H\), respectively. All genuine coordinate–coordinate, nonincident coordinate–edge, and disjoint edge–edge ridge pairs have orthogonal normals. Neighboring edge normals have cosine \(1/2\), and an edge normal and the odd-hole normal have cosine \(\sqrt{2/n}\). Applying the stated interior-angle convention gives the three claimed values.

For odd \(n\ge7\), right-angle ridges number \(\binom n2+n(n-2)+(\binom n2-n)=2n(n-2)\), since \(n\) of the edge pairs are neighbors. At \(n=5\), the five disjoint edge pairs disappear, leaving \(\binom52+5(5-2)=25\). There are always exactly \(n\) neighboring edge–edge ridges and \(n\) hole–edge ridges. The hole angle exceeds \(2\pi/3\) precisely when \(\sqrt{2/n}>1/2\), equivalently \(n<8\). All distributional and mean statements then follow from these exact multiplicities and \(\arcsin\sqrt{2/n}=\sqrt{2/n}+O(n^{-3/2})\).

## Verification
A standalone standard-library checker, `check_ridge_angles.py`, independently enumerates every cycle stable set at each \(4\le n\le13\), constructs proposed supporting facets, computes each pairwise intersection's affine dimension by exact rational elimination, and checks the outward-normal Gram products. It passed all tested orders, including the odd orders \(n=5,7,9,11,13\) and the exceptional pentagon. The checks do not establish the unrestricted theorem; the preceding proof does.

## Relationship to prior work
The stable-set-polytope framework and its one-skeleton are treated in Aliniaeifard–Benedetti–Bergeron–Li–Saliola (arXiv:1804.00360, first submitted April 2, 2018). The classical odd-cycle inequality and extended formulations are discussed by de Vries–Friedrich–Perscheid (first publicly published October 17, 2019, DOI below). These sources establish or use defining inequalities, not the three-level metric ridge census. Ehrenborg's 2024 face-polynomial paper concerns the **edge relaxation** \(Q\), which coincides with the integral stable-set polytope for even cycles but has an additional fractional vertex for odd cycles. Its enumerative face results must not be mistaken for the present odd-cycle metric spectrum. The established facial framework is credited; the claim here is the exact ridge-adjacency/dihedral spectrum and its sharp crossover, not the novelty of the odd-hole inequalities or the existence of the facet types.

## Limitations
The theorem uses the standard, fixed Euclidean embedding; arbitrary affine images generally change dihedral angles. It treats odd cycles of order at least five, not general graphs or other metrics. Finite checks provide corroboration, not an infinite-dimensional or independent certification. Bibliographic priority is provisional: a source with an equivalent angle or ridge-adjacency description not recovered in the literature comparison could cover part or all of the statement. In particular, the 2024 full text on cycle edge-relaxation face polynomials could not be inspected and is not classified as non-covering on the basis of its abstract alone; its scope differs from the odd-cycle clipped polytope.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first public version 2018-04-02), https://arxiv.org/abs/1804.00360.
2. S. de Vries, U. Friedrich, B. Perscheid, *An extended formulation for the 1-wheel inequalities of the stable set polytope*, *Networks* 75 (2020), 86–94, first published 2019-10-17, https://doi.org/10.1002/net.21906.
3. R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, *European Journal of Combinatorics* 118 (2024), 103906, https://doi.org/10.1016/j.ejc.2023.103906.
