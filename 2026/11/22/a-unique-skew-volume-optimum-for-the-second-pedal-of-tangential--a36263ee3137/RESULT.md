# A unique skew volume optimum for the second pedal of tangential rhombic prisms

## Finding

Let \(P_c\subset\mathbb R^3\), \(0\le c<1\), be the right rhombic prism bounded by the six unit-distance supporting planes
\[|\langle x,u_1\rangle|\le1,\quad |\langle x,u_2\rangle|\le1,\quad |x_3|\le1,\]
where \(u_1,u_2\) are unit vectors in the horizontal plane satisfying \(\langle u_1,u_2\rangle=c\). All six facets are tangent to the unit sphere. Define \(\mathcal D(K)\) as the convex hull of orthogonal feet from the origin onto the *facet supporting hyperplanes* of a full-dimensional convex polytope \(K\) containing the origin in its interior.

The exact two-step pedal volume is
\[
\boxed{\operatorname{vol}_3(\mathcal D^2(P_c))
=\frac{8\sqrt{1-c^2}(9+2c-3c^2)}{3(9-c^2)^2}.}
\]
Among all such normalized right rhombic prisms, this volume has a **unique maximum at a genuinely nonrectangular prism**: \(c=c_*\), the unique root in \((0,1)\) of
\[
3c^5-4c^4+48c^3-30c^2-99c+18=0.
\]
Precisely, \(7/40<c_*<22/125\), \(c_*\approx0.175097381279917\), and the maximal volume is approximately \(0.302143544127582\), strictly greater than the cubic value \(8/27\). The optimal relative improvement over the cube is approximately \(1.973446\%\).

The second pedal has exactly eight exposed vertices for every \(0\le c<1\). At \(c=0\) it is a cube, with six quadrilateral facets. For every \(0<c<1\) it has **four quadrilateral lateral facets and four triangular roof facets**, and it is not a parallelotope. The facet transition is immediate at the cube although the volume increases initially.

## Assumptions and scope

The unit of length is fixed by the common inradius \(1\) and vertical half-height \(1\). The parameter \(c\) is the absolute cosine of the angle between the two distinct pairs of horizontal facet normals; changing signs or exchanging normals does not change the prism. Thus \(0\le c<1\) parametrizes all congruence types in this normalized tangential right-rhombic-prism family. All volumes are ordinary Euclidean three-dimensional Lebesgue volumes, not volume ratios to the unbounded limit of the original prism. The endpoint \(c=1\) is excluded because the horizontal normals become parallel and the original prism ceases to be bounded.

## Proof

**First pedal and dual coordinates.** Put \(u_3=e_3\), \(U=[u_1\ u_2\ u_3]\), and \(W=U^{-\mathsf T}\) with columns \(w_1,w_2,w_3\). Then
\[
P_c=W[-1,1]^3,\qquad
\mathcal D(P_c)=\operatorname{conv}\{\pm u_1,\pm u_2,\pm e_3\}=P_c^\circ.
\]
The eight facet-supporting planes of the first pedal are
\[\langle W\varepsilon,y\rangle=1,\qquad \varepsilon\in\{-1,1\}^3.\]
Therefore the *entire* second pedal is the convex hull of the eight actual feet
\[
f_\varepsilon=\frac{W\varepsilon}{\|W\varepsilon\|^2}.
\]
This also follows from the established polar-inversion formula for two pedal steps on a circumscribed polytope, but the remaining shape and volume analysis is additional.

**Four vertical columns.** From \(u_i\cdot w_j=\delta_{ij}\), the two horizontal dual vectors satisfy
\[
\|w_1+w_2\|^2=\frac2{1+c},\quad
\|w_1-w_2\|^2=\frac2{1-c},\quad
(w_1+w_2)\cdot(w_1-w_2)=0,
\]
and \(w_3=e_3\). Choose horizontal orthonormal axes along \(w_1+w_2\) and \(w_1-w_2\). Define
\[
A=\frac{\sqrt{2(1+c)}}{3+c},\quad B=\frac{\sqrt{2(1-c)}}{3-c},\quad
h_+=\frac{1+c}{3+c},\quad h_-=\frac{1-c}{3-c}.
\]
The eight feet, in these axes, are exactly
\[
(\pm A,0,\pm h_+),\qquad (0,\pm B,\pm h_-),
\]
with independent signs. Their horizontal projection is the diamond \(\{|X|/A+|Y|/B\le1\}\). At each of its four corners there is a vertical segment with two distinct endpoints. Since each corner of the projected diamond is exposed, both endpoints of each vertical segment are exposed by sufficiently small positive or negative vertical tilts of a supporting functional. Hence all eight points are actual extreme vertices, not merely listed feet.

