# Poissonian extraction noise from strongly recycling exclusion chains

## Finding
Fix an integer \(L\ge2\) and rates \(\alpha,\beta>0\). In the continuous-time open exclusion chain with local reset specified below, let \(N_r(t)\) count right-boundary extractions by physical time \(t\), with \(N_r(0)=0\). Write
\[
c_L=\begin{cases}\alpha+\beta,&L=2,\\\alpha,&L\ge3.\end{cases}
\]
From the configuration \(e_1\) with only site 1 occupied, or from the stationary law, \((N_r(rt))_{0\le t\le H}\) converges in distribution in the Skorokhod \(J_1\) topology to a homogeneous Poisson counting process of rate \(c_L\), for every fixed \(H>0\), as \(r\to\infty\). In particular, for each fixed \(t>0\) and integer \(m\ge0\), its count probability tends to \(e^{-c_Lt}(c_Lt)^m/m!\).

From the stationary law, define the mean and variance rates \(J_r=\lim_{T\to\infty}T^{-1}\mathbb E N_r(T)\) and \(V_r=\lim_{T\to\infty}T^{-1}\operatorname{Var}N_r(T)\). Then \(rJ_r\to c_L\), \(rV_r\to c_L\), and \(V_r/J_r\to1\). The first-order mean-current formula is also given in [2]; the conclusions of interest here are the process and long-time variance limits. The large-reset limit in these variance-rate statements is taken after the long-time limit.

## Assumptions and scope
The state is \(\eta\in\{0,1\}^L\). A vacant site 1 receives a particle at rate \(\alpha\); an occupied site \(L\) loses its particle at rate \(\beta\), incrementing \(N_r\). An occupied site \(i<L\) sends its particle to a vacant site \(i+1\) at rate 1. Each occupied site \(i>1\) sends its particle to site 1 at rate \(r\) if site 1 is vacant. These are independent exponential transitions. The site-1 vacancy condition and separate reset rate for each eligible particle are essential. There is no global reset or particle annihilation. Here \(L,\alpha,\beta\) stay fixed.

## Proof

### 1. Uniform jump and time bounds
Use cycles from \(e_1\) to its first return after it leaves. They are iid, including their duration \(C_r\), reward \(M_r\) (number of extractions), and the locations of all extractions within the cycle. The departure is the rate-one hop to \(e_2\), where \(e_j\) denotes the configuration with just site \(j\) occupied.

There are constants \(K<\infty\), \(p>0\) such that from any state other than \(e_1\), the jump chain hits \(e_1\) within \(K\) transitions with probability at least \(p\), uniformly for \(r\ge1\). If site 1 is vacant and there are downstream particles, the next transition is a reset with probability at least \(r/(r+\alpha+\beta+L)\), and that transition occupies site 1. If the system is empty the next transition is injection to \(e_1\). From a state with site 1 occupied and other particles present, prescribe moving the rightmost particle to site \(L\) and then extracting it, repeatedly, without moving the particle at site 1. This takes at most \(L(L-1)\) steps and each prescribed transition has probability bounded below: the total rate along that path is bounded by \(L+\beta\) and the prescribed rate is either 1 or \(\beta\).

Iteration in blocks of \(K\) gives a uniform geometric tail for the number \(J\) of jumps to \(e_1\). Holding times given the jump path are independent exponentials with rates bounded below by \(\min(1,\alpha,\beta)>0\); this includes the initial holding at \(e_1\) in a full cycle. Thus return times and jump counts have uniformly bounded moments of each fixed order. At fixed \(r\) the same bounds give exponential tails (for time, use a sufficiently small exponential moment).

### 2. Rare rewards, including all sources of multiple extractions
At \(e_2\) the total rate is \(r+\alpha+\gamma\), where \(\gamma=\beta\) for \(L=2\) and \(\gamma=1\) otherwise. Reset returns to \(e_1\) with no reward. Injection creates two particles and guarantees at least one extraction by the return, by particle-number balance. When \(L=2\), a direct extraction at \(e_2\) gives exactly one reward, and the empty state then returns by injection. When \(L\ge3\), a hop to \(e_3\) is followed immediately by return to \(e_1\) on its next reset; the probability of a nonreset transition instead at \(e_3\) is \(O(1/r)\).

To control bursts after the initial injection, call a transition exceptional if it is nonreset and occurs with site 1 vacant and at least one downstream particle. Its conditional probability at any such jump is at most \((\alpha+\beta+L)/r\). Starting with two particles and site 1 occupied, if no exceptional transition occurs before return, all transitions from an occupied downstream configuration with site 1 vacant are resets. The system cannot inject another particle or extract with site 1 vacant, and the ordinary extraction reducing the population to one returns directly to \(e_1\). So there is exactly one reward. The exceptional condition also captures a lone downstream particle that exits before resetting: two extractions do not necessarily require an additional injection.

In fact, starting in any state other than \(e_1\), \(\mathbb E[J^q\mathbf1_{\{\text{exception before return}\}}]=O(r^{-1})\) for every fixed positive integer \(q\). To see this, split according to the index \(j\ge1\) of the first exceptional transition. The event of still being active before jump \(j\) has geometrically decreasing probability in \(j\). Given the history just before that jump, the probability of an exception is \(O(1/r)\); conditional on its destination the remaining jump count has bounded moments by Step 1. The contribution is bounded by a constant times \(r^{-1}(1+j^q)\Pr(J\ge j)\), which sums uniformly. Rewards are bounded by jump counts. This estimate applies to the post-injection path and also from \(e_3\), where a reward requires an exception before return. The rates of the first departure from \(e_2\), and the direct two-site exit when applicable, now give
\[
\Pr(M_r\ge1)=\frac{c_L}{r}+O(r^{-2}),\qquad
\mathbb E[M_r^q\mathbf1_{\{M_r\ge2\}}]=O(r^{-2})\quad(q=1,2).
\]
In particular \(\Pr(M_r\ge2)=O(r^{-2})\) and \(\mathbb E M_r,\mathbb E M_r^2=c_L/r+O(r^{-2})\), with the expansion for each moment separately.

