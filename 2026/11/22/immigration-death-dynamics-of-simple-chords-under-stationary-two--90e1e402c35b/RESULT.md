# Immigration–death dynamics of simple chords under stationary two-pair rewiring

## Finding

Arrange \(2n\) labeled points in cyclic order and take a uniformly random perfect matching. In each discrete step, choose two of its \(n\) matched pairs uniformly and replace them by either alternative matching of their four endpoints, each with probability \(1/2\). Let \(S_n(r)\) be the number of matched pairs occupying adjacent cyclic positions after \(r\) steps, including the closing boundary pair.

For \(n\ge3\) and every integer \(r\ge0\), stationarity gives the **exact temporal covariance**
\[
\operatorname{Cov}(S_n(0),S_n(r))
=\frac{4n(n-1)}{(2n-1)^2}
 \left(1-\frac{2n-1}{n(n-1)}\right)^r.
\]
The stationary mean and variance are \(2n/(2n-1)\) and \(4n(n-1)/(2n-1)^2\), respectively. These static moments are known; the temporal identity concerns their evolution under rewiring.

**Process limit.** On every bounded time interval, in the Skorokhod \(J_1\) topology,
\[
\bigl(S_n(\lfloor nt\rfloor)\bigr)_{t\ge0}
\ \Longrightarrow\ (Z(t))_{t\ge0},
\]
where \(Z\) is the stationary continuous-time immigration–death chain on nonnegative integers with generator
\[
(\mathcal Lf)(s)=2[f(s+1)-f(s)]+2s[f(s-1)-f(s)],
\]
with the death term interpreted as zero at \(s=0\). Its equilibrium law is \(\operatorname{Pois}(1)\), and
\[
\operatorname{Cov}(Z(0),Z(t))=e^{-2t},\qquad
\Pr(Z(0)=Z(t)=0)=\exp(-2+e^{-2t}).
\]
The latter follows by thinning stationary initial particles with survival probability \(e^{-2t}\), independently of arrivals surviving to time \(t\).

## Assumptions and scope

Let \(V=\{0,1,\ldots,2n-1\}\), and let \(\mathcal M_n\) be its set of perfect matchings. Initially \(M_0\) is uniform on \(\mathcal M_n\). At each step choose a uniformly random unordered pair of **distinct current matching edges**, then replace them by one of the two other pairings of their four endpoints, chosen equiprobably. Thus the current pairing is never repeated in a selected four-point block. The transition matrix is symmetric, so the uniform law is stationary. The count \(S_n\) records matching edges from the cycle \(C_{2n}\). The result concerns integer \(n\ge3\), every integer lag \(r\ge0\), and the stationary path law over all finite time horizons. The count process need not be Markov at finite \(n\); only its limit is asserted to be Markov.

## Proof

**1. Edge transition and exact eigenmode.** Fix any unordered pair \(e=\{a,b\}\) and let \(X_e(M)\) be its presence indicator. If present, it is selected for rewiring with probability \(2/n\), and then necessarily disappears. If absent, its endpoints belong to two distinct matching edges. Those two edges are selected with probability \(1/\binom n2\); exactly one of their two alternative pairings contains \(e\). Therefore, for *every* matching \(M\),
\[
\mathbb E[X_e(M_{r+1})\mid M_r=M]
=\left(1-\frac2n\right)X_e(M)+\frac{1-X_e(M)}{n(n-1)}.
\]
Summing over the \(2n\) cyclic adjacency pairs gives
\[
\mathbb E[S_n(r+1)\mid M_r]
= a_n S_n(r)+\frac{2n}{n(n-1)},\qquad
 a_n=1-\frac{2n-1}{n(n-1)}.
\]
The stationary mean \(\mu_n=2n/(2n-1)\) satisfies the fixed-point equation. Hence the centered observable \(S_n-\mu_n\) is an *exact eigenfunction* of the full matching-chain transition operator, even though the projected count need not be a Markov chain. Iterating the conditional expectation and multiplying by its stationary initial value yields
\(\operatorname{Cov}(S_n(0),S_n(r))=a_n^r\operatorname{Var}(S_n(0))\).

**2. Static moments and Poisson initial law.** There are \(2n\) cyclic adjacency edges. An individual is matched with probability \(1/(2n-1)\). Of the \(2n(2n-1)\) ordered pairs of distinct adjacency edges, exactly \(2n(2n-3)\) are vertex-disjoint. Such two edges coexist with probability \(1/[(2n-1)(2n-3)]\). Thus
\[
\mathbb E S_n=\mathbb E(S_n)_2=\frac{2n}{2n-1},\quad
\operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2}.
\]
Here \((s)_k=s(s-1)\cdots(s-k+1)\). More generally, the count of ordered, vertex-disjoint \(k\)-tuples of cyclic adjacency edges is \((2n)^k(1+O_k(n^{-1}))\), and their simultaneous matching probability is \(\prod_{j=0}^{k-1}(2n-2j-1)^{-1}\). Hence \(\mathbb E(S_n)_k\to1\) for each fixed \(k\ge0\). The factorial-moment criterion gives \(S_n(0)\Rightarrow\operatorname{Pois}(1)\).

