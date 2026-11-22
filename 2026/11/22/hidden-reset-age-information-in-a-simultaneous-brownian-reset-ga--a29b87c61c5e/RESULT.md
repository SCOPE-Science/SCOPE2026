# Hidden-reset-age information in a simultaneous Brownian-reset gas

## Finding

Let \(N\ge1\) independent one-dimensional Brownian coordinates be reset **together** to zero at the times of a rate-\(r\) Poisson process. At stationarity, let \(T\) be the elapsed time since the last reset, and observe a single simultaneous snapshot \(X=(X_1,\ldots,X_N)\). The mutual information \(I_N=I(T;X)\), in natural logarithmic units, is independent of the physical diffusion constant and resetting rate. It increases **strictly** with every added particle. Its exact finite-\(N\) expression and sharp first finite-size correction are

\[
I_N=-\int_{-\infty}^{\infty}g_{N/2}(v)\log g_{N/2}(v)\,dv-\big[\log\Gamma(N/2)-(N/2)\psi(N/2)+N/2\big],
\]
\[
g_k(v)=\frac{2}{\Gamma(k)}\exp\!\left(\frac{k+1}{2}v\right)K_{k-1}\!\left(2e^{v/2}\right),\qquad v\in\mathbb R,
\]
\[
I_1=\frac{1+\gamma_{\rm E}-\log\pi}{2},\qquad
I_N=\frac12\log N+1+\gamma_{\rm E}-\frac12\log(4\pi e)+\frac{2}{3N}+o(N^{-1}).
\]

The \(\tfrac12\log N\) leading order is an established general regular-parametric information law. The model-specific claim assessed here is the exact one-dimensional entropy representation, strict finite-population increase, and especially the explicit positive \(2/(3N)\) correction, rather than that leading order or the previously known Gaussian mixture itself.

## Assumptions and scope

Fix any integer \(N\ge1\), \(r>0\), and \(D>0\). Between resetting events, the \(N\) particles follow independent diffusion generators \(D\partial_{x_i}^2\), with all coordinates and noises restarted from zero at each common reset. Take the stationary distribution of the joint process. The age \(T\) has density \(r e^{-rt}\) for \(t>0\), and conditional on \(T=t\), the \(X_i\) are independent centered normals of variance \(2Dt\). The observer measures the full position vector exactly, without seeing the reset clock; no measurement noise, staggered clocks, nonzero reset sites, or memory across resets are included.

Let \(U=rT\), \(k=N/2\), and \(S=r\sum_{i=1}^N X_i^2/(4D)\). By Gaussian sampling, \(U\sim\operatorname{Exp}(1)\) and \(B\sim\operatorname{Gamma}(k,1)\) are independent with \(S=UB\). The statistic \(S\) is sufficient for \(U\), because the conditional Gaussian likelihood depends on \(X\) only through its squared radius and its angular distribution is independent of age. Hence \(I_N=I(U;S)\). All information quantities here are differential/discrete mutual information in nats, which remains invariant under the stated one-to-one rescalings.

## Proof

**1. Finite-population distribution and entropy.** The Mellin convolution of an exponential and a shape-\(k\) unit-rate Gamma variable gives, for \(s>0\),
\[
p_S(s)=\frac1{\Gamma(k)}\int_0^\infty u^{-k}e^{-u-s/u}s^{k-1}\,du
=\frac{2s^{(k-1)/2}}{\Gamma(k)}K_{k-1}(2\sqrt{s}).
\]
This is the standard Bessel-\(K\) product representation, not asserted to be new. On putting \(v=\log s\), its density is exactly \(g_k(v)=e^vp_S(e^v)\), as displayed above. Define \(W=\log U\), \(Z_k=\log B\). Because \(\log S=W+Z_k\) and \(Z_k\) is independent of \(W\),
\[
I_N=h(W+Z_k)-h(Z_k).
\]
The log-Gamma entropy follows directly from the Gamma density and expectations \(\mathbb E\log B=\psi(k)\), \(\mathbb EB=k\):
\[
h(Z_k)=\log\Gamma(k)-k\psi(k)+k.
\]
All entropies are finite: exponential and Gamma logarithms have all polynomial moments, and the density \(g_k\) has integrable exponentially decaying left and superexponentially decaying right entropy tails (the left tail may have a polynomial factor when \(k=1\)).

