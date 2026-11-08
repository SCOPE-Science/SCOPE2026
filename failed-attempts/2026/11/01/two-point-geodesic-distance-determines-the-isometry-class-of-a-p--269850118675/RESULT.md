# Two-point geodesic distance determines the isometry class of a planar flat torus

## Finding

**Theorem (distance-distribution rigidity in dimension two).** Let \(\Lambda\) be any full-rank Euclidean lattice in \(\mathbb R^2\), let \(T_\Lambda=\mathbb R^2/\Lambda\) carry its intrinsic quotient Euclidean distance, and let \(X,Y\) be independent normalized-area-uniform random points of \(T_\Lambda\). The law of \(D_\Lambda=d_{T_\Lambda}(X,Y)\) determines \(\Lambda\) up to Euclidean orthogonal congruence. Thus two planar flat tori have the same two-point geodesic distance distribution if and only if they are isometric.

The reconstruction is explicit. Let \(F_\Lambda(r)=\Pr(D_\Lambda\le r)\). The area and the angular exclusion profile are recovered from the distribution by

\[
A=\lim_{r\downarrow0}\frac{\pi r^2}{F_\Lambda(r)},\qquad H(r)=2\pi-\frac{A}{r}F_\Lambda'(r)\quad(r>0).
\]

Let \(V\) be the centered Dirichlet–Voronoi polygon of \(\Lambda\), and let \(h_1,\ldots,h_s\) be the distinct distances of its facets from the origin, with \(m_j\) facets at distance \(h_j\). Then \(H\) is locally Lipschitz away from these finitely many radii and at each one has the exact one-sided onset

\[
H(h_j+\varepsilon)-H(h_j)
=2m_j\sqrt{\frac{2}{h_j}}\,\varepsilon^{1/2}+O_\Lambda(\varepsilon)\qquad(\varepsilon\downarrow0).
\]

Consequently \(F_\Lambda\) determines the multiset of all facet distances, counting multiplicity. Every planar lattice has four or six Voronoi facets. With four facets the cell is rectangular and the two generator lengths are twice the two antipodal facet-pair distances. With six facets, the three facet-pair distances \(h_a,h_b,h_c\) give the lengths \(a=2h_a\), \(b=2h_b\), \(c=2h_c\) of an obtuse superbase; choosing \(u,v\) with \(\|u\|=a\), \(\|v\|=b\), and \(\|u+v\|=c\), the Gram matrix is

\[
G=\begin{pmatrix}a^2&(c^2-a^2-b^2)/2\\(c^2-a^2-b^2)/2&b^2\end{pmatrix}.
\]

Any ordering of the three recovered lengths corresponds to an integral change of lattice basis, possibly followed by an orthogonal reflection. Repeated distances, square tori, and the regular hexagonal torus are all included.

## Assumptions and scope

All tori are **two-dimensional, connected, flat, complete quotient tori** of full-rank Euclidean lattices, with the unscaled Riemannian distance. Sampling is independent normalized Riemannian area (Haar measure), not uniform sampling from a fundamental parallelogram with ambient, unreduced Euclidean distance. Distinct supports are counted without suppressing multiplicities. The distance law is assumed known exactly as a function, not estimated from finitely many observations.

A facet supported by a vector \(v\in\Lambda\setminus\{0\}\) has equation \(x\cdot v=\|v\|^2/2\); its supporting-line distance is \(h=\|v\|/2\). A relevant vector is one whose perpendicular-bisector inequality contributes a genuine facet of \(V\). There are exactly two opposite facets for each relevant vector pair. We write \(m(h)\) for the number of facets having support distance \(h\).

## Proof

**1. Haar reduction to radial areas.** The difference \(X-Y\) is Haar-uniform on \(T_\Lambda\), so selecting its closest representative in \(V\) gives a Lebesgue-uniform point of \(V\), except on its null-measure boundary. Since geodesic distance is the minimum norm among lattice translates,

