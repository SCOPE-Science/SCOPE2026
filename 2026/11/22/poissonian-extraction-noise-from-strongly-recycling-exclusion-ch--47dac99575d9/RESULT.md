# Poissonian extraction noise from strongly recycling exclusion chains

## Finding
Fix an integer \(L\ge 2\) and rates \(\alpha,\beta>0\). In the continuous-time, open, locally resetting totally asymmetric exclusion chain described below, let \(N_r(t)\) count particle extractions at the right reservoir by physical time \(t\). Start at the configuration with exactly site 1 occupied. With rightward hop rate 1 and reset rate \(r\), define
\[
c_L=\begin{cases}\alpha+\beta,&L=2,\\\alpha,&L\ge3.\end{cases}
\]
Then, as \(r\to\infty\), the complete counting process \(\{N_r(rt):t\ge0\}\) converges in distribution, in the Skorokhod \(J_1\) topology on every finite time interval, to a homogeneous Poisson process with rate \(c_L\). The same conclusion holds from the stationary initial law. In particular, for every fixed \(t>0\) and nonnegative integer \(m\),
\[
\lim_{r\to\infty}\Pr[N_r(rt)=m]=e^{-c_Lt}\frac{(c_Lt)^m}{m!}.
\]
If \(J_r\) and \(V_r\) respectively denote the stationary mean and asymptotic variance rates of the extraction count,
\[
J_r=\lim_{T\to\infty}\frac{\mathbb E N_r(T)}T,
\quad V_r=\lim_{T\to\infty}\frac{\operatorname{Var}N_r(T)}T,
\]
then \(rJ_r\to c_L\), \(rV_r\to c_L\), and the long-time Fano ratio \(V_r/J_r\to1\). These are **sequential** long-time and large-reset limits: uniformity when \(L\) grows with \(r\) is not claimed. The mean-current first-order law is previously established; the contribution assessed here is convergence of the *full extraction point process* and of its long-time noise.

## Assumptions and scope
The state is \(\eta=(\eta_1,\ldots,\eta_L)\in\{0,1\}^L\). Injection changes \(\eta_1=0\) to 1 at rate \(\alpha\). If \(\eta_L=1\), extraction changes it to 0 at rate \(\beta\), incrementing \(N_r\) by one. Each occupied \(i<L\) hops to the vacant site \(i+1\) at rate 1. Each occupied \(i>1\), *provided site 1 is vacant*, moves instantaneously to site 1 at rate \(r\), independently of other eligible sites. All clocks are independent. No global resetting or particle annihilation is performed. Positive rates make the finite-state chain irreducible. The initial state is \(e_1=(1,0,\ldots,0)\), unless stationarity is specified.

## Proof
**1. A regenerative cycle.** Every return to \(e_1\) after at least one transition is a genuine regeneration, since clocks are exponential. Initially the only possible transition out of \(e_1\) is the unit-rate hop to \(e_2=(0,1,0,\ldots,0)\). Write \(C_r\) for the duration, including this first exponential waiting time, of one \(e_1\)-to-\(e_1\) cycle and \(M_r\) for its number of extractions. Successive pairs \((C_r,M_r)\) are independent and identically distributed.

At \(e_2\), the competing transitions are resetting to \(e_1\) at rate \(r\), injection at rate \(\alpha\), and either extraction at rate \(\beta\) (if \(L=2\)) or a right hop at rate 1 (if \(L\ge3\)). An injection creates two particles and necessarily entails at least one extraction before the chain can return to a one-particle configuration \(e_1\): all resets and internal hops conserve particle number. For \(L=2\), a direct extraction from \(e_2\) also gives exactly one exit, after which the empty chain returns to \(e_1\) by injection.

For \(L\ge3\), reaching \(e_3\) from \(e_2\) before reset has probability \(O(r^{-1})\); from \(e_3\), an extraction or injection before the next reset has probability \(O(r^{-1})\), because the total nonreset rate is bounded for fixed \(L,\alpha,\beta\). Thus this secondary channel produces an extraction with probability \(O(r^{-2})\). Consequently,
\[
\Pr(M_r\ge1)=\frac{c_L}{r}+O(r^{-2}).\tag{1}
\]

**2. Uniform control of exceptional cycles.** A state with site 1 empty and at least one other particle has at least one reset transition, with total rate at least \(r\), into a state with site 1 occupied. A finite collection of such fast states therefore has holding times \(O(r^{-1})\). After collapsing these fast states by their eventual reset outcomes, the limiting finite chain from any state with at least two particles reaches a configuration with one fewer particle: starting from occupied site 1, move the rightmost particle successively right until it exits; these are ordinary hops followed by extraction and never require site 1 to become vacant. Such a path has probability bounded below independently of \(r\) (for fixed \(L,\alpha,\beta\)). Repetition reaches \(e_1\). Standard finite-state absorption estimates, or the resolvent of this explicitly described collapsed chain, therefore give uniform bounds on the first three moments of the return time to \(e_1\) from every state reached by a nonreset transition when \(r\) is sufficiently large.

