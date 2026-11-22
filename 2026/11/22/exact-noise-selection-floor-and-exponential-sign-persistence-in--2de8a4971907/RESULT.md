# Exact noise-selection floor and exponential sign persistence in quantile-averaged scalar Kaczmarz

## Finding
For a perfectly consistent scalar system with redundant identical rows, fresh symmetric measurement noise, and a full-screened quantile update, the treatment of selected observations changes the error by an **exact** multiplicative factor. Reusing the screening observations leaves a nonvanishing mean-square floor at every fixed quantile fraction below one, even when the averaging batch grows linearly with the number of rows. Independent re-querying of those same accepted row labels drives the squared error to zero. A related cached all-row update has a two-state sign process with an exactly known, exponentially long sign-persistence time.

Precisely, for integers \(m\ge2\), odd \(1\le h\le m\), and odd \(s\ge1\), put
\[
 a_{m,h}=2^{-m}\sum_{j=0}^{m}\binom mj
       \left(\frac{2\min\{j,h\}}h-1\right)^2.
\]
At every iteration \(k\ge1\), the reused and re-queried averaged updates defined below satisfy
\[
 \mathbb E[X_{k,\mathrm{reuse}}^2]=\frac1s+\left(1-\frac1s\right)a_{m,h},
 \qquad \mathbb E[X_{k,\mathrm{fresh}}^2]=\frac1s.
\]
Their exact mean-square ratio is therefore \(1+(s-1)a_{m,h}\). The all-eligible-row cached update has squared error \(a_{m,h}\) at every positive iteration and its successive signs form a symmetric Markov chain with flip probability
\[
 p_{m,h}=2^{-m}\sum_{j=0}^{(h-1)/2}\binom mj.
\]
For any odd sequence \(h=h_m\) such that \(h_m/m\to q\in(0,1)\),
\[
 a_{m,h_m}\longrightarrow F(q)=
 \begin{cases}1,&0<q\le1/2,\\
 ((1-q)/q)^2,&1/2<q<1,\end{cases}
\]
and
\[
 -m^{-1}\log p_{m,h_m}\longrightarrow
 I(q)=\log2+\frac q2\log\frac q2+
 \left(1-\frac q2\right)\log\left(1-\frac q2\right)>0.
\]
In particular, with \(s=h_m\), the mean-square ratio between reused and fresh sampled updates grows as \(m qF(q)\) to leading order; for the all-row update the expected sign-run length is \(p_{m,h_m}^{-1}=\exp(mI(q)+o(m))\).

## Assumptions and scope
Take \(A\in\mathbb R^{m\times1}\) with \(A_i=1\), and true solution \(x_*=0\) to \(Ax=0\). Thus this is an exactly consistent, full-column-rank, condition-one problem. Each observation of any row returns an independent Rademacher value \(\xi\in\{-1,+1\}\) with equal probabilities; observations are independent across both rows and repeated calls. There is **no fixed corruption**. Each iteration begins with a nonzero scalar iterate \(x\).

1. **Screening:** query every one of the \(m\) rows once, obtaining \(\xi_1,\ldots,\xi_m\), and retain precisely the \(h\) rows having smallest \(|\xi_i-x|\). Break ties arbitrarily within a residual level; this does not affect the conclusions.
2. **Sampled reused update:** sample \(s\) labels independently and uniformly *with replacement* from the retained set. With unit step, average the corresponding cached residual corrections; the new scalar iterate equals the average of the \(s\) cached signs.
3. **Sampled fresh update:** use exactly the same selection mechanism, but obtain an independent new Rademacher observation for **each selected occurrence**, including repeated labels. With unit step, average these new signs.
4. **All-eligible cached update:** use each of the \(h\) retained cached observations exactly once, with equal weights; no second-stage sampling takes place.

Each variant is a separately run process from any deterministic \(x_0\ne0\). Odd \(h\) and \(s\) ensure none of the processes hits zero, avoiding a residual-ranking tie between \(\xi=+1\) and \(\xi=-1\) at the next iteration. These are three explicitly distinct algorithms; in particular setting \(s=h\) in the sampled method does **not** equal the all-row method, because the former samples with replacement.

