# A sharp resource-lattice threshold for cooperation among long-lived stochastic commons

## Finding

Fix a finite resource–strategy continuous-time Markov chain with \(N\ge2\) agents, \(K\ge2\) indivisible resource units, and no immigration, resource restocking, or spontaneous strategy mutation. Let \(C_t\in\{0,\dots,N\}\) denote cooperators, let \(R_t\in\{0,\dots,K\}\) denote resource units, and let \(\tau=\inf\{t:R_t=0\}\). Set
\[
R_c=K\left(1-\frac{e_{cc}}b\right).
\]
Assume positive \(b,\nu,e_{cc},e_{cd},e_{dc},e_{dd}\), with \(0<e_{cc}<b<e_{dd}\), \(e_{cd}\ge e_{cc}\), and \(e_{dc}\ge e_{cc}\).

**Sharp conditional-selection theorem.** If \(R_c>1\), then for every deterministic initial state \(1\le C_0\le N\), \(1\le R_0\le K\), the conditional law satisfies, for some positive constants depending on parameters and initial state,
\[
\Pr(C_t\ne N\mid\tau>t)=O(e^{-\gamma t}),\qquad
\mathcal L(R_t\mid\tau>t)\longrightarrow\pi_c,
\]
with exponentially fast convergence in total variation. Here \(\pi_c\) is the unique quasi-stationary law of the pure-cooperator resource birth–death chain on \(\{1,\dots,K\}\), with birth rate \(\lambda_r=br(1-r/K)\) and death rate \(\mu_r=e_{cc}r\), killed upon reaching zero. If instead \(R_c\le1\), then for every initially mixed group \(1\le C_0<N\),
\[
\Pr(C_t=N,\ \tau>t)=0\quad\text{for all }t\ge0.
\]
Thus the integer-lattice feasibility threshold \(R_c>1\) is necessary and sufficient for *eventual conditional selection* of complete cooperation from every positive, initially nonpure-cooperator configuration. For every finite parameter choice in either regime, \(\tau<\infty\) almost surely, with an exponential extinction-time tail. These are claims about exceptionally long-lived realizations, not indefinite persistence.

## Assumptions and scope

The nonzero jumps from \((c,r)\), writing \(d=N-c\), are
\[
\begin{aligned}
(c,r)&\to(c,r+1)&&\text{at }br(1-r/K),\\
(c,r)&\to(c,r-1)&&\text{at }\frac r{N(N-1)}\big[e_{cc}c(c-1)+(e_{cd}+e_{dc})cd+e_{dd}d(d-1)\big],\\
(c,r)&\to(c+1,r)&&\text{at }\frac{\nu cd}{N}\left(1-\frac r{R_c}\right)^+,\\
(c,r)&\to(c-1,r)&&\text{at }\frac{\nu cd}{N}\frac r{R_c},
\end{aligned}
\]
where \(u^+=\max(u,0)\); jumps outside the state space are suppressed. Resource zero is absorbing in the resource coordinate, but strategy changes remain possible there. This is the exact finite-state microscopic model given in the initiating paper's main equation (1) and Supplemental Material equations (S1) and (S4), without invoking its diffusion approximation. Importantly, resource stock is *integer-valued*, so resource scarcity capable of inducing a cooperator transition requires at least one positive integer \(r<R_c\).

The comparison \(e_{cd},e_{dc}\ge e_{cc}\) rules out mixed pairs harvesting less than two cooperators. These hypotheses, positive strategy-update speed, and the finite population and resource lattice are essential to the stated uniform theorem. \(R_c=1\) belongs to the non-selection case.

## Proof

**1. Extinction and strategy-absorbing classes.** At every positive resource state, the resource death rate is at least \(e_{cc}r>0\), while every transition rate is finite. From any state, a path consisting of at most \(K\) resource deaths reaches \(r=0\). Finite state space permits a common strictly positive lower probability of this event in a fixed time block; the Markov property yields a geometric bound on \(\Pr(\tau>t)\), proving almost-sure extinction and an exponential tail. At \(r=0\), cooperator births are positive whenever \(0<c<N\), whereas cooperator losses vanish, so eventual absorption is at \((0,0)\) or \((N,0)\). Every invariant probability on the full finite chain is a mixture of those point masses.

