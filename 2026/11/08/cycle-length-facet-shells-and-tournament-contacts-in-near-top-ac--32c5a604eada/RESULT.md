# Cycle-length facet shells and tournament contacts in near-top acyclohedra

## Finding
For every integer \(n\ge5\), the centered acyclohedron \(\mathcal A_{n,n-3}\) is Euclidean-isometric to the complete-graph cycle-space projection zonotope
\[
Z_n=\sqrt n\,\Pi\bigl([-\tfrac12,\tfrac12]^{\binom n2}\bigr),
\]
where \(\Pi\) is orthogonal projection from oriented edges of \(K_n\) to its circulation space \(C=\ker D\). Its dimension is \(d=\binom{n-1}{2}\).

The facets are in one-to-one correspondence with **oriented simple cycles** of \(K_n\). A length-\(\ell\) cycle gives a supporting hyperplane at Euclidean distance \(\sqrt{n\ell}/2\) from the center, with exactly \(\binom n\ell(\ell-1)!\) facets on that shell, for each \(3\le\ell\le n\). Consequently the unique largest Euclidean inball is centered at zero and has
\[
r_n^2=\frac{3n}{4},\qquad \#\{\text{tangent facets}\}=2\binom n3.
\]

The unique minimum enclosing Euclidean sphere is also centered at zero. Its squared radius is
\[
R_n^2=\frac n4\left(\binom n2-\epsilon_n\right),\qquad
\epsilon_n=\begin{cases}0,&n\text{ odd},\\1,&n\text{ even}.\end{cases}
\]
Its contact vertices correspond precisely to **regular tournaments** of \(K_n\) when \(n\) is odd and **almost-regular tournaments** (all indegree-outdegree differences \(\pm1\)) when \(n\) is even. Different such tournaments give different contact vertices, and no other points of the polytope contact the sphere. The Euclidean diameter equals \(2R_n\), achieved exactly by antipodal outer contact pairs.

Both the unique maximum-volume inscribed (John) ellipsoid and minimum-volume enclosing (Löwner) ellipsoid are the foregoing concentric Euclidean balls, respectively.

## Assumptions and scope
Fix \(n\ge5\). Let \(V=\mathbb R^n\) have orthonormal basis \(e_1,\ldots,e_n\); give each exterior power its standard inner product. Let \(u=\sum_{i=1}^ne_i\), and let \(\partial=\iota_u\) be the simplicial boundary on exterior monomials. Define the original, uncentered acyclohedron by
\[
\mathcal A_{n,n-3}=\sum_{\substack{S\subset[n]\\|S|=n-2}}[0,\partial e_S]
\subset\Lambda^{n-3}V,
\]
where \(e_S\) is the increasing wedge. Subtract its generator midpoint sum \(c_0=\tfrac12\sum_S\partial e_S\); all metric statements concern its affine span with the induced Euclidean metric. The center in the uncentered coordinates is \(c_0\). Generator signs have no effect on the centered zonotope.

Orient each edge of \(K_n\) from the smaller endpoint to the larger, let \(m=\binom n2\), and let the \(n\times m\) incidence map \(D\) have edge column \(e_i-e_j\) for \(i<j\). Write \(C=\ker D\), \(\Pi\) for its orthogonal projection, and \(\sigma\in\{\pm1\}^m\) for a tournament's signed edge orientations. A regular tournament has \(D\sigma=0\); an almost-regular tournament has all coordinates of \(D\sigma\) equal to \(\pm1\).

