# Inverse-rank collapse with vanishing Pearson correlation in bivariate power-Lindley survival models

## Finding

For the bivariate power-Lindley survival family of Martínez-Flórez, Arnold and Gómez [1], keep its two Lindley parameters and two conditional-shape parameters fixed and increase the nonnegative coupling parameter \(\kappa\). Its copula converges uniformly to the Fréchet lower-bound copula, so both Kendall's \(\tau\) and Spearman's \(\rho_S\) tend to \(-1\). Nevertheless, its ordinary Pearson correlation tends to zero from below with an **explicit sharp logarithmic equivalent**:

\[
\operatorname{Corr}(X_1,X_2)
=-\frac{A_1A_2}{\sqrt{B_1B_2}\,\log\kappa}
+o\!\left(\frac1{\log\kappa}\right).
\]

The strictly positive constants \(A_i,B_i\) are defined in the next section. In particular, Pearson correlation is strictly negative for every finite \(\kappa>0\), vanishes at \(\kappa=0\), and has a strictly negative interior minimum as a function of \(\kappa\); no uniqueness of that minimum is asserted. Perfect negative *rank* dependence can therefore coexist in the limit with arbitrarily small absolute *linear* correlation.

## Assumptions and scope

Fix \(\theta_1,\theta_2,a_1,a_2>0\), and let the coupling \(\kappa\in[0,\infty)\) vary. Define

\[
H_\theta(x)=\theta x-\log\left(1+\frac{\theta x}{\theta+1}\right),
\qquad x\ge0,
\]

and let \(h_\theta=H_\theta^{-1}\). For \(i=1,2\), write \(h_i=h_{\theta_i}\). Let the positive transformed variables \((Y_1,Y_2)\) have density

\[
p_\kappa(y,z)=Z_\kappa^{-1}
\exp\{-a_1y-a_2z-\kappa yz\},\qquad y,z>0,
\]

where \(Z_\kappa\) is the integral of the numerator on the positive quadrant, and set \(X_i=h_i(Y_i)\). The change \(y=H_{\theta_1}(x_1)\), \(z=H_{\theta_2}(x_2)\) gives precisely the conditionally specified bivariate power-Lindley survival family [1, Eq. (22) and Eq. (32)], with \((a_1,a_2,\kappa)=(\alpha_1,\alpha_2,\alpha_{12})\).

Set

\[
A_i=\int_0^\infty \frac{h_i(y)e^{-a_i y}}{y}\,dy,
\qquad
B_i=\int_0^\infty \frac{h_i(y)^2e^{-a_i y}}{y}\,dy.
\]

Both constants are finite and strictly positive for every stated parameter choice. Write \(C_\kappa\) for the copula of \((X_1,X_2)\) (the same as the copula of \((Y_1,Y_2)\)) and \(W(u,v)=\max\{u+v-1,0\}\) for \(0\le u,v\le1\). All limits below hold with \(\theta_i,a_i\) fixed and \(\kappa\to\infty\); they do not assert uniformity over parameter choices.

## Proof

**Step 1: controlling the inverse hazard and normalization.** A direct derivative gives

\[
H_\theta'(x)=\frac{\theta^2(1+x)}{\theta+1+\theta x}
\in\left[\frac{\theta^2}{\theta+1},\theta\right].
\]

Consequently, \(h_\theta\) is strictly increasing, and for \(y\ge0\),

\[
\frac{y}{\theta}\le h_\theta(y)\le \frac{\theta+1}{\theta^2}y.
\]

Integrating out \(z\) and substituting into the exponential integral \(E_1(s)=\int_s^\infty e^{-t}\,dt/t\) gives

\[
Z_\kappa=\int_0^\infty\frac{e^{-a_1y}}{a_2+\kappa y}\,dy
=\frac{e^{a_1a_2/\kappa}}{\kappa}
E_1\!\left(\frac{a_1a_2}{\kappa}\right)
\sim\frac{\log\kappa}{\kappa}.
\]

Here \(E_1(s)=-\log s-\gamma+o(1)\) at \(s\downarrow0\); at \(\kappa=0\), \(Z_0=1/(a_1a_2)\).

