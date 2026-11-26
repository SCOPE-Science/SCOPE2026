# Collision Cauchy tails and a sharp square-root nugget cost in two-node Gaussian kernel quadrature

## Finding

For two independent uniformly sampled nodes and a Gaussian radial-basis kernel, unregularized kernel quadrature amplifies arbitrarily small independent Gaussian measurement noise into an error with an exact two-sided inverse-linear tail. The same construction without measurement noise is uniformly bounded for every fixed Lipschitz integrand. A positive kernel nugget restores finite variance, but its sharp small-nugget noise-amplification cost diverges as the reciprocal square root of the nugget.

Precisely, for every \(\alpha>0\) and \(\sigma>0\), define
\[
C_{\alpha,\sigma}=\frac{\sigma}{\alpha\sqrt\pi}\int_0^1|m_\alpha'(u)|\,du
=\frac{\sigma}{\alpha^{3/2}}\left[2\operatorname{erf}(\sqrt\alpha/2)-\operatorname{erf}(\sqrt\alpha)\right]>0.
\]
The unregularized independent-noise contribution \(R_0\) satisfies
\[
\lim_{t\to\infty}t\Pr(R_0>t)=\lim_{t\to\infty}t\Pr(R_0<-t)=C_{\alpha,\sigma}.
\]
Consequently \(\mathbb E|R_0|^p<\infty\) exactly for \(0<p<1\). For every fixed Lipschitz integrand, the complete noisy quadrature error has the same asymptotic positive and negative tail coefficients and the same moment cutoff.

