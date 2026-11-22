# A dimension-four Gaussian boundary for quenched stationary voter time averages

## Finding
Consider the nearest-neighbour voter model on \(\mathbb Z^d\) with independent sitewise Poisson resets to each site's **fixed original** fair opinion. Let every site copy one uniformly selected neighbour at rate \(1\), and reset at rate \(r>0\). Write \(\xi_x\in\{-1,+1\}\) for the independent fair original opinions. For a fixed realization \(\xi\), let \(\sigma_x(t)\) be the stationary process and define the quenched long-time local occupation mean
\[
M_r(\xi)=\lim_{T\to\infty}\frac1T\int_0^T\sigma_0(t)\,dt.
\]
The limit exists in conditional \(L^2\) and equals \(\sum_x k_r(x)\xi_x\), where \(k_r(x)=r\int_0^\infty e^{-rt}p_t(x)\,dt\) and \(p_t\) is the continuous-time simple symmetric nearest-neighbour random-walk heat kernel with total jump rate \(1\).

Let \(V_d(r)=\mathbb E_\xi[M_r(\xi)^2]\) and \(Z_{d,r}=M_r(\xi)/\sqrt{V_d(r)}\), the standardized quenched time average. The following sharp **dimension-four transition** holds as \(r\downarrow0\):
\[
\boxed{\quad Z_{d,r}\ \Longrightarrow\ N(0,1)\quad\text{if and only if}\quad 1\le d\le4.\quad}
\]
For every \(d\ge5\), instead, under the coupling using the same original spins for all \(r\),
\[
Z_{d,r}\ \xrightarrow{L^2}\
Y_d=\frac{\sum_{x\in\mathbb Z^d}G_d(x)\xi_x}{\sqrt{S_d}},\qquad
G_d(x)=\int_0^\infty p_t(x)\,dt,\qquad
S_d=\sum_xG_d(x)^2<\infty.
\]
The limit \(Y_d\) is non-Gaussian and has strictly negative excess kurtosis
\[
\mathbb E Y_d^4-3=-\frac{2\sum_xG_d(x)^4}{S_d^2}<0.
\]
The disorder variance exhibits the corresponding regimes:
\[
V_d(r)\sim
\begin{cases}
\displaystyle \left(\frac d{2\pi}\right)^{d/2}\Gamma(2-d/2)r^{d/2},&d=1,2,3,\\[6pt]
\displaystyle \frac4{\pi^2}r^2\log(1/r),&d=4,\\[6pt]
\displaystyle S_dr^2,&d\ge5.
\end{cases}
\]
At the critical dimension, the standardized excess kurtosis vanishes at the **sharp logarithmic-squared rate**
\[
\boxed{\quad \mathbb E Z_{4,r}^4-3
\sim-\frac{\pi^4}{8\log^2(1/r)}\sum_{x\in\mathbb Z^4}G_4(x)^4.\quad}
\]
In dimension one there is also the exact identity
\[
V_1(r)=\frac{\sqrt r\,(1+r)}{(r+2)^{3/2}}.
\]
These statements concern the **distribution across fixed original opinion fields** of a *conditional stationary time average*, not the annealed single-time spin or annealed two-point correlations.

## Assumptions and scope
Fix any integer dimension \(d\ge1\). At each lattice site independently, a rate-one clock makes its spin copy a uniformly selected one of the \(2d\) nearest-neighbour spins. A separate independent rate-\(r\) Poisson clock sets that spin to its own initial value \(\xi_x\). The latter are i.i.d. fair symmetric signs, sampled once and kept fixed throughout the dynamics. There are no common/global resets, fresh-spin resets, external fields, or synchronous updates. The lattice is infinite from the outset. The limits in the theorem are taken first in stationary physical time and then as \(r\to0\), at fixed dimension; no joint \(T,r\) limit is asserted.

Let \(L f(x)=(2d)^{-1}\sum_{|e|=1}(f(x+e)-f(x))\). Define the heat kernel \(p_t(x)=\Pr_0(X_t=x)\) for its random walk. The expectation \(\mathbb E_\xi\) averages only over the initially fixed field. The stationary spin process conditional on \(\xi\) is constructed by the usual graphical ancestor path traced backwards until its first rate-\(r\) reset. This almost surely terminates in finite backward time, giving a unique stationary local law and a well-defined process on every finite site collection.

