# A two-thirds absolute-fluctuation transition in inverse first-passage landscapes

## Finding
Consider the family of one-dimensional overdamped diffusions designed to have the **exact** mean absorption-time profile \(\mathbb E[T_x]=A x^{\alpha}\). Although that mean diverges as the starting point \(x\) tends to infinity for every \(\alpha>0\), the **absolute variance** exhibits a sharp trichotomy at \(\alpha=2/3\): it approaches a finite positive Gamma–Beta constant below the threshold, grows logarithmically at the threshold, and grows as a specified power above it. In the finite-variance regime, a consistent spatial-independent-increment coupling of first-passage times has a nondegenerate centered \(L^2\) limit.

Fix \(A>0\) and \(0<\alpha<2\), and write
\[
a=A\alpha,\qquad b=2-\alpha,\qquad c=(ab)^{-1},\qquad p=\alpha/b.
\]
Let \(V_\alpha(x)=\operatorname{Var}(T_x)\). Then, for every \(x>0\),
\[
\boxed{\displaystyle
V_\alpha(x)=\frac{2a^2c^{-2p}}{b^2}
\int_0^{cx^b} u^{p-1}e^u\Gamma(p,u)\,du,}
\]
where \(\Gamma(p,u)=\int_u^\infty t^{p-1}e^{-t}\,dt\) is the upper incomplete Gamma function. Precisely,
\[
\boxed{\displaystyle
\begin{array}{ll}
0<\alpha<2/3:&V_\alpha(x)\longrightarrow V_\infty
=\frac{2a^2c^{-2p}}{b^2}\Gamma(2p)B(p,1-2p),\\[4pt]
\alpha=2/3:&V_\alpha(x)\sim 2a^3\log x,\\[4pt]
2/3<\alpha<2:&V_\alpha(x)\sim\frac{2a^3}{3\alpha-2}x^{3\alpha-2}.
\end{array}}
\]
In the first regime, the finite-limit error is sharp:
\[
\boxed{\displaystyle V_\infty-V_\alpha(x)\sim
\frac{2a^3}{2-3\alpha}x^{3\alpha-2}.}
\]
The special case \(A=1\), \(\alpha=1/2\) yields the explicit nonzero plateau
\[
V_\infty=\frac29\left(\frac34\right)^{2/3}\Gamma(1/3)^2
=1.3164988794270698\ldots.
\]

