# Critical Hilbert–Schmidt continuum limit of generalized Cesàro differences

## Finding
For fixed real \(a,b>0\), let \(C_t\) denote the generalized discrete Cesàro operator on \(\ell^2(\mathbb N_0)\) defined below. Set \(A_\varepsilon=C_{1-a\varepsilon}-C_{1-b\varepsilon}\) and embed the lattice isometrically as step functions of mesh \(\varepsilon\) in \(L^2(0,\infty)\). After extending the resulting operator by zero on the orthogonal complement, the step-function embedding of \(A_\varepsilon\) converges **in Hilbert–Schmidt norm** to the integral operator
\[
(H_{a,b}f)(x)=\frac1x\int_0^x\bigl(e^{-a(x-y)}-e^{-b(x-y)}\bigr)f(y)\,dy.
\]
This implies convergence in \(\ell^2\) of the **entire ordered singular-value lists**, and the exact boundary metric
\[
\lim_{\varepsilon\downarrow0}\|A_\varepsilon\|_{\mathcal S_2}^2
=\|H_{a,b}\|_{\mathcal S_2}^2
=\log\frac{(a+b)^2}{4ab}
=2\log\cosh\left(\frac{\log(a/b)}2\right).
\]
For \(a\ne b\), these Hilbert–Schmidt distances do not collapse although both constituent operators converge strongly to the same noncompact classical Cesàro operator. The expression is invariant under simultaneously multiplying \(a\) and \(b\) by the same positive scalar.

## Assumptions and scope
Work over complex Hilbert spaces. For \(0\le t<1\), set
\[
(C_tf)_n=\frac1{n+1}\sum_{k=0}^nt^{n-k}f_k\qquad(n\in\mathbb N_0).
\]
For arbitrary fixed \(a,b>0\), take \(0<\varepsilon<1/\max\{a,b\}\). Write \(I_n^\varepsilon=[n\varepsilon,(n+1)\varepsilon)\), and define the isometry \(U_\varepsilon:\ell^2(\mathbb N_0)\to L^2(0,\infty)\) by \(U_\varepsilon e_n=\varepsilon^{-1/2}\mathbf1_{I_n^\varepsilon}\). Let \(\widetilde A_\varepsilon=U_\varepsilon A_\varepsilon U_\varepsilon^*\); it acts as zero on the orthogonal complement of the step-function subspace. The convergence claim is for this isometric embedding, not for an unembedded discrete operator. If \(a=b\), both operators vanish and all assertions hold trivially. The singular sequences count multiplicity, and zeros may be appended.

## Proof
**1. Exact Hilbert–Schmidt Gram formula.** Since \(t<1\), summing the squared matrix entries gives
\[
\langle C_t,C_s\rangle_{\mathcal S_2}
=\sum_{n=0}^\infty\frac1{(n+1)^2}\sum_{j=0}^n(ts)^j
=F(ts),\qquad
F(q)=\frac{\zeta(2)-\operatorname{Li}_2(q)}{1-q}.
\]
Here \(\zeta(2)=\sum_{m=1}^\infty m^{-2}\) and \(\operatorname{Li}_2(q)=\sum_{m=1}^\infty q^m/m^2\). The formula is valid for \(0\le t,s<1\) and \(0\le q<1\). Hence
\[
\|A_\varepsilon\|_{\mathcal S_2}^2
=F((1-a\varepsilon)^2)+F((1-b\varepsilon)^2)
-2F((1-a\varepsilon)(1-b\varepsilon)).\tag{1}
\]
By differentiation of the dilogarithm,
\[
\zeta(2)-\operatorname{Li}_2(1-\eta)
=\int_0^\eta\frac{-\log u}{1-u}\,du
=\eta(1-\log\eta)+O\bigl(\eta^2|\log\eta|\bigr)
\]
as \(\eta\downarrow0\). Therefore \(F(1-\eta)=1-\log\eta+O(\eta|\log\eta|)\). Applying this to the three arguments of (1), with respective deficits \(2a\varepsilon+O(\varepsilon^2)\), \(2b\varepsilon+O(\varepsilon^2)\), and \((a+b)\varepsilon+O(\varepsilon^2)\), yields
\[
\|A_\varepsilon\|_{\mathcal S_2}^2
=\log\frac{(a+b)^2}{4ab}
+O_{a,b}\bigl(\varepsilon|\log\varepsilon|\bigr).\tag{2}
\]

**2. The continuous kernel and its norm.** For \(x>y>0\), define
\[
K_{a,b}(x,y)=\frac{e^{-a(x-y)}-e^{-b(x-y)}}x,
\]
and set it to zero for \(x\le y\). Changing to \(u=x-y\) and integrating over \(x\ge u\), Tonelli gives
\[
\int_0^\infty\int_0^x|K_{a,b}(x,y)|^2\,dy\,dx
=\int_0^\infty\frac{(e^{-au}-e^{-bu})^2}{u}\,du.
\]
This integral is finite: near zero the numerator is \(O(u^2)\), while at infinity it decays exponentially. Applying Frullani's identity to \(e^{-2au}-2e^{-(a+b)u}+e^{-2bu}\) evaluates it as \(2\log(a+b)-\log(2a)-\log(2b)\), which agrees with (2). Thus \(H_{a,b}\) is Hilbert–Schmidt and has the asserted squared norm.