## Proof
**1. Quenched stationary mean and time average.** The backward ancestor of the spin at the origin moves as a continuous-time simple random walk of total jump rate \(1\) until an independent exponential time of rate \(r\). It then reads the corresponding fixed original opinion. Therefore the conditional stationary mean is
\[
m_r(0;\xi)=\mathbb E[\sigma_0(0)\mid\xi]=\sum_xk_r(x)\xi_x,
\qquad k_r(x)=r\int_0^\infty e^{-rt}p_t(x)\,dt.
\]
All weights are nonnegative and sum to one. For \(s\ge0\), conditioning on the complete spin field at time zero, the future conditional expectation of the spin at the origin is the sum of a term \(e^{-rs}(P_s\sigma(0))_0\) and a term depending only on \(\xi\); here \(P_s=e^{sL}\). Consequently stationary conditional covariance obeys
\[
\bigl|\operatorname{Cov}(\sigma_0(s),\sigma_0(0)\mid\xi)\bigr|\le e^{-rs},
\]
since a convex average of spins and an individual spin both have conditional variances at most one. Thus
\[
\mathbb E\left[\left(\frac1T\int_0^T\sigma_0(t)dt-m_r(0;\xi)\right)^2\middle|\xi\right]
\le\frac2{rT}.
\]
The stationary time average hence converges in conditional \(L^2\) to \(M_r(\xi)=m_r(0;\xi)\).

**2. Exact disorder variance and fourth cumulant.** Independence and fairness of the original signs imply \(\mathbb E_\xi M_r=0\) and \(V_d(r)=\sum_xk_r(x)^2\). By symmetry and the Chapman–Kolmogorov identity,
\[
\begin{aligned}
V_d(r)&=r^2\int_0^\infty\!\int_0^\infty e^{-r(s+t)}
\sum_xp_s(x)p_t(x)\,dsdt\\
&=r^2\int_0^\infty t e^{-rt}p_t(0)\,dt.
\end{aligned}
\]
A convergent Rademacher series with weights \(a_x\) has fourth moment \(3(\sum a_x^2)^2-2\sum a_x^4\), first for finite truncations and then by bounded fourth moments. Therefore at every positive reset rate
\[
\mathbb E Z_{d,r}^4-3
=-2\frac{\sum_xk_r(x)^4}{V_d(r)^2}.
\]
These identities are exact, not approximations.

**3. Heat-kernel scaling.** The local central limit theorem with the above jump-rate normalization gives
\[
p_t(0)\sim\left(\frac d{2\pi t}\right)^{d/2}\quad(t\to\infty).
\]
For \(1\le d\le3\), substitute \(u=rt\) in the variance integral and use its standard Gaussian heat-kernel bound to obtain the stated Gamma-function coefficient. For \(d=4\), split the integral at fixed large time and at \(1/r\): the asymptotic \(p_t(0)\sim4/(\pi^2t^2)\) yields \(V_4(r)\sim(4/\pi^2)r^2\log(1/r)\). For \(d\ge5\), \(\int_0^\infty tp_t(0)dt<\infty\); dominated convergence gives \(V_d(r)/r^2\to S_d=\int_0^\infty tp_t(0)dt\). This also proves \(S_d=\sum_xG_d(x)^2\) by Tonelli and the semigroup identity.

**4. Gaussian part and sharp boundary.** The largest weight is at the origin, because \(p_t(x)\le p_t(0)\), so \(\max_xk_r(x)=k_r(0)\). The standard small-killing estimates give \(k_r(0)=O(r^{1/2})\) for \(d=1\), \(O(r\log(1/r))\) for \(d=2\), and \(O(r)\) for \(d\ge3\). Comparing these estimates to the variance asymptotics proves
\[
\frac{\max_xk_r(x)}{\sqrt{V_d(r)}}\longrightarrow0
\qquad(1\le d\le4).
\]
For any fixed \(r\), the Rademacher expansion is square-summable and its normalized variance is one. The displayed maximum-weight estimate is the Lindeberg condition for its independent bounded summands; truncating the infinite array to have arbitrarily small leftover variance gives the standard triangular-array central limit theorem. Hence \(Z_{d,r}\Rightarrow N(0,1)\) for \(d\le4\).

