# An exact kurtosis identifiability threshold for renewal-aged porous-medium packets

## Finding

Let \(\sigma>0\), \(r>0\), and \(\ell_\sigma>0\). Let \(A\) have the exponential distribution of rate \(r\), independent of \(Y_\sigma\), whose density on \([-1,1]\) is
\[
f_\sigma(y)=\frac{(1-y^2)^{1/\sigma}}{B(1/2,1+1/\sigma)}\mathbf1_{\{|y|<1\}}.
\]
Define the stationary renewal-aged porous-medium packet variable
\[
X_\sigma=\ell_\sigma A^{1/(\sigma+2)}Y_\sigma,
\]
where \(\ell_\sigma\) is the (positive) similarity-length constant of a Barenblatt–Pattle packet; its precise value cancels below. The law of \(X_\sigma\) is the exponential-age mixture of the one-dimensional point-source porous-medium similarity densities.

The standardized fourth moment, \(K(\sigma)=\mathbb E[X_\sigma^4]/(\mathbb E[X_\sigma^2])^2\), is
\[
K(\sigma)=3\frac{3\sigma+2}{5\sigma+2}\frac{\Gamma(1+4/(\sigma+2))}{\Gamma(1+2/(\sigma+2))^2}.
\]
It decreases **strictly** and continuously from the limiting value \(K(0)=6\) to the unattained limit \(9/5\) as \(\sigma\to\infty\). Thus a single stationary kurtosis in \((9/5,6)\) identifies \(\sigma>0\) uniquely, independent of \(r\) and \(\ell_\sigma\); the ordinary-diffusion endpoint \(\sigma=0\) has \(K=6\). Precisely one finite positive nonlinearity, \(\sigma_*=1.148530617210168865\ldots\), has Gaussian fourth moment \(K(\sigma_*)=3\).

This fourth-order Gaussian match does **not** make the packet law Gaussian. At that parameter its standardized sixth cumulant is strictly negative:
\[
\frac{\kappa_6(X_{\sigma_*})}{\mathbb E[X_{\sigma_*}^2]^3}=
15\frac{(3\sigma_*+2)^2}{(5\sigma_*+2)(7\sigma_*+2)}\frac{\Gamma(1+6/(\sigma_*+2))}{\Gamma(1+2/(\sigma_*+2))^3}-15<0.
\]
It equals approximately \(-0.48606085132651666\). These statements hold for **every** positive reset rate and positive packet length scale.

## Assumptions and scope

The object is the normalized *renewal mixture of independently aged self-similar packets*, not an assertion that a nonlinear porous-medium PDE with a linear source term has this mixture as its solution. The free one-dimensional porous-medium equation is \(\partial_t p=c_\sigma\partial_{xx}(p^{\sigma+1})\), \(c_\sigma>0\), with point-source Barenblatt profiles. Its positive-length similarity variable has time scaling \(t^{1/(\sigma+2)}\) and compact shape \((1-y^2)_+^{1/\sigma}\). The stationary exponential-age mixture is defined exactly by the displayed independent product; no trajectory-level Markov representation of the nonlinear PDE is presumed. The ratio results are unchanged by the particular positive value of \(c_\sigma\) or by spatial scaling. The endpoint \(\sigma=0\) means the continuous heat-kernel/Laplace-resetting limit, not the singular \(Y_\sigma\) representation at \(\sigma=0\).

## Proof

For each integer \(j\ge1\), independence and beta integration give the exact even moment
\[
\mathbb E X_\sigma^{2j}=
\ell_\sigma^{2j}r^{-2j/(\sigma+2)}\Gamma\left(1+\frac{2j}{\sigma+2}\right)
\frac{B(j+1/2,1+1/\sigma)}{B(1/2,1+1/\sigma)}.
\]
Indeed, the seed moment follows by substituting \(z=y^2\) on \([-1,1]\); the exponential age integral is \(r\int_0^\infty e^{-rt}t^q\,dt=r^{-q}\Gamma(1+q)\). Every displayed moment exists for all finite \(\sigma>0\). At \(j=1,2\), beta recurrences yield the stated formula for \(K\).

