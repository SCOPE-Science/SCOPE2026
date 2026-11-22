# A dimension-sixteen anisotropy inversion for Santaló products of shifted-cube polars

## Finding
For an integer \(n\ge 2\) and a displacement vector \(t=(t_1,\ldots,t_n)\in(-1,1)^n\), define the shifted cube and its polar cross-polytope by
\[
Q_t=\prod_{i=1}^n[t_i-1,t_i+1],\qquad
K_t=Q_t^\circ=\operatorname{conv}\left\{\frac{e_i}{1+t_i},-\frac{e_i}{1-t_i}:1\le i\le n\right\}.
\]
Let \(s(t)\) be the unique Santaló point of \(K_t\), and set
\[
\mathcal M_n(t)=\operatorname{vol}_n(K_t)\operatorname{vol}_n\big((K_t-s(t))^\circ\big).
\]
The following fourth-order expansion holds with a uniform sixth-order remainder in a neighborhood of the origin (for each fixed \(n\)):
\[
\boxed{\begin{aligned}
\log\frac{n!\,\mathcal M_n(t)}{4^n}
={}&-\frac{n-1}{2(n+2)}\sum_{i=1}^nt_i^2
+\frac{9(n+1)}{4(n+2)^3}\left(\sum_{i=1}^nt_i^2\right)^2\\
&+\frac{n^3-12n^2-51n-28}{20(n+2)^3}\sum_{i=1}^nt_i^4
+O_n(\|t\|_2^6).
\end{aligned}}
\]
In particular, \(s(t)=-3t/(n+2)+O_n(\|t\|_2^3)\).

**Sharp local anisotropy ordering.** Write \(q_i=t_i^2\). There exists a radius \(\varepsilon_n>0\) such that, throughout \(0\le\sum_iq_i<\varepsilon_n\), the map \(q\mapsto\log\mathcal M_n(t)\) is strictly Schur-*concave* for \(2\le n\le15\), and strictly Schur-*convex* for \(n\ge16\). Here the map depends only on \(q\), not on the signs of the coordinates of \(t\). In particular, at any fixed squared imbalance \(\sum_i t_i^2=\rho^2\), with \(0<\rho<\sqrt{\varepsilon_n}\):

- If \(2\le n\le15\), the *smallest* Santaló volume product occurs exactly for one nonzero coordinate of magnitude \(\rho\), and the *largest* occurs exactly when every coordinate has magnitude \(\rho/\sqrt n\).
- If \(n\ge16\), these two extremal classes exchange places: equal coordinate magnitudes minimize and a single nonzero coordinate maximizes.

The equality statements are up to coordinate permutations and independent sign changes. The strict inequalities hold for all other squared-coordinate allocations on the same simplex; the assertion is local in \(\rho\), not global for arbitrary displacements.

## Assumptions and scope
All volumes are ordinary \(n\)-dimensional Lebesgue volumes. The polar of an origin-containing convex body \(K\) is \(K^\circ=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\); its Santaló point is the unique minimizer of \(s\mapsto\operatorname{vol}_n((K-s)^\circ)\) over \(\operatorname{int}K\). Because \(|t_i|<1\), the shifted cube contains the origin and the polar \(K_t\) is full-dimensional. The subscripted \(O_n\) constants may depend on the fixed dimension; the existence of \(\varepsilon_n\) does not assert a dimension-uniform lower bound. The norm is Euclidean.

The question is geometric, involving centered polar volumes and anisotropy of opposite axial vertices, rather than the inverse-problem optimization objective used to produce related shifted-zonotope regularizers. The first public motivating source was dated 12 November 2026.

