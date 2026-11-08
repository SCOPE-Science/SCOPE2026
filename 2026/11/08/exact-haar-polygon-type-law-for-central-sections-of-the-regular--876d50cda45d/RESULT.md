# Exact Haar polygon-type law for central sections of the regular truncated icosahedron

## Finding
Let \(P\) be the regular truncated icosahedron (the conventional soccer-ball solid) and let \(H=n^\perp\), with \(n\) a uniformly distributed unit vector. Almost surely \(P\cap H\) is a polygon with exactly one of the five numbers of sides \(10,12,14,16,18\). The complete distribution, to the displayed precision, is:

| Number of sides | Probability (numerical evaluation of exact finite angle sums) |
| ---: | ---: |
| 10 | 0.48587214526399 |
| 12 | 0.29341082662371 |
| 14 | 0.16522498337204 |
| 16 | 0.02546740394350 |
| 18 | 0.03002464079675 |

All five probabilities are strictly positive. **Exactness means the finite algebraic-arctangent formulas below, not that the printed decimals are rational or certified decimal intervals.** In particular, an 18-gon is slightly more probable than a 16-gon.

## Assumptions and scope
Set \(\varphi=(1+\sqrt5)/2\). Use the twelve icosahedral vertices \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), and \((\pm\varphi,0,\pm1)\), with independent signs. If \(v_i,v_j\) are joined by an original icosahedral edge, the sixty vertices of the truncated solid are \((2v_i+v_j)/3\) for the sixty directed edges \((i,j)\). A common factor \(1/3\) does not affect the polygon-type law. There are thirty original edges, twenty original triangular faces and ninety truncated edges. Uniformity is Haar measure on unoriented two-planes through the center, equivalently uniform area on the normal sphere modulo antipodes. It is **not** the invariant Crofton measure on affine planes meeting \(P\).

## Proof
**(1) Reduction to edge signs.** Outside the finite union of great circles perpendicular to truncated vertices, the plane \(n^\perp\) meets a truncated edge \((w_i,w_j)\) in its relative interior exactly when \((n\cdot w_i)(n\cdot w_j)<0\). Each such crossing gives one polygon vertex. Thus the side count equals the total number of opposite-sign endpoint pairs among all ninety edges, and is constant on each region of the corresponding great-circle arrangement.

**(2) Exact symmetry chamber and its arrangement.** The full icosahedral reflection group acts by 120 spherical chambers. A fundamental chamber is the spherical triangle whose vertices point along one original icosahedron vertex \(v_a\), one adjacent edge midpoint direction \(v_a+v_b\), and the adjacent face-center direction \(v_a+v_b+v_c\). It has spherical area \(\pi/30\). The sixty truncated vertex vectors determine thirty unoriented perpendicular great circles. Exactly seven of them intersect the interior of this fundamental triangle, by exact sign comparisons in \(\mathbb Z[\varphi]\). Their arrangement has twelve positive-area cells, as established exhaustively by the attached stand-alone certificate.

**(3) Complete cell list.** Encode the signs of the seven active hyperplanes in their deterministic certificate order. The following is the full list of strictly feasible patterns, together with their section side counts and numbers of extreme spherical rays; all other 116 of the 128 sign patterns have no positive-area intersection with the fundamental chamber.

| Pattern | Sides | Extreme rays |
| --- | ---: | ---: |
| `-++++--` | 10 | 4 |
| `+-+++--` | 10 | 3 |
| `+-+++++` | 10 | 3 |
| `--+++--` | 12 | 4 |
| `-+-++--` | 12 | 3 |
| `-++-+--` | 12 | 3 |
| `+-+++-+` | 12 | 3 |
| `---++--` | 14 | 4 |
| `--+++-+` | 14 | 3 |
| `-+--+--` | 14 | 4 |
| `----+--` | 16 | 3 |
| `-------` | 18 | 3 |

For each signed cone, every possible extreme ray is obtained by intersecting two of its ten boundary planes; sign feasibility and polygon side counts are tested exactly in \(\mathbb Z[\varphi]\). The certificate checks all 128 patterns, counts the 12 nonempty full-dimensional regions and verifies 3, 4, 3, 1 and 1 regions of types 10, 12, 14, 16 and 18 respectively. The full-dimensionality tests use strict exact inequalities for a sum of extreme rays, not just a nonempty boundary. Degenerate normals lie in finitely many great circles and therefore have zero Haar measure.

