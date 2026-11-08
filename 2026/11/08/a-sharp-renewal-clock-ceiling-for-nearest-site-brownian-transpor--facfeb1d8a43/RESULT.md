# A sharp renewal-clock ceiling for nearest-site Brownian transport

## Finding

Consider a one-dimensional Brownian particle of diffusivity \(D>0\) and a fixed infinite regular lattice of instantaneous resetting sites with spacing \(\ell>0\). At independent renewal epochs the particle is sent to its nearest lattice site, without altering the underlying Brownian diffusivity. Across **all iid positive renewal-interval distributions** with finite second moment, and allowing the mean interval to vary, the sharp effective diffusivity satisfies
\[
\frac{D_{\mathrm{eff}}}{D}\leq C_* = \frac{F(\theta_*)}{2\theta_*}=1.33247788734838\ldots,
\]
where
\[
F(\theta)=2\sum_{k=0}^{\infty}(2k+1)Q\!\left(\frac{k+1/2}{\sqrt{2\theta}}\right),\qquad Q(z)=\frac1{\sqrt{2\pi}}\int_z^{\infty}e^{-u^2/2}\,du,
\]
and \(\theta_*\) is the **unique** positive solution of \(\theta F'(\theta)=F(\theta)\). Numerically \(\theta_*=0.0918903456528753\ldots\). Equality holds if and only if every reset interval equals \(\ell^2\theta_*/D\) almost surely. In particular no randomization of independent renewal intervals can improve the universally optimal periodic protocol.

This ceiling strictly exceeds the entire Poisson-clock family in the nearest-site model: the Poisson effective diffusivity is always less than \(5D/4\), whereas the explicit deterministic clock with interval \(\ell^2/(10D)\) has diffusivity exceeding \(5D/4\). The motivating Poisson model has a reported optimal enhancement of approximately \(1.16923D\); the sharp renewal ceiling is approximately \(1.33248D\).

## Assumptions and scope

For every \(D,\ell>0\), let \(B\) be Brownian motion with \(\mathbb E[(B_t-B_s)^2]=2D|t-s|\). Let \(S_1,S_2,\dots\) be iid, strictly positive, independent of \(B\), with \(0<\mu=\mathbb ES_1<\infty\) and \(\mathbb ES_1^2<\infty\). At \(T_j=\sum_{i=1}^jS_i\), replace the particle's current position by the nearest point of \(\ell\mathbb Z\); ties have probability zero. Start at the site zero. Between renewals the particle follows independent Brownian increments. Define \(D_{\mathrm{eff}}=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\); this limit exists under the stated assumptions. The optimization is over the interval law and its mean, **not** over irregular site arrangements, adaptive reset clocks, drift, or finite-speed returns.

## Proof

**1. Exact renewal-reward diffusivity.** Conditional on a reset interval \(S=s\), the lattice-site increment is \(\ell K_s\), where \(K_s\) is the nearest integer to a centered Gaussian of variance \(2Ds/\ell^2\). Its conditional mean is zero and conditional variance is \(\ell^2F(Ds/\ell^2)\). For \(\theta>0\), the tail-sum identity for the integer square gives
\[
F(\theta)=2\sum_{k\ge0}(2k+1)\Pr\{N(0,2\theta)\ge k+1/2\}.
\]
Condition on the renewal intervals through observation time \(t\). The completed site jumps are centered and mutually orthogonal conditional on those intervals, and the residual Brownian increment is independent and centered conditional on the intervals. Therefore
\[
\operatorname{Var}(X_t)=\ell^2\mathbb E\!\sum_{j:T_j\le t}F(DS_j/\ell^2)+2D\mathbb E[t-T_{N(t)}].
\]
Renewal-reward theory implies that the first term divided by \(t\) converges to \(\ell^2\mathbb E[F(DS/\ell^2)]/\mu\). The second term divided by \(t\) vanishes under \(\mathbb ES^2<\infty\) (the renewal age has bounded expectation asymptotically). Hence
\[
\frac{D_{\mathrm{eff}}}{D}=\frac{\mathbb E F(\Theta)}{2\mathbb E\Theta},\qquad \Theta=DS/\ell^2.
\]
The ratio is a \(\Theta\)-size-biased average of \(R(\theta)=F(\theta)/(2\theta)\); thus it cannot exceed \(\sup_{\theta>0}R(\theta)\), and equality forces the interval law to be supported entirely on maximizers of \(R\).

**2. Strict rise up to a universal scale.** Put \(z_k=(k+1/2)/\sqrt{2\theta}\), \(\phi(z)=e^{-z^2/2}/\sqrt{2\pi}\), and \(H(\theta)=\theta F'(\theta)-F(\theta)\). Termwise differentiation, valid for fixed positive \(\theta\), gives
\[
H(\theta)=\sum_{k\ge0}(2k+1)[z_k\phi(z_k)-2Q(z_k)].
\]
For \(0<\theta\le1/16\), all \(z_k\ge\sqrt2\). The strict Gaussian Mills inequality \(Q(z)<\phi(z)/z\) implies each summand is positive. Therefore \(H(\theta)>0\) and \(R'(\theta)>0\) throughout this range.

**3. Strict concavity beyond that scale.** The periodic sawtooth Fourier series, applied to Gaussian rounding and differentiated for every \(\theta>0\), yields the exact representation
\[
F(\theta)=2\theta+\frac1{12}+\sum_{n=1}^{\infty}(-1)^n\left(8\theta+\frac1{\pi^2n^2}\right)e^{-4\pi^2n^2\theta},
\]
so
\[
F''(\theta)=16\pi^2\sum_{n\ge1}(-1)^nn^2(2un^2-3)e^{-un^2},\quad u=4\pi^2\theta.
\]
For \(\theta\ge1/16\), one has \(u\ge\pi^2/4>9/4\). The magnitudes \(a_n=n^2(2un^2-3)e^{-un^2}\) are positive and strictly decreasing, because
\[
\frac{a_{n+1}}{a_n}\le\frac{(1+1/n)^4e^{-u(2n+1)}}{1-3/(2un^2)}<48e^{-27/4}<1.
\]
The alternating series begins with a negative term, hence \(F''(\theta)<0\) for all \(\theta\ge1/16\). Thus \(H'(\theta)=\theta F''(\theta)<0\) there. The Fourier representation also shows \(H(\theta)\to-1/12\) as \(\theta\to\infty\), whereas the previous step shows \(H(1/16)>0\). There is exactly one \(\theta_*>1/16\) with \(H(\theta_*)=0\). Together with \(F(\theta)/\theta\to0\) as \(\theta\downarrow0\) and \(F(\theta)/(2\theta)\to1\) at infinity, this proves \(R\) has a unique global maximum. The size-bias equality condition now forces \(S=\ell^2\theta_*/D\) almost surely.

**4. A strict Poisson-versus-periodic separation.** For exponential intervals of rate \(r>0\), the displacement at a reset is Laplace-distributed. Writing \(\alpha=\ell\sqrt{r/(4D)}\), its rounded second moment gives the previously published formula
\[
\frac{D_{\mathrm{eff}}^{\mathrm{Pois}}}{D}=\alpha^2\frac{\cosh\alpha}{\sinh^2\alpha}.
\]
For every \(\alpha>0\), \(5\sinh^2\alpha-4\alpha^2\cosh\alpha>0\): the power-series coefficients through degree six yield \(\alpha^2[1-\alpha^2/3+\alpha^4/18]>0\), and all further coefficients are positive. Hence \(D_{\mathrm{eff}}^{\mathrm{Pois}}<5D/4\). Conversely at \(\theta=1/10\), keeping only the first nonnegative tail contribution gives \(R(1/10)\ge10Q(\sqrt5/2)>5/4\). The final strict inequality follows, for example, from the alternating error-function series at \(z=\sqrt{5/8}\):
\[
\operatorname{erf}(z)<\frac2{\sqrt\pi}\left(z-\frac{z^3}{3}+\frac{z^5}{10}\right)<\frac34.
\]
Consequently a periodic clock beats *every* Poisson clock on the same regular resetting lattice, and the unique all-renewal maximizer is the stated deterministic clock. \(\square\)

## Verification

The enclosed `check.py` evaluates \(F\) by both Gaussian tail sums and its independent Fourier representation, checks the derivative condition and strict sign over diagnostic grids, compares an integrated exponential-clock reward against the closed Poisson formula, and reproduces the numerical maximizing period and enhancement. These finite checks supplement but do not replace the analytical sign and uniqueness proofs. Executing `python check.py` with Python 3 and its standard library reproduces the diagnostic report.

## Relationship to prior work

Alston and Bertrand, *Boosting macroscopic diffusion with local resetting* (arXiv:2401.12772, first posted 2024-01-23), introduce nearest-site resetting and obtain a best regular-lattice **Poisson** diffusivity near \(1.169D\); their model assumes exponential reset intervals and optimizes reset rate and spatial site geometry. The theorem above replaces that timing assumption by any independent renewal law and proves a sharp, uniquely attained **all-clock** ceiling. The nearest-integer Gaussian moment formula is a standard rounded-data identity, related to the study of Gaussian rounding by Schneeweiss, Komlos and Ahmad (2006) and Tricker (1984); that identity itself is not claimed as new. The value lies in connecting renewal transport to a sharp global variational principle and proving the strict unique optimum, with an explicit Poisson separation. Neither resetting to a fixed origin nor optimizations of unrelated first-passage observables imply the result.

## Limitations

The optimality covers iid reset intervals that are independent of the Brownian trajectory, with finite second moment, a one-dimensional **regular** lattice, and instantaneous nearest-site projection. No claim is made about adaptive clocks, heavy-tailed clocks outside the stated moment condition, nonregular lattices, finite reset speeds, or a global optimum across different physical mechanisms. The numerical digits of \(\theta_*\) and \(C_*\) are evaluations of exact implicit definitions, not separate symbolic closed forms. The precise publication priority against unindexed rounding literature is not independently certified; a potentially relevant 1984 paper was not available in full text.

## References

- H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772 (2024-01-23), https://arxiv.org/abs/2401.12772.
- H. Schneeweiss, J. Komlos and A. S. Ahmad, *Symmetric and Asymmetric Rounding*, SFB 386 Paper 479 (2006), https://epub.ub.uni-muenchen.de/1847/1/paper_479.pdf.
- A. R. Tricker, *Effects of Rounding on the Moments of a Probability Distribution*, *The Statistician* **33** (1984), 381–390, https://doi.org/10.2307/2987741 (abstract reviewed; full text unavailable).
- A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Scaled Brownian motion with renewal resetting*, arXiv:1812.05667 (2018), https://arxiv.org/abs/1812.05667 (different fixed-origin reset mechanism).
