# Exact Haar polygon-type law for central sections of the regular truncated octahedron

## Finding

**Theorem.** Let \(K\subset\mathbb R^3\) be the regular truncated octahedron with vertices given by all distinct signed coordinate permutations of \((0,1,2)\). Let \(u\) be a Haar-uniform unit vector on \(S^2\), and let \(N(u)\) count vertices of the planar convex polygon \(K\cap u^\perp\). Then almost surely \(N\in\{6,8,10\}\), and each event has strictly positive probability. Set
\[
U=2\arctan\frac{1}{\sqrt{105}+2\sqrt{21}+10+4\sqrt5},\quad
V=2\arctan\frac{1}{\sqrt{126}+4\sqrt6+11+2\sqrt{21}},
\]
\[
W=2\arctan\frac{2}{3\sqrt{126}+33+7\sqrt{21}+13\sqrt6}.
\]
The exact law is
\[
\boxed{\Pr(N=6)=1-\frac{12(U+V+W)}\pi,\quad
\Pr(N=8)=\frac{12(U+W)}\pi,\quad
\Pr(N=10)=\frac{12V}\pi.}
\]
Numerically, these probabilities are, respectively, approximately \(0.498450689918\), \(0.316108855580\), and \(0.185440454502\).

## Assumptions and scope

The sampling measure is uniform **orientation** among planes through the center, not uniform translation among all intersecting planes. The unit normals \(u\) and \(-u\) define the same plane. The polyhedron is fixed up to similarity; the numbers of vertices of intersections are unchanged by scale. For exceptional normals passing through an original vertex, the usual generic section-edge intersection count may change, but all exceptional orientations form finitely many great circles and have measure zero.

## Proof

**1. Polyhedron and edge-crossing rule.** The convex hull of the 24 signed permutations of \((0,1,2)\) has exactly 14 facets, described by \(\pm x_i\le 2\), for \(1\le i\le3\), and \(\pm x_1\pm x_2\pm x_3\le3\) for all eight sign choices. Its 36 edges are exactly the vertex pairs whose squared Euclidean separation is \(2\), as can be checked directly using these facet inequalities; every vertex has three incident edges. For any generic normal \(u\), each edge crosses the plane exactly when the dot products of its endpoints with \(u\) have opposite signs. A generic plane section is a convex polygon whose vertices are precisely these edge crossings. Thus the section vertex count equals
\[
N(u)=\#\{\{v,w\}\in E(K):(u\cdot v)(u\cdot w)<0\}.
\]

**2. Complete normal-chamber classification.** Signed coordinate permutations of \(u\) preserve \(N(u)\), so reduce to the fundamental spherical chamber \(x\ge y\ge z\ge0\), and normalize nonexceptional directions to \(u=(1,y,z)\), with \(0<z<y<1\). Every original vertex has coordinates \((0,\pm1,\pm2)\) in some order. An interior zero of the signed dot product is therefore possible only on \(y=1/2\), \(z=y/2\), or \(z=1/2\). These three lines partition the fundamental chamber into the following five connected open regions. The number shown in the right column results from the complete 36-edge crossing rule above; a rational witness for each chamber is provided, so the finite sign test and absence of additional separating lines establish the count *throughout* each region.

| Region | Normal inequalities, with \(0<z<y<1\) | Rational witness \((y,z)\) | \(N\) |
| --- | --- | --- | ---: |
| I | \(y<1/2,\ z<y/2\) | \((1/4,1/16)\) | 8 |
| II | \(y<1/2,\ y/2<z<y\) | \((1/4,3/16)\) | 10 |
| III | \(y>1/2,\ z<y/2\) | \((3/4,1/8)\) | 6 |
| IV | \(y>1/2,\ y/2<z<1/2\) | \((3/4,7/16)\) | 8 |
| V | \(y>1/2,\ z>1/2\) | \((3/4,5/8)\) | 6 |

