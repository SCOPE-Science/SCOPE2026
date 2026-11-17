# Balanced-sign facets and the complete incenter locus of \(K_{2,q}\) symmetric-edge polytopes

## Finding
Let \(q\ge3\) be an integer, let \(G=K_{2,q}\), and let \(P_q\) be its standard symmetric-edge polytope in the intrinsic Euclidean hyperplane \(H=\{x\in\mathbb R^{q+2}:\sum_i x_i=0\}\). The complete support-facet distance spectrum, its largest inscribed Euclidean-ball radius, and **every** maximizing center are determined explicitly.

Set \(h=(e_1-e_2)/2\), \(w_j=(e_1+e_2)/2-e_{j+2}\) for \(1\le j\le q\), and \(W=\sum_{j=1}^{q}w_j\). Put
\[
Q_q=q-\frac{\delta_q^2}{q+2},\qquad r_q=\frac1{\sqrt{Q_q}},\qquad T_q=1-\sqrt2\,r_q,
\]
where \(\delta_q=0\) for even \(q\) and \(\delta_q=1\) for odd \(q\). Then the Euclidean inradius is exactly \(r_q\). Its complete set of centers is
\[
\mathcal Z_q=\begin{cases}
\{t h:|t|\le T_q\},&q\text{ odd},\\[2mm]
\{t h+sW:|t|\le T_q,\ |s|\le U_q\},&q\text{ even},
\end{cases}
\qquad
U_q=\frac{1-\sqrt{1-4/[q(q+2)]}}2\quad(q\text{ even}).
\]
In particular, the incenter locus has affine dimension \(1\) for odd \(q\) and \(2\) for even \(q\). Both parameters have positive extent for the stated range.

The polytope has exactly \(2+2^q\) facets: two segment-end facets at distance \(1/\sqrt2\) from the origin, and one cross-polytope facet for each sign vector \(\varepsilon\in\{-1,1\}^q\). Writing \(S=\sum_j\varepsilon_j\), the latter facet is at distance
\[
d_S=\left(q-\frac{S^2}{q+2}\right)^{-1/2}.
\]
For each \(S=-q,-q+2,\ldots,q\), precisely \(\binom q{(q+S)/2}\) such facets occur. At the origin-centered maximal ball, exactly \(\binom q{q/2}\) facets are tangent for even \(q\), and exactly \(2\binom q{(q-1)/2}\) for odd \(q\); no segment-end facet is tangent. For an even \(q\), at \(s=U_q\) precisely the additional sign facets with \(S=2\) become tangent, and at \(s=-U_q\) those with \(S=-2\) do; either endpoint \(|t|=T_q\) contributes the corresponding segment-end facet. For an odd \(q\), the interior of the incenter segment has only the indicated balanced-sign tangencies, while each endpoint adds one segment-end facet.

## Assumptions and scope
All radii and distances use the Euclidean norm inherited from \(\mathbb R^{q+2}\) on the affine span \(H\); they are not lattice-normalized, graph-combinatorial, or volumes of ellipsoids. The polytope is
\[
P_q=\operatorname{conv}\{\pm(e_i-e_j):i\in\{1,2\},\ j\in\{3,\ldots,q+2\}\}.
\]
Here an incenter means any center of a closed Euclidean ball of the maximum possible radius contained in \(P_q\). All assertions hold for every integer \(q\ge3\), with no finite cutoff. The family is one of the three complete-multipartite exceptional decomposable symmetric-edge families; no statement is made about general \(K_{p,q}\) with \(p\ge3\).

## Proof
**Step 1: Orthogonal product and facets.** Every vertex is of the form \(\pm h\pm w_j\) with the two signs independent. Since \(\langle h,w_j\rangle=0\), taking convex hulls gives an exact orthogonal Cartesian product
\[
P_q=[-h,h]+C_q,\qquad C_q=\operatorname{conv}\{\pm w_1,\ldots,\pm w_q\}.
\]
The \(q\) vectors \(w_j\) form a basis of the \(q\)-dimensional subspace orthogonal to \(h\) within \(H\), because their Gram matrix is
\[
\Gamma=(\langle w_i,w_j\rangle)_{i,j}=I_q+\tfrac12\mathbf1\mathbf1^{\mathsf T}.
\]
Thus \(C_q\) is an invertible linear image of the \(q\)-cross-polytope, with facets indexed by \(\varepsilon\in\{-1,1\}^q\). Let \(F_\varepsilon\) be its unique intrinsic normal satisfying \(\langle F_\varepsilon,w_j\rangle=\varepsilon_j\). Its facet inequality is \(\langle F_\varepsilon,y\rangle\le1\). The elementary rank-one inverse identity
\[
\Gamma^{-1}=I_q-\frac{\mathbf1\mathbf1^{\mathsf T}}{q+2}
\]
implies \(\|F_\varepsilon\|^2=q-S^2/(q+2)\). The product also has precisely two segment-end facets, of origin distance \(\|h\|=1/\sqrt2\). This proves the full facet spectrum and its multiplicities.

**Step 2: Sharp radius.** A centrally symmetric convex body has an origin-centered maximum-radius ball: if both the ball centered at \(c\) and its reflection are contained, convexity contains their Minkowski midpoint, the origin-centered ball of the same radius. Therefore the inradius is the least supporting-facet distance from the origin. Since \(S\) runs through integers of the parity of \(q\), \(\|F_\varepsilon\|^2\) is maximal exactly when \(|S|=\delta_q\), with value \(Q_q\). For every \(q\ge3\), \(Q_q>2\), so the cross-polytope bound \(1/\sqrt{Q_q}\) is strictly less than the segment half-width \(1/\sqrt2\). This gives the asserted inradius and exactly the stated tangencies at the origin.

