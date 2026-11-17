# An angular fingerprint and a two-scale dihedral law for matching-deleted Laplacian simplices

## Finding
Let \(n\ge3\), let \(0\le m\le\lfloor n/2\rfloor\), and let \(G_{n,m}\) be the graph obtained from the complete graph on \(n\) labelled vertices by deleting a matching of \(m\) edges. Let \(L\) be its ordinary unweighted graph Laplacian and \(T_{n,m}=\operatorname{conv}\{Le_i:1\le i\le n\}\) in the inherited Euclidean metric on the zero-sum hyperplane. This is an \((n-1)\)-simplex. Write \(s=n-2m\), \(c=1/(n-1)\), and \(k=1+2n/(n-2)^2\).

For every pair of distinct facets, their interior dihedral angle is one of the following values, with the indicated **exact multiplicity** (terms of multiplicity zero are omitted):

| Facet pair indexed by vertices | Dihedral angle | Multiplicity |
|:--|:--|--:|
| Both vertices unmatched | \(\arccos(c)\) | \(\binom{s}{2}\) |
| One matched, one unmatched | \(\arccos(c/\sqrt{k})\) | \(2ms\) |
| Matched vertices in different deleted edges | \(\arccos(c/k)\) | \(2m(m-1)\) |
| Endpoints of the same deleted edge | \(\arccos((c+k-1)/k)\) | \(m\) |

All angles are strictly acute. Whenever the relevant types are present, the angles increase strictly in the order **same deleted edge, both unmatched, mixed, different deleted edges**. In particular, if \(m>0\), the deleted matching is reconstructed *exactly* from the labelled facet-angle matrix: its edges are precisely the pairs having the smallest interior dihedral angle. Thus the geometric facet data retain the missing-edge locations, not merely the deletion count.

There is also a two-scale high-dimensional angular law. Suppose \(n\to\infty\) along any sequence with \(m/n\to\rho\in[0,1/2]\), and let \(\Theta_n\) be the interior dihedral angle of a uniformly sampled ridge. Then
\[
 n^2\left(\frac\pi2-\Theta_n-\frac1n\right)\ \xrightarrow{\mathrm d}\ 1-B,\qquad B\sim\operatorname{Binomial}(2,2\rho).
\]
The exceptional same-edge ridges have exact probability \(2m/[n(n-1)]\); when such a ridge is present its angle obeys \(n(\pi/2-\Theta_n)\to3\), whereas all other types satisfy \(n(\pi/2-\Theta_n)\to1\). The exceptional ridges therefore disappear from the weak second-order bulk law while retaining a threefold first-order angular defect.

## Assumptions and scope
The graph is simple, unweighted, undirected and connected. All missing edges are pairwise vertex-disjoint; the formula does not cover intersecting deletions. The facet \(F_i\) is the convex hull of all columns \(Le_j\) except \(Le_i\). Each unordered pair \(\{i,j\}\) labels a ridge \(F_i\cap F_j\), also when \(n=3\), where ridges are zero-dimensional. Angles use the standard ambient Euclidean inner product restricted to \(\mathbf1^\perp\), rather than an arbitrary lattice-affine coordinate metric.

## Proof
**1. Orthogonal spectral splitting.** Put \(P=I-\mathbf1\mathbf1^{\mathsf T}/n\). For each deleted edge \(\{a,b\}\), put \(d_{ab}=e_a-e_b\), and define \(W=\frac12\sum_{\{a,b\}\text{ deleted}}d_{ab}d_{ab}^{\mathsf T}\). Because deleted edges are disjoint, their normalized difference vectors are orthonormal; hence \(W^2=W\), \(PW=WP=W\). The graph Laplacian is exactly
\[
 L=nP-2W.
\]
Its eigenvalue is \(n-2>0\) on \(\operatorname{im}W\), \(n\) on \(\mathbf1^\perp\cap\ker W\), and zero on \(\mathbb R\mathbf1\). It consequently has rank \(n-1\), so its \(n\) zero-sum columns are the vertices of a simplex. Its Moore–Penrose inverse and the Gram matrix of the facet normals are
\[
 L^+=\frac1nP+\left(\frac1{n-2}-\frac1n\right)W,
 \qquad H=(L^+)^2=\frac1{n^2}P+\delta W,
\]
where \(\delta=4(n-1)/[n^2(n-2)^2]\).

