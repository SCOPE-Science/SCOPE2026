# Curvature removes rational-angle spatial locking in Feres random circular billiards

## Finding
Let \(N\geq7\) be an integer, \(\alpha=\pi/N\), and \(0<\theta<\alpha\). Consider the Feres random reflection system on the boundary of a geodesic disk of radius \(r\) in either the hyperbolic plane of curvature \(-1\), with \(r>0\), or the unit sphere of curvature \(+1\), with \(0<r<\pi/2\). The boundary coordinate \(s\) is the polar angle, taken modulo \(2\pi\); the initial state \((s,\theta)\) is deterministic.

Define \(a=4\alpha-\theta\), \(b=2\alpha+\theta\) and the angular jump functions
\[
\Gamma_{-,r}(v)=2\operatorname{atan2}(\sin v,\cosh r\cos v),\qquad
\Gamma_{+,r}(v)=2\operatorname{atan2}(\sin v,\cos r\cos v),
\]
where \(\operatorname{atan2}(y,x)\in(0,\pi)\) for \(y>0\). For either curvature sign, put
\[
E_{\pm}(N,\theta)=\left\{r:\frac{\Gamma_{\pm,r}(a)-\Gamma_{\pm,r}(b)}{2\pi}\in\mathbb Q\right\}
\]
inside its admissible radius domain. **Each set \(E_{\pm}(N,\theta)\) is countable.** For every radius outside that set and every deterministic initial boundary position, the one-time boundary-position law at collision \(n\) converges weakly to normalized arclength measure as \(n\to\infty\). In fact, for every fixed nonzero integer Fourier mode \(k\), its expectation decays exponentially in \(n\), with a mode-, angle- and radius-dependent rate.

Conversely, for every fixed admissible positive radius, at most countably many \(\theta\in(0,\alpha)\) belong to the displayed exceptional resonance set. In the Euclidean disk, for every *rational* \(\theta/\pi\) with rational \(\alpha/\pi\), the boundary-coordinate law is instead supported on a fixed finite subgroup translate at every collision and cannot converge weakly to arclength. Thus both signs of nonzero curvature generically remove this rational-angle obstruction, although the full billiard with rational \(\alpha/\pi\) is not globally mixing.

The countable sets are **sufficiently inclusive exceptional sets**, not an assertion that every radius inside them fails spatial convergence. The theorem neither asserts total-variation convergence nor a rate uniform over Fourier modes.

## Assumptions and scope
The four angle maps and their state-dependent probabilities are the original Feres random map described in [1, Section 3] and [2, Section 3]:
\[
T_1(v)=v+2\alpha,\quad T_2(v)=-v+2\pi-4\alpha,\quad
T_3(v)=v-2\alpha,\quad T_4(v)=-v+4\alpha.
\]
Choose map \(T_i\) at angle \(v\) with probability \(p_i(v)\), using the normalized definition \(u_\beta(v)=\tfrac12(1+\tan\beta/\tan v)\) from [1, equation (2)]. The probability functions \(p_i\) are given piecewise in [1, equation (2)]; in particular each admissible \(T_1/T_3\) reversal and \(T_4\) involution has positive transition probability in the interior intervals used below. A collision first changes the angle to \(v'=T_i(v)\), then advances the boundary coordinate by \(\Gamma_{\pm,r}(v')\) modulo \(2\pi\), matching the random billiard convention [2, Section 4]. Both initial and subsequent angles remain in \((0,\pi)\).

The reachable angle class \(\mathcal C_\theta\) is finite for rational \(\alpha/\pi\) [1, Proposition 3.6; 2, Proposition 3.2]. Every positive-probability edge is reversible by the opposite Feres branch, hence its transition matrix \(P\) is irreducible on that finite class [1, Remark 1; 2, Remark 3.1]. Its period need not be one; the theorem concerns the position marginal, not a general unconditioned joint angular limit.

