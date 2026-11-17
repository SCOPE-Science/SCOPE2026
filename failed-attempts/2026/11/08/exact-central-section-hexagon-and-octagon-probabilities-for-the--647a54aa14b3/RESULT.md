# Exact central-section hexagon and octagon probabilities for the rhombic dodecahedron

## Finding

Let \(K\) be the rhombic dodecahedron with six axial vertices and eight cubic vertices,
\[
K=\operatorname{conv}\left(\{\pm e_1,\pm e_2,\pm e_3\}\cup
\left\{\left(\frac{s_1}{2},\frac{s_2}{2},\frac{s_3}{2}\right):s_i\in\{-1,1\}\right\}\right).
\]
Choose a Haar-uniform unit normal \(u\in S^2\) and intersect \(K\) with the plane \(u^\perp\) through the center. Write \(N(u)\) for the number of vertices of the resulting polygon. Except on a finite union of great circles, \(N(u)\in\{6,8\}\), with the exact rule
\[
N(u)=6\quad\Longleftrightarrow\quad
\max\{|u_1|,|u_2|,|u_3|\}<
\text{the sum of the other two coordinate magnitudes}.
\]
Set \(\alpha=\arccos(1/3)\). The complete probability law is
\[
\Pr(N=6)=\frac{6\alpha}{\pi}-2=0.35095931218\ldots,
\qquad
\Pr(N=8)=3-\frac{6\alpha}{\pi}=0.64904068782\ldots.
\]
Equivalently, the normal sphere is subdivided into eight congruent central spherical triangles for hexagon sections and twenty-four congruent corner spherical triangles for octagon sections. There is no generic quadrilateral section.

## Assumptions and scope

The solid is the full-dimensional, centrally symmetric, Euclidean rhombic dodecahedron in the coordinates above; uniformity is spherical area measure on unit normals, not uniform offsets of planes or uniform points inside the solid. The normal vectors \(u\) and \(-u\) specify the same plane, but spherical and unoriented-plane probabilities agree by antipodal symmetry. The exceptional directions satisfy one of \(u_i=0\) or \(\pm u_1\pm u_2\pm u_3=0\), which have spherical measure zero; their non-generic contact multiplicities do not enter the law.

The polyhedron has an additional halfspace description
\[
K=\left\{x\in\mathbb R^3:
|x_i|+|x_j|\le1\quad\text{for every }1\le i<j\le3\right\}.
\]
It has fourteen vertices, twelve rhombic facets, and twenty-four edges. Every edge joins an axial vertex \(\pm e_i\) to a cubic vertex \((s_1,s_2,s_3)/2\) with the corresponding sign \(s_i\).

## Proof

**Step 1 (edge crossings and the exact type criterion).** For a generic normal, every vertex of the planar section is the intersection of the central plane with exactly one polyhedron edge. Such an edge crosses if and only if its endpoint scalar products with \(u\) have opposite signs. Because the vertex and edge set is invariant under signed coordinate permutations, one may take \(u=(a,b,c)\) with \(a>b>c>0\), excluding the walls \(a=b+c\) and permutation coincidences. The latter coincidence planes are not needed for the classification, since the conclusions extend across them by continuity wherever no vertex lies in the plane.

The three positive axial vertices have positive scalar products. For each cubic vertex with sign triple, its scalar-product sign is that of \(\pm a\pm b\pm c\), and it has three incident edges leading to the three sign-matched axial vertices. If \(a<b+c\), the signs for the eight cubic vertices in the order
\[
(+++),(++-),(+-+),(+--),(-++),(-+-),(--+),(---)
\]
are respectively
\[
+,+,+,-,+,-,-,-.
\]
The corresponding numbers of crossing incident edges are \(0,1,1,1,1,1,1,0\), totaling six. If \(a>b+c\), only the \((+--)\) and \((-++)\) cubic signs reverse; each then contributes two rather than one crossing edge, giving eight crossings. Signed coordinate permutations cover all generic normals, proving the dichotomy and the strict triangle-inequality criterion.

**Step 2 (geometric partition of normals).** The sign walls consist of the three coordinate great circles and the four distinct diagonal great circles represented by \(\pm u_1\pm u_2\pm u_3=0\), with opposite sign patterns identifying the same circle. In every open octant there is one central region where the positive coordinate magnitudes satisfy all three strict triangle inequalities. This region is the spherical triangle with vertices
\[
\frac{(1,1,0)}{\sqrt2},\quad
\frac{(1,0,1)}{\sqrt2},\quad
\frac{(0,1,1)}{\sqrt2}
\]
after the relevant coordinate sign changes. The complementary region of the octant is the disjoint union of three corner spherical triangles, on each of which one coordinate magnitude strictly exceeds the other two combined. Thus there are exactly eight central triangles and twenty-four corner triangles, accounting for all but a zero-area set of directions.

