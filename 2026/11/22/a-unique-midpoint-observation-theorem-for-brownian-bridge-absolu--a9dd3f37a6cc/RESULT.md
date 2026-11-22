# A unique midpoint observation theorem for Brownian-bridge absolute-area quadrature

## Finding
Let \(B=(B_s)_{0\le s\le1}\) be a standard Brownian bridge with \(\mathbb E[B_s B_t]=\min(s,t)-st\), and let its absolute area be \(J=\int_0^1|B_s|\,ds\). Fix any finite absolute observation-noise variance \(\eta\ge0\). At one deterministic time \(t\in[0,1]\), observe \(Y_t=B_t+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent of the bridge, and estimate \(J\) by its posterior mean. Then the unique global minimizer of the mean-square Bayes risk \(R_\eta(t)=\mathbb E[(J-\mathbb E[J\mid Y_t])^2]\) is \(t=1/2\) for **every** finite \(\eta\ge0\).

The unconditional moments and minimum risk are
\[
\mathbb EJ=\frac{\sqrt{2\pi}}8,\qquad \mathbb EJ^2=\frac7{60},\qquad \operatorname{Var}J=\frac7{60}-\frac\pi{32},
\]
\[
\boxed{R_\eta^*=\frac7{60}-\frac\pi{32}-\frac2\pi\sum_{m=1}^\infty\frac{[(2m-3)!!]^2}{(2m)!}\frac{G_m^2}{(1+4\eta)^{2m}},\quad G_m=2\int_0^{1/2}s^{m+1/2}(1-s)^{1/2-m}\,ds.}
\]
Here \((-1)!!=1\). Each term is nonnegative; the series converges, including at \(\eta=0\). In particular, no affine function of \(Y_t\) improves upon the constant estimator \(\mathbb EJ\), because \(\operatorname{Cov}(J,Y_t)=0\) at every observation time. By contrast, the nonlinear posterior mean at \(1/2\) strictly reduces the risk for every finite \(\eta\).

At zero noise, the variance explained at the midpoint is \(0.01048443978\ldots\), about \(56.6975\%\) of the prior variance, and \(R_0^*=0.00800745646\ldots\). In the high-noise limit,
\[
\boxed{\operatorname{Var}J-R_\eta^*\sim\frac{(3\pi/8-1)^2}{16\pi\eta^2}\quad(\eta\to\infty).}
\]
The quadratic decay, instead of a linear inverse-noise decay, reflects the evenness of the absolute-area functional.

## Assumptions and scope
The bridge is real, centered and pinned at zero at both endpoints on the unit interval. The only permitted information is one full real-valued observation at a preselected deterministic time with independent *Gaussian* additive measurement noise of the same absolute variance \(\eta\) for all candidate times. The Bayes estimator is the unrestricted conditional mean, not a linear estimator. The noise variance is finite (there is no informative observation in the formal infinite-variance limit). The risk integrates over both bridge and observation noise. The expression for \(G_m\) is finite for every integer \(m\ge1\) because the integration interval ends at \(1/2\). Endpoint observations convey no information and give prior risk. These assertions do not address multiple, adaptive, non-Gaussian-noise, or spatially heteroscedastic measurements.

## Proof
**1. Stationary-coordinate representation.** For \(s\in(0,1)\), set \(u=\log(s/(1-s))\), \(s(u)=(1+e^{-u})^{-1}\), and \(Z_u=B_{s(u)}/\sqrt{s(u)(1-s(u))}\). A direct calculation using the bridge covariance shows that \(Z\) is a stationary, variance-one Gaussian process with \(\mathbb E[Z_uZ_v]=e^{-|u-v|/2}\). Changing variables gives
\[
J=\int_{\mathbb R}w(u)|Z_u|\,du,\qquad w(u)=[s(u)(1-s(u))]^{3/2}=\frac1{8\cosh^3(u/2)}.
\]
The weight \(w\) is strictly positive, even, integrable and strictly decreasing as \(|u|\) increases. These identities hold in \(L^2\), by Gaussian square integrability and \(w\in L^1\).

**2. Orthogonal projection and strict midpoint optimality.** Let \(v\) be the logit coordinate of a candidate observation \(t=s(v)\). Standardize the noisy observation to \(W_v=Y_{s(v)}/\sqrt{s(v)(1-s(v))+\eta}\). It is standard Gaussian, and
\[
\operatorname{Corr}(Z_u,W_v)=r_ve^{-|u-v|/2},\qquad r_v=\left[\frac{s(v)(1-s(v))}{s(v)(1-s(v))+\eta}\right]^{1/2}.
\]
For \(\eta=0\), interpret \(r_v=1\) at interior times. Write \(\psi_k(z)=\mathrm{He}_k(z)/\sqrt{k!}\) for probabilists' orthonormal Hermite polynomials. The exact Gaussian regression identity is
\[
\mathbb E[\psi_k(Z_u)\mid W_v]=(r_ve^{-|u-v|/2})^k\psi_k(W_v).
\]
The nonconstant Hermite coefficients of \(|z|\) vanish at odd orders, while at even orders \(2m\) they are
\[
b_{2m}=\mathbb E[|Z|\psi_{2m}(Z)]=\sqrt{\frac2\pi}\frac{(-1)^{m-1}(2m-3)!!}{\sqrt{(2m)!}}\ne0,\qquad m\ge1.
\]
These follow from the Gaussian Hermite integration-by-parts identity (or the distributional derivatives of \(|z|\)). By expanding \(|Z_u|\) in Gaussian \(L^2\), integrating against \(w\), conditioning, and applying Parseval, we obtain the **exact** explained-variance formula
\[
\Delta_\eta(v)=\operatorname{Var}(\mathbb E[J\mid W_v])=\sum_{m=1}^\infty b_{2m}^2r_v^{4m}H_m(v)^2,
\qquad H_m(v)=\int_{\mathbb R}w(u)e^{-m|u-v|}\,du.
\]
The interchanges are justified by the contraction of conditional expectation in \(L^2\), \(w\in L^1\), and Parseval; all coefficients contribute nonnegatively. For any \(v>0\), differentiation of the convolution of the smooth \(w\) with the Laplace kernel gives
\[
H_m'(v)=m\int_0^\infty e^{-my}\bigl[w(v+y)-w(v-y)\bigr]dy<0.
\]
Indeed \(|v+y|>|v-y|\), so each integrand is negative. Also \(H_m\) is even. The factor \(r_v\) is even and nonincreasing in \(|v|\) because \(s(v)(1-s(v))=1/[4\cosh^2(v/2)]\) is strictly decreasing as \(|v|\) increases; when \(\eta>0\), \(r_v\) is strictly decreasing. For \(\eta=0\), strict decrease of every \(H_m\) alone suffices. Since \(b_2\ne0\), every finite-variance observation has a strictly larger explained variance at \(v=0\) than at any \(v\ne0\); endpoint times give zero gain. Thus \(t=s(0)=1/2\) is the unique global minimizer of Bayes risk, with no reliance on a numerical grid.

**3. Exact series and high-noise asymptotic.** At \(v=0\), \(r_0^2=1/(1+4\eta)\) and symmetry of \(w\) gives
\[
H_m(0)=2\int_{-\infty}^0 w(u)e^{mu}du=2\int_0^{1/2}s^{m+1/2}(1-s)^{1/2-m}ds=G_m.
\]
Substituting \(b_{2m}^2\) into the explained-variance formula gives the series. Its convergence at \(\eta=0\) follows from Parseval and \(J\in L^2\). At large \(\eta\), the first Hermite mode dominates; since \(G_1=3\pi/8-1\) and \(b_2^2=1/\pi\),
\[
\Delta_\eta(0)=\frac{G_1^2}{\pi(1+4\eta)^2}+O((1+4\eta)^{-4})\sim\frac{G_1^2}{16\pi\eta^2}.
\]
The remainder estimate follows by bounding all higher terms by the finite zero-noise Parseval series times \((1+4\eta)^{-4}\).

**4. Unconditional moments and the impossibility of affine information.** The first moment is
\(\mathbb EJ=\sqrt{2/\pi}\int_0^1\sqrt{s(1-s)}ds=\sqrt{2\pi}/8\). For \(0<s<t<1\), the bivariate Gaussian absolute-product identity yields
\[
\mathbb E[|B_s||B_t|]=\frac2\pi\left[\sqrt{s(1-t)(t-s)}+s(1-t)\arcsin\sqrt{\frac{s(1-t)}{t(1-s)}}\right].
\]
Integrating over the ordered triangle gives respective inner contributions \(2\pi/105\) and \(17\pi/1680\); the second follows by integration by parts, with endpoint term \(\pi/48\) and residual \(\tfrac14\mathrm B(1/2,5/2)\mathrm B(5/2,2)=3\pi/280\). Multiplying the ordered triangle by \(4/\pi\) proves \(\mathbb EJ^2=7/60\). Subtracting the square of the first moment yields \(\operatorname{Var}J=7/60-\pi/32\). Lastly, simultaneous global sign reversal \(B\mapsto-B\) leaves \(J\) unchanged but reverses \(B_t\), hence \(\mathbb E[JB_t]=0\), and independent centered noise has zero covariance. The best affine estimator of \(J\) from any \(Y_t\) is therefore the constant \(\mathbb EJ\), despite the strictly positive nonlinear explained variance established above.

## Verification
Run `python VERIFY.py` from the directory containing `requirements.txt` (install its three scientific Python dependencies as needed). This independent computational check verifies the exact beta-moment algebra, the first eight even Hermite coefficients, the midpoint gain via two different formulas (a convergent Hermite series and double Gaussian covariance quadrature), reflection and a finite sample of strict comparisons, and the high-noise leading term. It passed 31 assertions. The source code is supplied in full. Finite numerical checks do not prove global optimality or series convergence; the analytic proof above does.

## Relationship to prior work
Alsolami, Burridge and Gnacik (2020) study tracked two-dimensional Brownian bridges through gyration and shape statistics; their quadratic shape observables and sampling setup motivate careful observation design but neither imply this nonlinear one-point absolute-area Bayes theorem nor its risk formula. Swanepoel (2017) computes areas and arcsine laws for Gaussian signed path integrals; a signed linear area is distinct from the absolute-area functional. Grothaus and Voßhall (2016) derive an integration-by-parts calculus for the law of the bridge modulus; this is a different distributional identity and is credited as prior analytic treatment of the modulus. Relevant published numerical-integration results address signed Brownian integrals with random stratification, while a separate Brownian-bridge local-time result gives covariances between local time and the absolute area but not conditional variance from a noisy point observation. The elementary Brownian-bridge covariance, Gaussian Hermite regression and absolute-value moments are classical ingredients, not claimed as discoveries. The contribution here is the conjunction of distribution-free-in-precision unique *sampling location* for this nonlinear target, the exact full Bayes risk series, the affine-information obstruction and the sharp high-noise asymptotic.

## Limitations
The result applies only to centered pinned one-dimensional Gaussian Brownian bridges, an absolute-area target, one predetermined *real-valued* observation, and independent additive Gaussian errors of spatially constant absolute variance. Its uniqueness theorem does not imply uniqueness for other path functionals, non-Gaussian noise, or more observation times. The high-noise limit describes a fixed Gaussian model, not minimax errors across unknown integrands. The exact series requires numerical truncation for displayed decimal values. Accessible full texts and research records were checked for implications, but literature completeness and publication priority have not undergone independent verification.

## References
1. N. Alsolami, J. Burridge and M. Gnacik, *Size and shape of tracked Brownian bridges*, arXiv:2004.05394, first posted 11 April 2020, https://arxiv.org/abs/2004.05394 ; open-access full text https://pure.port.ac.uk/ws/portalfiles/portal/21255440/Brownian_bridges.pdf.
2. J. Swanepoel, *A note on Brownian areas and arcsine laws*, 31 March 2017, https://www.journals.ac.za/sasj/article/download/5227/3260/.
3. M. Grothaus and R. Voßhall, *Integration by parts on the law of the modulus of Brownian bridge*, arXiv:1609.02438, first posted 8 September 2016, https://arxiv.org/abs/1609.02438.
4. *A factorized local-time–displacement covariance profile for the Brownian bridge*, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-factorized-local-time-displacement-covariance-profile-for-the--254aad83cd24.
5. *Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature*, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-design-loss-and-gaussian-fluctuations-for-stratified-brown--f119d713d36c.
