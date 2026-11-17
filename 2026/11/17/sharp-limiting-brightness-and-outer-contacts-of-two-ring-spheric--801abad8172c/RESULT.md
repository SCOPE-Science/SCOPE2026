# Sharp limiting brightness and outer contacts of two-ring spherical-design Minkowski polytopes

## Finding
For each integer \(n\ge4\), put \(\theta_j=2\pi j/n\), \(c=\sqrt{2/3}\), \(h=1/\sqrt3\), and
\[
 X_n=\{(c\cos\theta_j,c\sin\theta_j,\sigma h):0\le j<n,\;\sigma\in\{-1,1\}\}\subset\mathbb S^2.
\]
This is an equal-weight spherical \(3\)-design but not a spherical \(4\)-design. Let \(P_n\) be the unique-up-to-translation convex polytope whose facet unit normals are the \(2n\) points of \(X_n\), with each facet having area \(2\pi/n\). Let \(Z_n=\Pi P_n\) be its projection body, whose support function equals the Euclidean area of the orthogonal projection of \(P_n\) perpendicular to its argument. Write \(r_n\) and \(R_n\) for the unrestricted Euclidean inradius and circumradius of \(Z_n\).

**Theorem.** For every \(n\ge4\),
\[
 R_n=\frac{2\pi}{\sqrt3}.
\]
The maximum-support directions are exactly the two poles \(\pm(0,0,1)\) for \(n\ge5\). At \(n=4\), they are those two poles and the four horizontal diagonal directions \((\pm1,\pm1,0)/\sqrt2\).

There is a unique \(u_*\in(0,\pi/2)\) satisfying \(u_*=\sin(2u_*)\). Define
\[
 t_*=\sin u_*,\qquad z_*=\frac{\sqrt2t_*}{\sqrt{1+2t_*^2}},\qquad
 \rho_*=\frac{4\sqrt{2/3}\,[\cos u_*+u_*\sin u_*]}{\sqrt{1+2\sin^2u_*}}.
\]
Then \(r_n\to\rho_*\) with the explicit, all-order error estimate
\[
 \left|r_n-\rho_*\right|\le\frac{\pi^2\sqrt{2/3}}{n}\quad(n\ge4).
\]
Numerically, \(u_*=0.9477471335\ldots\), \(z_*=0.7541775883\ldots\), \(\rho_*=2.9021390777\ldots\), whereas \(R_n=3.6275987284\ldots\). If \(v_n\) is *any* unit direction minimizing the brightness of \(P_n\), then \(\lvert (v_n)_3\rvert\to z_*\). In particular,
\[
 \lim_{n\to\infty}\frac{R_n}{r_n}=\frac{2\pi}{\sqrt3\,\rho_*}=1.2499741161\ldots>1.
\]
Thus an unbounded number of equal-area facets with precisely isotropic normal moments through degree three does **not** force the projection body to become spherical. The limiting least-bright directions are oblique, not equatorial or polar.

## Assumptions and scope
All metric data are Euclidean in the ambient \(\mathbb R^3\). The inradius and circumradius refer to the full projection body, with centers unrestricted. Since every projection body is centrally symmetric, its origin-centered extremal radii are globally optimal: averaging any included ball and its reflection gives an equally large centered ball, and averaging opposite containing-ball centers also yields a centered containing ball. The facet-area normalization is essential: total surface area of \(P_n\) is \(4\pi\). Nothing is asserted about arbitrary spherical designs or about the exact finite-\(n\) value of \(r_n\).

## Proof
**1. Exactly cubic spherical design.** For \(n\ge4\), sums of \(e^{ik\theta_j}\) vanish for \(k\in\{1,2,3\}\). The two rings have symmetric opposite heights. Therefore all degree-one and degree-three coordinate moments vanish, cross second moments vanish, and the diagonal second moments are \(c^2/2=1/3\), \(c^2/2=1/3\), \(h^2=1/3\). These are exactly the spherical moments of polynomials of total degree at most three. Their fourth vertical moment is \(h^4=1/9\), versus \(1/5\) for normalized uniform surface measure on \(\mathbb S^2\), so they are not \(4\)-designs. The standard Minkowski existence-and-uniqueness theorem applies: the normals are balanced, are not confined to a great circle, and carry positive weights \(2\pi/n\).

