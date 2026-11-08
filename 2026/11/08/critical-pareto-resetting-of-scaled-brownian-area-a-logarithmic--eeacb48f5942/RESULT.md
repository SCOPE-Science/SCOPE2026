# Critical Pareto resetting of scaled Brownian area: a logarithmic law, one-stable fluctuations, and almost-sure intermittency

## Finding
For the absolute area \(A(t)=\int_0^t |X_s|\,ds\) of scaled Brownian motion under independent full resetting, consider the matched Pareto exponent \(\alpha=\rho=1+\beta/2\). With the unit conventions and parameters below, write \(c=4/((2+\beta)\sqrt\pi)\), \(\mu=\rho/(\rho-1)\), \(n_t=t/\mu\), and \(b(x)=\mathbb E[Y\mathbf{1}_{\{Y\le x\}}]\), where \(Y\) is the area of a completed reset excursion. Then, for every \(0<\beta<2\):

\[
\frac{A(t)}{t\log t}\xrightarrow[t\to\infty]{\mathbb P}\frac c\mu=\frac{4\beta}{(2+\beta)^2\sqrt\pi},\qquad
\frac{A(t)-n_t b(n_t)}{n_t}\Longrightarrow Z_c,
\]
where \(Z_c\) is the nondegenerate totally right-skewed one-stable distribution specified by
\[
\mathbb E e^{iuZ_c}=\exp\!\left\{c\int_0^\infty\frac{e^{iux}-1-iux\mathbf{1}_{\{x\le1\}}}{x^2}\,dx\right\}
=\exp\!\left\{c\left[-\frac\pi2|u|+iu(1-\gamma_E-\log|u|)\right]\right\},
\]
with the expression at \(u=0\) interpreted continuously. In contrast, for the same model,
\[
\limsup_{t\to\infty}\frac{A(t)}{t\log t}=+\infty\quad\text{almost surely}.
\]
The explicit finite-scale centering is
\[
b(x)=\mathbb E\!\left[\xi\log(x/\xi)\mathbf{1}_{\{\xi\le x\}}\right]
=c\log x-\mathbb E[\xi\log\xi]+o(1),
\]
where \(\xi\) is the unit-time unreset absolute area defined below. Thus convergence in probability at the logarithmic critical scaling does not strengthen to almost-sure convergence.

## Assumptions and scope
Fix \(0<\beta<2\). In each fresh excursion, \(X_s=\sqrt2\,B(s^\beta)\) for \(s\ge0\), with \(B\) a fresh standard Brownian motion. At the end of a reset interval the position and the local Brownian clock both restart, independently across cycles. The intervals \(\tau_i\) are independent of all Brownian motions, independent and identically distributed, with density \(\rho t^{-1-\rho}\mathbf{1}_{\{t\ge1\}}\) and \(\rho=1+\beta/2\). Let \(T_n=\sum_{i=1}^n\tau_i\), \(N(t)=\max\{n:T_n\le t\}\), \(\xi_i=\int_0^1|\sqrt2B_i(s^\beta)|\,ds\), and \(Y_i=\tau_i^\rho\xi_i\). The total area is \(A(t)=\sum_{i=1}^{N(t)}Y_i+R(t)\), where \(R(t)\) is the unfinished-excursion area. Every limit concerns real \(t\to\infty\), not a finite simulation. The time cutoff \(1\) and diffusivity parameter \(1\) are fixed normalizations; arbitrary fixed positive values can be reinstated by scaling.

## Proof
**1. Gaussian excursion amplitude.** Brownian scaling gives \(\int_0^\tau|\sqrt2 B(s^\beta)|ds\overset{d}{=}\tau^\rho\xi\). For \(\xi=\int_0^1 |\sqrt2 B(s^\beta)|ds\), Tonelli and the absolute Gaussian first moment yield
\[
\mathbb E\xi=\int_0^1\frac{2}{\sqrt\pi}s^{\beta/2}\,ds=\frac4{(2+\beta)\sqrt\pi}=c.
\]
By Cauchy--Schwarz, \(\xi\le (\int_0^1 2B(s^\beta)^2ds)^{1/2}\), so \(\mathbb E\xi^2<\infty\); therefore \(\mathbb E|\xi\log\xi|<\infty\).

