# A continuous Gumbel law for growing-memory Pólya contagion streaks

## Finding
Fix two strictly positive real parameters \(\alpha,\beta\), let \(c=\alpha+\beta\), and use the finite-reinforcement-memory Pólya binary sequence described below. For integer memory lengths \(M=M_n\) with
\[
 M\longrightarrow\infty,\qquad \frac{M^{\beta+3}\log n}{n}\longrightarrow0,
\]
define
\[
 q_M=\frac{\alpha+M}{c+M},\quad
 u_M=\frac{(\alpha)_M}{(c)_M},\quad
 \tau_M=-\log q_M,\quad
 b_{n,M}=M+\frac{\log[n u_M(1-q_M)]}{\tau_M}.
\]
Writing \(L_n\) for the longest streak of consecutive ones among \(Z_1,\ldots,Z_n\), we prove the *continuous* extreme-value limit
\[
 \mathbb P\{\tau_M(L_n-b_{n,M})\le x\}\longrightarrow\exp(-e^{-x})
 \qquad(x\in\mathbb R).
\]
For every sequence of integers \(k_n\ge M_n\) with \(n p_{k_n}\to\lambda\in(0,\infty)\), where
\[
 p_k=u_M(1-q_M)q_M^{k-M},
\]
the point process of times \(i/n\), \(2\le i\le n-k+1\), at which \(Z_{i-1}=0\) and \(Z_i=\cdots=Z_{i+k-1}=1\) converges on \((0,1)\) to homogeneous Poisson intensity \(\lambda\,dt\). Consequently, the absence probability of such starts tends to \(e^{-\lambda}\). The Gumbel law arises because \(\tau_M\to0\), removing the integer-lattice oscillation present when \(M\) is fixed.

## Assumptions and scope
For each \(n\), start an urn with red and black masses in ratio \(\alpha:\beta\), and add one unit of the sampled colour at each draw. Only the most recent \(M\) reinforcements remain after the first \(M\) draws. Equivalently, for \(t\le M\) use the classical Pólya predictive rule, and for \(t>M\),
\[
 \mathbb P(Z_t=1\mid Z_1,\ldots,Z_{t-1})
 =\frac{\alpha+Z_{t-1}+\cdots+Z_{t-M}}{c+M}.
\]
The first \(M\) draws provide the natural invariant initialization. Here \((a)_j=\prod_{h=0}^{j-1}(a+h)\) with \((a)_0=1\). The theorem concerns any fixed \(\alpha,\beta>0\) and any deterministic integer memory sequence satisfying the displayed growth hypothesis. A one means a universal-vertex arrival in the associated threshold-graph encoding; if a graph construction forces the last vertex universal, apply the result to the preceding unforced draws.

## Proof
**1. Stationarity and exact run probabilities.** Every ordered binary block \(w\in\{0,1\}^M\), with \(s\) ones, has probability
\[
 \pi_M(w)=\frac{(\alpha)_s(\beta)_{M-s}}{(c)_M}.
\]
This distribution is invariant under the order-\(M\) shift chain: the conditional predictive probability of the next one in the exchangeable \((M+1)\)-draw classical Pólya law is \((\alpha+s)/(c+M)\), precisely the finite-memory kernel. Hence every consecutive \(M\)-block has the displayed law. In particular, for \(k\ge M\),
\[
 \mathbb P(Z_i=\cdots=Z_{i+k-1}=1)=u_M q_M^{k-M},
\]
and, for \(i\ge2\), stationarity and subtraction of the \((k+1)\)-ones event yield
\[
 \mathbb P(A_i)=\mathbb P(Z_{i-1}=0,Z_i=\cdots=Z_{i+k-1}=1)
 =u_M(1-q_M)q_M^{k-M}=p_k.
\]
The gamma-ratio asymptotics give
\[
 u_M=\frac{\Gamma(c)}{\Gamma(\alpha)}M^{-\beta}(1+O(M^{-1})),\quad
 1-q_M=\frac{\beta}{M+c},\quad
 \tau_M\sim\frac{\beta}{M}.
\]

**2. Uniform mixing for growing \(M\).** Couple two order-\(M\) state chains started arbitrarily by applying the *same* independent uniform random variable at each subsequent update. If \(d_t\) denotes the probability of unequal bits at time \(t\), with the initial \(M\) coordinates indexed by nonpositive times, then for \(t\ge1\)
\[
 d_t\le\frac1{c+M}\sum_{j=1}^M d_{t-j}.
\]
Choose \(\kappa=\min\{c/4,1/4\}\). Since for every integer \(M\ge1\),
\[
 \sum_{j=1}^M e^{\kappa j/M^2}
 \le M+\kappa e^{\kappa}<M+c,
\]
induction from \(d_t\le1\) for \(t\le0\) gives \(d_t\le e^{-\kappa t/M^2}\) for all positive \(t\). A union bound on the last \(M\) bits proves that the total-variation distance between an arbitrary initial order-\(M\) state, evolved \(g\) steps, and stationary law is at most
\[
 \varepsilon_M(g)=M\exp[-\kappa(g-M+1)_+/M^2],
\]
with the right-hand side truncated at 1 if necessary. This uniform estimate is the essential ingredient missing from a fixed-chain-only rare-word limit.

