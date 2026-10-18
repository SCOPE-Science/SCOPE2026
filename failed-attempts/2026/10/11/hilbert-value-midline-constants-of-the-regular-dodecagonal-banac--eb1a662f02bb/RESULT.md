# Hilbert-value midline constants of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\), where
\[
N_{12}(s,t)=
\max\left\{
|s|,\ |t|,\
\left|\frac{\sqrt3s+t}{2}\right|,\
\left|\frac{s+\sqrt3t}{2}\right|,\
\left|\frac{-s+\sqrt3t}{2}\right|,\
\left|\frac{-\sqrt3s+t}{2}\right|
\right\}.
\]
Its unit ball is the regular dodecagon circumscribed about the Euclidean unit disk.

For the Chen--Yang--Liu--Li equilateral-midline constants
\[
M_1(X)
=
\sup
\left\{
\frac{\|x+y\|+\|2x-y\|}{2}:
\|x\|=\|y\|=\|x-y\|=1
\right\},
\]
\[
M_2(X)
=
\sup
\left\{
\frac{\|x+y\|^2+\|2x-y\|^2}{2}:
\|x\|=\|y\|=\|x-y\|=1
\right\},
\]
and
\[
M_3(X)
=
\sup
\left\{
\frac{\sqrt{\|x+y\|}+\sqrt{\|2x-y\|}}{2}:
\|x\|=\|y\|=\|x-y\|=1
\right\},
\]
one has
\[
M_1(X_{12})=\sqrt3,
\qquad
M_2(X_{12})=3,
\qquad
M_3(X_{12})=\sqrt[4]{3}.
\]

These are exactly the values taken by Hilbert spaces, even though \(X_{12}\) is a non-Hilbert polyhedral plane.

## Assumptions and scope
All scalars are real. The norm is the inradius-one regular-dodecagon norm displayed above.

Write the twelve signed supporting functionals as
\[
\begin{aligned}
f_0(s,t)&=s,
&
f_1(s,t)&=\frac{\sqrt3s+t}{2},
&
f_2(s,t)&=\frac{s+\sqrt3t}{2},
\\
f_3(s,t)&=t,
&
f_4(s,t)&=\frac{-s+\sqrt3t}{2},
&
f_5(s,t)&=\frac{-\sqrt3s+t}{2},
\end{aligned}
\]
together with
\[
f_{j+6}=-f_j
\qquad
(0\le j<6).
\]
Then
\[
N_{12}(z)=\max_{0\le j<12}f_j(z).
\]

For an admissible pair define
\[
A=N_{12}(x+y),
\qquad
B=N_{12}(2x-y).
\]
The proof first determines the exact global maxima of
\[
\frac{A+B}{2}
\quad\text{and}\quad
\frac{A^2+B^2}{2}.
\]
The \(M_3\) value then follows from the first one by concavity of the square root.

## Proof
Consider the compact polytope
\[
P=
\left\{
(x,y)\in\mathbb R^4:
f_i(x)\le1,\ 
f_i(y)\le1,\ 
f_i(x-y)\le1
\text{ for }0\le i<12
\right\}.
\]
Every pair satisfying
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1
\]
has at least one tight supporting facet in each of the three blocks. Hence every admissible pair belongs to at least one face
\[
F_{ijk}
=
\left\{
(x,y)\in P:
f_i(x)=f_j(y)=f_k(x-y)=1
\right\},
\qquad
0\le i,j,k<12.
\]

There are
\[
12^3=1728
\]
such tight-facet systems. Exact arithmetic in \(\mathbb Q(\sqrt3)\) shows that \(168\) have nonempty intersection with \(P\). Of these, \(24\) are nondegenerate line segments and the remaining \(144\) are points.

Fix one nondegenerate segment and parametrize it affinely by \(t\). For each signed facet \(f_m\),
\[
f_m(x+y)
\quad\text{and}\quad
f_m(2x-y)
\]
are affine functions of \(t\). Therefore
\[
A(t)=N_{12}(x+y)
\quad\text{and}\quad
B(t)=N_{12}(2x-y)
\]
are maxima of finitely many affine functions and hence are convex and nonnegative on the segment.

It follows that
\[
\frac{A(t)+B(t)}2
\]
is convex, so its maximum on the segment is attained at an endpoint. Also, because the square function is convex and nondecreasing on \([0,\infty)\),
\[
A(t)^2
\quad\text{and}\quad
B(t)^2
\]
are convex. Thus
\[
\frac{A(t)^2+B(t)^2}{2}
\]
also attains its segment maximum at an endpoint.

