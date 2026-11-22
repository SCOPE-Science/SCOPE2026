# Unequal-ball lens John ellipsoids and a three-scale high-dimensional contact law

## Finding
Let \(m\ge4\) be an integer, \(R>r>0\), and \(R-r<L<R+r\). In \(\mathbb R^m\) set
\[
K=B(0,R)\cap B(Le_1,r),\qquad
E(z,a,b)=\left\{(x_1,x_\perp):\frac{(x_1-z)^2}{a^2}+\frac{\|x_\perp\|^2}{b^2}\le1\right\}.
\]
The unique maximum-volume inscribed ellipsoid of \(K\), without restrictions on competitors, equals \(E(z,a,b)\) given by the following exact classification.

Put \(g=R/r>1\) and \(L_c=m(R^2-r^2)/((m-1)R)\).

**Axial-tip regime:** If \(g\ge m\), or \(g<m\) and \(L\le L_c\), there is a unique \(a>0\) satisfying
\[
r^2=(a+mv)(a+v/m),\qquad v=a+L-R>0.
\]
Then \(z=R-a\), \(b^2=a(a+mv)\). The large ball contacts the ellipsoid only at its positive axial tip; the small ball contacts one latitude whose normalized axial coordinate is \(-1/m\).

**Two-latitude regime:** This occurs exactly if \(1<g<m\) and \(L_c<L<R+r\). There is a unique \(u\in(\sqrt{g/m},1)\) satisfying
\[
\frac Lr=\frac{u+1/(mu)}{\sqrt{(k+1)(k+1/(m^2u^2))}},\qquad
k=\frac{u^2-g^2/(m^2u^2)}{g^2-1}.
\]
Put \(H=L/(u+1/(mu))\), \(a=kH\), \(b^2=a(a+H)\), and \(z=Hu\). The larger and smaller balls contact the ellipsoid, respectively, along normalized axial latitudes \(u\) and \(-1/(mu)\); hence their latitude product is exactly \(-1/m\). Each contact locus is an \((m-2)\)-sphere (two points when \(m=2\)). The two prescriptions agree continuously at \(L=L_c\).

**A new dimension-scale law.** Fix \(g>1\) and \(\lambda\in(g-1,g+1)\), set \(R=gr\), \(L=\lambda r\), and let \(u_m\) denote the positive contact latitude from the first ball (\(u_m=1\) in the tip regime). Write \(A=g^2-1\). As \(m\to\infty\),
\[
\begin{array}{ll}
\lambda\le A/g:&u_m=1\quad\text{for all sufficiently large }m,\\[2pt]
A/g<\lambda<\sqrt A:&u_m\longrightarrow\sqrt{A(A/\lambda^2-1)},\\[2pt]
\lambda=\sqrt A:&m^{1/4}u_m\longrightarrow(2A)^{1/4},\\[2pt]
\sqrt A<\lambda<g+1:&m^{1/2}u_m\longrightarrow\sqrt{(\lambda^2+A)/(\lambda^2-A)}.
\end{array}
\]
Thus the positive John-contact latitude changes from an order-one quantity to order \(m^{-1/2}\) through the distinct critical order \(m^{-1/4}\) at the natural separation \(L=\sqrt{R^2-r^2}\).

## Assumptions and scope
All balls are closed Euclidean balls and have full-dimensional proper overlap. The two radii are strictly unequal. The central result is stated for \(m\ge4\), not for the previously treated three-dimensional unequal-radius lens or the congruent-ball case. The formulas themselves also admit lower dimensions, which serve only as consistency checks. The John ellipsoid means the unrestricted maximal-volume ellipsoid, not a prescribed axis-aligned approximation. The halfaxes satisfy \(0<a<b\) for strict proper overlap.

## Proof
**1. A general containment calculation.** Transform a unit parameter vector \((t,\sqrt{1-t^2}\,\omega)\), \(-1\le t\le1\), \(\omega\in S^{m-2}\), to the boundary point \((z+at,b\sqrt{1-t^2}\,\omega)\). Its squared distance to either center \(c e_1\), \(c=0\) or \(L\), is
\[
(z-c)^2+b^2+2a(z-c)t-(b^2-a^2)t^2.
\]
Put \(q=b^2-a^2>0\). This strictly concave quadratic attains its unconstrained maximum at \(t_c=a(z-c)/q\), clipped to \([-1,1]\). In either branch the displayed ellipsoid is contained in each ball by checking the exact maximum, not merely sample directions.

