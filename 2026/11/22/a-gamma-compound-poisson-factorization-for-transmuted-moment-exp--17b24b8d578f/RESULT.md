# A gamma–compound-Poisson factorization for transmuted moment-exponential count mixtures

## Finding

Let \(\beta>0\), \(-1\le\alpha\le1\), and let \(\Lambda\) have density
\[
f_{\alpha,\beta}(x)=\frac{x e^{-x/\beta}}{\beta^2}
\left[1-\alpha+2\alpha(1+x/\beta)e^{-x/\beta}\right],\qquad x>0.
\]
This is the complete signed-transmutation range in which the displayed function is a probability density. For **every** \(-1<\alpha\le1\), it admits the independent convolution representation
\[
\boxed{\Lambda\ \overset d=\ Y+J,\quad
Y\sim\operatorname{Gamma}(2,\text{rate }2/\beta),\quad
J\sim\operatorname{CP}(\lambda_\alpha,H_{\alpha,\beta}),\quad
\lambda_\alpha=\log\frac4{1+\alpha}.}
\]
The compound-Poisson jump measure \(\lambda_\alpha H_{\alpha,\beta}(dx)\) has an explicit nonnegative density \(\rho_{\alpha,\beta}(x)\), given below. In particular, the mixing law is infinitely divisible throughout its entire admissible signed-transmutation range. At the exact boundary \(\alpha=-1\), the same gamma factor remains valid, but its specified independent remainder has an **infinite-activity** Lévy measure; hence the residual compound-Poisson representation with that fixed gamma factor is possible exactly when \(\alpha>-1\).

For the corresponding mixed-Poisson count \(N\mid\Lambda\sim\operatorname{Poisson}(\Lambda)\), the same representation yields
\[
\boxed{N\ \overset d=\ N_0+N_1,\qquad
N_0\sim\operatorname{NB}(2,q),\quad q=\frac{\beta}{\beta+2},\qquad
N_1\text{ compound Poisson},}
\]
where \(N_0,N_1\) are independent, the negative-binomial parameterization is \(\mathbb E[z^{N_0}]=((1-q)/(1-qz))^2\), and the residual nonnegative integer jump intensities are
\[
\mu_n=\int_0^\infty e^{-x}\frac{x^n}{n!}\rho_{\alpha,\beta}(x)\,dx>0,\qquad n\ge1.
\]
At \(\alpha=-1\), \(N\) remains infinitely divisible and hence compound Poisson as a nonnegative integer law; it is only the *specified continuous gamma-factor residual* that has infinite activity.

## Assumptions and scope

The shape \(\alpha\) is dimensionless and \(\beta\) is a positive scale, as in the transmuted moment-exponential mixing density of Alrumayh and Khogeer (2023). Their count model explicitly uses \(0<\alpha<1\); the present classification also covers admissible negative transmutation and boundary values of the same formula. The density condition follows because \(g(t)=2(1+t)e^{-t}\) decreases from \(2\) to \(0\): the bracket is \(1-\alpha+\alpha g(t)\), nonnegative for all \(t\ge0\) precisely when \(-1\le\alpha\le1\). Integration to one follows directly from Gamma integrals.

For \(0<|\alpha|<1\), define
\[
P_\alpha(y)=(1+\alpha)y^3+6(1+\alpha)y^2+6(2+\alpha)y+8.
\]
It has one negative real zero \(-A\) and conjugate zeros \(-B\pm iC\), where \(A,B,C>0\) and \(C>0\). The dimensionless Lévy kernel and jump density are
\[
\begin{aligned}
k_\alpha(t)&=2e^{-t}+3e^{-2t}-e^{-At}-2e^{-Bt}\cos(Ct),\\
\rho_{\alpha,\beta}(x)&=\frac{k_\alpha(x/\beta)-2e^{-2x/\beta}}{x}\\
&=\frac{2e^{-x/\beta}+e^{-2x/\beta}-e^{-Ax/\beta}-2e^{-Bx/\beta}\cos(Cx/\beta)}{x}.
\end{aligned}
\]
At the degenerate values, use the continuous formulas \(\rho_{0,\beta}(x)=2(e^{-x/\beta}-e^{-2x/\beta})/x\), \(\rho_{1,\beta}(x)=(e^{-2x/\beta}-e^{-4x/\beta})/x\), and \(\rho_{-1,\beta}(x)=[2e^{-x/\beta}+e^{-2x/\beta}-e^{-4x/(3\beta)}]/x\). The latter describes an infinite-activity subordinator, not a compound-Poisson variable.

## Proof