**(4) Exact probability formulas.** Each region \(C\) has an explicitly reconstructible cyclic list of algebraic extreme rays \(r_1,\ldots,r_m\), from its two-plane intersections and sign constraints. Normalize them to unit vectors \(u_i=r_i/\|r_i\|\) and define the exact spherical triangle area
\[
\Omega(u,v,w)=2\operatorname{atan2}\!\bigl(|\det(u,v,w)|,\,1+u\cdot v+v\cdot w+w\cdot u\bigr).
\]
Its exact area is \(\mathcal A(C)=\sum_{j=2}^{m-1}\Omega(u_1,u_j,u_{j+1})\). For \(k\in\{10,12,14,16,18\}\), the **exact** probability is therefore
\[
\boxed{\Pr\{\#\operatorname{vertices}(P\cap H)=k\}=\frac{30}{\pi}\sum_{C:\,\#\mathrm{sides}(C)=k}\mathcal A(C).}
\]
Every ray entering this finite expression is specified algebraically and without optimization by the accompanying certificate, so this is a finite exact arctangent-sum value. Evaluating the sums gives the table above. Their total spherical area is \(\pi/30\), and hence the probabilities total one.

## Verification
Run `python3 trunc_icosa_exact_certificate.py`. It uses only the Python standard library. All incidences, comparisons, cone feasibility and type counts are computed using exact integers representing elements of \(\mathbb Z[\varphi]\). Area evaluation, angle sums and displayed decimal values use floating-point functions, but their defining expressions are mathematically exact as specified above. The program prints `EXACT_CERTIFICATE_OK`, the twelve chamber sign patterns and normalized law, and checks their summed area against \(\pi/30\).

Run `python3 trunc_icosa_independent_check.py` with NumPy and SciPy installed. It independently assembles the truncated icosahedron geometrically, samples 250000 uniform directions, and checks 100 planar section convex hulls against edge-crossing counts. These stochastic tests support, but do not replace, the exhaustive algebraic sign certificate and the area identity.

## Relationship to prior work
Sukiasyan (1982) presents a general combinatorial technique for polygon type probabilities of random **affine** polyhedron sections under the invariant measure on intersecting planes, with examples of pyramids and prisms; the present sampling fixes each plane at the center and uses Haar orientation, and the truncated-icosahedron five-type law is not tabulated there. Geiger and Lengyel (2008) study the same soccer-ball polyhedron and optimize surface roundness moments, without computing the random central-section polygon law. Earlier work gives a full central-section law for the **untruncated** regular icosahedron (only decagons and dodecagons), which does not imply the present five-type law after truncation. General polyhedral section algorithms supply antecedents, not the evaluated result here. Historical priority remains provisional, and unindexed numerical tables could constitute overlap.

## Limitations
The probabilities refer only to a plane through the exact center, not arbitrary affine planes. They count polygon sides, not metric shape, area or perimeter of the random section. They describe the specific uniform one-third truncation of the regular icosahedron; changing the truncation depth can alter the law. Numerical values are approximations of finite exact angle formulas, not rigorous rational enclosures. The proposed priority assessment is not an independent audit.

## References
- Adél Geiger and András Lengyel, *On the Roundness of Polyhedra for Soccer Ball Design*, International Journal of Space Structures **23** (2008), 133–142, doi:10.1260/026635108786260992; first public online 2008-09-01. Public author-uploaded text: https://www.researchgate.net/publication/239433350_On_the_Roundness_of_Polyhedra_for_Soccer_Ball_Design .
- G. S. Sukiasyan, *On random sections of polyhedra*, Doklady Akademii Nauk SSSR **263** (1982), 809–812, MathNet identifier `dan45193`, https://www.mathnet.ru/eng/dan45193 .
- M. Ferraro and L. Zaninetti, *Statistics of cross sections of Voronoi tessellations*, Physical Review E **84** (2011), 041107, doi:10.1103/PhysRevE.84.041107 (background on random-section statistics, different objects and observables).