In particular, on entering a two-particle state via the rare injection above, the expected number of subsequent excursions with site 1 vacant is bounded uniformly. Each such excursion has injection probability at most \(\alpha/r\), so the conditional probability of creating a third particle before the first extraction is \(O(r^{-1})\). Two extractions before the cycle ends require at least one such additional injection. Uniform finite-state moment bounds also control the number of extractions per such exceptional cycle, yielding
\[
\Pr(M_r\ge2)=O(r^{-2}),\quad
\mathbb E M_r=\frac{c_L}{r}+O(r^{-2}),\quad
\mathbb E M_r^2=\frac{c_L}{r}+O(r^{-2}),\tag{2}
\]
\[
\mathbb E C_r=1+O(r^{-1}),\quad
\sup_{r\ge r_0}\mathbb E C_r^3<\infty,\quad
\mathbb E(M_r C_r)=O(r^{-1}).\tag{3}
\]
The \(1\) in the mean cycle length comes from the initial unit-rate hop; ordinary cycles return after a further \(O(r^{-1})\) time.

**3. Poisson process limit.** On physical time interval \([0,rt]\), the renewal counting theorem and uniform second moments in (3) give \(rt+o_{\Pr}(r)\) complete regeneration cycles, uniformly for \(t\) in compact intervals. Their independent indicator marks \(\mathbf1_{\{M_r\ge1\}}\) have probability \(c_L/r+O(r^{-2})\). Bernoulli rare-event convergence gives a rate-\(c_L\) Poisson process on the time scale \(t\), and the renewal time change is asymptotically the identity. By (2), the probability of any cycle carrying two or more exits among \(O(r)\) cycles is \(O(r^{-1})\). Uniform cycle-length moments ensure their scaled duration vanishes in probability; thus actual exit times and cycle markers agree in the \(J_1\) limit.

For a stationary start, the stationary configuration converges to \(e_1\) as \(r\to\infty\): at stationarity, the probability of an empty-first-site state with downstream particles is \(O(r^{-1})\); collapsing fast resets leaves \(e_1\) as the unique recurrent state because any multi-particle configuration can lose its rightmost particle at the exit. Therefore the initial transient is negligible on the \(r\)-time scale, and the same limit follows.

**4. Long-time noise.** The regenerative-reward formulas, valid for every fixed \(r\), are
\[
J_r=\frac{\mathbb E M_r}{\mathbb E C_r},\qquad
V_r=\frac{\mathbb E[(M_r-J_r C_r)^2]}{\mathbb E C_r}.
\]
Substitution of (2)–(3) gives \(rJ_r\to c_L\), \(rV_r\to c_L\) and \(V_r/J_r\to1\), proving the claim.

## Verification
Run `python CHECKER.py` in the same folder as this document, with NumPy and SciPy installed. It constructs the full \(2^L\)-state continuous-time generator, independently solves for the stationary distribution, and computes the current-noise variance from the tilted-generator Poisson equation \(Qh=J\mathbf1-B\mathbf1\). Cases \(L=2,3,4\) with several positive boundary rates and increasingly large reset rates test approach to the asserted current coefficient and unit Fano ratio. A separate exact two-site rational current formula is also checked. This finite computation does **not** certify the all-\(L\) regenerative estimates or the process-level limit.

## Relationship to prior work
Pelizzola and Pretti introduced and analyzed precisely the local-reset open-TASEP model, mainly via mean-field stationary phase diagrams and kinetic Monte Carlo in thermodynamic scaling (Journal of Physics A 55 (2022), 454001; accessible arXiv copy 2402.13698). Nagar and Gupta's 2023 review treats related local-reset exclusion processes and their stationary profiles. The established *finite-chain* strong-reset **mean-current** asymptotics \(J_r\sim c_L/r\) already precede this result and are not asserted as novel. Published finite-chain covariance-reversal results concern one-time occupation correlations. None of those statements implies the present full extraction counting-process convergence, absence of surviving compound-Poisson bursts, or long-time Fano limit. The comparison is model-specific, not a claim of global priority.

## Limitations
Finite \(L\) is fixed before taking \(r\to\infty\); no joint growing-size regime or finite-\(r\) exact counting law is proved. The process-level convergence is for bounded scaled time windows; the Fano statement separately takes the long observation-time limit at each fixed \(r\). The rate of convergence depends on \(L,\alpha,\beta\), and no uniform constant over these parameters is claimed. Numerical checks support but do not prove the full parameter result. The possibility of an unindexed equivalent counting-statistics theorem is a literature risk.

## References
1. A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, Journal of Physics A: Mathematical and Theoretical 55 (2022), 454001, DOI: 10.1088/1751-8121/ac9d72. Freely readable version: https://arxiv.org/abs/2402.13698. Author manuscript availability documented at https://iris.polito.it/handle/11583/2973072 (14 November 2022).
2. A. Nagar and S. Gupta, *Stochastic resetting in interacting particle systems: A review*, Journal of Physics A 56 (2023), 283001; https://arxiv.org/abs/2305.16955.
3. N. Bhatia and A. K. Gupta, *Totally asymmetric simple exclusion process with local resetting in a resource-constrained environment*, Physical Review E 109 (2024), 024109, DOI: 10.1103/PhysRevE.109.024109 (different reservoir model).