**1. Rational Laplace transform.** Direct integration, with \(y=\beta s\), gives
\[
\mathcal L_\Lambda(s)=\frac{1-\alpha}{(1+y)^2}
+\frac{2\alpha}{(2+y)^2}+\frac{4\alpha}{(2+y)^3}
=\frac{P_\alpha(y)}{(1+y)^2(2+y)^3},\qquad s\ge0.
\]
The formula normalizes to \(\mathcal L_\Lambda(0)=1\). Its discriminant in \(y\) is \(432\alpha^2(\alpha^2-1)<0\) for \(0<|\alpha|<1\). Thus the cubic has one real root and a nonreal conjugate pair. Since
\[
P_\alpha(-4)=8(\alpha-1),\quad P_\alpha(-2)=4\alpha,\quad P_\alpha(-1)=1-\alpha,
\]
the unique real root satisfies \(2<A<4\) for \(0<\alpha<1\), and \(1<A<2\) for \(-1<\alpha<0\). The Vieta relation \(A+2B=6\) implies, respectively, \(1<B<2\) and \(2<B<5/2\). The remaining roots exist as conjugates with \(C>0\); no bound on \(C\) is required.

**2. Lévy–Khintchine factorization.** Factor \(P_\alpha(y)=(1+\alpha)(y+A)[(y+B)^2+C^2]\). For a complex \(r\) with positive real part, the Frullani identity
\[
\log(1+s/r)=\int_0^\infty(1-e^{-sx})e^{-rx}\frac{dx}{x}
\]
holds with consistent analytic branches; pairing the two conjugate roots produces the real cosine term. Taking logarithms of the normalized Laplace transform therefore yields the exact identity
\[
-\log\mathcal L_\Lambda(s)=\int_0^\infty(1-e^{-sx})\frac{k_\alpha(x/\beta)}{x}\,dx.
\]
The gamma factor of shape two and rate \(2/\beta\) has Lévy density \(2e^{-2x/\beta}/x\). Subtracting it produces \(\rho_{\alpha,\beta}\) above; positivity is not automatic from the rational transform and must be established.

**3. Global positive kernel.** Write \(E_\alpha(t)=x\rho_{\alpha,\beta}(x)\) with \(t=x/\beta\). If \(0<\alpha<1\), then \(A>2\), \(B>1\), and
\[
E_\alpha(t)=2\bigl(e^{-t}-e^{-Bt}\cos Ct\bigr)+\bigl(e^{-2t}-e^{-At}\bigr)>0\quad(t>0).
\]
If \(-1<\alpha<0\), then \(A>1\) and \(B>2\), giving the lower bound
\[
E_\alpha(t)\ge (2e^{-t}-e^{-At})+(e^{-2t}-2e^{-Bt})
\ge e^{-t}-e^{-2t}>0\quad(t>0).
\]
At \(\alpha=0\) and \(\alpha=1\), the explicit degenerate kernels are strictly positive as well. In each case \(E_\alpha(0)=0\), \(E_\alpha\) is differentiable at zero, and \(E_\alpha(t)\) decays exponentially at infinity. Consequently \(\rho_{\alpha,\beta}\) is positive and integrable on \((0,\infty)\). The logarithmic Laplace identity proves the stated independent gamma-plus-compound-Poisson convolution.

**4. Exact activity and its boundary.** The residual Laplace transform is \(\mathcal L_J(s)=\mathcal L_\Lambda(s)/[2/(2+\beta s)]^2\). As \(s\to\infty\),
\[
\mathcal L_J(s)\longrightarrow \frac{1+\alpha}{4}
=\exp\left(-\int_0^\infty\rho_{\alpha,\beta}(x)\,dx\right),
\]
so \(\int\rho=\log(4/(1+\alpha))\) for \(-1<\alpha\le1\). At \(\alpha=-1\), the polynomial reduces to \(P_{-1}(y)=6y+8\); direct factorization gives the displayed \(\rho_{-1,\beta}\), which is positive because \(2e^{-t}-e^{-4t/3}>0\), but \(x\rho_{-1,\beta}(x)\to2\) as \(x\downarrow0\). Thus \(\int_0^1\rho\,dx=\infty\). Infinite divisibility survives; finite residual activity does not. Outside \([-1,1]\), the proposed mixing density changes sign, so it is not a probability law of the stated family.

**5. Poissonization and explicit integer jump masses.** Conditional on \(Y\), the Poisson count has the negative-binomial law above. If \(J=\sum_{j=1}^{K}Z_j\) with \(K\sim\operatorname{Poisson}(\lambda_\alpha)\) and \(Z_j\) having the normalized density \(\rho/\lambda_\alpha\), conditional Poisson splitting yields independent count contributions with \(\operatorname{Poisson}(Z_j)\) marks. Discard their zero marks. The resulting nonzero integer mark intensities are exactly \(\mu_n\), strictly positive for each \(n\ge1\), and their sum is finite because \(\sum_{n\ge1}\mu_n=\int(1-e^{-x})\rho(x)\,dx\le\lambda_\alpha\). This proves the count convolution, without identifying the continuous activity rate with the generally smaller rate of nonzero integer marks.

