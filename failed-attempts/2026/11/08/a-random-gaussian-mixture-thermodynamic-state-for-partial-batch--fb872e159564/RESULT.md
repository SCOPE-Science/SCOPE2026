# A random Gaussian-mixture thermodynamic state for partial-batch Brownian resetting

## Finding

Consider the one-dimensional, noninteracting Brownian gas under *uniform fixed-size batch resetting*, defined below. For any sequence of populations and batch sizes with
\[
N\longrightarrow\infty,\qquad \frac{m_N}{N}\longrightarrow p\in(0,1),
\]
the stationary empirical position measure has a non-deterministic thermodynamic limit. Let \(E_0,E_1,\ldots\) be independent exponential random variables of rate \(r\), set \(T_j=\sum_{h=0}^{j}E_h\), and write \(q=1-p\). Then the limit is the random Gaussian mixture
\[
\boxed{\displaystyle \nu=\sum_{j=0}^{\infty}p q^j\,\mathcal N(0,2DT_j).}
\]
In a coupling using the same backward global resetting clock, the empirical measures converge weakly *in probability* to \(\nu\). The limit has the distributional Gaussian-smoothing identity
\[
\nu\ \stackrel{\rm law}{=}\ \mathcal N(0,2DE_0)*\bigl[p\delta_0+q\nu'\bigr],
\]
where \(\nu'\) is an independent copy of \(\nu\), independent of \(E_0\).

The global mean-square displacement \(Q_N=N^{-1}\sum_{i=1}^N X_i^2\) converges in probability (under that coupling), with convergence of the first two moments, to the *non-self-averaging* random variable
\[
\boxed{\displaystyle Q=\int x^2\,\nu(dx)=2D\sum_{j=0}^{\infty}q^jE_j.}
\]
Its entire Laplace transform and every cumulant are explicit:
\[
\boxed{\displaystyle
\mathbb E[e^{-sQ}]=\prod_{j=0}^{\infty}\left(1+\frac{2Ds}{r}q^j\right)^{-1},\quad s\ge0,\qquad
\kappa_n(Q)=\frac{(n-1)!(2D/r)^n}{1-q^n},\quad n\ge1.}
\]
In particular,
\[
\mathbb E Q=\frac{2D}{rp},\qquad
\operatorname{Var}Q=\frac{4D^2}{r^2p(2-p)},\qquad
\frac{\operatorname{Var}Q}{(\mathbb E Q)^2}=\frac{p}{2-p}>0.
\]
The upper tail has the *sharp prefactor*, not just a logarithmic rate:
\[
\boxed{\displaystyle
\Pr(Q>x)\sim \frac{\exp[-rx/(2D)]}{\prod_{j=1}^{\infty}(1-q^j)}\quad(x\to\infty).}
\]
The product defining the prefactor is finite and strictly greater than one for \(0<p<1\). The completely synchronous endpoint \(p=1\) reduces to the previously known one-common-age Gaussian gas; its collective energy is simply exponential of mean \(2D/r\). No claim of novelty is made for that endpoint, the one-point marginal, or the previously known two-point covariance.

## Assumptions and scope

Fix \(D>0\) and \(r>0\). For each integer \(N\ge2\), the \(N\) labeled particles diffuse independently with generator \(D\partial_{xx}\), between global events from a single Poisson process of rate \(r\). At each event a fresh uniformly sampled subset of exactly \(m_N\in\{1,\ldots,N\}\) labels is moved instantaneously to zero; all other positions are left unchanged. Subsets at different events and Brownian noises are independent. Stationarity is defined using a two-sided Poisson process and the last reset of each particle in the infinite past. Such a last reset exists almost surely, because an individual particle's reset points form a rate-\(rm_N/N\) thinned Poisson process.

The new thermodynamic result concerns **fixed positive fractional batch size** \(m_N/N\to p\in(0,1)\) at fixed \(r,D\). It does not assert the same limit for a fixed integer batch size as \(N\to\infty\), for interacting Brownian particles, or for non-Poissonian global event intervals. Random-measure convergence means convergence in probability against each bounded continuous test function, under the explicit shared-clock coupling; the corresponding weak law on probability measures follows. Energies are unbounded test functions and are handled separately.

## Proof

**1. Stationary realization and backward-clock ages.** Read the global Poisson events backward from observation time zero. The interval from zero to the most recent event is \(E_0\), the gap to the next older event is \(E_1\), and so on. By stationary Poisson independent increments these gaps are independent \(\operatorname{Exp}(r)\) variables. If label \(i\) was most recently reset at backward event index \(J_i=j\), its current position is conditionally centered Gaussian with variance \(2DT_j\). Conditional on all event times and all reset subsets, the positions are independent, because the driving Brownian noises are independent.

**2. Concentration of the age-class fractions.** Write \(p_N=m_N/N\), \(q_N=1-p_N\), and \(F_{N,j}=N^{-1}\#\{i:J_i=j\}\). A fixed label belongs to the subset at an event with probability \(p_N\), so
\[
\mathbb E F_{N,j}=p_Nq_N^j.
\]
For two distinct labels, the probability that both are selected at a given event is
\(c_N=m_N(m_N-1)/[N(N-1)]\), and the probability that both are not selected is
\(b_N=(N-m_N)(N-m_N-1)/[N(N-1)]\). Therefore
\[
\mathbb E\!\left[\mathbf1_{\{J_i=j\}}\mathbf1_{\{J_k=j\}}\right]=c_N b_N^j
\qquad (i\ne k).
\]
For every fixed \(j\), as \(N\to\infty\), these probabilities tend respectively to \(p q^j\) and \(p^2q^{2j}\), because \(c_N\to p^2\), \(b_N\to q^2\). The exact variance formula for \(F_{N,j}\) then gives \(F_{N,j}\to p q^j\) in \(L^2\). Moreover the expected fraction of labels with \(J_i>J\) is \(q_N^{J+1}\), uniformly small for large \(J\) and all sufficiently large \(N\).

**3. Random empirical-measure limit.** Fix a bounded continuous test function \(f\), and put
\(h_f(t)=\int f(x)\,\mathcal N(0,2Dt)(dx)\). Given the reset times and subsets, the mean of \(N^{-1}\sum_i f(X_i)\) equals \(\sum_{j\ge0}F_{N,j}h_f(T_j)\), and its conditional variance is at most \(\|f\|_\infty^2/N\). The finite-\(j\) convergence in step 2 and the tail-mass bound prove convergence in probability to \(\sum_{j\ge0}pq^jh_f(T_j)\), conditionally on the shared Poisson times. Uniform boundedness of the expected empirical squared displacement gives tightness in probability of the empirical measures; a countable convergence-determining family of bounded continuous tests upgrades the preceding convergence to weak convergence in probability. This establishes the random Gaussian-mixture limit and the convolution identity, the latter by separating the most recent gap \(E_0\) from all older independent gaps.

**4. Unbounded energy and its exact series.** Individual reset times form a thinned rate-\(rp_N\) Poisson process. Thus the single-particle age is \(\operatorname{Exp}(rp_N)\), and conditional Gaussian moments yield
\[
\mathbb E X_i^4=\frac{24D^2}{r^2p_N^2},\qquad
\mathbb E X_i^8=\frac{40320D^4}{r^4p_N^4}.
\]
Since \(p_N\to p>0\), these moments are uniformly bounded for all sufficiently large \(N\). Truncating the test function \(x^2\) and using the fourth-moment bound extends step 3 to \(Q_N\) in probability and in first moment. Jensen's inequality and the eighth-moment bound make \(Q_N^2\) uniformly integrable, giving convergence of second moments. Tonelli's theorem gives
\[
\int x^2\nu(dx)=2D\sum_{j\ge0}pq^j\sum_{h=0}^jE_h
=2D\sum_{h\ge0}\left(\sum_{j\ge h}pq^j\right)E_h
=2D\sum_{h\ge0}q^hE_h.
\]
The sum is finite almost surely, because its expectation is finite.

**5. Transform, cumulants, and sharp tail.** Independence of the exponential gaps yields the product Laplace transform. The cumulant formula follows by differentiating the convergent logarithmic product at zero (equivalently by adding independent exponential cumulants); absolute convergence follows from \(q<1\). The stated first two moments and nonzero coefficient of variation follow by substituting \(n=1,2\).

For the tail, write \(Q=(2D/r)(Z_0+W)\), where the \(Z_j=rE_j\) are independent unit exponentials and \(W=\sum_{j\ge1}q^jZ_j\). For every \(1<\lambda<q^{-1}\), \(\mathbb E e^{\lambda W}<\infty\) by convergence of \(\prod_{j\ge1}(1-\lambda q^j)^{-1}\). With \(t=rx/(2D)\), conditioning on \(W\) gives exactly
\[
e^t\Pr(Z_0+W>t)=\mathbb E[e^W\mathbf1_{\{W\le t\}}]+e^t\Pr(W>t).
\]
The first term increases to \(\mathbb E e^W=\prod_{j\ge1}(1-q^j)^{-1}\); the second tends to zero by the exponential moment with parameter \(\lambda>1\). This proves the sharp tail. For \(p=1\), the empty-product convention gives prefactor one.

## Verification

An executable standard-library checker is supplied in `CHECK.py`. It validates exact finite-population moment-generator balances, the two-point Fourier marginal against the published formula, positive fluctuations, the cumulant identities, deterministic-seed conditional-clock realizations, and convergence of the sharp tail product. Its completed execution reported **7,499 passing checks**. These finite checks corroborate algebra and normalization; they are not used as proofs of the infinite-size or infinite-tail assertions.

For an additional independent finite-size consistency test, let \(a_{2,N}=1-(N-m_N)(N-m_N-1)/[N(N-1)]\). Direct application of the generator gives
\[
\mathbb E X_i^2=\frac{2D}{rp_N},\quad
\mathbb E X_i^4=\frac{24D^2}{r^2p_N^2},\quad
\mathbb E[X_i^2X_j^2]=\frac{8D^2}{r^2p_N a_{2,N}}\quad(i\ne j).
\]
Consequently \(\lim_{N\to\infty}\operatorname{Var}Q_N=4D^2/[r^2p(2-p)]\), exactly matching the variance of the derived series. The source's pair covariance already contains this variance information; that matching variance is a consistency check, not the claimed novelty.

## Relationship to prior work

De Mauro, Majumdar, and Schehr, arXiv:2601.20077 (first submitted January 27, 2026), introduced the fixed-size batch-reset model, its exact recursive stationary Fourier marginals, the one- and two-point correlations, and their large-population scaling. Its supplemental Sections S6 and S8–S10 calculate pair fluctuations, connected density correlations, spectral form factors, and higher-dimensional extensions. Those established results imply the finite-size second-moment consistency formula above. The present result concerns instead the **full random weak limit of the empirical measure** at positive fractional batch size, together with the **complete limiting collective-energy law and its sharp right-tail prefactor**; these are not the pair covariance, normalized correlation coefficient, or averaged spectral form factor.

Biroli, Larralde, Majumdar, and Schehr, arXiv:2211.00563, treated simultaneous resetting of *all* labels, corresponding to the already-known endpoint \(p=1\). De Mauro, Biroli, Majumdar, and Schehr, arXiv:2509.06658, extended simultaneous resetting to general renewal intervals, again resetting all particles at every event. Their conditional-independent structure therefore has a single common reset age rather than the geometric hierarchy of ages for \(0<p<1\). Another calculation of multi-particle excursion rates under the same partial-batch clock concerns a fixed number of tagged positions and not the empirical-measure thermodynamic limit. The geometric exponential series is a standard perpetuity type; novelty is claimed only for the exact physical realization and the resulting collective distribution, not for general identities about weighted sums of exponentials.

## Limitations

The limit takes population size to infinity at a fixed nonzero batch fraction. Sending the fraction to zero simultaneously with population size can produce another scaling regime, not resolved here. The Gaussian conditional law assumes free diffusion, instantaneous zero resets, independent noise and Poisson global events. The random empirical measure is not a finite-population exact CIID representation. No claims are made about relaxation rates, dynamic covariance, interacting systems, or non-Poissonian partial batches. An unindexed equivalent large-population construction, or an implicit large-population extraction from the published full marginal recursion, remains a possible priority risk pending independent literature review.

## References

1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077, version 1 publicly submitted January 27, 2026; revised 2026 version with supplement, https://arxiv.org/abs/2601.20077 .
2. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, https://arxiv.org/abs/2211.00563 .
3. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, https://arxiv.org/abs/2509.06658 .
4. G. de Mauro, S. N. Majumdar, and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634, https://arxiv.org/abs/2606.31634 (only its accessible abstract was compared).