**2. Complete brightness formula.** Cauchy's projection formula gives, for every unit \(v\),
\[
 b_n(v)=h_{Z_n}(v)=\frac\pi n\sum_{j=0}^{n-1}\sum_{\sigma=\pm1}|\langle(c\cos\theta_j,c\sin\theta_j,\sigma h),v\rangle|.
\]
Set \(v=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\) with \(0\le z\le1\), since the expression is even in \(z\). The identity \(\lvert A+B\rvert+\lvert A-B\rvert=2\max(\lvert A\rvert,\lvert B\rvert)\) gives
\[
 \frac{b_n(v)}\pi=\frac2n\sum_{j=0}^{n-1}\max\{c\sqrt{1-z^2}|\cos(\theta_j-\phi)|,hz\}.\tag{1}
\]

**3. Exact outer radius and equality directions.** Degree-two exactness gives \(\frac1{2n}\sum_{x\in X_n}\langle x,v\rangle^2=1/3\). Cauchy--Schwarz in (1) yields \(b_n(v)\le 2\pi/\sqrt3\), with equality if and only if \(\lvert\langle x,v\rangle\rvert=1/\sqrt3\) for every \(x\in X_n\). The vertical directions meet this condition. For both signs of the height, subtracting the corresponding squared equalities shows \(4chz(v_1\cos\theta_j+v_2\sin\theta_j)=0\) for each \(j\). If \(z\ne0\), the \(n\) azimuths span the horizontal plane and hence \(v_1=v_2=0\). If \(z=0\), all \(\lvert\cos(\theta_j-\phi)\rvert\) must equal \(1/\sqrt2\). This is impossible for \(n\ge5\): it would require all \(\cos(2\theta_j-2\phi)=0\), yet consecutive angles differ by \(4\pi/n\), which can be a multiple of \(\pi\) only for \(n=4\) among \(n\ge4\). For \(n=4\), the four azimuths are coordinate directions, and \(v=(\pm1,\pm1,0)/\sqrt2\) gives precisely the four further equality directions. The maximum of a symmetric body's support function over the sphere equals its circumradius, proving the claim.

**4. Uniform continuum limit, with an error bound.** For any \(z,\phi\), the periodic function \(\theta\mapsto\max\{c\sqrt{1-z^2}|\cos(\theta-\phi)|,hz\}\) is Lipschitz with constant at most \(c\). On each centered mesh cell of length \(2\pi/n\), integrating the distance to its midpoint gives a discrepancy of at most \(\pi c/(2n)\) between the equal-weight Riemann sum and the circle average. Thus the right-hand side of (1) converges uniformly (in \(z,\phi\)) to
\[
 F(z)=\frac4\pi\int_0^{\pi/2}\max\{c\sqrt{1-z^2}\cos\theta,hz\}\,d\theta
\]
with uniform error at most \(\pi c/n\) in the dimensionless quantity \(b_n/\pi\). Taking minima and multiplying by \(\pi\) gives the claimed error \(\pi^2c/n\) for the inradii.

**5. Exact limiting minimum.** Put \(t=hz/(c\sqrt{1-z^2})=z/(\sqrt2\sqrt{1-z^2})\). For \(0\le t\le1\), the integral splits at \(\theta=\arccos t\), yielding
\[
 F(t)=\frac{4c}{\pi\sqrt{1+2t^2}}\left[\sqrt{1-t^2}+t\arcsin t\right].\tag{2}
\]
For \(t\ge1\), it becomes \(F=2hz=2t\sqrt{2/3}/\sqrt{1+2t^2}\), strictly increasing. In the open interval \(0<t<1\), the sign of the derivative of (2) is the sign of
\[
 \arcsin t-2t\sqrt{1-t^2}.
\]
With \(u=\arcsin t\), this is \(u-\sin(2u)\). The function \(\sin(2u)-u\) is strictly concave on \((0,\pi/2)\), has positive initial derivative, and is negative at \(\pi/2\); therefore it has exactly one positive zero \(u_*\), and (2) decreases before and increases after this zero. The boundary \(t=1\) and the branch \(t>1\) cannot improve it. Hence the minimum is unique in \(z\), attained at the stated \(z_*\), and \(\pi F(z_*)=\rho_*\). Uniform convergence plus uniqueness forces \(\lvert(v_n)_3\rvert\to z_*\) for any sequence of minimizing directions. The positive radius ratio follows from the strict inequality \(\rho_*<R_n\), or simply from the explicitly evaluated expressions.

