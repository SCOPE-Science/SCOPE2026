# Exact sharp circular-variation decay under iterated von Mises smoothing

## Finding
For \(\beta>0\), define the von Mises probability density on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) by
\[
k_\beta(\theta)=\frac{e^{\beta\cos\theta}}{2\pi I_0(\beta)},\qquad
I_j(\beta)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{\beta\cos\theta}\cos(j\theta)\,d\theta.
\]
Write \(T_\beta f=k_\beta*f\), with convolution against ordinary Lebesgue measure. For any positive integer \(r\), its \(r\)-fold iterate has exact sharp real bounded-variation seminorm
\[
\boxed{K_r(\beta)=\sup_{\operatorname{TV}(f)>0}\frac{\operatorname{TV}(T_\beta^r f)}{\operatorname{TV}(f)}=\frac4\pi\sum_{j=0}^\infty\frac{(-1)^j}{2j+1}\left(\frac{I_{2j+1}(\beta)}{I_0(\beta)}\right)^r.}
\]
All nonconstant equality cases are, up to an additive constant, a nonzero multiple of the indicator of a semicircle, with arbitrary circular translation. The same coefficient is the sharp two-input bounded-variation Lipschitz ratio, since the operator is linear. In particular,
\[
\boxed{K_1(\beta)=\frac{L_0(\beta)}{I_0(\beta)},}
\]
where \(L_0\) denotes the order-zero modified Struve function, defined here by \(L_0(\beta)=\frac2\pi\int_0^{\pi/2}\sinh(\beta\cos\theta)\,d\theta\). For every \(r,s\ge1\),
\[
0<K_{r+s}(\beta)<K_r(\beta)K_s(\beta)<1,
\qquad K_r(\beta)\sim\frac4\pi\left(\frac{I_1(\beta)}{I_0(\beta)}\right)^r\quad(r\to\infty).
\]
For the single application, \(K_1(\beta)\sim2\beta/\pi\) as \(\beta\downarrow0\), while \(1-K_1(\beta)\sim\sqrt{8/(\pi\beta)}e^{-\beta}\) as \(\beta\to\infty\).

## Assumptions and scope
All functions are real and periodic, with bounded distributional variation \(\operatorname{TV}(f)=|Df|(\mathbb T)\); representatives are identified almost everywhere. The density is positive, smooth, and normalized so that \(\int_{\mathbb T}k_\beta=1\). Every \(\beta\) is finite and strictly positive. The iterate count \(r\) is a positive integer. A constant has variation zero. The extremizer description concerns positive-variation functions; semicircle endpoints have no importance as point values. The statement does not assume that the convolution powers are themselves von Mises densities (generally they are not).

## Proof
**1. Strict circular unimodality survives convolution.** Suppose \(a,b\) are positive smooth even probability densities, strictly decreasing in geodesic angle \(\theta\in(0,\pi)\). Their circular convolution \(h=a*b\) is even. For \(0<\theta<\pi\), differentiation and pairing \(u\) with \(-u\) gives
\[
h'(\theta)=\int_0^\pi a'(u)[b(\theta-u)-b(\theta+u)]\,du<0.
\]
Indeed, the circular geodesic distance from \(\theta-u\) to zero is strictly smaller than the distance from \(\theta+u\) for \(0<\theta,u<\pi\), so the bracket is strictly positive and \(a'(u)<0\). The von Mises density has \(k_\beta'(u)=-\beta\sin(u)k_\beta(u)<0\) there. Induction therefore proves every \(h_r=k_\beta^{*r}\) is smooth, positive, even, and strictly decreasing in geodesic angle.

**2. Exact translation distance.** For any such even strictly decreasing probability density \(h\), let \(h_\delta(\theta)=h(\theta-\delta)\) with \(0\le\delta\le\pi\), and define \(d_h(\delta)=\frac12\int_{\mathbb T}|h-h_\delta|\). The sign of \(h(\theta)-h_\delta(\theta)\) is positive exactly on the semicircle \((\delta/2-\pi,\delta/2)\). Consequently
\[
d_h(\delta)=\int_{\delta/2-\pi}^{\delta/2}h(\theta)\,d\theta-\int_{\delta/2-\pi}^{\delta/2}h(\theta-\delta)\,d\theta,
\quad d_h'(\delta)=h(\delta/2)-h(\pi-\delta/2)>0\quad(0<\delta<\pi).
\]
Thus the unique maximizing separation is antipodal, and
\[
\max_{\delta}d_h(\delta)=d_h(\pi)=2\int_{-\pi/2}^{\pi/2}h(\theta)\,d\theta-1.
\]