**Step 2: separate marginal and mixed moments.** Each marginal density has the form

\[
p_{Y_i}(y)=Z_\kappa^{-1}
\frac{e^{-a_i y}}{a_{3-i}+\kappa y},\qquad y>0.
\]

For \(p=1,2\), dominated convergence applies because

\[
0\le\frac{\kappa h_i(y)^p e^{-a_i y}}{a_{3-i}+\kappa y}
\le\frac{h_i(y)^p e^{-a_i y}}{y},
\]

and the right-hand side is integrable (like \(y^{p-1}\) near zero and exponentially decaying up to a polynomial factor at infinity). It follows that

\[
\mathbb E[X_i]\sim\frac{A_i}{\log\kappa},\qquad
\mathbb E[X_i^2]\sim\frac{B_i}{\log\kappa},\qquad
\operatorname{Var}(X_i)\sim\frac{B_i}{\log\kappa}.
\]

On the other hand, the linear bound on \(h_i\) gives \(\mathbb E[X_1X_2]\le c_1c_2\mathbb E[Y_1Y_2]\) for fixed positive \(c_i\). Conditional on \(Y_1=y\), \(Y_2\) is exponential of rate \(a_2+\kappa y\), and hence

\[
Z_\kappa\mathbb E[Y_1Y_2]
=\int_0^\infty\frac{y e^{-a_1y}}{(a_2+\kappa y)^2}\,dy
=O\!\left(\frac{\log\kappa}{\kappa^2}\right),
\]

where splitting at \(y=1/\kappa\) proves the last estimate. Thus \(\mathbb E[X_1X_2]=O(1/\kappa)=o((\log\kappa)^{-2})\), and

\[
\operatorname{Cov}(X_1,X_2)
\sim-\frac{A_1A_2}{(\log\kappa)^2}.
\]

Dividing by the marginal standard deviations proves the displayed sharp Pearson equivalent.

**Step 3: strict negativity at each finite positive coupling.** Given \(Y_1=y\), the distribution of \(Y_2\) is \(\operatorname{Exp}(a_2+\kappa y)\). Since \(h_2\) strictly increases, \(m_2(y)=\mathbb E[h_2(Y_2)\mid Y_1=y]\) strictly decreases in \(y\) for \(\kappa>0\). Thus \(\operatorname{Cov}(X_1,X_2)=\operatorname{Cov}(h_1(Y_1),m_2(Y_1))<0\) by the independent-copy identity for covariance of an increasing function and a strictly decreasing function under a nondegenerate continuous law. At \(\kappa=0\) the two coordinates are independent. Continuity of the first two moments and of covariance for finite \(\kappa\), together with the proved zero limits at both ends, implies the existence of at least one strictly negative interior minimum of Pearson correlation.

**Step 4: inverse-rank degeneration.** For \(\kappa>1\) define \(T_i=-\log Y_i/\log\kappa\). Fix \(0<u<v<1\). Uniformly over \(y\in[\kappa^{-v},\kappa^{-u}]\), the marginal integrand \(e^{-a_1 y}/(a_2+\kappa y)\) equals \((1+o(1))/(\kappa y)\). Therefore

\[
\mathbb P(u<T_1<v)
=\frac1{Z_\kappa}
\int_{\kappa^{-v}}^{\kappa^{-u}}
\frac{e^{-a_1y}}{a_2+\kappa y}\,dy
\longrightarrow v-u.
\]

The same estimates show that the mass of \(T_1\) outside any fixed enlargement of \([0,1]\) vanishes. Hence \(T_1\Rightarrow U\), where \(U\) is uniform on \([0,1]\). Realize the conditional distribution using an independent unit-rate exponential \(E\):

\[
Y_2=\frac{E}{a_2+\kappa Y_1},\qquad
T_2=\frac{\log(a_2+\kappa Y_1)-\log E}{\log\kappa}.
\]

Because \(T_1\Rightarrow U\) in \((0,1)\) with probability tending to one, the logarithmic expression converges jointly to \(1-U\). Thus

\[
(T_1,T_2)\Rightarrow(U,1-U).
\]

