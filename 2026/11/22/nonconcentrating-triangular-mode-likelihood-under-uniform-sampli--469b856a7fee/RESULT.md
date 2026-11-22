# Nonconcentrating triangular-mode likelihood under uniform sampling: a Brownian-bridge argmax law

## Finding

Let \(X_1,\ldots,X_n\) be independent uniform observations on \([0,1]\). Fit the triangular density with unknown mode \(\theta\in[0,1]\), and choose **any measurable global likelihood maximizer** \(\widehat\theta_n\). The expected log likelihood per observation is *constant* in \(\theta\). Nevertheless, its random, globally centered profile has a nondegenerate functional limit:
\[
\left\{\frac{\ell_n(\theta)-\ell_n(1/2)}{\sqrt n}:0\leq\theta\leq1\right\}\ \Longrightarrow\
\left\{Z(\theta)=-\int_{1/2}^{\theta}\frac{B(t)}{t(1-t)}\,dt:0\leq\theta\leq1\right\}
\quad\text{in }C([0,1]),
\]
where \(B\) is a standard Brownian bridge and both integrals have their continuous improper-endpoint meanings. Almost surely \(Z\) has one and only one global maximizer \(\Theta\). Consequently
\[
\widehat\theta_n\Longrightarrow\Theta,
\qquad
\Pr(\Theta<1/2)=\Pr(\Theta>1/2)=1/2,
\qquad \Pr(\Theta=1/2)=0.
\]
Thus a triangular-mode maximum-likelihood fit to uniform data **does not concentrate at any deterministic mode**. This is the singular, completely unidentified boundary of the nontriangular-density asymptotics considered by Hjort (2026).

## Assumptions and scope

The observations are i.i.d. \(\operatorname{Uniform}[0,1]\), with known endpoints. For \(0<\theta<1\) the fitted density is
\[
f_\theta(x)=\begin{cases}2x/\theta,&0\leq x\leq\theta,\\2(1-x)/(1-\theta),&\theta<x\leq1.\end{cases}
\]
The \(\theta=0\) and \(\theta=1\) models are the continuous limits \(2(1-x)\) and \(2x\), respectively. For samples in the open interval, define \(\ell_n(\theta)=\sum_{i=1}^n\log f_\theta(X_i)\), extended continuously to both endpoints. Every global maximizer exists by continuity. Ties may be resolved measurably in any way; the limit does not depend on tie-breaking. For each fixed \(n\), all maximizers lie among the sample points.

## Proof

**1. Exact score and global profile.** Let \(F_n(t)=n^{-1}\sum_{i=1}^n\mathbf1_{\{X_i\leq t\}}\) and \(B_n(t)=\sqrt n\{F_n(t)-t\}\). Between consecutive sample points, direct differentiation gives
\[
\ell_n'(t)=-\frac{nF_n(t)}t+\frac{n(1-F_n(t))}{1-t}
=-\sqrt n\frac{B_n(t)}{t(1-t)}.
\]
The log likelihood is continuous at each sample point, so integration across finitely many pieces gives the *exact identity*, including at endpoints,
\[
\frac{\ell_n(\theta)-\ell_n(1/2)}{\sqrt n}
=-\int_{1/2}^{\theta}\frac{B_n(t)}{t(1-t)}\,dt.
\tag{1}
\]
For \(t\) before the smallest sample the score is positive, and after the largest it is negative. Between successive observations, its second derivative is
\[
\ell_n''(t)=\frac{nF_n(t)}{t^2}+\frac{n(1-F_n(t))}{(1-t)^2}>0.
\]
Therefore every finite-sample maximum occurs at an observed point. For the population criterion, using \(\int_0^\theta\log(x/\theta)\,dx=-\theta\) and \(\int_\theta^1\log((1-x)/(1-\theta))\,dx=-(1-\theta)\), we obtain
\[
\mathbb E\{n^{-1}\ell_n(\theta)\}=\log2-1
\quad\text{for all }0\leq\theta\leq1.
\tag{2}
\]

**2. Functional convergence, including the singular endpoints.** The uniform empirical-process theorem gives \(B_n\Rightarrow B\) in the uniform topology on bounded functions over \([0,1]\). On \([\delta,1-\delta]\), with \(0<\delta<1/2\), integration against \(1/[t(1-t)]\) is continuous in that topology. To remove the cutoff, Cauchy–Schwarz and the exact binomial variance yield, simultaneously for every \(n\geq1\),
\[
\mathbb E\int_0^\delta\frac{|B_n(t)|}{t(1-t)}\,dt
\leq\int_0^\delta\frac{dt}{\sqrt{t(1-t)}}
=2\arcsin\sqrt\delta\longrightarrow0.
\tag{3}
\]
The identical estimate holds near \(1\) and for \(B\), whose pointwise variance is \(t(1-t)\). The sup norm between the full integral process and its truncated counterpart is bounded by the sum of the two tails. Converging-together and Donsker theorems applied to (1) now give the claimed convergence in \(C([0,1])\). In particular, the improper endpoint integrals exist almost surely and form continuous paths.

