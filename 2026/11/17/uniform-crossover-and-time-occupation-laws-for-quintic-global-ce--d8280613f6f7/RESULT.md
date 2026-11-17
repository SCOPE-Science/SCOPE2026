# Uniform crossover and time-occupation laws for quintic global centers

## Finding
Consider the real polynomial differential system
\[
\dot x=v,\qquad \dot v=-x-\alpha x^3v^2-\beta x^5,
\quad \alpha\ge0,\quad\beta>0.
\]
For every amplitude \(A>0\), its solution from \((x,v)=(A,0)\) is periodic; let \(T_{\alpha,\beta}(A)\) denote its **minimal period in original physical time**. Set \(q=\alpha A^4\), and define the positive functions
\[
I_q(u)=\int_u^1r^5e^{qr^4/2}\,dr,\quad
J_q(u)=\int_u^1r e^{qr^4/2}\,dr,\qquad 0\le u<1,
\]
\[
\Phi(q)=2\sqrt2\int_0^1\frac{e^{qu^4/4}}{\sqrt{I_q(u)}}\,du.
\]
The following **uniform, all-parameter comparison** holds for every \(A>0\), \(\beta>0\), and \(\alpha\ge0\):
\[
\boxed{\quad
\frac{\Phi(\alpha A^4)}{\sqrt{1+3/(\beta A^4)}}
\ \le\ A^2\sqrt\beta\,T_{\alpha,\beta}(A)
\ \le\ \Phi(\alpha A^4).\quad}
\tag{1}
\]
In particular, for every fixed \(\beta>0\) and **every** sequence of amplitudes \(A\to\infty\) with \(\alpha=\alpha_A\ge0\), the ratio of the middle expression in (1) to \(\Phi(\alpha_A A^4)\) converges to 1, **uniformly over all possible \(\alpha_A\)**; its relative error is at most \(3/(2\beta A^4)\).

The crossover function \(\Phi\) is continuously differentiable and strictly decreasing on \([0,\infty)\), with the exact limits
\[
\boxed{\Phi(0)=\frac{2\sqrt3}{3}\mathrm B\!\left(\tfrac16,\tfrac12\right),
\qquad \lim_{q\to\infty}\sqrt q\,\Phi(q)=2\pi.}
\tag{2}
\]
Here \(\mathrm B\) is the Euler beta function. Thus the new continuous crossover resolves the nonuniform transition between the pure-quintic high-amplitude scale and the positive velocity-coupling scale established for **fixed** parameters in preceding work.

There is also a **physical-time occupation crossover**. If a point is sampled uniformly during one original-time period and \(U_A=|x|/A\), then, whenever \(A\to\infty\) and \(\alpha_A A^4\to q\in[0,\infty)\), the law of \(U_A\) converges weakly to the density
\[
\boxed{\rho_q(u)=\frac{e^{qu^4/4}/\sqrt{I_q(u)}}{\int_0^1e^{qs^4/4}/\sqrt{I_q(s)}\,ds},\qquad 0<u<1.}
\tag{3}
\]
At the conservative endpoint, \(\rho_0(u)\) is proportional to \((1-u^6)^{-1/2}\). As \(q\to\infty\), the law in (3) concentrates at \(u=1\), and its refined turning-point layer \(Z_q=q(1-U_q)\), for \(U_q\) sampled with density \(\rho_q\), converges to
\[
\boxed{g(z)=\frac2\pi\frac{e^{-z}}{\sqrt{1-e^{-2z}}},\qquad z>0.}
\tag{4}
\]
The sign of \(x\) under uniform physical-time sampling is symmetric at every amplitude, so the signed normalized position converges to an equally weighted pair of turning points after the subsequent \(q\to\infty\) limit.

## Assumptions and scope
The parameters \(\beta>0\) and \(\alpha\ge0\) are arbitrary, and \(A>0\). The amplitude-dependent family \(\alpha_A\) in the limiting statements may vary without any smoothness or monotonicity condition. Every comparison concerns the **unrescaled original time**; only the displayed amplitude and probability variables are normalized. Formula (1) is nonasymptotic. All results concern the global-center locus within the six-parameter quintic family classified by da Cruz and Llibre, with primary MSC 34C05. The density statements are weak-convergence claims under uniform sampling of the physical-time phase, not claims about every pointwise trajectory at a fixed phase.