Write \(u(\sigma)=2/(\sigma+2)\) and \(G(u)=\Gamma(1+2u)/\Gamma(1+u)^2\). The logarithmic derivative \(G'(u)/G(u)=2[\psi(1+2u)-\psi(1+u)]\) is strictly positive for \(u>0\), because the digamma \(\psi\) is strictly increasing on positive arguments. As \(\sigma\) increases, \(u\) decreases strictly, while the separate factor \((3\sigma+2)/(5\sigma+2)\) also decreases strictly (derivative \(-4/(5\sigma+2)^2\)). Their product is therefore strictly decreasing. Gamma continuity gives \(K(0)=3\Gamma(3)/\Gamma(2)^2=6\) and \(\lim_{\sigma\to\infty}K(\sigma)=3\cdot3/5=9/5\). The intermediate-value theorem and strict monotonicity establish exactly one \(K=3\) point and the stated inversion range.

For the sixth moment define
\[
S(\sigma)=15\frac{(3\sigma+2)^2}{(5\sigma+2)(7\sigma+2)}
\frac{\Gamma(1+6/(\sigma+2))}{\Gamma(1+2/(\sigma+2))^3}.
\]
The rational factor has strictly negative derivative
\[
-\frac{4(3\sigma+2)(17\sigma+6)}{(5\sigma+2)^2(7\sigma+2)^2}.
\]
The gamma factor \(\Gamma(1+3u)/\Gamma(1+u)^3\) is strictly increasing in \(u>0\), since its logarithmic derivative equals \(3[\psi(1+3u)-\psi(1+u)]>0\). Hence \(S\) strictly decreases with \(\sigma\). The reproducible high-precision interval checks provide \(K(1.14)>3\), \(K(1.15)<3\), and \(S(1.14)<15\), so \(\sigma_*\in(1.14,1.15)\) and \(S(\sigma_*)<15\). Symmetry gives \(\kappa_6=\mu_6-15\mu_4\mu_2+30\mu_2^3\); at \(K=3\), this is \(\mu_2^3(S-15)<0\). Thus the fourth-order Gaussian match is not a Gaussian law.

## Verification

Run `python checker.py` using Python 3 and mpmath 1.3 or later. It evaluates rational-endpoint gamma-function inequalities using interval arithmetic, independently integrates beta-profile and exponential-age moments at eight nonlinearity values, and finds the unique root after its existence and uniqueness have been proved analytically. The checked interval differences have wide strict sign margins: \(K(1.14)-3\approx0.0068825062368\), \(K(1.15)-3\approx-0.0011784904342\), and \(S(1.14)-15\approx-0.4009907223186\). These numerical checks validate arithmetic signs; uniqueness and the all-parameter statements depend on the analytic derivative proof, not on sampling.

## Relationship to prior work

Chełminiak (arXiv:2107.14680; 2021 public version, 2022 revision and journal publication) derives the Barenblatt density, the resetting renewal mixture, its stationary integral formula, and its second moment. This work **does not claim** those constructions as new. The additional conclusion proved here is the complete one-to-one kurtosis law in the nonlinear exponent, including the unique fourth-order Gaussian blind spot and its strict sixth-order resolution. The earlier general integral formula determines all moments in principle; the monotone global identifiability classification is not an immediate restatement of that integral. Lenzi et al. (2023) study related nonlinear resetting and generalized stationary densities; their accessible abstract and indexed descriptive sections do not establish the precise global threshold, but a complete full-text claim-by-claim comparison remains a residual priority risk.

## Limitations

This is a population-level renewal-age mixture statement, not a trajectory-wise law for an arbitrary nonlinear McKean or porous-medium evolution with imposed resetting. The scale \(\ell_\sigma\), reset rate and transport coefficient cannot be determined from kurtosis alone. The identification is mathematical for exact moments; no claims about noisy finite-sample identifiability, convergence rates of estimators, or a fourth-moment characterization of Gaussian laws are made. The sixth-cumulant test uses interval numerical bounds at rational points plus analytic monotonicity; it is not an independently formalized proof assistant certificate. Novelty is relative to the actual cited literature and indexed searches, not an assertion of exhaustive world-literature priority.

## References

1. P. Chełminiak, *Non-linear diffusion with stochastic resetting*, arXiv:2107.14680v1 (30 July 2021), v2 (6 March 2022), Journal of Physics A 55 (2022) 384004, https://arxiv.org/abs/2107.14680, https://doi.org/10.1088/1751-8121/ac870a.
2. E. K. Lenzi et al., *Results for Nonlinear Diffusion Equations with Stochastic Resetting*, Entropy 25 (2023), 1647, https://doi.org/10.3390/e25121647.
3. R. K. Singh, K. Górska, T. Sandev, *General approach to stochastic resetting*, Phys. Rev. E 105 (2022), 064133, https://arxiv.org/abs/2203.04046.
