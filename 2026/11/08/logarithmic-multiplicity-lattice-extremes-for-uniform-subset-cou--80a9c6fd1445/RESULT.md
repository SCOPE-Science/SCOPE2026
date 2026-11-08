# Logarithmic-multiplicity lattice extremes for uniform subset coupon draws

## Finding

Consider \(N\) coupon types. In each integer round, independently of all other rounds, choose a uniformly random \(d_N\)-element subset of the \(N\) types and give each chosen type one occurrence. Fix \(\alpha>0\), suppose \(p_N=d_N/N\to p\in(0,1)\), and require each type to be sampled at least \(m_N=\lceil\alpha\log N\rceil\) times. Write \(T_N\) for the first round at which this requirement is met.

For \(0<u,v<1\), set the binary relative entropy
\[
D(u\Vert v)=u\log\frac{u}{v}+(1-u)\log\frac{1-u}{1-v}.
\]
There is a unique \(\beta_N>\alpha/p_N\) solving
\[
\beta_N D(\alpha/\beta_N\Vert p_N)=1.
\]
Define
\[
\eta_N=\frac{\alpha(1-p_N)}{p_N(\beta_N-\alpha)},\qquad
r_N=\frac{(1-p_N)\beta_N}{\beta_N-\alpha},\qquad s_N=-\log r_N.
\]
All sufficiently large \(N\) satisfy \(0<\eta_N,r_N<1\); these parameters converge to their analogues \(\beta,\eta,r,s\) at \(p\). Let
\[
q_N(t)=\Pr\big\{\operatorname{Bin}(t,p_N)<m_N\big\},\qquad
b_N=\min\{t\in\mathbb Z_{\ge0}:Nq_N(t)\le1\},\qquad
\theta_N=Nq_N(b_N).
\]
Then
\[
\boxed{b_N=\beta_N\log N-\frac{\log\log N}{2s_N}+O(1).}
\]
In particular, \(\theta_N\le1\) and \(\theta_N\ge r+o(1)\). If \(U_N(t)\) counts the types with fewer than \(m_N\) occurrences after \(t\) rounds, then for each fixed integer \(k\), \(U_N(b_N+k)\) is asymptotically Poisson with moving mean \(\theta_N r_N^k\). Uniformly over all integer \(k\),
\[
\boxed{\Pr(T_N-b_N\le k)=\exp(-\theta_N r_N^k)+o(1).}
\]
This is a phase-dependent *discrete*, rather than continuous, extreme-value law. In particular its geometric base \(r\) depends on \(\alpha\) as well as on \(p\).

There are also additive constant-order moment laws. For \(\vartheta\in(0,1]\) and \(u\in(0,1)\), put
\[
\begin{aligned}
\mu(\vartheta,u)&=\sum_{j=0}^{\infty}(1-e^{-\vartheta u^j})
 -\sum_{j=1}^{\infty}e^{-\vartheta u^{-j}},\\
M_2(\vartheta,u)&=\sum_{j=0}^{\infty}(2j+1)(1-e^{-\vartheta u^j})
 +\sum_{j=1}^{\infty}(2j-1)e^{-\vartheta u^{-j}}.
\end{aligned}
\]
Both series converge absolutely. Then
\[
\boxed{\begin{aligned}
\mathbb E T_N&=b_N+\mu(\theta_N,r_N)+o(1),\\
\operatorname{Var}(T_N)&=M_2(\theta_N,r_N)-\mu(\theta_N,r_N)^2+o(1).
\end{aligned}}
\]
The asymptotics hold along **every** sequence \(N\to\infty\) satisfying the stated assumptions, including sequences without a limiting lattice phase \(\theta_N\).

## Assumptions and scope

The subsets have exactly \(d_N\) distinct coupons per round, are uniform among all \(\binom{N}{d_N}\) subsets, and are independent across rounds. The batch fraction converges to a strictly interior value \(p\). The threshold multiplicity is \(m_N=\lceil\alpha\log N\rceil\) with fixed \(\alpha>0\). Time is counted in integer rounds. The theorem does not claim a growing-threshold result outside this logarithmic regime, nor does it apply to unequal coupon probabilities, to sampling with replacement within a batch, or to dependent batches.

## Proof

