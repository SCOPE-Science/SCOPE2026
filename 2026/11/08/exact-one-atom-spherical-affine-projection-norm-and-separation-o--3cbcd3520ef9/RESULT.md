# Exact one-atom spherical affine projection norm and separation of local and global norming transitions

## Finding
Fix a unit vector \(N\in\mathbb S^2\). For \(0<w<1\), let \(\mu_w=(1-w)\sigma+w\delta_N\), where \(\sigma\) is normalized surface measure. Let \(P_w\) be the \(L^2(\mu_w)\)-orthogonal projector onto restrictions of affine real functions in three coordinates, and \(\Lambda_w=\|P_w\|_{L^\infty(\mu_w)\to L^\infty(\mu_w)}\). Put
\[
r=\frac{w}{1+3w},\quad t=1+3x\cdot N\in[-2,4],\quad q_r(t)=1+\frac{2r}{3}t-r\left(\frac23-r\right)t^2,\quad u_r(t)=1-rt.
\]
Define
\[
F_r(t)=\frac{9q_r(t)+u_r(t)^2}{6\sqrt{q_r(t)}}+r|t|,
\quad P_r(t)=(9q_r(t)-u_r(t)^2)q'_r(t)-4rq_r(t)u_r(t),
\]
\[
R_r(t)=P_r(t)^2-144r^2q_r(t)^3.
\]
For every \(0<w<1\), the sharp norm has the following **finite algebraic determination**, without a continuous optimization:
\[
\boxed{\Lambda_w=\max\bigl\{F_r(t): t\in\{-2,0,4\}\cup\bigl(\operatorname{Roots}_{\mathbb R}(R_r)\cap(-2,4)\bigr)\bigr\}.}
\]
The polynomial \(R_r\) has degree six for \(0<r<1/4\), and all norming evaluation locations are exactly the latitude circles \(x\cdot N=(t-1)/3\) corresponding to maximizers in the displayed finite set.

There is a persistent exact calibration \(F_r(0)=5/3\), at latitude \(x\cdot N=-1/3\), which is a strict local **minimum** of the row norm for every positive \(w\). At the antipode \(x=-N\),
\[
H(r):=F_r(-2)=\frac{5-10r+8r^2}{3(1-2r)}.
\]
The antipode is a strict local maximizer of the row norm **if and only if** \(w>1/3\). At \(w=1/3\) it is not locally maximal. Nonetheless, at \(w=1/3\), the off-antipodal latitude \(t=5/4\) has strictly larger row norm than \(H(1/6)\). For all \(w\) sufficiently close to \(1\), the antipode is the **unique global norming evaluation location**. Consequently there exists at least one weight \(w_*\in(1/3,1)\) at which the antipode and an off-antipodal latitude are distinct simultaneous **global** normers. Thus the onset of local antipodal maximality at \(w=1/3\) is strictly separated from the transition to global antipodal norming.

The endpoint limits are \(\lim_{w\downarrow0}\Lambda_w=5/3\) and \(\lim_{w\uparrow1}\Lambda_w=2\). For all sufficiently small positive \(w\), there is a unique norming latitude circle, with \(t\to5/4\) (equivalently \(x\cdot N\to1/12\)) as \(w\downarrow0\).

## Assumptions and scope
All scalar functions are real and are identified \(\mu_w\)-almost everywhere. The support of \(\mu_w\) is the entire sphere for \(0<w<1\); both the continuous and atomic terms enter the \(L^\infty\) norm. The projection acts on bounded measurable functions. The finite-root formula is an exact algorithmic algebraic characterization (real polynomial roots), not a claim that all roots have simple radical expressions. No assertion of a unique global transition weight is made.

## Proof
**1. Kernel and row norm.** Rotation symmetry lets us set \(N=(0,0,1)\). Under \(\mu_w\), the coordinate mean is \(wN\), and the centered covariance matrix is \(\operatorname{diag}((1-w)/3,(1-w)/3,(1-w)(1+3w)/3)\). Orthogonality of constants and centered coordinates gives the reproducing kernel
\[
K_w(x,y)=1+\frac{3(x_1y_1+x_2y_2)}{1-w}+\frac{3(x_3-w)(y_3-w)}{(1-w)(1+3w)}.
\]
In particular \(K_w(x,N)=(1+3x_3)/(1+3w)\). The \(L^\infty\) operator norm is the supremum of \(\int|K_w(x,y)|\,d\mu_w(y)\) over \(x\in\mathbb S^2\), because for each evaluation point the sign of the row kernel attains the operator norm of that evaluation functional, and compactness gives a maximum.

