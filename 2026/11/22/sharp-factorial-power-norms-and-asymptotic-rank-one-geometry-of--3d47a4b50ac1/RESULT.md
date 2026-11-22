# Sharp factorial power norms and asymptotic rank-one geometry of polynomial Hardy Volterra operators

## Finding
Let \(H^2(\mathbb D)\) be the Hardy Hilbert space with orthonormal basis \(1,z,z^2,\ldots\). Let
\[
g(z)=\sum_{j=1}^{d}a_jz^j,\qquad a_j\ge 0,\quad a_1>0,
\]
where at least two coefficients are positive. Put \(S=\{j:a_j>0\}\), \(G=\sum_j a_j\), \(p_j=a_j/G\), \(\mu=\sum_j jp_j\), \(\sigma^2=\sum_j(j-\mu)^2p_j>0\), and
\[
h=\gcd\{j-j_0:j\in S,\ j\ne j_0\},
\]
where \(j_0\) is any element of \(S\). The positive integer \(h\) does not depend on that choice. Define the analytic Volterra operator
\[
(T_gf)(z)=\int_0^z f(w)g'(w)\,dw
\]
and the rank-one operator \((R_kf)(z)=f(0)g(z)^k/k!\) for integers \(k\ge1\).

**Theorem.** For every fixed polynomial in this class,
\[
\boxed{\lim_{k\to\infty}\frac{k!\,k^{1/4}}{G^k}\,\|T_g^k\|
=\left(\frac{h^2}{4\pi\sigma^2}\right)^{1/4}.}
\]
More precisely, writing \(D=\sum_{j=1}^{d}ja_j\), the operator-norm error satisfies the explicit all-\(k\) bound
\[
\boxed{\|T_g^k-R_k\|\le
\frac{D\,G^{k+1}}{a_1^2(k+1)k!}.}
\]
Consequently
\[
\frac{\|T_g^k-R_k\|}{\|T_g^k\|}=O_g(k^{-3/4}),\qquad
\frac{s_2(T_g^k)}{s_1(T_g^k)}=O_g(k^{-3/4}),
\]
where singular values are in nonincreasing order. Equivalently, after scaling by \(k!/\|g^k\|_{H^2}\), the \(k\)-th power is within \(O_g(k^{-3/4})\) in operator norm of the rank-one map \(f\mapsto f(0)g^k/\|g^k\|_{H^2}\). The target vector is allowed to depend on \(k\): no convergence of these changing rank-one targets is claimed.

For the entire binomial subfamily \(g(z)=z+a z^m\), \(a>0\) and integer \(m\ge2\), the leading power-norm constant is independent of \(m\):
\[
\boxed{\|T_g^k\|\sim\frac{(1+a)^k}{k!}
\left(\frac{(1+a)^2}{4\pi ak}\right)^{1/4}.}
\]
The support spacing affects the number of contributing unit-circle saddle points, but cancels the corresponding increase in the degree variance for this binomial family.

## Assumptions and scope
All operators act on the **complex** Hardy space \(H^2(\mathbb D)\). The polynomial has finitely many nonnegative real coefficients, a strictly positive linear coefficient, and at least one additional positive coefficient. The coefficient-space norm is \(\|f\|_{H^2}^2=\sum_{n\ge0}|\widehat f(n)|^2\). No normalization of \(G\) is imposed. Constants in \(O_g(\cdot)\) may depend on the fixed polynomial, not on \(k\). The single-monomial case has \(\sigma^2=0\) and is excluded from the Gaussian formula.

