# Sharp entropy-endpoint laws along the fixed-mean Poisson–geometric path

## Finding

For each fixed mean \(\mu>0\), let \(X_t=P_{\mu-t}+G_t\) for \(0\le t\le\mu\), where the two summands are independent, \(P_{\mu-t}\) is Poisson with mean \(\mu-t\), and \(G_t\) is zero-based geometric with mean \(t\):
\[
 \Pr(G_t=n)=\frac{1}{1+t}\left(\frac{t}{1+t}\right)^n,
 \qquad n=0,1,2,\ldots.
\]
Write \(h_\mu(t)=H(X_t)=-\sum_{n\ge0}\Pr(X_t=n)\log\Pr(X_t=n)\), with natural logarithms. The entire path has mean \(\mu\), variance \(\mu+t^2\), and satisfies **strict convex ordering**: \(X_s<_{\mathrm{cx}}X_t\) whenever \(0\le s<t\le\mu\), meaning that every non-affine strictly convex test function with existing expectation has strictly smaller expectation at \(s\) than at \(t\). Its Shannon entropy is **strictly increasing**:
\[
 H(\operatorname{Pois}(\mu))=h_\mu(0)<h_\mu(t)<h_\mu(\mu)
 = (1+\mu)\log(1+\mu)-\mu\log\mu,
 \quad 0<t<\mu.
\]
More importantly, there are **exact quadratic entropy laws at both endpoints**, with no undetermined constants:
\[
 \boxed{\displaystyle\lim_{t\downarrow0}
 \frac{h_\mu(t)-h_\mu(0)}{t^2}
 =\frac12\,\mathbb E_{N\sim\operatorname{Pois}(\mu)}
 \left[\log\frac{N+2}{N+1}\right]>0,}
\]
\[
 \boxed{\displaystyle\lim_{t\uparrow\mu}
 \frac{h_\mu(\mu)-h_\mu(t)}{(\mu-t)^2}
 =\frac{1}{2(1+\mu)}.}
\]
The first-order sensitivity of entropy vanishes at **both** ends of the entire interpolation, even though entropy increases strictly in its interior. The second formula equivalently gives the sharp local Kullback–Leibler distance from the maximum-entropy geometric law of the same mean.

## Assumptions and scope

All variables take values in \(\mathbb Z_{\ge0}\). At \(t=0\), the geometric term is identically zero; at \(t=\mu\), the Poisson term is identically zero. The path is exactly the Poisson–geometric convolution family, restricted to the statistically natural fixed-mean slice. The definition of strict convex ordering is the ordinary convex order together with a strict inequality for every *strictly convex* test function for which both expectations are finite; no claim of strictness for every merely convex function is made.

For \(0<t<\mu\), put \(q=t/(1+t)\), \(\lambda=\mu-t\), \(a=\lambda/q\), and \(S_n(a)=\sum_{j=0}^{n}a^j/j!\). The probability-generating function and probability masses are
\[
 G_t(z)=\frac{\exp((\mu-t)(z-1))}{1+t(1-z)},\qquad
 p_n(t)=e^{-\lambda}(1-q)q^n S_n(a)>0.
\]
Thus the logarithms, entropy, and all moments exist. The statements concern the *one-dimensional marginal counts*, not a fitted regression or a time-series transition mechanism.

## Proof

**1. A mean-preserving, strictly convexly increasing path.** For \(q=t/(1+t)\), the logarithm of the generating function has the compound-Poisson expansion
\[
 \log G_t(z)=(\mu-t)(z-1)
 +\sum_{k\ge1}\frac{q^k}{k}(z^k-1).
\]
Write \(a_1(t)=\mu-t+q\) and \(a_k(t)=q^k/k\) for \(k\ge2\). On \((0,\mu)\), direct differentiation gives
\[
 a_k'(t)=\frac{q^{k-1}}{(1+t)^2}>0\ (k\ge2),
 \qquad a_1'(t)=-\sum_{k\ge2}k a_k'(t).
\]
For any convex sequence \(\phi:\mathbb Z_{\ge0}\to\mathbb R\) of at most polynomial growth, differentiating the generating function and exchanging absolutely convergent sums yields
\[
 \frac{d}{dt}\mathbb E\phi(X_t)
 =\sum_{k\ge2}a_k'(t)\,
 \mathbb E\!\left[\phi(X_t+k)-\phi(X_t)
 -k\bigl(\phi(X_t+1)-\phi(X_t)\bigr)\right]\ge0.
\]
Each bracket is nonnegative by convexity, and is strictly positive for a strictly convex sequence and \(k\ge2\). At the endpoints, continuity of the distributions with their exponential moments, followed by integration in \(t\), extends the inequalities. Standard convex-order truncation extends them beyond polynomial-growth tests whenever the expectations exist. The mean and variance follow either from independence or the generating function, giving \(\mathbb E X_t=\mu\) and \(\mathrm{Var}(X_t)=\mu+t^2\).

