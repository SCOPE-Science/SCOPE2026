# The exact Löwner ellipsoid and sharp cycle-length extremizers of cactus symmetric-edge polytopes

## Finding

Let \(G=(V,E)\) be any connected simple cactus graph on \(n\ge 2\) vertices. Its \(c\ge0\) cycles have lengths \(k_1,\ldots,k_c\ge3\), and \(b\) edges are bridges. Put \(d=n-1=b+\sum_{i=1}^{c}(k_i-1)\), and use the standard Euclidean inner product on the intrinsic zero-sum space \(H=\{x\in\mathbb R^n:\sum_{v\in V}x_v=0\}\). For every edge \(e=uv\), let \(a_e=e_u-e_v\), with arbitrary choice of orientation. Define
\[
P_G=\operatorname{conv}\{\pm a_e:e\in E\},\qquad
w_e=\begin{cases}1,&e\text{ is a bridge},\\ (k_i-1)/k_i,&e\in C_i,\end{cases}
\qquad M_G=\sum_{e\in E}w_ea_ea_e^{\mathsf T}\big|_H.
\]
The **unique** minimum-volume ellipsoid containing \(P_G\) is centered at the origin and is exactly
\[
\mathcal E_G=\{x\in H:x^{\mathsf T}M_G^{-1}x\le1\}.
\]
Every one of the \(2|E|\) vertices \(\pm a_e\) lies on \(\partial\mathcal E_G\). With \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\) and \(F(k)=k((k-1)/k)^{k-1}\), its intrinsic Euclidean volume is
\[
\boxed{\operatorname{Vol}_d(\mathcal E_G)=\kappa_{n-1}\sqrt{n\prod_{i=1}^{c}F(k_i)}.}
\]
The empty product is one: every tree on \(n\) vertices therefore has the same enclosing-ellipsoid volume \(\kappa_{n-1}\sqrt n\), although its optimal ellipsoid need not be a Euclidean isometric copy of another tree's.

For integers \(c\ge1\) and \(n\ge2c+1\), write \(q=\lfloor(n-1)/c\rfloor\) and \(s=n-1-cq\), so \(0\le s<c\). Among all connected simple \(n\)-vertex cactus graphs with exactly \(c\) cycles, the **sharp** range is
\[
\boxed{\kappa_{n-1}\sqrt{n(4/3)^c}\ \le\ \operatorname{Vol}_{n-1}(\mathcal E_G)\ \le\ \kappa_{n-1}\sqrt{nF(q+1)^{c-s}F(q+2)^s}.}
\]
Equality at the lower end holds **if and only if all cycles are triangles** (the remaining edges, if any, are bridges). Equality at the upper end holds **if and only if there are no bridges and the cycle lengths differ by at most one**, namely \(c-s\) cycles of length \(q+1\) and \(s\) cycles of length \(q+2\). These characterize equality by cycle-length data, not by a unique graph isomorphism class. When \(n=2c+1\), the two bounds coincide. For \(c=0\), all graphs are trees and the stated tree formula applies.

## Assumptions and scope

A cactus is a finite connected simple graph in which each edge belongs to at most one simple cycle; different cycles may share vertices. The ambient zero-sum Euclidean realization is essential: using grounded coordinates \(\mathbb R^{n-1}\) **without transporting the metric** does not preserve the stated shape or numerical Euclidean volume. The restriction of \(M_G\) to \(H\) is positive definite because \(G\) is connected. The ellipsoid's center is optimized freely, not fixed in advance. The volume and equality results include trees and all allowed cycle attachments, not only bouquets of cycles.

## Proof

**1. Vertices and determinant.** The incidence roots span \(H\) by connectivity, so \(P_G\) is full dimensional in \(H\). Each \(a_e\) is a genuine vertex: the functional \(x\mapsto a_e\cdot x\) takes value \(2\) at \(a_e\) but at most \(1\) at every other signed edge root of a simple graph. The same holds for \(-a_e\).

Introduce temporarily independent positive edge weights \(z_e\), and set \(M(z)=\sum_e z_ea_ea_e^{\mathsf T}|_H\). The weighted matrix-tree theorem gives \(\det_H M(z)=n\tau_G(z)\), with \(\tau_G(z)\) the weighted spanning-tree polynomial. Every spanning tree of a cactus contains every bridge and deletes exactly one edge from each cycle; conversely every such choice is a spanning tree. Hence
\[
\det_H M(z)=n\prod_{e\text{ bridge}}z_e
\prod_{i=1}^{c}\left(\sum_{e\in C_i}\ \prod_{f\in C_i\setminus\{e\}}z_f\right).
\]
In particular, at \(z=w\) this determinant equals \(n\prod_i F(k_i)\).

**2. Exact contact certificate.** Jacobi's determinant derivative identity on \(H\) reads
\[
\frac{\partial}{\partial z_e}\log\det_H M(z)
=a_e^{\mathsf T}M(z)^{-1}a_e.
\]
For a bridge at weight \(1\), the right side is \(1\). For an edge in a length-\(k\) cycle with every cycle-edge weight \(\alpha=(k-1)/k\), differentiating that cycle's factor \(k\alpha^{k-1}\) gives \((k-1)\alpha^{k-2}\). Their ratio is \((k-1)/(k\alpha)=1\). Therefore
\[
\boxed{a_e^{\mathsf T}M_G^{-1}a_e=1\quad\text{for every edge }e.}
\]
Thus \(\mathcal E_G\) contains \(P_G\), and all signed root vertices touch its boundary. Also
\(\sum_e w_e=b+\sum_i(k_i-1)=d\).

