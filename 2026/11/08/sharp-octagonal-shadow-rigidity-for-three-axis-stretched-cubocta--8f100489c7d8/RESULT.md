# Sharp octagonal-shadow rigidity for three-axis-stretched cuboctahedra

## Finding
Let \(C\subset\mathbb R^3\) be the regular cuboctahedron with vertex set
\[
\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}.
\]
For arbitrary \(a,b,c>0\), put \(C_{a,b,c}=\operatorname{diag}(a,b,c)C\). Let \(u\) be uniformly distributed on the unit sphere, and let \(H(u)\) denote the number of vertices in the orthogonal projection of \(C_{a,b,c}\) onto \(u^\perp\). Then \(H(u)\in\{6,8\}\) almost surely, and with
\[
r_1=\frac{a^{-1}}{\sqrt{a^{-2}+b^{-2}+c^{-2}}},\quad
r_2=\frac{b^{-1}}{\sqrt{a^{-2}+b^{-2}+c^{-2}}},\quad
r_3=\frac{c^{-1}}{\sqrt{a^{-2}+b^{-2}+c^{-2}}}
\]
the *complete* projection-vertex-count law is
\[
\boxed{\Pr(H=8)=\frac4\pi\sum_{i=1}^3\arccos(r_i)-3,\qquad
\Pr(H=6)=1-\Pr(H=8).}
\]
It satisfies the globally sharp, rigid bounds
\[
\boxed{3-\frac{12}{\pi}\arcsin\!\left(\frac1{\sqrt3}\right)
\ \le\ \Pr(H=8)\ <\ 1.}
\]
The lower equality holds if and only if \(a=b=c\) (up to overall scale), and every probability in this half-open interval occurs for some positive axes. The upper endpoint is approached, but never attained, under axis degeneration. For the regular cuboctahedron the hexagonal-shadow probability is
\(\frac{12}{\pi}\arcsin(1/\sqrt3)-2\approx0.3509593121836436\),
while its octagonal-shadow probability is approximately \(0.6490406878163564\).

## Assumptions and scope
The sample is a Haar-uniform *unoriented* projection plane, equivalently the orthogonal complement of an independent uniform unit vector. A projected vertex is a genuine extreme vertex of the planar convex hull, not an original vertex whose projection is hidden or interior. The theorem covers all positive *diagonal* stretches in the displayed coordinate basis and their rigid motions. It does not claim the same exact formula for arbitrary nonorthogonal linear shears. Directions for which a face is viewed edge-on or projected edges coalesce form a finite union of great circles and hence have probability zero.

## Proof
**1. Facets and edge incidence.** The cuboctahedron is the intersection
\[
C=\{x\in\mathbb R^3:|x_i|\le1\ (i=1,2,3),\quad |x_1|+|x_2|+|x_3|\le2\}.
\]
Its six square faces have outward normals \(\pm e_i\), and its eight triangular faces have normals \((\pm1,\pm1,\pm1)\). Every one of its 24 edges joins exactly one square and one triangle. For each coordinate \(i\), exactly eight edges lie in squares perpendicular to \(e_i\). After diagonal stretching, unit-normal direction vectors may be taken as
\[
\pm a_i^{-1}e_i,\quad (\sigma_1/a,\sigma_2/b,\sigma_3/c)
\quad(\sigma_i\in\{-1,1\}),
\]
with \((a_1,a_2,a_3)=(a,b,c)\).

**2. Only hexagons and octagons.** An edge of a three-dimensional convex polytope is a genuine projected silhouette edge exactly when its two incident face normals have inner products of opposite signs with the viewing normal \(u\) (outside the exceptional directions). Set \(w_i=|u_i|/a_i\), and by signed coordinate symmetries suppose \(w_1\ge w_2\ge w_3>0\) with strict inequalities. Under the sign pattern of the six square and eight triangle face normals, four triangular sign patterns always contribute exactly one silhouette edge each, while the two remaining patterns contribute one edge each when \(w_1<w_2+w_3\), or two edges each when \(w_1>w_2+w_3\). Hence
\[
H(u)=\begin{cases}6,&\max_i w_i<\sum_{j\ne i}w_j,\\
8,&\max_i w_i>\sum_{j\ne i}w_j.\end{cases}
\]
The inequalities are exhaustive away from measure-zero boundaries. In particular the model has no generic four-, ten-, or twelve-vertex shadows.

**3. Exact Haar law.** For two nonzero normal vectors \(v,z\) making angle \(\delta\in(0,\pi)\), the set of uniformly random \(u\in S^2\) for which \((u\cdot v)(u\cdot z)<0\) consists of two spherical lunes of total area \(4\delta\). Its probability is therefore \(\delta/\pi\). At any square--triangle edge of coordinate family \(i\), the angle between the *outward* normals has cosine
\[
\cos\delta_i=\frac{a_i^{-1}}{\sqrt{a^{-2}+b^{-2}+c^{-2}}}=r_i.
\]
There are eight such edges per family. Linear expectation of the silhouette-edge count gives
\[
\mathbb E H=\frac8\pi\sum_{i=1}^3\delta_i.
\]
As \(H\in\{6,8\}\), we have \(\mathbb EH=6+2\Pr(H=8)\). Solving gives the stated complete law. This edge-angle expectation identity is a standard integral-geometric ingredient; the family-wise classification and sharp minimization below are the substantive new statements.