**2. Strict log-concavity and entropy ordering.** The masses are strictly log-concave for \(0<t<\mu\). Indeed, put \(w_j=a^j/j!\), so \(S_n=\sum_{j\le n}w_j\); then for every \(n\ge1\)
\[
 S_n^2-S_{n-1}S_{n+1}
 =\frac{w_n}{n+1}\left[(n+1)S_n-aS_{n-1}\right]
 =\frac{w_n}{n+1}\left[(n+1)+\sum_{j=1}^n(n+1-j)w_j\right]>0.
\]
The geometric factor \(q^n\) does not change these inequalities. Define \(\psi_t(n)=-\log p_n(t)\), a strictly convex sequence. Since \(\sum_n p_n'(t)=0\), differentiation of Shannon entropy gives
\[
 h_\mu'(t)=\sum_{k\ge2}a_k'(t)\,
 \mathbb E\!\left[\psi_t(X_t+k)-\psi_t(X_t)
 -k\bigl(\psi_t(X_t+1)-\psi_t(X_t)\bigr)\right]>0.
\]
All exchanges are justified by the geometric tail, finite moments and locally uniform exponential bounds on the coefficients and their derivatives. Entropy is continuous at \(0\) and \(\mu\), as can be seen by uniformly bounded exponential moments in a compact neighborhood of either endpoint. The endpoint laws are Poisson and geometric; the geometric entropy formula follows by summing the geometric series. The strict interior derivative plus continuity establishes the inequalities for all endpoints.

**3. Exact Poisson-endpoint curvature.** The generating-function derivative simplifies *without approximation* to
\[
 \partial_t G_t(z)=\frac{t(1-z)^2}{1+t(1-z)}G_t(z).
\]
At \(t=0\), therefore, \(p_n'(0)=0\) and \(p_n''(0)=\pi_n-2\pi_{n-1}+\pi_{n-2}\), where \(\pi_n=e^{-\mu}\mu^n/n!\) and \(\pi_j=0\) for \(j<0\). The right second derivative of entropy exists, and its \(p_n'(0)\)-squared term vanishes. Consequently,
\[
 h_\mu''(0)=-\sum_{n\ge0}
 (\pi_n-2\pi_{n-1}+\pi_{n-2})\log\pi_n
 =\mathbb E_{N\sim\operatorname{Pois}(\mu)}\left[
 \log\frac{N+2}{N+1}\right].
\]
For completeness, the differentiation at the endpoint can be justified by splitting the entropy sum at \(n=\lceil K\log(1/t)\rceil\), with \(K\) fixed sufficiently large. On the initial segment the convolution formula and \(q=O(t)\) give uniform, termwise Taylor expansions relative to the Poisson masses because \(nq/\lambda=o(1)\). On the tail, choose a fixed exponential-moment radius \(R>1\) for \(t\) in a sufficiently small neighborhood of zero; the probabilities and their first two derivatives are bounded by \(C_RR^{-n}\), while \(-\log p_n(t)\le C_\mu+C_\mu n\log(n+1)\) follows from the positive Poisson summand. Taking \(K\log R>6\) makes the omitted entropy and derivative tails \(o(t^2)\); the logarithmic derivative of each convolution mass is bounded by \(C_\mu(n+1)/t\) for \(t>0\), so the Fisher-type tail is at worst a polynomial in \(n\) times \(t^{-2}R^{-n}\). Thus \(h_\mu(t)=h_\mu(0)+\frac12h_\mu''(0)t^2+o(t^2)\), proving the first boxed limit.

**4. Exact geometric-endpoint curvature.** Write \(g_n=(1-q_*)q_*^n\) for the geometric law of mean \(\mu\), with \(q_*=\mu/(1+\mu)\). Since \(-\log g_n\) is affine in \(n\), and \(X_t\) and \(g\) have the same mean,
\[
 h_\mu(\mu)-h_\mu(t)
 =D_{\mathrm{KL}}(p(t)\Vert g)
 =\sum_{n\ge0}p_n(t)\log\frac{p_n(t)}{g_n}.
\]
The exact generating-function derivative at the endpoint is
\[
 \left.\partial_t G_t(z)\right|_{t=\mu}
 =\frac{\mu(1-z)^2}{(1+\mu(1-z))^2}.
\]
Let \(s_n=(\partial_t p_n)(\mu)/g_n\) be its coefficientwise score. Extracting coefficients yields the simple closed form
\[
 s_0=\frac\mu{1+\mu},\qquad
 s_n=\frac{n-1-2\mu}{\mu(1+\mu)}\quad(n\ge1).
\]
Direct summation using \(\sum_{n\ge1}q_*^n=q_*/(1-q_*)\), \(\sum_{n\ge1}nq_*^n=q_*/(1-q_*)^2\), and \(\sum_{n\ge1}n^2q_*^n=q_*(1+q_*)/(1-q_*)^3\) gives
\[
 \sum_{n\ge0}g_ns_n=0,
 \qquad \sum_{n\ge0}g_ns_n^2=\frac1{1+\mu}.
\]
The masses depend smoothly on \(t\) from the left, with a locally uniform geometric upper tail and polynomially bounded score derivatives. Therefore the quadratic Taylor expansion of relative entropy at \(g\) is valid in the weighted summation norm:
\[
 D_{\mathrm{KL}}(p(\mu-\varepsilon)\Vert g)
 =\frac{\varepsilon^2}{2}\sum_{n\ge0}g_ns_n^2+o(\varepsilon^2)
 =\frac{\varepsilon^2}{2(1+\mu)}+o(\varepsilon^2).
\]
This completes the second boxed limit. Both coefficients are strictly positive for every fixed \(\mu>0\).

## Verification

The companion `verify.py` is a standalone Python 3 standard-library reproducer. Run `python3 verify.py` in the directory containing both files. It independently constructs the probability masses by the positive recurrence \(p_{n+1}=q p_n+(1-q)e^{-\lambda}\lambda^{n+1}/(n+1)!\), checks normalization and the exact mean/variance, compares entropy across the path, verifies strict log-concavity at representative parameters, checks numerical convergence to the two coefficients, and tests the geometric endpoint score and its squared norm. The final success marker is `VERIFICATION_OK`. These finite checks are supplementary only: the continuous-in-parameter and all-index assertions are established analytically in the proof.

## Relationship to prior work

Nandi, Chakraborty and Biswas [1,2] investigated this same independent Poisson-plus-geometric count family under the PoiG name and studied its generating function, moments, log-concavity, stochastic orders and inference. Neither the generating function nor the model itself is claimed as new here. The same law is also the shape-one slice of the older Delaporte (Poisson–negative-binomial convolution) distribution [5]; neither this alias nor the parent family is claimed as new. The manuscript abstract and the 2024 journal abstract were available, but the full source text could not be retrieved; that creates a remaining risk concerning the exact scope of the originally reported stochastic-order results. The present mathematical claim is restricted to the fixed-mean entropy interpolation **together with both exact quadratic endpoint coefficients**.

The general theorem of Yu, as presented and proved or applied in Xia–Lv [3], establishes entropy ordering from convex ordering when the upper law is log-concave. That theorem substantially anticipates the qualitative entropy implication *once the particular fixed-mean convex-order path is established*. The classical maximum-entropy characterization of the geometric law and the general entropy-ordering theorem likewise give the endpoint inequality, but do not supply either displayed Poisson–geometric endpoint coefficient. The strictly increasing interior path and two explicit asymptotics are the claim assessed here, not the general entropy-ordering principle. No broader priority or uniqueness assertion is made.

## Limitations

The result is a one-parameter, fixed-mean slice of the two-parameter Poisson–geometric family; it does not treat independent perturbations of both parameters, Rényi entropy, statistical estimator risk, or arbitrary mixtures. Strict convex order is claimed only for strictly convex test functions with existing expectations. The asymptotics are **pointwise in each fixed mean** \(\mu>0\), not uniform as \(\mu\downarrow0\) or \(\mu\to\infty\). Numerical checks do not independently certify the analytic continuum theorem. Earlier literature may contain an equivalent statement missed because the original full text was inaccessible; independent external validation and historical priority certification have not occurred.

## References

[1] A. Nandi, S. Chakraborty and A. Biswas, *A new over-dispersed count model*, arXiv:2301.01480, first submitted 4 January 2023, https://arxiv.org/abs/2301.01480.

[2] A. Nandi, S. Chakraborty and A. Biswas, *A new over-dispersed count model based on Poisson-Geometric convolution*, Communications in Statistics - Simulation and Computation, published online 21 March 2024, https://doi.org/10.1080/03610918.2024.2329997.

[3] W. Xia and W. Lv, *Log-concavity and relative log-concave ordering of compound distributions*, Probability in the Engineering and Informational Sciences, published online 29 January 2024, https://doi.org/10.1017/S0269964823000293, Theorem 1.1 and Sections 3–5.

[4] O. Johnson, *Log-concavity and the maximum entropy property of the Poisson distribution*, arXiv:math/0603647, 2006, https://arxiv.org/abs/math/0603647 (background on discrete entropy and log-concavity).

[5] *Delaporte distribution*, classical Poisson–negative-binomial convolution (shape-one negative-binomial component reduces to a zero-based geometric), general definition and formula at https://en.wikipedia.org/wiki/Delaporte_distribution.
