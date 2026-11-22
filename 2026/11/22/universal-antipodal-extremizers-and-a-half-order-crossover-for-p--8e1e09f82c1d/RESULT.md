# Universal antipodal extremizers and a half-order crossover for Poisson-mixture approximation

## Finding

Let \(\mathbb T=\mathbb R/\mathbb Z\), with normalized Lebesgue measure, and let \(V(f)=|Df|(\mathbb T)\) be the ordinary *circular* total variation of a real periodic function \(f\in BV(\mathbb T)\). For \(0\le r\le1\), write \(P_r\) for the circle Poisson convolution whose Fourier multiplier is \(r^{|n|}\) at nonzero integer frequency \(n\), with \(P_0\) the mean projection and \(P_1\) the identity. Given any Borel probability measure \(\nu\) on \([0,1]\) satisfying \(\nu([0,1))>0\), define \(T_\nu f=\int_{[0,1]}P_r f\,d\nu(r)\) and \(m_n=\int_{[0,1]}r^n\,d\nu(r)\). The exact operator norm of the approximation error is
\[
\boxed{\sup_{V(f)>0}\frac{\|f-T_\nu f\|_{L^2(\mathbb T)}}{V(f)}=C_\nu,\qquad
C_\nu^2=\frac1{2\pi^2}\sum_{j=0}^{\infty}\frac{(1-m_{2j+1})^2}{(2j+1)^2}.}
\]
Every nonconstant equality case is, up to almost-everywhere equality, a nonzero multiple of an indicator of a semicircle, plus an arbitrary constant:
\[
\boxed{f(x)=a+b\,\mathbf1_{[\theta,\theta+1/2)}(x),\quad a\in\mathbb R,\ b\in\mathbb R\setminus\{0\},\ \theta\in\mathbb T.}
\]
The rigidity holds for **every** nonidentity positive mixture, including mixtures with an atom at \(r=0\) or \(r=1\).

For the single-radius Poisson means \(\nu=\delta_r\), write \(H(z)=[\operatorname{Li}_2(z)-\operatorname{Li}_2(-z)]/2\) for \(0\le z\le1\). Then
\[
\boxed{C_r^2=\frac{H(1)-2H(r)+H(r^2)}{2\pi^2},\qquad H(1)=\frac{\pi^2}{8},\quad C_0=\frac14,}
\]
and \(C_r^2\) is strictly decreasing for \(0<r<1\), with
\[
\frac{d}{dr}C_r^2=\frac1{2\pi^2r}\log\!\left(\frac{1+r^2}{(1+r)^2}\right),\qquad
C_r^2\sim\frac{\log2}{2\pi^2}(1-r)\quad(r\uparrow1).
\]

A consequential special case is the fractional Poisson semigroup \(S_{\alpha,t}\) with Fourier multiplier \(\exp(-t|n|^\alpha)\), for \(0<\alpha\le1\) and \(t>0\). Its sharp squared approximation constant is
\[
\boxed{C_\alpha(t)^2=\frac1{2\pi^2}\sum_{j=0}^{\infty}\frac{\bigl(1-e^{-t(2j+1)^\alpha}\bigr)^2}{(2j+1)^2},}
\]
with exactly the same semicircle extremizers for every exponent and time. As \(t\downarrow0\), **three sharply distinct regimes** occur:
\[
\boxed{
C_\alpha(t)^2\sim
\begin{cases}
\displaystyle\frac{(1-2^{-(2-2\alpha)})\zeta(2-2\alpha)}{2\pi^2}\,t^2,&0<\alpha<1/2,\\[5pt]
\displaystyle\frac{t^2\log(1/t)}{2\pi^2},&\alpha=1/2,\\[5pt]
\displaystyle\frac{\Gamma(1-1/\alpha)\left(1-2^{1/\alpha-1}\right)}{2\pi^2}\,t^{1/\alpha},&1/2<\alpha<1,\\[5pt]
\displaystyle\frac{\log2}{2\pi^2}\,t,&\alpha=1.
\end{cases}}
\]
Every displayed coefficient is strictly positive. This gives a sharp half-order transition between quadratic, quadratic-logarithmic and fractional-power error laws.

## Assumptions and scope