## Proof
**1. Primal volume and perspective polar identity.** Each of the \(2^n\) orthants of \(K_t\) is an axis-aligned simplex. Adding their determinants yields
\[
\operatorname{vol}_n(K_t)
=\frac{1}{n!}\prod_{i=1}^n\left(\frac1{1+t_i}+\frac1{1-t_i}\right)
=\frac{2^n}{n!}\prod_{i=1}^n(1-t_i^2)^{-1}.
\tag{1}
\]
For \(s\in\operatorname{int}K_t\), the perspective map \(y\mapsto y/(1-\langle s,y\rangle)\) is a diffeomorphism from \(Q_t\) onto \((K_t-s)^\circ\). Its Jacobian equals \((1-\langle s,y\rangle)^{-(n+1)}\). With independent uniform variables \(U_i\in[-1,1]\), therefore,
\[
\operatorname{vol}_n((K_t-s)^\circ)=2^n F_n(s,t),\qquad
F_n(s,t)=\mathbb E\left(1-\sum_{i=1}^ns_i(U_i+t_i)\right)^{-(n+1)}.
\tag{2}
\]
The denominator is positive throughout \(Q_t\) for the admissible centers \(s\). At \(t=0\), the unique minimizer is \(s=0\). The Hessian with respect to \(s\) there is \((n+1)(n+2)I/3\), so the analytic implicit-function theorem gives an analytic local minimizer \(s(t)\). Strict convexity of polar volume identifies it with the global Santaló center. Reflection in each coordinate implies \(s_i(t)\) is odd in \(t_i\) and even in all other \(t_j\); hence \(s(t)=O_n(\|t\|)\).

**2. Fourth-order expansion.** Let \(c=n+1\), \(b=\sum_i s_it_i\), \(v=\sum_i s_i^2\), and \(w=\sum_i s_i^4\). Since \(\mathbb EU_i^2=1/3\) and \(\mathbb EU_i^4=1/5\), the fourth central moment of \(\sum_i s_iU_i\) is \(v^2/3-2w/15\). Expanding \((1-z)^{-c}\) and retaining terms of total degree at most four (with \(s=O_n(t)\)) yields
\[
\begin{aligned}
F_n(s,t)=1
&+cb+\frac{c(c+1)}6v
+\frac{c(c+1)}2b^2
+\frac{c(c+1)(c+2)}6bv\\
&+\frac{c(c+1)(c+2)(c+3)}{24}
\left(\frac{v^2}{3}-\frac{2w}{15}\right)
+O_n(\|t\|^6).
\end{aligned}\tag{3}
\]
The quadratic form in \(s\) is minimized uniquely at
\[
s_0(t)=-\frac3{n+2}t,
\tag{4}
\]
and the true minimizer differs from \(s_0(t)\) by \(O_n(\|t\|^3)\). The quadratic term's first derivative vanishes at \(s_0\), so this correction affects the minimum only at order six. Substituting (4) into (3), and then using
\[
\log\frac{n!\,\mathcal M_n(t)}{4^n}
=\log F_n(s(t),t)-\sum_i\log(1-t_i^2)
\tag{5}
\]
gives the displayed coefficients after collecting \(\big(\sum t_i^2\big)^2\) and \(\sum t_i^4\). The combined remainder is sixth order: all odd degrees vanish under simultaneous sign reversal, while analyticity supplies a convergent even expansion near the origin.

