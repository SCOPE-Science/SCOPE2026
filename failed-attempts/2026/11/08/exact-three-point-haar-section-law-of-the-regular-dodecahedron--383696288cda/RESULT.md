# Exact three-point Haar section law of the regular dodecahedron

## Finding

Let \(D\) be a regular Euclidean dodecahedron centered at the origin. Choose a unit vector \(U\) uniformly from the sphere \(S^2\), independently of all other choices. Write \(N(U)\) for the number of vertices of the convex polygon \(D\cap U^\perp\). Set
\[
\alpha=\arccos(1/3),\qquad \beta=\arccos(\sqrt5/3).
\]
Then the **entire** Haar central-section vertex-count law is
\[
\boxed{\begin{aligned}
\Pr(N=6)&=\frac5\pi(2\pi-3\alpha-3\beta),\\
\Pr(N=8)&=\frac{15}\pi(2\alpha+\beta-\pi),\\
\Pr(N=10)&=\frac3\pi(2\pi-5\alpha).
\end{aligned}}
\]
Numerically these probabilities are respectively \(0.638408811559\), \(0.238989468900\), and \(0.122601719541\). All other values have probability zero. The exact expectation is \(\mathbb E N=30\beta/\pi\approx6.968385815963\).

More precisely, the sphere of generic normals is partitioned by ten great circles into \(92\) spherical polygons: twenty geodesic hexagons each corresponding to six section vertices, sixty geodesic triangles corresponding to eight section vertices, and twelve geodesic pentagons corresponding to ten section vertices. The respective spherical chamber areas are
\[
2\pi-3\alpha-3\beta,\qquad 2\alpha+\beta-\pi,\qquad 2\pi-5\alpha.
\]
By polar duality, this is also the exact vertex-count law of the planar orthogonal shadow of a regular icosahedron under Haar-uniform projection direction.

## Assumptions and scope

The dodecahedron is convex and regular, not deformed or translated away from its center. A plane is always central. Normals are sampled with normalized rotation-invariant surface measure; opposing normals describe the same plane and have the same count. A generic normal means no vertex of the dodecahedron belongs to the section plane. Nongeneric directions lie on ten great circles and have probability zero. Section vertices mean ordinary corners of a nondegenerate convex polygon, so for generic normals each section vertex lies in the relative interior of one dodecahedron edge. No claim is made about offset sections, nonregular solids, exceptional orientations or the full metric distribution of section areas.

For an explicit model define \(\varphi=(1+\sqrt5)/2\) and take vertices
\[
(\pm1,\pm1,\pm1),\quad(0,\pm\varphi^{-1},\pm\varphi),\quad(\pm\varphi^{-1},\pm\varphi,0),\quad(\pm\varphi,0,\pm\varphi^{-1}).
\]
Each sign choice is independent within a displayed coordinate family. A common scaling does not affect the theorem.

## Proof

**1. Exact finite arrangement.** Scale the displayed coordinates by \(2\varphi\), obtaining eight sign combinations of \((1+\sqrt5,1+\sqrt5,1+\sqrt5)\) and twelve vectors given by cyclic permutations of \((0,\pm2,\pm(3+\sqrt5))\). All twenty vectors have the same squared length \(18+6\sqrt5\). Two of them form an edge of the dodecahedron exactly when their squared Euclidean distance is \(16\); there are thirty such edges, as can also be seen directly from the three regular pentagons incident at every vertex.

The vertices come in ten antipodal pairs. Choose one representative \(v_i\) from each pair, with \(i=0,\ldots,9\), and form the ten great circles \(\langle U,v_i\rangle=0\). For a generic \(U\), the signs \(s_i=\operatorname{sgn}\langle U,v_i\rangle\) are constant in each chamber of their complement. A dodecahedron edge is crossed by \(U^\perp\) precisely when its endpoint signs differ. Consequently, \(N(U)\) is constant in each sign chamber and is computed by summing thirty Boolean edge-crossing indicators.

**2. Exhaustive chamber certificate in an algebraic number field.** No three of the ten great circles meet at a point. Every crossing of circles \(i,j\) is therefore one of the two rays \(\pm(v_i\times v_j)\), and all their remaining eight dot products with the other representative axes are nonzero. There are exactly \(2\binom{10}{2}=90\) distinct crossings. Each crossing is a corner of four spherical sign chambers, formed by the four possible signs at axes \(i,j\); the other eight signs are determined by the crossing ray. Every chamber of this arrangement is a geodesically convex spherical polygon with at least one such corner, so enumerating these four sign patterns at all ninety crossings finds *every* chamber.

The bundled `verify_dodecahedron.py` implements this enumeration using integer pairs representing \(a+b\sqrt5\), with exact arithmetic and exact sign decisions. It constructs the twenty vertices, thirty edges, ten axes and ninety distinct crossings; it produces precisely ninety-two distinct sign chambers. For each chamber, it counts its incident crossing vertices, the thirty section-edge crossings, and the normalized inner products of the two inward axis normals at each corner. The complete exact outcome is:

| Chambers | Corners per spherical chamber | Section vertices | Corner normal products, with multiplicity |
| ---: | ---: | ---: | --- |
| 20 | 6 | 6 | \(1/3\) three times, \(\sqrt5/3\) three times |
| 60 | 3 | 8 | \(-1/3\) twice, \(-\sqrt5/3\) once |
| 12 | 5 | 10 | \(1/3\) five times |

Here a *corner normal product* is the inner product of the unit inward normals to its two bounding great-circle halfspaces. The table is not an incomplete random sample: every chamber occurs adjacent to one of the enumerated great-circle intersections, and the exact construction checks nonconcurrency before enumerating. The total counts also satisfy Euler's equation \(90-180+92=2\), independently agreeing with the known number of cells for ten great circles with no triple intersections.

