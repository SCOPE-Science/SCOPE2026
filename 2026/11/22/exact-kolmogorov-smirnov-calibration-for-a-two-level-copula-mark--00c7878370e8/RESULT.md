# Exact Kolmogorov–Smirnov calibration for a two-level copula Markov chain

## Finding

Consider the stationary uniform-marginal Markov chain induced by the two-level copula in Longla's 2023 preprint (published in 2024). For its **ordinary, unweighted empirical distribution function** \(F_n(u)=n^{-1}\sum_{j=1}^n\mathbf 1\{U_j\le u\}\), the asymptotic two-sided Kolmogorov–Smirnov statistic has an explicit one-dimensional integral distribution. The integral depends on the copula's persistence parameter through one Gaussian variance, and its distribution is strictly stochastically increasing in that persistence parameter. At the periodic endpoint, the limiting distribution is exactly the square of a rescaled classical Kolmogorov distribution; at the absorbing endpoint, the empirical CDF is inconsistent for the uniform margin. The latter endpoint distinctions are part of the same calibration classification.

More precisely, fix \(\alpha>0\), put \(p=(1+\alpha)^{-1}\), \(v=p(1-p)\), and define
\[
 \phi(u)=\begin{cases}\sqrt\alpha,&0\le u<p,\\-1/\sqrt\alpha,&p\le u\le1.\end{cases}
\]
Let \((U_j)_{j\ge1}\) be the stationary Markov chain with transition density
\[
 c_{\alpha,\lambda}(u,w)=1+\lambda\phi(u)\phi(w),\qquad
 -\min(\alpha,\alpha^{-1})\le\lambda\le1.
\]
Write \(D_n=\sup_{0\le u\le1}|F_n(u)-u|\). If \(|\lambda|<1\), then
\[
 \sqrt n D_n\Rightarrow S_{p,\lambda}=\sup_{u\in[0,1]}|\mathcal G_{p,\lambda}(u)|,
\]
where \(\mathcal G_{p,\lambda}\) is the continuous centered Gaussian process with covariance
\[
 K_{p,\lambda}(s,t)=\min(s,t)-st+
 \frac{2\lambda}{1-\lambda}\frac{g_p(s)g_p(t)}{v},\quad
 g_p(t)=\min(t,p)-pt.
\]
Put \(\sigma^2=(1+\lambda)/(1-\lambda)\), \(\gamma_a(y)=(2\pi a)^{-1/2}\exp[-y^2/(2a)]\), and the killed Brownian heat kernel
\[
 k_z(t;0,y)=\frac1z\sum_{j=1}^\infty
 \sin\frac{j\pi}{2}\sin\frac{j\pi(y+z)}{2z}
 \exp\left[-\frac{j^2\pi^2t}{8z^2}\right]
 \quad(t,z>0,\ -z<y<z).
\]
Then for every \(z>0\),
\[
 \boxed{\Pr(S_{p,\lambda}\le z)=
 \int_{-z}^{z}\gamma_{\sigma^2v}(y)
 \frac{k_z(p;0,y)}{\gamma_p(y)}
 \frac{k_z(1-p;0,y)}{\gamma_{1-p}(y)}\,dy.}
\]
For fixed \(p\in(0,1)\) and every \(z>0\), this CDF is **strictly decreasing** with \(\lambda\) on its admissible mixing interval. In particular the usual iid Kolmogorov critical values are asymptotically anticonservative for \(\lambda>0\) and conservative for \(\lambda<0\).

The only admissible \(\lambda=-1\) case is \(\alpha=1\), \(p=1/2\). Although the label chain then alternates periodically, the empirical-process CLT still holds and
\[
 \sqrt nD_n\Rightarrow S_-,\qquad\Pr(S_-\le z)=\mathsf K(\sqrt2z)^2,
 \qquad\mathsf K(x)=1-2\sum_{j\ge1}(-1)^{j-1}e^{-2j^2x^2}.
\]
At \(\lambda=1\), almost surely conditional on the absorbing label,
\[
 D_n\longrightarrow\begin{cases}1-p,&\text{with probability }p,\\p,&\text{with probability }1-p,\end{cases}
\]
so \(\sqrt nD_n\to+\infty\) in probability. All assertions concern known copula and known uniform margins, **not** statistics with fitted parameters.

## Assumptions and scope

The parameter \(\alpha\) is finite and positive; the two-level copula density is nonnegative precisely for \(-\min(\alpha,\alpha^{-1})\le\lambda\le1\). The process starts with its stationary uniform marginal; no parameter or marginal is estimated. The first-public-source date is 2023-08-21, as recorded on arXiv:2308.11074 (original version), regardless of the 2024 journal publication date. The primary MSC2020 class is 62G10 (nonparametric hypothesis testing), with connections to 62G30, 60J10 and 62H05.

