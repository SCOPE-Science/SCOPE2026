# A square-root sample-size transition and an infinite cusp ladder for a fitted-Poisson empirical weight test

## Finding

The fitted-Poisson-weight, order-one empirical weight-function statistic of Kirui, Bothma, Smuts, Steyn and Visagie is exactly the unhalved total-variation distance between empirical and fitted probability mass functions. For independent Poisson data with an intensity that changes with sample size, it has a sharp transition when the expected number of occupied count cells is of the same order as the sample size.

Let \(n\to\infty\), let \(\lambda_n\to\infty\), and let \(X_{n,1},\ldots,X_{n,n}\) be independent \(\operatorname{Pois}(\lambda_n)\) variables. Set
\[
\widehat p_n(k)=\frac1n\sum_{i=1}^n\mathbf1_{\{X_{n,i}=k\}},\qquad
\widehat\lambda_n=\frac1n\sum_{i=1}^nX_{n,i},\qquad
q_\theta(k)=e^{-\theta}\frac{\theta^k}{k!}.
\]
The source statistic is
\[
D_n=\sum_{k=0}^{\infty}q_{\widehat\lambda_n}(k)
\left|\frac{\widehat p_n(k)}{q_{\widehat\lambda_n}(k)}-1\right|
=\sum_{k=0}^{\infty}|\widehat p_n(k)-q_{\widehat\lambda_n}(k)|.
\]
The formula at \(\widehat\lambda_n=0\) is understood by the continuous extension of the final expression; this event has asymptotically negligible probability.

**Theorem.** If \(\lambda_n/n^2\to\kappa\in[0,\infty]\), then \(D_n\to\mathcal D(\kappa)\) in probability, where \(\mathcal D(0)=0\), \(\mathcal D(\infty)=2\), and for \(0<\kappa<\infty\),
\[
\mathcal D(\kappa)=\int_{\mathbb R}\mathbb E|K_y-f_\kappa(y)|\,dy
=2\int_{\mathbb R}f_\kappa(y)\,
\Pr\{\operatorname{Pois}(f_\kappa(y))=\lfloor f_\kappa(y)\rfloor\}\,dy,
\]
\[
f_\kappa(y)=\frac{e^{-y^2/(2\kappa)}}{\sqrt{2\pi\kappa}},\qquad
K_y\sim\operatorname{Pois}(f_\kappa(y)).
\]
(The integral uses marginal laws only; no joint construction of the \(K_y\) is needed.) The function \(\mathcal D\) is continuous and strictly increasing from zero to two.

More sharply, \(\mathcal D\) is continuously differentiable on \((0,\infty)\), is real-analytic away from the points
\[
\kappa_j=\frac1{2\pi j^2}\quad(j=1,2,\ldots),
\]
and is **not twice differentiable** at any \(\kappa_j\). At each such point there is a real-analytic local function \(H_j\) for which
\[
\mathcal D(\kappa)=H_j(\kappa)+c_j(\kappa_j-\kappa)_+^{3/2}
+o(|\kappa-\kappa_j|^{3/2}),
\qquad c_j=\frac4{3\sqrt{2\pi}}\,
\frac{e^{-j}j^j}{j!}\,\kappa_j^{-3/2}>0.
\]
For example, \(\mathcal D(0.2)=1.099789562606\ldots\), while the first nonsmooth point occurs at \(\kappa_1=0.159154943091895\ldots\) with \(\mathcal D(\kappa_1)=1.027858248254\ldots\).

## Assumptions and scope

The sample size is an integer \(n\ge1\); \(\lambda_n>0\) is deterministic and tends to infinity. The sample within each row is iid Poisson with common mean \(\lambda_n\), independent across indices within that row. No coupling across rows is needed. The limiting statement concerns the **unscaled fitted-Poisson-weight \(L_1\)** statistic and its null distribution, not the empirical-weight or Laplace-weight variants, and does not assert a bootstrap rejection probability. The distance \(D_n\) is the full \(\ell_1\) norm, **twice** the probabilistic total-variation distance.

## Proof

**1. Removing mean estimation.** Define \(D_n^0=\sum_{k\ge0}|\widehat p_n(k)-q_{\lambda_n}(k)|\). By the reverse triangle inequality, \(|D_n-D_n^0|\le\sum_k|q_{\widehat\lambda_n}(k)-q_{\lambda_n}(k)|\). The Poisson Hellinger affinity is exactly
\[
\sum_{k\ge0}\sqrt{q_s(k)q_t(k)}=\exp\{-\tfrac12(\sqrt s-\sqrt t)^2\}.
\]
Consequently \(\|q_s-q_t\|_1\le2|\sqrt s-\sqrt t|\). Since \((\sqrt{\widehat\lambda_n}-\sqrt{\lambda_n})^2\le(\widehat\lambda_n-\lambda_n)^2/\lambda_n\), and \(\operatorname{Var}(\widehat\lambda_n)=\lambda_n/n\), Cauchy–Schwarz gives \(\mathbb E|D_n-D_n^0|\le2/\sqrt n\). The fitted parameter therefore does not affect any limit below.

