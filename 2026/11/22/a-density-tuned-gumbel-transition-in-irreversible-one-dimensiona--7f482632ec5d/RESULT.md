# A density-tuned Gumbel transition in irreversible one-dimensional spin ordering

## Finding
For a periodic one-dimensional \(\delta\)-Ising chain in kinetic sector \(Q^{(1)}(0,2)\), with independently initialized plus-spin probability \(p\in(0,1)\), there is a sharp **three-regime law** for the time \(T_L\) until the first all-plus state. Conditional on at least one plus spin initially (necessary because the all-minus state is absorbing), the following statements hold in continuous time with independent unit-rate site clocks; they also hold when time is measured in Monte Carlo sweeps of the random-sequential discrete update rule.

Set \(\lambda_p=\min\{2p,1\}\). For fixed \(p\), put
\[
 b_{L,p}=\begin{cases}
 \dfrac{\log L+\log\left(\dfrac{p(1-p)^2}{1-2p}\right)}{2p},&0<p<\tfrac12,\\[6pt]
 \log L+\log\log L-\log 8,&p=\tfrac12,\\[4pt]
 \log L+\log\left(\dfrac{p^2(1-p)}{2p-1}\right),&\tfrac12<p<1.
 \end{cases}
\]
Then, for every real \(x\),
\[
 \lim_{L\to\infty}\Pr\!\left\{\lambda_p(T_L-b_{L,p})\le x\mid\text{at least one initial plus spin}\right\}=\exp(-e^{-x}). \tag{1}
\]
In particular, the critical initial density \(p=1/2\) creates an additional \(\log\log L\) ordering delay, which is absent for any other fixed density.

The crossover persists in a sharp density window. Fix any real \(a\) and use the triangular initial densities \(p_L=1/2+a/\log L\), for all sufficiently large \(L\). Define
\[
 w(a)=\begin{cases}(1-e^{-2a})/(2a),&a\ne0,\\1,&a=0,\end{cases}
 \quad c_L(a)=\log L+\log\log L-\log8+\log w(a).
\]
Then, for every real \(x\),
\[
 \lim_{L\to\infty}\Pr\{T_L\le c_L(a)+x\mid\text{at least one initial plus spin}\}=\exp(-e^{-x}). \tag{2}
\]
This resolves the crossover uniformly for each fixed finite detuning \(a\), without claiming uniformity for an unbounded family of detunings.

## Assumptions and scope
The system is a ring of \(L\ge3\) spins. A minus spin flips irreversibly to plus at rate one if at least one adjacent spin is plus; a plus spin never flips. This is precisely the spin-flip rule of \(Q^{(1)}(0,2)\) in the source paper. The initial states are independent Bernoulli spins, with \(p\) (or \(p_L\)) the probability of plus, independent of the site clocks. Every spin is updated at rate one; continuous-time units therefore equal Monte Carlo sweep units asymptotically. The event of no initial plus spin is excluded in (1)–(2): that event has probability \((1-p)^L\), and the ordering time would otherwise be infinite. We assume strictly positive initial densities bounded away from zero and one for the triangular-window statement.

A minus run of initial length \(k\ge1\) bounded by plus spins on both sides shrinks by a single flip at rate two while its length is at least two, and by a single rate-one flip when only one minus spin remains. Accordingly its lifetime \(H_k\) is distributed as a sum of \(k-1\) independent \(\operatorname{Exp}(2)\) variables and one independent \(\operatorname{Exp}(1)\) variable. Different initial runs have independent lifetimes, because a plus spin cannot revert and the site clocks are independent.

