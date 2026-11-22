# A stationary immigration–death law for isolation at the dynamic connectivity threshold

## Finding

Fix \(x\in\mathbb R\) and let \(p_n=(\log n+x)/n\). On the complete graph with \(n\) labelled vertices, run independent rate-one Poisson refresh clocks on all edges; at each refresh, replace that edge's state by a fresh Bernoulli\((p_n)\) observation. Initialize every edge independently with the same Bernoulli\((p_n)\) law. Let \(I_n(s)\) count isolated vertices at physical time \(s\). For all fixed \(m\ge1\) and \(0\le t_1<\cdots<t_m<\infty\),

\[
\big(I_n(t_1/\log n),\ldots,I_n(t_m/\log n)\big)
\xrightarrow{d}\big(Z(t_1),\ldots,Z(t_m)\big),
\]

where \(Z\) is a stationary immigration–death process with immigration rate \(\lambda=e^{-x}\) and unit per-individual death rate; in particular its fixed-time distribution is \(\operatorname{Poisson}(\lambda)\).

The stronger *exact temporal-signature law* holds: for each nonempty subset \(H\subseteq\{1,\ldots,m\}\), let \(N_{n,H}\) count vertices isolated at exactly the observation indices in \(H\). The vector of all \(2^m-1\) such counts converges to independent Poisson variables. Their limiting means vanish unless \(H=[a,b]\cap\mathbb Z\) is an uninterrupted block, in which case the mean is

\[
\nu_{a,b}=\lambda e^{-(t_b-t_a)}\,
\begin{cases}1-e^{-(t_a-t_{a-1})},&a>1,\\1,&a=1\end{cases}
\begin{cases}1-e^{-(t_{b+1}-t_b)},&b<m,\\1,&b=m.\end{cases}
\]

Consequently, for fixed \(t\ge0\), the pair \((I_n(0),I_n(t/\log n))\) converges to a bivariate Poisson law with common intensity \(\lambda e^{-t}\) and two exclusive intensities \(\lambda(1-e^{-t})\). For \(C_n(s)\), the indicator that the graph at time \(s\) is connected, the same finite-dimensional convergence holds with the limit \(\mathbf1\{Z(t_j)=0\}\). Thus

\[
\lim_{n\to\infty}\Pr\{C_n(0)=C_n(t/\log n)=1\}=\exp\{-\lambda(2-e^{-t})\}.
\]

## Assumptions and scope

All graphs are simple, undirected, on the fixed labelled vertex set \(\{1,\ldots,n\}\). The limit is along sufficiently large \(n\) for which \(0<p_n<1\). Different unordered edges use independent stationary refresh processes, and every refresh selects a new independent Bernoulli state even if it equals the previous one. Every temporal observation instant \(t_j\) is fixed before \(n\to\infty\). Convergence is a statement about finite-dimensional random vectors, not weak convergence of entire sample paths. For \(m=1\), the sole block has mean \(\lambda\).

Define the *snapshot support* of a vertex \(v\) as the subset of indices at which its degree is zero. Only nonempty supports enter \(N_{n,H}\); a vertex never isolated at any selected time is not counted. The immigration–death process can be constructed in stationarity using \(\operatorname{Poisson}(\lambda)\) initial individuals with independent exponential unit lifetimes, plus independent rate-\(\lambda\) immigrants each with an independent exponential unit lifetime.

## Proof

**1. Exact joint isolation probability.** For any nonempty set \(S\) of observation indices, let \(s_1<\cdots<s_k\) be its ordered elements. The probability that one stationary edge is absent at *every* time in \(S\) equals

\[
q_n(S)=(1-p_n)\prod_{j=2}^{k}\left[1-p_n\left(1-e^{-(t_{s_j}-t_{s_{j-1}})/\log n}\right)\right].
\tag{1}
\]

Indeed, conditional on being absent at the earlier instant, the edge is still absent at the next instant with probability \(e^{-\Delta/\log n}+(1-e^{-\Delta/\log n})(1-p_n)\). The Markov property multiplies these conditional probabilities. If \(\operatorname{span}(S)=t_{s_k}-t_{s_1}\) (zero for a singleton), then \(n p_n=\log n+x\), and Taylor expansions for fixed \(S\) yield

\[
(n-1)\log q_n(S)=-\log n-x-\operatorname{span}(S)+o(1),\qquad
nq_n(S)^{n-1}\longrightarrow \lambda e^{-\operatorname{span}(S)}.
\tag{2}
\]

For distinct vertices \(v_1,\ldots,v_r\) and nonempty observation subsets \(S_1,\ldots,S_r\), their simultaneous requested isolation events have the **exact** probability

\[
\Pr\{v_i\text{ isolated at all indices in }S_i,\ 1\le i\le r\}
=\prod_{i=1}^r q_n(S_i)^{n-r}
\prod_{1\le i<j\le r}q_n(S_i\cup S_j).
\tag{3}
\]

Each of the \(n-r\) edges from a tagged vertex to an untagged vertex must be absent on its own required set; each edge between two tagged vertices must be absent on the union of their required sets. These edge requirements are independent. For fixed \(r\), \(q_n(S)\to1\), so (2)–(3) imply

\[
n^r\Pr\{v_i\text{ isolated at all indices in }S_i\text{ for each }i\}
\longrightarrow\prod_{i=1}^r \lambda e^{-\operatorname{span}(S_i)}.
\tag{4}
\]

**2. Exact temporal signatures.** To require a tagged vertex to be isolated at *exactly* the indices in a nonempty set \(H\), impose isolation at \(H\) and exclude isolation at each index outside \(H\). Inclusion–exclusion over these exclusions, together with (4), shows that, for distinct tagged vertices having prescribed supports \(H_1,\ldots,H_r\),

