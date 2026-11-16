# Sharp half-derivative Sobolev loss for the double Fourier sphere transform

## Finding
Let \(\Phi:\mathbb T^2\to\mathbb S^2\) be the double Fourier sphere (DFS) parametrization
\[
\Phi(\lambda,\theta)=(\cos\lambda\sin\theta,\ \sin\lambda\sin\theta,\ \cos\theta),
\]
with both torus coordinates \(2\pi\)-periodic. Write \(Tf=f\circ\Phi\) for a smooth spherical function. For **every pair of real numbers** \(s,t\ge0\), the operator \(T\), initially defined on smooth functions, admits a bounded extension
\[
T:H^s(\mathbb S^2)\longrightarrow H^t(\mathbb T^2)
\]
**if and only if** \(s\ge t+\tfrac12\). The endpoint \(s=t+\tfrac12\) is included. For \(s<t+\tfrac12\), smooth functions whose spherical \(H^s\)-norms stay bounded have torus \(H^t\)-norms tending to infinity.

Equivalently, for each \(t\ge0\), the weighted Fourier-coefficient estimate
\[
\sum_{(m,n)\in\mathbb Z^2}(1+m^2+n^2)^t
  \bigl|\widehat{f\circ\Phi}(m,n)\bigr|^2
\le C_t\|f\|_{H^{t+1/2}(\mathbb S^2)}^2
\]
holds, with the standard normalized torus Fourier coefficients; replacing the source exponent \(t+\tfrac12\) by any smaller nonnegative exponent makes the estimate false. The constant \(C_t\) is not asserted optimal.

A consequence is that every spherical \(f\in H^s(\mathbb S^2)\) with \(s>\tfrac32\) has an absolutely summable DFS Fourier series, since it maps into some \(H^t(\mathbb T^2)\) with \(t>1\).

## Assumptions and scope
All Sobolev spaces are inhomogeneous \(L^2\)-based spaces on the standard round two-sphere and flat two-torus. Their norms are defined by the spectral multipliers \((1-\Delta)^{\sigma/2}\); equivalent chart-based norms give the same boundedness criterion. The torus Fourier coefficient is \((2\pi)^{-2}\int_{\mathbb T^2}F(\lambda,\theta)e^{-i(m\lambda+n\theta)}\,d\lambda\,d\theta\). The assertion is for all real \(s,t\ge0\) and all complex-valued functions, with a bounded extension interpreted by density of smooth functions. No assertion is made about negative target Sobolev exponents, the optimal operator norm, or the reverse map.

## Proof
**1. Local geometry and the borderline weight.** Near the north pole use the smooth plane chart \(x=(x_1,x_2)\mapsto(x_1,x_2,\sqrt{1-|x|^2})\), with \(|x|<r_0<1/2\), and a cutoff supported there. On its two DFS preimage patches, \(x=(\sin\theta\cos\lambda,\sin\theta\sin\lambda)\) up to harmless changes of angular orientation. Hence
\[
d\lambda\,d\theta=\frac{dx_1\,dx_2}{|x|\sqrt{1-|x|^2}},
\]
up to finite multiplicity. Identical estimates hold near the south pole. All partial derivatives in \(\lambda,\theta\) of the chart-coordinate map are bounded uniformly, including at the poles in the original coordinates. The multivariable chain rule therefore gives, for every integer \(k\ge0\) and multiindex \(|\beta|\le k\),
\[
\int_{\Phi^{-1}(U)} |\partial^\beta(Tf)|^2\,d\lambda\,d\theta
\le C_k\sum_{|\alpha|\le k}\int_{|x|<r_0}
\frac{|\partial^\alpha g(x)|^2}{|x|}\,dx,
\]
where \(g\) is the cut-off chart expression of \(f\). The chart cutoffs may be chosen so that each \(g\) extends by zero as a smooth compactly supported function on \(\mathbb R^2\).

