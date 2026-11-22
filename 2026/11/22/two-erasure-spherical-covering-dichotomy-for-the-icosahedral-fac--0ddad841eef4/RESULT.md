# Two-erasure spherical covering dichotomy for the icosahedral face-center code

## Finding

Let \(I\subset S^2\) comprise the twelve vertices of a unit-circumradius regular icosahedron, let \(D\subset S^2\) comprise its twenty outward unit face normals (the vertices of the normalized dual dodecahedron), and put \(X=I\cup D\). For a finite nonempty \(Y\subset S^2\), define its covering cosine and radius by
\[
\mu(Y)=\min_{z\in S^2}\max_{y\in Y}z\cdot y,\qquad \rho(Y)=\arccos\mu(Y).
\]
Define the positive algebraic constants
\[
\begin{gathered}
t=1/\sqrt5,\quad u=\sqrt{(5+2\sqrt5)/15},\quad v=\sqrt{(5-2\sqrt5)/15},\\
A=2(1+t),\qquad B=8/3,\qquad C=2(u+v),\\
\gamma=\sqrt{\frac{AB-C^2}{4(A+B-2C)}}=0.768858636428994\ldots.
\end{gathered}
\]
For **every two-element subset** \(E\subset X\), the following exact dichotomy holds:
\[
\boxed{\mu(X\setminus E)=
\begin{cases}
\gamma,&E=\{i,d\},\ i\in I,\ d\in D,\ i\cdot d=u,\\
u,&\text{otherwise}.
\end{cases}}
\]
There are exactly **60 exceptional** pairs, corresponding to the incidences of icosahedral vertices with faces, and **436 ordinary** pairs, out of \(\binom{32}{2}=496\). The respective spherical covering radii are \(\arccos\gamma=39.7484942522\ldots^\circ\) and \(\arccos u=37.3773681406\ldots^\circ\). Every exceptional pair has a **unique** deepest uncovered direction (the outward normal of its new closest supporting quadrilateral). In particular, the full two-erasure covering radius of the code equals \(\arccos\gamma\), while the unpunctured radius is only \(\arccos h\), with
\[
h=\sqrt{\frac{1+\sqrt5/3-2u^2}{3+\sqrt5/3-4u}}=0.922602194543989\ldots.
\]

## Assumptions and scope

All points lie on the Euclidean unit sphere in \(\mathbb R^3\); angular distances are geodesic spherical distances. The sets \(I,D\) use the *same unit circumradius*, not the unequal vertex radii of the conventional Catalan solid. Orient the icosahedron so that \(\varphi=(1+\sqrt5)/2\), \(r=\sqrt{1+\varphi^2}\), and \(I\) is obtained from \((0,\pm1,\pm\varphi)/r\) by cyclic coordinate permutations. Let \(D\) consist of \((\pm1,\pm1,\pm1)/\sqrt3\), together with the cyclic permutations of \((0,\pm\varphi,\pm\varphi^{-1})/\sqrt3\). All independent signs occur. The specified coordinates completely define both orbits and the incidence relation \(i\cdot d=u\).

## Proof

**1. Two overlapping unit-radius covering codes.** The regular icosahedron has twenty triangular faces, with unit outward normals \(D\), all at distance \(u\) from the origin. The regular dual dodecahedron has twelve pentagonal faces, with outward normals \(I\), also at distance \(u\). Consequently, for every \(z\in S^2\),
\[
\max_{i\in I}z\cdot i\ge u,\qquad \max_{d\in D}z\cdot d\ge u.
\]
The four possible mixed inner products are \(u,v,-v,-u\), with \(u\) occurring on precisely sixty vertex–face incidences. For unequal same-orbit sites the inner products are at most \(t=1/\sqrt5\) in \(I\), and at most \(\sqrt5/3\) in \(D\); both are less than \(u\).

**2. All nonexceptional deletions.** If two sites are removed from the same orbit, the other entire orbit still ensures covering cosine at least \(u\). At either deleted site, every remaining site has inner product at most \(u\), and some sites of the opposite orbit attain \(u\); hence the covering cosine is exactly \(u\).

Suppose instead that the removed sites are \(i\in I\) and \(d\in D\), but are nonincident. Their inner product is at most \(v\), and the strict elementary radical inequality
\[
v<2u^2-1=\cos(2\arccos u)
\]
shows that their spherical separation exceeds \(2\arccos u\). If some direction had dot product less than \(u\) with **every surviving site**, the separate \(u\)-covering properties of \(I\) and \(D\) would force this direction to lie within \(\arccos u\) of *both* removed sites. The spherical triangle inequality forbids that. Thus \(\mu\ge u\). At \(z=i\), the remaining sites have maximum dot product exactly \(u\), since \(i\) retains its five incident face normals and all other icosahedral sites give at most \(t\). Hence \(\mu=u\).

**3. A complete facet certificate for an incident deletion.** Icosahedral symmetry is transitive on its sixty vertex–face incidences. Label the twelve icosahedral sites and twenty dodecahedral sites by the signed-coordinate enumeration in `verify.py` (indices \(0,\ldots,11\) and \(12,\ldots,31\)). Choose the incident deletion \(E=\{0,12\}\). The undamaged hull has sixty triangular facets, one icosahedral and two dodecahedral vertices in each. Exactly nine such triangles contain a removed site, leaving fifty-one inherited supporting facets.