## Proof

**1. Two-state reduction, with all boundary parameters.** Put \(I_j=\mathbf1\{U_j<p\}\). Direct block integration of \(c_{\alpha,\lambda}\) gives, ordering states \(1,0\),
\[
 P=\begin{pmatrix}p+\lambda(1-p)&(1-p)(1-\lambda)\\p(1-\lambda)&1-p+\lambda p\end{pmatrix}.
\]
The stationary probabilities are \((p,1-p)\), and the second eigenvalue is \(\lambda\). Conditional on the *entire* state sequence, the \(U_j\)'s are independent and uniform on the appropriate one of \([0,p]\) and \((p,1]\). This follows since the transition density is constant on each source/destination block. For \(|\lambda|<1\), this two-state chain is irreducible and aperiodic, including admissible cases where one diagonal entry is zero. Its stationary indicator covariance is \(\operatorname{Cov}(I_0,I_k)=v\lambda^k\).

**2. Functional central limit theorem and independence of components.** Set \(L_n=n^{-1/2}\sum_{j=1}^n(I_j-p)\). From the bounded martingale-difference representation \((I_j-p)-\lambda(I_{j-1}-p)\), the finite-state Markov CLT yields
\[
 L_n\Rightarrow Z,\qquad Z\sim N(0,v(1+\lambda)/(1-\lambda)).
\]
At \(\lambda=-1,p=1/2\), the labels alternate and \(L_n\to0\), so the same conclusion holds with \(Z\equiv0\). Conditional on the labels, both within-block samples consist of independent uniforms. The conditional Donsker theorem with random sample sizes \(n^{-1}\sum I_j\to p\) and \(n^{-1}\sum(1-I_j)\to1-p\) yields two mutually independent centered Gaussian bridge processes \(R_L\) and \(R_R\), independent of \(Z\). Specifically, their covariances on their respective blocks are
\[
 \operatorname{Cov}(R_L(s),R_L(t))=\min(s,t)-st/p\quad(s,t\le p),
\]
\[
 \operatorname{Cov}(R_R(s),R_R(t))=\min(s,t)-p-\frac{(s-p)(t-p)}{1-p}\quad(s,t\ge p),
\]
with zero covariance across blocks; each vanishes at its own endpoints. To see the decomposition directly, for \(u\le p\) the conditional expectation of \(\mathbf1\{U_j\le u\}\) is \(I_j u/p\), and for \(u\ge p\) it is \(I_j+(1-I_j)(u-p)/(1-p)\). Consequently
\[
 \mathbb G_n(u)=\sqrt n(F_n(u)-u)\Rightarrow
 \mathcal G_{p,\lambda}(u)=R(u)+h_p(u)Z,
\]
where \(R\) equals \(R_L\) or \(R_R\) on the corresponding block, and \(h_p(u)=u/p\) for \(u\le p\), \(h_p(u)=(1-u)/(1-p)\) for \(u\ge p\). Standard random-size empirical bridge tightness gives convergence in \(\ell^\infty([0,1])\). Direct covariance algebra with \(g_p(u)=v h_p(u)\) produces the claimed kernel; the continuous mapping theorem yields \(\sqrt nD_n\Rightarrow S_{p,\lambda}\).

**3. Exact CDF of the supremum.** The residual bridge \(R\) has precisely the law of a standard Brownian bridge conditioned to be zero at time \(p\), independent of its knot value. Thus conditionally on \(Z=y\), \(\mathcal G_{p,\lambda}\) consists of two independent ordinary Brownian bridges, one from \(0\) to \(y\) over duration \(p\), the other from \(y\) to \(0\) over duration \(1-p\). By the Markov property, a bridge from \(a\) to \(b\) over time \(t\) stays in \((-z,z)\) with probability \(k_z(t;a,b)/\gamma_t(b-a)\). Expanding the Dirichlet heat equation \(\partial_t k=\tfrac12\partial_{yy}k\) on \((-z,z)\) in normalized sine eigenfunctions gives the displayed absolutely convergent kernel for every positive \(t,z\). Multiplying the two conditional survival probabilities and integrating against the Gaussian density of \(Z\) gives the claimed one-dimensional integral. Replacing open by closed barriers has no effect because the supremum has no atom at positive \(z\).