The norm \(\|\cdot\|_2\) is with respect to probability measure \(dx\) on the unit circle, not arc-length measure on a circle of circumference \(2\pi\). All inputs are real-valued elements of \(BV(\mathbb T)\), modulo almost-everywhere equality; \(Df\) is the signed periodic distributional derivative. The variation of an indicator of a nontrivial proper arc is exactly \(2\), counting both jump endpoints. The mixture measure \(\nu\) may have arbitrary atoms and continuous parts, but must have strictly positive mass away from the identity radius \(r=1\); if \(\nu=\delta_1\), the error operator is zero and equality is nonrigid. The semigroup claim excludes \(t=0\) and \(\alpha=0\). No claim is made for complex-valued variation, nonradial kernels, negative mixture weights, or a different normalization of variation.

## Proof

**1. Reduction of any real circular BV function to arcs.** For nonconstant \(f\), its signed derivative has Jordan decomposition \(Df=\eta_+-\eta_-\) with \(\eta_+(\mathbb T)=\eta_-(\mathbb T)=V(f)/2\); the equality of masses follows from periodicity. Let \(\mu_\pm=2\eta_\pm/V(f)\) be probability measures. For ordered points \(a,b\in\mathbb T\), let \(I_{a,b}\) be the positively oriented arc from \(a\) to \(b\). The distributional derivative of its indicator is \(\delta_a-\delta_b\). Consequently
\[
f=\text{constant}+\frac{V(f)}2\int_{\mathbb T^2}\mathbf1_{I_{a,b}}\,d\mu_+(a)d\mu_-(b)
\quad\text{in }L^1(\mathbb T).
\]
The equality holds up to a constant because both sides have the same distributional derivative. The convolution error annihilates constants and is bounded on \(L^2\), so the Hilbert-space triangle inequality yields
\[
\frac{\|(I-T_\nu)f\|_2}{V(f)}\le\frac12\sup_{a,b}\|(I-T_\nu)\mathbf1_{I_{a,b}}\|_2.
\]
Translation invariance reduces the supremum to an arc of length \(d\in[0,1]\).

**2. The exact arc objective.** The nonzero Fourier coefficients of \(\mathbf1_{[0,d)}\) have squared modulus \(\sin^2(\pi nd)/(\pi^2 n^2)\). Parseval therefore gives the squared error divided by four:
\[
F_\nu(d):=\frac14\|(I-T_\nu)\mathbf1_{[0,d)}\|_2^2
=\frac1{2\pi^2}\sum_{n=1}^\infty\frac{(1-m_n)^2\sin^2(\pi nd)}{n^2}.
\]
This series converges uniformly and is symmetric under \(d\mapsto1-d\). We show that \(F_\nu\) is **strictly increasing** throughout \((0,1/2)\), for every admitted mixture, a property not available by maximizing the Fourier terms individually.

**3. Positive mixed differences and strict monotonicity.** Write \(\vartheta=2\pi d\in(0,\pi)\). For \(u\in[0,\infty]\), define
\[
A_u(\vartheta)=\sum_{n=1}^\infty\frac{e^{-un}\sin(n\vartheta)}n,
\qquad A_0(\vartheta)=\frac{\pi-\vartheta}{2},\quad A_\infty(\vartheta)=0,
\]
where the first series has its ordinary conditionally convergent meaning at \(u=0\). For finite \(u>0\), this is \(\arg(1-e^{-u}e^{-i\vartheta})\), equivalently the arctangent with positive real and imaginary denominator components. Differentiating explicitly in \(u\) proves
\[
\frac{\partial^2 A_u(\vartheta)}{\partial u^2}
=\frac{e^{-u}(1-e^{-2u})\sin\vartheta}
{\bigl(1-2e^{-u}\cos\vartheta+e^{-2u}\bigr)^2}>0.
\]
Hence \(u\mapsto A_u(\vartheta)\) is strictly convex on \((0,\infty)\), convex continuously up to the endpoints, and for any \(u,v\in(0,\infty]\),
\[
A_0(\vartheta)-A_u(\vartheta)-A_v(\vartheta)+A_{u+v}(\vartheta)>0.
\]
For finite positive \(u,v\), the difference equals the double integral of the strictly positive second derivative over \([0,u]\times[0,v]\); limiting cases with \(\infty\) follow by continuity. It is zero if \(u=0\) or \(v=0\).