**2. Strict increase.** The conditional law of each additional coordinate given \(U\) is the nondegenerate normal \(N(0,2DU/r)\), with conditional independence across particles. For any existing snapshot, the posterior on \(U\) has positive density over \((0,\infty)\), so its mixture of normal laws for the next coordinate is not the same as every fixed-\(U\) Gaussian. Conditional independence cannot hold between the next coordinate and the positive posterior-variance \(U\). Thus the chain rule gives \(I_{N+1}-I_N=I(U;X_{N+1}\mid X_1,\ldots,X_N)>0\). This proves strictness for all \(N\), not just sampled dimensions.

**3. Exact one-coordinate benchmark.** For \(N=1\), integrating over reset ages produces the Laplace density \(p_{X_1}(x)=\tfrac12\sqrt{r/D}\,e^{-|x|\sqrt{r/D}}\). Thus \(h(X_1)=1+\log(2\sqrt{D/r})\). On the other hand \(h(X_1\mid T)=\tfrac12\log(4\pi eD/r)-\gamma_{\rm E}/2\), because \(\mathbb E\log U=-\gamma_{\rm E}\). Their difference gives the stated exact \(I_1\).

**4. First finite-size correction.** Center the log-Gamma variable by \(\widetilde Z_k=\log B-\psi(k)\), which does not change entropy. Its cumulants are polygamma functions: \(\mathbb E\widetilde Z_k=0\), \(\mathbb E\widetilde Z_k^2=\psi_1(k)=k^{-1}+O(k^{-2})\), and \(\mathbb E|\widetilde Z_k|^3=O(k^{-3/2})\). The density of \(W=\log U\) is \(f(w)=e^{w-e^w}\), with \(h(W)=1+\gamma_{\rm E}\) and finite Fisher translation information
\[
J(f)=\int_{\mathbb R}\frac{f'(w)^2}{f(w)}\,dw=\mathbb E(1-U)^2=1.
\]
The small-centered-noise entropy expansion, justified here by Taylor expansion of the smooth \(f\) on growing compact intervals and Gamma-log moment/tail bounds on their complements, gives
\[
h(W+\widetilde Z_k)=h(W)+\tfrac12\psi_1(k)J(f)+o(k^{-1})
=1+\gamma_{\rm E}+\frac1{2k}+o(k^{-1}).
\]
For an explicit check of the potentially delicate entropy term, writing \(p_k=f*\mathcal L(\widetilde Z_k)\) gives the **exact** cross-entropy identity
\[
h(p_k)-h(f)=\big(ke^{-\psi(k)}-1\big)-D_{\rm KL}(p_k\Vert f).
\]
Here is an explicit tail-controlled justification of that relative-entropy remainder. Fix \(0<\delta<\log2\) and split the centered log-Gamma perturbation into \(\lvert\widetilde Z_k\rvert\le\delta\) and its complement. Gamma Chernoff bounds make both the discarded mass and its \(\mathbb E[e^{\widetilde Z_k}-1-\widetilde Z_k]\)-contribution exponentially small in \(k\). By convexity of relative entropy, the discarded component contributes at most that exponentially small cross-entropy amount. For shifts \(z,z'\) in the retained interval, the exact likelihood overlap is
\[
\int_{\mathbb R}\frac{f(w-z)f(w-z')}{f(w)}\,dw=\frac{e^{-z-z'}}{e^{-z}+e^{-z'}-1}.
\]
The denominator stays positive because \(\delta<\log2\). This overlap is analytic near \((0,0)\), equals one if either shift vanishes, and its power expansion under two independent centered log-Gamma perturbations gives retained-mixture \(\chi^2=O(k^{-2})\): the potentially first-order mixed term contains the square of the truncated mean, which is exponentially small, while the first nonvanishing centered terms contain at least the product of two second moments. As \(D_{\rm KL}\le\log(1+\chi^2)\), the retained divergence is \(O(k^{-2})\). Therefore \(D_{\rm KL}(p_k\Vert f)=O(k^{-2})+O(e^{-c k})=o(k^{-1})\). Meanwhile \(ke^{-\psi(k)}-1=(2k)^{-1}+O(k^{-2})\). This independently identifies the coefficient and its domain of validity. Finally Stirling and digamma expansion give
\[
h(Z_k)=\frac12\log\left(\frac{2\pi e}{k}\right)+\frac1{6k}+O(k^{-2}).
\]
Subtracting and using \(k=N/2\) yields precisely \(I_N=\tfrac12\log N+1+\gamma_{\rm E}-\tfrac12\log(4\pi e)+2/(3N)+o(N^{-1})\).

## Verification

The accompanying standalone script `code/verify.py` integrates the exact Bessel-\(K\) entropy density, checks normalization and posterior normalization, tests strictly increasing information for \(1\le N\le24\), compares the exact one-particle value and several finite-population benchmarks, and tests the large-population expansion. A fresh replay completed 78 assertions. Representative information values in nats are \(I_1=0.216242889526066\), \(I_2=0.388074842246354\), \(I_{10}=1.019727194271036\), and \(I_{80}=2.010812672184483\). These finite tests corroborate the analytic proof; none establish the unbounded-\(N\) statements by enumeration. Run with Python 3 and SciPy; the command is `python code/verify.py`.

## Relationship to prior work

Masó-Puigdellosas, Campos and Méndez (2022) derive and analyze diffusion **conditioned backward reset ages**, including the scalar Brownian positional conditioning used as a conceptual antecedent here [1]. Biroli, Larralde, Majumdar and Schehr (2022; published 2023) derive exactly the simultaneous-reset many-body stationary Gaussian mixture (their Eq. 4), its Bessel-\(K\) position law, and squared-position correlations [2]. Our Gaussian mixture, common reset clock, and product distribution are consequences of these established premises; the main and supplementary analysis of [2] addresses density, extremal statistics, spacings and counting rather than the information-theoretic correction computed here. Clarke and Barron's general Bayesian information asymptotics [3] cover the leading \(\tfrac12\log N\) mechanism, so leading logarithmic growth is not claimed as a novelty. Related studies of hidden common environments can also produce logarithmically growing mutual information but do not imply this exponential-age-specific positive \(2/(3N)\) coefficient without further analysis. The novelty assessment is conditional on these comparisons and is not a guarantee of publication priority.

## Limitations

The result requires a common exponential resetting clock and an exact simultaneous snapshot of conditionally Gaussian freely diffusing particles. It is not a finite-sample estimator-risk or experimental identifiability guarantee under noise. The displayed remainder is \(o(N^{-1})\), not a claimed uniform bound for moderate \(N\). The cited general asymptotic theorem and the earlier many-body mixture imply important parts of the statement; only the genuinely additional model-specific information identity, monotonicity and first finite-size correction are being assessed. Broader hidden-variable asymptotic literature could contain an equivalent coefficient and needs independent priority review. Independent scientific validation has not been performed.

## References

[1] A. Masó-Puigdellosas, D. Campos and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613 (first posted 2022-05-03), https://arxiv.org/abs/2205.01613.

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first posted 2022-11-01), https://arxiv.org/abs/2211.00563; Phys. Rev. Lett. 130, 207101 (2023).

[3] B. S. Clarke and A. R. Barron, *Information-theoretic asymptotics of Bayes methods*, IEEE Transactions on Information Theory 36, 453–471 (1990), https://doi.org/10.1109/18.54897.
