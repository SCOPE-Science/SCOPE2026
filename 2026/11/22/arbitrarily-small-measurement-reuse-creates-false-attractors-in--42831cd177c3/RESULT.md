# Arbitrarily small measurement reuse creates false attractors in residual-screened scalar Kaczmarz

## Finding

For an exactly consistent scalar system, residual screening of noisy observations can create two **false stable equilibria** even when every measurement noise variable is centered. Arbitrarily small positive reuse probability is enough, and increasing the number of update queries cannot remove the resulting bias or all the sampling variance. The same effect leads to **actual almost-sure convergence to a wrong solution on an event of probability exceeding \(0.89\)** for a valid decreasing-step schedule.

Let \(m\ge2\) be the number of candidate observations, \(s\ge1\) the number of update queries, and \(p\in[0,1]\) the probability of reusing the screened observation in each update query. Put
\[
\kappa_m=1-2^{1-m},\qquad \mu=p\kappa_m.
\]
For every nonzero current iterate \(x\), the exact conditional mean and variance of the averaged queried right-hand side \(\overline Y\) are
\[
\boxed{\mathbb E(\overline Y\mid x)=\mu\operatorname{sgn}(x),\qquad
\operatorname{Var}(\overline Y\mid x)=p^2(1-\kappa_m^2)+\frac{1-p^2}{s}.}
\]
Consequently, \(p=0\) is the sharp refresh frontier: with full fresh querying the only mean-equilibrium is zero, whereas every \(p>0\) produces stable nonzero mean-equilibria \(\pm\mu\), and the large-batch variance tends to the positive floor \(p^2(1-\kappa_m^2)\).

For every \(p>0\), start the actual stochastic iteration from \(X_0=\mu\), use independent new candidate batches at successive steps and the harmonic stepsizes \(\eta_n=\mu/[4(n+1)]\), and update
\[
X_{n+1}=(1-\eta_n)X_n+\eta_n\overline Y_n.
\]
Then
\[
\boxed{\Pr\bigl(\lim_{n\to\infty}X_n=\mu\bigr)\ge1-\frac{\pi^2}{96}>0.89.}
\]
The reference solution remains exactly zero. In contrast, for \(p=0\) this algorithm converges almost surely to zero for every deterministic \(0<\eta_n\le1\) with \(\sum_n\eta_n=\infty\) and \(\sum_n\eta_n^2<\infty\).

## Assumptions and scope

The exact scalar linear system has as many identical unit-normalized coefficient rows as desired, all equal to one, and exact right-hand side zero. Whenever a measurement is queried, its observed right-hand side is \(+1\) or \(-1\), independently with probability \(1/2\). These are *dense bounded mean-zero observation errors*, not sparse adversarial corruptions. The streaming candidates and all refresh coins are independent across iterations.

At iterate \(x\), the screening stage queries \(m\) independent observations \(B_1,\ldots,B_m\in\{-1,+1\}\). Choose one index minimizing \(|x-B_i|\), using an independent uniform tie rule, and call its observed sign \(S\). For each of the \(s\) update queries, an independent Bernoulli coin with probability \(p\) determines whether the previously stored value \(S\) is reused; otherwise draw a new independent Rademacher sign. Denote the update values by \(Y_1,\ldots,Y_s\) and their average by \(\overline Y\). The update rows all have coefficient one; the method is a relaxed scalar Kaczmarz step toward \(\overline Y\).

This specifies **one screened winning observation per candidate batch** and allows repeated querying of that selected row. It is not a claim about arbitrary accepted-set sizes, independent row geometry, random-matrix QRK convergence, or a different quantile-threshold acceptance scheme.

## Proof

**1. Winner law.** If \(x>0\), the positive observation has strictly smaller absolute residual than the negative one, because \(|x-1|<|x+1|\). Therefore \(S=+1\) unless all \(m\) candidates are negative. The exceptional probability is \(2^{-m}\), so \(\mathbb E(S\mid x)=1-2^{1-m}=\kappa_m\) and \(\operatorname{Var}(S\mid x)=1-\kappa_m^2\). For \(x<0\), symmetry changes the mean sign. At \(x=0\), uniform tie breaking makes the mean zero. These facts hold for all nonzero magnitudes of \(x\), including outside the observation interval.

**2. Conditional moments with mixed reuse.** Conditional on \(S\), the update values \(Y_j\) are independent and satisfy \(\mathbb E(Y_j\mid S)=pS\) and \(\operatorname{Var}(Y_j\mid S)=1-p^2\). Consequently, by total expectation and total variance,
\[
\mathbb E(\overline Y\mid x)=p\mathbb E(S\mid x),\qquad
\operatorname{Var}(\overline Y\mid x)=\frac{1-p^2}{s}+p^2\operatorname{Var}(S\mid x).
\]
These are the displayed formulas. For \(0<p\le1\) and finite \(m\ge2\), \(\mu>0\) and \(1-\kappa_m^2>0\). On the positive half-line the mean iteration maps \(x\) to \((1-\eta)x+\eta\mu\), so \(+\mu\) attracts all positive states under any fixed \(0<\eta\le1\). The negative half-line similarly attracts to \(-\mu\). For \(p=0\), the mean update simply contracts to zero. This proves the exact sharp boundary in the stated family.