Consequently the global \(M_1\) and \(M_2\) problems reduce to the finite set of endpoints of the \(168\) nonempty faces. Exact evaluation gives
\[
\max\frac{A+B}{2}=\sqrt3
\]
and
\[
\max\frac{A^2+B^2}{2}=3.
\]
Therefore
\[
M_1(X_{12})=\sqrt3,
\qquad
M_2(X_{12})=3.
\]

Both bounds are attained simultaneously. Take
\[
x=(1,\sqrt3-2),
\qquad
y=(\sqrt3-1,\sqrt3-1).
\]
Direct substitution gives
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1,
\]
and
\[
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3.
\]

Finally, for every admissible pair,
\[
\frac{\sqrt A+\sqrt B}{2}
\le
\sqrt{\frac{A+B}{2}}
\le
\sqrt{\sqrt3}
=
\sqrt[4]{3},
\]
where the first inequality is concavity of the square root. The same explicit pair has
\[
A=B=\sqrt3,
\]
so equality holds throughout. Hence
\[
M_3(X_{12})=\sqrt[4]{3}.
\]

## Verification
The bundled `verify.py` works exactly in \(\mathbb Q(\sqrt3)\). It reconstructs all twelve signed facets, all thirty-six half-space inequalities for \(x\), \(y\), and \(x-y\), and all \(1728\) choices of one tight facet from each block.

For every consistent rank-three system it computes the exact feasible interval of the resulting affine line. It confirms that exactly \(168\) faces are nonempty, with \(24\) nondegenerate segments. It then evaluates the two convex objectives at every face endpoint and obtains
\[
M_1=\sqrt3,
\qquad
M_2=3.
\]
The checker separately verifies the explicit equality pair.

The \(M_3\) value is not inferred from numerical sampling. It follows analytically from
\[
\frac{\sqrt A+\sqrt B}{2}
\le
\sqrt{\frac{A+B}{2}}
\]
and the proved \(M_1\) bound, with equality at the explicit pair.

## Relationship to prior work
Chen, Yang, Liu and Li introduced \(M_1\), \(M_2\) and \(M_3\) to quantify midlines associated with equilateral triangles inscribed in a Banach-space unit sphere. Their paper proves that Hilbert spaces have
\[
M_1=\sqrt3,
\qquad
M_2=3,
\qquad
M_3=\sqrt[4]{3},
\]
and studies general inequalities and several classical examples. The inspected full text contains no regular-dodecagonal or regular-polygon computation and closes by identifying further work on these constants as an open direction.

The closely related earlier work of Chen, Liu and Li develops the equilateral-triangle constants \(H\) and \(G_L\) in the same geometric program and is classified primarily under MSC \(46B20\). The identity
\[
M_2(X)=\frac12G_L(X)
\]
is immediate from the two definitions, but no inspected source gives \(G_L\) for the regular dodecagon. A public exact \(G_L\) result exists for the regular octagon, which is a different normed plane and does not imply the present value.

A separate public theorem on regular \(4n\)-gonal norms uses the symbol \(M_3\) for an equilateral-triangle perimeter extremum. That notation denotes a different invariant and has no implication for the square-root midline constant \(M_3\) defined above.

The resulting coincidence with all three Hilbert values is therefore a genuine geometric feature of this non-Hilbert polyhedral plane rather than a consequence of the Hilbert characterization.

## Limitations
The result is specific to the regular dodecagonal plane. It does not classify the three midline constants on every regular polygon, nor does it characterize all non-Hilbert spaces that share one or more Hilbert values.

The finite polyhedral reduction is exact for \(M_1\) and \(M_2\), but it does not classify all maximizing pairs. Bibliographic and semantic searches cannot establish absolute novelty; an equivalent dodecagonal calculation under another affine normalization remains a residual literature risk.

## References
1. B. Chen, Z. Yang, Q. Liu and Y. Li, “Some Geometric Constants Related to the Midline of Equilateral Triangles in Banach Spaces,” Symmetry 14 (2022), 348, doi:10.3390/sym14020348. Published 9 February 2022.
2. B. Chen, Q. Liu and Y. Li, “Inscribed triangles in the unit sphere and a new class of geometric constants,” arXiv:2112.05922, first publicly posted 11 December 2021. Primary Mathematics Subject Classification: 46B20.