## Proof
**1. Exact lifetime distribution of an initially geometric minus run.** In an infinite iid Bernoulli spin sequence, the length \(K\) of a minus run immediately following a plus spin, conditional on being nonempty, is geometric on the positive integers with \(\Pr(K=k)=p(1-p)^{k-1}\). Conditional on \(K=k\), independence of the exponential waiting times gives
\[
 \mathbb E(e^{-sH_K}\mid K=k)=(1+s)^{-1}\left(\frac{2}{s+2}\right)^{k-1},\qquad s\ge0.
\]
Summing the geometric series gives the exact Laplace transform
\[
 \mathbb E(e^{-sH_K})=\frac{p(s+2)}{(s+1)(s+2p)}.\tag{3}
\]
Its corresponding survival probability is
\[
 R_p(t)=\Pr(H_K>t)=
 \begin{cases}
 \dfrac{p e^{-t}-(1-p)e^{-2pt}}{2p-1},&p\ne\tfrac12,\\[6pt]
 e^{-t}\left(1+\dfrac t2\right),&p=\tfrac12,
 \end{cases}\qquad t\ge0.\tag{4}
\]
At \(p=1/2\), the Laplace transform has a double pole at \(s=-1\); that pole collision is the origin of the extra \(\log\log L\) term.

**2. Renewal decomposition and the maximum law.** Read the initial Bernoulli configuration from a fixed cut. Except for the possible minus run that crosses the cut, its full minus runs are represented by alternate iid plus/minus runs. Each plus-run length is geometric with parameter \(1-p\), each subsequent minus-run length is geometric with parameter \(p\), and each plus/minus cycle has mean length
\[
 \mathbb E[\text{cycle length}]=\frac1{1-p}+\frac1p=\frac1{p(1-p)}.
\]
The renewal law of large numbers therefore shows that the number \(N_L\) of full minus runs obeys \(N_L/L\to p(1-p)\) in probability. For triangular \(p_L\to1/2\), the same limit is \(1/4\) by a triangular-array law of large numbers, since the geometric cycle lengths have uniformly bounded second moments in a neighborhood of one half. Conditional on the initial run lengths, the relevant lifetimes are independent, and the successive full-run lengths are independent even though the total number of runs is random. The possible run touching the fixed cut is formed from at most two geometric-tailed boundary fragments, and its length (hence extinction time) is tight uniformly in \(L\) for the specified parameter regimes. Its chance of surviving any times tending to infinity therefore vanishes.

For any \(\epsilon>0\), with probability tending to one, the set of complete domains contains at least \(\lfloor(p(1-p)-\epsilon)L\rfloor\) and at most \(\lceil(p(1-p)+\epsilon)L\rceil\) complete iid run lifetimes (with the evident \(1/4\) replacement in the triangular case). Thus its maximum is bounded, in distribution on a high-probability event, between maxima of those two deterministic numbers of iid copies of \(H_K\). If \(t_L\to\infty\) and \(Lp(1-p)R_p(t_L)\to\Lambda\), these iid maxima have distribution limits \(\exp[-(1\pm\epsilon/(p(1-p)))\Lambda]\). Send \(\epsilon\downarrow0\) and discard the vanishing cut-run and all-minus events to obtain
\[
 \Pr(T_L\le t_L)\longrightarrow e^{-\Lambda}.\tag{5}
\]
The analogous triangular-array version uses \(p_L\) and \(\epsilon\) about \(1/4\).

**3. Three fixed-density regimes.** For \(p<1/2\), (4) has the leading tail \(R_p(t)\sim (1-p)e^{-2pt}/(1-2p)\). For \(p>1/2\), its leading tail is \(R_p(t)\sim p e^{-t}/(2p-1)\). At \(p=1/2\), \(R_p(t)=e^{-t}(1+t/2)\), so the extra linear factor supplies a \(\log\log L\) centering term. In each case, substituting \(t_L=b_{L,p}+x/\lambda_p\) into the leading tail gives \(Lp(1-p)R_p(t_L)\to e^{-x}\). Equation (5) proves (1).

**4. Critical density window.** Write \(p_L=1/2+a/\log L\) and \(t_L=c_L(a)+x\). The exact tail (4), combined with \(t_L/\log L\to1\), yields
\[
 R_{p_L}(t_L)=e^{-t_L}\left[\frac{\log L}{2}w(a)+o(\log L)\right].
\]
The same estimate at \(a=0\) follows directly from the second line of (4). Because \(Lp_L(1-p_L)\sim L/4\), the specified \(c_L(a)\) makes the expected number of surviving complete runs tend to \(e^{-x}\), and the triangular version of (5) proves (2).