## Proof
**1. Geometry of the geodesic circle.** Fix \(0<v<\pi\). The center and consecutive collision points form an isosceles constant-curvature geodesic triangle of equal radial sides \(r\). Split it along the midpoint geodesic of the chord. The resulting right triangle, by the spherical or hyperbolic sine and cosine laws, gives, respectively,
\[
\sin^2\frac{\Gamma_{+,r}(v)}2
 =\frac{\sin^2v}{1-\sin^2r\cos^2v},\qquad
\sin^2\frac{\Gamma_{-,r}(v)}2
 =\frac{\sin^2v}{1+\sinh^2r\cos^2v}.
\]
The collision advances in the positive boundary orientation. Select the branch \(0<\Gamma<\pi\) for \(v<\pi/2\), \(\Gamma=\pi\) for \(v=\pi/2\), and \(\pi<\Gamma<2\pi\) for \(v>\pi/2\). Equivalently, the preceding \(\operatorname{atan2}\) formulas hold, since the half-jump satisfies
\[
\tan\frac{\Gamma_{-,r}(v)}2=\frac{\tan v}{\cosh r},\qquad
\tan\frac{\Gamma_{+,r}(v)}2=\frac{\tan v}{\cos r},
\]
with quadrants fixed by \(\operatorname{atan2}\). Both functions are strictly increasing and real analytic in \(v\in(0,\pi)\), and real analytic in admissible \(r\). At radius zero their common continuous limit is \(2v\).

**2. Two inequivalent positive two-step return loops.** Put \(v=2\alpha-\theta\in(\alpha,2\alpha)\) and \(a=v+2\alpha=4\alpha-\theta\in(3\alpha,4\alpha)\), \(b=4\alpha-v=2\alpha+\theta\in(2\alpha,3\alpha)\). Since \(N\geq7\), the exact transition intervals in [1, equation (2)] allow the strictly positive paths
\[
 v\xrightarrow{T_1}a\xrightarrow{T_3}v,
 \qquad v\xrightarrow{T_4}b\xrightarrow{T_4}v.
\]
For clarity, the needed positive probabilities follow directly from the normalized law: \(p_1(v)=u_\alpha(v)>0\), \(p_4(v)=u_\alpha(-v)>0\), and \(p_3(a)=u_\alpha(-a)>0\). For \(2\alpha<b<3\alpha\),
\[
2p_4(b)=1-2\cos(2\alpha)+(2\sin(2\alpha)-\tan\alpha)\cot b.
\]
Its coefficient of \(\cot b\) is positive for \(0<\alpha<\pi/6\), and the expression is zero at \(b=3\alpha\); since cotangent decreases on this interval, \(p_4(b)>0\) at its interior points. The normalized values at all these edges lie in \((0,1)\).

The first accumulates boundary jump \(\Gamma_{\pm,r}(a)+\Gamma_{\pm,r}(v)\), while the second accumulates \(\Gamma_{\pm,r}(b)+\Gamma_{\pm,r}(v)\). Their difference is precisely
\[
\Delta_{\pm,r}(\theta)=\Gamma_{\pm,r}(4\alpha-\theta)-\Gamma_{\pm,r}(2\alpha+\theta)>0.
\]
The state \(v\) is in the class of \(\theta\): the strictly positive path \(\theta\xrightarrow{T_1}\theta+2\alpha\xrightarrow{T_4}v\) reaches it.

**3. Exceptional radii are countable.** At the flat radius limit,
\[\Delta_{\pm,0}(\theta)=2(a-b)=4(\alpha-\theta)\in(0,4\alpha).\]
In positive curvature, as \(r\uparrow\pi/2\), \(\Gamma_{+,r}(a)\) and \(\Gamma_{+,r}(b)\) both approach \(\pi\), so \(\Delta_{+,r}\to0\). In negative curvature, as \(r\to\infty\), \(\Gamma_{-,r}(b)\to0\) because \(b<3\alpha<\pi/2\), whereas \(\Gamma_{-,r}(a)\to0,\pi,\text{ or }2\pi\) according as \(a<\pi/2\), \(a=\pi/2\), or \(a>\pi/2\). None of these three limits equals \(4(\alpha-\theta)\): the latter is strictly between zero and \(4\alpha\leq4\pi/7<\pi\). Thus each \(r\mapsto\Delta_{\pm,r}(\theta)\) is a nonconstant real-analytic function on its radius interval. For each rational \(q\), its level set \(\Delta_{\pm,r}(\theta)=2\pi q\) is discrete in the interval, hence countable. Their countable union is \(E_{\pm}(N,\theta)\).

For a fixed admissible \(r\), the function \(\theta\mapsto\Delta_{\pm,r}(\theta)\) is likewise nonconstant and real analytic on \((0,\alpha)\): it tends to \(0\) as \(\theta\uparrow\alpha\), and to the strictly positive difference \(\Gamma_{\pm,r}(4\alpha)-\Gamma_{\pm,r}(2\alpha)\) as \(\theta\downarrow0\). The same level-set argument proves the additional assertion about exceptional initial angles.