The fundamental chamber has spherical area \(4\pi/48=\pi/12\). Denote its indicated boundary rays by \(A=(1,0,0)\), \(E=(2,1,0)\), \(B=(4,2,1)\), \(C=(2,1,1)\), \(D=(2,2,1)\), \(F=(1,1,0)\) and \(Q=(1,1,1)\). The regions I, II, IV are spherical triangles \(AEB\), \(ABC\), \(BCD\), respectively; the other two regions are the complementary quadrilateral \(EFDB\) and triangle \(CDQ\). Hence regions I and IV produce octagons, region II decagons, and their complement hexagons.

**3. Exact spherical areas.** For three vectors \(a,b,c\) spanning a positively oriented spherical triangle of area below \(2\pi\), its area is
\[
\Omega(a,b,c)=2\arctan\frac{|\det(a,b,c)|}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(b\cdot c)\|a\|+(c\cdot a)\|b\|}.
\]
Substitution gives \(\Omega(A,E,B)=U\), \(\Omega(A,B,C)=V\), \(\Omega(B,C,D)=W\), with the radicals in the theorem. Multiplying by the 48 congruent signed-permutation chambers and dividing by \(4\pi\) gives \(12/\pi\) times the relevant fundamental-chamber area. The formulas for \(\Pr(N=8)\) and \(\Pr(N=10)\) follow. Complementation gives \(\Pr(N=6)\). Each relevant region has positive area, so each probability is positive. This completes the proof.

## Verification

A standalone Python 3 standard-library script, `verify_truncated_octahedron.py`, independently enumerates all 24 vertices and 36 edges, checks the 14 defining facets, tests exact rational witnesses in each chamber both by edge sign crossings and by exact edge-plane intersection points, evaluates the three independent solid-angle formulas, and compares the areas with direct one-dimensional spherical Jacobian quadratures. It also checks 180,000 independently generated random orientation normals against the complete predicted distribution. Run with `python3 verify_truncated_octahedron.py`.

The analytical normal-chamber partition, finite exhaustive edge list and exact solid-angle identity—not the Monte Carlo sample—prove the stated all-orientation law.

## Relationship to prior work

Random polyhedral-section methods have a substantial classical literature. Socha (1988) determines distributions of individual observed section angles for random affine planes through model polyhedra, including a Kelvin-type tetrakaidecahedron; its investigated statistic and sampling scheme differ from the exact *central* polygon-count law here. Paul (1981) reports numerical sectional-area frequency distributions for truncated octahedra; the full article was not available for inspection, so its detailed numerical outputs remain a priority risk. Ferraro and Zaninetti (2011) calculate radius and area distributions of random Voronoi sections, using spherical approximations; their published full text does not evaluate the present section vertex-count distribution. Ohser and Mücklich (1995) develop size/shape stereological reconstruction for ensembles of prisms and random polyhedra, not this exact three-value law. Related exact Haar central-section laws for regular icosahedra, rectangular boxes and higher-dimensional cubes concern other convex bodies and do not imply the formula for this regular truncated octahedron.

## Limitations

The theorem concerns the symmetric regular truncated octahedron only, not deformations or individual random Poisson-Voronoi cells. It uses exact Haar-uniform central planes, not randomly translated planes. No sampling-error confidence intervals or statistical stability theorem are asserted. Historical priority cannot be certified without inspection of all older relevant full texts, especially Paul (1981). Verification experiments have finite scope and cannot replace the geometric proof.

## References

1. M. Ferraro and L. Zaninetti, “Statistics of cross sections of Voronoi tessellations,” *Physical Review E* **84** (2011), 041107, first published 2011-10-07. https://doi.org/10.1103/PhysRevE.84.041107.
2. P. Socha, “Random plane section of a polyhedron,” *Acta Stereologica* **7** (1988), 41–46. https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf.
3. J. L. Paul, “Distribution curves of sectional areas through some families of convex particles,” *Journal of Microscopy* **122** (1981), 165–172. https://doi.org/10.1111/j.1365-2818.1981.tb01255.x.
4. J. Ohser and F. Mücklich, “Stereology for some classes of polyhedrons,” *Advances in Applied Probability* **27** (1995), 384–396. https://doi.org/10.2307/1427832.