**3. Spherical area calculation.** In a chamber specified by inward unit circle normals \(w_i,w_j\), the interior angle at their intersection is \(\pi-\arccos\langle w_i,w_j\rangle\). Girard's spherical polygon excess formula therefore gives chamber area
\[
\Omega=2\pi-\sum_{\text{chamber corners }(i,j)}\arccos\langle w_i,w_j\rangle.
\]
Substituting the three exact normal-product multisets in the table gives, in order, \(\Omega_6=2\pi-3\alpha-3\beta\), \(\Omega_8=2\alpha+\beta-\pi\), and \(\Omega_{10}=2\pi-5\alpha\). The resulting areas are strictly positive. Since uniform \(U\) has density \(1/(4\pi)\) with respect to spherical area, multiply the respective areas by the chamber multiplicities \(20,60,12\) and divide by \(4\pi\). This proves the three probabilities. Algebraically,
\[
20\Omega_6+60\Omega_8+12\Omega_{10}=4\pi,
\]
so no positive-mass orientation class has been omitted.

**4. An independent first-moment identity.** Adjacent dodecahedron vertices make central angle \(\beta\), because their squared edge length is \(16\) and their common squared radius is \(18+6\sqrt5\), implying the cosine \(\sqrt5/3\). For any two radial vectors with angular separation \(\gamma\), a Haar-uniform plane normal separates them with probability \(\gamma/\pi\), by projecting the normal onto their two-dimensional span and counting the opposite-sign angular intervals. Thus the expected number of crossed edges equals \(30\beta/\pi\). Directly combining the three obtained probabilities gives the same expression, checking the normalization without spherical cell-area summation.

**5. Relation to icosahedral shadows.** If \(P\) contains the origin in its interior and \(L=U^\perp\), the polar in \(L\) of the orthogonal projection of \(P\) is \(P^\circ\cap L\). A planar convex polygon and its polar have the same number of vertices. The polar of a centered regular icosahedron is a centered regular dodecahedron up to positive similarity. Therefore the preceding law is also the silhouette-vertex law for generic orthogonal projections of the regular icosahedron.

## Verification

Run `python3 verify_dodecahedron.py` using Python 3 with no external packages. The checker asserts exact algebraic vertex and edge construction, nonconcurrent great circles, ninety distinct oriented crossings, ninety-two chambers, all chamber corner counts, all section-vertex counts, and the three complete corner-normal-product multisets. All combinatorial and sign decisions use exact arithmetic in \(\mathbb Z[\sqrt5]\); floating point is used only after the exact theorem has been established to display the decimal probabilities and test the spherical-area sum. The expected output starts with `DODECAHEDRON_EXACT_ARRANGEMENT_OK` and ends with `DODECAHEDRON_MEAN`.

An independent random-direction edge-crossing sample (300,000 unit normals) yielded counts \(191838,71600,36562\) for the three vertex counts, respectively, close to the proven probabilities. This experiment is corroboration, not an infinite proof. All necessary exact finite cases are verified by the included checker, and the continuum of directions is handled by the geometric chamber partition and spherical area argument.

## Relationship to prior work

The random-view silhouette literature develops general expected-complexity bounds; Glisse and Lazard, *An Upper Bound on the Average Size of Silhouettes* (arXiv:cs/0702087, first posted February 14, 2007), explicitly recalls the classical edgewise expected-silhouette formula. Its general expectation calculation is consistent with the independently derived mean above, but neither this source's inspected full text nor its theorems give the three-point distribution for a regular icosahedron's shadow. Glisse, Lazard, Michel and Pouget, *Silhouette of a Random Polytope* (INRIA report 2013, journal 2016), study silhouettes of random spherical Poisson polytopes rather than a fixed regular Platonic solid under uniform views.

Standard icosahedron projection examples exhibit hexagonal, octagonal and decagonal silhouettes, without providing their Haar probabilities. The pre-existing rectified-truncated-icosahedron polyhedron has a known \(20/60/12\) count of hexagonal/triangular/pentagonal faces, which is a natural combinatorial comparator; those counts alone do not state the central-section incidence or provide the three spherical chamber areas under the present random-plane measure. A published exact law for *central icosahedron sections* concerns the polar-dual *dodecahedron projections*, not central dodecahedron sections or icosahedron projections. No equivalence or stronger statement encompassing this exact law was identified in the checked sources. This is a source-bounded originality assessment, not an assertion of global priority.

## Limitations

Only Haar-uniform orientations and central planar sections of the regular dodecahedron are covered. Zero-measure exceptional normals are excluded. The theorem does not determine section perimeter, area or vertex-position distributions, nor the law under noncentral affine planes. The ten-circle arrangement and an isomorphic \(92\)-face combinatorial tessellation have known predecessors, and a comprehensive historical source on this precise icosahedral silhouette distribution may be unindexed or inaccessible. No independent mathematical audit has been performed.

## References

1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, first posted February 14, 2007, https://arxiv.org/abs/cs/0702087.
2. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a Random Polytope*, J. Comput. Geom. **7** (2016), 86–99; original INRIA RR-8327, 2013, https://doi.org/10.20382/jocg.v7i1a5.
3. *The Icosahedron*, projection examples, https://eusebeia.qfbox.info/4d/icosahedron.
4. *Rectified truncated icosahedron*, polyhedral face-count data, https://en.wikipedia.org/wiki/Rectified_truncated_icosahedron.
5. *Exact Haar polygon-type law for central icosahedron sections* (2026), publicly indexed geometric research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