**3. A probability bound for the actual noisy iterates.** Fix \(p>0\) and set \(X_0=\mu\). Define \(\tau=\inf\{n\ge0:X_n\le0\}\). While \(n<\tau\), write \(e_n=X_n-\mu\). The conditional-mean formula gives
\[
e_{n+1}=(1-\eta_n)e_n+\eta_n\xi_n,
\quad\mathbb E(\xi_n\mid\mathcal F_n)=0,
\quad\mathbb E(\xi_n^2\mid\mathcal F_n)\le1.
\]
The last bound follows because \(\overline Y_n\in[-1,1]\) for every outcome. Since \(0<\eta_n\le1/4\), the stopped squared error \(Z_n=(X_{n\wedge\tau}-\mu)^2\) obeys
\[
\mathbb E(Z_{n+1}\mid\mathcal F_n)
\le Z_n-\eta_n e_n^2\mathbf 1_{\{\tau>n\}}+\eta_n^2.
\]
In particular \(\mathbb E Z_n\le\sum_{j<n}\eta_j^2\). On \(\{\tau\le n\}\), the stopped iterate is nonpositive and therefore \(Z_n\ge\mu^2\). Hence
\[
\Pr(\tau<\infty)\le\frac{\sum_{n\ge0}\eta_n^2}{\mu^2}
=\frac1{16}\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{96}.
\]
The same nonnegative almost-supermartingale inequality, with \(\sum\eta_n^2<\infty\), shows that \(Z_n\) converges almost surely and \(\sum_n\eta_n e_n^2\mathbf1_{\{\tau>n\}}<\infty\) almost surely. Indeed this is the standard elementary supermartingale convergence lemma applied after adding the nonnegative remaining tail \(\sum_{j\ge n}\eta_j^2\). On \(\{\tau=\infty\}\), \(Z_n=e_n^2\) converges, and because \(\sum_n\eta_n=\infty\) its limit must be zero. Thus \(X_n\to\mu\) on an event of probability at least \(1-\pi^2/96\).

**4. Full-refresh comparison.** For \(p=0\), each \(\overline Y_n\) has conditional mean zero and second moment \(1/s\), independently of the screening event. For any deterministic \(0<\eta_n\le1\),
\[
\mathbb E(X_{n+1}^2\mid\mathcal F_n)
=(1-\eta_n)^2X_n^2+\eta_n^2/s
\le(1-\eta_n)X_n^2+\eta_n^2.
\]
By the same supermartingale convergence argument and the sum conditions on steps, \(X_n^2\) converges almost surely and \(\sum_n\eta_n X_n^2<\infty\), forcing its limit to zero. This establishes full-refresh almost-sure correctness.

## Verification

The accompanying standalone `verify.py` performs exact-rational exhaustive comparisons for all candidate sign configurations for \(m=2,\ldots,8\), reuse probabilities \(p\in\{0,1/9,1/3,1/2,7/8,1\}\), both signs of the iterate, and \(s=1,\ldots,8\). For \(s\in\{1,2,4\}\), it additionally enumerates the joint law of all averaged update outcomes and verifies normalization, expectation, and variance without relying on the total-variance formula. The program returned `VERIFY_OK 2268`. It is a finite consistency check; the proof of the general parameter theorem and almost-sure statement is the exact argument above.

## Relationship to prior work

Battaglia, Cai, Chen, Ma, Needell, and Wu (2026) analyze a streaming quantile Kaczmarz algorithm in which the quantile is formed from a candidate group and a **separate independent** observation is reserved for the update. Their convergence theorem is for sparse Massart/oblivious corruptions, a different model from the present dense Rademacher noise; their source motivates testing the role of independence. Cai, Chen, Ma, and Wu (2025 preprint, 2026 journal) study the sample size for quantile selection, not partial reuse drift.

Shvaiko and Rebrova (first public 16 November 2026) establish and discuss the qualitative selection-bias problem in averaged quantile Kaczmarz and analyze full re-querying, with an alternate accepted-set sampling scheme. Thus the mere assertion that selection biases reused noise is **already known** and is not the originality claim here. The added statement is the exact all-batch \(p\)-interpolation and sharp zero-reuse frontier combined with a constructive high-probability **pathwise** false-limit theorem under decreasing stepsizes. A previous exact scalar all-eligible cached/fresh moment identity concerns constant unit steps and endpoints, not this quantitative phase diagram or almost-sure attraction.

## Limitations

This is an exactly specified **scalar, repeated-row, minimum-residual winner** oracle with dense independent bounded noise; it does not imply failure under other screening quantiles, multidimensional random designs, or sparsely corrupted streaming systems. Only a **positive lower bound** on wrong-attractor convergence probability is proved; no exact basin-hitting probability or universal starting-point convergence law is claimed. The screened-noise conditional mean is discontinuous at zero, so generic smooth-drift stochastic-approximation theorems do not directly apply without their hypotheses. The experiment checker verifies finite cases and is not a substitute for the analytic probabilistic proof. Mathematical priority has not been independently audited.

## References

1. E. Battaglia, J.-F. Cai, J. Chen, A. Ma, D. Needell and T. Wu, *Quantile Randomized Kaczmarz for Streaming Linear Systems with Massart Noise*, arXiv:2608.27968, first public 28 August 2026. https://arxiv.org/abs/2608.27968
2. J.-F. Cai, J. Chen, A. Ma and T. Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185, first public 21 July 2025; later SIAM J. Matrix Anal. Appl. 47 (2026), 802–823. https://arxiv.org/abs/2507.15185
3. S. Shvaiko and E. Rebrova, *Beyond the error horizon: averaged quantile Kaczmarz methods for corrupted and noisy linear systems*, arXiv:2611.21926, first public 16 November 2026. https://arxiv.org/abs/2611.21926