## Proof
**1. Energy, global periodicity and exact time quadrature.** Define
\[
p_\alpha(x)=e^{\alpha x^4/4},\quad
V_{\alpha,\beta}(x)=\int_0^x e^{\alpha s^4/2}(s+\beta s^5)\,ds,\quad
H(x,v)=\tfrac12 p_\alpha(x)^2v^2+V_{\alpha,\beta}(x).
\]
Since \(p_\alpha'/p_\alpha=\alpha x^3\), direct differentiation along the vector field gives \(\dot H=0\). The potential is even, strictly increasing on positive arguments, and coercive. Each level \(H=V(A)>0\) is a single compact regular oval, carrying one nonstationary periodic trajectory with turning points \(\pm A\). Its minimal physical period is
\[
T_{\alpha,\beta}(A)=4\int_0^A\frac{p_\alpha(x)}{\sqrt{2[V_{\alpha,\beta}(A)-V_{\alpha,\beta}(x)]}}\,dx.
\tag{5}
\]

**2. Exact scaled identity and the uniform kernel comparison.** Substituting \(x=Au\) in (5) and setting \(q=\alpha A^4\), \(\varepsilon=(\beta A^4)^{-1}\), gives the exact identity
\[
A^2\sqrt\beta\,T_{\alpha,\beta}(A)
=2\sqrt2\int_0^1\frac{e^{qu^4/4}}{\sqrt{I_q(u)+\varepsilon J_q(u)}}\,du.
\tag{6}
\]
For fixed \(u<1\), the ratio \(I_q(u)/J_q(u)\) is the expectation of \(r^4\) under the probability density proportional to \(r\exp(qr^4/2)\) on \([u,1]\). Its derivative with respect to \(q\) equals \(\tfrac12\operatorname{Var}(r^4)\ge0\). Consequently
\[
\frac{I_q(u)}{J_q(u)}\ge\frac{I_0(u)}{J_0(u)}
=\frac{1+u^2+u^4}{3}\ge\frac13.
\tag{7}
\]
In particular \(0<J_q(u)/I_q(u)\le3\), **independently of both \(q\) and \(u\)**. Factoring \(I_q\) out of (6) and using
\[
\frac1{\sqrt{1+3\varepsilon}}
\le\frac1{\sqrt{1+\varepsilon J_q(u)/I_q(u)}}\le1
\]
proves (1), with \(1-(1+t)^{-1/2}\le t/2\) giving the relative error. The constant \(3\) in the elementary kernel ratio is attained at \(q=u=0\); no assertion is made that the induced period error constant is globally optimal.

**3. Strict crossover monotonicity and the finite endpoint.** Write \(w_q(u)=e^{qu^4/4}/\sqrt{I_q(u)}\). Differentiating under the integral gives, for each \(0\le u<1\),
\[
\frac{\partial}{\partial q}\log w_q(u)
=\frac14\left[u^4-\frac{\int_u^1r^9e^{qr^4/2}\,dr}{\int_u^1r^5e^{qr^4/2}\,dr}\right]<0,
\tag{8}
\]
because the weighted average of \(r^4\) strictly exceeds \(u^4\). For \(q\) in a compact interval, \(w_q\) and its derivative are bounded by a constant times \((1-u^6)^{-1/2}\), allowing differentiation and yielding \(\Phi'(q)<0\). At \(q=0\), \(I_0(u)=(1-u^6)/6\), so \(\Phi(0)=2\sqrt2\sqrt6\,\mathrm B(1/6,1/2)/6\), the first equality in (2).

**4. The infinite endpoint and turning-point law.** Put \(z=q(1-u)\) for \(q>0\), and define \(D_q(z)=\tfrac q2[1-(1-z/q)^4]\), for \(0\le z\le q\). Then the exact change of variables gives
\[
\frac{w_q(1-z/q)}{\sqrt q}
=\frac{e^{-D_q(z)/2}}{\sqrt{\int_0^z(1-v/q)^5e^{-D_q(v)}\,dv}}=:K_q(z).
\tag{9}
\]
For each fixed \(z>0\), \(K_q(z)\to K_\infty(z)=\sqrt2e^{-z}/\sqrt{1-e^{-2z}}\). For \(q\ge2\) and \(0\le z\le q\), the elementary inequalities \(z/2\le D_q(z)\le2z\), together with \((1-v/q)^5\ge1/32\) for \(0\le v\le\min(z,1)\), give
\[
0<K_q(z)\le C\frac{e^{-z/4}}{\sqrt{\min(z,1)}}.
\]
Extending \(K_q\) by zero for \(z>q\), dominated convergence yields
\[
\sqrt q\,\Phi(q)=2\sqrt2\int_0^qK_q(z)\,dz
\longrightarrow 2\sqrt2\cdot\sqrt2\int_0^\infty\frac{e^{-z}}{\sqrt{1-e^{-2z}}}\,dz=2\pi.
\]
The identity \(\int_0^\infty e^{-z}(1-e^{-2z})^{-1/2}\,dz=\pi/2\) follows by \(s=e^{-z}\). The probability density of \(Z_q=q(1-U_q)\) is exactly \(K_q(z)/\int_0^qK_q(v)\,dv\), so the same dominated convergence proves (4). Tightness of \(Z_q\) gives \(U_q\to1\) in probability.

**5. Occupation crossover for amplitude-dependent parameters.** Along the outgoing and incoming quarter-arcs, \(dt/dx=p_\alpha(x)/\sqrt{2[V(A)-V(x)]}\) in absolute value. By symmetry each original-time period contains four such traversals. Thus the density of \(U_A=|x|/A\) is precisely the integrand of (6), normalized by its integral. For \(q_A=\alpha_A A^4\to q<\infty\), its numerator converges pointwise to \(w_q(u)\), while \(I_{q_A}(u)\ge(1-u^6)/6\) supplies an integrable majorant for bounded \(q_A\); since \(\varepsilon_A\to0\), dominated convergence gives (3) and weak convergence. The vector field is odd under \((x,v)\mapsto(-x,-v)\); a half-period shift swaps signs, proving sign symmetry.

## Verification
The standalone `verify_crossover.py` derives \(\dot H=0\) symbolically and checks the exact beta endpoint numerically, strict crossover decrease at representative values, convergence toward the \(2\pi\) endpoint, 18 finite-amplitude instances of the uniform comparison, and 16 independent kernel-ratio instances. Executing the supplied source produces `CHECK_OK`. These finite checks are not used as proofs of the all-parameter statements; their proofs are the identities, positive variance, dominated-convergence arguments, and inequalities above.

## Relationship to prior work
Da Cruz and Llibre [1] classify the global centers of the six-parameter quintic family and identify this two-parameter locus, but do not analyze the double scaling of its physical period or position occupation. A subsequently published period theorem [2] establishes monotone periods and the *fixed-parameter* high-amplitude endpoints, using an energy quadrature and a positive-coupling boundary layer. Those established results and tools are acknowledged here. Neither fixed-parameter limit alone provides the uniform all-parameter two-sided comparison (1), the continuous finite \(q\) crossover and its strict response (2), or the corresponding physical-time probability density (3). The endpoint \(\sqrt q\,\Phi(q)\to2\pi\) is compatible with, and uses a boundary-layer method closely related to, [2]; this endpoint method alone is not claimed as a novel technique. Beléndez and collaborators [3] solve the uncoupled quintic oscillator, which corresponds to the \(q=0\) endpoint only. Yang and Zeng [4] study broad Liénard period criteria, but their accessible abstract does not address this particular two-scale limit.

## Limitations
The theorem assumes \(\beta>0\). It does not address \(\beta=0\), non-global quintic centers, forced systems, perturbations, or other observables beyond the stated time-sampled coordinate. The error estimate controls the **relative** scaled period and is uniform in the velocity-coupling parameter; the occupation limit (3) assumes \(q_A\) has a finite limit. An analogous occupation law for arbitrary oscillatory or nonperiodic initial data is not asserted. The exact crossover density is a limit of uniform physical-time sampling, not a statistical claim about experimental ensembles. An inaccessible full text of a general period-function paper [4] and potentially unindexed equivalent formulations remain publication-priority risks; no exhaustive literature claim is made.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1, first public 2023-12-09, https://arxiv.org/html/2312.05709v1 .
2. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, publicly archived mathematical research result, 2026-10-11, published-finding corpus record ffe383da977f (fixed-parameter period classification).
3. A. Beléndez et al., *Closed-Form Exact Solutions for the Unforced Quintic Nonlinear Oscillator*, Advances in Mathematical Physics (2017), doi:10.1155/2017/7396063 .
4. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proc. Royal Soc. Edinburgh Sect. A 143 (2013), 205–221, doi:10.1017/S0308210511000096 (abstract inspected; full text not obtained).
