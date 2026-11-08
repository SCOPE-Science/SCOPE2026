# Almost-sure section-vertex rigidity in the cube–octahedron interpolation

## Finding
For each real parameter \(t\in[1,3]\), put
\[
K_t=[-1,1]^3\cap\{(x,y,z):|x|+|y|+|z|\le t\}.
\]
For a uniformly random unit normal \(u\), let \(N_t(u)\) count vertices in the central planar section \(K_t\cap u^\perp\). The number \(N_t(u)\) is almost surely constant **if and only if** \(t=1\) or \(t=2\). In the first case it is six almost surely; in the second case it is eight almost surely.

The statement is stronger than an isolated cuboctahedron count: for every \(1<t<2\), hexagonal and octagonal sections each occur for an open set of normal directions; for every \(2<t\le3\), hexagonal and quadrilateral sections each occur for an open set of normal directions. Thus the two rigid parameters are precisely the octahedral endpoint and the interior cuboctahedron.

## Assumptions and scope
All sections are by planes through the origin, and normals have the rotationally invariant (Haar) distribution. A *generic* normal is one for which no vertex of \(K_t\) lies in the plane. For a fixed three-dimensional polytope the nongeneric normals lie on finitely many great circles and have measure zero. For generic normals, each section vertex lies in the relative interior of a polytope edge whose endpoints have opposite signs under the normal; every such sign-changing edge produces exactly one section vertex.

The parameter \(t=1\) gives the octahedron with vertices \(\pm e_i\); \(t=2\) gives the cuboctahedron with vertices the signed coordinate permutations of \((1,1,0)\); and \(t=3\) gives the cube. The assertion concerns this entire family, without identifying all section counts at nonrigid parameters.

## Proof
**Step 1 (octahedral endpoint).** At \(t=1\), the graph of the octahedron connects each vertex to all nonantipodal vertices. For a generic normal with nonzero coordinates, exactly one of \(e_i\), \(-e_i\) is positive, giving three positive and three negative vertices. Of their nine opposite-sign pairs, exactly three are antipodal nonedges. Hence there are \(9-3=6\) sign-changing edges, and the section is a hexagon.

**Step 2 (cuboctahedral rigidity).** At \(t=2\), the twenty-four edges of the cuboctahedron are partitioned into the four boundary edges of each of the six square faces \(x_i=\pm1\); each edge belongs to exactly one square face (and one triangular face). Outside the measure-zero set where a coordinate is zero or two coordinate magnitudes coincide, signed coordinate permutations reduce the normal to \(u_1>u_2>u_3>0\). In the two squares \(x_1=\pm1\), all four vertex signs agree, so there are no crossing edges. In each square \(x_2=\pm1\), three signs agree and one differs, giving two crossing boundary edges per square. In each square \(x_3=\pm1\), the four signs form two adjacent positives and two adjacent negatives, giving two crossing edges per square. The six squares therefore contribute \(0+4+4=8\) distinct crossings, hence eight section vertices. Equalities among coordinate magnitudes or zero coordinates are exceptional measure-zero directions.

**Step 3 (persistent hexagons away from the cuboctahedron).** Set the normal proportional to \((1,1,1)\). On the plane \(x+y+z=0\), the elementary inequality \(\|x\|_\infty\le\|x\|_1/2\) holds (where \(x\) now denotes the three-coordinate vector). For \(t<2\), every point in the octahedral slice \(\|x\|_1\le t\) satisfies \(\|x\|_\infty\le t/2<1\), so the cube inequalities are inactive and the section is the hexagon with vertices obtained by permuting \((t/2,-t/2,0)\). For \(t>2\), the cube's diagonal section is the hexagon with vertices obtained by permuting \((1,-1,0)\); it satisfies \(\|x\|_1\le2<t\), so the octahedral inequality is inactive. In either strict regime the plane avoids vertices of the three-dimensional polytope; the hexagonal combinatorial type is therefore stable on a neighborhood of the normal. The same argument yields a hexagon at \(t=1\), already treated.