**3. A unique Gaussian global argmax.** Write \(I=\int_0^1B(t)\,dt\) and \(\eta=6I\). Since \(\operatorname{Var}(I)=1/12\) and \(\operatorname{Cov}(B(t),I)=t(1-t)/2\), the Gaussian residual
\[
B_\perp(t)=B(t)-\eta t(1-t)
\]
is independent of \(\eta\sim N(0,3)\). Setting \(Z_\perp(\theta)=-\int_{1/2}^{\theta}B_\perp(t)/[t(1-t)]\,dt\), we have
\[
Z(\theta)=Z_\perp(\theta)-\eta(\theta-1/2).
\tag{4}
\]
For *any fixed* continuous function \(g\) on \([0,1]\), the support function \(h(c)=\max_{0\leq t\leq1}\{g(t)-c(t-1/2)\}\) is finite and convex, hence differentiable for Lebesgue-almost every real \(c\). If distinct values of \(t\) attained its maximum, its subgradient would contain at least two distinct slopes \(-(t-1/2)\), so \(h\) would not be differentiable. Conditional on \(Z_\perp=g\), the independent \(\eta\) has an absolutely continuous law. Therefore (4) has a unique maximizing \(\Theta\) almost surely. The argmax continuous mapping theorem on the compact interval, combined with the functional convergence, proves \(\widehat\theta_n\Rightarrow\Theta\) regardless of the measurable tie rule.

**4. Symmetry and genuine randomness.** The reversed, sign-flipped bridge \(B^*(t)=-B(1-t)\) has the same law as \(B\), and its integrated profile is exactly \(Z^*(t)=Z(1-t)\). Therefore \(\Theta\) and \(1-\Theta\) have the same distribution. On the other hand, \(Z\) is differentiable at \(1/2\) and \(Z'(1/2)=-4B(1/2)\ne0\) almost surely. Hence \(\Pr(\Theta=1/2)=0\), and symmetry forces equal probabilities \(1/2\) on either side. In particular, the estimator cannot be consistent for any fixed deterministic parameter.

## Verification

The accompanying standalone `checker.py` verifies finite-sample exact score identities by independent likelihood evaluation, equality of the population objective at rational modes, exact Brownian-bridge covariance decompositions at rational times, and symmetric endpoint-contrast calculations. It is a diagnostic; no finite simulation or finite check is used to infer functional convergence, almost-sure uniqueness, or the global infinite-dimensional limit. Those follow analytically in the four steps above. Run `python3 checker.py` with standard Python only.

## Relationship to prior work

Hjort, *Unlikely likelihoods: likelihood analysis for the triangular and random histogram models*, arXiv:2611.01030v1, Section 3.2 (2026-10-31), studies the very same triangular likelihood under nontriangular sampling densities but assumes a **unique** solution to \(F(\theta)=\theta\) and \(f(\theta)>1\). Under uniform sampling, \(F(\theta)=\theta\) and \(f(\theta)=1\) identically: the hypotheses fail maximally. Its local Gaussian/quadratic limit and normal estimator are therefore not a prior statement of this global centered Brownian-bridge process or random argmax law. Hjort cites Oliver (1972) for the finite-sample sample-point maximization, which is acknowledged here.

Ferguson, *An Inconsistent Maximum Likelihood Estimate*, *Journal of the American Statistical Association* **77** (1982), 831–834, DOI 10.1080/01621459.1982.10477894, instead gives a different parametric family interpolating a triangular and a uniform distribution; its abstract reports a deterministic inconsistent limit at the uniform endpoint. That does not imply the present random mode-argmax law. The empirical-process theorem, Gaussian regression decomposition and convex support-function differentiability are standard ingredients, not independently claimed discoveries.

## Limitations

The result concerns i.i.d. exactly uniform sampling with known interval endpoints and this one-parameter triangular-mode family. It does not cover nearby alternatives on an unspecified local scale, arbitrary misspecification, predictive performance, other triangular parametrizations, Bayesian posteriors or uniqueness of the finite-sample MLE. The exact density of \(\Theta\) is not determined. The literature comparison does not establish worldwide historical priority; the full text of some older algorithmic works was not independently inspected. No independent mathematical validation has been performed.

## References

1. N. L. Hjort (2026), *Unlikely likelihoods: likelihood analysis for the triangular and random histogram models*, arXiv:2611.01030v1 (first publicly submitted 2026-10-31), https://arxiv.org/html/2611.01030v1.
2. T. S. Ferguson (1982), *An Inconsistent Maximum Likelihood Estimate*, *JASA* **77**, 831–834, https://doi.org/10.1080/01621459.1982.10477894.
3. Standard empirical-process convergence for the uniform empirical CDF (Donsker's theorem) and the continuous argmax mapping theorem; standard convex differentiability and Gaussian orthogonal projection facts.