Write \(z=x_3\). For uniform \(y\in\mathbb S^2\), the scalar \(K_w(x,y)\) has the same distribution as \(a+bU\), where \(U\) is uniform on \([-1,1]\),
\[
a=\frac{1+2w-3wz}{(1-w)(1+3w)},\quad b=\frac{3\sqrt{(1+3w)^2(1-z^2)+(z-w)^2}}{(1-w)(1+3w)}>0.
\]
For \(0<w<1\), one has \(b>|a|\) for all \(-1\le z\le1\): the difference of their squared numerators is a concave quadratic in \(z\) with strictly positive endpoint values. Thus \(\frac12\int_{-1}^1|a+bU|\,dU=(a^2+b^2)/(2b)\). Adding the atomic kernel contribution and substituting \(r=w/(1+3w)\), \(t=1+3z\), yields exactly the displayed \(F_r(t)\). In particular \(q_r>0\) on the whole interval, since it is concave with positive endpoint values \(q_r(-2)=(1-2r)^2\) and \(q_r(4)=(1-4r)^2\).

**2. Finite algebraic critical-point reduction.** On either \((-2,0)\) or \((0,4)\), direct differentiation gives
\[
F'_r(t)=\frac{P_r(t)}{12q_r(t)^{3/2}}+r\operatorname{sgn}(t).
\]
Hence each interior critical point satisfies \(R_r(t)=0\). Its degree is six, with leading coefficient \(16r^4(3r-2)^2(4r-3)^2/9>0\). The only possible nonsmooth interior point is \(t=0\), so the finite set of candidate values contains every maximizer. Conversely every listed candidate is a legal evaluation latitude, so taking the maximum yields exactly \(\Lambda_w\).

**3. A calibration minimum and the local antipodal threshold.** Substitution shows \(q_r(0)=u_r(0)=1\), whence \(F_r(0)=5/3\) and \(F'_r(0^-)=-8r/9<0<F'_r(0^+)=10r/9\). At \(t=-2\), the row norm is \(H(r)\), and the one-sided derivative into the interval is
\[
F'_r(-2^+)=\frac{8r(r-1)^2(6r-1)}{9(2r-1)^3}.
\]
This is positive for \(r<1/6\) and negative for \(r>1/6\), so the endpoint is a strict local maximum precisely for \(r>1/6\), equivalently \(w>1/3\). At \(r=1/6\), the derivative vanishes but \(F''_r(-2^+)=5/48>0\), excluding a local maximum. Moreover
\[
F_{1/6}(5/4)-H(1/6)=-\frac{113}{72}+\frac{2795\sqrt{581}}{41832}>0.
\]
Therefore local antipodal maximality begins strictly before global antipodal norming.

**4. Endpoint limits, off-antipodal normers, and coexistence.** At \(r=0\), \(F_0\equiv5/3\). Uniform first-order expansion on \([-2,4]\) gives \(F_r(t)=5/3+r\phi(t)+O(r^2)\), where \(\phi(t)=(-4t^2+10t)/9\) for \(t\ge0\) and \(\phi(t)=(-4t^2-8t)/9\) for \(t\le0\). The first branch has the unique global maximum \(25/36\) at \(t=5/4\); the second has maximum \(4/9\). Uniform convergence, strict curvature near \(5/4\), and the implicit function theorem produce the unique norming latitude for all sufficiently small positive \(r\).