**5. Discrete-time Monte Carlo sweeps.** Poissonize the uniform sequential site-selection chain by adding independent exponential interattempt times of mean \(1/L\); this produces independent unit-rate site clocks. If \(J_L\) is the number of attempts to absorption, the Poissonized time minus \(J_L/L\), conditional on \(J_L\), has mean zero and variance \(J_L/L^2\). By the union bound on the \(O(L)\) domains and (4), the conditional mean Poissonized ordering time is \(O(\log L)\) for every fixed \(p\in(0,1)\) and for \(p_L\to1/2\). Therefore \(\mathbb E[J_L\mid\text{initial plus}]=O(L\log L)\). Chebyshev's inequality gives \(J_L/L-T_L=o_{\Pr}(1)\), which transfers all limits to the original sweep normalization.

## Verification
The self-contained `verify.py` computes (3)–(4) symbolically, checks the exact geometric mixture against transient matrix exponentials for the finite domain-length generator, and compares direct random sequential spin-flip simulations with the independent-domain construction. It also simulates genuinely Bernoulli-initial rings and checks asymptotic tail intensities, including the near-critical profile. Numerical agreement supports algebraic normalization but cannot establish (1) or (2); the preceding renewal and tail arguments supply the infinite-size proof.

## Relationship to prior work
Cao, Jiang and Zhang (arXiv:2610.36829, first public October 27, 2026), particularly their Section IV on ordering and Appendix C on domain-length recursions, define this exact irreversible kinetic sector and derive mean passage times for two deterministic starting patterns. These source results provide the process definition and finite-run ideas; they do not supply the iid Bernoulli full ordering-time distribution, its density-dependent three-regime classification, or the shrinking critical window.

Ottino-Löffler, Scott and Strogatz (2017) consider a one-seed network infection model with an infected-source-then-neighbor update mechanism, obtaining different fixation-time limits on a cycle. Their process and initialization do not imply the saturated site-update random-domain theorem. A related, publicly indexed result titled *A log-log extinction delay and a near-resonant Gumbel crossover in a directed epidemic* (2026) produces a similar \((1-e^{-\theta})/\theta\) function from competing recovery rates on a directed complete bipartite graph. Its full result and proof concern an initially fully infected source population, a receiver population with reinfections, and a shared random infection field. It does **not** assert the present irreversible one-dimensional spin-domain decomposition or its exact three fixed-density phases. The matched two-exponential resonance mechanism is acknowledged; the crossover functional form alone is not claimed as novel. Classical extreme-value theory supplies the iid-maximum step, not by itself the geometric-run lifetime law or the precise critical density and constants.

## Limitations
The result is restricted to irreversible, nearest-neighbor one-dimensional dynamics with iid initial spins and a fixed density or a fixed-width \(1/\log L\) critical detuning. The finite ring always has a permanently trapped all-minus initial condition with probability \((1-p)^L\); an unconditional finite-\(L\) mean time is therefore infinite unless this event is excluded. No claim is made for other kinetic sectors, correlated initial states, higher dimensions, the unbounded-detuning window, or uniform rates of distributional convergence. The finite-size Gumbel approximation can converge slowly near critical density. The result has undergone only the accompanying mathematical review, and historical coverage outside the examined sources cannot be excluded.

## References
1. Dehen Cao, Wei Jiang and Ya Zhang, *Kinetic Sectors and Nonequilibrium Dynamics in the \(\delta\)-Ising Model*, arXiv:2610.36829, first public 2026-10-27, https://arxiv.org/abs/2610.36829; full text https://borowiecki.dev/pdf/2610.36829.
2. E. Ottino-Löffler, J. G. Scott and S. H. Strogatz, *Takeover times for a simple model of network infection*, Physical Review E 96, 012313 (2017), https://doi.org/10.1103/PhysRevE.96.012313.
3. *A log-log extinction delay and a near-resonant Gumbel crossover in a directed epidemic*, public mathematical record, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-log-log-extinction-delay-and-a-near-resonant-gumbel-crossover--4fedaca5b99e.
4. Standard iid-maxima extreme-value argument, used explicitly in the proof above; no new general extreme-value theorem is claimed.
