# The projection body of the rhombic triacontahedron: an exact icosahedral determinant spectrum

## Finding

Take \(\varphi=(1+\sqrt5)/2\), and the six vectors
\[
\begin{aligned}
v_1&=(0,1,\varphi),&v_2&=(0,-1,\varphi),\\
v_3&=(1,\varphi,0),&v_4&=(-1,\varphi,0),\\
v_5&=(\varphi,0,1),&v_6&=(\varphi,0,-1).
\end{aligned}
\]
The Minkowski sum \(Z=\sum_{i=1}^{6}[0,v_i]\), after translation, is a regular rhombic triacontahedron. With the **unpolarized projection body** \(\Pi Z\), defined by support function \(h_{\Pi Z}(u)=\operatorname{area}_2(Z\mid u^\perp)\) for unit \(u\), we prove
\[
\operatorname{vol}_3(Z)=40+20\sqrt5,\qquad
\operatorname{vol}_3(\Pi Z)=28160+12480\sqrt5,
\]
and therefore
\[
\boxed{\ \frac{\operatorname{vol}_3(\Pi Z)}{\operatorname{vol}_3(Z)^2}=
\frac{48-4\sqrt5}{5}=7.811145618\ldots\ }.
\]
The exact shortfall from the sharp zonoid bound 8 is \(4(\sqrt5-2)/5>0\). Moreover, the projection body has precisely 30 congruent regular square faces, 20 regular hexagonal faces, and 12 regular decagonal faces, with 120 vertices and 180 edges. Up to similarity it is the uniform truncated icosidodecahedron. An exhaustive algebraic classification of **all 455** triple determinants of its 15 generators is part of the finding; see below.

## Assumptions and scope

The geometry is Euclidean in dimension three, with the displayed fixed generator normalization. Segments \([0,v]\) may be translated without changing projection volumes. The projected area is ordinary orthogonal projected area and \(\Pi Z\) is unpolarized (not \((\Pi Z)^\circ\)). The 15 vectors \(c_{ij}=v_i\times v_j\), for \(1\le i<j\le6\), are understood as generators of the centrally symmetric zonotope \(\Pi Z=\sum_{i<j}[-c_{ij},c_{ij}]\). Each claim concerns this canonical fixed polyhedron or its affine images; it does not characterize all six-generator zonotopes. Multiplicities are counted over unordered triples of distinct indexed generators, even if a determinant vanishes.

## Proof

**Zonotope determinant identities.** For vectors \(w_1,\ldots,w_m\in\mathbb R^3\), the volume of \(\sum_j[0,w_j]\) equals \(\sum_{i<j<k}|\det(w_i,w_j,w_k)|\). Orthogonal planar projected area of this sum is \(\sum_{i<j}|u\cdot(w_i\times w_j)|\) for unit \(u\). Thus the projection body is exactly \(\sum_{i<j}[-w_i\times w_j,w_i\times w_j]\), and its volume is \(8\sum_{a<b<c}|\det(c_a,c_b,c_c)|\); factor 8 reflects the doubled segments and must not be dropped.

**Original determinant spectrum.** Write \(r=\sqrt5\). Directly substituting the six displayed vectors and using \(\varphi^2=\varphi+1\), their twenty unordered triple determinants split into exactly ten with magnitude \(1+r\) and ten with magnitude \(3+r\). Therefore
\[
\operatorname{vol}_3(Z)=10(1+r)+10(3+r)=40+20r.
\]

**Projection-body determinant spectrum.** Form the fifteen cross products \(c_{ij}=v_i\times v_j\). Every one has Euclidean length \(1+r\). Exhausting the \(\binom{15}{3}=455\) indexed triples gives this five-level exact spectrum:

| Magnitude \(|\det(c_a,c_b,c_c)|\) | Number of triples |
|:--|--:|
| \(0\) | 70 |
| \(6+2\sqrt5\) | 100 |
| \(8+4\sqrt5\) | 180 |
| \(14+6\sqrt5\) | 100 |
| \(16+8\sqrt5\) | 5 |