## Verification
The accompanying independent script `check_projection_design.py` constructs the \(2n\) normals for \(4\le n\le30\), checks moment tensors through degree three, verifies failure of the fourth vertical moment, computes the exact brightness support formula numerically, and independently searches facet-normal candidates using all nonparallel generator cross products. For a three-dimensional zonotope these span all facet-normal candidates; thus this test does not assume the continuum formula. It evaluates 65 deterministic random unit directions per dimension, checks the sharp outer bound and the uniform finite-size error, and numerically minimizes the continuum formula independently. The run passed **1,948 test assertions**. To reproduce, run `python check_projection_design.py` with Python, NumPy, and SciPy. These finite tests verify implementation and sample geometry; the assertions for all \(n\) and the limiting theorem are proved analytically above.

## Relationship to prior work
Congpei An (2026), *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1, supplies the equal-area normal realization and the general projection-body brightness formula, as well as bounds as design **strength** increases. Those are explicitly used, not claimed as original. The new claim fixes strength exactly three, allows the number of nodes to diverge, and determines a nontrivial sharp limiting brightness minimum, extremizing cone, persistent anisotropy, and exact finite outer-contact directions. An's later *Dual Geometry of Spherical Designs* (arXiv:2609.02439v1) studies polarity and self-polar incidence rather than this projection-body limit. A preceding exact result on this identical two-ring equal-area polytope family (research finding 7cc0bd2c-fbd6-4315-9d63-3a19cd2582f2) had already established that the original polytopes are regular bipyramids and determined their own inradii, circumradii, volumes, and Hausdorff distances; **none of those original-body quantities is asserted as new here**. The present theorem concerns the distinct projection bodies, their planar-shadow area extrema, an oblique limiting least-bright direction, and a nonalgebraic minimization equation. These are not numerical restatements of the previous original-body radius or volume formulas. A separately published result *Sharp spherical covering by two twisted regular latitude rings* optimizes the covering radius of the same underlying class of spherical node configurations, a different functional that does not determine their absolute-projection means. The continuum cosine-transform integral is elementary, but its sharp minimization and the explicit fixed-strength obstruction are the asserted additions.

## Limitations
The inradius is characterized **asymptotically**, with explicit \(O(1/n)\) error, not by a claimed closed finite-\(n\) formula. The outer contact description does not classify every exposed face of the projection body. The construction uses aligned, equally populated two-ring designs at the specific latitude \(z=\pm1/\sqrt3\); it does not treat general twists, unequal weights, or arbitrary spherical designs. It provides no counterexample to rates where the design strength increases. Historic priority against classical cosine-transform calculations in different terminology remains provisional, and no independent audit has been performed.

## References
1. C. An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1 (2026-08-12), with an earlier author-uploaded public copy dated 2026-08-11, Sections 3 and 6. https://arxiv.org/abs/2608.11570
2. C. An, *Dual Geometry of Spherical Designs: Polarity, Self-Polar Rigidity, and Quadrature Structure*, arXiv:2609.02439v1, first posted 2026-09-02. https://arxiv.org/abs/2609.02439
3. *Sharp spherical covering by two twisted regular latitude rings*, published mathematical research record dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-spherical-covering-by-two-twisted-regular-latitude-rings--d6c704c1d311
4. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, 2nd ed., Cambridge University Press (2014), Minkowski's existence theorem and Cauchy's projection formula.
5. Earlier publicly uploaded copy of Ref. 1, dated 2026-08-11, https://www.researchgate.net/publication/412115876_Minkowski_Polytopes_of_Spherical_Designs_High-Order_Isotropy_and_Quantitative_Sphericity
