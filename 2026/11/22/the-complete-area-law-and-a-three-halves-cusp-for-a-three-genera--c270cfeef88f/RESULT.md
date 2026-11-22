# The complete area law and a three-halves cusp for a three-generator random zonogon

## Finding
Choose three independent Haar-uniform unoriented planar unit vectors \(u_1,u_2,u_3\), and let \(Z=[0,u_1]+[0,u_2]+[0,u_3]\) be their Minkowski-sum zonogon. Let \(A\) denote its Euclidean area and \(T(t)=\Pr(A\ge t)\). This is almost surely a centrally symmetric hexagon of perimeter \(6\), the smallest non-parallelogram unit-segment zonogon.

The support of \(A\) is \([0,a_*]\), with \(a_*=3\sqrt3/2\), and its **entire survival function** is the following one-dimensional inverse-sine integral (\(0<t<a_*\)):
\[
T(t)=\frac2{\pi^2}\int_0^\pi L_t(x)\,dx,
\quad L_t(x)=\begin{cases}
\pi-x,&t\le2\sin x,\\
\pi-2\arcsin\!\left(\dfrac{t-\sin x}{2\cos(x/2)}\right),&2\sin x<t<\sin x+2\cos(x/2),\\
0,&t\ge\sin x+2\cos(x/2).
\end{cases}
\]
Set \(T(t)=1\) for \(t\le0\) and \(T(t)=0\) for \(t\ge a_*\). The values at the measure-zero endpoints in the displayed integrand are understood by continuity.

There are three sharply different threshold geometries. The two extreme tails satisfy
\[
\Pr(A<t)=\frac3{4\pi^2}t^2+O(t^4)\quad(t\downarrow0),
\qquad T(a_*-h)=\frac8{3\pi}h+O(h^{3/2})\quad(h\downarrow0).
\]
At the **interior threshold \(t=2\)**, which is exactly the largest area obtainable when any one pair of segments is parallel, the full survival function is continuously differentiable but not twice differentiable. More precisely,
\[
T(2-h)+T(2+h)-2T(2)=-\frac8{\pi^2}h^{3/2}+O(h^2)\quad(h\downarrow0).
\]
Thus the one-dimensional density has a square-root cusp, not an atom, at an intrinsic geometric transition.

There are marked endpoint limits. Independently of the global rotation, root the cyclic direction gaps at the *labelled first segment*. The resulting triple \((X,Y,W)\), with sum \(\pi\), is uniform on the simplex. Conditional on \(A<t\), one of the three gaps is asymptotically \(\pi\); its index is uniform on \(\{1,2,3\}\), and the other two gaps divided by \(t\) converge in total variation to the uniform law on \(\{(r,s):r,s\ge0,\ r+s\le1/2\}\), independent of the index. The normalized small-area mark \(A/t\) converges to \(\operatorname{Beta}(2,1)\). Conditional on \(A>a_*-h\), the pair \(((X-\pi/3)/\sqrt h,(Y-\pi/3)/\sqrt h)\) converges in total variation to the uniform distribution on \(\{(p,q):\sqrt3(p^2+pq+q^2)\le2\}\); the normalized deficit \((a_*-A)/h\) converges to Uniform\([0,1]\).

## Assumptions and scope
The three generator lengths are exactly one. Each direction is independent and uniform modulo \(\pi\), and the area refers to the zonogon defined using segments \([0,u_j]\), **not** \([-u_j,u_j]\) (whose area would be four times larger). All distributions are with respect to these three directions and no extra random lengths. The limiting laws hold at a fixed generator count of three with thresholds tending to their specified values, not as the generator count grows. Probability events with strict versus weak inequalities agree because the area variable has no atoms. The projective-direction root is the first *labelled* direction, not the smallest direction in a fixed coordinate interval.

## Proof
**1. Exact probability coordinates and the alias to cyclic triangles.** The classical zonotope determinant formula gives
\[
A=|\det(u_1,u_2)|+|\det(u_1,u_3)|+|\det(u_2,u_3)|.
\]
Rotate all angles by the negative of the first labelled angle modulo \(\pi\). The remaining two projective angles are independent Uniform\([0,\pi)\). Put their increasing order at \(X\) and \(X+Y\), and set \(W=\pi-X-Y\). Their order-statistic Jacobian gives the constant joint density \(2/\pi^2\) for \(X>0,Y>0,X+Y<\pi\), i.e. normalized Dirichlet\((1,1,1)\) cyclic gaps. Hence
\[
A=\sin X+\sin Y+\sin W=4\cos(X/2)\cos(Y/2)\cos(W/2).
\]
Doubling the direction angles puts three iid uniform points on the Euclidean unit circle. Their three chord lengths are \(2\sin X,2\sin Y,2\sin W\), so **the zonogon area equals exactly half their inscribed-triangle perimeter**. This equivalence is used in the literature comparison, not claimed as a new phenomenon.