**3. One-step births, deaths and double-event control.** In a switch let \(B\) be the number of newly created cyclic adjacency edges and \(D\) the number of destroyed ones. Conditioned on the current matching \(M\), with \(s=S_n(M)\),
\[
\mathbb E[B\mid M]=\frac{2n-s}{n(n-1)},\qquad
\mathbb E[D\mid M]=\frac{2s}{n}.
\]
Every missing adjacency edge is created with probability \(1/[n(n-1)]\), and every present adjacency edge is destroyed with probability \(2/n\). In particular \(B,D\le2\).

In stationary law, the probability of two destroyed adjacency edges is \(O(n^{-2})\): the switch must select a pair of present adjacency edges, and \(\mathbb E(S_n)_2=O(1)\). By reversibility, two newly created adjacency edges have the same probability as two destroyed ones. Finally, simultaneous creation and destruction is \(O(n^{-2})\): given a destroyed adjacency edge, a new adjacency edge must join one of its endpoints to one of its at most four cyclic neighbors; selecting the particular other matched edge and alternative reconnection has probability at most a constant times \(1/[n(n-1)]\) per present adjacency edge. The stationary expected number of present adjacency edges is bounded. Thus
\[
\Pr(B+D\ge2)=O(n^{-2}).
\]
Consequently, for every bounded function \(f\) on the nonnegative integers, with \(\Delta_n f(M)=\mathbb E[f(S_n(M_1))-f(S_n(M))\mid M_0=M]\),
\[
\mathbb E_{\mathrm{stat}}\left|n\Delta_n f(M)-\mathcal Lf(S_n(M))\right|\longrightarrow0.
\]
The rates \(2\) and \(2s\) follow by multiplying the displayed conditional mean births and deaths by \(n\); the discrepancy from simultaneous events is bounded by \(O(n\Pr(B+D\ge2))\). For fixed finite-support test functions the bound is uniform in values of \(f\) on the relevant range.

**4. Tightness and identification.** For each fixed \(T\), the expected number of births during the first \(\lfloor nT\rfloor\) steps equals \(\lfloor nT\rfloor\,\mathbb E_{\mathrm{stat}}B=O(T+1)\); also \(\sup_{t\le T}S_n(\lfloor nt\rfloor)\) is bounded by the initial count plus total births. This gives compact containment. Before exiting \(\{0,\ldots,K\}\), the one-step chance of any change is bounded by \(2K/n+2/(n-1)\), uniformly over all underlying matching states. It follows that the probability of a count change during at most \(n\delta+1\) steps after any bounded stopping time, on the event of remaining below \(K\), is \(O_K(\delta+n^{-1})\). These estimates give Aldous tightness in \(D([0,T],\mathbb Z_{\ge0})\), and also rule out multiple limit jumps from one discrete update.

For finite-support bounded \(f\), the exact conditional martingale for the discrete chain has predictable compensator \(\sum\Delta_n f(M_j)\). By stationarity and the mean generator estimate from Step 3, its difference from \(\int_0^t\mathcal L f(S_n(\lfloor nu\rfloor))\,du\) vanishes in \(L^1\), uniformly on each finite horizon. Every subsequential limit therefore solves the \(\mathcal L\)-martingale problem with Poisson(1) initial law. The immigration–death chain is nonexplosive and has a unique such solution (construct independent immigration Poisson clocks and exponential lifetimes). This identifies every limit and proves path convergence.

## Verification

Run `python verify.py` in the directory containing this document. The standard-library program enumerates all perfect matchings for \(2\le n\le6\), enumerates every possible two-pair switch from each matching, and checks the exact conditional eigenfunction, stationary mean and variance, and one-step covariance using rational arithmetic. It reports `ALL EXACT ENUMERATION CHECKS PASSED`. These finite checks support the identities but do not prove the asymptotic martingale argument; the infinite result is proved in Steps 2–4.

## Relationship to prior work

Flajolet and Noy (2000) analyze static chord-diagram components and crossings, providing the archival setting. Acan (2015) establishes static short-chord Poisson laws. Published exact static factorial-moment and sharp Poisson-approximation refinements for simple chords are acknowledged; the finite stationary mean and variance above are not offered as original formulas. Olesker-Taylor (2021) studies a perfect-matching rewiring chain with a lazy local transition (the current pairing can be selected again), focusing on global mixing and cutoff. His chain is a mixture of the identity and the forced re-pairing step defined here. The global mixing result does not give the temporal law of cyclic adjacent pairs. The contribution assessed here is the **full stationary path limit under local rewiring**, together with the exact temporal eigenmode and the induced two-time void law.

## Limitations

The theorem assumes initially uniform matchings, fixed circular site labels, and uniform two-pair forced rewiring. It does not assert the same limit from arbitrary initial configurations or for general weighted matching chains. No sharp error rate for path convergence is claimed. General Markov-chain Poisson-approximation methods may subsume parts of the derivation; no independent historical-priority certification has been performed. No independent scientific audit has been conducted.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, research report dated 4 March 2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first version 7 January 2015, https://arxiv.org/abs/1501.01489.
3. S. Olesker-Taylor, *Cutoff for Rewiring Dynamics on Perfect Matchings*, arXiv:2108.11890, first version 26 August 2021, https://arxiv.org/abs/2108.11890.
4. *Sharp total-variation constant for simple chords in a uniform chord diagram*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-total-variation-constant-for-simple-chords-in-a-uniform-ch--f3c18b7beed6 (static distribution refinements).
5. *Exact short-chord/crossing transfer and independent Poisson–Gaussian limits*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-short-chord-crossing-transfer-and-independent-poisson-gaus--0749abe76974 (static mixed-count law and moments).