**2. Exact borderline reward tail.** If \(U\) is uniform on \((0,1)\), then \(\tau^\rho\overset{d}{=}1/U\). Since \(\xi\) and \(\tau\) are independent, \(Y\overset{d}{=}\xi/U\); conditioning on \(\xi\) gives the *exact*, not merely asymptotic, formulas
\[
\mathbb P(Y>x)=\mathbb E\min\{1,\xi/x\},\qquad b(x)=\mathbb E[\xi\log(x/\xi)\mathbf{1}_{\{\xi\le x\}}].
\]
Dominated convergence gives \(x\mathbb P(Y>x)\to c\). For the centering, subtract \(c\log x-\mathbb E[\xi\log\xi]\) from the exact identity; the remainder is \(\mathbb E[\xi\log(\xi/x)\mathbf{1}_{\{\xi>x\}}]\to0\) by integrability and monotonic truncation. Thus \(b(x)=c\log x-\mathbb E[\xi\log\xi]+o(1)\).

**3. Stable domain of attraction.** Let \(S_n=\sum_{i=1}^nY_i\). The regular variation in step 2 implies vague convergence \(n\mathbb P(Y/n\in dx)\Rightarrow c x^{-2}\mathbf{1}_{\{x>0\}}dx\), with no negative jumps. The compensator for jumps \(x\le1\) is exactly \(b(n)\). The characteristic-function triangular-array argument (or the Lévy--Khintchine domain-of-attraction theorem at index one) gives
\[
(S_n-nb(n))/n\Longrightarrow Z_c,
\]
whose Lévy measure is \(cx^{-2}\mathbf{1}_{\{x>0\}}dx\). The exponent above results by integrating this Lévy measure with the stated truncation function. In particular \(S_n/(n\log n)\to c\) in probability. These conclusions are distributional limit theorems, not finite enumeration.

**4. Random renewal count is negligible at the stable scale.** Here \(\mu=\mathbb E\tau=\rho/(\rho-1)<\infty\). Pick \(p\in(1,\rho)\) and \(q\in(1/p,1)\). Since \(\mathbb E|\tau-\mu|^p<\infty\), the von Bahr--Esseen inequality yields \(T_n-\mu n=O_{\mathbb P}(n^{1/p})\). Renewal inversion hence gives \(|N(t)-n_t|=O_{\mathbb P}(n_t^{1/p})=o_{\mathbb P}(n_t^q)\). For a deterministic block of \(m=O(n^q)\) extra nonnegative rewards, truncate them at \(n\): by step 2,
\[
\mathbb P(\max_{j\le m}Y_j>n)=O(m/n),\qquad
\frac m n\mathbb E[Y\mathbf{1}_{\{Y\le n\}}]=O(n^{q-1}\log n)\to0.
\]
A union bound and Markov's inequality show that the reward mass in such a block is \(o_{\mathbb P}(n)\). Sandwich \(S_{N(t)}\) between \(S_{\lfloor n_t-n_t^q\rfloor}\) and \(S_{\lceil n_t+n_t^q\rceil}\), using the reward independence across cycles (not independence of \(N(t)\) from rewards). Therefore \(S_{N(t)}-S_{\lfloor n_t\rfloor}=o_{\mathbb P}(n_t)\).

**5. Incomplete excursion and the full limit.** The backward recurrence age \(B(t)=t-T_{N(t)}\) is tight as \(t\to\infty\), by the finite-mean nonarithmetic renewal-age theorem. Conditional on that age, a fresh Brownian path generates \(R(t)\overset{d}{=}B(t)^\rho\xi'\) with \(\xi'\) independent of the reset intervals. Hence \(R(t)=O_{\mathbb P}(1)\) and \(R(t)/n_t\to0\) in probability. Combining with steps 3--4, replacing \(\lfloor n_t\rfloor\) by \(n_t\) in the explicit centering (a difference \(O(\log n_t)\)), proves the asserted one-stable limit. Since \(b(n_t)\sim c\log t\), the logarithmic weak law follows.