The initial holding time has mean 1 and the holding at \(e_2\) has mean \((r+\alpha+\gamma)^{-1}\). Only a nonreset departure from \(e_2\), of probability \(O(1/r)\), adds further duration; its conditional moments are bounded by Step 1. Consequently
\[
\mathbb E C_r=1+O(r^{-1}),\qquad
\sup_{r\ge1}\mathbb E C_r^3<\infty,\qquad
\mathbb E(M_r C_r)=O(r^{-1}).
\]
For the mixed moment, rewards vanish on reset departures from \(e_2\). On the other departures the first two holding times retain their exponential laws conditional on the destination, and the remaining reward and duration have bounded second moments.

### 3. The counting-process limit
Index successive cycles by \(i\ge1\) and initially put one point at \(i/r\) if cycle \(i\) is marked by at least one exit. This is an iid Bernoulli lattice process with success probability \(c_L/r+O(r^{-2})\); its point process converges on bounded intervals to the Poisson point process of rate \(c_L\). For instance, counts on disjoint subintervals are independent binomials converging to the corresponding independent Poisson variables; equivalently the product of single-site Laplace factors converges by Riemann sums to the Poisson Laplace functional.

Let \(S_{r,i}\) be the physical end time of cycle \(i\). For every fixed \(U>0\), the maximal inequality for centered independent cycle durations, the uniform second-moment bound, and \(\mathbb E C_r\to1\) give
\[
\max_{i\le \lfloor rU\rfloor}|S_{r,i}/r-i/r|\xrightarrow{\Pr}0,\qquad S_{r,0}=0.
\]
No independence between a mark and its cycle duration is required for this estimate. Take \(U>H\); with high probability the first \(\lfloor rU\rfloor\) cycles cover \([0,rH]\), and none has two exits, by the rare-burst bound and the union bound. An actual exit lies between the two endpoints of its marked cycle, so all actual scaled exit times are uniformly within \(o_{\Pr}(1)\) of their lattice markers. The limiting Poisson process is simple and has no point at 0 or \(H\). In detail, discard events where any lattice marker lies within \(\delta\) of either endpoint, a probability bounded in the limit by \(O(\delta)\); on the remaining events, for sufficiently small displacement the ordered marker and actual jump times match in \([0,H]\). A piecewise linear increasing time change matching corresponding jumps and fixing the endpoints bounds their \(J_1\) distance by the maximal displacement. Taking \(\delta\downarrow0\) proves the limit.

For the stationary start, stationary cycle occupation gives \(\pi_r(e_1)=1/\mathbb E C_r\to1\), since the only time at \(e_1\) in a cycle is its initial rate-one holding time. The stationary path law differs in total variation from the \(e_1\)-start path law by at most \(1-\pi_r(e_1)\), by coupling the two when their initial states agree. Thus the same limit holds.

### 4. Sequential long-time variance
At each fixed \(r\) the regenerative rate formulas are
\[
J_r=\frac{\mathbb E M_r}{\mathbb E C_r},\qquad
V_r=\frac{\mathbb E[(M_r-J_r C_r)^2]}{\mathbb E C_r}.
\]
The finite moments required for the regenerative variance formula follow from Step 1, including for the delay to the first regeneration from stationarity. These formulas take the long-time limit before any limit in \(r\). Step 2 gives \(rJ_r\to c_L\); the mixed and duration terms in the centered square are \(O(r^{-2})\), whereas \(\mathbb E M_r^2=c_L/r+O(r^{-2})\). This yields \(rV_r\to c_L\) and, since \(c_L>0\), \(V_r/J_r\to1\).

## Verification
The accompanying `CHECKER.py` (NumPy/SciPy) constructs a finite continuous-time generator, solves the stationary equations, and tests the stationary current and long-time variance using the marked-generator Poisson equation. Its tests for \(L=2,3,4\), including a two-site rational current, are finite corroboration only. The uniform jump estimates, reward estimates, process convergence and all-fixed-\(L\) variance limit are analytic.

## Relationship to prior work and limitations
Pelizzola and Pretti [1] specify the same local reset and study stationary profiles, occupation correlations and lattice-size scaling. Their thermodynamic analysis is not used here as a source for the fixed-size mean-current coefficients. The separate fixed-size current result [2] gives both coefficients with \(O(r^{-2})\) errors; no priority ordering is asserted between the fixed-size results. Mean-current asymptotics alone do not control rare bursts, give process convergence or determine the long-time Fano ratio. No uniformity with growing \(L\), finite-reset counting law, or quantitative \(J_1\) rate is claimed. The prior-work comparison is bounded, not an exhaustive priority assertion.

## References
1. A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, J. Phys. A **55** (2022), 454001. [DOI](https://doi.org/10.1088/1751-8121/ac9d72); [arXiv:2402.13698](https://arxiv.org/abs/2402.13698).
2. *Universal strong-reset current and the two-site anomaly in an open exclusion chain*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-universal-strong-reset-current-and-the-two-site-anomaly-in-an-op--8c13e05907a3/RESULT.md).