At the other limit \(r\uparrow1/4\), \(q_{1/4}(t)=(4-t)(5t+12)/48\). The continuous limiting row function is \(F_{1/4}\), with value \(1\) at \(t=4\). On \([-2,0]\) and \([0,4]\), respectively, the exact nonnegative factorizations
\[
36q_{1/4}(t)(2+t/4)^2-(9q_{1/4}(t)+u_{1/4}(t)^2)^2=\frac{(4-t)(t+2)(8t^2+29t+44)}8,
\]
\[
36q_{1/4}(t)(2-t/4)^2-(9q_{1/4}(t)+u_{1/4}(t)^2)^2=\frac{(4-t)(8t^3-15t^2-42t+88)}8
\]
show \(F_{1/4}(t)\le2\), with equality only at \(t=-2\). Indeed the first quadratic has negative discriminant, and in the second cubic substituting \(s=t-2\in[-2,2]\) gives \(8s^3+33s^2-6s+8\ge17s^2-6s+8>0\). The inequality is strict also at \(t=4\), where the direct limiting value is \(1\). Continuity is uniform up to \(t=4\) because the numerator ratio is bounded by a multiple of \(\sqrt q\) near that endpoint. Consequently \(\Lambda_w\to2\), and the unique limiting maximizer is the antipode. Moreover, its inward derivative is strictly negative at \(r=1/4\), so a uniform local comparison and compactness imply the antipode remains the unique global normer for every \(r\) sufficiently near \(1/4\) from below.

For existence of an actual global coexistence weight, let \(S\) be the set of \(r\in[1/6,1/4)\) for which \(F_r(-2)=\max_tF_r(t)\). This set is nonempty near \(1/4\), while the strict comparison at \(1/6\) excludes an open right neighborhood of \(1/6\). Put \(r_* =\inf S\in(1/6,1/4)\). Continuity gives antipodal global maximality at \(r_*\). Because \(F'_{r_*}(-2^+)<0\), this maximizer is strictly isolated from other possible maximizers in a neighborhood of \(-2\). The fact that antipodal global maximality fails at parameters arbitrarily below \(r_*\), compactness of maximizing positions, and passage to a subsequence then produce a second global maximizer at some \(t_*>-2\). The inverse substitution \(w_*=r_*/(1-3r_*)\) proves \(w_*\in(1/3,1)\).

## Verification
The companion `checker.py` executes symbolic polynomial identities, verifies the degree-six critical polynomial, its calibration and endpoint derivatives, the two limiting polynomial factorizations, and independent numerical integration of the original spherical kernel for 35 parameter/evaluation pairs. For five rational weights it compares evaluation at every real critical root with dense independent sampling. Symbolic identities cover the full parameter domain where stated; numerical tests are corroboration, not an infinite proof. Run with `python checker.py` using Python, SymPy, and SciPy.

## Relationship to prior work
The rank-one reproducing-kernel update itself is classical and **not claimed as original**: Fernández, Pérez, Piñar and Xu, arXiv:0801.0065, Theorem 1 and kernel formula (6), derive multivariate Uvarov modifications; Delgado et al., arXiv:0911.2818, treat several mass points and Jacobi-simplex kernels. Hangelbroek et al., arXiv:1005.2424, study boundedness of manifold least-squares projectors in substantially different kernel spaces. The claims here add a complete finite algebraic *sharp endpoint norm* evaluation for the specified mixed measure and a proved separation between local and global norming transitions. Neither the generic kernel update alone nor broad projector boundedness supplies these optimization and phase statements without further mathematical analysis.

## Limitations
The assertions concern one positive point mass added to uniform spherical area, real affine approximation, and \(\mathbb S^2\). They do not classify every stationary latitude, identify a unique global transition weight, give a simple closed formula for the coexistence weight, or cover multiple atoms, nonuniform continuous weights, higher degrees, or higher-dimensional spheres. The phase-transition existence proof is nonconstructive, while each fixed-weight norm is reduced to finitely many real roots. Equivalent prior results in less-indexed literature remain a research risk; no independent mathematical audit is claimed.

## References
1. L. Fernández, T. E. Pérez, M. A. Piñar and Y. Xu, *Krall-type Orthogonal Polynomials in Several Variables*, arXiv:0801.0065v1 (public 2007-12-29), especially section 3 and formula (6). https://arxiv.org/abs/0801.0065
2. A. M. Delgado, L. Fernández, T. E. Pérez, M. A. Piñar and Y. Xu, *Orthogonal Polynomials in Several Variables for Measures with Mass Points*, arXiv:0911.2818v1 (public 2009-11-15), especially section 2. https://arxiv.org/abs/0911.2818
3. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424v1 (public 2010-05-13), sections 4–5. https://arxiv.org/abs/1005.2424