**3. Strict local Schur order.** Since independent coordinate reflections preserve the volume product, \(G_n(q):=\log\mathcal M_n(t)\) is a real analytic symmetric function of \(q_i=t_i^2\) near \(q=0\). Denote the coefficient of \(\sum_iq_i^2\) in the fourth-order formula by
\[
\beta_n=\frac{n^3-12n^2-51n-28}{20(n+2)^3}.
\]
For any \(i\ne j\), permutation symmetry makes the numerator \(\partial_{q_i}G_n-\partial_{q_j}G_n\) divisible analytically by \(q_i-q_j\). The quotient equals
\[
\frac{\partial_{q_i}G_n(q)-\partial_{q_j}G_n(q)}{q_i-q_j}
=2\beta_n+O_n\left(\sum_k|q_k|\right),
\tag{6}
\]
including its continuous value on the diagonal. The cubic polynomial \(p(n)=n^3-12n^2-51n-28\) is negative for integers \(2\le n\le15\) and positive for every integer \(n\ge16\): \(p(15)<0<p(16)\), while \(p'\) has just one positive zero between 9 and 10, after which \(p\) increases. Thus a sufficiently small common simplex neighborhood makes every quotient in (6) strictly negative or strictly positive, respectively. The differentiable Schur criterion gives strict Schur-concavity or Schur-convexity. The vector \((\rho^2,0,\ldots,0)\) majorizes every nonnegative vector of sum \(\rho^2\), while \((\rho^2/n,\ldots,\rho^2/n)\) is majorized by every such vector. Strictness of the criterion yields precisely the asserted equality classes.

## Verification
Run `python3 check_anisotropy.py` using Python 3, SymPy and mpmath. It independently reassembles the Taylor coefficients from the fourth moment, checks their exact simplified identities and the integer sign transition, evaluates the Santaló minimizer for both extreme allocations using high-precision moment-generating series for sums of independent uniforms, and checks those series against direct one-dimensional quadrature. The current saved checker returns `ANISOTROPY_CHECKS_OK ... total_checks= 11`. The numerical checks include dimensions \(2,3,15,16\), where both sides of the transition are tested. They are corroboration, not a proof of the infinite-dimensional statement; the analytic sign and Schur arguments provide that proof.

## Relationship to prior work
Metya, Leong and Soh (arXiv:2611.16142v1, 12 November 2026, especially §8.2 and Theorem 8.6) identify the polar of a shifted zonotope as an optimal convex regularizer for paired-basis atomic data. Their formulation motivates this explicit geometry but does not calculate Santaló products or compare anisotropy at fixed squared displacement.

Pavlov and Telen (arXiv:2402.18955, especially §1 and the polar-volume rationality framework) establish the general semialgebraic geometry of Santaló centers. That framework alone does not state the fourth-order coefficient or the dimension-sixteen reversal for the specific family.

The public result *Universal Santaló displacement and sharp Mahler response of unequal-height bipyramids* treats an unequal *single* apex pair above a common equatorial body, yielding an exact one-coordinate second-order deficit. Its specific asymmetric cross-polytope specialization corresponds to \(t=(\delta,0,\ldots,0)\); it does not compare simultaneous imbalances or determine the mixed fourth-order coefficient that changes the minimizing allocation. *Strict Mahler-product monotonicity along simplex asymmetric difference bodies* instead concerns a different simplex-reflection Minkowski sum. The classical Meyer–Reisner shadow-system theorem concerns convexity/monotonicity along deformations, not the fixed-Euclidean-imbalance Schur sign reversal. These results are credited rather than represented as independent parts of the new statement.

## Limitations
This is a *local* anisotropy classification at a fixed squared displacement, not a global claim for all \(t\in(-1,1)^n\). No dimension-uniform threshold is provided. The explicit sixth-order remainder controls only fixed dimensions. The prior-literature comparison checks closely related statements and records but cannot rule out differently named unindexed priority; the full older shadow-system article was inspected through its published abstract, not its entire text. No independent mathematical audit has been performed.

## References
1. N. Metya, O. Leong and Y. S. Soh, *Gradient Flows over Convex Bodies for Learning Optimal Regularizers*, arXiv:2611.16142v1, publicly posted 12 November 2026, Theorem 8.6 and §8.2, https://arxiv.org/html/2611.16142v1.
2. D. Pavlov and S. Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955, 2024, especially §1 and the polar-volume formula, https://arxiv.org/pdf/2402.18955.
3. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, *Mathematika* 53 (2006), 129–148, DOI:10.1112/S0025579300000061.
4. *Universal Santaló displacement and sharp Mahler response of unequal-height bipyramids*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-santal-displacement-and-sharp-mahler-response-of-unequ--d98e8b7c23bd.
5. *Strict Mahler-product monotonicity along simplex asymmetric difference bodies*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-mahler-product-monotonicity-along-simplex-asymmetric-diff--516fa817d276.