## Proof
**1. Exact power kernel.** For every analytic \(f\) and integer \(k\ge1\), repeated integration and the fundamental theorem of calculus give
\[
T_g^kf(z)=\frac1{(k-1)!}\int_0^z
f(w)g'(w)[g(z)-g(w)]^{k-1}\,dw.
\]
Indeed, assuming the formula for \(k\), exchange the integrations on the triangular segment and integrate \(g'(u)[g(u)-g(w)]^{k-1}\) in \(u\). This is an algebraic identity and does **not** require the polynomial \(g\) to be injective. In particular, \(T_g^k1=g^k/k!\).

**2. A uniform rank-one remainder.** Set \(w=tz\) in the preceding formula and subtract the constant part \(f(0)\). For \(|z|=1\) and \(0\le t\le1\), coefficient positivity gives
\[
|zg'(tz)|\le D,\qquad
|g(z)-g(tz)|\le\sum_j a_j(1-t^j)
=G-g(t)\le G-a_1t.
\]
By orthogonality of the Hardy monomials,
\[
\|f(t\cdot)-f(0)\|_{H^2}^2
=\sum_{n\ge1}|\widehat f(n)|^2t^{2n}
\le t^2\|f\|_{H^2}^2.
\]
Minkowski's inequality for boundary \(L^2\), followed by a positive beta-integral, now gives
\[
\begin{aligned}
\|(T_g^k-R_k)f\|_{H^2}
&\le\frac{D\|f\|_{H^2}}{(k-1)!}
\int_0^1t(G-a_1t)^{k-1}\,dt\\
&\le \frac{D\|f\|_{H^2}}{(k-1)!}
\int_0^{G/a_1}t(G-a_1t)^{k-1}\,dt\\
&=\frac{D G^{k+1}}{a_1^2(k+1)k!}\|f\|_{H^2}.
\end{aligned}
\]
For the second inequality, \(G/a_1\ge1\) and the extended integrand is nonnegative. All estimates extend from polynomials to \(H^2\) by continuity. Boundedness of \(T_g\) itself also follows directly from the finite sum of Hilbert–Schmidt shifts \(z^n\mapsto ja_jz^{n+j}/(n+j)\).

**3. Exact boundary saddle count.** Parseval gives
\[
\|g^k\|_{H^2}^2
=\frac1{2\pi}\int_{-\pi}^{\pi}|g(e^{i\theta})|^{2k}\,d\theta.
\]
The triangle inequality gives \(|g(e^{i\theta})|\le G\). Equality holds precisely when the complex numbers \(e^{ij\theta}\), for \(j\in S\), share one argument. Thus the maximizers are exactly the \(h\) roots of unity \(\theta=2\pi r/h\) modulo \(2\pi\). At each such point, putting \(u\) for angular displacement,
\[
G^{-2}|g(e^{i(\theta+u)})|^2
=\left|\sum_{j\in S}p_je^{iju}\right|^2
=1-\sigma^2u^2+O_g(u^4).
\]
Since \(\sigma^2>0\), all maxima are nondegenerate; off fixed neighborhoods of them, compactness of the circle gives a uniform strict upper bound below \(G\). The elementary Gaussian Laplace method at all \(h\) maxima therefore yields
\[
\|g^k\|_{H^2}^2
=G^{2k}\frac{h}{2\sqrt{\pi\sigma^2 k}}\bigl(1+O_g(k^{-1})\bigr),
\]
and hence
\[
\|R_k\|=\frac{G^k}{k!}
\left(\frac{h^2}{4\pi\sigma^2k}\right)^{1/4}
\bigl(1+O_g(k^{-1})\bigr).
\]

**4. Operator norms and singular collapse.** As \(\|T_g^k\|-\|R_k\|\) is bounded in absolute value by \(\|T_g^k-R_k\|\), Step 2 divided by the last formula is \(O_g(k^{-3/4})\). This proves the sharp power-norm asymptotic. Every \(T_g^k\) is compact, and the variational characterization of singular values gives \(s_2(T_g^k)\le\|T_g^k-R_k\|\), while \(s_1(T_g^k)=\|T_g^k\|\); the claimed singular ratio follows. For \(g(z)=z+az^m\), the support difference is \(h=m-1\) and \(\sigma^2=(m-1)^2a/(1+a)^2\), giving the displayed binomial formula.

## Verification
The accompanying `verify.py` is a self-contained Python-standard-library checker. It compares two distinct exact coefficient representations of the repeated-integral formula for several genuinely nonmonomial rational-coefficient polynomials, verifies \(k!T_g^k1=g^k\) exactly, checks the finite Laplace coefficient ratios, and checks exact support-rescaling invariance of the binomial \(H^2\) norm. Running `python verify.py` completed **168 assertions**. Additionally, finite matrix singular-value computations for \(g(z)=z+0.3z^2\) and \(g(z)=z+z^2\) at powers 2, 5, 10 and 20 showed decreasing relative rank-one errors. These are supplementary finite tests, not a proof of the infinite-dimensional theorem; the proof is Steps 1–4 above.

## Relationship to prior work
Chalmoukis and Stylogiannis (first public 4 May 2020; published 2021) prove boundedness and quasi-nilpotency of generalized Volterra operators for multiplier symbols on coefficient-sequence spaces. Their Theorem 1.2 supplies a qualitative spectral framework, but no leading factorial power-norm constant or changing-rank-one approximation for the positive-polynomial class. Peláez, Rättyä and Wu (2023) study nonnegative-coefficient symbols in **mapping problems from weighted Dirichlet spaces into \(H^\infty\)**, not iterated Hardy-operator norm asymptotics. Eveson's 2003 and 2004/2005 papers establish sharp high-power asymptotics and rank-one approximations for **real-variable Volterra convolution operators on \(L^p(0,1)\)**. Those important analogues are credited; their convolution hypotheses and underlying function spaces do not imply the stated Hardy-space result, in particular the exact boundary-circle arithmetic multiplicity and variance coefficient. No universal claim of historical uniqueness is made.

## Limitations
The theorem does not treat arbitrary complex or signed coefficients, symbols with no linear term, nonpolynomial symbols, or varying symbols as \(k\to\infty\). No optimal second singular-value coefficient or convergence rate better than the stated upper bound is asserted. The classical Gaussian Laplace expansion is invoked only after its nondegeneracy and localization hypotheses have been verified. Originality is assessed against the cited primary texts and available indexed results; unindexed equivalent results remain possible. No independent external mathematical audit has been performed.

## References
1. N. Chalmoukis and G. Stylogiannis, *Quasi-nilpotency of Generalized Volterra Operators on Sequence Spaces*, first posted 4 May 2020, arXiv:2005.01660; *Results in Mathematics* 76 (2021), article 173, DOI: 10.1007/s00025-021-01482-7. https://arxiv.org/abs/2005.01660
2. J. Á. Peláez, J. Rättyä and F. Wu, *Volterra-type operators mapping weighted Dirichlet space into H-infinity*, *Mathematische Zeitschrift* 304 (2023), article 31, DOI: 10.1007/s00209-023-03290-x. https://doi.org/10.1007/s00209-023-03290-x
3. S. P. Eveson, *Asymptotic behaviour of iterates of Volterra operators on L-p(0,1)*, arXiv:math/0409516 (27 September 2004); *Integral Equations and Operator Theory* 53 (2005), 331–341. https://arxiv.org/abs/math/0409516
4. S. P. Eveson, *Norms of Iterates of Volterra Operators on L2*, *Journal of Operator Theory* 50 (2003), 369–386. https://jot.theta.ro/jot/archive/2003-050-002/2003-050-002-010.pdf
