# Invisible stationary heterogeneity and irreversible circulation in Fermi public-goods imitation

## Finding

For the well-mixed heterogeneous public-goods game with symmetric mutation and pairwise Fermi imitation, the finite action-profile chain is reversible **if and only if all individual contribution costs are equal** (provided imitation and selection are nonzero). This holds for every number of players \(N\ge 2\). In the two-player case a stronger observational phenomenon occurs: the **entire stationary action-profile distribution depends only on the sum of the two Fermi cooperation-acceptance probabilities**, but unequal costs generate a nonzero oriented stationary probability current. Thus an unequal-cost system and an equal-cost system can have exactly the same stationary snapshot distribution yet different time-reversal properties.

## Assumptions and scope

Let \(N\ge 2\), \(c_i>0\), \(\beta>0\), and \(0<\eta<1\). Each player chooses \(C\) or \(D\). For an action profile with cooperator set \(S\subseteq\{1,\ldots,N\}\), individual payoffs are

\[\pi_i(S)=R(S)-c_i\mathbf{1}_{\{i\in S\}},\]

where \(R(S)\) is **the same shared return for every player in that profile**; it may depend arbitrarily on \(S\). The linear public-goods instance is \(R(S)=r\sum_{j\in S}c_j/N\), for any positive return multiplier \(r\).

In one discrete update, choose a focal player uniformly. With probability \(\eta\), reset the focal action to an independent fair choice between \(C\) and \(D\). Otherwise choose uniformly one of the other \(N-1\) players and copy that player's action with probability \([1+\exp(\beta(\pi_i-\pi_j))]^{-1}\). This is the symmetric-mutation pairwise Fermi rule, and includes a self-loop. Define

\[p_i=\frac{1}{1+e^{\beta c_i}},\qquad q_i=1-p_i,\qquad u=\frac{\eta}{2N},\qquad v=\frac{1-\eta}{N(N-1)}.\]

In particular, \(0<p_i<1/2\). For \(i\notin S\) and \(i\in S\) respectively, the exact off-diagonal transitions are

\[P(S,S\cup\{i\})=u+v\sum_{j\in S}p_j,\qquad P(S,S\setminus\{i\})=u+v(N-|S|)q_i.\]

No other off-diagonal transitions occur. Positive mutation makes the chain irreducible and aperiodic, with a unique positive stationary distribution.

## Proof

**Part 1: universal sharp reversibility classification.** Fix distinct players \(i,j\) and let \(B=\{1,\ldots,N\}\setminus\{i,j\}\), \(A=u+v\sum_{k\in B}p_k\). Consider the four-state elementary cycle

\[B\longrightarrow B\cup\{i\}\longrightarrow B\cup\{i,j\}\longrightarrow B\cup\{j\}\longrightarrow B.\]

The ratio of the product of its forward transition probabilities to the backward product is exactly

\[\mathcal R_{ij}=\frac{(A+vp_i)(u+vq_j)}{(A+vp_j)(u+vq_i)}.\]

All factors are strictly positive. Since \(q_i=1-p_i\), it follows by strict factor comparison that \(\mathcal R_{ij}>1\) precisely when \(p_i>p_j\), and \(\mathcal R_{ij}=1\) precisely when \(p_i=p_j\). The function \(c\mapsto[1+e^{\beta c}]^{-1}\) is strictly decreasing, so unequal costs produce a cycle violating Kolmogorov's necessary criterion for reversibility. Consequently reversibility forces all \(c_i\) to be equal.

Conversely, when every cost is \(c\), write \(p=p_i\) and \(q=1-p\). The transition probability for adding a specified cooperator to a \(k\)-cooperator configuration is \(u+vkp\), and the probability for removing that cooperator from the resulting configuration is \(u+v(N-k-1)q\). Put \(w_0=1\) and

\[w_{k+1}=w_k\frac{u+vkp}{u+v(N-k-1)q}\quad(0\le k<N).\]

Assign stationary probability \(w_{|S|}/Z\) to each labeled state, where \(Z=\sum_{k=0}^N\binom Nk w_k\). On every edge between configurations of sizes \(k\) and \(k+1\), the displayed recurrence gives detailed balance. These are all the edges, proving reversibility and the stated necessary-and-sufficient condition.

**Part 2: exact two-player stationary law and hidden current.** For \(N=2\), denote \(00=\varnothing\), \(10=\{1\}\), \(01=\{2\}\), and \(11=\{1,2\}\). The exact stationary distribution is

\[\begin{aligned}
\rho_{00}&=\frac{2u+v(q_1+q_2)}{2(4u+v)},\\
\rho_{10}&=\rho_{01}=\frac{u}{4u+v},\\
\rho_{11}&=\frac{2u+v(p_1+p_2)}{2(4u+v)}.
\end{aligned}\]

