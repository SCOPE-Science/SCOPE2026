# Exact Haar silhouette-vertex distribution of the regular icosahedron

## Finding
Let \(I\) be any regular convex Euclidean icosahedron. For a unit vector \(U\) uniform on \(S^2\), orthogonally project \(I\) onto \(U^\perp\), and denote the number of genuine projected polygon vertices by \(N(U)\). Put
\[
a=\arccos(\sqrt5/3),\qquad b=\arccos(1/3).
\]
Then, with probability one,
\[
\begin{aligned}
\Pr\{N=6\}&=10-\frac{15}{\pi}(a+b),\\
\Pr\{N=8\}&=\frac{15}{\pi}(a+2b-\pi),\\
\Pr\{N=10\}&=6-\frac{15b}{\pi}.
\end{aligned}
\]
These are approximately \(0.63840881155934\), \(0.23898946889977\), and \(0.12260171954089\), respectively. In particular, \(\mathbb E[N]=30a/\pi\approx6.96838581596311\).

## Assumptions and scope
The body is the convex hull of the twelve points \((0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\) with \(\varphi=(1+\sqrt5)/2\). The four independent sign choices in each coordinate family give twelve vertices. Direction \(U\) is sampled by normalized sphere area, and \(U\) and \(-U\) yield the same projection. The statement concerns orthogonal projected shadows, not planes intersecting the icosahedron. If \(U\) is orthogonal to a face normal, the projected outline can undergo a combinatorial transition; the finite exceptional great-circle set is excluded in the almost-sure claim.

## Proof
**Face-normal decomposition.** Each of the 20 equilateral triangular facets has outward normal proportional to the sum of its three vertices. Facets occur in antipodal pairs, giving exactly ten unoriented normal axes \(B_1,\ldots,B_{10}\). The ten associated great circles \(\langle B_i,U\rangle=0\) partition the unit sphere into chambers. Each chamber is the intersection of ten open hemispheres and is therefore connected and spherically convex. At generic \(U\), an icosahedron edge belongs to the projected polygon boundary precisely when the outward normals of its two incident faces have opposing signs against \(U\). Indeed these are the front/back faces of that edge; convexity prevents an occluded contour segment. The 30-edge sign count is constant on a chamber and equals \(N(U)\).

**Exact chamber certificate.** Work in the ring \(\mathbb Z[\varphi]\), using the relation \(\varphi^2=\varphi+1\). All facet sums, cross products, dot products, and their signs can be computed exactly in this ring; see the complete standalone `verify.py`. All 45 pairs of distinct normal great circles meet in two antipodal points, and no third great circle passes through either intersection point. Each intersection belongs to four adjacent chambers. For each pair \(i<j\), the two cross-product rays \(\pm (B_i\times B_j)\), together with the four possible signs at the zero entries \(i,j\), enumerate exactly the 360 chamber-corner incidences. They identify exactly 92 distinct nonempty sign chambers. For each chamber, the certificate counts its corner incidences, their two signed facet normals, and the silhouette edges from the original 20-facet/30-edge adjacency data. The exhaustive exact outcomes are:

| Projected vertices | Chambers | Chamber corners | Interior-angle multiplicities |
|---|---:|---:|---|
| 6 | 20 | 6 | three \(\pi-a\), three \(\pi-b\) |
| 8 | 60 | 3 | one \(a\), two \(b\) |
| 10 | 12 | 5 | five \(\pi-b\) |

No numerical threshold controls the exhaustive classification: all incidence and angle-type tests are exact ring computations. The signed normal angles have absolute cosines \(1/3\) or \(\sqrt5/3\), verified symbolically by the certificate.

**Spherical areas.** For a convex spherical \(q\)-gon with interior angles \(\gamma_1,\ldots,\gamma_q\), Girard's formula yields area \(\sum_i\gamma_i-(q-2)\pi\). The six-corner cells therefore have area \(2\pi-3(a+b)\), the three-corner cells area \(a+2b-\pi\), and the five-corner cells area \(2\pi-5b\). Multiplying each area by its chamber count and dividing by the full sphere area \(4\pi\) gives the displayed probabilities. The three total areas sum exactly to \(4\pi\), so this is exhaustive. Substituting them in \(6p_6+8p_8+10p_{10}\) simplifies to \(30a/\pi\), independently consistent with the classical single-edge silhouette probability \(a/\pi\) times the 30 edges.

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker builds all twelve icosahedral vertices in exact algebraic integer pairs, reconstructs 30 edges and 20 facets, forms ten antipodal facet-normal axes, and exhaustively enumerates all 360 great-circle intersection/chamber incidences without floating-point sign decisions. It checks the exact list of three chamber profiles and the angle identities. Finally, a separately implemented direct orthogonal-projection convex-hull experiment on 36,000 sampled normal directions compares empirical projected vertex counts against the three exact probabilities; these finite samples are supplementary, not the basis of the proof. The full exact checker returned `EXACT_ICOSAHEDRON_SHADOW_TYPE_CERTIFICATE_OK`; direct geometry returned `INDEPENDENT_ORTHOGONAL_PROJECTION_HULL_TEST_OK`.

## Relationship to prior work
Glisse and Lazard (2007) study the average silhouette complexity of classes of polyhedra and recall the general per-edge dihedral-angle expectation formula. That formula implies the expectation computed here but not the three-point distribution or 92-chamber spherical arrangement. Kettner and Welzl (1996/1997) study contour edges and average silhouette sizes, including algorithms and experiments; their general results do not by themselves imply the claimed distribution, although their full report was not completely inspectable for a specific icosahedron table. Glisse, Lazard, Michel, and Pouget (2013/2016) treat Poisson-generated random polytopes and worst-direction silhouette size rather than uniformly random directions for one fixed regular solid. The law for a central *section* of the regular icosahedron concerns a different geometric operation and does not imply this projected-shadow law.

## Limitations
The claim is specific to orthogonal projection of the convex regular icosahedron, not arbitrary viewpoints at finite distance, nonconvex immersed surfaces, or central slices. The exact enumeration is a finite, executable symbolic proof; the empirical comparison is not an infinite proof. Prior-art priority remains provisional because not every historical report is fully accessible. Independent mathematical audit has not been performed.

## References
Glisse, M. and Lazard, S., *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, initial public submission 2007-02-14, https://arxiv.org/abs/cs/0702087.

Kettner, L. and Welzl, E., *Contour Edge Analysis for Polyhedron Projections*, ETH Zürich report, December 1996, https://www.research-collection.ethz.ch/bitstreams/e71a7fd9-7bc0-4217-ac29-5b3180921d84/download (bibliographic year/month; no exact first-public day verified).

Glisse, M., Lazard, S., Michel, J., and Pouget, M., *Silhouette of a random polytope*, Journal of Computational Geometry 7(1) (2016), 86–99, https://doi.org/10.20382/jocg.v7i1a5 (earlier 2013 technical-report version).