**2. A global finite-contact certificate.** For two normalized axial latitudes \(t_+>0>t_-\) with \(t_+t_-=-1/m\), define \(w_+=-t_-/(t_+-t_-)\), \(w_-=t_+/(t_+-t_-)\). On each latitude take \(\omega\) equally among the \(2(m-1)\) vectors \(\pm e_j\), \(2\le j\le m\), with total probability \(w_+\) or \(w_-\). Then the mean is zero and the covariance is \(I_m/m\): the axial variance equals \(-t_+t_-=1/m\) and each perpendicular variance equals \((1-1/m)/(m-1)=1/m\). If these points are actual boundary contacts of the transformed lens with the unit ball, multiplying their probabilities by \(m\) supplies John's positive contact certificate. Hence the exhibited ellipsoid is uniquely maximal among *all* translated and rotated ellipsoids. This works when \(t_+=1\); the repeated transverse representatives coalesce into the axial tip.

**3. The axial-tip construction and its validity.** Assume the candidate ellipse touches the larger ball at its right pole, \(z+a=R\), and the smaller at \(t_-=-1/m\). Its stationary condition for the smaller ball gives \(q=ma v\), where \(v=a+L-R>0\). Equality of the smaller-ball maximum is precisely \(r^2=(a+mv)(a+v/m)\). For \(L\in(R-r,R+r)\), the function of \(a\) on the right is strictly increasing on \(a>\max(0,R-L)\), starts below \(r^2\), and tends to infinity, so it has exactly one positive solution. With \(b^2=a(a+mv)\), the smaller ball is contained and touches the normalized latitude \(-1/m\). The maximum squared distance to the larger center occurs at \(t=1\) precisely when \(z\ge mv\), or \(R-a\ge mv\). At this point it equals \(R^2\). Thus the same finite-contact certificate proves global optimality whenever that inequality holds.

The solution \(a(L)\) is differentiable and, by differentiating its defining equation,
\[
a'(L)=-\frac{(m^2+1)a+2mv}{(m+1)^2(a+v)}.
\]
Consequently the validity expression \(R-a-mv\) decreases strictly in \(L\), since its derivative equals \(-(m-1)(a+mv)/((m+1)(a+v))<0\). At a possible zero, \(a=(m^2r^2-R^2)/(R(m^2-1))\) and \(L=L_c=m(R^2-r^2)/((m-1)R)\). The zero lies in the proper-overlap interval if and only if \(R<mr\). If \(R\ge mr\) the tip certificate remains valid up to external tangency; otherwise it is valid exactly through \(L_c\).

**4. Both spherical boundaries active.** For \(1<g<m\), choose \(u\in(\sqrt{g/m},1)\) and define \(k,H,a,b,z,L\) as in the finding. Then \(q=aH\), \(z=Hu\), \(z-L=-H/(mu)\). The two quadratic maxima occur at \(u\in(0,1)\) and \(-1/(mu)\in(-1,0)\), and their exact values are
\[
(a+H)(a+Hu^2)=R^2,\qquad
(a+H)(a+H/(m^2u^2))=r^2.
\]
Both follow on inserting \(k=(u^2-g^2/(m^2u^2))/(g^2-1)\) and the definition of \(H\). Thus the proposed ellipsoid lies in the lens and has the two stated latitude contacts. Their product is \(-1/m\), so Step 2 certifies unrestricted optimality.

The function of \(u\) on the right of the scalar equation for \(L/r\) is continuous on \((\sqrt{g/m},1]\), tends to \(g+1\) as \(u\downarrow\sqrt{g/m}\), and equals \(L_c/r\) at \(u=1\). Every intermediate \(L\) occurs by continuity. If two parameters produced the same \(L\), they would yield two John ellipsoids, hence the same unique ellipsoid, yet its unique positive larger-ball contact latitude is the respective \(u\); therefore the parameters coincide. This proves existence and uniqueness of the root and shows the two branches join at the endpoint.