A direct signed-coordinate substitution gives precisely three new supporting polygons, with the following ordered vertex labels and outward unit-support distances:

| New supporting face | Ordered vertices | Distance to origin |
|---|---|---|
| Mixed quadrilateral | \((1,2,21,20)\) | \(\gamma\) |
| Dodecahedral quadrilateral | \((16,20,21,27)\) | \(u\) |
| Mixed triangle | \((1,2,22)\) | \(\beta\) |

Here
\[
\beta=\sqrt{\frac{2(1+t)-4u^2}{6+2t-8u}}
=0.828263486752208\ldots.
\]
The new quadrilateral's opposite icosahedral and dodecahedral edges are parallel: the differences of its vertex pairs are respectively \((\varphi^{-1},-\varphi,1)/r\) and \((\varphi^{-1},-\varphi,1)/\sqrt3\). Thus the four vertices are coplanar. Its two pair-sums have Gram matrix \(\left(\begin{smallmatrix}A&C\\C&B\end{smallmatrix}\right)\). The plane has equal dot product with all four unit vertices; solving its two equal-support equations and normalizing gives exactly \(\gamma^2=(AB-C^2)/(4(A+B-2C))\). The dodecahedral quadrilateral lies in the plane formerly containing the five dodecahedral neighbors of site \(0\), so has distance \(u\). The three-vertex Gram matrix of the remaining triangle has off-diagonal entries \(t,u,u\), giving the stated formula for \(\beta\). Original triangular facet distance is \(h\) as displayed in the finding.

For completeness, these are not merely possible planes. The exact-coordinate certificate checks strict supporting inequalities against **all thirty retained sites** for every new polygon, with equality only at the listed vertices; it also verifies strict support for all sixty undamaged original faces. The fifty-one old triangles plus these three new polygons have thirty vertices, eighty-two edges and fifty-four faces, every edge contained in exactly two polygonal boundaries, and connected one-skeleton. Therefore they form a closed connected polygonal surface on the boundary of the convex hull, and exhaust that boundary. Direct algebraic substitution and certified rational enclosures establish
\[
0<\gamma<u<\beta<h.
\]
Since the origin lies inside this full-dimensional hull, its minimum support over unit directions is the least distance of its supporting facet planes, namely \(\gamma\). Exactly one facet has that distance, so the worst direction is unique. Symmetry transfers the conclusion to all sixty incident pairs.

**4. Multiplicities.** There are \(\binom{12}{2}=66\) icosahedron–icosahedron pairs, \(\binom{20}{2}=190\) dodecahedron–dodecahedron pairs, sixty incident mixed pairs and \(12\cdot20-60=180\) nonincident mixed pairs. Together with steps 2–3 these give all \(496\) cases and both values.

## Verification

Run `python3 verify.py` from the extracted package. The independent, standard-library checker uses only `fractions.Fraction` and integer square roots to construct rational enclosing intervals for **all algebraic coordinates**, cross products, facet-support inequalities and closed-form distances. It verifies all sixty original strict-support triangles, the complete fifty-four-face incident-deletion boundary, polygon adjacency and Euler counts, the three replacement support heights, ordering of the four heights, incidence counts and the nonincident cap-separation inequality. The only zero-identities in the coplanar faces are justified algebraically in the proof; small-enclosure assertions in the checker are consistency checks, not substitutes for those identities. The checker returns `PASS` with the numerical enclosures. The proof is for all 496 deletions, using symmetry and geometry; finite floating-point sampling is not used to extrapolate a theorem.

## Relationship to prior work

Hoehner's paper first establishes the inscribed 32-vertex pentakis-dodecahedral realization as the global volume maximizer, explicitly describing its sixty triangular facets, two vertex orbits and exact mixed Gram products. It studies **volume**, not the spherical covering radius under deletion. The older pentakis-dodecahedron metric tables concern a different, Catalan, unequal-shell realization; direct substitution of their inradius would be incorrect here. Published results about icosahedral or icosidodecahedral single-orbit coverings, and about two-vertex **volume losses**, do not determine the spherical covering radius after erasure of two sites. The new distinction is the all-pairs covering dichotomy, exact exceptional coefficient and unique deepest direction after an incident-pair deletion.

## Limitations

The theorem concerns this particular unit-sphere 32-site set. It neither asserts that the original set minimizes spherical covering radius among all 32-site configurations nor that its two-erasure robustness is globally optimal. The originality assessment is based on inspected and searchable literature; an unindexed historical equivalent remains possible. No independent mathematical audit has been performed.

## References

- S. Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777v1 (first publicly posted 7 November 2026), especially Theorem 1.4 and §7.3: https://arxiv.org/html/2611.10777v1
- H. Cohn, *Spherical codes*, background on the distinct maximum-minimum-separation problem: https://cohn.mit.edu/spherical-codes/
- D. McCooey, *Pentakis Dodecahedron*, metric table for the unequal-shell Catalan solid, not the present inscribed realization: https://www.dmccooey.com/polyhedra/java/PentakisDodecahedron.html