**4. Fourier spectral gap from return-loop disagreement.** Let \(P(x,y)\) be the finite irreducible transition matrix on \(\mathcal C_\theta\). For \(k\in\mathbb Z\setminus\{0\}\), form the twisted matrix
\[
 K_k(x,y)=P(x,y)\exp\bigl(ik\Gamma_{\pm,r}(y)\bigr).
\]
Its operator norm on \(\ell^\infty\) does not exceed one. Suppose \(K_k f=\lambda f\) with \(|\lambda|=1\). At a state where \(|f|\) is maximal, the triangle equality and irreducibility force \(|f|\) to be constant and, along every positive edge \(x\to y\),
\[
 e^{ik\Gamma_{\pm,r}(y)}f(y)=\lambda f(x).
\]
Multiplying along both length-two loops at \(v\) and cancelling the nonzero \(f(v)\) yields
\[e^{ik\Delta_{\pm,r}(\theta)}=1.\]
If \(r\notin E_{\pm}(N,\theta)\), this contradicts the irrationality of \(\Delta_{\pm,r}(\theta)/(2\pi)\). Hence \(\rho(K_k)<1\) for every fixed \(k\ne0\). Finite-dimensional spectral theory gives constants \(C_k<\infty\), \(0<q_k<1\) with \(\|K_k^n\|\le C_k q_k^n\) for all \(n\geq0\). From any point \((s,x)\) with \(x\in\mathcal C_\theta\),
\[
 \left|\mathbb E_{s,x}e^{iks_n}\right|
 =\left|e^{iks}(K_k^n\mathbf1)(x)\right|\le C_kq_k^n.
\]
The zero Fourier mode equals one. Approximation of continuous functions on the circle by trigonometric polynomials implies weak convergence of the boundary-position law to Haar measure.

**5. Flat arithmetic obstruction.** In a Euclidean disk the jump is \(\Gamma_{0,r}(w)=2w\). If both \(\alpha/\pi\) and \(\theta/\pi\) are rational, every angle in the finite reachable Feres class is a rational multiple of \(\pi\), so all jumps belong to a finite subgroup of \(\mathbb R/(2\pi\mathbb Z)\). The position law stays in the translate of that finite subgroup determined by \(s\), and cannot converge weakly to nonatomic Haar measure. This proves the contrast without asserting failure at every radius in either curved exceptional set.

## Verification
The standalone `check_curved_billiards.py` evaluates the exact Feres four-branch transition probabilities using the normalized \(u\)-function, constructs representative finite angular chains, checks stochastic row sums and positivity of both return loops, evaluates both curved angular-jump formulas, and compares a finite list of Fourier-twisted matrix spectral radii with one. It completed 966 supporting finite checks using \(N\in\{7,8,9,10,11,13\}\), three interior angle ratios, and six representative curved radii. This finite computation is **not** a proof of irrationality of the loop phase or of convergence over infinitely many modes; the analytic and spectral arguments above supply those statements.

## Relationship to prior work
Vales and Pinto-de-Carvalho [1] define the planar Feres random billiard, prove geometric and angular facts, and study density and Liouville-started laws. Vales [2] extends its geometry to constant-curvature surfaces, proves an absolutely continuous starting-measure Knudsen law and pathwise density hypotheses, and establishes a global mixing criterion based on irrationality of the reflection parameter. The theorem here concerns **a single fixed starting collision position and angle**, for **rational reflection parameter**, and finds a **curvature-radius-dependent, countable-exception weak spatial convergence law** absent from those inspected statements. It is distinct from the known planar conditional law, which excludes rational angles rather than showing their generic curved equidistribution. Global invariant angular classes remain intact; no global mixing for rational \(\alpha/\pi\) follows.

## Limitations
The exceptional set is an explicit countable resonance superset of possible non-equidistributing radii; its points have not been exhaustively classified. Convergence is weak only, not in total variation (the law at each finite time is atomic). Exponential decay applies to each fixed Fourier mode, not uniformly in the mode or in \(N,\theta,r\). Geodesic disks are restricted to radius less than \(\pi/2\) on the sphere. The originating formulas and finite irreducible angle classes are used; there is no claim about general reflecting curves, randomized initial angular distributions or global system mixing. Scholarly priority remains subject to comparison with unindexed or inaccessible literature.

## References
[1] T. Vales and S. Pinto-de-Carvalho, *A Random Billiard Map in the Circle*, arXiv:2005.01892 (first public 2020; inspected arXiv v4, 2022), especially Sections 3, 5 and 6. https://arxiv.org/abs/2005.01892

[2] T. Vales, *Random circular billiards on surfaces of constant curvature: Pseudo integrability and mixing*, arXiv:2212.00872 (first public 2022-12-01; inspected v2, 2024), especially Sections 2–6. https://arxiv.org/abs/2212.00872