These positive probabilities sum to one. For each singleton state, incoming flow is \(u(\rho_{00}+\rho_{11})\) and outgoing flow is \((2u+v)\rho_{10}\) or \((2u+v)\rho_{01}\), respectively, so the singleton stationarity equations hold. The \(00\) and \(11\) balances follow by direct substitution, proving the formula by uniqueness of stationarity. This law depends only on \(p_1+p_2\), and in particular each labeled player has the same stationary cooperation probability \(\rho_{11}+u/(4u+v)\).

Orient the square \(00\to10\to11\to01\to00\). Its stationary edge current (positive in this orientation) is

\[J=\rho_{00}P(00,10)-\rho_{10}P(10,00)=\frac{uv(p_1-p_2)}{2(4u+v)}.\]

Stationarity forces this same signed flow around all four oriented edges. Thus \(J\ne0\) exactly when contributions differ, while the stationary distribution cannot detect the contrast if \(p_1+p_2\) is held fixed. The cycle affinity is

\[\mathcal A=\log\frac{(u+vp_1)(u+vq_2)}{(u+vp_2)(u+vq_1)},\]

and \(J\mathcal A>0\) whenever costs differ. In the standard finite-chain entropy-production convention, \(J\mathcal A\) is the positive per-update entropy production for this four-state cycle.

**Exact observational-equivalence example.** Take \(\eta=1/5\), \(\beta=1\), and unequal costs \((c_1,c_2)=(\log3,\log2)\), giving \((p_1,p_2)=(1/4,1/3)\), \(u=1/20\), \(v=2/5\). Then

\[(\rho_{00},\rho_{10},\rho_{01},\rho_{11})=(5/9,1/12,1/12,5/18),\qquad J=-1/720,\qquad \mathcal R_{12}=57/77.\]

The homogeneous-cost model \(c_1=c_2=\log(17/7)\), for which \(p_1=p_2=7/24\), has *exactly the same four stationary probabilities* but \(J=0\). Both models obey the specified positive-cost assumptions.

## Verification

The companion script `verify_finite_chain.py` reconstructs exact transition matrices with Python's rational arithmetic and checks every row sum, the four-cycle product ratio, the explicit stationary distribution, current, and homogeneous detailed-balance identities. It tests both equal and unequal contributions for two through five players. Run `python3 verify_finite_chain.py`; it requires only the Python standard library. The checker is a finite consistency test; the theorem for all \(N\ge2\) follows from the analytic proof above.

## Relationship to prior work

Foster, Knight and Krapohl's *The Cooperation Ceiling: Extrinsic Population Dynamics and the Intrinsic Escape* defines the heterogeneous public-goods Fermi-mutation process and proves an upper bound on mean cooperation from payoff domination. Its main results do not provide the sharp reversibility classification or the exact stationary-snapshot/current separation above. Related work on introspection dynamics with mutation proves a product-form stationary law for that **different, counterfactual-self-comparison update rule**; it does not imply reversible Fermi imitation. Reversibility of noisy logit response in potential games likewise concerns a different update kernel. The Kolmogorov cycle criterion is standard; the present contribution is its exact specialization and the paired stationary-indistinguishability phenomenon for this particular source model.

## Limitations

The result assumes complete well-mixed pairwise sampling, a common gross return across players, fixed positive contributions, identical fair mutation probabilities, and strictly positive selection intensity. It does not characterize mutation-free fixation, network-constrained imitation, player-specific mutation, or nonlinear contributions with player-specific shared returns. Equality of snapshot distributions does not imply equality of transition laws or time-correlations. The research finding is literature-bounded and not independently audited; other historical sources could contain equivalent statements.

## References

1. H. Foster, V. Knight and S. Krapohl, *The Cooperation Ceiling: Extrinsic Population Dynamics and the Intrinsic Escape*, arXiv:2606.31740 (first posted 30 June 2026), https://arxiv.org/abs/2606.31740.
2. H. Foster, V. Knight and S. Krapohl, *Introspection dynamics with mutation in additive games*, Dynamic Games and Applications (2026), https://doi.org/10.1007/s13235-026-00715-0.
3. V. Auletta, D. Ferraioli, F. Pasquale, P. Penna and G. Persiano, *Convergence to Equilibrium of Logit Dynamics for Strategic Games*, arXiv:1212.1884 (2012), https://arxiv.org/abs/1212.1884.
4. Kolmogorov's criterion for reversibility of finite Markov chains (standard Markov-chain theorem), https://en.wikipedia.org/wiki/Kolmogorov%27s_criterion.