**3. Factorial moments of rare run starts.** Take any \(k=k_n\ge M\) such that \(n p_k\to\lambda\in(0,\infty)\). The exact formula above implies
\[
 q_M^{k-M}=O(M^{\beta+1}/n),\qquad k=O(M\log n).
\]
Fix an integer moment order \(r\ge1\), choose \(g=C_rM^2\log n\) with sufficiently large fixed \(C_r\), and put \(h=k+g\). The coupling bound gives \(n^r\varepsilon_M(g)=o(1)\). Moreover,
\[
 h q_M^{k-M}=O(M^{\beta+3}\log n/n)=o(1),\qquad h=o(n).
\]
For \(r\) distinct ordered potential start locations with all consecutive gaps at least \(h\), the mixing estimate after the previous length-\(k\) word implies their joint probability is \(p_k^r+O_r(\varepsilon_M(g))\). Such separated tuples number asymptotically \(n^r\) when ordered without restriction, and yield the main factorial moment \(\lambda^r\).

For tuples containing close starts, partition the sorted locations into \(j<r\) clusters using gaps smaller than \(h\). There are \(O_r(n^j h^{r-j})\) such tuples. Starts within a distance at most \(k\) are incompatible, so their joint probability is zero. Otherwise, regardless of previous observations, after any specified start the conditional probability of the next \(k\)-ones streak is at most \(q_M^{k-M}\): at most \(M\) early bits have probability bounded by one and each later success is bounded by \(q_M\). Between clusters, the preceding block has at least \(g\) steps to mix. Consequently the joint probability is bounded by
\[
 (p_k+\varepsilon_M(g))^j\big(q_M^{k-M}\big)^{r-j}.
\]
Summing over close tuples gives at most a constant times
\[
 (np_k+o(1))^j\big(hq_M^{k-M}\big)^{r-j}=o(1).
\]
Thus every factorial moment of the total count tends to \(\lambda^r\), proving Poisson convergence. The same estimates for disjoint macroscopic subintervals give joint independent Poisson counts and hence the stated point-process limit.

**4. Recovering the maximum and removing the lattice.** If a length-\(k\) streak is present but no \(A_i\) occurs, it must begin at the very first bit. The probability of this exceptional event is at most
\[
 u_Mq_M^{k-M}=p_k/(1-q_M)=O(M/n)=o(1).
\]
Therefore \(\mathbb P(L_n<k)\to e^{-\lambda}\). Given fixed \(x\in\mathbb R\), choose \(k=1+\lfloor b_{n,M}+x/\tau_M\rfloor\). Since \(\tau_M\to0\),
\[
 n p_k=\exp[-\tau_M(k-b_{n,M})]\longrightarrow e^{-x}.
\]
The inequality \(\tau_M(L_n-b_{n,M})\le x\) is equivalent to \(L_n<k\), which completes the proof.

## Verification
Run the included standalone `checker.py` using Python 3. It directly enumerates finite draw words with rational probabilities for \(1\le M\le4\) and integer \(\alpha,\beta\in\{1,2,3\}\). It checks stationarity of each memory block, all-one probabilities, zero-then-ones probabilities, and total mass; it is supplemental to the coupling and factorial-moment argument. The asymptotic statements are infinite theorems proved above, not consequences of the finite checks.

## Relationship to prior work
Yu, Alajaji and Gharesifard [1] formulate Pólya threshold graphs, including the finite-memory sequential indicator model; their investigation emphasizes graph degrees, spectra and consensus, not growing-memory extreme streaks. Alajaji and Fuja [2] develop the underlying finite-memory contagion channel and its invariant block statistics. Earlier Markov word-count Poisson approximations [3,4] address stationary Markov sequences and are credited as methodological precursors; the changing state-space dimension \(2^{M_n}\), vanishing contraction rate, explicit critical threshold and disappearance of lattice oscillations require the uniform-in-memory estimates established here. Makri and collaborators [5] consider success runs in the classical nonexpiring Pólya urn. No historical uniqueness is asserted beyond inspected comparisons.

## Limitations
The memory restriction \(M^{\beta+3}\log n=o(n)\) is a sufficient regime, not claimed optimal. The result does not describe \(M\) fixed, nonstationary initializations, unequal-memory reinforcement removal, or graph observables beyond the streak length. The point-process theorem concerns left endpoints of long runs and not every overlapping subword occurrence. Related general rare-word Poisson approximation bounds may potentially yield a broader parameter range; a full priority search beyond inspected sources remains advisable. The proof uses no independence assumption between runs.

## References
[1] J. Yu, F. Alajaji and B. Gharesifard, *Pólya Thresholds Graphs*, arXiv:2603.18452v1, 19 March 2026. https://arxiv.org/html/2603.18452v1

[2] F. Alajaji and T. Fuja, *A Communication Channel Modeled on Contagion*, IEEE Transactions on Information Theory 40 (1994), 2035–2041. Open preprint: https://drum.lib.umd.edu/bitstreams/24b9367d-d820-4c7d-978d-7c7cf4b024e0/download

[3] O. Chryssaphinou, S. Papastavridis and E. Vaggelatou, *Poisson Approximation for the Non-Overlapping Appearances of Several Words in Markov Chains*, Combinatorics, Probability and Computing 10 (2001), 293–308. DOI: 10.1017/S096354830100476X.

[4] E. Roquain and S. Schbath, *Improved compound Poisson approximation for the number of occurrences of any rare word family in a stationary Markov chain*, Advances in Applied Probability 39 (2007), 128–140. DOI: 10.1239/aap/1175266472.

[5] F. S. Makri and collaborators, *Success run statistics defined on an urn model*, Advances in Applied Probability 39 (2007). https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C3B5A694CDFF993F8C769CD78754DF61/S0001867800002202a.pdf/success_run_statistics_defined_on_an_urn_model.pdf