**2. The critical fractional Hardy estimate.** In two dimensions, the \(p=2\), fractional-order-\(1/2\) case of the fractional Hardy inequality states that, for every \(u\in C_c^\infty(\mathbb R^2)\),
\[
\int_{\mathbb R^2}\frac{|u(x)|^2}{|x|}\,dx
\le C_{\rm H}\iint_{\mathbb R^2\times\mathbb R^2}
\frac{|u(x)-u(y)|^2}{|x-y|^3}\,dx\,dy
\le C'_{\rm H}\|u\|_{H^{1/2}(\mathbb R^2)}^2.
\]
For clarity, the hypotheses \(N=2\), \(p=2\), \(\sigma=1/2\) satisfy \(0<\sigma<1\) and \(p<N/\sigma\) in Frank--Seiringer's Theorem 1.1 [3]; the weight exponent \(p\sigma\) equals one and the difference-kernel exponent \(N+p\sigma\) equals three. Applying this inequality to each \(u=\partial^\alpha g\) with \(|\alpha|\le k\), and using localization of fractional Sobolev norms under smooth charts and cutoffs, gives the endpoint integer estimate
\[
\|Tf\|_{H^k(\mathbb T^2)}\le C_k\|f\|_{H^{k+1/2}(\mathbb S^2)}.
\]
On the complement of the pole patches, \(\Phi\) is locally a smooth covering with bounded inverse Jacobian, so the weaker \(H^k\)-to-\(H^k\) estimate suffices. Summing the finitely many patches proves the displayed endpoint estimate globally.

**3. Every real target order.** Standard Hilbert-space interpolation of the Sobolev scales on compact smooth manifolds gives
\[
[H^{k+1/2}(\mathbb S^2),H^{k+3/2}(\mathbb S^2)]_\eta
=H^{k+\eta+1/2}(\mathbb S^2),
\]
and likewise \([H^k(\mathbb T^2),H^{k+1}(\mathbb T^2)]_\eta=H^{k+\eta}(\mathbb T^2)\) for \(0\le\eta\le1\). Interpolating the integer endpoint estimates proves boundedness for every real \(t\ge0\). If \(s>t+1/2\), apply the usual Sobolev embedding \(H^s\hookrightarrow H^{t+1/2}\).

**4. Sharpness, including the endpoint distinction.** Fix a nonzero real \(h\in C_c^\infty((1,2))\). Let \(\rho(p)\) be the geodesic distance on the sphere from the north pole and define, for all sufficiently small \(\varepsilon>0\),
\[
f_\varepsilon(p)=\varepsilon^{s-1}h(\rho(p)/\varepsilon).
\]
This is globally smooth, supported in a polar annulus of radii \(\varepsilon\) and \(2\varepsilon\). Euclidean scaling in the two-dimensional normal chart, together with smooth-chart equivalence of Sobolev norms, shows
\[
\sup_{0<\varepsilon<\varepsilon_0}\|f_\varepsilon\|_{H^s(\mathbb S^2)}<\infty
\qquad(s\ge0).
\]
Indeed a smooth compactly supported Euclidean profile \(g(x/\varepsilon)\) has \(H^s(\mathbb R^2)\)-norm at most \(C_s\varepsilon^{1-s}\) for \(0<\varepsilon\le1\); the prefactor cancels that power.