**4. Strict calibration ordering.** For the same \(p\), the residual \(R\) has a law independent of \(\lambda\); all dependence enters through the variance of the one-dimensional normal knot \(Z\). If \(\lambda_1<\lambda_2<1\), couple \(Z_2=Z_1+W\) with \(W\) an independent centered normal of strictly positive variance. The ball \(A_z=\{f:\sup|f|\le z\}\) in continuous path space is symmetric and convex. Anderson's Gaussian shift inequality gives \(\Pr(R+h_p Z_1+w h_p\in A_z)\le\Pr(R+h_p Z_1\in A_z)\) for every \(w\). This centered Gaussian shift probability is continuous, positive at zero, and tends to zero for \(|w|\to\infty\), as can already be seen at the knot \(p\). Since \(W\) has full support, averaging yields a **strict** inequality between the CDFs for all \(z>0\). The same argument applies starting at the periodic \(\lambda=-1,p=1/2\) case, with a zero-variance knot.

**5. Endpoints.** At \(p=1/2,\lambda=-1\), labels alternate and the independent within-block limit bridges each have amplitude \(\sqrt{1/2}\); hence the supremum is the maximum of two independent \(2^{-1/2}\)-scaled classical Kolmogorov suprema, giving \(\mathsf K(\sqrt2z)^2\). At \(\lambda=1\), transitions between blocks are impossible and, conditional on the initial block, all subsequent observations are independent uniforms on that block. The strong law gives the stated conditional limiting empirical CDF discrepancy. This proves the non-Gaussian phase boundary and completes the classification.

## Verification

The standalone script `verify.py` checks the two-state stationary reduction and algebraic covariance identity, evaluates the heat-kernel integral by independent numerical quadrature, reproduces the classical Kolmogorov CDF at \(\lambda=0\), and checks representative strict dependence orderings and the periodic-endpoint limit. A finite simulation illustrates convergence; its random error is not used as proof. The exact endpoint claims and infinite-sample asymptotics are established analytically above.

## Relationship to prior work

Longla, *New copula families and mixing properties* (arXiv:2308.11074; 2024 journal publication), introduces the two-level copula and studies its spectral decomposition and mixing structure. Longla and Hamadou (2025) and Longla and Siddiqua (2025) study parameter estimation, CLTs and independence tests for related copula Markov chains. Doukhan–Fermanian–Lang (2009) give a broad weak-dependence empirical-process CLT, which covers the existence of a Gaussian limit in relevant mixing cases but does **not** state the present model-specific scalar killed-heat-kernel law, strict dependence-parameter KS calibration ordering, or its periodic/absorbing endpoint contrast. Janczura–Weron (2013) calibrate weighted *residual* empirical distributions in regime switching, rather than the ordinary marginal empirical CDF of this copula chain. The Brownian killed heat kernel and Anderson inequality are standard; their general validity is not claimed as new. The contribution is their exact conjunction for the specified Markov observation model and the sharp usable calibration boundary.

## Limitations

The statistic assumes known uniform margins and known copula parameters. Estimating either changes the asymptotic distribution. The integral is an exact asymptotic null CDF, not a finite-sample formula or a convergence-rate bound. At the absorbing boundary \(\lambda=1\), a stationary but nonergodic sample is not a consistent estimator of its unconditional marginal. Other piecewise-constant copula families and general continuous-state Markov models are not classified. Full historical priority cannot be certified from available literature alone; a related 2025 handbook chapter was available chiefly through its public overview rather than its full text. No independent mathematical audit has been undertaken.

## References

1. M. Longla, *New copula families and mixing properties*, arXiv:2308.11074, first posted 2023-08-21; *Statistical Papers* **65** (2024), 4331–4363, https://doi.org/10.1007/s00362-024-01559-9.
2. P. Doukhan, J.-D. Fermanian and G. Lang, *An empirical central limit theorem with applications to copulas under weak dependence*, *Statistical Inference for Stochastic Processes* **12** (2009), 65–87, https://doi.org/10.1007/s11203-008-9026-3.
3. M. Longla and M.-A. Hamadou, *Estimation problems for some perturbations of the independence copula*, *Statistical Papers* **66** (2025), 156, https://doi.org/10.1007/s00362-025-01778-8.
4. M. Longla and S. Siddiqua, *Comparative Study of Estimation Methods for a New Family of Copula-Based Reversible Markov Chains*, *Mathematics* **13** (2025), 3661, https://doi.org/10.3390/math13223661.
5. J. Janczura and R. Weron, *Goodness-of-fit testing for the marginal distribution of regime-switching models with an application to electricity spot prices*, *Advances in Statistical Analysis* **97** (2013), 239–270, https://doi.org/10.1007/s10182-012-0202-9.
6. M. Longla, *On estimation problems based on type I Longla copulas*, *Handbook of Statistics* **52** (2025), 3–28, https://doi.org/10.1016/bs.host.2025.01.006 (overview examined; full chapter not inspected).
