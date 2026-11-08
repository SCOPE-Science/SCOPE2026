# Universal inertia and covariance laws for cactus graphical zonotopes

## Finding
For every connected simple cactus graph \(G\) with \(n\ge2\) vertices and \(c\) cycles, let its centered graphical zonotope be
\[
 Z_G=\sum_{uv\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2]\subset\{x\in\mathbb R^n:\sum_vx_v=0\}.
\]
Let \(X\) be uniform with respect to intrinsic Euclidean \((n-1)\)-dimensional volume on \(Z_G\). Then \(\mathbb E X=0\), and its covariance is the weighted Laplacian
\[
 \operatorname{Cov}(X)=\frac1{12}\left(\sum_{e\text{ bridge}} b_eb_e^{\mathsf T}+\sum_{C\text{ cycle}}\frac{k_C+2}{k_C}\sum_{e\in E(C)}b_eb_e^{\mathsf T}\right),
\]
where \(b_e=e_u-e_v\) is an arbitrarily oriented incidence column and \(k_C=|E(C)|\). In particular the **normalized Euclidean inertia** (second radial moment about the centroid) obeys the universal law
\[
 J(Z_G):=\mathbb E\|X\|^2=\operatorname{tr}\operatorname{Cov}(X)=\frac{n-1+3c}{6}.
\]
Thus this metric quantity is insensitive to every cycle length and to all ways the cycles and bridges are attached, once the vertex and cycle counts are fixed.

There is also a closed affine-invariant isotropic constant. Writing \(d=n-1\), \(\operatorname{Vol}_d\) for intrinsic Euclidean volume, and
\[
 L(Z_G)^2=\frac{\det_{\mathbf1^\perp}(\operatorname{Cov}(X))^{1/d}}{\operatorname{Vol}_d(Z_G)^{2/d}},
\]
one has
\[
 \operatorname{Vol}_d(Z_G)=\sqrt n\prod_C k_C,
 \qquad
 L(Z_G)^2=\frac1{12}\left(\prod_C\frac{\big((k_C+2)/k_C\big)^{k_C-1}}{k_C}\right)^{1/(n-1)}.
\]
Empty products are one. The trace law has the sharp bounds over all connected simple cactus graphs on \(n\) vertices:
\[
 \frac{n-1}{6}\ \le\ J(Z_G)\ \le\ \frac{n-1+3\lfloor(n-1)/2\rfloor}{6}.
\]
The minimum occurs exactly for trees; the maximum occurs exactly for graphs with the maximum possible \(\lfloor(n-1)/2\rfloor\) cycles (achievable by edge-disjoint triangles joined at articulation vertices, with one possible extra bridge).

## Assumptions and scope
A cactus means a connected simple graph in which every edge belongs to at most one simple cycle. Cycles may meet in articulation vertices. All edges carry unit generator lengths; the ambient metric is the ordinary Euclidean metric of the canonical incidence-coordinate realization, restricted to \(\mathbf1^\perp\). Uniformity refers to volume **on the zonotope**, not the pushforward of uniform independent edge coefficients; the latter generally gives a different probability law when cycles occur.

## Proof
**1. Independent quotient factors.** Orient the edges of each simple cycle consistently, and all bridges arbitrarily. For each cycle \(C\), the sum of its incidence columns is zero. The real kernel of the incidence map consists exactly of the independent one-dimensional spaces of constant edge coefficients on each cycle: this follows because the cactus cycle vectors are independent (disjoint edge supports) and their number \(c\) equals the nullity \(|E|-n+1\). Consequently, the incidence map induces a linear isomorphism
\[
 \mathbb R^{B}\ \oplus\!\bigoplus_C\mathbf1_{k_C}^{\perp}\longrightarrow\mathbf1_n^{\perp},
\]
where \(B\) is the bridge set. Subtracting the mean from coefficients on each cycle sends \([-1/2,1/2]^{k}\) onto
\[
 Q_k=\{y\in\mathbf1_k^\perp:\max_i y_i-\min_i y_i\le1\}.
\]
Hence the zonotope is a fixed invertible linear image of \([-1/2,1/2]^B\times\prod_C Q_{k_C}\). The constant Jacobian of this isomorphism shows that a uniform point in the zonotope corresponds to the **product of uniform measures** on these factor polytopes. All factors are centrally symmetric, so the mean is zero.

**2. Exact projected-cube covariance.** Let \(Y\) be uniform on \(Q_k\), \(k\ge3\). Coordinate permutations act transitively and preserve volume. For each of the \(k!\) order chambers \(y_{\pi(1)}\le\cdots\le y_{\pi(k)}\), the consecutive gaps \(g_j=y_{\pi(j+1)}-y_{\pi(j)}\) obey \(g_j\ge0\) and \(\sum_{j=1}^{k-1}g_j\le1\). The chamber-to-gap map is linear with constant nonzero Jacobian, and the chambers have equal volumes by coordinate symmetry. Thus the \(k\) nonnegative quantities \(g_1,\ldots,g_{k-1},1-\sum_jg_j\) have the uniform Dirichlet \((1,\ldots,1)\) law, and the rank permutation is independent and uniform.