Let \(R,S\) be independent with law \(\nu\), and put \(U=-\log R\), \(W=-\log S\) with \(-\log0=\infty\). Expanding \((1-m_n)^2=\mathbb E[(1-R^n)(1-S^n)]\) and differentiating the uniformly convergent integrated arc series on compact subintervals of \((0,1/2)\) gives
\[
F_\nu'(d)=\frac1{2\pi}\mathbb E\bigl[A_0(\vartheta)-A_U(\vartheta)-A_W(\vartheta)+A_{U+W}(\vartheta)\bigr]>0.
\]
For full justification when \(\nu\) has endpoint atoms, first prove the identity for fixed \(R,S\in[0,1]\), using Abel summation at radius \(1\). Each angular sine sum is uniformly bounded on compact subsets of \((0,\pi)\), independently of its radius; dominated convergence then permits integrating the fixed-radius derivative over the probability law. Because \(\nu([0,1))^2>0\), the integrand is positive on a set of positive probability. Symmetry of \(F_\nu\) therefore makes \(d=1/2\) its **unique** global maximizer. At this point all even-frequency sine terms vanish, giving the claimed odd-frequency sharp constant.

**4. Equality cases.** The upper bound of Step 1 is attained by any indicator of a semicircle because it has circular variation \(2\). If a nonconstant \(f\) attains it, equality in the pointwise upper bound inside the triangle inequality forces the positively oriented distance from \(a\) to \(b\) to be \(1/2\) for \(\mu_+\otimes\mu_-\)-almost every pair. Product independence then forces both marginals to be point masses (if all pairs are antipodal, there cannot be two distinct points in either support). Their locations are antipodal. Thus \(Df\) is a signed pair of antipodal Dirac masses, and \(f\) has exactly the asserted form. There are no further equality cases.

**5. Poisson-radius closed form.** For \(\nu=\delta_r\), evaluate the odd-index series by \(H(r)=[\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)]/2\). Direct differentiation yields
\[
\frac{d}{dr}\bigl[H(1)-2H(r)+H(r^2)\bigr]
=\frac1r\log\!\left(\frac{1+r^2}{(1+r)^2}\right).
\]
The logarithm is negative on \((0,1)\), giving strict monotonicity. Taking the derivative at \(r=1\) from the left gives the stated sharp linear boundary asymptotic; \(H(1)=\pi^2/8\) gives the endpoint \(C_0\).

**6. Fractional Poisson subordination and three critical regimes.** For \(0<\alpha<1\), the Bernstein-function identity for \(\lambda\mapsto\lambda^\alpha\) yields a probability distribution of nonnegative \(U\) such that \(\mathbb E e^{-nU}=e^{-t n^\alpha}\). The pushforward of \(U\) under \(R=e^{-U}\) is an admissible \(\nu\) on \([0,1]\), so Steps 1–4 apply. For \(\alpha=1\) take the deterministic radius \(r=e^{-t}\). This proves the exact constant and extremizers for all displayed fractional orders.

When \(0<\alpha<1/2\), divide the odd-frequency series by \(t^2\) and apply dominated convergence: the summands are bounded by \(n^{2\alpha-2}\), which are summable over odd integers. The coefficient is \((1-2^{-(2-2\alpha)})\zeta(2-2\alpha)/(2\pi^2)\). At \(\alpha=1/2\), split the sum at \(n\asymp t^{-2}\); the low-frequency part is \(t^2\sum_{n\le t^{-2},\,n\text{ odd}}n^{-1}+O(t^2)=t^2\log(1/t)+O(t^2)\), while the high-frequency tail is \(O(t^2)\). For \(1/2<\alpha\le1\), put \(\varepsilon=t^{1/\alpha}\). The odd-frequency Riemann sum, with mesh \(2\varepsilon\), converges to
\[
\frac{C_\alpha(t)^2}{t^{1/\alpha}}
\longrightarrow\frac1{4\pi^2}\int_0^\infty
\frac{(1-e^{-x^\alpha})^2}{x^2}\,dx.
\]
The integrand is integrable at zero exactly when \(\alpha>1/2\), and at infinity for every exponent. Integrating by parts and substituting \(y=x^\alpha\) gives
\[
\int_0^\infty\frac{(1-e^{-x^\alpha})^2}{x^2}\,dx
=2\int_0^\infty(e^{-y}-e^{-2y})y^{-1/\alpha}\,dy
=2\Gamma(1-1/\alpha)\bigl(1-2^{1/\alpha-1}\bigr)
\]
for \(1/2<\alpha<1\). The integral identity follows directly by subtracting the two exponentials before integration; each isolated gamma integral is not used outside its convergent range. At \(\alpha=1\), the integral instead equals \(2\log2\). This yields the remaining coefficients and shows their positivity.