## Proof
**Selection lemma.** For \(x>0\), the identity \(|1-x|<|-1-x|\) holds, including for \(x>1\). Thus the screening keeps as many positive signs as possible; the number \(J\) of positive cached observations is \(\mathrm{Binomial}(m,1/2)\). If \(J\ge h\), all selected cached signs are positive. Otherwise the selected set contains exactly \(J\) positive and \(h-J\) negative signs. For \(x<0\), the same statement holds with negative and positive signs interchanged. Consequently, independently of the sign and magnitude of the nonzero current iterate, the proportion of eligible cached signs agreeing with its sign is
\[
 \pi_J=\frac{\min\{J,h\}}h,
 \qquad \mathbb P(J=j)=2^{-m}\binom mj.
\]
The random variable \(J\) is independent of the past because screening is freshly repeated each iteration.

**One-step exact errors.** Conditional on \(J=j\) and the sign of \(x\), each reused second-stage draw has values \(\pm1\), with conditional mean \(\operatorname{sgn}(x)(2\pi_j-1)\) and conditional variance \(4\pi_j(1-\pi_j)\). The conditional mean square of the average of \(s\) such draws is therefore
\[
 \frac1s+\left(1-\frac1s\right)(2\pi_j-1)^2.
\]
Averaging over the binomial law proves the first formula. All-row averaging gives exactly \(x_{\mathrm{new}}=\operatorname{sgn}(x)(2\pi_J-1)\) and hence mean square \(a_{m,h}\). In the fresh variant, conditioning on every screening observation and every selected row label leaves \(s\) independent mean-zero unit-variance Rademacher updates. Their average has mean square exactly \(1/s\). Since an odd number of signs never averages to zero, all conditional identities can be iterated inductively for every \(k\ge1\), regardless of the initial magnitude.

**Sign process and run lengths.** For the all-row update with odd \(h\), \(2\pi_J-1\) is never zero; its sign is negative exactly when \(J\le(h-1)/2\). Hence the sign flips with probability \(p_{m,h}\), independent of the current sign and the entire past. The transition matrix is
\[
 \begin{pmatrix}1-p_{m,h}&p_{m,h}\\p_{m,h}&1-p_{m,h}\end{pmatrix}.
\]
It has stationary sign probabilities \((1/2,1/2)\), sign autocorrelation \((1-2p_{m,h})^\ell\) at lag \(\ell\) in stationarity, and geometric run lengths with mean \(1/p_{m,h}\). Because \(0<p_{m,h}\le1/2\), this Markov chain is irreducible and has no absorbing sign.

**Large-system limits.** Write \(J_m\sim\mathrm{Binomial}(m,1/2)\) and suppose \(h_m/m\to q\in(0,1)\). The law of large numbers and bounded convergence give
\[
 2\min\{J_m,h_m\}/h_m-1\xrightarrow{\mathbb P}
 2\min\{1/(2q),1\}-1,
\]
whose square is \(F(q)\). This proves the exact floor limit, including the threshold \(q=1/2\). If \(s=h_m\), then \(h_m\to\infty\), so the reused/fresh squared-error ratio \(1+(h_m-1)a_{m,h_m}\) divided by \(m\) converges to \(qF(q)>0\).

For the flip exponent put \(r_m=(h_m-1)/2\), so \(r_m/m\to q/2<1/2\). The binomial coefficients increase on \(0\le j\le r_m\) for all sufficiently large \(m\), yielding
\[
 2^{-m}\binom m{r_m}\le p_{m,h_m}
 \le (r_m+1)2^{-m}\binom m{r_m}.
\]
Taking logarithms and applying Stirling's formula establishes
\[
 \lim_{m\to\infty}-m^{-1}\log p_{m,h_m}
 =\log2-H(q/2)=I(q),
\]
where \(H(t)=-t\log t-(1-t)\log(1-t)\). Since \(q/2\in(0,1/2)\), \(I(q)>0\). This gives the exponential sign-persistence law with a justified \(o(m)\) remainder in the logarithm, not an unproved sharp multiplicative prefactor.