**2. Entire distribution and support.** Hold \(X=x\) fixed. On \(0\le y\le\pi-x\),
\[
A(x,y)=\sin x+2\cos(x/2)\sin(y+x/2).
\]
This is symmetric and strictly concave in \(y\); its endpoint value is \(2\sin x\) and its maximum is \(\sin x+2\cos(x/2)\). Solving \(A(x,y)\ge t\) gives an interval of length \(L_t(x)\) in the three displayed cases. Integrating against \(2/\pi^2\) proves the exact survival formula. The strict concavity of sine on \((0,\pi)\) and the gap-sum constraint give \(A\le3\sin(\pi/3)=a_*\), with equality only at equal gaps. The infimum zero is reached at simplex corners in the closure. A nonconstant analytic map on the open simplex has measure-zero level sets, establishing absence of atoms.

**3. Small-area corner law and marked limit.** The only zeroes of the continuous extension of \(A\) to the closed simplex are its three corners. At the corner \((X,Y,W)=(\pi-r-s,r,s)\), with \(r,s\ge0\),
\[
A=\sin(r+s)+\sin r+\sin s=2(r+s)+O((r+s)^3).
\]
Therefore the sublevel region at this corner has area \(t^2/8+O(t^4)\). Multiplying by the constant joint density \(2/\pi^2\), then summing three disjoint corners, gives \(3t^2/(4\pi^2)+O(t^4)\). After rescaling by \(t\), the corner regions tend in measure to the triangle \(r+s\le1/2\), proving the claimed total-variation marked convergence and uniform corner label. On this triangle the radial coordinate \(2(r+s)\) has density \(2q\) on \([0,1]\), giving \(\operatorname{Beta}(2,1)\).

**4. Maximal-area ellipse and marked limit.** Write \(X=\pi/3+u\), \(Y=\pi/3+v\), \(W=\pi/3-u-v\). Taylor's theorem gives
\[
a_*-A=\frac{\sqrt3}{2}(u^2+uv+v^2)+O((|u|+|v|)^3).
\]
The quadratic form is positive definite, so the near-maximum superlevel region is confined to \(u,v=O(\sqrt h)\). Its rescaled limiting ellipse has area \(4\pi/3\). Multiplication by the density \(2/\pi^2\) gives \(8h/(3\pi)+O(h^{3/2})\). The rescaled domains converge in symmetric difference to the ellipse, proving total-variation convergence to its uniform law. A uniform point in a two-dimensional ellipse has uniformly distributed normalized positive-definite quadratic radius, proving the Uniform\([0,1]\) normalized area deficit.

**5. Interior three-halves cusp.** The only critical point of \(A\) in the *interior* of the gap simplex is its global maximum: the stationary equations \(\cos X=\cos Y=\cos W\) force equal gaps. Hence the level \(A=2\) is regular in the interior. On each of the three simplex edges, \(A=2\sin x\) has a unique nondegenerate maximum \(2\) at the edge midpoint. At such a contact, use signed tangential displacement \(s\) from the midpoint and inward normal gap \(r\ge0\). Then
\[
A(s,r)=2-s^2+r+O(|s|^3+|sr|+r^2).
\]
Away from these three contact points the coarea/change-of-variables representation for the level-set area varies smoothly enough in the threshold to contribute \(O(h^2)\) to the symmetric second difference. If the inward coordinate were allowed to be negative, the same local integrals would also vary smoothly. The restriction \(r\ge0\) *removes* for \(t=2-h\) an artificial strip of area
\[
\int_{-\sqrt h}^{\sqrt h}(h-s^2)\,ds=\frac43h^{3/2}
\]
at each edge contact, with \(O(h^2)\) geometric error; for \(t=2+h\) there is no such strip. The three contacts contribute \(-3(2/\pi^2)(4/3)h^{3/2}=-8h^{3/2}/\pi^2\) to the second difference, proving the stated cusp. This calculation also yields a continuous first derivative and a one-sided unbounded second derivative at \(2\).

