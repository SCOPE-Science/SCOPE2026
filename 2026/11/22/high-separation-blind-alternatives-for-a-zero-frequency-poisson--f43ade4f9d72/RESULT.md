# High-separation blind alternatives for a zero-frequency Poisson test

## Finding

Let \(P_{\lambda}\) denote a Poisson law of mean \(\lambda>0\), and consider the mean-and-zero-frequency goodness-of-fit statistic of Di Noia, Barabesi, Marcheselli, Pisani and Pratelli, specialized to the Poisson null. For independent observations \(X_1,\ldots,X_n\), put
\[
\widehat\mu=\frac1n\sum_{i=1}^n X_i,\quad
\widehat p_0=\frac1n\sum_{i=1}^n\mathbf1_{\{X_i=0\}},\quad
Z_n=\frac{\sqrt n\,(e^{-\widehat\mu}-\widehat p_0)}{\sqrt{e^{-\widehat\mu}-(\widehat\mu+1)e^{-2\widehat\mu}}}.
\]
Use the source's zero convention if the denominator vanishes.

**Theorem.** For every pair of integers \(u\ge1\), \(v\ge2\), set \(\lambda=uv\), \(r=e^{-\lambda}\), and define \(Q_{u,v}\) by the following four (distinct) support points and probabilities:

| Count | Probability under \(Q_{u,v}\) |
| --- | --- |
| \(0\) | \(r\) |
| \(\lambda-u\) | \(\frac{v}{u+v}[1-r(\lambda+v)]\) |
| \(\lambda\) | \(r(u+1)(v-1)\) |
| \(\lambda+v\) | \(\frac{u}{u+v}[1-r(\lambda-u)]\) |

Let \(H_{u,v}=(1-\lambda^{-2})Q_{u,v}+\lambda^{-2}P_{\lambda}\). This is a full-support, non-Poisson count law with
\[
H_{u,v}\{0\}=e^{-\lambda},\qquad
\mathbb E_H X=\lambda,\qquad
\operatorname{Var}_H X=\lambda.
\]
For **each fixed** admissible \((u,v)\), independent samples of increasing size from \(H_{u,v}\) obey
\[
Z_n\xrightarrow{d}N(0,1).
\]
Hence the original two-sided Gaussian-calibrated rejection rule \(|Z_n|>z_{1-\alpha/2}\) has limiting rejection probability exactly \(\alpha\), for every fixed \(0<\alpha<1\), despite the nonnull law having full support.

Meanwhile, if \(u,v\to\infty\) with \(v/u\to\rho\in(0,\infty)\),
\[
\sqrt{uv}\bigl[1-d_{\mathrm{TV}}(P_{uv},H_{u,v})\bigr]
\longrightarrow G(\rho):=\frac{e^{-\rho/2}+e^{-1/(2\rho)}}{\sqrt{2\pi}}.
\]
This makes the one-observation total-variation distance tend to one. **Within this two-offset moment-matching construction**, its limiting overlap coefficient has exactly two symmetric minimizers \(\rho_*\) and \(1/\rho_*\), where \(\rho_*>1\) is the unique solution above one of
\[
\rho-\rho^{-1}=4\log\rho.
\]
In particular,
\[
\rho_*=8.822620943170486\ldots,\qquad
\min_{\rho>0}G(\rho)=0.381804810252850\ldots.
\]
Integer sequences approximating \(v/u=\rho_*\) attain the displayed constant asymptotically.

## Assumptions and scope

All variables take values in \(\mathbb N_0\); all null and alternative observations are independent and identically distributed. The sample-size limit for the test is **at a fixed pair** \((u,v)\), followed separately by a different large-parameter analysis of total variation. No joint limit allowing \(u,v\) to grow with sample size is asserted. The minimization pertains to the exhibited two-offset family, not all distributions matching the three constraints. The numerical constants come from the analytic equations, not numerical optimization used as proof.

## Proof

**1. Legitimate probability law and moments.** Write \(L=uv\) and \(r=e^{-L}\). The probability at \(L-u\) is positive because
\(v(u+1)e^{-uv}\le4e^{-2}<1\) for \(u\ge1,v\ge2\); the probability at \(L+v\) is positive since \(u(v-1)e^{-uv}<1\). The center and zero probabilities are positive. Direct expansion gives total mass one, and
\[
\sum_x xQ_{u,v}\{x\}=L,\qquad
\sum_x (x-L)^2Q_{u,v}\{x\}=L.
\]
For the second identity the zero atom contributes \(L^2r\), and the remaining two off-center atoms contribute \(u^2Q_{u,v}\{L-u\}+v^2Q_{u,v}\{L+v\}=L-L^2r\). The mixture \(H\) has the same zero mass, first moment and variance because \(P_L\) does; its Poisson component makes its support all of \(\mathbb N_0\). It differs from the Poisson law (for example its noncentral atom masses at \(L-u\) and \(L+v\) remain bounded away from the corresponding small Poisson masses in the large-parameter sequence; for each admissible fixed pair, it is also non-Poisson because a nontrivial finite-support component cannot equal a Poisson law).

**2. Identical Gaussian calibration.** Under either \(P_L\) or \(H_{u,v}\), the vector \((X,\mathbf1_{\{X=0\}})\) has expectation \((L,r)\) and covariance matrix
\[
\Sigma=\begin{pmatrix}L&-Lr\\-Lr&r(1-r)\end{pmatrix},
\]
because \(X\mathbf1_{\{X=0\}}=0\). The bivariate i.i.d. central limit theorem and a first-order Taylor expansion give
\[
\sqrt n(e^{-\widehat\mu}-\widehat p_0)
=-r\sqrt n(\widehat\mu-L)-\sqrt n(\widehat p_0-r)+o_p(1),
\]
whose asymptotic variance is \(\sigma_L^2=r-(L+1)r^2>0\). Indeed \(e^L>1+L\). The denominator converges in probability to \(\sigma_L\). Slutsky's theorem yields \(Z_n\Rightarrow N(0,1)\) under both laws, and normal continuity yields the stated rejection probability. No claim about equality of their exact finite-sample laws is made.