\[
F_\Lambda(r)=\frac{|V\cap B_r(0)|}{A},\quad A=|V|=\det(\Lambda).
\]

For \(0<r<\min_i h_i\), the Euclidean disk \(B_r\) lies in \(V\), hence \(F_\Lambda(r)=\pi r^2/A\); in particular \(A\) is determined. Let \(U_r\) be the set of angles \(\theta\in[0,2\pi)\) for which the point \(r(\cos\theta,\sin\theta)\) lies outside \(V\). Its angular measure is \(H(r)\). Polar differentiation (or the coarea formula) gives \(A F_\Lambda'(r)=r(2\pi-H(r))\). The derivative exists for every positive radius, including radii of vertices, by continuity of angular measure; a null set of boundary directions does not affect it.

**2. Strictly interior facet feet.** For a facet associated with a lattice vector \(v\), the point \(x=v/2\) is in the relative interior of that facet. Indeed, by the strict Voronoi-vector criterion, the only shortest elements of the congruence class \(v+2\Lambda\) are \(\pm v\) (see Kurlin, Lemma 2.5, or the Voronoi-relevant-vector characterization). For any \(w\in\Lambda\setminus\{0,v\}\) we therefore have \(\|v-2w\|>\|v\|\), which is equivalent to \(\|v/2-w\|>\|v/2\|\). Thus every other lattice bisector inequality is strict at \(v/2\), and a neighborhood of that point on the boundary of \(V\) consists solely of the facet in question. This includes rectangular and equal-length degeneracies.

**3. Recovering every support distance.** Write a facet inequality as \(x\cdot n\le h\), with outward unit normal \(n\). On the circle of radius \(r\), that inequality excludes the angular interval \(\big|\theta-\arg(n)\big|<\arccos(h/r)\) when \(r>h\), and excludes none when \(r\le h\). Because the foot \(hn\) is interior to its facet, for \(r\) sufficiently close to \(h\) from above this newly excluded arc is not overlapped by any other facet's excluded arc. Its length therefore contributes exactly

\[
2\arccos(h/r)=2\sqrt{\frac{2}{h}}\,(r-h)^{1/2}+O_h((r-h)^{3/2}).
\]

For a radius \(h\) shared by \(m(h)\) facets, their foot neighborhoods are disjoint, so these contributions add. All arcs belonging to inequalities with strictly smaller support distances have smooth endpoints in \(r\), except where their endpoints coincide. Such coincidences correspond to rays through Voronoi vertices. A Voronoi vertex cannot be a facet foot by Step 2, hence the relevant circle meets each incident facet line transversely and each endpoint angle varies with bounded derivative locally. A union of finitely many intervals whose endpoints are locally Lipschitz has locally Lipschitz total length. Therefore these previously active arcs affect \(H(h+\varepsilon)-H(h)\) only by \(O(\varepsilon)\), even if a vertex radius happens to coincide with \(h\). This proves the claimed coefficient and also that every radius **other than a facet distance** has locally Lipschitz \(H\). The singularities are positive, so no cancellation is possible. Consequently the exact law determines all \((h,m(h))\), including coincident facet distances.

**4. Reconstructing the lattice.** By planar Voronoi reduction every rank-two lattice has an obtuse superbase \(u,v,w\), with \(u+v+w=0\), \(u,v\) a lattice basis. Its Voronoi domain has six facets \(\pm u,\pm v,\pm w\) in the strict case, or a rectangle with four facets in the degenerate case (Kurlin, Theorem 2.9 and Lemmas 2.8, 4.3). In the strict case the three recovered pairs of facet distances give the unordered set of lengths \(\{\|u\|,\|v\|,\|w\|\}\). Given any ordering, form the displayed Gram matrix, since \(w=-u-v\). Permuting \(u,v,w\) changes an integral lattice basis by a matrix in \(\operatorname{GL}_2(\mathbb Z)\); changing all signs or reflecting does not change the isometry class. The Gram matrix therefore recovers \(\Lambda\) uniquely up to orthogonal congruence. In the four-facet case the relevant vectors are the two orthogonal generators of a rectangular lattice, whose lengths likewise follow from the support distances. This completes the proof for every rank-two lattice.

## Verification

The standalone standard-library program `verify_flat_torus.py` independently computes the Voronoi polygon from a finite neighbor half-plane intersection, constructs its facet thresholds, and compares two integrals of \(F_\Lambda\): polar radial integration and integration of union lengths of excluded circular arcs. It also verifies reconstructed area and finite-difference singularity coefficients in square, rectangular, triangular, and oblique examples. Run `python3 verify_flat_torus.py` in the directory containing the program. The recorded run passed 8 lattice configurations, 48 numerical CDF comparisons, 57 finite-difference checks, and all area/reconstruction consistency assertions.

Finite neighborhood clipping and floating-point checks do **not** prove the universal classification or the expansion. The mathematical proof is Steps 1–4 and uses the published planar Voronoi-superbase classification.

## Relationship to prior work

Kwakkel, Martens and Peixoto (2011) proved **focal rigidity** for flat tori: an equivalence of the full geodesic-multiplicity stratification forces an isometry up to scale. This is a different, richer datum; their theorem does not identify the scalar two-point geodesic-distance law as a complete invariant. Bonifas and Dadush (2014) treated Voronoi-relevant vectors for lattice closest-vector algorithms and supply relevant background, not the inverse distance-law statement. Leipold, Lazar, Brakke and Srolovitz (2015) classified Voronoi-cell topologies of perturbed planar lattices; their distributions concern perturbation-induced topology, not Haar-geodesic distances. Kurlin (2022, accessible full article) established complete invariants from **shortest Voronoi vector lengths** and from the discrete lattice point-distance sequence. Those are acknowledged reconstruction ingredients. Its `PDD` is a pointwise nearest-neighbor-distance sequence among lattice points, **not** the distribution of distances between two independent Haar-random points on the quotient torus. The new inference is that a single scalar random geodesic-distance law reveals the complete support-distance multiset, including multiplicities, via square-root singularities.

Targeted searches in the mathematical literature and published findings found no stronger or equivalent statement about the exact Haar two-point distance distribution. This negative search is not proof of worldwide historical novelty; older unindexed formulas or indirect consequences may exist.

## Limitations

The theorem is restricted to dimension two, exact Euclidean quotient metrics, normalized-area sampling, and the entire exact distribution. It does not assert numerical stability under noisy empirical CDF measurements, finite-sample reconstruction accuracy, recovery of an oriented marking, or higher-dimensional analogues. The proof uses the known planar obtuse-superbase classification; it does not claim that classification is new. Independent priority review has not been performed.

## References

1. F. Kwakkel, M. Martens and M. Peixoto, *Focal Rigidity of Flat Tori*, public preprint 2011-04-29, arXiv:1104.5541, https://arxiv.org/abs/1104.5541.
2. N. Bonifas and D. Dadush, *Short Paths on the Voronoi Graph and the Closest Vector Problem with Preprocessing*, public preprint 2014-12-18, arXiv:1412.6168, https://arxiv.org/abs/1412.6168.
3. H. Leipold, E. A. Lazar, K. A. Brakke and D. J. Srolovitz, *Statistical Topology of Perturbed Two-Dimensional Lattices*, public preprint 2015-09-10, arXiv:1509.03280v1, https://arxiv.org/html/1509.03280v1.
4. V. Kurlin, *Mathematics of 2-Dimensional Lattices*, first published 2022-12-07, *Foundations of Computational Mathematics* 24 (2024), 805–863, doi:10.1007/s10208-022-09601-8, https://link.springer.com/article/10.1007/s10208-022-09601-8.