## Verification
The included `checker.py` uses only Python's exact integer arithmetic and `fractions.Fraction`. It enumerates the binomial screening distribution and the conditional binomial second-stage law for \(2\le m\le12\), every admissible odd \(h\), and several odd \(s\), verifying the exact formulas including the sampled/full-screen distinction. It checks finite examples and illustrates three asymptotic limits; these finite computations are **not** the proof for arbitrary \(m\). Run `python3 checker.py`; the recorded successful execution printed `VERIFY_OK 867`.

For \(m=5\), \(h=3\), \(s=3\), the exact values are
\[
 a_{5,3}=7/12,\quad \mathbb E[X_{\mathrm{reuse}}^2]=13/18,
 \quad\mathbb E[X_{\mathrm{fresh}}^2]=1/3,\quad
 p_{5,3}=3/16.
\]
Thus the exact reused/fresh mean-square ratio is \(13/6\) and the all-row mean sign-run length is \(16/3\) iterations.

## Relationship to prior work
Cai, Chen, Ma, and Wu (2025 preprint; 2026 journal) analyze the subsampling cost of quantile Kaczmarz with a fixed sparse corruption vector; their main theorem concerns convergence over a finite horizon, not these independent remeasurement and exact binomial identities. Cheng, Jarman, Needell, and Rebrova (2022 preprint) introduce quantile-averaged block Kaczmarz using residual screening and cached averaged updates. Coria, Haddock, and Pacheco (2024) investigate time-varying noise and corruption for quantile randomized Kaczmarz, but not the stated finite-\(m\) all-row sign law. Shvaiko and Rebrova (posted 16 November 2026) explicitly distinguish re-queried and reused AQRK observations and prove general benefits of re-querying. Thus **the qualitative bias-versus-requery observation is prior work, not claimed here**. The specific contribution assessed here is the joint exact sampled-batch risk, fixed-quantile nonzero-floor function, and binomial large-deviation sign-persistence law on one sharply defined scalar testbed.

## Limitations
This is a structured one-dimensional, redundant-row example with independent bounded two-point query noise. Its threshold is in the asymptotic *screening fraction* and is **not** a universal threshold for quantile Kaczmarz on arbitrary matrices. The mean-square identities rely on unit steps and a fresh measurement on **every** new residual query; other relaxation or measurement models need different analysis. Exponential sign persistence does not imply a permanent wrong-sign state, does not establish the mixing rate of arbitrary non-scalar iterates, and is not a numerical instability. The number of screening queries scales with \(m\); the theorem does not claim the fresh method is cheaper in query cost. The special case \(q=1\) is excluded from the positive-floor asymptotic, and no optimality claim over other algorithms is made. The structural example does not assert a general theorem for non-scalar systems.

## References
- Jian-Feng Cai, Junren Chen, Anna Ma, Tong Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185v1 (first posted 21 July 2025), https://arxiv.org/abs/2507.15185.
- Lu Cheng, Benjamin Jarman, Deanna Needell, Elizaveta Rebrova, *On Block Accelerations of Quantile Randomized Kaczmarz for Corrupted Systems of Linear Equations*, arXiv:2206.12554v1 (2022), https://arxiv.org/abs/2206.12554.
- Alfredo Coria, Jamie Haddock, Francisco Pacheco, *On Quantile Randomized Kaczmarz for Linear Systems with Time-Varying Noise and Corruption*, arXiv:2403.19874 (2024), https://arxiv.org/abs/2403.19874.
- Sofiia Shvaiko, Elizaveta Rebrova, *Beyond the error horizon: averaged quantile Kaczmarz methods for corrupted and noisy linear systems*, arXiv:2611.21926v1 (posted 16 November 2026), https://arxiv.org/html/2611.21926v1. This later source is included as closely related literature, not as the eligibility-determining precursor.