**3. The sharp BV quotient and all equality cases.** For nonconstant \(f\in BV(\mathbb T)\), the signed measure \(\mu=Df\) has total mass zero. Its Jordan parts \(\mu_+,\mu_-\) each have mass \(m=\operatorname{TV}(f)/2\). Choose any probability coupling \(\gamma\) of \(\mu_+/m\) and \(\mu_-/m\). In total-variation norm of signed measures,
\[
\|h*\mu\|_{\mathrm{var}}\le m\int\|h(\cdot-x)-h(\cdot-y)\|_{L^1}\,d\gamma(x,y)
\le2m\,d_h(\pi).
\]
Since \(D(h*f)=h*Df\), the second inequality establishes \(\operatorname{TV}(h*f)\le d_h(\pi)\operatorname{TV}(f)\). A semicircle indicator has derivative \(\delta_a-\delta_{a+\pi}\) (up to sign), and both inequalities are equalities, proving sharpness. Strict increase of \(d_h(\delta)\) shows equality is possible only if \(\gamma\)-almost all coupled pairs are antipodal. This forces both Jordan parts to be opposite singleton atoms; hence \(f\) is exactly a translated, scaled semicircle indicator plus a constant. Applying this to \(h=h_r\) proves the claimed exact norm and rigidity for every iterate.

**4. Evaluate the coefficient.** The von Mises density has absolutely convergent Fourier series
\[
k_\beta(\theta)=\frac1{2\pi}\left[1+2\sum_{j=1}^{\infty}\frac{I_j(\beta)}{I_0(\beta)}\cos(j\theta)\right].
\]
Under circular convolution, Fourier coefficients multiply, so \(h_r\) has the same expansion with the displayed ratio raised to power \(r\). Since \(\int_{-\pi/2}^{\pi/2}\cos(j\theta)\,d\theta=2\sin(j\pi/2)/j\), the semicircle mass formula in Step 2 gives the boxed alternating odd-harmonic series. For \(r=1\), separating \(e^{\beta\cos\theta}\) and \(e^{-\beta\cos\theta}\) over opposite semicircles gives exactly \(L_0(\beta)/I_0(\beta)\).

**5. Strict multiplicative improvement.** The operator norm inequality gives \(K_{r+s}\le K_rK_s\). If equality held, use the semicircle indicator attaining \(K_{r+s}\). After applying \(T_\beta^r\), its derivative is a nonzero smooth signed density (the difference of two strictly shifted circular kernels). Step 3 shows that no such non-atomic derivative can attain the \(K_s\) inequality, contradiction. Thus \(K_{r+s}<K_rK_s\). Since every \(h_r\) is strictly positive and nonconstant, \(0<K_r<1\). Finally, by the Bessel recurrence \(I_{n-1}(\beta)-I_{n+1}(\beta)=2nI_n(\beta)/\beta\), the odd coefficients satisfy \(I_1>I_3>I_5>\cdots>0\); their rapidly convergent series and the spectral expansion imply \(K_r=(4/\pi)(I_1/I_0)^r+O((I_3/I_0)^r)\). The small-\(\beta\) limit follows by series expansion. For \(\beta\to\infty\), the two antipodal-tail integrals are concentrated in boundary layers of width \(\beta^{-1}\) around \(\pm\pi/2\); combining this with \(I_0(\beta)\sim e^\beta/\sqrt{2\pi\beta}\) yields the stated sharp exponential deficit.

## Verification
The standalone \(\texttt{check.py}\) uses only Python's standard library to compute the modified Bessel coefficients from positive term series and compare the spectral coefficient with independent semicircle quadrature for one application, verify numerical strict submultiplicativity for several positive concentrations and iterate counts, and test the first-mode large-iterate prediction. Its finite precision checks do not prove the universal claims, which follow from Steps 1–5.

## Relationship to prior work
García-Portugués, Crujeiras, and González-Manteiga (2012) introduce and analyze directional and directional-linear von Mises kernel estimators, including mean-integrated-squared-error and convolution calculations. García-Portugués (2013) treats exact risk and bandwidth selection with von Mises mixtures, including nontrivial convolution quantities. These are \(L^2\) risk results, not sharp \(BV\) operator norms over arbitrary input signals. A published analysis of circular heat smoothing gives a sharp variation coefficient for the heat kernel, but the von Mises iterates have different Fourier multipliers \((I_j(\beta)/I_0(\beta))^r\), not the heat multipliers \(e^{-tj^2}\); the heat result cannot be substituted to derive these coefficients. The zero-mass-measure coupling argument draws on the standard Dobrushin contraction principle. The contribution is the explicit all-iterate von Mises coefficient, complete extremizer rigidity, strict multiplicative improvement, and sharp asymptotic decay. No exhaustive priority claim is made regarding unindexed earlier calculations.

## Limitations
Only the real circular one-parameter von Mises density with strictly positive finite concentration and positive integer convolution powers is covered. Other directional kernels, higher spheres, non-circular domains, complex BV, and noninteger fractional convolution powers are not established. The sharp constants are not claimed to determine optimal statistical bandwidths or stochastic estimator risks. Publication priority relative to unindexed work is uncertain.

## References
1. E. García-Portugués, R. M. Crujeiras, and W. González-Manteiga, *Kernel density estimation for directional-linear data*, arXiv:1210.3214, first public submission 2012-10-11, https://arxiv.org/abs/1210.3214.
2. E. García-Portugués, *Exact risk improvement of bandwidth selectors for kernel density estimation with directional data*, arXiv:1306.0517, first public submission 2013-06-03, https://arxiv.org/abs/1306.0517.
3. The modified Bessel and Struve integral representations in Step 4 are standard special-function definitions; the bounded-variation sharp norm and iteration formulas are established above.