For two fixed different labels, if their ranks are \(m\) positions apart, the difference equals the sum of \(m\) successive gaps; its second moment is \(m(m+1)/(k(k+1))\). The rank separation equals \(m\), for \(1\le m\le k-1\), with probability \(2(k-m)/(k(k-1))\). Therefore
\[
 \mathbb E(Y_i-Y_j)^2=\sum_{m=1}^{k-1}\frac{2(k-m)}{k(k-1)}\frac{m(m+1)}{k(k+1)}=\frac{k+2}{6k}.
\]
Exchangeability and \(\sum_iY_i=0\) imply \(\operatorname{Cov}(Y)=\alpha_k(I_k-\mathbf1\mathbf1^{\mathsf T}/k)\). The difference variance is \(2\alpha_k\), so \(\alpha_k=(k+2)/(12k)\).

**3. Covariance, volume and inertia.** A bridge coefficient is uniform on \([-1/2,1/2]\) and has variance \(1/12\). Every oriented cycle incidence matrix annihilates \(\mathbf1\), so its covariance contribution is \(\alpha_k B_CB_C^{\mathsf T}\). Independence of the factors yields the claimed weighted Laplacian. Since every edge root has squared norm two,
\[
 \operatorname{tr}\operatorname{Cov}(X)=\frac16\Bigl(|B|+\sum_C(k_C+2)\Bigr).
\]
The cactus identity \(|B|+\sum_C(k_C-1)=n-1\) reduces this to \((n-1+3c)/6\).

For the ordinary zonotope volume, the standard parallelepiped decomposition gives \(\operatorname{Vol}_{n-1}(Z_G)=\sqrt n\,\tau(G)\), since every oriented spanning-tree incidence basis has Gram determinant \(n\). A spanning tree of a cactus is obtained by omitting one edge from each cycle, whence \(\tau(G)=\prod_C k_C\).

Set \(w_e=1\) on bridges and \(w_e=(k_C+2)/k_C\) on cycle edges. Then \(12\operatorname{Cov}(X)\) is the weighted Laplacian. The weighted matrix-tree theorem gives
\[
 \det_{\mathbf1^\perp}(12\operatorname{Cov}(X))=n\prod_C k_C\left(\frac{k_C+2}{k_C}\right)^{k_C-1}.
\]
(The bridge weights equal one.) Combine this with the exact volume and the definition of \(L\) to obtain the stated isotropic-constant formula.

**4. Sharp range.** The cactus identity and \(k_C\ge3\) give \(n-1=|B|+\sum_C(k_C-1)\ge2c\). Equality in the lower inertia bound requires \(c=0\), i.e. a tree. Equality in the upper bound requires \(c=\lfloor(n-1)/2\rfloor\). Such graphs exist for each \(n\), by using triangles attached at one common vertex (and adding a bridge if \(n\) is even).

**5. Necessity of the cactus condition.** For the graph with edges \(01,12,20,13,23\), two triangles share the edge \(12\), violating the cactus hypothesis. Exact polyhedral integration in dimension three gives \(J=13/8\), whereas naively substituting \(n=4\), cyclomatic rank two into the cactus expression would give \(3/2\). The supplied checker independently obtains this value through a complete rational facet triangulation. This is a boundary example, not part of the asserted cactus theorem.

## Verification
Run `python3 cactus_inertia_checker.py` from the same directory. It uses only the Python standard library and exact rational arithmetic. It independently integrates uniform cycle-factor covariances over all coordinate-ordering simplices for eight cactus examples, verifies 238 covariance matrix entries, all displayed trace identities, the weighted matrix-tree cofactors, and the expected spanning-tree counts. For the non-cactus diamond it independently constructs the signed incidence image, enumerates its supporting facets and integrates over 32 rational tetrahedra, obtaining \(13/8\). The final marker is `CACTUS_UNIFORM_INERTIA_EXACT_CHECKS_PASSED`. These are finite consistency tests; the argument above proves the statements for every cactus graph.

## Relationship to prior work
Padrol, Pilaud and Poullot investigate the combinatorial deformation cones of graphical zonotopes; their results fix the natural graphical-zonotope setting but do not express uniform-volume second moments. Joós and Lángi extend zonotope volume decompositions to intrinsic volumes and investigate isoperimetric questions; the volume formula used above belongs to that established framework. Neither paper's inspected geometric statements imply the covariance formula, universal trace law, or affine-invariant isotropic-constant product. The current conclusions are derived here from the independent cycle quotient decomposition and uniform-volume order-chamber integration; they should not be confused with variance of the *directional width* of a zonotope, which involves a different measure and random variable. Historical priority remains provisional pending further comparison of differently named volume-moment formulas.

## Limitations
The metric is canonical Euclidean incidence geometry, not arbitrary affine coordinates or edge weights. The exact trace law uses edge-disjoint cycles; it need not hold for overlapping cycles, as the explicit diamond shows. The result is an analytic theorem with finite numerical-free checker corroboration, not an independent audit or a claim about all graphs. The individual covariance entries may depend on cycle positions and graph topology despite the universal trace.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, first arXiv version 2021-11-24, arXiv:2111.12422v1; DOI 10.1007/s00454-023-00586-x.
2. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, first arXiv version 2022-06-07, arXiv:2206.03204v1; DOI 10.1112/mtk.12191.
3. The classical matrix-tree theorem and zonotope spanning-tree volume decomposition are used in their standard forms; the novel calculation here concerns uniform Euclidean second moments on the cactus quotient factors.