For regularization \(\eta>0\), the sharp noise-variance amplification law is
\[
\lim_{\eta\downarrow0}\sqrt\eta\,\mathbb E_{X,Y}\|w^\eta\|_2^2=B_\alpha,
\qquad B_\alpha=\frac{\pi}{4\alpha^{3/2}}\int_0^1(m_\alpha'(u))^2\,du>0.
\]
Thus with the observation-noise-matched nugget \(\eta=\sigma^2\) and zero underlying integrand, the unconditional mean-squared quadrature error is asymptotic to \(B_\alpha\sigma\) as \(\sigma\downarrow0\), rather than the order \(\sigma^2\) obtained from simply averaging two independent noisy measurements.

## Assumptions and scope

Fix any \(\alpha>0\). Let \(X,Y\) be independent \(\operatorname{Uniform}[0,1]\) random variables. Let \(Z_1,Z_2\) be independent \(N(0,\sigma^2)\) errors with \(\sigma>0\), independent of the nodes. For \(x,y\in[0,1]\), set
\[
k_\alpha(x,y)=e^{-\alpha(x-y)^2},\qquad
m_\alpha(x)=\int_0^1 k_\alpha(x,t)\,dt,
\qquad m_\alpha'(x)=e^{-\alpha x^2}-e^{-\alpha(1-x)^2}.
\]
Write \(\rho=e^{-\alpha(X-Y)^2}\) and \(K=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\). For every \(\eta\ge0\), define the two kernel-quadrature weights, almost surely, by
\[
w^\eta=(K+\eta I_2)^{-1}\begin{pmatrix}m_\alpha(X)\\m_\alpha(Y)\end{pmatrix},
\qquad R_\eta=w^\eta_1 Z_1+w^\eta_2 Z_2.
\]
For any deterministic Lipschitz \(f:[0,1]\to\mathbb R\), the noisy estimate is \(\widehat I_\eta(f)=w^\eta_1[f(X)+Z_1]+w^\eta_2[f(Y)+Z_2]\) and the true integral is \(I(f)=\int_0^1 f(t)\,dt\). The asymptotic moment claim for the complete estimation error concerns \(\eta=0\) only. All results are for two independently drawn nodes and exact arithmetic.

## Proof

### Weight decomposition

Let \(u=(X+Y)/2\) and \(\delta=X-Y\). Their joint density equals one on \(0<u<1\) and \(|\delta|<2\min(u,1-u)\). Writing \(m=m_\alpha\), the symmetric and antisymmetric weights satisfy the exact identities
\[
s_\eta=w^\eta_1+w^\eta_2=\frac{m(X)+m(Y)}{1+\eta+\rho},
\qquad d_\eta=w^\eta_1-w^\eta_2=\frac{m(X)-m(Y)}{1+\eta-\rho}.
\]
Therefore \(w^\eta_1=(s_\eta+d_\eta)/2\), \(w^\eta_2=(s_\eta-d_\eta)/2\), and
\[
\|w^\eta\|_2^2=\tfrac12(s_\eta^2+d_\eta^2).
\]
Since \(m\) is smooth on \([0,1]\), uniformly in admissible \((u,\delta)\),
\[
m(u+\delta/2)-m(u-\delta/2)=m'(u)\delta+O(\delta^3),
\qquad 1-e^{-\alpha\delta^2}=\alpha\delta^2+O(\delta^4).
\]
In particular, as \(\delta\to0\), \(d_0=m'(u)/(\alpha\delta)+O(\delta)\), while \(s_0\) stays bounded. More strongly, the difference between \(R_0\) and
\[
R_*=\frac{m'(u)}{2\alpha\delta}(Z_1-Z_2)
\]
is uniformly bounded in absolute value by a fixed constant (depending on \(\alpha\)) times \(|Z_1|+|Z_2|\). Hence this remainder has Gaussian tails uniformly over the nodes, and its addition cannot change any \(t^{-1}\) tail coefficient.

### Exact two-sided collision tails

For \(u\in[0,1]\), put \(V(u)=m'(u)(Z_1-Z_2)/(2\alpha)\). Conditional on \(u,Z_1,Z_2\), the positive tail of \(R_*=V(u)/\delta\) contributes an interval of signed separations of length
\[
\min\left\{\frac{|V(u)|}{t},\,2\min(u,1-u)\right\}
\]
(the interval is on the side of zero with the sign of \(V\)). Multiplying by \(t\), integrating over \(u\), and applying dominated convergence using domination by \(|V(u)|\), yields
\[
\lim_{t\to\infty}t\Pr(R_*>t)=\int_0^1\mathbb E|V(u)|\,du
=\frac{\sigma}{\alpha\sqrt\pi}\int_0^1|m'(u)|\,du,
\]
because \(\mathbb E|Z_1-Z_2|=2\sigma/\sqrt\pi\). The negative tail has the same coefficient by symmetry. For an explicit evaluation, \(m'(u)>0\) on \((0,1/2)\) and \(m'(u)<0\) on \((1/2,1)\); integration gives
\[
\int_0^1|m'(u)|\,du
=\sqrt{\frac\pi\alpha}\left[2\operatorname{erf}(\sqrt\alpha/2)-\operatorname{erf}(\sqrt\alpha)\right].
\]
For \(0<p<1\), \(|R_0|\le C_\alpha(|Z_1|+|Z_2|)(1+|\delta|^{-1})\) and \(\Pr(|\delta|\in dr)=2(1-r)\,dr\) on \((0,1)\), so the absolute moment is finite. At \(p\ge1\) the strictly positive inverse-linear lower tail makes the moment infinite.

If \(f\) is Lipschitz with constant \(L\), the noiseless estimate has the exact decomposition
\[
Q_0(f)=w^0_1f(X)+w^0_2f(Y)
=\tfrac12s_0[f(X)+f(Y)]+\tfrac12d_0[f(X)-f(Y)].
\]
The first term is bounded. For the second, \(|m(X)-m(Y)|\le\|m'\|_\infty|\delta|\), \(|f(X)-f(Y)|\le L|\delta|\), and \(1-e^{-\alpha\delta^2}\ge(1-e^{-\alpha})\delta^2\) for \(|\delta|\le1\). Thus \(Q_0(f)-I(f)\) is uniformly bounded, and adding it to \(R_0\) does not change either sharp tail coefficient or the moment cutoff.

### Sharp nugget cost

For \(\eta\ge0\), \(s_\eta\) is uniformly bounded. Therefore its squared contribution vanishes after multiplying its expectation by \(\sqrt\eta\). For the antisymmetric term, substitute \(\delta=\sqrt{\eta/\alpha}\,z\), use the expansions above, and observe that for \(|\delta|\le1\),
\[
\eta+1-e^{-\alpha\delta^2}\ge\eta+(1-e^{-\alpha})\delta^2.
\]
This gives an integrable domination by a constant times \(z^2/(1+c_\alpha z^2)^2\) after the rescaling. The transformed integration domain tends to \(\{(u,z):0<u<1,\ z\in\mathbb R\}\), modulo a measure-zero boundary. Dominated convergence, the factor \(1/2\) in the weight-norm identity, and \(\int_{-\infty}^\infty z^2(1+z^2)^{-2}\,dz=\pi/2\) yield
\[
\lim_{\eta\downarrow0}\sqrt\eta\mathbb E\|w^\eta\|_2^2
=\frac\pi{4\alpha^{3/2}}\int_0^1(m'(u))^2\,du.
\]
The last integral is strictly positive, and can optionally be evaluated as
\[
\int_0^1(m_\alpha'(u))^2\,du
=\sqrt{\frac\pi{2\alpha}}\left[\operatorname{erf}(\sqrt{2\alpha})-2e^{-\alpha/2}\operatorname{erf}(\sqrt{\alpha/2})\right].
\]
Finally, conditional independence of the noise gives \(\mathbb E[R_\eta^2\mid X,Y]=\sigma^2\|w^\eta\|_2^2\). Setting \(\eta=\sigma^2\) and letting \(\sigma\downarrow0\) proves the mean-square asymptotic. For \(f=0\), this is also the exact total estimator mean-square error, with no noiseless integration error.

## Verification

The accompanying self-contained `verify.py` uses standard numerical quadrature, Gaussian normal tails and direct two-by-two matrix solves to check the weight decomposition, derivative norms, explicit constants and near-singular limiting behavior. It prints **PASS: 47 independent formula/numerical tests** using Python 3 with NumPy and SciPy. The universal tail, moment and nugget-limit statements are established by the analytic proof above; the finite numerical tests are diagnostics, not infinite-parameter certificates.

For \(\alpha=1\) and \(\sigma=1\), the one-sided tail constant is approximately \(0.198298962676\), and the nugget-amplification constant is approximately \(0.124378134669\). The verifier reports scaled nugget variances converging toward the latter as \(\eta\) shrinks and scaled positive tails converging toward the former as the threshold increases.

## Relationship to prior work

Briol et al. (2017) investigate random node distributions for kernel quadrature and convergence properties of noiseless integration. Karvonen, Kanagawa and Särkkä (2018) examine positivity and magnitudes of Bayesian quadrature weights, including kernel-conditioning concerns; Karvonen and Särkkä (2018) also analyze Gaussian kernel quadrature on structured Gauss-Hermite nodes. Cai, Lam and Scarlett (2022) study general noisy Gaussian-process/Bayesian quadrature error rates and kernel regularization. Hayakawa, Oberhauser and Lyons (2023) study random sampling-based kernel quadrature and Nyström approximations. The claim here concerns the specific two-node, random-collision, independent-observation-noise moment spectrum and exact ridge constant, not the broad fact that nearly coincident nodes ill-condition kernel Gram matrices. The inspected formulations do not directly give the displayed constants or the two-sided tail limit; additional specialized prior treatments may exist.

## Limitations

Two independent uniform nodes, the squared-exponential kernel on \([0,1]\), fixed positive bandwidth, independent Gaussian observational noise, and exact arithmetic are essential to the stated theorem. The noiseless boundedness statement assumes a fixed Lipschitz integrand, rather than arbitrary data that vary discontinuously with node location. The nugget-variance law is for the independent-noise contribution, not a general error bound for arbitrary nonzero integrands. It does not assert general-dimensional, multi-node, floating-point, or adaptively sampled analogues. Independent external mathematical validation has not been performed.

## References

- F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen, M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369v1 (June 11, 2017), https://arxiv.org/abs/1706.03369.
- T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss-Hermite nodes*, arXiv:1803.09532v1 (March 26, 2018), https://arxiv.org/abs/1803.09532.
- T. Karvonen, M. Kanagawa, S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, arXiv:1812.08509v1 (December 20, 2018), https://arxiv.org/abs/1812.08509.
- X. Cai, C. T. Lam, J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1 (February 22, 2022), https://arxiv.org/abs/2202.10615.
- S. Hayakawa, H. Oberhauser, T. Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, arXiv:2301.09517v1 (January 23, 2023), https://arxiv.org/abs/2301.09517.