**2. Reference Perron vector.** On positive resource states with \(c=N\), let \(Q_c\) be the killed generator with rates \(\lambda_r\) and \(\mu_r\) above. It is an irreducible Metzler matrix on \(r=1,\ldots,K\), with a simple spectral bound \(-\alpha<0\), positive right eigenvector \(v=(v_1,\ldots,v_K)\), and positive left eigenvector \(\pi_c\), normalized to sum to one. Put \(v_0=0\). The eigenvector satisfies
\[
\lambda_r(v_{r+1}-v_r)+\mu_r(v_{r-1}-v_r)=-\alpha v_r.
\]
The skip-free birth–death process preserves stochastic order in initial stock: two processes started with ordered resource stocks can be coupled without crossing. Consequently \(\Pr_r(\tau>t)\) is nondecreasing in \(r\) at every \(t\). Since \(e^{Q_ct}\mathbf1\sim e^{-\alpha t}v(\pi_c\mathbf1)/(\pi_cv)\), it follows that \(v_{r+1}\ge v_r\). The inequality is strict: if \(v_{r+1}=v_r>0\) at any \(r<K\), the eigenvalue equation at \(r+1\) would have nonnegative left-hand side (its downward term is zero and upward term nonnegative), contradicting its strictly negative right-hand side. Thus
\[
0=v_0<v_1<\cdots<v_K.
\]
This strict monotonicity is the key nonstandard comparison step; numerical eigensolver output is not used to infer it.

**3. Spectral separation.** For \(0\le c\le N\), every resource death rate is at least \(e_{cc}r\), as the weighted pair frequencies sum to one and every extraction coefficient is at least \(e_{cc}\). Denote by \(Q_d\) the killed \(c=0\) block and by \(Q_I\) the killed subgenerator on all \(1\le c\le N-1,1\le r\le K\), also killing trajectories upon a strategy exit to \(c=0\) or \(c=N\). Take the positive test function \(H(c,r)=v_r\). Comparing to \(Q_cv=-\alpha v\), the greater resource death rates can only decrease \(Q_IH\) and \(Q_dv\), since \(v_r-v_{r-1}>0\). Within \(Q_I\), all interior strategy jumps leave \(H\) unchanged, whereas killing a strategy jump leaving the interior subtracts its strictly positive rate times \(v_r\). In particular, at every \((c,r)\) with \(c=1\), the down-strategy exit rate \(\nu(N-1)r/(NR_c)\) is strictly positive. Hence
\[
Q_IH\le-\alpha H\quad\text{with at least one strict coordinate},
\qquad Q_dv<-\alpha v.
\]
When \(R_c>1\), the interior block is irreducible: resource deaths lead to \(r=1\), where both cooperator gains and losses are strictly possible at each interior \(c\), and resource births permit movement back to any \(r\). The irreducible Metzler Perron comparison (multiply the first inequality by a positive left Perron vector) gives
\[
s(Q_I)<-\alpha,\qquad s(Q_d)<-\alpha.
\]
The transient generator \(Q\), indexed by the \(K(N+1)\) states with \(r\ge1\), has these three blocks along its diagonal, with one-way exits from interior to the two strategy-fixation blocks. Its *unique dominant* eigenvalue is therefore \(-\alpha\), carried by the all-cooperator block; the remaining spectrum lies strictly to the left.

**4. Reachability and conditional convergence.** From every state with \(c\ge1\) and \(r\ge1\), a finite positive-probability path of resource deaths leads to \(r=1\) without strategy change. Because \(R_c>1\), at \(r=1\) every successive \(c\to c+1\) jump up to \(c=N\) has strictly positive rate, so the dominant pure-cooperator block is accessible. Consequently the coefficient of its Perron mode in \(\Pr_{c,r}((C_t,R_t)\in\cdot,\tau>t)\) is positive. Finite-dimensional Jordan decomposition and the strict spectral gap imply exponential convergence of that positive measure, upon normalization by \(\Pr(\tau>t)\), to the distribution supported at \(c=N\) with resource marginal \(\pi_c\). This also proves the total-variation statement.

**5. Sharp converse.** If \(R_c\le1\), then every positive resource stock \(r\ge1\) has \((1-r/R_c)^+=0\). Hence no \(c\to c+1\) event can occur before \(\tau\). Starting with \(c<N\), the process cannot attain \(c=N\) while \(r>0\), proving the claimed obstruction. Both directions include the equality boundary without a limiting approximation.