Thus \(\operatorname{vol}_3(\Pi Z)=8[100(6+2r)+180(8+4r)+100(14+6r)+5(16+8r)]=28160+12480r\). Dividing by \((40+20r)^2\) and rationalizing yields \((48-4r)/5\), and subtracting from 8 yields \(4(r-2)/5\). All identities are exact in the quadratic number field \(\mathbb Q(\sqrt5)\), not numerical estimates.

**Regular facets and combinatorics.** A facet plane of a three-dimensional zonotope is perpendicular to a pairwise cross product of its generators. Removing parallel repetitions, the 105 generator-pair cross products give exactly 31 unoriented facet-normal lines. Fifteen normal lines have exactly two perpendicular generator directions, ten have exactly three, and six have exactly five. In each two-direction case the two equal-length generators are perpendicular. In each three-direction case pairwise absolute cosine is \(1/2\). In each five-direction case pairwise absolute cosines are exactly among \(\varphi/2\) and \((\varphi-1)/2\), the two chord-angle values of a regular pentagonal direction set. Therefore each corresponding face is a regular \(4\)-, \(6\)-, or \(10\)-gon, respectively, and equal generator lengths make every edge length \(2(1+\sqrt5)\). Each unoriented normal yields two opposite faces, so the facet counts are 30, 20, 12. Summing face incidences gives 180 edges; Euler's relation gives 120 vertices. These are the regular-face metric and incidence data of the uniform truncated icosidodecahedron, establishing the named identification up to similarity.

## Verification

The supplied standalone `rt_projection_checker.py` performs exact symbolic arithmetic with SymPy: it checks the 20 original minors; all 455 projection-body minors and their multiplicities; the projection-body normalization; and all 105 pairwise generator cross products, reduced to exactly 31 normal lines, including each two-, three-, or five-generator angle test and the full face vector. It requires only Python and SymPy and prints `ALL_CHECKS_PASSED` if every assertion holds. Independent numerical convex-hull evaluation with SciPy identified 32 original vertices and 120 projection-body vertices and reproduced both volumes to floating-point tolerance. These are algorithmic diagnostics, not independent mathematical validation; the exact finite enumeration plus the displayed determinant identities is the certificate.

## Relationship to prior work

Saroglou's *On the shape of a convex body with respect to its second projection body* (arXiv:1409.4347, Section 3) gives the general zonotope determinant formulas and the upper inequality \(\operatorname{vol}_3(\Pi K)/\operatorname{vol}_3(K)^2\le8\) for zonoids. The inequality and general volume formulas are **not** claimed as new. Eppstein's *Zonohedra and Zonotopes* lists explicit generators for the rhombic triacontahedron and for the uniform truncated icosidodecahedron separately. The presented result combines these classical inputs into an exact *projection-body identity* and a complete 455-triple determinant spectrum; neither these numerical classifications nor the operator correspondence was located in the inspected texts. The conventional vertex, face, and volume tables for the uniform truncated icosidodecahedron are likewise not themselves asserted as new. A prior study of truncated-octahedron projected volumes addresses a different solid and hence does not imply this specific icosahedral evaluation.

## Limitations

This is a complete finite exact classification for one canonical icosahedrally symmetric zonotope, not a new projection-body inequality or a theorem for all zonohedra. The computation uses a standard volume identity and an explicit classical generator model; the novelty is therefore narrow, consisting of the algebraic spectrum and projection-body correspondence. Historical priority is provisional: a previously indexed but not searchable polyhedral table, or a source treating Coxeter zonotopes under an equivalent name, could already contain the map or exact quotient. Publisher access to the full 2011 paper was incomplete, although a related 2014 full text and Eppstein's full generators article were materially inspected. Independent mathematical audit has not been performed.

## References

1. C. Saroglou, *Volumes of projection bodies of some classes of convex bodies*, 2011, DOI: https://doi.org/10.1112/S0025579311001860.
2. C. Saroglou, *On the shape of a convex body with respect to its second projection body*, arXiv:1409.4347 (first public version September 15, 2014): https://arxiv.org/abs/1409.4347.
3. D. Eppstein, *Zonohedra and Zonotopes*, generator tables: https://ics.uci.edu/~eppstein/junkyard/ukraine/ukraine.html.
4. *Truncated icosidodecahedron*, conventional uniform-polyhedron data: https://en.wikipedia.org/wiki/Truncated_icosidodecahedron.