**1. A one-type large-deviation saddle.** Write \(L=\log N\), \(p=p_N\) temporarily, \(m=\lceil\alpha L\rceil\), and \(q(t)=\Pr\{\operatorname{Bin}(t,p)\le m-1\}\). The function \(f(z)=zD(\alpha/z\Vert p)\) is zero at \(z=\alpha/p\), tends to infinity, and has derivative
\[
 f'(z)=\log\frac{z-\alpha}{z(1-p)}>0\quad(z>\alpha/p).
\]
Hence the asserted unique \(\beta_N\). For \(t=\beta_N L+O(\log L)\), successive binomial masses below \(m-1\) have ratio
\[
\frac{\Pr(\operatorname{Bin}(t,p)=j-1)}{\Pr(\operatorname{Bin}(t,p)=j)}
=\frac{j(1-p)}{(t-j+1)p}\le\eta_N+o(1),\quad j\le m-1.
\]
The ratio is \(\eta_N+o(1)\) for each fixed number of steps below the endpoint, and \(\eta_N\to\eta<1\). Summing the asymptotically geometric lower tail and using uniform Stirling estimates gives
\[
q(t)=\frac{1+o(1)}{1-\eta_N}\frac{\exp\big[-tD((m-1)/t\Vert p_N)\big]}
{\sqrt{2\pi t\,((m-1)/t)(1-(m-1)/t)}}.
\]
The error is uniform for integer \(t=\beta_N L+O(\log L)\). Put \(\delta_N=m-1-\alpha L\), which remains bounded. Taylor expansion of the relative-entropy exponent at \((\beta_N L,\alpha L)\) yields
\[
tD((m-1)/t\Vert p_N)=L+s_N(t-\beta_N L)+\delta_N\log\eta_N+o(1).
\]
Consequently, uniformly in the indicated window,
\[
\boxed{Nq(t)=\frac{C_N+o(1)}{\sqrt L}\,r_N^{\,t-\beta_N L},\qquad
 C_N=\frac{\eta_N^{-\delta_N}}
 {(1-\eta_N)\sqrt{2\pi\alpha(1-\alpha/\beta_N)}}.}
\]
The quantities \(C_N\) and their reciprocals are uniformly bounded. The threshold \(b_N\) therefore exists and satisfies the stated centering formula. In the same window,
\[
\frac{q(t+1)}{q(t)}\longrightarrow r
\]
uniformly. Since \(Nq(b_N)\le1<Nq(b_N-1)\), it follows that \(r+o(1)\le\theta_N\le1\). For fixed integer \(k\), \(Nq(b_N+k)=\theta_Nr_N^k(1+o(1))\).

**2. Joint rare-type probabilities.** Fix \(h\ge1\) distinct coupon labels and one particular binary inclusion pattern on those labels in one round, containing \(a\) inclusions. Its exact probability is
\[
\frac{(d_N)_{a}(N-d_N)_{h-a}}{(N)_{h}},
\]
where \((z)_j=z(z-1)\cdots(z-j+1)\). Since \(p_N\) stays away from zero and one, the ratio to the corresponding \(h\) independent \(\operatorname{Bernoulli}(p_N)\) pattern probability is \(1+O_h(N^{-1})\), uniformly over all patterns. Over \(t=O(\log N)\) independent rounds, the likelihood ratio for **every** \(h\)-label history lies between \(1-O_h(t/N)\) and \(1+O_h(t/N)\). In particular, for fixed \(k\) and \(t=b_N+k\), the probability that all \(h\) labels remain under-collected is
\[
q_N(t)^h\bigl(1+O_h(t/N)\bigr).
\]
Thus the factorial moments of \(U_N(t)\) obey
\[
\mathbb E(U_N(t))_h=(N)_h q_N(t)^h(1+o(1))
 =\bigl(\theta_Nr_N^k\bigr)^h+o(1).
\]
The boundedness of the moving means gives the Poisson law (by subsequences, or the factorial-moment characterization), and hence the asserted completion-time probability at every fixed integer \(k\).

**3. Uniform tails and moments.** For any two distinct coupon types, condition on the first one's total number \(A\) of occurrences during \(t\) rounds. The second type then has distribution
\[
\operatorname{Bin}\left(A,\frac{d_N-1}{N-1}\right)
 +\operatorname{Bin}\left(t-A,\frac{d_N}{N-1}\right),
\]
with independent summands. Increasing \(A\) replaces a larger success probability by a smaller one. Therefore \(\Pr\{B<m_N\mid A\}\) is nondecreasing in \(A\), whereas \(\mathbf1_{\{A<m_N\}}\) is nonincreasing. Their covariance is nonpositive. Summing over pairs proves
\[
\operatorname{Var}U_N(t)\le\mathbb E U_N(t)=Nq_N(t).
\]
It follows by Chebyshev that
\[
\Pr(T_N\le t)=\Pr(U_N(t)=0)\le\frac1{Nq_N(t)},
\]
while the union bound gives \(\Pr(T_N>t)\le Nq_N(t)\).