**3. Total-variation asymptotics.** For discrete laws, \(1-d_{\mathrm{TV}}(P,Q)=\sum_k\min(P\{k\},Q\{k\})\). For \(u,v\to\infty\) with positive finite ratio, the two off-center masses of \(Q\) have positive limiting weights while the central and zero masses are of order \(O(uv e^{-uv})\). The Poisson local limit theorem, uniformly at these two displacements on the standard-deviation scale, gives
\[
\sqrt{uv}\,P_{uv}\{uv-u\}\to\frac{e^{-1/(2\rho)}}{\sqrt{2\pi}},\qquad
\sqrt{uv}\,P_{uv}\{uv+v\}\to\frac{e^{-\rho/2}}{\sqrt{2\pi}}.
\]
Thus the two outer minima are the Poisson point masses for large parameters; the center and zero minima are negligible on the \(\sqrt{uv}\) scale. Consequently \(\sqrt{uv}(1-d_{\mathrm{TV}}(P,Q))\to G(\rho)\). Since \(H=(1-\varepsilon)Q+\varepsilon P\),
\[
1-d_{\mathrm{TV}}(P,H)=\varepsilon+(1-\varepsilon)[1-d_{\mathrm{TV}}(P,Q)],
\]
with \(\varepsilon=(uv)^{-2}=o((uv)^{-1/2})\), proving the claimed limit for full-support \(H\).

**4. Sharp minimization inside the family.** Set \(z=\rho\) and let \(f(z)=z-z^{-1}-4\log z\). Symmetry gives \(G(z)=G(1/z)\), so it suffices to take \(z\ge1\). Differentiating \(G\) with respect to \(t=\sqrt z\) shows that its derivative has the sign of \(f(z)\). Now \(f(1)=0\) and
\[
f'(z)=\frac{(z-2)^2-3}{z^2}.
\]
Thus \(f\) is strictly decreasing on \((1,2+\sqrt3)\), then strictly increasing and tending to infinity. There is exactly one zero \(z_*>2+\sqrt3\), with \(G\) decreasing to \(z_*\) and increasing afterward. Its reciprocal is the only other minimizer. Approximating this positive real ratio by \(v/u\) with integers \(u,v\to\infty\) completes the sharp asymptotic construction.

## Verification

Run `python3 verify.py` with Python 3 from the same directory. The checker independently evaluates 480 finite high-precision mass, moment, and influence-variance assertions across 96 parameter pairs, then checks the reciprocal optimizer and Poisson overlap convergence. It passed. The symbolic identities and asymptotic argument above, not these finite assertions, establish the theorem.

## Relationship to prior work

Di Noia et al., *Goodness-of-fit test for count distributions with finite second moment* (first public preprint 2021-12-22; arXiv:2112.11861; subsequent journal publication 2022/2023), introduce the mean-and-zero-frequency statistic and prove asymptotic null normality and consistency where the population zero-mass discrepancy is nonzero. Their Proposition 3.1 and proof (pp. 5–6 of the accessible arXiv version), Section 4, and their discussion and tables were checked. They explicitly recognize that zero-mass conditions limit consistency. The present result does **not** claim that observation is new; it supplies a quantitative, full-support, variance-matched obstruction with a sharp total-variation constant inside a natural four-atom construction. Classical multivariate central limit and Poisson local limit theorems are proof ingredients, not newly established claims.

Frey's 2012 exact Poisson Kolmogorov–Smirnov work instead uses a conditional empirical-distribution process and does not state the present mean-and-zero-frequency construction; only its accessible abstract was checked. Other count-data Stein tests and Poisson goodness-of-fit surveys provide context for alternative procedures, not evidence that they share this statistic. A broader moment-matching impossibility principle could subsume the calibration observation, but no reviewed source was found that also establishes the explicit family and reciprocal-spacing optimum.

## Limitations

The result does not apply to a generic test using the whole empirical distribution, to tests using additional empirical cells, or to discretization-aware procedures designed to exploit small lattice differences. The sharp coefficient is optimized **only in the displayed two-offset family**; no global least-overlap theorem over all matched-moment alternatives is proved. Fixed-parameter calibration and the growing-parameter total-variation limit are separate statements, not a simultaneous high-dimensional-power claim. The literature comparison is not a proof of universal novelty, and independent checking of the mathematical result remains outstanding.

## References

1. Di Noia, A., Barabesi, L., Marcheselli, M., Pisani, C., and Pratelli, L. *Goodness-of-fit test for count distributions with finite second moment*. arXiv:2112.11861 (originally 2021-12-22), https://arxiv.org/abs/2112.11861 ; Journal of Nonparametric Statistics 35 (2023), 19–37, https://doi.org/10.1080/10485252.2022.2137728.
2. Frey, J. *An exact Kolmogorov–Smirnov test for the Poisson distribution with unknown mean*. Journal of Statistical Computation and Simulation 82 (2012), 1023–1033, https://doi.org/10.1080/00949655.2011.563740.
3. Mijburgh, P. A. and Visagie, I. J. H. *An overview of goodness-of-fit tests for the Poisson distribution*. South African Statistical Journal 54 (2020), 207–230, https://doi.org/10.37920/sasj.2020.54.2.6.