**4. Sharp minimum and rigidity.** Define \(t_i=r_i^2\in(0,1)\). Then \(t_1+t_2+t_3=1\), and
\[
\Pr(H=8)=3-\frac4\pi F(t_1,t_2,t_3),\qquad
F(t_1,t_2,t_3)=\sum_{i=1}^3\arcsin\sqrt{t_i}.
\]
On the closed simplex, \(F\) is continuous. On a boundary edge with, say, \(t_3=0\), the identity \(\arcsin\sqrt t+\arcsin\sqrt{1-t}=\pi/2\) gives \(F=\pi/2\) everywhere, including boundary vertices. At the barycenter,
\(F(1/3,1/3,1/3)=3\arcsin(1/\sqrt3)>\pi/2\).
Thus every global maximum of \(F\) occurs in the open simplex. For \(t\in(0,1)\),
\[
\frac{d}{dt}\arcsin\sqrt t=\frac1{2\sqrt{t(1-t)}}.
\]
At an interior constrained extremum, all three quantities \(t_i(1-t_i)\) are equal. Any two coordinates therefore coincide, or sum to one; the latter is impossible when the third coordinate is positive. All three coordinates must coincide. Thus the unique global maximizer of \(F\) is the barycenter, giving the lower bound and its equality characterization \(a=b=c\). Likewise, because the barycenter is the only interior critical point and is a strict global maximum while every boundary value is \(\pi/2\), no positive triple can have \(F\le\pi/2\), yielding the strict upper bound \(\Pr(H=8)<1\). Along \(t=(s,(1-s)/2,(1-s)/2)\) with \(s\in[1/3,1)\), continuity and the boundary limit \(F\to\pi/2\) show that every intermediate probability is realized. This also proves sharpness of the upper endpoint.

## Verification
`verify.py` independently enumerates the 24 genuine cuboctahedron edges, computes convex-hull projections from original Euclidean vertices, counts central-plane edge crossings, compares the dihedral-angle probability with an independent solid-angle triangulation formula, and checks Monte Carlo frequencies for four noncongruent axis triples. It also probes sharpness numerically over random positive axis ratios. One deterministic run returned:

```
VERIFY_OK shapes=4 directions=800000 projection_hulls=1600 central_sections=1604 independent_cone_formula=4 sharpness_trials=5000
```

The second probability formula used for the independent check is
\[
\Pr(H=8)=\frac2\pi\sum_{\rm cyclic}\arctan\frac{bc}{a(\sqrt{a^2+b^2}+\sqrt{a^2+c^2})}.
\]
It follows by triangulating each of the six conical regions \(|u_i|/a_i>\sum_{j\ne i}|u_j|/a_j\) and evaluating spherical triangle solid angles. The exact proof above does not rely on simulations or finite enumeration to establish an infinite-uniform-direction statement.

## Relationship to prior work
Glisse and Lazard (2007) study upper bounds on the expected silhouette complexity of polyhedra; Glisse, Lazard, Michel and Pouget (2016) study maximum silhouette complexity of random spherical polytopes. The general edge-dihedral-angle averaging idea is preexisting and not claimed new. Koca, Al Ajmi and Al-Shidhani (2010) study Coxeter-group constructions of quasi-regular polyhedra; they do not state a Haar silhouette law for the diagonal cuboctahedral family. An existing published result on *triaxial octahedron* shadow probabilities concerns a different, six-vertex polytope and cannot directly provide the present octagonal-shadow law for the twelve-vertex cuboctahedron. An earlier central-section result for the cuboctahedron is not part of the present finding: central sections and orthogonal projections are different geometric operations. The new content is the complete two-point shadow law for this continuum of axis-stretched cuboctahedra together with its sharp, rigid global extremum.

## Limitations
The theorem is exact only for a fixed cuboctahedron subjected to positive diagonal coordinate stretches, not general shears and not other Archimedean solids. The probability law by itself does not determine all three axis ratios. The hexagon/octagon classification is almost-sure, not a statement about exceptional viewing directions. The sharpness limit uses degenerate *limits* of positive triples, never a degenerate polytope in the theorem. Literature priority is provisional, particularly concerning obscure tabulations of silhouette distributions and exact consequences of general dihedral-angle methods. The work has not undergone independent external validation.

## References
1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087 (first public version 2007-02-14), https://arxiv.org/abs/cs/0702087.
2. M. Koca, M. Al Ajmi and S. Al-Shidhani, *Quasi Regular Polyhedra and Their Duals with Coxeter Symmetries Represented by Quaternions II*, arXiv:1006.2973 (first public version 2010-06-15), https://arxiv.org/abs/1006.2973.
3. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a Random Polytope*, Journal of Computational Geometry **7** (2016), 86--99, DOI 10.20382/jocg.v7i1a5 (published 2016-03-18), https://doi.org/10.20382/jocg.v7i1a5.
