# Sharp bounded-variation norm and off-centre rigidity of quadratic Jacobi projection

## Finding
For each real \(p>0\), equip \((-1,1)\) with the symmetric Jacobi probability measure
\[
 d\mu_p(x)=\frac{(1-x^2)^{p-1}}{B(1/2,p)}\,dx,
\]
and let \(P_p\) be the \(L^2(\mu_p)\)-orthogonal projector onto real polynomials of degree at most two. For real \(BV(-1,1)\), use the **unweighted distributional total-variation seminorm** \(V(f)=|Df|((-1,1))\). Write
\[
 c=2p+3,\qquad
 u_+=\frac{c^2-c+4+\sqrt{(c^2-c+4)^2-4(c-2)c^2}}{2(c-2)c^2},
 \qquad a_p=\sqrt{u_+}.
\]
Then \(1/\sqrt c<a_p<1\), and the **exact, attained sharp seminorm amplification** is
\[
\boxed{\sup_{V(f)>0}\frac{V(P_pf)}{V(f)}
 =\frac{2p+1}{2pB(1/2,p)}(1-a_p^2)^p
 \left(ca_p+\frac1{ca_p}\right).}
\]
All extremizers, modulo almost-everywhere equality and addition of constants, are nonzero scalar multiples of a single step at \(+a_p\) or \(-a_p\). In particular the maximizing jump is **strictly off-centre for every** \(p>0\): no centrally located step is extremal. Moreover,
\[
 \lim_{p\downarrow0}\|P_p\|_{V\to V}=\frac53,\qquad
 \lim_{p\to\infty}\frac{\|P_p\|_{V\to V}}p
 =\sqrt{\frac2{\pi e}},\qquad
 \lim_{p\to\infty}\sqrt{2p+3}\,a_p=1.
\]
At uniform weight \(p=1\), the sharp norm is approximately \(1.63318209583481\), attained for jumps at \(\pm0.52034121962315\). This is a norm of **output variation**, not a range-violation or uniform-error bound.

## Assumptions and scope
The input is a real essentially defined function in \(BV(-1,1)\), with its usual distributional derivative. A constant has zero input and output variation because \(P_p1=1\). The measure is a probability law (the harmless normalization does not change the orthogonal projector). The integrable weight exponent \(p-1\) may be any real number greater than \(-1\). The output is a real quadratic polynomial, so its variation is the integral of the absolute derivative over \((-1,1)\). The degree is fixed at two; no general higher-degree or nonsymmetric Jacobi statement is made.

## Proof
**1. Kernel and exact response to a jump.** Symmetric beta integration gives
\[
 v=\mathbb E_{\mu_p}X^2=\frac1{2p+1},\quad
 \mathbb E_{\mu_p}X^4=\frac3{(2p+1)(2p+3)},\quad
 w=\operatorname{Var}_{\mu_p}(X^2)
 =\frac{4p}{(2p+1)^2(2p+3)}.
\]
Thus \(1,x,x^2-v\) are mutually orthogonal, and the reproducing kernel is
\[
 K_p(t,s)=1+\frac{ts}v+\frac{(t^2-v)(s^2-v)}w.
\]
For \(-1<a<1\), define \(H_a(s)=\mathbf1_{[a,1)}(s)\). Differentiate \(P_pH_a(t)=\int_a^1K_p(t,s)d\mu_p(s)\) and use the exact primitive identities
\[
 \int_a^1s\,d\mu_p(s)=\frac{(1-a^2)^p}{2pB(1/2,p)},\quad
 \int_a^1(s^2-v)d\mu_p(s)
 =\frac{a(1-a^2)^p}{(2p+1)B(1/2,p)}.
\]
They give the affine derivative
\[
 (P_pH_a)'(t)=A_p(a)(1+cat),\qquad
 A_p(a)=\frac{2p+1}{2pB(1/2,p)}(1-a^2)^p.
\tag{1}
\]
Consequently, for \(b=|ca|\), integration of an affine absolute value yields the **exact step gain**
\[
 F_p(a)=V(P_pH_a)=A_p(a)J(b),\qquad
 J(b)=\begin{cases}2,&0\le b\le1,\\b+b^{-1},&b>1.\end{cases}
\tag{2}
\]
The function \(F_p\) is even, vanishes as \(|a|\to1\), and its centered value is \(F_p(0)=2A_p(0)\).