## Verification

The accompanying standalone `verify.py` reconstructs the finite killed generators from the four jump-rate formulas, checks nonnegative off-diagonal entries, row sums and resource mortality, verifies strict dominance of the all-cooperator eigenvalue and strict monotonicity of its right Perron vector across **90** parameter families (\(N=2,\ldots,6\), \(K=2,\ldots,7\), \(e_{cc}=1/4,1/2,4/5\) with explicit fixed remaining rates), tests the exact-rational critical boundary, and compares finite-time conditional survival laws. Run with `python verify.py` (NumPy and SciPy required). These finite checks corroborate *but do not replace* the all-size analytic proof.

For example, fixing \(N=3\), \(b=\nu=1\), \(e_{cc}=e_{cd}=1/2\), and \(e_{dc}=e_{dd}=3/2\), capacity \(K=2\) gives \(R_c=1\) and bars any cooperator gain at positive resource. Capacity \(K=3\) gives \(R_c=3/2\) and the conditional all-cooperator probability from \((C_0,R_0)=(1,2)\) exceeds \(1-10^{-12}\) by \(t=60\) in the numerically evaluated generator. The asymptotic result follows from the proof rather than that example.

## Relationship to prior work

Caruso, Menegazzo, Latora, and Suweis [1] formulate the finite resource–strategy Markov process (Supplemental equations S1–S4), derive its diffusion approximation, and study noise-driven quasi-cycles over finite observational horizons. Their work provides the microscopic starting point, but does not state a conditional, infinite-time classification by the integer threshold \(K(1-e_{cc}/b)>1\).

McAvoy, Fraiman, Hauert, Wakeley, and Nowak [2] analyze fluctuating-size evolutionary public-goods populations, metastable cooperative and defective states, and quasi-stationarity; the qualitative prospect of cooperative communities surviving longer is already present. Their offspring-based Wright–Fisher system has neither this particular discrete common-resource transition law nor the scarcity gate \((1-r/R_c)^+\), so the sharp lattice gate and the conditional Yaglom limit for [1] are not implied by that paper. Chazottes, Collet, and Méléard [3] develop general quasi-stationary methods for multitype population models; such methods support the type of spectral reasoning here but do not supply the model-specific boundary and strict spectral comparison. Previously published resource-feedback results use distinct deterministic or discretely updated models [4]. These comparisons are literature-bounded, not a claim of universally established priority.

## Limitations

All resource trajectories eventually hit zero almost surely: conditioning on \(\tau>t\) for large \(t\) selects rare histories and is not the same as showing a sustainable long-term ecosystem. For large \(N,K\), transient oscillatory behavior can persist on biologically relevant timescales. No uniform-in-\(N,K\) spectral gap or extinction-time asymptotic is proved. The result assumes positive resource-linked mortality at every positive stock, no external replenishment, no mutation at strategy boundaries, finite \(N,K\), and the specified extraction-rate ordering. The theorem does not establish a Yaglom limit for an initial all-defector population; such populations remain in their own defector class. The spectral bound and its sharp resource threshold are mathematical properties of this specified CTMC only.

## References

1. S. C. Caruso, F. Menegazzo, V. Latora, S. Suweis, *Resonant Amplification of Demographic Noise in Stochastic Common-Pool Resource Dynamics*, arXiv:2610.41830v1, first posted 2026-10-30, https://arxiv.org/abs/2610.41830 .
2. A. McAvoy, N. Fraiman, C. Hauert, J. Wakeley, M. A. Nowak, *Public goods games in populations with fluctuating size*, Theoretical Population Biology **121** (2018), 72–84, https://doi.org/10.1016/j.tpb.2018.01.004 .
3. J.-R. Chazottes, P. Collet, S. Méléard, *On time scales and quasi-stationary distributions for multitype birth-and-death processes*, arXiv:1702.05369, https://arxiv.org/abs/1702.05369 .
4. Related resource-feedback results at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-attainable-cooperation-interval-and-payoff-independent-res--1b85fc8baee7 and https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-greed-dependent-extinction-boundary-in-an-allee-common-poo--1e50ea949486 .
