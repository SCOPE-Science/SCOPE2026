# Hub persistence and sharp arm-balance extremals for voter dynamics on spider trees

## Finding

Let \(S(r_1,\ldots,r_k)\) be the finite tree obtained by attaching \(k\ge1\) paths of positive integer edge-lengths \(r_1,\ldots,r_k\) to one central vertex \(o\), with distinct paths otherwise disjoint. Put \(L=\sum_{i=1}^k r_i\). Initially \(o\) holds opinion \(1\) and every other vertex holds opinion \(0\). Each vertex has an independent rate-one Poisson clock and, upon ringing, copies a uniformly chosen neighbor. Define *center persistence* as the event that \(o\) never changes from \(1\), up to the almost surely finite time of unanimous consensus.

**Exact persistence and extremal allocation theorem.** For every \(k\ge1\) and all \(r_i\ge1\),
\[
\Pr(\text{center persistence})=p(r_1,\ldots,r_k)
=\prod_{i=1}^{k}\frac{k}{k+2r_i-1}.
\]
The probability that the eventual consensus opinion is \(1\) is, in contrast,
\[
\Pr(\text{consensus at }1)=\frac{k}{2L}.
\]

For \(k\ge2\) and fixed \(L\ge k\), let \(q=\lfloor L/k\rfloor\) and \(t=L-kq\). The exact minimum and maximum persistence over all compositions of \(L\) into \(k\) positive integer lengths are
\[
\begin{aligned}
p_{\min}&=\left(\frac{k}{k+2q-1}\right)^{k-t}
             \left(\frac{k}{k+2q+1}\right)^t,\\
p_{\max}&=\frac{k}{k+2L-2k+1}
             \left(\frac{k}{k+1}\right)^{k-1}.
\end{aligned}
\]
The minimizing multiset contains \(k-t\) copies of \(q\) and \(t\) copies of \(q+1\); the maximizing multiset contains \(k-1\) ones and one \(L-k+1\). Both characterizations are unique up to permuting the arms (and coincide when forced by \(L\)).

For fixed \(r\ge1\), the uniform-arm family satisfies
\[
p(\underbrace{r,\ldots,r}_{k\ \mathrm{arms}})
=\left(1+\frac{2r-1}{k}\right)^{-k}\longrightarrow e^{-(2r-1)}.
\]
For example, setting \(L=2k\) gives limiting probabilities \(e^{-3}\) for \(k\) arms of length two and \(e^{-1}/3\) for lengths \((k+1,1,\ldots,1)\), despite a common center degree \(k\), total vertex count \(2k+1\), and opinion-one fixation probability \(1/4\). At \(k=3,L=6\), the corresponding exact persistence values are \(1/8\) and \(27/160\).

## Assumptions and scope

All graph edges are unweighted and undirected. The center has degree \(k\); there are \(L\) edges and \(L+1\) vertices. Voter clocks run in continuous time at rate one *per vertex*, not per edge; neighbor selection is uniform. The initial configuration is a single opinion-one center and an entirely opinion-zero periphery. The probability is over clock rings and neighbor choices. A clock ring producing no opinion change does not count as a reversal. Persistence ends at consensus and is distinct from the event of eventual opinion-one fixation. The theorem is not asserted for arbitrary initial opinions or arbitrary attached motifs.

## Proof

**1. Freeze the center until its first reversal.** Give the center a fixed opinion \(1\) while evolving the path arms with the original Poisson clocks. The center's rate-one update clock is split, by independent Poisson thinning, into \(k\) independent rate-\(1/k\) clocks, one for each first vertex of an arm. If that first vertex currently holds \(0\), the corresponding center clock would cause the first reversal. If it holds \(1\), the clock produces no change. The path processes and these thinned center clocks are independent across arms. Therefore the event of never reversing factors into \(k\) separate survival events.

**2. A path has a single mobile interface.** On an arm of length \(r\), while the center stays \(1\), all opinion-one vertices form an initial consecutive prefix of length \(J\in\{0,1,\ldots,r\}\). This holds initially and is preserved because only the two vertices adjacent to its unique interface can change. State \(J=r\) is absorbing. When \(r\ge2\), the transitions are: \(0\to1\) at rate \(1/2\); for \(1\le J\le r-2\), \(J\to J\pm1\) each at rate \(1/2\); and \(r-1\to r-2\) at rate \(1/2\), \(r-1\to r\) at rate \(1\). For \(r=1\), the sole transition \(0\to1\) has rate \(1\). All other clock rings have no effect on \(J\).

**3. Exact local-time law.** For \(r\ge2\), write \(h_j\) for the probability, starting at interface position \(j\), of reaching \(r\) before revisiting \(0\). The boundary conditions are \(h_0=0\), \(h_r=1\). Harmonicity on the interior yields \(h_j=jh_1\) for \(1\le j\le r-1\), while the endpoint equation \(3h_{r-1}=h_{r-2}+2\) gives \(h_1=2/(2r-1)\). Every visit to \(J=0\) lasts an independent exponential time of rate \(1/2\). After departure, the probability of absorption at \(r\) before another visit to \(0\) is \(h_1\). The number of visits is geometric with success probability \(h_1\). Hence the total time \(T_r\) spent at \(J=0\) before absorption is exponentially distributed with rate \((1/2)h_1=1/(2r-1)\); equivalently,
\[
\mathbb E[e^{-sT_r}]=\frac{1}{1+s(2r-1)}\qquad(s\ge0).
\]
For \(r=1\), \(T_1\) is exponential of rate one, giving the same formula.