## Verification
The self-contained file `verify.py` checks the pairwise-determinant identity on separately generated angles, evaluates the exact one-dimensional survival formula by midpoint quadrature, compares it with 300,000 seeded independent three-direction samples at seven levels, checks the classical mean \(\mathbb EA=6/\pi\), and checks numerical convergence of both extreme coefficients and the interior three-halves cusp. Run with `python verify.py` using Python 3 standard library only. The finite numerical checks corroborate the explicit identities and asymptotic normalizations; the proofs above are the basis for their infinite-precision claims.

## Relationship to prior work
The segment-sum determinant formula and the extremal regular-hexagon configuration are classical, and they are not claimed here. The full law is equivalently that of *half the perimeter* of a triangle formed by three independent uniform points on a unit circle. The uniform cyclic-triangle angle law and expected perimeter already appear in Steven Finch's *Mathematical Constants II*, Section 5.15.2; these facts are credited, and the inspected section contains side/angle and triangle-area distributions but not this exact perimeter survival law with its cusp and marked endpoint limits. Alonso-Gutiérrez and Prochno (arXiv:1608.00830, publicly available July 31, 2016, primary MSC 52A22) study random convex sets related to zonotopes, with support-function and mean-width estimates. Joós and Lángi (arXiv:2206.03204) establish deterministic zonotope volume formulas and extremal inequalities, and Schneider (arXiv:2202.06774) establishes valuation expectations and a limit theorem; none of these inspected main results gives this finite three-generator area law.

Three previously published related random-zonogon results were compared at the level of their full published scientific statements, not titles: *A non-Gaussian sine-product law for areas of uniformly directed planar zonogons* (2026-10-25) provides finite mean/variance and an \(n\to\infty\) limit but explicitly does not assert a full finite-\(n\) area law; *Perimeter-normalized random zonogons* (2026-11-08) establishes triangular-array second-order \(n\to\infty\) laws; *A critical radial-noise crossover* (2026-11-08) studies large-\(n\) radial-length noise and explicitly does not give finite-sample area density. Those results include stronger facts in their own large-generator regimes, but do not imply the three-generator threshold and conditional-marked formulas here. The exact one-dimensional CDF, interior density cusp and endpoint laws are the contribution.

## Limitations
This is the fixed three-segment, equal-length, independent Haar-direction model. It does not cover nonuniform angular laws, random segment lengths, higher-dimensional volumes, or asymptotic laws in the number of segments. The exact expression is one-dimensional quadrature rather than a closed elementary antiderivative. The historical comparison used identifiable full relevant sections and accessible public results; it does not exclude all unindexed classical treatments of circular-triangle perimeter density. A relevant earlier 2011 original survey version by Finch was not accessible in full in its original form, though the closely corresponding later published book section was read. Independent mathematical validation has not been performed.

## References
1. D. Alonso-Gutiérrez and J. Prochno, *On the geometry of random convex sets between polytopes and zonotopes*, arXiv:1608.00830v1 (first publicly posted July 31, 2016), primary MSC 52A22; see main-result statements. https://arxiv.org/abs/1608.00830
2. S. R. Finch, *Mathematical Constants II*, Section 5.15.2, "Unit Circumradius" (published book, 2019). Related original *Random Triangles V* survey (2011); see the unit-circumradius cyclic triangle calculations.
3. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204v1 (first public posting June 7, 2022), especially Section 3 and the segment mixed-volume identity. https://arxiv.org/abs/2206.03204
4. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (first public posting February 14, 2022), Theorems 1 and 3. https://arxiv.org/abs/2202.06774
5. *A non-Gaussian sine-product law for areas of uniformly directed planar zonogons*, public research result dated 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-non-gaussian-sine-product-law-for-areas-of-uniformly-directed--2e185012cf0e
6. *Perimeter-normalized random zonogons: universal second-order area law and a sharp spike obstruction*, public research result dated 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perimeter-normalized-random-zonogons-universal-second-order-area--9a9fb17a260f
7. *A critical radial-noise crossover for areas of random planar zonotopes*, public research result dated 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-critical-radial-noise-crossover-for-areas-of-random-planar-zon--95e0628386f8