Each \(T_i\) has a continuous marginal approaching the uniform law. Its copula therefore converges pointwise to \(W\) by convergence of quantiles at every interior probability level. The maps from \(X_i\) to \(T_i\) are decreasing in *both* coordinates, so the copula of \(X\) is the double survival reflection of that of \(T\); the copula \(W\) is fixed by this double reflection. Accordingly, \(C_\kappa\to W\) pointwise on the whole unit square. Convergence is uniform by the common unit-Lipschitz bound for copulas and compactness of the square. Finally, the rank-score product formula for Spearman's coefficient and the two-independent-copies sign formula for Kendall's coefficient are continuous at the tie-free limit \((U,1-U)\); both converge to \(-1\).

## Verification

The companion `check.py` evaluates the two one-dimensional coefficient integrals, computes the marginal first and second moments from their exact one-dimensional integrals, and samples from the exact conditional exponential representation using inverse marginal CDF interpolation. Run `python check.py` with NumPy and SciPy. For \(\theta_1=\theta_2=a_1=a_2=1\), it obtains \(A_1=A_2\approx1.65845197625\), \(B_1=B_2\approx2.27068611250\), and the predicted Pearson coefficient \(A_1^2/B_1\approx1.21129157500\). At \(\kappa=10^8\), one fixed-seed simulation of 12,000 pairs gave Pearson \(-0.0745\), Kendall \(-0.8601\), and Spearman \(-0.9741\); the slow logarithmic convergence in Pearson correlation is expected. The finite-parameter diagnostics are *not* proof of the all-parameter theorem, which follows from the preceding integrability and weak-convergence arguments.

## Relationship to prior work

The underlying bivariate power-Lindley law, conditional distributions, transforms, general covariance formulas and numerical correlation ranges were already developed in [1]. The exponential-conditionals parent density and its negative finite-parameter Pearson correlation were established in [2]. General proportional-hazards transformations of bivariate exponential models are discussed in [3]; efficient generation of exponential-conditionals pairs is studied in [4]. The added result is the **simultaneous exact inverse-rank copula limit and nonzero logarithmic Pearson prefactor for the specified Lindley inverse-hazard coordinates**. Neither a new copula family nor a novel conditional specification is claimed. The full text of [2] was not accessible for exhaustive priority comparison; the publication-priority judgment is therefore provisional.

## Limitations

The theorem holds for fixed strictly positive \(\theta_i,a_i\) and nonnegative coupling, with the limit only along \(\kappa\to\infty\); it is not uniform over the shape or Lindley parameters. The endpoint \(\kappa=\infty\) is a limit of copulas, not an ordinary two-dimensional density with the stated marginals. No finite-coupling equality with the lower Fréchet bound, no rank convergence rate, and no uniqueness of the Pearson minimum are asserted. Earlier literature may contain unindexed results concerning the underlying exponential-conditionals strong-coupling asymptotics; historical priority requires further human source review. Independent mathematical review has not been performed.

## References

[1] G. Martínez-Flórez, B. C. Arnold and H. W. Gómez (2024), "A Bivariate Power Lindley Survival Distribution," *Mathematics* 12(21), 3334, first published 24 October 2024. https://doi.org/10.3390/math12213334. Open full text: https://repositorioabierto.uantof.cl/server/api/core/bitstreams/ce66f4ec-3c07-4e84-a173-83b396d4f60e/content.

[2] B. C. Arnold and D. J. Strauss (1988), "Bivariate Distributions with Exponential Conditionals," *Journal of the American Statistical Association* 83(402), 522–527. https://doi.org/10.1080/01621459.1988.10478627 (indexed abstract; complete article not inspected).

[3] B. C. Arnold, G. Martínez-Flórez and H. W. Gómez (2022), "Bivariate Proportional Hazard Models: Structure and Inference," *Symmetry* 14(10), 2073. https://doi.org/10.3390/sym14102073.

[4] Y. Yu (2009), "Efficient Simulation of a Bivariate Exponential Conditionals Distribution," arXiv:0909.4129. https://arxiv.org/abs/0909.4129.