**2. Exact finite-sample mean and concentration.** For \(B\sim\operatorname{Bin}(n,p)\) and \(m=\lfloor np\rfloor\), the binomial splitting identity yields
\[
\mathbb E|B-np|=2np(1-p)\Pr\{\operatorname{Bin}(n-1,p)=m\}.
\]
Indeed \(\mathbb E(B-np)=0\), and the positive-part expectation equals \(np\big(\Pr\{\operatorname{Bin}(n-1,p)\ge m\}-\Pr\{\operatorname{Bin}(n,p)\ge m+1\}\big)\), which is \(np(1-p)\Pr\{\operatorname{Bin}(n-1,p)=m\}\). Applying this identity cellwise,
\[
\mathbb ED_n^0=2\sum_{k\ge0}q_{\lambda_n}(k)(1-q_{\lambda_n}(k))
\Pr\{\operatorname{Bin}(n-1,q_{\lambda_n}(k))=\lfloor nq_{\lambda_n}(k)\rfloor\}.
\]
Replacing a single observation changes \(D_n^0\) by at most \(2/n\). The Efron–Stein inequality gives \(\operatorname{Var}(D_n^0)\le2/n\) for every \(n\) and \(\lambda_n\). Hence it suffices to identify the deterministic mean limit.

**3. Critical regime.** Suppose \(\lambda_n/n^2\to\kappa\in(0,\infty)\). For \(y_{n,k}=(k-\lambda_n)/n\), the Poisson local central limit theorem gives, uniformly over \(|y_{n,k}|\le M\) for each fixed \(M\),
\[
nq_{\lambda_n}(k)=f_\kappa(y_{n,k})+o(1).
\]
The binomial absolute-deviation expectation is continuous under \(\operatorname{Bin}(n,p_n)\Rightarrow\operatorname{Pois}(t)\) when \(np_n\to t\) and the means are uniformly bounded; uniform integrability follows from bounded second moments. Therefore the central part of \(\mathbb ED_n^0=(1/n)\sum_k\mathbb E|\operatorname{Bin}(n,q_{\lambda_n}(k))-nq_{\lambda_n}(k)|\) is a Riemann sum tending to \(\int_{-M}^M\mathbb E|K_y-f_\kappa(y)|\,dy\). The omitted tails contribute at most \(2\Pr\{|\operatorname{Pois}(\lambda_n)-\lambda_n|>Mn\}\), and this is uniformly small as \(M\to\infty\) by Chebyshev and \(\lambda_n/n^2\to\kappa\). This proves the integral limit. For \(K\sim\operatorname{Pois}(t)\), the same positive-part calculation gives \(\mathbb E|K-t|=2t\Pr\{K=\lfloor t\rfloor\}\), including at integer \(t\).

**4. Outer regimes.** If \(\lambda_n/n^2\to0\), restrict to the central window \(|k-\lambda_n|\le L\sqrt{\lambda_n}\), which contains at most \(2L\sqrt{\lambda_n}+2\) cells. Cauchy–Schwarz bounds the expected \(\ell_1\) error in this window by the square root of the number of cells divided by \(n\); the expected error outside is at most twice its Poisson mass, at most \(2/L^2\). For fixed \(L\), the central bound vanishes, then \(L\to\infty\) yields \(\mathbb ED_n^0\to0\). If \(\lambda_n/n^2\to\infty\), write \(D_n^0=2(1-\sum_k\min(\widehat p_n(k),q_{\lambda_n}(k)))\). Since the overlap is at most \(\sum_{i=1}^nq_{\lambda_n}(X_{n,i})\), its mean is at most \(n\max_kq_{\lambda_n}(k)=O(n/\sqrt{\lambda_n})\to0\). Together with concentration, this proves both endpoints.