**2. Global maximization over the jump.** It suffices to put \(a\in[0,1]\). On \([0,1/c]\) equation (2) is strictly decreasing away from zero. On \((1/c,1)\), differentiation of \((1-a^2)^p(ca+1/(ca))\), with \(u=a^2\), shows that its derivative has the **opposite sign** of
\[
 Q_c(u)=(c-2)c^2u^2-(c^2-c+4)u+1.
\tag{3}
\]
The exact evaluations
\[
 Q_c(c^{-2})=\frac{2(c-3)}{c^2}>0,
 \quad Q_c(c^{-1})=-\frac4c<0,
 \quad Q_c(1)=(c-3)(c^2+1)>0
\]
show that \(Q_c\) has exactly two roots \(u_-\in(c^{-2},c^{-1})\) and \(u_+\in(c^{-1},1)\). Therefore \(F_p\) decreases to a local minimum at \(\sqrt{u_-}\), increases to its sole positive off-centre local maximum at \(a_p=\sqrt{u_+}\), then decreases to zero. Only \(F_p(0)\) and \(F_p(a_p)\) remain as possible global maxima.

The latter is **strictly larger for every** \(c>3\). Indeed, evaluate at \(a=c^{-1/2}\) to obtain
\[
 \frac{F_p(c^{-1/2})}{F_p(0)}
 =\frac{c+1}{2\sqrt c}\left(1-\frac1c\right)^{(c-3)/2}=R(c).
\]
For \(c>3\), elementary logarithmic bounds \(\log(1-z)>-z/(1-z)\) for \(0<z<1\), and \(\log(1+z)\ge2z/(2+z)\) for \(z\ge0\), imply
\[
 \log R(c)>\frac{(c-1)^2}{c^2+6c+1}
 -\frac{c-3}{2(c-1)}
 =\frac{(c-3)^3-4(c-3)+16}{2(c-1)(c^2+6c+1)}>0.
\]
The last numerator is positive: for \(0\le t=c-3\le2\), \(t^3-4t+16\ge8\); for \(t\ge2\), \(t^3-4t+16\ge16\). Hence \(F_p(a_p)>F_p(c^{-1/2})>F_p(0)\). Together with the sign analysis, this proves that the *only* maximizers of the step gain are \(\pm a_p\), with the claimed exact value.

**3. All BV inputs and equality.** For an arbitrary real \(BV(-1,1)\) function, its signed Stieltjes derivative is a finite measure \(Df\), and up to almost-everywhere equality it has a representation as a constant plus a superposition of interior Heaviside steps \(H_a\). Since the projection preserves constants and equation (1) is continuous in \(a\), Fubini and the triangle inequality give
\[
 \begin{aligned}
 V(P_pf)&=\int_{-1}^1\left|\int_{(-1,1)}(P_pH_a)'(t)\,dDf(a)\right|dt\\
 &\le\int_{(-1,1)}F_p(a)\,d|Df|(a)
 \le F_p(a_p)V(f).
 \end{aligned}
\]
A unit jump at either \(a_p\) or \(-a_p\) attains the bound. Equality in the final inequality forces \(Df\) to be supported on \(\{-a_p,a_p\}\). The two affine derivative profiles \(1\pm ca_pt\) are positive together near \(t=0\) but have opposite signs near an endpoint, so any combination with nonzero coefficients at both sites gives strict loss in the integrated triangle inequality. Thus one jump (plus an arbitrary constant) is necessary and sufficient.

