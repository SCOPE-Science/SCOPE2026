# A sharp dimension-nine inball transition for norm-five cubic shell polytopes

## Finding
For each integer \(d\geq 5\), let
\[
P_d=\operatorname{conv}\left\{v\in\mathbb Z^d:\sum_{i=1}^d v_i^2=5\right\}
\]
with the ambient standard Euclidean metric. Denote by \(r_d\) the radius of its largest contained Euclidean ball and by \(R_d\) the smallest enclosing-ball radius. Then the unique incenter and circumcenter are the origin, and
\[
r_d=\begin{cases}\sqrt3,&5\leq d\leq8,\\5/\sqrt d,&d\geq9,\end{cases}
\qquad R_d=\sqrt5.
\]
Precisely \(8\binom d3\) facets touch the maximum inscribed ball when \(5\leq d\leq8\), and precisely \(2^d\) facets touch it when \(d\geq9\). The former are the signed three-coordinate support hyperplanes
\[
\sum_{i\in I}\varepsilon_i x_i=3,
\quad |I|=3,\quad \varepsilon_i\in\{-1,1\},
\]
whereas the latter are the fully supported sign hyperplanes
\[
\sum_{i=1}^d\varepsilon_i x_i=5,
\quad\varepsilon_i\in\{-1,1\}.
\]
Thus the inball's contact-normal support abruptly changes from three coordinates to all coordinates at dimension nine. The radius ratio is \(\sqrt{5/3}\) through dimension eight and \(\sqrt{d/5}\) from dimension nine onward. Every shell vector is a polytope vertex; the full vertex count is \(4d(d-1)+32\binom d5\). In dimension eight, there are \(2016\) vertices and exactly \(448\) inball-contact facets.

## Assumptions and scope
The integer \(d\ge5\) is arbitrary. The polytope lives in the full ambient \(\mathbb R^d\); distances are not normalized by lattice covolume or by volume. A *contact facet* is a codimension-one face whose supporting hyperplane meets the largest inscribed ball. The claim concerns only the fifth positive quadratic shell of the standard cubic lattice; it does not assert a formula for all shell indices or other integral lattices.

Every integer vector of squared norm five has precisely one of two absolute-value patterns: \((2,1,0,\ldots,0)\) or \((1,1,1,1,1,0,\ldots,0)\). Signed permutations give all \(4d(d-1)+32\binom d5\) different vectors. Every such vector \(v\) is exposed because the functional \(x\mapsto v\cdot x\) attains its unique maximum among all shell vectors at \(v\): by Cauchy–Schwarz, \(v\cdot w<5\) for all distinct shell points \(w\). Therefore the displayed count is the exact vertex count. Their antipodal symmetry and full linear span make the origin an interior point.

## Proof
**Step 1: centered inballs and the polar.** If a ball of radius \(r\) centered at \(c\) is in \(P_d\), central symmetry also puts the radius-\(r\) ball centered at \(-c\) in \(P_d\). Convexity then puts the radius-\(r\) ball centered at zero in \(P_d\). Thus it suffices to find the centered inradius. Since zero is interior, with \(P_d^\circ=\{u:u\cdot x\le1\text{ for every }x\in P_d\}\), inclusion of the origin-centered radius-\(r\) ball is equivalent to \(r\lVert u\rVert_2\le1\) for every \(u\in P_d^\circ\). Hence
\[
r_d^{-2}=\max\{\lVert u\rVert_2^2:u\in P_d^\circ\}.
\]

**Step 2: exact polar chamber.** The support function, with \(s_1\ge\cdots\ge s_d\ge0\) the sorted absolute coordinate values of \(u\), is
\[
h_{P_d}(u)=\max\{2s_1+s_2,\ s_1+s_2+s_3+s_4+s_5\}.
\]
The signed-permutation group preserves both the polar and Euclidean norm. Therefore work in the Weyl chamber \(u_1\ge\cdots\ge u_d\ge0\). Put \(z_j=u_j-u_{j+1}\ge0\), with \(u_{d+1}=0\). Then \(u_i=\sum_{j=i}^d z_j\) and the chamber of \(P_d^\circ\) has the exact nonnegative-orthant description
\[
2z_1+3\sum_{j=2}^d z_j\le1,
\qquad \sum_{j=1}^d\min(j,5)z_j\le1.
\]
A vertex of this bounded polytope has at most two strictly positive \(z_j\), since at most two additional inequalities can be active besides nonnegativity. The strictly convex function \(\lVert u\rVert_2^2\) has its maximum at one of these vertices.