**6. Almost-sure nonconvergence.** By the tail from step 2, for each integer \(m\ge1\),
\[
\sum_{j\ge3}\mathbb P(Y_j>m j\log j)=\infty.
\]
The cycle rewards are independent across \(j\), so the second Borel--Cantelli lemma makes these events occur infinitely often, simultaneously for every integer \(m\). On such reset completion epochs \(T_j\), the nonnegative total area obeys \(A(T_j)\ge Y_j\), while \(T_j/j\to\mu\) almost surely by the ordinary renewal strong law. Consequently the ratio \(A(T_j)/(T_j\log T_j)\) exceeds arbitrarily large constants along subsequences, proving the almost-sure infinite limsup. This does not contradict the weak law in step 5.

## Verification
The accompanying `verify.py` recomputes the exact Pareto-to-uniform transformation, first Gaussian-area coefficient, reward-tail and truncated-mean identities, and key finite-parameter comparisons using deterministic numerical integration and symbolic algebra. These checks support the algebra only. Regular-variation limits, renewal-age tightness, index-one stable convergence, and the almost-sure Borel--Cantelli conclusion are proved above, not inferred from simulations. Run with `python3 verify.py` (Python standard library).

## Relationship to prior work
Méndez and Cristín (arXiv:2610.19985v1, 14 October 2026) derive the renewal representation, scaled Brownian excursion area, finite-order moments, and strict-regime asymptotics in their Sections II--V. Their critical line \(\alpha=1+\beta/2\) separates a superlinear mean area regime and a linear mean area regime, but their asymptotic cases are stated with strict inequalities and they do not give a logarithmic weak law, a one-stable full-area fluctuation law, or the almost-sure limsup contrast. Méndez and Flaquer-Galmés (Phys. Rev. E 112, 044123, 2025) establish a broad renewal functional framework and lower moment regimes, not this exact critical-area classification. Classical renewal-reward and stable-law theory supplies general tools; no novelty is claimed for the general one-stable domain-of-attraction theorem or the Borel--Cantelli lemma themselves. The model-specific critical-scale coefficient, centering, and joint probabilistic/almost-sure classification are the subject here.

## Limitations
The result assumes completely independent Brownian restarts, Pareto waiting times with the exact matched exponent, and finite mean interarrival time; it does not cover nonrenewal resetting, partial resets, or arbitrary non-Pareto slowly varying reset tails. The nondegenerate stable fluctuation limit holds after the specified truncated-mean centering, not after subtracting a finite complete-cycle mean (which does not exist). The weak law does not imply self-averaging in a second-moment or almost-sure sense. General renewal-reward results may furnish a more abstract proof; external independent publication-priority assessment has not been performed.

## References
1. V. Méndez and J. Cristín, *Absolute area under a scaled Brownian motion with resetting*, arXiv:2610.19985v1 (first posted 14 October 2026), https://arxiv.org/abs/2610.19985 ; full text https://arxiv.org/html/2610.19985v1 .
2. V. Méndez and R. Flaquer-Galmés, *Statistical properties of stochastic functionals under general resetting*, Physical Review E **112**, 044123 (2025), https://doi.org/10.1103/pcm7-bw2y ; open text https://webs.uab.cat/vmendez/wp-content/uploads/sites/97/2025/10/133.pdf .
3. J. B. Levy and M. S. Taqqu, *Renewal reward processes with heavy-tailed interrenewal times and heavy-tailed rewards*, Bernoulli **6** (2000), 23--44; https://math.bu.edu/people/murad/abstracts/30/30.html (related general limit literature; full text not established here).
4. H. Horii, R. Lefevere, M. Itami and T. Nemoto, *Anomalous fluctuations of renewal-reward processes with heavy-tailed distributions*, arXiv:2203.08584 (2022), https://arxiv.org/abs/2203.08584 .