**4. Weight-parameter limits.** As \(p\downarrow0\), the upper root \(u_+\to1\), with \(1-u_+=\Theta(p)\). Also \(pB(1/2,p)\to1\), hence \(A_p(a_p)\to1/2\) and \(J(ca_p)\to3+1/3\), proving the limit \(5/3\). As \(p\to\infty\), the displayed quadratic has \(u_+\sim1/c\), so \(pa_p^2\to1/2\), \((1-a_p^2)^p\to e^{-1/2}\), and \(B(1/2,p)\sim\sqrt{\pi/p}\). Therefore \(A_p(a_p)\sim\sqrt{p/(\pi e)}\) and \(J(ca_p)\sim\sqrt{2p}\), proving the linear-growth constant and the jump-location limit.

## Verification
Execute `python3 verify_jacobi_bv.py` from the same directory. The standard-library checker independently integrates Jacobi moments by exact rational polynomial expansion for integer shapes, checks all derivative coefficients, scans the global maximizer across the parameter regimes, independently integrates the absolute affine derivative, and tests the variation inequality on 7,500 random signed step combinations. It also checks both limiting regimes numerically. These finite calculations corroborate the exact identities; the preceding proof, not their sample count, establishes the unrestricted assertions.

## Relationship to prior work
The classical symmetric Jacobi and ultraspherical basis and kernel are well established. Kaber's 2006 work addresses the large-degree Gibbs overshoot and steepness for a fixed sign input; it does not give a degree-two sharp unweighted BV seminorm over all input functions. The 2011 survey of Kopotun–Leviatan–Prymak–Shevchuk concerns constrained shape-preserving approximation, whereas the operator here is an unconstrained orthogonal projection. A closely related published analysis, *Sharp two-branch monotone range envelope for quadratic symmetric Jacobi projection* (published-finding corpus, 2026), gives the exact step-response polynomial and optimizes its **range** over jump and evaluation positions; it does not state, or optimize, the integrated absolute derivative in (2). The distinction matters: its range optimizers can change branches with the Jacobi weight, whereas the present BV optimizer is always one strictly off-centre step and yields a different exact norm. *Two-term endpoint growth and Gaussian scaling of quadratic ultraspherical projection* (published-finding corpus, 2026) optimizes the \(L^\infty\) kernel mass and its large-parameter corrections; the BV norm here is taken with respect to **unweighted distributional input variation** and is not the \(L^1\) or \(L^\infty\) operator norm. The common elementary reproducing kernel does not itself determine the global maximization and strict off-centre criterion.

## Limitations
The result is degree-two only, for real-valued inputs, symmetric Jacobi probability measures and unweighted variation on an open interval. It does not assert a sharp Sobolev norm, shape preservation, uniform-error bounds, any theorem for asymmetric weights, or uniformity as polynomial degree also grows. The prior-work comparison is based on the named accessible documents and indexed searches, not an exhaustive historical-priority certificate; an unindexed equivalent TV theorem remains possible. The finite computational diagnostics are not a replacement for proof.

## References
1. S. M. Kaber, *The Gibbs Phenomenon for Jacobi Expansions*, Communications in Applied Analysis **10** (2006), 133–148, https://www.acadsol.eu/en/articles/10/2/3.pdf.
2. K. A. Kopotun, D. Leviatan, A. Prymak, I. A. Shevchuk, *Uniform and Pointwise Shape Preserving Approximation by Algebraic Polynomials*, arXiv:1109.0968v1 (public 2011-09-05), https://arxiv.org/abs/1109.0968.
3. C. P. Calderón and W. Urbina, *On Abel Summability of Jacobi Polynomials Series, the Watson Kernel and Applications*, arXiv:1207.4524v1 (public 2012-07-18), https://arxiv.org/abs/1207.4524.
4. *Sharp two-branch monotone range envelope for quadratic symmetric Jacobi projection*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-two-branch-monotone-range-envelope-for-quadratic-symmetric--68d5f845db4a.
5. *Two-term endpoint growth and Gaussian scaling of quadratic ultraspherical projection*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-term-endpoint-growth-and-gaussian-scaling-of-quadratic-ultra--c29cf166ae49.