Because \(\rho(\Phi(\lambda,\theta))\) equals the geodesic circle distance from \(\theta\) to \(2\pi\mathbb Z\), the pulled-back function is independent of \(\lambda\) and equals \(\varepsilon^{s-1}H(\theta/\varepsilon)\) near \(\theta=0\), periodically extended, where \(H(u)=h(|u|)\) is a nonzero compactly supported smooth even function. Its one-dimensional Fourier coefficients are exactly
\[
\widehat{Tf_\varepsilon}(0,n)
=\frac{\varepsilon^s}{2\pi}\widehat H(\varepsilon n),
\qquad \widehat H(\xi)=\int_{\mathbb R}H(u)e^{-i\xi u}\,du,
\]
with every coefficient for nonzero first frequency vanishing. Choose any interval \([a,b]\subset(0,\infty)\) on which \(|\widehat H|\) has a strictly positive lower bound; such an interval exists because the Fourier transform of a nonzero smooth compactly supported function is nonzero away from isolated points. There are at least \(c/\varepsilon\) integers with \(a\le\varepsilon n\le b\), each weighted by \((1+n^2)^t\ge c_t\varepsilon^{-2t}\). Consequently
\[
\|Tf_\varepsilon\|_{H^t(\mathbb T^2)}
\ge c_{s,t,h}\varepsilon^{s-t-1/2}.
\]
This diverges whenever \(s<t+1/2\), disproving boundedness even on smooth data. Combining with Steps 2--3 proves the if-and-only-if assertion. The Fourier coefficient formulation follows from Parseval, and the absolute-summability consequence follows by Cauchy--Schwarz with \(\sum_{(m,n)\in\mathbb Z^2}(1+m^2+n^2)^{-t}<\infty\) for \(t>1\). \(\square\)

## Verification
The proof is analytic. In particular, no finite sampling is used to claim an infinite-dimensional bound. A reproducible standard-library Python check, `check_scaling.py`, independently evaluates the exact polar change-of-measure formulas for smooth radial test functions and compares the expected \(\varepsilon^{-1/2}\) growth for pulled-back \(L^2\) and \(H^1\) seminorms. The saved output is `SCALING_CHECK.txt`. These computations illustrate rather than replace the fractional Hardy and interpolation arguments.

## Relationship to prior work
Mildenberger--Quellmalz [1, Sections 2 and 6] define exactly this DFS parametrization and construct a function in \(H^1(\mathbb S^2)\) whose pullback is not in \(H^1(\mathbb T^2)\). Their main Sobolev statement is this failure of same-order preservation; it neither states nor implies the endpoint half-derivative *sufficiency* established above. Their 2023 generalization [2] gives Hölder/continuous Fourier approximation on manifolds and does not state this spherical Sobolev threshold. The present proof uses the established fractional Hardy inequality [3], not a new Hardy constant. Its contribution is the exact necessary-and-sufficient Sobolev mapping threshold, including the critical endpoint and all real target orders, for the specific DFS transform. A broader composition-operator theorem could conceivably imply the threshold; no independent general uniqueness or historical-priority claim is made.

## Limitations
The numerical constant in the operator bound is not optimized. The result does not classify negative-order target spaces, non-\(L^2\) Sobolev exponents, or other degenerate manifold parametrizations. The established fractional Hardy theorem supplies the critical endpoint ingredient. These statements are mathematical proofs and internal analytical checks, not an independent audit or a claim of publication priority.

## References
[1] S. Mildenberger and M. Quellmalz, *Approximation Properties of the Double Fourier Sphere Method*, arXiv:2108.05662 (first submitted 2021-08-12); J. Fourier Anal. Appl. 28, article 31 (2022), https://arxiv.org/abs/2108.05662 ; https://doi.org/10.1007/s00041-022-09928-4 .

[2] S. Mildenberger and M. Quellmalz, *A double Fourier sphere method for d-dimensional manifolds*, arXiv:2301.06540 (2023); Sampling Theory Signal Processing and Data Analysis 21, article 23 (2023), https://arxiv.org/abs/2301.06540 ; https://doi.org/10.1007/s43670-023-00064-8 .

[3] R. L. Frank and R. Seiringer, *Non-linear ground state representations and sharp Hardy inequalities*, arXiv:0803.0503 (2008), Theorem 1.1 with parameters \(N=2,p=2,s=1/2\); J. Funct. Anal. 255 (2008), 3407–3430, https://arxiv.org/abs/0803.0503 .