**5. Non-Gaussian part.** For \(d\ge5\), the transient Green function \(G_d(x)\) is square-summable by step 3 and \(0\le k_r(x)/r\uparrow G_d(x)\) as \(r\downarrow0\). Dominated convergence in \(\ell^2\) therefore implies
\[
\frac{M_r(\xi)}r\xrightarrow{L^2(\mathbb P_\xi)}\sum_xG_d(x)\xi_x.
\]
Together with \(V_d(r)/r^2\to S_d>0\), this proves the asserted normalized \(L^2\) limit. The Green weights are bounded, nonzero and square-summable; the fourth-moment identity yields a finite strictly negative fourth cumulant. Thus the limiting law cannot be standard Gaussian. This proves the 'only if' direction.

**6. Critical logarithmic fourth cumulant.** In dimension four, the standard simple-random-walk Green estimate \(G_4(x)\le C(1+|x|)^{-2}\) implies \(\sum_xG_4(x)^4<\infty\). By monotone convergence, \(\sum_x[k_r(x)/r]^4\to\sum_xG_4(x)^4\). Substitute this and the sharp variance asymptotic of step 3 into the exact fourth-cumulant identity of step 2 to obtain the displayed \(-\pi^4/8\) coefficient.

**7. One-dimensional normalization check.** Solving \(((1+r)I-(T+T^{-1})/2)k=r\delta_0\) on \(\mathbb Z\) yields \(k_r(n)=\sqrt{r/(r+2)}\,\lambda_r^{|n|}\), with \(\lambda_r=1+r-\sqrt{r(r+2)}\). Summing its geometric squares proves \(V_1(r)=\sqrt r(1+r)/(r+2)^{3/2}\), consistent with the \(d=1\) heat-kernel coefficient \(1/(2\sqrt2)\).

## Verification
The standalone file `check_voter_memory.py` uses only Python's standard library. It checks the quenched mean obtained by inverting the rational resolvent against a separately constructed **full finite-state stationary spin generator** for three- and four-site rings, at two rational reset rates, and evaluates the exact environmental fourth cumulant. It further tests finite Fourier/Green identities, an independently summed one-dimensional formula, and the small-rate coefficient. Execution gives 231 deterministic checks. These finite tests verify important normalization and algebraic components, not the infinite-lattice limit. To reproduce, run `python3 check_voter_memory.py`.

## Relationship to prior work
Grange's 2022 work establishes precisely this local resetting-to-original-opinions mechanism and the one-point resolvent equation, initial-state memory, annealed two-point correlations, and domain walls. **Neither the one-point resolvent representation nor its Markov-generator derivation is claimed as new.** A published comparison for finite voter rings establishes a related memory resolvent and equal-time correlation inequalities, also not claimed as new. Pymar and Rivera treat fresh fair opinion noise and finite-graph density behavior, a distinct reset rule and observable. The specific contribution assessed here is the complete, dimension-sharp **quenched stationary site-time-average distributional limit**, its Gaussian-to-non-Gaussian boundary at \(d=4\), and its sharp critical excess-kurtosis coefficient. Standard random-walk Green estimates and Lindeberg's theorem are used, rather than claimed as new. An unlocated general theorem about random Green-function convolutions could imply the limit, and publication priority is not independently verified.

## Limitations
The claim requires independent fair original spins, homogeneous local reset clocks at positive rate, symmetric nearest-neighbour copying, the infinite regular lattice, and the order of time limits specified above. It neither describes annealed equal-time spin fluctuations nor asserts a Gaussian law for fixed quenched original spins. It does not give a uniform joint \(T\to\infty\), \(r\downarrow0\) limit, arbitrary graph extension, or full rate for convergence in distribution below four dimensions. All Gaussian/non-Gaussian assertions concern standardized variables; their unstandardized disorder variance tends to zero as \(r\downarrow0\). No publication-priority certification or independent scientific audit is asserted.

## References
1. P. Grange, *Voter model under stochastic resetting*, initial arXiv posting 18 July 2022, https://arxiv.org/abs/2207.08590 (local reset to fixed original spins and mean resolvent).
2. R. Pymar and N. Rivera, *On the stationary distribution of the noisy voter model*, initial arXiv posting 2 December 2021, https://arxiv.org/abs/2112.01478 (fresh-noise voter model on graphs).
3. *Fixed-opinion memory strictly enhances voter correlations on every finite ring*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-fixed-opinion-memory-strictly-enhances-voter-correlations-on-eve--6fc6c892fbed/RESULT.md (finite-cycle resolvent and equal-time correlations).
4. Standard continuous-time simple-random-walk local central limit theorem and Green-kernel estimates as used in the proof; these classical inputs are not attributed as original discoveries.