\[
n^r\Pr\{\text{tag }i\text{ has exact support }H_i\text{ for all }i\}
\longrightarrow \prod_{i=1}^r\nu_{H_i},
\quad
\nu_H=\lambda\sum_{S\supseteq H}(-1)^{|S\setminus H|}
 e^{-\operatorname{span}(S)}.
\tag{5}
\]

The function \(e^{-\operatorname{span}(S)}\) depends only on the *first and last* selected indices. Therefore, if \(H\) omits an index between its own first and last indices, inclusion–exclusion cancels exactly and \(\nu_H=0\). If \(H=\{a,a+1,\ldots,b\}\), every outside index further from the block's endpoints than its immediate neighboring indices can again be canceled pairwise. The remaining one-sided differences give precisely the displayed formula for \(\nu_{a,b}\). These means are nonnegative and their sum over blocks containing any fixed \(j\) is \(\lambda\).

Taking ordered distinct vertices to form any fixed mixed falling-factorial moment of the counts \((N_{n,H})_{H\ne\varnothing}\) and applying (5) shows that this moment tends to the product of the corresponding powers of \(\nu_H\). The joint Poisson distribution with independent coordinates has these mixed factorial moments and is moment-determinate. Tightness follows from the bounded first moments. Thus the entire finite vector of exact-signature counts converges to independent Poisson coordinates, with noncontiguous coordinates degenerating to zero.

**3. Identification of the limiting process.** In a stationary immigration–death process, any individual alive at a finite collection of sampled times must have a lifetime interval that covers one uninterrupted block of those times. Poisson thinning of the stationary Poisson population and of the independent Poisson immigration process makes the numbers with distinct sampled-time blocks independent Poisson. An individual existing at time \(t_a\) survives until \(t_b\) with probability \(e^{-(t_b-t_a)}\); for it to be absent at the previous observation if \(a>1\) contributes \(1-e^{-(t_a-t_{a-1})}\), by time reversibility in stationarity; absence at the next observation if \(b<m\) gives the corresponding forward-survival complement. This yields precisely \(\nu_{a,b}\). Since \(I_n\) is the sum of all signature counts containing the relevant index, its finite-dimensional distribution converges to that of \(Z\). The two-time bivariate Poisson decomposition and probability that both limiting counts vanish follow immediately.

**4. Connectivity.** For \(p_n=(\log n+x)/n\), the classical Erdős–Rényi connectivity theorem states that the probability of a disconnected graph with no isolated vertices tends to zero. Each observed snapshot has the stationary law \(G(n,p_n)\); a union bound over the fixed \(m\) snapshots gives the same assertion simultaneously for them all. Hence connectivity indicators agree with the zero-isolation indicators at all selected snapshots with probability tending to one. Their finite-dimensional limit is accordingly \(\mathbf1\{Z(t_j)=0\}\).

## Verification

Run `python3 check_isolation.py` using only the Python 3 standard library. It independently enumerates the two-snapshot states of every edge for small complete graphs, checking the exact tagged-vertex formula against direct rational probabilities. It also tests the limiting exact-support intensities at multiple sample times, the stationary marginal mass identity, the two-time covariance formula, and nonnegativity of temporal-block intensities. A run of the included program passed 347 deterministic assertions. These finite and numerical tests are consistency checks; the infinite theorem follows from (1)–(5), multivariate factorial moments, and the classical connectivity result.

## Relationship to prior work

Lubetzky and Steif, *Strong noise sensitivity and random graphs*, arXiv:1306.6373v1 (2013), Theorem 3.6, prove that minimum-degree and connectivity properties have a sharp **noise sensitivity/stability threshold** at refresh probability of order \(1/\log n\). Their critical-regime assertion is neither sensitivity nor stability; it does not state the explicit joint Poisson temporal-signature law, limiting immigration–death process, or the critical two-time connectivity probability. The present result supplies these quantitative descriptions on precisely that established scale, without claiming the scale itself as new.

Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132v1 (2015), proves broad **one-snapshot** Poisson approximation for isolation counts; one-time Poisson marginals cannot determine multi-time dependence. Clementi, Monti, Pasquale and Silvestri, *Information Spreading in Stationary Markovian Evolving Graphs*, arXiv:1103.0741v1 (2011), study **flooding times and expansion** in stationary evolving networks, not the rare temporal isolated-vertex signatures of a sparse complete-graph model. Related published results on static circle-geometric isolation and monotone bipartite edge-arrival completion concern different graph ensembles or different time evolution, and do not imply (5). The exact formulas here are checked by the included executable and historical uniqueness is not claimed.

## Limitations

The claim concerns only equilibrium independent-edge refreshing of Erdős–Rényi graphs, fixed real \(x\), fixed finitely many observation times, and the specified \(1/\log n\) acceleration. It does not establish functional process convergence, pathwise coupling, total-variation error rates for growing numbers of observations, or any statement about exceptional instants between observations. The classical connectivity-isolation equivalence is used as prior mathematical knowledge. Although major directly relevant sources were inspected, undetected historical priority or a stronger general multitime rare-event theorem remains possible. No independent validation has been conducted.

## References

1. E. Lubetzky and J. Steif, *Strong noise sensitivity and random graphs*, arXiv:1306.6373v1, 26 June 2013, Theorem 3.6. https://arxiv.org/abs/1306.6373
2. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132v1, 25 July 2015. https://arxiv.org/abs/1507.07132
3. A. Clementi, A. Monti, F. Pasquale and R. Silvestri, *Information Spreading in Stationary Markovian Evolving Graphs*, arXiv:1103.0741v1, 3 March 2011. https://arxiv.org/abs/1103.0741
4. Classical connectivity-isolation equivalence for \(G(n,(\log n+x)/n)\), as cited and used in Lubetzky–Steif, op. cit.