## Verification

The bundled standalone `check.py` uses Python 3, SymPy and mpmath. From the bundled source it verifies the mixed-phase convexity algebra, exact half-arc curvature for single radii, the dilogarithm derivative identity, the Fourier-series closed form against bounded truncations, strict positivity for example Poisson mixtures, and each small-time regime against independently summed Fourier values. These finite checks are reproducibility checks and are not the proof of the universal statement or the limiting asymptotics; those are established in Steps 1–6.

## Relationship to prior work

Roncal–Stinga (2012) supply fractional-torus spectral and semigroup foundations, but their operator regularity and Harnack results do not give a sharp real circular BV-to-\(L^2\) approximation norm or equality classification. Carneiro–Svaiter (2013) study variation-nonexpansivity of maximal heat/Poisson convolution operators, not the present fixed-time residual norm. Gomilko–Tomilov (2014) supply general positive Bernstein semigroup subordination, a premise used to enter the fractional family, without evaluating this BV norm. Prestin–Savchuk–Shidlich (2016) give direct and inverse integral-metric estimates for Taylor–Abel–Poisson operators; their full preprint treats \(K\)-functionals and approximation order rather than this sharp equality problem. The previously published *Exact optimal two-jump Poisson leakage and its logarithmic boundary law* treats an \(L^1\) defect restricted to binary two-jump traces; the previously published *A sharp Lipschitz phase transition for fractional heat on the circle* treats the Lipschitz-to-Lipschitz norm of the semigroup, not the real BV-to-\(L^2\) norm of the error operator. None of these inspected statements implies the all-mixture sharp inequality, its complete extremizer classification and its sharp half-order asymptotics. General historical rearrangement or approximation results might contain a differently formulated equivalent; no absolute priority claim is made.

## Limitations

The result assumes a positive probability mixture of ordinary Poisson radii. A general nonnegative or contractive Fourier multiplier need not obey the mixed-difference convexity used here. The variation is *periodic* real scalar variation: using one-sided interval variation would change the normalization and extremizers. There is no assertion for arbitrary complex-valued measures, asymmetric kernels, or noncompact domains. The small-time coefficients are pointwise in fixed \(\alpha\), not uniform when the fractional exponent approaches the critical order \(1/2\). Independent mathematical and historical-priority review remain outstanding.

## References

1. L. Roncal and P. R. Stinga, *Fractional Laplacian on the torus*, arXiv:1209.6104v1, first public 2012-09-27. https://arxiv.org/abs/1209.6104
2. E. Carneiro and B. F. Svaiter, *On the variation of maximal operators of convolution type*, arXiv:1309.1529v1, first public 2013-09-06. https://arxiv.org/abs/1309.1529
3. A. Gomilko and Y. Tomilov, *On subordination of holomorphic semigroups*, arXiv:1408.1417v1, first public 2014-08-06. https://arxiv.org/abs/1408.1417
4. J. Prestin, V. Savchuk and A. Shidlich, *Direct and inverse approximation theorems of periodic functions by Taylor–Abel–Poisson means*, arXiv:1609.09615v1, first public 2016-09-30. https://arxiv.org/abs/1609.09615
5. *Exact optimal two-jump Poisson leakage and its logarithmic boundary law*, published mathematical record, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-optimal-two-jump-poisson-leakage-and-its-logarithmic-bound--5a5f88c645ff
6. *A sharp Lipschitz phase transition for fractional heat on the circle*, published mathematical record, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-lipschitz-phase-transition-for-fractional-heat-on-the-ci--4f6e1d65bde8