**5. High-dimensional contact crossover.** For fixed \(g>1\) and \(\lambda=L/r\), the finite-dimensional threshold tends to \(A/g\) from above. Beyond it, put \(y=u_m^2\). The defining equation is *exactly*
\[
\lambda^2=
\frac{m^2 y A^2(my+1)^2}
{(m^2 y^2+m^2Ay-g^2)(m^2y^2-1)}.
\]
The allowed range is \(g/m<y<1\), and Step 4 gives unique solutions, monotonic in \(y\). For fixed \(A/g<\lambda<\sqrt A\), taking a nonzero limit \(y\) yields \(\lambda^2=A^2/(y+A)\); bracketing by nearby positive constants gives the stated limit. For \(\sqrt A<\lambda<g+1\), set \(y=x/m\), bracket positive \(x>g\) and pass to \(\lambda^2=A(x+1)/(x-1)\), obtaining the stated \(x\). At \(\lambda=\sqrt A\), bracket \(y=\beta/\sqrt m\). Uniform expansion for fixed \(\beta>0\) gives
\[
\frac{\lambda^2}{A}
=1+\left(\frac2\beta-\frac\beta A\right)m^{-1/2}+O_\beta(m^{-1}).
\]
The unique root consequently has \(\sqrt m\,y\to\sqrt{2A}\), proving the quarter-power limit. The bounds also exclude other scales; no interpolation from finite numerical experiments is used.

## Verification
Run `python3 verify.py` in the directory containing this result and the checker. It performs independent exact quadratic-max containment checks for 320 parameter combinations over several dimensions, a separate 251-direction grid per ball, finite contact covariance checks, threshold continuity checks and high-dimensional asymptotic comparisons. Numerical evidence supplements but does not replace Steps 1–5. The source code is included as a standalone file with only Python standard-library dependencies.

## Relationship to prior work
Güler and Gürtuna (arXiv:0709.0707v1, 2007) provide the general maximum-inscribed-ellipsoid framework and solve ellipsoidal slabs and truncated cones, not intersections of two unequal balls. Ball's 1997 lecture supplies the John contact theorem used for the unrestricted optimality certificate. Finch (arXiv:1301.5515v1, 2013) studies intersecting equal spheres and their geometric measures rather than inscribed ellipsoids. The previously available all-dimensional result for two *equal-radius* balls has two equal-and-opposite normalized contact latitudes; it does not imply the unequal-radius tip/contact phase or its high-dimensional scaling. A previously obtained three-dimensional unequal-radius classification is a lower-dimensional case, and no new priority is claimed for that case. A published unequal-ball **convex-hull Löwner** result concerns the outer ellipsoid of a union's convex hull, not the inner ellipsoid of an intersection; their polar bodies are not identified by a general ball-to-ball polarity. A 2015 optimization discussion provides a general semidefinite program for intersecting disks, but not the exact dimension-dependent contact classification or the quarter-power law. Thus the novel focus here is the full higher-dimensional asymmetric classification and the new high-dimensional three-scale contact limit, subject to historical-priority uncertainty.

## Limitations
The construction applies only to two Euclidean balls with unequal radii in proper overlap, not arbitrary ellipsoids, three or more balls, or non-Euclidean norms. The second-phase root is uniquely characterized rather than expressed in radicals. The dimensional crossover assumes a fixed strict radius ratio and fixed separation parameter; joint scaling of these parameters is not addressed. The global originality comparison is evidence-based rather than a mathematical proof of historical uniqueness. Independent human mathematical validation has not been performed.

## References
1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, first public 2007-09-05. https://arxiv.org/abs/0709.0707
2. K. Ball, *An Elementary Introduction to Modern Convex Geometry*, MSRI Publications 31 (1997), Lecture 3, pp. 13–19. https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Ball/ball.pdf
3. P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246v1, 2012-07-31. https://arxiv.org/abs/1207.7246
4. S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, first public 2013-01-23, §1. https://arxiv.org/html/1301.5515v1
5. *Exact John ellipsoids and contact latitudes of symmetric ball lenses in all dimensions*, public mathematical finding, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-john-ellipsoids-and-contact-latitudes-of-symmetric-ball-le--02e413e91d3d
6. *A sharp contact bifurcation for the Löwner ellipsoid of two unequal balls*, public mathematical finding, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-contact-bifurcation-for-the-l-wner-ellipsoid-of-two-uneq--424a15eeef51
7. M. Grant, answer on maximum-volume ellipsoids in intersections of disks, Mathematics Stack Exchange, 2015-04-02, citing Boyd and Vandenberghe, *Convex Optimization*, §8.4.2. https://math.stackexchange.com/questions/1202928/longest-chord-in-the-intersection-n-disks-circle-areas