**4. Independent center-copy hazards.** A center clock labeled by this arm reverses the center only if it rings during the occupation time \(T_r\), precisely when its first vertex is zero. Given \(T_r\), the probability of no such ring is \(e^{-T_r/k}\). Averaging gives \(\mathbb E[e^{-T_r/k}]=k/(k+2r-1)\). Independence over arms proves the stated exact product. Every arm is absorbed at all ones in finite time under the frozen-center process, so surviving all hazards leads to all-one consensus without a center reversal. Conversely, a center that never reverses must survive every arm hazard.

**5. Eventual fixation.** The degree-weighted fraction of opinion-one vertices, \(\big(\sum_v\deg(v)\eta(v)\big)/(2L)\), is a bounded martingale under this vertex-update voter model. On a finite connected graph consensus is reached almost surely; at consensus the martingale equals the consensus opinion. Initially it is \(\deg(o)/(2L)=k/(2L)\). Optional convergence gives the exact fixation probability. This is not the persistence probability and depends only on \(k\) and \(L\).

**6. Sharp extremals and limits.** Taking logarithms of the product gives
\[
\log p=k\log k-\sum_{i=1}^k\log(k+2r_i-1).
\]
The function \(u\mapsto\log(k+2u-1)\) is strictly concave for \(u\ge1\). Whenever two lengths differ by at least two, transferring one unit from the larger to the smaller strictly increases the displayed sum and therefore strictly decreases \(p\). Iterating yields the unique balanced minimizer. Transferring one unit in the opposite direction while keeping both lengths positive strictly increases \(p\); iterating gives the unique maximizer with only one length greater than one. Substitution proves the exact extrema. The uniform-arm limit follows from \((1+a/k)^{-k}\to e^{-a}\). For \(L=2k\), substitute \(q=2,t=0\) and the extreme tuple into the formulas; the limits are \(e^{-3}\) and \(e^{-1}/3\). This completes the proof.

## Verification

Two independent, included programs verify finite instances without serving as substitutes for the all-size argument. The labelled-state continuous-time Markov chain checker (`direct_ctmc_check.py`) solves a killed-generator linear system on the entire peripheral opinion state space and agrees with the proposed rational value for 16 nonidentical arm profiles (up to seven peripheral vertices). The separate exact-rational interface-chain solver (`interface_extremal_check.py`) checks 108 arm-length/center-degree pairs and enumerates all positive arm-length compositions for 40 fixed-\((k,L)\) parameter choices. Their stdout records are embedded as `direct_ctmc_check.out` and `interface_extremal_check.out`. Code uses Python 3 and, for the first checker, NumPy and SciPy. Neither finite check proves an infinite claim; the six proof steps above do.

## Relationship to prior work

Ben-Naim, Frachebourg, and Krapivsky introduced and analyzed voter persistence and spin-change statistics in classical lattice and mean-field settings (1995 preprint). Sood and Redner studied fixation/consensus on heterogeneous graphs, including complete bipartite and star examples (2004 preprint). Pickering and Lim analyzed a spectral formulation for voter processes on complete and complete-bipartite graphs (2014 preprint). These works supply the model and relevant observables, but the inspected statements do not supply the spider-tree persistence product or its fixed-order-and-degree arm-balance extremal law. In particular, degree-weighted fixation does not imply no-flip persistence.

A separate exact hub-persistence result for *clique bouquets* treats a different graph class: its peripheral pieces are cliques directly adjacent to the center, not disjoint rooted paths. The star (all arms of length one) is shared. None of the previous clique-blade formula's nontrivial families has the path-interface rates used here, so the present length-dependent product and balancing extremal do not follow as a special case. This comparison supports distinctness but does not certify global historical priority.

## Limitations

The formula assumes independent rate-one vertex clocks, uniform neighbor copying, the single-center opinion-one initial state, and positive integer path lengths. It does not describe the entire distribution of reversal counts, time to consensus, other initial states, or general attached graph motifs. The infinite-family statements are analytically proved; finite computer checks provide reproducibility but not independent validation. Searches cannot exclude unindexed equivalent prior literature; no claim of independently audited priority is made.

## References

1. E. Ben-Naim, L. Frachebourg, P. L. Krapivsky, *Coarsening and Persistence in the Voter Model*, first arXiv version 1995-11-08, https://arxiv.org/abs/cond-mat/9511040 .
2. V. Sood and S. Redner, *Voter Model on Heterogeneous Graphs*, first arXiv version 2004-12-22, https://arxiv.org/abs/cond-mat/0412599 .
3. W. Pickering and C. Lim, *Solution of the Voter Model by Spectral Analysis*, first arXiv version 2014-08-09, https://arxiv.org/abs/1408.2130 .