**5. Strict increase and the cusp ladder.** Put \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and \(a(t)=\Pr\{\operatorname{Pois}(t)=\lfloor t\rfloor\}\), with the continuous value at integer \(t\). The critical integral becomes
\[
\mathcal D(\kappa)=2\int_{\mathbb R}\varphi(z)a(\varphi(z)/\sqrt\kappa)\,dz.
\]
On \(j<t<j+1\), \(a(t)=e^{-t}t^j/j!\), with derivative \(a'(t)=a(t)(j/t-1)<0\); at \(t=j\), the adjacent formulas agree because the two Poisson modes tie. Thus \(a\) is continuous and strictly decreasing, so \(\mathcal D\) is continuous and strictly increasing with \(\kappa\). As \(\kappa\downarrow0\), \(a(\varphi(z)/\sqrt\kappa)\to0\) for every finite \(z\), by the Poisson mode bound; as \(\kappa\to\infty\), it tends to one. Dominated convergence gives the stated endpoints.

At each positive integer \(j\), the one-sided derivatives of \(a\) have a strictly positive jump \(a(j)/j\): the derivative below \(j\) is \(-a(j)/j\), and the derivative above is zero. At \(\kappa_j=(2\pi j^2)^{-1}\) the maximum of \(\varphi(z)/\sqrt\kappa\), attained only at \(z=0\), crosses the integer \(j\). The crossings of smaller integers occur at nonzero \(z\) and are transverse, so their integrated contributions have a real-analytic local continuation; denote the resulting analytic background by \(H_j\). Writing \(\delta=\kappa_j-\kappa>0\), in the newly activated central window
\[
|z|<\sqrt{\delta/\kappa_j}+O(\delta^{3/2}),\qquad
\frac{\varphi(z)}{\sqrt\kappa}-j
=\frac j2\left(\frac\delta{\kappa_j}-z^2\right)+O(\delta^2+z^4),
\]
the difference between the high- and low-modal branches is \((a(j)/j)(\varphi(z)/\sqrt\kappa-j)+O((\varphi(z)/\sqrt\kappa-j)^2)\). Integrating it against \(2\varphi(z)\) gives exactly
\[
\frac{4\varphi(0)a(j)}{3\kappa_j^{3/2}}\delta^{3/2}+o(\delta^{3/2}),
\]
which is \(c_j\delta^{3/2}\). The positive coefficient forces failure of twice differentiability; the exponent \(3/2\) gives continuity of the first derivative. Away from the locally finite set of modal-crossing points the piecewise analytic integrals over moving transverse boundaries are analytic. This finishes the proof.

## Verification

The supplementary standalone Python checker `check.py` requires Python 3, NumPy, SciPy and prints 126 successful checks on execution. It checks an independently enumerated finite binomial absolute-deviation identity for 63 parameter pairs; the exact Poisson identity for 13 intensities; 17 strict profile increments; 20 profile boundary checks; seven first-cusp branch/coefficient checks; and six central-truncation approximations of finite-sample expected distances. It is run using `python check.py`. Its numerical integrations and finite parameter tests corroborate but do not replace the analytic proof of the full continuum theorem and infinitely many cusps.

## Relationship to prior work

Kirui et al. (2024 preprint; 2025 journal publication) introduce and compute the fitted-Poisson-weight \(L_1\) statistic, and Kirui's 2023 thesis contains the same definition and a discussion of Poisson modes. That work covers fixed-parameter simulations and null calibration, not the increasing-mean \(\lambda_n\asymp n^2\) regime, its exact Gaussian-occupancy curve, or the integer-modal cusp ladder. The Poisson mode formula itself is classical and is not claimed as new.

Berend and Kontorovich (2012) provide general empirical-distribution \(\ell_1\) concentration bounds. Their concentration principle is acknowledged here; their fixed-law bounds alone do not state this Poisson triangular-array transition or the nonanalytic critical curve. Barbour (2009) develops general occupancy-count approximations; occupancy Poissonization is background, but that article studies occupied-box-count distributions rather than the exact modal-mean integral or its cusp ladder. Standard Poisson local limits and binomial-to-Poisson approximation are also background. Earlier work on the same weighted test in a **vanishing** Poisson intensity concerns a separate, non-implicative regime.

## Limitations

This theorem treats only the original fitted-Poisson-weight \(L_1\) statistic and an exactly specified growing-mean Poisson null. The outer-regime limits zero and two do not by themselves specify the behavior of bootstrap critical values or asymptotic test size/power. The singularity theorem concerns the deterministic critical curve and does not assert singular sample-path fluctuations. The underlying occupancy and Poisson-mode principles are classical; although a literature comparison identified no direct statement of the combined result, a general result outside the inspected sources might yield a related corollary. No independent mathematical audit is claimed.

## References

1. W. Kirui, E. Bothma, M. Smuts, A. Steyn, and I. J. H. Visagie, *On new tests for the Poisson distribution based on empirical weight functions*, first public arXiv version 2024-02-20, arXiv:2402.12866, https://arxiv.org/abs/2402.12866; *South African Statistical Journal* 59 (2025), 21–36, doi:10.37920/sasj.2025.59.1.2.
2. W. C. Kirui, *On a new class of tests for the Poisson distribution based on empirical weight functions*, North-West University master's thesis (graduation May 2023), https://repository.nwu.ac.za/bitstreams/6bc2adcb-3dbb-4312-b440-4d92cc48d5f6/download, Chapter 3, pp. 16–23, and Chapter 5, pp. 30–31. Public repository deposit date not established here.
3. D. Berend and A. Kontorovich, *On the Convergence of the Empirical Distribution*, arXiv:1205.6711 (2012), https://arxiv.org/abs/1205.6711.
4. A. D. Barbour, *Univariate approximations in the infinite occupancy scheme*, arXiv:0902.0879 (2009), https://arxiv.org/abs/0902.0879.