## Proof
**1. An isometric cycle-space model.** Under the Euclidean Hodge star \(*:\Lambda^{n-3}V\to\Lambda^3V\), each \(*\partial e_{[n]\setminus\{i,j\}}\) equals, up to its individual sign, \(u\wedge e_i\wedge e_j\). Indeed, \(*\iota_u\alpha\) equals \(u\wedge *\alpha\) up to the fixed degree-dependent sign, and \(*e_{[n]\setminus\{i,j\}}\) is a signed \(e_i\wedge e_j\). By the exterior-product inner-product identity,
\[
\langle u\wedge e_i\wedge e_j,u\wedge e_k\wedge e_l\rangle
=n\,\delta_{(ij),(kl)}-\langle e_i-e_j,e_k-e_l\rangle.
\]
Since \(DD^{\mathsf T}=nI-\mathbf1\mathbf1^{\mathsf T}\), we have
\[
\Pi=I-\frac1nD^{\mathsf T}D,\qquad n\Pi=nI-D^{\mathsf T}D.
\]
Thus, after harmless individual generator sign changes, the Gram matrices of the centered acyclohedron generators and the vectors \(\sqrt n\,\Pi e_{ij}\) coincide. The linear map matching these spanning configurations is an isometry. Moreover \(\operatorname{rank}\Pi=m-n+1=\binom{n-1}{2}\).

**2. Every facet and its metric shell.** For a nonzero normal \(f\in C\), the support function of \(Z_n\) is
\[
h_{Z_n}(f)=\frac{\sqrt n}{2}\sum_{e=1}^{m}|f_e|.
\]
Its exposed face has freely varying generators precisely at coordinates \(e\) with \(f_e=0\). Its codimension in \(C\) is therefore the dimension of the subspace of circulations supported on \(\operatorname{supp}f\). The face is a facet if and only if this dimension is one, equivalently if and only if \(f\) has inclusion-minimal nonzero circulation support. For a graph, those supports are exactly simple cycles; on a simple cycle the circulation is unique up to a scalar, with unit coefficients \(\pm1\). A length-\(\ell\) cycle normal \(f\) has \(\|f\|^2=\ell\) and \(h(f)=\sqrt n\ell/2\); the supporting hyperplane distance is \(\sqrt{n\ell}/2\). There are \(\binom n\ell(\ell-1)!/2\) unoriented simple cycles and two opposite facet normals per cycle, yielding the claimed shell multiplicity. The smallest possible length is three, establishing \(r_n^2=3n/4\) and the tangent-facet count.

The origin-centered inball is maximal by central symmetry: any ball of radius \(r\) and center \(c\) in a centrally symmetric body obeys \(r+|\langle f,c\rangle|/\|f\|\le h(f)/\|f\|\) for all normals \(f\). At radius \(r_n\), every triangular cycle normal forces \(\langle f,c\rangle=0\). Triangles span the complete-graph circulation space, so \(c=0\): the incenter is unique.

**3. Outer sphere and all contacts.** Every point in the zonotope is the image of a cube point and the squared norm is convex, so the maximum squared norm is attained at a cube corner \(\sigma/2\), \(\sigma\in\{\pm1\}^m\). Orthogonal projection gives
\[
\left\|\frac{\sqrt n}{2}\Pi\sigma\right\|^2
=\frac{nm-\|D\sigma\|^2}{4}.
\]
Every component of \(D\sigma\) has the parity of \(n-1\), and their sum is zero. When \(n\) is odd, \(\|D\sigma\|^2\ge0\), attained by a cyclic regular tournament. When \(n\) is even, each component is odd, so \(\|D\sigma\|^2\ge n\); equality is attained by deleting any vertex from a cyclic regular tournament on \(n+1\) vertices. Equality requires exactly the stated regular or almost-regular tournaments.

Any cube corner whose image attains the largest possible norm maps to a vertex: if its image were a nontrivial convex combination, strict convexity of squared Euclidean norm would force the combination's endpoints to coincide. Different maximizing signed corners cannot map to one vertex. Indeed an exposing vector in the relative interior of that vertex's normal cone can be chosen to have nonzero pairing with every nonzero generator \(\Pi e_{ij}\); it then uniquely determines all maximizing cube signs. Strict convexity further excludes all nonvertex contact points. Since \(Z_n=-Z_n\) has antipodal outer contacts, the origin-centered ball of radius \(R_n\) is the unique minimum enclosing ball: any center other than zero would require a larger ball to enclose an antipodal diametral pair. Equality in the diameter inequality \(\|x-y\|\le\|x\|+\|y\|\le2R_n\) forces antipodal outer contacts.