**Step 3 (spherical excess and normalization).** Each pair of central-triangle vertices has inner product \(1/2\), so every side has spherical length \(\pi/3\). The spherical cosine rule gives
\[
\cos\alpha=\frac{\cos(\pi/3)-\cos^2(\pi/3)}{\sin^2(\pi/3)}=\frac13.
\]
By Girard's spherical-excess formula, each central spherical triangle has area \(3\alpha-\pi\). The eight central regions therefore have total area \(8(3\alpha-\pi)\). Dividing by the unit sphere's total area \(4\pi\) yields \(\Pr(N=6)=6\alpha/\pi-2\); taking the complement gives \(\Pr(N=8)=3-6\alpha/\pi\). In particular the twenty-four corner triangles each have area \(\pi/2-\alpha\), and
\[
8(3\alpha-\pi)+24(\pi/2-\alpha)=4\pi.
\]
The classification and probability formulas follow.

## Verification

The included `verify_fcc_sections.py` uses Python 3 standard-library arithmetic to enumerate all feasible intersections of triples of supporting facet planes, thus independently certify the complete fourteen-vertex list; it then reconstructs the twelve facets from their supporting inequalities, derives the twenty-four edges from facet intersections, and verify the exact crossing count for all forty-eight signed-coordinate permutations of each of two interior representatives (ninety-six tests). It independently checks the thirty-two spherical-cell count and the exact area normalization, then compares the closed-form probability with 240,000 isotropically sampled directions. The recorded result was

`VERIFY_OK vertices=14 facets=12 edges=24 exact_symmetry_cases=96 spherical_regions=32 hexagon_regions=8 octagon_regions=24 sampled_normals=240000 observed_hexagon=0.351720833 formula_hexagon=0.350959312 error=0.000761521`

The full proof uses the symbolic classification and spherical excess; finite sampling alone is not evidence for the all-direction assertion. Run the verifier with `python3 verify_fcc_sections.py`.

## Relationship to prior work

Socha (1988) studies the distribution of **angles** seen where isotropically sampled affine planes intersect polyhedra. His Figure 2 explicitly includes a rhombic dodecahedron. The quantity is a plane-corner-angle density for **random offsets**, rather than the vertex count of Haar-uniform **central** sections, and the article does not give the present two-atom polygon-type law. The polyhedron's combinatorial data and its relation to the face-centered-cubic (FCC) Voronoi cell are classical. Hausel, Makai and Szűcs (2000) investigate inscribed cubes and covering by rhombic dodecahedra; Gabbrielli, Jiao and Torquato (2012) investigate FCC-related three-dimensional tessellations; neither establishes the central-section orientation law. The claim here is only the exact classification and two probabilities for this fixed solid—not a new characterization of the solid, nor a universal formula for all polyhedra.

## Limitations

The law is specific to center-passing planes of the rhombic dodecahedron. Uniform-offset stereology, noncentral planes, deformed cells, conditional section areas and section perimeters are not treated. No statistical estimator or numerical stability guarantee is claimed. Historical priority may be affected by older solid-geometry sources not fully accessible in electronic form, notably Alsina and Nelsen's 2015 plane-sections chapter; the available index and contents do not resolve whether a comparable probability calculation appears there. Independent mathematical validation has not been performed.

## References

1. P. Socha, "Random Plane Section of a Polyhedron," *Acta Stereologica* **7**(1) (1988), pp. 41–46. Full article: https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf
2. T. Hausel, E. Makai Jr., A. Szűcs, "Inscribing cubes and covering by rhombic dodecahedra via equivariant topology," *Mathematika* **47** (2000), 371–397, first published 1 December 2000. https://doi.org/10.1112/S0025579300015965
3. R. Gabbrielli, Y. Jiao and S. Torquato, "Families of tessellations of space by elementary polyhedra via retessellations of face-centered-cubic and related tilings," *Physical Review E* **86** (2012), 041141, published 22 October 2012. https://doi.org/10.1103/PhysRevE.86.041141
4. C. Alsina and R. B. Nelsen, *A Mathematical Space Odyssey: Solid Geometry in the 21st Century*, MAA Press (2015), chapter 5, "Plane sections"; contents available at https://books.google.com/books?id=2F_0DwAAQBAJ
5. "Kepler and the Rhombic Dodecahedron," *Mathematical Association of America*, geometric background and combinatorial counts. https://old.maa.org/press/periodicals/convergence/kepler-and-the-rhombic-dodecahedron-honeycombs-and-the-rhombic-dodecahedron