**Step 3: single- and double-support vertices.** If precisely one \(z_j\) is nonzero, the possible squared norms are
\[
\frac14\ (j=1),\quad \frac29\ (j=2),\quad \frac13\ (j=3),\quad \frac14\ (j=4),\quad \frac j{25}\ (5\le j\le d).
\]
Two-positive-coordinate vertices must have indices \(i\in\{1,2\}\) and \(j\ge4\), because the first support inequality is stricter for indices one and two, both tie at index three, and the second is stricter at indices four and above. Both inequalities are tight for a two-positive-coordinate vertex. Solving the corresponding two-by-two systems yields the following exhaustive squared norms:
\[
\begin{array}{c|c}
(i,j)&\lVert u\rVert_2^2\\\hline
(1,4)&7/25\\
(2,4)&5/18\\
(1,j),\ j\ge5&(j+8)/49\\
(2,j),\ j\ge5&(j+16)/81.
\end{array}
\]
The zero vertex contributes zero. Consequently
\[
\max_{u\in P_d^\circ}\lVert u\rVert_2^2
=\max\left\{\frac13,\frac d{25},\frac{d+8}{49},\frac{d+16}{81}\right\}.
\]
For \(5\le d\le8\), the unique maximum is \(1/3\), attained in the chamber only at \(u=(1/3,1/3,1/3,0,\ldots,0)\). Indeed \(d/25\le8/25\), \((d+8)/49\le16/49\), and \((d+16)/81\le24/81\), all strictly smaller than \(1/3\). For \(d\ge9\), the unique maximum is \(d/25\), attained in the chamber only at \(u=(1/5,\ldots,1/5)\). The differences from the competing last two terms are \((24d-200)/1225>0\) and \((56d-400)/2025>0\), respectively. This proves the radii and all potential contact normal directions.

**Step 4: the contact planes really are facets.** A polar maximizer yields a support plane closest to zero; we also verify the face is codimension one. In dimensions five through eight, use the representative plane \(x_1+x_2+x_3=3\). The six permutations of \((2,1,0,0,\ldots,0)\) supported on the first three coordinates span a two-dimensional affine difference space on these coordinates. The additional shell points with first three coordinates all one and two arbitrary signed unit coordinates among the remaining \(d-3\) coordinates have differences spanning the remaining \(d-3\) coordinate directions. Thus the exposed face has dimension at least \(2+(d-3)=d-1\), so is a facet. In dimensions nine and higher, the representative plane \(\sum_i x_i=5\) contains all \(0/1\) vectors with exactly five ones, whose convex hull is the \(d-1\)-dimensional hypersimplex. This plane too defines a facet. Symmetry gives all signed coordinate permutations of these planes. The polar chamber's unique maximizer and symmetry ensure there are no other contact directions, yielding the exact facet counts.

**Step 5: uniqueness of centers and outer sphere.** Any maximum-radius center \(c\) must satisfy \(u\cdot c=0\) for every normalized signed contact facet normal \(u\), by applying the ball-containment inequalities to each antipodal pair of contact facets. These normal vectors span \(\mathbb R^d\), so \(c=0\). All shell vertices have squared norm five and occur in opposite pairs spanning \(\mathbb R^d\), giving a unique minimum enclosing sphere centered at zero with radius \(\sqrt5\): any enclosing ball of radius \(R\) centered at \(c\) must satisfy \(R^2\ge5+\lVert c\rVert^2\) by averaging squared distances to \(v\) and \(-v\). This completes the theorem.

## Verification
The accompanying `verify.py` enumerates all polar-chamber candidate vertices with exact rational arithmetic and checks their unique maxima in dimensions five through twenty. It also independently constructs every integer shell vector and all predicted contact supporting hyperplanes for dimensions five, six, eight, and nine, verifies support values over the complete finite generating set, and computes the affine rank of each representative contact facet exactly. Execution returned `PASS: 2916 exact rational / support / rank assertions`. This is a finite consistency check; the unrestricted quantifiers are established by the algebraic proof above, not by extrapolation from this computation. The file can be run with Python 3.10+ and SymPy: `python verify.py`.

## Relationship to prior work
Corradetti, *Integral Shell Polytopes of Composition Algebras* (first arXiv submission on 2026-05-10), Theorem 5.2 and Proposition 5.4, identifies the cubic-lattice coordinate model of the intermediate Okubo lattice and classifies its first shell orbits, including the 2016-point fifth shell. The above decomposition into the two signed-permutation patterns agrees with that previously published shell classification. The new claim is the exact Euclidean inradius, its dimension-nine contact-facet transition, and uniqueness of optimal centers; the source's shell-orbit counts alone do not imply these numbers without the geometric support optimization. The eight-dimensional original-lattice metric has a scale factor of \(\sqrt2\); the theorem's radii apply to the explicitly stated standard \(\mathbb Z^d\) coordinates, not unrescaled Okubo coordinates.

Results about Gaussian spherical random polytopes, root polytopes, and type-\(B\) generalized permutohedra concern different models or general extremal envelopes. No equivalent all-dimensional fifth-cubic-shell inball formula was located in the inspected sources and research-record searches. This establishes only best-knowledge priority, not an exhaustive historical uniqueness assertion.

## Limitations
This calculation does not enumerate all facets: it classifies exactly those facets touching the largest inscribed ball. It is for quadratic-shell index five and \(d\ge5\) only. Finite verification is a check on the exact proof and not an infinite certificate. Historic mathematical literature may contain an equivalent formulation under an alternative name; no independent audit has been performed.

## References
1. Daniele Corradetti, *Integral Shell Polytopes of Composition Algebras*, arXiv:2605.09458v1, 2026-05-10. https://arxiv.org/abs/2605.09458 . See Theorem 5.2, Remark 5.3 and Proposition 5.4, especially pages 15–17.
2. Gilles Bonnet and Eliza O'Reilly, *Facets of spherical random polytopes*, *Mathematische Nachrichten* 295 (2022), 1901–1933, https://doi.org/10.1002/mana.202000314 . A different, probabilistic spherical-polytope setting used solely for contrast.