**Step 3: All possible centers.** Write an arbitrary intrinsic center uniquely as \(x=t h+\sum_j z_jw_j\). The two segment-end facets allow a radius-\(r_q\) ball exactly when \(|t|\le1-\sqrt2r_q=T_q\). Each of the remaining inequalities allows that ball precisely when
\[
\varepsilon\cdot z+r_q\sqrt{q-S^2/(q+2)}\le1.
\tag{1}
\]
For all signs satisfying \(|S|=\delta_q\), the norm term is exactly \(1\), so (1) forces \(\varepsilon\cdot z\le0\). The opposite sign is also an equality case and forces \(\varepsilon\cdot z\ge0\), hence \(\varepsilon\cdot z=0\).

If \(q\) is odd, all signs with \(S=\pm1\) span \(\mathbb R^q\): for any two indices, choose a sum-one sign vector opposite at those positions and swap them to obtain twice their coordinate difference; these differences span the sum-zero space, and a sum-one sign vector supplies the remaining direction. Therefore \(z=0\). The remaining signs obey (1) automatically, because their normal lengths do not exceed \(\sqrt{Q_q}\). This proves the odd case, including completeness.

If \(q\) is even, the signs with \(S=0\) span exactly \(\mathbf1^\perp\): swapping two opposite signs yields every coordinate difference, and all balanced vectors have sum zero. Hence \(z=s\mathbf1\). For signs with \(S\ne0\), the paired positive/negative conditions (1) become
\[
|s|\le f_q(|S|):=\frac{1-\sqrt{1-S^2/[q(q+2)]}}{|S|}
=\frac{|S|/[q(q+2)]}{1+\sqrt{1-S^2/[q(q+2)]}}.
\]
The last expression is strictly increasing in positive \(|S|\le q\). The smallest nonzero admissible value is \(|S|=2\); hence all facets are satisfied exactly when \(|s|\le f_q(2)=U_q\). This proves the rectangle formula with no omitted constraints. Strict monotonicity also establishes exactly which extra facets touch at its two \(s\)-endpoints. The two independent segment-end inequalities establish the remaining endpoint contact statement.

## Verification
The included standalone script `verify_k2q.py` was executed from its actual package path. It passed **6134** assertions/comparisons: rational Gram-inverse and sign-shell checks for every integer \(3\le q\le70\), direct construction of the original vertices and all facets in an independent orthonormal model for \(3\le q\le6\), and Chebyshev-center linear programs in those cases. The script verifies the full multiset of facet distances against the formula; these computational checks are corroboration only, not an infinite-dimensional proof. The unrestricted proof is given above.

## Relationship to prior work
Higashitani and Mori, *Minkowski decomposability of symmetric edge polytopes* (arXiv:2608.02445, first submitted 2026-08-03), identify \(K_{2,q}\) as one of the exceptional Minkowski-decomposable families and explicitly decompose its polytope. Their arguments concern decomposability and face adjacency, not intrinsic Euclidean inball centers or the complete distance shell. Codenotti, Riccardi and Venturello, *The number of edges of a symmetric edge polytope* (arXiv:2512.16572, 2025), classify graphs meeting a sharp edge-count bound, including this family; edge counts do not imply the metric information here. Kölbl's *On a Conjecture Concerning the Roots of Ehrhart Polynomials of Symmetric Edge Polytopes from Complete Multipartite Graphs* (arXiv:2404.02136, 2024) investigates Ehrhart polynomial roots, not Euclidean inballs. The polarity and lattice-enumeration literature concerns arithmetic data under nonisometric duality.

Other published specialized symmetric-edge inball results address stars, cycles, wheels, and crowns. In particular, an explicit star incenter-parity result concerns \(K_{1,q}\), whose standard symmetric-edge polytope is a single nonorthogonal cross-polytope, rather than the present \(K_{2,q}\) orthogonal product. No claim that a search proves historical uniqueness is made.

## Limitations
This statement is specific to the standard root-vector realization and the complete bipartite part size two. An arbitrary linear realization changes metric distances and its incenter locus. It does not determine maximum-volume John ellipsoids, general complete multipartite graphs, or \(q=1,2\). A search of accessible publications and mathematical-record summaries did not identify the complete stated radius/center theorem; a preexisting unindexed equivalent formula or general theorem may remain undiscovered. Some related record texts could be compared only from their accessible summaries, and that limitation is not a proof of noncoverage.

## References
1. A. Higashitani and A. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445 (2026-08-03), https://arxiv.org/abs/2608.02445.
2. G. Codenotti, R. Riccardi and L. Venturello, *The number of edges of a symmetric edge polytope*, arXiv:2512.16572 (2025-12-18), https://arxiv.org/abs/2512.16572.
3. M. Kölbl, *On a Conjecture Concerning the Roots of Ehrhart Polynomials of Symmetric Edge Polytopes from Complete Multipartite Graphs*, arXiv:2404.02136 (2024-04-02), https://arxiv.org/abs/2404.02136.
4. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, Discrete Appl. Math. 328 (2023), 139–153.