**3. Global minimality and uniqueness, including arbitrary centers.** Let an arbitrary competing ellipsoid containing \(P_G\) be \(\{x\in H:(x-h)^{\mathsf T}S^{-1}(x-h)\le1\}\), where \(S\) is positive definite and \(h\in H\). Applying containment to both \(a_e\) and \(-a_e\) and averaging gives
\[
a_e^{\mathsf T}S^{-1}a_e+h^{\mathsf T}S^{-1}h\le1.
\]
Multiplying by \(w_e\) and summing yields
\[
\operatorname{tr}(S^{-1}M_G)+d\,h^{\mathsf T}S^{-1}h\le d.
\]
The arithmetic-geometric mean inequality on the positive eigenvalues of \(S^{-1/2}M_GS^{-1/2}\) implies
\[
\left(\frac{\det_H M_G}{\det_H S}\right)^{1/d}
\le\frac{\operatorname{tr}(S^{-1}M_G)}d\le1.
\]
Therefore \(\det_H S\ge\det_H M_G\). Since ellipsoid volume equals \(\kappa_d\sqrt{\det_H S}\), \(\mathcal E_G\) is globally minimum-volume. Equality forces \(h=0\) and every eigenvalue in the displayed arithmetic-geometric mean inequality to equal one; hence \(S=M_G\). This proves uniqueness among all enclosing ellipsoids, not only centered ones.

**4. Sharp bounds at fixed cycle count.** For real \(x>2\), let \(g(x)=\log F(x)=(x-1)\log(x-1)-(x-2)\log x\). Then
\[
g'(x)=\log(1-1/x)+2/x>0,
\qquad g''(x)=\frac{2-x}{x^2(x-1)}<0.
\]
Positivity follows, for instance, from \(\log(1-u)>-u/(1-u)\) for \(0<u<1\). Thus \(F\) strictly increases for integer \(k\ge3\), and \(\log F\) is strictly concave. With \(c\) cycles, the allowed lengths satisfy \(k_i\ge3\) and \(\sum_i(k_i-1)\le n-1\); the unused amount is precisely the number of bridges. Strict increase gives the lower equality only at \(k_i=3\) for all \(i\), while at the maximum no bridges can remain. Under the resulting fixed sum \(\sum_i(k_i-1)=n-1\), strict concavity (or an elementary smoothing of two lengths differing by at least two) shows that \(\log\prod_iF(k_i)\) is maximized exactly at balanced lengths, as stated. All feasible length profiles can be realized by attaching the cycles at one common vertex and using the remaining vertices as bridge leaves. This proves both sharp bounds and all equality cases.

## Verification

Run `python3 verify_cactus.py` with Python 3 and no third-party dependencies. The independent finite checker constructs weighted reduced Laplacians, computes their rational determinants and inverses, verifies the determinant formula and every contact identity exactly, and enumerates feasible cycle-length profiles for the extremal bounds. Its reproducible output is `CACTUS_ROOT_ELLIPSOID_EXACT_CHECKS_PASSED 110 1274 75`: 110 constructed cactus graphs, 1,274 exact edge-contact identities, and 75 fixed-order/cycle-count extremal profiles. These finite tests corroborate rather than replace the proof for arbitrary \(n\).

## Relationship to prior work

Ohsugi and Tsuchiya (first public preprint 2020) study cactus graphs through \(h^*\)-polynomials and normalized volumes of the **suspended graph's** symmetric edge polytope; those lattice quantities are not Euclidean enclosing-ellipsoid volumes for \(P_G\). D'Alì, Juhnke-Kubitzke, and Koch (2023) show that the unimodular class of a symmetric edge polytope is controlled by its graphic matroid. This implies a qualitative affine-volume invariance for fixed-dimensional graphical-matroid twins, including cactus graphs with the same cycle lengths, but does not give the explicit optimal Euclidean shape, cycle weights, contact certificate, volume constant, or the sharp fixed-\(n,c\) bounds proved here. Chen, Davis, and Korchevskaia (2021) classify facets by bipartite subgraphs, not enclosing ellipsoids. General minimum-volume ellipsoid/D-optimal design duality appears in Todd's work; the present calculation supplies the specific nontrivial cactus optimization and extremizers. Searches did not identify an earlier theorem with this complete explicit statement; historical priority remains provisional.

## Limitations

This is a theorem about simple connected cactus graphs with the canonical \(e_u-e_v\) Euclidean realization. Graphs with overlapping edge cycles, weighted root configurations, or arbitrary nonlinear transformations are not covered. The invariance of the **optimal volume** under attachment changes does not mean that the corresponding optimal matrices are Euclidean-isometric. The general duality theorem and the matrix-tree theorem are established ingredients; the explicit cactus solution and strict extremal classification are the new deductions. The computation is a finite check only. An equivalent prior result expressed solely through D-optimal design of cactus incidence matrices cannot be excluded by bibliographic search alone.

## References

1. H. Ohsugi and A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621 (first posted August 19, 2020); Combinatorial Theory 1 (2021), Paper 9. https://arxiv.org/abs/2008.08621
2. A. D'Alì, M. Juhnke-Kubitzke, and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933 (July 10, 2023). https://arxiv.org/abs/2307.04933
3. T. Chen, R. Davis, and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (July 26, 2021). https://arxiv.org/abs/2107.12315
4. M. J. Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, ICIAM lecture notes (July 6, 2007), Sections 4–9. https://people.orie.cornell.edu/miketodd/ublndetz.pdf
5. The weighted matrix-tree theorem and Jacobi determinant identity (standard results, used with their usual normalizations).