**Step 4 (persistent octagons before the cuboctahedron).** Fix \(1<t<2\) and choose \(0<\varepsilon<\min(1,t-1)\). With normal proportional to \((1,\varepsilon,0)\), the plane is \(x=-\varepsilon y\). Its section is affinely identified with
\[
|y|\le1,\qquad |z|\le1,\qquad (1+\varepsilon)|y|+|z|\le t.
\]
Indeed \(|x|=\varepsilon|y|<1\) makes the remaining cube inequality redundant. Each of the four square corners is truncated, since \(2+\varepsilon>t\), while the midpoint of each square side is strictly inside the strip constraint, since \(1+\varepsilon<t\) and \(1<t\). There are therefore exactly eight vertices, with all defining inequalities strict at nonincident vertices. The octagonal type persists in an open neighborhood of the normal.

**Step 5 (persistent quadrilaterals after the cuboctahedron).** Fix \(2<t\le3\) and \(0<\varepsilon<\min(1,t-2)\). On \(x=-\varepsilon y\), every point of the cube slice satisfies \(|x|+|y|+|z|\le2+\varepsilon<t\). Hence the octahedral constraint is inactive and the section is precisely the square \(|y|,|z|\le1\), with four vertices. Again, the strict margin ensures persistence under small perturbations of the normal.

**Step 6 (probability).** A nonempty open subset of the normal sphere has positive Haar measure. Thus each nonrigid parameter supports two different section-vertex counts with positive probability, while Steps 1–2 prove almost-sure constancy at precisely \(t=1\) and \(t=2\). This proves the theorem.

## Verification
The independent finite rational checker `cuboctahedron_section_checker.py` constructs the planar inequalities induced by all fourteen supporting halfspaces, enumerates pairwise line intersections using exact fractions, filters infeasible points, and computes a convex hull without using the polytope-edge crossing argument. It verifies sample directions for nine parameter values and 1,915 additional rational normal/parameter cases. Run with `python3 cuboctahedron_section_checker.py`; its success sentinel is `OCTAGONAL_RIGIDITY_EXACT_RATIONAL_CHECK_OK 1915`. These are finite consistency checks only. The all-parameter conclusion rests on the six analytic proof steps above.

## Relationship to prior work
The one-parameter cube-to-octahedron truncation via cuboctahedra was investigated for particle packing and phase behavior by Gantapara et al. (2013, 2014) and in a broader polyhedral shape-space study by Chen et al. (2013). Those sources treat forward shape families and packing transitions, not the central-section vertex-count rigidity question.

Published research records on the same intersection family establish other invariants, such as illumination number and maximal inscribed tetrahedral volume; they do not, on the statements inspected, imply the present almost-sure classification. Other published records give random central-section laws for rectangular boxes, the regular icosahedron, and the four-cube. Those are different sections or objects. This is a best-knowledge originality assessment, not a global priority certificate.

## Limitations
This theorem neither determines the full probability distribution at nonrigid parameters nor characterizes all three-dimensional polytopes with almost-surely constant section size. Exceptional normals can produce fewer vertices even at the rigid parameters. Related older archival literature could remain unindexed or unnoticed, and independent priority review has not been performed.

## References
1. A. P. Gantapara, J. de Graaf, R. van Roij, and M. Dijkstra, “Phase Diagram and Structural Diversity of a Family of Truncated Cubes: Degenerate Close-Packed Structures and Vacancy-Rich States,” *Physical Review Letters* 111, 015501 (published July 1, 2013), DOI: https://doi.org/10.1103/PhysRevLett.111.015501.
2. A. P. Gantapara et al., “Phase Behavior of a Family of Truncated Hard Cubes,” arXiv:1412.2597 (first submitted December 8, 2014), https://arxiv.org/abs/1412.2597.
3. E. R. Chen, D. Klotsa, M. Engel, P. F. Damasceno, and S. C. Glotzer, “Complexity in surfaces of densest packings for families of polyhedra,” arXiv:1309.2662 (first submitted September 10, 2013), https://arxiv.org/abs/1309.2662.