**3. Norm convergence, not just a scalar asymptotic.** The integral kernel of \(\widetilde A_\varepsilon\) is
\[
K_\varepsilon(x,y)=\begin{cases}
\dfrac{(1-a\varepsilon)^{n-k}-(1-b\varepsilon)^{n-k}}{\varepsilon(n+1)},&x\in I_n^\varepsilon,\ y\in I_k^\varepsilon,\ k\le n,\\
0,&\text{otherwise}.
\end{cases}
\]
For almost every \((x,y)\) with \(0<y<x\), \(\varepsilon(n+1)\to x\), \(\varepsilon(n-k)\to x-y\), and the two powers tend to their corresponding exponentials. Thus \(K_\varepsilon(x,y)\to K_{a,b}(x,y)\) almost everywhere. Equation (2) proves that the \(L^2((0,\infty)^2)\) norms of these kernels converge to the \(L^2\) norm of the limiting kernel. A bounded sequence in \(L^2\) converging almost everywhere has that limit as its weak \(L^2\) limit (truncate test functions and use uniform integrability on sets of finite measure). Weak convergence together with convergence of norms in a Hilbert space implies strong convergence. Hence
\[
\|\widetilde A_\varepsilon-H_{a,b}\|_{\mathcal S_2}
=\|K_\varepsilon-K_{a,b}\|_{L^2((0,\infty)^2)}\longrightarrow0.
\]
For any two compact Hilbert–Schmidt operators, the singular-value perturbation inequality gives \(\sum_{j\ge1}|s_j(T)-s_j(S)|^2\le\|T-S\|_{\mathcal S_2}^2\); apply it to the embedded operators. Isometric embedding preserves all nonzero singular values, proving the full-list assertion.

**4. Strong-limit contrast.** Every \(C_t\) is dominated entrywise by the classical Cesàro operator \(C_1\), whose norm on \(\ell^2\) is \(2\). Thus \(\sup_{0\le t<1}\|C_t\|\le2\). On finitely supported vectors, dominated convergence of the output sequences gives \(C_t f\to C_1 f\) in \(\ell^2\), and uniform boundedness extends this to all vectors. For \(a\ne b\), equation (2) nevertheless gives a strictly positive Hilbert–Schmidt limit for their difference. The scale invariance follows immediately from the formula; for \(a\approx b\), the metric is asymptotic to \(\tfrac12|\log(a/b)|\).

## Verification
The accompanying `check.py` independently re-evaluates the finite Hilbert–Schmidt Gram identity using exact rational arithmetic, evaluates the asymptotic squared norm numerically at decreasing meshes, and checks the continuous Frullani integral against its closed form. These computations test normalization and finite algebra only: the limit and infinite-dimensional singular-value statement are proved above. The checker uses only Python's standard library.

## Relationship to prior work
Rhaly's original generalized Cesàro matrix work establishes basic Hilbert–Schmidt properties and discusses lack of norm convergence at the classical endpoint. Curbera and Ricker study compactness, fine spectra and operator norms in broad Banach sequence-space classes, including the \(\ell^2\) setting. The 2023 continuation by Albanese, Bonet and Ricker addresses spectra and dynamics in nonnormable sequence spaces; it motivates testing how a two-rate boundary approach behaves in a Hilbert ideal rather than in the underlying strong operator topology. The present claim concerns a **two-parameter critical boundary layer** in Hilbert–Schmidt geometry and convergence of all singular values under mesh embedding, rather than spectra of a single fixed parameter or the known endpoint operator-norm discontinuity. Standard Hilbert–Schmidt kernel and singular-value perturbation theorems are ingredients, not the claimed specific identification. Historical priority of the equivalent two-parameter boundary-layer formulation remains uncertain.

## Limitations
The theorem assumes fixed positive \(a,b\) and a common mesh tending to zero; it does not give a uniform statement when either rate itself depends on \(\varepsilon\), nor an explicit closed formula for the individual singular values of \(H_{a,b}\). The \(\ell^2\) convergence is for singular-value lists after the stated embedding, not trace-norm convergence. No independent mathematical audit has been performed.

## References
1. H. C. Rhaly Jr., “Generalized Cesàro Matrices,” *Canadian Mathematical Bulletin* 27 (1984), 417–422. https://doi.org/10.4153/CMB-1984-064-5
2. G. P. Curbera and W. J. Ricker, “Fine spectra and compactness of generalized Cesàro operators in Banach lattices in \(\mathbb C^{\mathbb N_0}\),” first public arXiv version 17 February 2023, arXiv:2302.08750. https://arxiv.org/abs/2302.08750
3. A. A. Albanese, J. Bonet and W. J. Ricker, “Spectral properties of generalized Cesàro operators in sequence spaces,” first public arXiv version 8 May 2023, arXiv:2305.04805. https://arxiv.org/abs/2305.04805