For \(0<|\alpha|<1\), define \(q_j=\beta/(\beta+j)\), \(r_A=\beta/(\beta+A)\), \(R=\beta/\sqrt{(\beta+B)^2+C^2}\), and \(\phi=\arctan(C/(\beta+B))\). The complete count Lévy coefficients are the concrete convergent expressions
\[
\nu_n=\frac{2q_1^n+3q_2^n-r_A^n-2R^n\cos(n\phi)}{n},
\qquad \mu_n=\nu_n-\frac{2q_2^n}{n}>0\qquad(n\ge1).
\]
Here \(\log\mathbb E[z^N]=\sum_{n\ge1}\nu_n(z^n-1)\), and the negative-binomial factor contributes \(2q_2^n/n\). The integral argument above proves positivity for *all* indices, not just the checked initial coefficients.

## Verification

The accompanying standalone `verify.py` uses exact symbolic algebra to check the rational Laplace identity, discriminant, root-bracketing polynomial evaluations, degenerate parameter factorization, density normalization and mean \(\mathbb E\Lambda=\beta(2-3\alpha/4)\). At \((\alpha,\beta)=(1/9,1)\), it factors
\[
P_{1/9}(y)=\frac29(y+3)(5y^2+15y+12)
\]
and checks \(G(0)=64/243\), \(\nu_1=31/32\), \(\nu_2=1453/6144\), \(\nu_3=69263/884736\), and \(\mu_1=29/96\) exactly. It checks six initial positive residual integer intensities and numerical roots/kernel values for illustrative parameters. The proof of global nonnegativity and of *every* coefficient is the analytic argument in Sections 2–5 above, **not** the finite computations.

To reproduce, with Python and SymPy installed, run `python verify.py` from the directory containing this result and the checker. No unpublished datasets or external network calls are required.

## Relationship to prior work

Alrumayh and Khogeer (2023) defined the discrete Poisson–transmuted moment-exponential model, including its density, probability mass function, moments, simulation, estimation and regression applications. The full openly readable article was inspected through its Sections 2–8; it does not present the gamma-plus-compound-Poisson factor, the global positive Lévy kernel or the exact residual activity. This result starts from the **same density**, not an arbitrary reparameterized different count law.

Hassan, Abdul-Moniem and Gad (2020) studied a broader generalized transmuted moment-exponential *continuous* distribution, explicitly listing the present ordinary transmuted moment-exponential family as a submodel. The inspected definition, structural-property section and conclusion concern moments, quantiles, residual life and estimation; they provide no gamma-plus-positive-Lévy-kernel decomposition of this special case. Thus the underlying mixing density itself is not new.

Bhati, Kumawat and Gómez-Déniz (2015 preprint; subsequently published) investigated infinite divisibility for a **transmuted exponential** Poisson mixture. Its mixing density combines ordinary exponentials, whereas the present **transmuted moment-exponential** mixing density has the Gamma-shape-two/three terms and the cubic numerator proved here. That earlier restricted infinite-divisibility argument cannot by itself supply this explicit independent gamma-factor construction.

The general Lévy–Khintchine and Poisson-mixture principles are standard and not claimed as new. The substantive family-specific result is positivity of the explicitly extracted residual Lévy measure throughout the full valid transmutation interval, with its sharp finite/infinite activity boundary and count decomposition.

## Limitations

This is a mathematical self-review, **not an independent audit or a certified historical priority determination**. Historical coverage searches and accessible full-text comparisons cannot exclude every unpublished or unindexed equivalent result. For \(\alpha=-1\), the residual is an infinite-activity subordinator, not a finite-jump compound Poisson process; its count distribution nonetheless has a compound-Poisson representation. There is no assertion here about uniqueness of gamma factors at other rates, self-decomposability, inference optimality, empirical fit, or process-level independence beyond the explicitly constructed representation.

## References

1. Alrumayh, A., and Khogeer, H. A. (20 June 2023), *A New Two-Parameter Discrete Distribution for Overdispersed and Asymmetric Data: Its Properties, Estimation, Regression Model, and Applications*, Symmetry 15(6), 1289. https://doi.org/10.3390/sym15061289. Full text: https://www.mdpi.com/2073-8994/15/6/1289.
2. Bhati, D., Kumawat, P., and Gómez-Déniz, E. (2015), *A New Count Model Generated from Mixed Poisson Transmuted Exponential Family with an application to Health Care Data*, arXiv:1504.01097, first posted 5 April 2015. https://arxiv.org/abs/1504.01097.
3. Hassan, A. S., Abdul-Moniem, I. B., and Gad, K. A. (13 May 2020), *A Generalized Transmuted Moment Exponential Distribution: Properties and Application*, Academic Journal of Applied Mathematical Sciences 6(5), 41–52. https://doi.org/10.32861/ajams.65.41.52.
4. Steutel, F. W., and van Harn, K. (2004), *Infinite Divisibility of Probability Distributions on the Real Line*, CRC Press. Standard reference for Lévy–Khintchine and discrete compound-Poisson theory; not a direct source of the family-specific theorem.