The exact recursion
\[
q_N(t+1)=q_N(t)-p_N\Pr\{\operatorname{Bin}(t,p_N)=m_N-1\}
\]
shows that its successive ratio is bounded above by some constant strictly below one for all \(t\ge b_N\). Indeed the conditional boundary mass at \(m_N-1\), given a count below \(m_N\), is bounded away from zero at \(b_N\), and is nondecreasing in \(t\) by the binomial monotone likelihood-ratio property. Therefore \(\Pr(T_N>b_N+j)\le C\rho_1^j\) for constants \(\rho_1<1\) and all \(j\ge0\).

Choose an intermediate \(\beta_0\) strictly between \(\alpha/p\) and \(\beta\). On all times from \(\lceil\beta_0L\rceil\) to \(b_N\), a uniform lower bound on the conditional boundary mass likewise gives \(q_N(t+1)/q_N(t)\le\rho_2<1\). Hence \(\Pr(T_N\le b_N-j)\le C\rho_2^j\) until that intermediate time. Before it, \(Nq_N(t)\ge N^{c_0}\) for some \(c_0>0\), so Chebyshev bounds the remaining \(O(L)\) left-tail terms by \(N^{-c_0}\). This proves uniform integrability of all fixed powers of \(T_N-b_N\).

At fixed integers the limiting distribution is that of the integer-valued \(Z_{\vartheta,u}\) with \(\Pr(Z_{\vartheta,u}\le k)=e^{-\vartheta u^k}\). The tail bounds upgrade pointwise convergence to a uniform CDF approximation and convergence of first two moments to the displayed absolutely convergent lattice sums, uniformly along possible subsequential phases. This proves the theorem.

## Verification

The reproducible companion `verify.py` uses only the Python 3 standard library. It checks the exact hypergeometric inclusion-pattern identity against enumeration, the binomial survival recurrence, the two-label nonpositive defect covariance for finite parameters, and numerical saddlepoint/local-ratio diagnostics for multiple probabilities, thresholds and sample sizes. Running `python3 verify.py` yielded **3,326 passed assertions**. These are finite checks and numerical diagnostics, not substitutes for the preceding analytic arguments.

## Relationship to prior work

Castro and Marinho (arXiv:2610.33199, publicly posted October 23, 2026) determine growing-multiplicity cutoff profiles for **one uniformly sampled coupon per draw**, via gamma extremes and a continuous Gumbel window. The present model samples a fixed positive proportion of coupons **without replacement within each round**, and its integer-round terminal scale does not diverge. Their single-coupon result does not imply the present binomial large-deviation saddle or phase-dependent lattice law.

Berend and Sher (arXiv:2605.06953) analyze uniform group drawing, including positive-fraction batches, for collecting **one copy per type**. Their periodic correction is relevant background, but does not cover a logarithmically growing required multiplicity. Schilling and Henze (2021) treat **fixed** multiplicity in group drawings. Betken and Thäle (2023) study undrawn types (zero occurrences) under a different asymptotic batch regime. Doumas and Spektor (arXiv:2607.01463) focus on one-copy collection and a different retention rule. All are distinct from the simultaneous large-deviation and growing-multiplicity regime here.

The general theory of occupancy extremes, older random group-allocation results and any broader theorem on dependent binomial maxima may contain a stronger applicable statement; no unconditional claim of historical uniqueness is made.

## Limitations

The theorem assumes a deterministic positive limiting sampling fraction and a logarithmic multiplicity with bounded rounding error. It does not cover \(m_N/\log N\to0\) or \(\infty\), and it does not establish where a continuous extreme-value regime begins. The phase \(\theta_N\) need not converge. The primary literature comparisons do not constitute an exhaustive priority search; an inaccessible or differently formulated general occupancy theorem remains possible. Independent mathematical review has not been performed.

## References

1. M. E. Castro and R. Marinho, *Cutoff profile for the coupon collector with many collections*, arXiv:2610.33199 (2026), https://arxiv.org/html/2610.33199v1.
2. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953 (2026), https://arxiv.org/html/2605.06953v1.
3. J. Schilling and N. Henze, *Two poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability 58 (2021), 966–977, https://doi.org/10.1017/jpr.2021.15.
4. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, Journal of Applied Probability 60 (2023), 1352–1366, https://doi.org/10.1017/jpr.2023.6.
5. A. V. Doumas and S. Spektor, *Two Multi--Draw Coupon Collector models with different retention rules*, arXiv:2607.01463 (2026), https://arxiv.org/abs/2607.01463.