**4. John and Löwner ellipsoids.** Permutations of \([n]\) preserve the original exterior construction and induce signed-edge orthogonal transformations on \(C\), leaving \(Z_n\) invariant. This orthogonal representation of \(S_n\) on \(C\) is irreducible: if \(Q\) is an invariant symmetric operator, extend it to oriented-edge space as \(\Pi Q\Pi\). Symmetry gives equal diagonal entries; entries for two edges sharing a vertex differ only by the incidence sign; and entries between disjoint edges vanish by swapping the endpoints of one edge while fixing the other. Therefore every such operator has form \(aI+bD^{\mathsf T}D\), which restricts to \(aI\) on \(C\). By the spectral theorem, no proper invariant real subspace exists. Also there is no nonzero fixed vector in \(C\). The uniqueness and symmetry of John and Löwner ellipsoids force their centers to zero and quadratic forms to be scalar, hence they are centered balls. Their radii are exactly the already determined inradius and minimum-enclosing radius.

## Verification
The accompanying standalone exact-arithmetic programs use only Python's standard library. `verify_family.py` checks the oriented exterior-boundary Gram matrix against \(nI-D^{\mathsf T}D\), verifies simple-cycle flow normals, exhausts all \(2^{\binom n2}\) sign vectors for \(n=5,6\), and confirms the predicted contact strata; it obtains 24 contacts for \(n=5\) and 2640 for \(n=6\). The separate `verify_acyclohedron.py` exhaustively enumerates all 74 facets of \(\mathcal A_{5,2}\) by exact rational linear algebra, independently recovering the \(20,30,24\) facet shell multiplicities, inball and circumsphere, and its 24 outer contacts. These finite checks are corroboration; the preceding argument proves all integers \(n\ge5\).

## Relationship to prior work
Pohoata and Zhu introduce hypergraphic zonotopes and acyclohedra, study their volumes and hypertournaments, and give examples of their facets. Their studied invariants and descriptions do not furnish the above full metric classification of the near-top family in the inspected preprint. The cycle-space model is related to classical graph-matroid duality, and minimal-support circulations as cycles, as well as regular and almost-regular tournaments, are known ingredients. The contribution is the canonical **Euclidean isometry**, its complete facet-distance shells and sharp insphere, and the parity-sensitive minimum sphere and John–Löwner classification for every near-top acyclohedron.

For clarity, the previously studied **orthogonal cographic symmetric-edge polytope** \(\operatorname{conv}\{\pm\Pi e_{ij}\}\) is not this projected-cube zonotope \(\Pi([-1/2,1/2]^m)\): one is the convex hull of projected coordinate vectors and the other is their Minkowski sum. Their known metric classification therefore does not imply the stated formulas. Likewise, the published radius results for vertex-transitive root-system zonotopes require vertex transitivity, absent here because the extremal tournament contact classification leaves other vertices at smaller radii.

## Limitations
The theorem is for the near-top uniformity \(d=n-3\), not every \(\mathcal A_{n,d}\) or arbitrary hypergraphs; all Euclidean quantities depend on the specified orthonormal exterior-basis metric. Facet distances and extremal contacts are classified, not all vertex radial shells or all face numbers. Counts of regular/almost-regular tournament contacts are characterized combinatorially rather than given by a closed formula for arbitrary \(n\). Finite tests cannot independently establish the all-order theorem. Historical priority remains provisional because other literature may contain equivalent cographic-zonotope metric formulas under different terminology.

## References
1. Cosmin Pohoata and Daniel G. Zhu, *Hypergraphic zonotopes and acyclohedra*, arXiv:2503.21752v1 (first posted 2025-03-27), https://arxiv.org/abs/2503.21752 .
2. Mario Sanchez and Brett Kolesnik, *The Geometry of Random Tournaments*, arXiv:2009.09322 (2020), https://arxiv.org/abs/2009.09322 .
3. *Parity-sharp John and Löwner balls of orthogonal cographic complete-graph polytopes*, publicly available full research statement (2026), distinguished from the projected-cube construction by its defining convex hull.
4. Martin Winter, *Classification of Vertex-Transitive Zonotopes*, arXiv:1912.10469 (2019); the vertex-transitive assumption does not hold for this family.