## Assumptions and scope
The process on \((0,\infty)\), killed upon hitting the origin, has generator
\[
\mathcal Lf(x)=f''(x)-U'(x)f'(x),\qquad
U(x)=(\alpha-1)\log x+cx^{2-\alpha}.
\]
Equivalently, \(dX_t=-U'(X_t)dt+\sqrt2\,dW_t\) until the first hit of \(0\). The potential and drift need only be regular on the **open** half-line; a logarithmic singularity at \(0\) is allowed. The boundary at \(0\) is accessible because the scale and speed densities behave respectively as \(x^{\alpha-1}\) and \(x^{1-\alpha}\), both locally integrable under the stated assumptions. The process is absorbed at that boundary. The diffusivity coefficient in the generator is exactly one, not one half. The additive constant in \(U\) is immaterial. The parameter \(\alpha=2\), involving a purely logarithmic potential and potentially divergent second moments at each fixed starting point, is **not** included in this theorem.

The comparison takes \(A\) and \(\alpha\) fixed and sends the **initial distance** \(x\to\infty\). The theorem does not assert a cutoff in temporal moments at any fixed \(x\): the first two hitting-time moments are finite for every finite \(x>0\).

## Proof
**1. The prescribed mean.** Set \(q(x)=a x^{\alpha-1}\) and \(H(x)=cx^b\), so that \(H'(x)=1/q(x)\) and \(e^{U(x)}=q(x)e^{H(x)}\). Because \(H(x)\to\infty\),
\[
\int_x^\infty e^{-U(z)}\,dz
=\int_x^\infty \frac{e^{-H(z)}}{q(z)}\,dz
=e^{-H(x)}.
\]
The standard absorbing-diffusion first-passage representation therefore gives
\[
\frac{d}{dx}\mathbb E[T_x]
=e^{U(x)}\int_x^\infty e^{-U(z)}\,dz=q(x),
\]
and \(\mathbb E[T_x]=\int_0^xq(y)\,dy=A x^\alpha\). These positive integrals also establish finite mean and almost-sure absorption.

**2. A centered second-moment identity.** The positive Green/Kac moment recursion for the same killed diffusion is
\[
M_2(x)=2\int_0^x e^{U(y)}\int_y^\infty
M_1(z)e^{-U(z)}\,dz\,dy,
\qquad M_j(x)=\mathbb E[T_x^j].
\]
It is finite for every finite \(x\): the integrand has stretched-exponential decay at infinity; at the origin \(M_1(z)e^{-U(z)}=O(z)\) and \(e^{U(y)}=O(y^{\alpha-1})\). Differentiate \(V=M_2-M_1^2\) and use integration by parts, namely
\[
\int_x^\infty M_1(z)\frac{e^{-H(z)}}{q(z)}\,dz
=M_1(x)e^{-H(x)}+\int_x^\infty q(z)e^{-H(z)}\,dz.
\]
The mean-square terms cancel and give the exact positive variance derivative
\[
\boxed{\displaystyle
V'(x)=2q(x)e^{H(x)}\int_x^\infty q(z)e^{-H(z)}\,dz.}
\]
In particular \(V(0)=0\), \(V'(x)>0\), and the normalization of the variance is fixed without an arbitrary homogeneous solution.

**3. Exact integral and all three regimes.** Substitute \(u=c z^b\) into the tail integral to obtain
\[
\int_x^\infty q(z)e^{-H(z)}\,dz
=\frac{a}{b}c^{-p}\Gamma(p,cx^b).
\]
A second substitution \(u=c y^b\) in \(\int_0^xV'(y)dy\) gives the asserted exact variance formula. Near \(u=0\), its integrand is \(\Gamma(p)u^{p-1}(1+o(1))\), hence integrable. At infinity the standard incomplete-Gamma expansion yields
\[
u^{p-1}e^u\Gamma(p,u)=u^{2p-2}(1+O(u^{-1})).
\]
This is integrable at infinity exactly when \(p<1/2\), equivalently \(\alpha<2/3\). At \(p=1/2\) it gives the logarithm, and above it gives the power, with the displayed constants after substituting \(c=(ab)^{-1}\). The same expansion, integrated from \(cx^b\) to infinity, proves the sharp subcritical remainder.

For \(p<1/2\), evaluate the plateau by Fubini:
\[
\begin{aligned}
\int_0^\infty u^{p-1}e^u\Gamma(p,u)\,du
&=\int_{0<u<v<\infty}u^{p-1}v^{p-1}e^{-(v-u)}\,du\,dv\\
&=\Gamma(2p)\int_0^1s^{p-1}(1-s)^{-2p}\,ds\\
&=\Gamma(2p)B(p,1-2p).
\end{aligned}
\]
All exchanges are justified by positivity; this integral converges precisely for \(p<1/2\).

**4. A limiting centered arrival-time random variable.** For ordered spatial levels \(0=x_0<x_1<\cdots<x_n\), the strong Markov property at successive downward hitting levels decomposes the hitting time from \(x_n\) to \(0\) into independent passage-time increments \(x_j\to x_{j-1}\). These consistent convolution laws admit an increasing, independent-increment process \(\mathcal T(x)\) with \(\mathcal T(x)\stackrel d=T_x\). The centered process \(\mathcal T(x)-A x^\alpha\) is an \(L^2\) martingale in spatial level; its variance equals \(V_\alpha(x)\). In the regime \(0<\alpha<2/3\), these variances are bounded by \(V_\infty\). Martingale convergence gives an almost-sure and \(L^2\) limit of this coupling. Its mean is zero and its variance is the strictly positive \(V_\infty\), so it is nondegenerate. In particular the centered physical marginal \(T_x-A x^\alpha\) converges weakly to this law as \(x\to\infty\).

## Verification
The standalone `checker.py` evaluates the exact variance derivative using the upper incomplete Gamma function and independently checks the backward first- and second-moment equations, the constant-force \(\alpha=1\) case, the explicit \(\alpha=3/2\) second-moment polynomial, and the Gamma–Beta plateau. It also samples the large-distance derivative asymptotic. Run `python checker.py` with Python, `mpmath`, and `sympy`. The analytic incomplete-Gamma expansion, Fubini calculation, and martingale convergence—not finite numerical tests—prove the infinite-distance claims.

## Relationship to prior work
Keidar, Reuveni and Sokolov (2026) prove uniqueness of the potential from a prescribed mean first-passage profile, including the exact power-law profile and its explicit potential. Those inverse-potential statements, the forward mean formula, and the general one-dimensional Green/Kac second-moment recursion are prior foundations here. The claim made here is instead the **evaluated second-moment variance formula, sharp critical exponent and constants, and bounded-variance centered spatial limit** for that family.

Bansaye, Collet, Martinez, Méléard and San Martin (2017/2019) analyze entrance from infinity and hitting-time fluctuations for diffusions with **uniformly bounded** first-passage means; that principal hypothesis fails for \(A x^\alpha\), which grows unbounded. Radice (2023) obtains first-passage functionals in **purely logarithmic** potentials; these correspond to the excluded quadratic-potential endpoint, not the stretched-power-plus-logarithm landscapes here. Classical backward moment equations underlie the calculation, but do not themselves state this evaluated phase boundary.

## Limitations
The result concerns fixed \(A,\alpha\), unit diffusion coefficient, the exact prescribed mean profile, an absorbing origin, and large initial distance. It does not provide finite-distance relative errors, inference stability with noisy measured means, a universality theorem for approximate power-law profiles, or a central limit theorem in the divergent-variance regimes. The a.s. centered limit is proved for a distributionally consistent spatial coupling, **not** for independent experiments or a single common-noise coupling of trajectories at all starting positions. Publication priority of the evaluated threshold remains subject to independent literature examination.

## References
- T. D. Keidar, S. Reuveni and I. M. Sokolov, *The Inverse Mean First-Passage Time Problem*, arXiv:2611.03831v1, first submitted 2026-11-02. https://arxiv.org/html/2611.03831v1
- V. Bansaye, P. Collet, S. Martinez, S. Méléard and J. San Martin, *Diffusions from Infinity*, arXiv:1711.08603v1, first submitted 2017-11-23; *Transactions of the American Mathematical Society* 372 (2019), 5781–5823. https://arxiv.org/abs/1711.08603
- M. Radice, *First-passage functionals of Brownian motion in logarithmic potentials and heterogeneous diffusion*, arXiv:2307.12699v1, first submitted 2023-07-24; *Physical Review E* 108 (2023), 044151. https://arxiv.org/abs/2307.12699
- E. Martin, U. Behn and G. Germano, *First-passage and first-exit times of a Bessel-like stochastic process*, arXiv:1007.4588v1, first submitted 2010-07-26; *Physical Review E* 83 (2011), 051115. https://arxiv.org/abs/1007.4588