**2. Facet geometry.** For a point \(x=\sum_j\lambda_j Le_j\), with \(\sum_j\lambda_j=1\), one has \(\langle L^+e_i,x\rangle=\lambda_i-1/n\). Thus \(L^+e_i\) is a nonzero inward normal of \(F_i\). With \(H_{ij}=\langle L^+e_i,L^+e_j\rangle\), the interior dihedral angle at \(F_i\cap F_j\) is
\[
 \theta_{ij}=\arccos\!\left(\frac{-H_{ij}}{\sqrt{H_{ii}H_{jj}}}\right).
\]
Set \(b=(n-1)/n^3\). The diagonal entries of \(H\) are \(b\) at unmatched vertices and \(bk\) at matched vertices, because \(\delta/(2b)=k-1\). For \(i\ne j\), the entry is \(-1/n^3\), except at endpoints of the same deleted edge, where it is \(-1/n^3-\delta/2\). Dividing the negative off-diagonal entries by the appropriate geometric means gives exactly the four arguments of \(\arccos\) in the table.

**3. Multiplicity, ordering and reconstruction.** There are \(s\) unmatched vertices and \(2m\) matched vertices, forming \(m\) disjoint pairs. The four respective pair counts are \(\binom{s}{2}\), \(2ms\), \(\binom{2m}{2}-m=2m(m-1)\) and \(m\); they total \(\binom n2\), so the table is exhaustive. Since \(k>1\) and \(0<c<1\),
\[
 \frac{c+k-1}{k}>c>\frac c{\sqrt k}>\frac ck>0.
\]
The inverse-cosine function is strictly decreasing. The angular ordering, acuteness and matching reconstruction follow. This also proves that the four nonempty categories cannot accidentally coincide.

**4. Two-scale limit.** With \(z=1/n\), the four cosine arguments, in table order, have expansions
\[
 \begin{aligned}
 c&=z+z^2+O(z^3),\\
 c/\sqrt k&=z+O(z^3),\\
 c/k&=z-z^2+O(z^3),\\
 (c+k-1)/k&=3z+3z^2+O(z^3).
 \end{aligned}
\]
For every type \(\frac\pi2-\theta=\arcsin(\cos\theta)\), and \(\arcsin t=t+O(t^3)\) as \(t\to0\). Therefore the scaled second-order defects are respectively \(1+o(1)\), \(o(1)\), \(-1+o(1)\), and \(2n+O(1)\). Their respective probabilities under a uniformly chosen ridge tend to \((1-2\rho)^2\), \(4\rho(1-2\rho)\), \(4\rho^2\), and \(0\), because the last probability is exactly \(2m/[n(n-1)]\). The first three limiting masses are those of \(1-\operatorname{Binomial}(2,2\rho)\), proving weak convergence even though the vanishing-probability exceptional value diverges. The first-order limits for exceptional and ordinary ridges follow directly from the leading terms.

## Verification
The standalone script `verification/check_angles.py` uses exact rational arithmetic. For every \(n=3,\ldots,16\) and each possible matching size \(0\le m\le\lfloor n/2\rfloor\), it constructs the original graph Laplacian, independently checks the pseudoinverse identity \(LL^+=P\), computes the normal Gram matrix by matrix multiplication, checks every squared normalized normal product and negative sign, and verifies each type multiplicity. This covers 77 parameter pairs and 4,774 individual ridges. It does not constitute an infinite-dimensional proof; the unrestricted argument is above.

To reproduce: run `python verification/check_angles.py` with Python 3 and only its standard library.

## Relationship to prior work
Braun and Meyer introduced graph Laplacian simplices and studied their Ehrhart/reflexivity behavior, including complete graphs. Meyer and Pllaha studied coding-theoretic aspects and dual simplices. Devriendt and Van Mieghem develop the different Fiedler graph-simplex construction whose vertex Gram matrix is \(L\), whereas the present Laplacian-column simplex has vertex Gram matrix \(L^2\); its angular data therefore are not the same. Juhnke-Kubitzke and Köhne study higher-dimensional Laplacian polytopes of simplicial complexes. The present result concerns the full inherited-Euclidean dihedral spectrum and a two-scale limit under independent matching deletions, rather than lattice, coding, graph-spectrum, or intrinsic-volume data.

## Limitations
The result requires the deleted edges to be disjoint and does not classify arbitrary dense-graph Laplacian simplices. Asymptotic statements are for \(n\to\infty\) with \(m/n\) convergent; no rate of convergence of the empirical angle distribution is asserted. The arithmetic verification covers finite orders only. The literature comparison does not establish absolute historical priority; equivalent unindexed results may exist. No independent audit has been performed.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085 (first public version 21 June 2017), https://arxiv.org/abs/1706.07085.
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960 (first public version 9 September 2018), https://arxiv.org/abs/1809.02960.
3. K. Devriendt and P. Van Mieghem, *The Simplex Geometry of Graphs*, arXiv:1807.06475 (first public version 17 July 2018), https://arxiv.org/abs/1807.06475.
4. M. Juhnke-Kubitzke and D. Köhne, *Laplacian Polytopes of Simplicial Complexes*, arXiv:2301.11602 (first public version 27 January 2023), https://arxiv.org/abs/2301.11602.