For \(c>0\), \(h_+>h_-\). The upper boundary over the diamond is the maximum-height function
\[
z_{\max}(X,Y)=h_+-(h_+-h_-)\frac{|Y|}{B},
\]
and the lower boundary is its negative. The two signs of \(Y\) give the two upper triangular facets and two lower triangular facets. The four sides of the diamond lift to four quadrilateral lateral facets. When \(c=0\), \(h_+=h_-=1/3\), the two triangles on each roof become one flat quadrilateral, and the whole body is the cube of half-side \(1/3\).

**Exact volume.** The diamond has area \(2AB\), and the mean of \(|Y|/B\) over its uniform area measure is \(1/3\), as can be checked by integrating the horizontal section length \(2A(1-|Y|/B)\). Thus
\[
\operatorname{vol}_3(\mathcal D^2(P_c))
=\iint_{|X|/A+|Y|/B\le1}2z_{\max}(X,Y)\,dX\,dY
=\frac{4AB}{3}(2h_++h_-),
\]
which simplifies to the displayed closed expression. It remains valid at \(c=0\) by continuity. It tends to \(0\) as \(c\uparrow1\), because \(B\to0\).

**Unique skew maximum.** Differentiating the positive volume expression gives
\[
V'(c)=\frac{8F(c)}{3\sqrt{1-c^2}(9-c^2)^3},\qquad
F(c)=3c^5-4c^4+48c^3-30c^2-99c+18.
\]
For \(0\le c\le1\),
\[
F'(c)=15c^4-16c^3+144c^2-60c-99
\le 15c+144c-60c-99=99(c-1),
\]
where \(c^4\le c\), \(c^2\le c\), and \(-16c^3\le0\). Consequently \(F'<0\) throughout \([0,1)\). Since \(F(0)=18>0\), \(F(1)=-64<0\), there is one and only one critical point \(c_*\), which is the strict global maximum. Direct exact substitutions give \(F(7/40)>0\) and \(F(22/125)<0\); the quoted decimals are diagnostics and not needed for uniqueness. Since \(V'(0)>0\), the cube is strictly suboptimal in this family.

## Verification

The included standalone `verify_rhombic_pedal.py` checks the symbolic volume identity and derivative exactly, checks rational signs bracketing the maximizing root, and computes the polyhedral volume through *exact rational tetrahedron determinants* at 48 distinct rational configurations (including the cube). Numerical convex hulls are used only to select a boundary triangulation for these independent exact-volume diagnostics; they are not the proof of the complete family statement. Each exact computed volume equals the analytic formula at its parameter. Run `python verify_rhombic_pedal.py` with Python, SymPy, NumPy, and SciPy installed. The analytic proof above covers all real \(0\le c<1\).

## Relationship to prior work

M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1, Proposition 4.1, already gives the two-step inversion-of-vertices formula for arbitrary circumscribed polytopes, and Proposition 4.2 treats the four-step return of rectangular boxes. Those statements are **not claimed as new**. Another earlier result classifies precisely when the second pedal of a general three-dimensional parallelotope remains a parallelotope; that qualitative rigidity does not supply the eight-face shape, exact volume or unique nonorthogonal volume maximum here. The publicly available *Four-step pedal return and aspect-ratio inversion for prisms over bicentric polytopes* treats bases having both a centered incircle and circumcircle; a nonsquare rhombus is not cyclic, and that theorem gives no volume extremum for this family.

The contribution is the full sharp three-dimensional volume profile under the natural fixed-inradius tangential constraint, its noncubical unique optimizer, and the accompanying facet transition. It is a restricted family theorem and does not classify all circumscribed six-facet polytopes or the volumes of further pedal iterates.

## Limitations

The reference point must be the common incenter and the body must be a **right** rhombic prism with all six facet distances equal to one. The result says nothing about sheared vertical directions, arbitrary parallelepipeds without an insphere, arbitrary starting points, or unrestricted minimax properties of the pedal map. The supplied finite arithmetic checks are corroboration, not a substitute for the analytic proof. The novelty assessment remains provisional against potentially unindexed older inversion/pedal literature; it is not an independent mathematical audit.

## References

1. M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1, first public version 2026-10-31, https://arxiv.org/html/2611.01247v1 (especially Proposition 4.1 and Proposition 4.2).
2. *Four-step pedal return and aspect-ratio inversion for prisms over bicentric polytopes*, publicly indexed mathematical note, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-step-pedal-return-and-aspect-ratio-inversion-for-prisms-ove--c2558824bf16 (comparison only).
3. G. M. Ziegler, *Lectures on Polytopes*, Springer, 1995, Chapter 2 (standard polarity and face duality).
