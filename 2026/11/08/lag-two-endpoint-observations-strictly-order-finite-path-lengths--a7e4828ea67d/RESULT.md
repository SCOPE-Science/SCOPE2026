# Lag-two endpoint observations strictly order finite path lengths in the synchronous noisy voter model

## Finding
Let \(P_n\) be the unweighted path on vertices \(0,1,\ldots,n-1\), with \(n\ge2\), observed only at the endpoint \(0\). In the synchronous noisy voter model every vertex, independently each integer time, refreshes to a fair binary opinion with probability \(\varepsilon\in(0,1)\), or otherwise copies a uniformly selected neighbor's *previous-time* opinion. Put \(c=1-\varepsilon\). For \(T\ge3\), define the observed lag-two repetition frequency
\[
H_{n,T}=\frac1{T-2}\sum_{t=0}^{T-3}\mathbf1\{\xi_t(0)=\xi_{t+2}(0)\}.
\]
From **any** initial opinion law, \(H_{n,T}\to h_n(c)\) almost surely. These limits strictly order **all** path lengths, at every positive noise level:
\[
 h_2(c)>h_3(c)>h_4(c)>\cdots\qquad(0<c<1).
\]
In particular any two different endpoint-rooted finite paths are distinguished almost surely by a single lag-two observation statistic; knowledge of the shared noise parameter identifies the length. Quantitatively, for integers \(2\le n<m\),
\[
 h_n(c)-h_m(c)\ge \frac{c^2}{4}\left(\frac{c^2}{4}\right)^{n-2}(1-c^2)>0.
\]
There is also an exact probabilistic representation. For \(n\ge3\), let \(L=n-1\) and let \(Z\) be standard nearest-neighbor simple random walk on \(\mathbb Z^2\), started at \((1,-1)\), with each of its four compass moves having probability \(1/4\). Let \(\tau_L\) be its first exit from the open rectangle \((0,L)\times(-L,0)\). Then
\[
 h_n(c)=\frac12+\frac{c^2}{4}\bigl(1+\mathbb E[c^{2\tau_L}]\bigr),\qquad
 h_2(c)=\frac{1+c^2}{2}.
\]
The square-exit identity, strict stochastic comparison of exit times, and the explicit gap are parts of the finding.

## Assumptions and scope
All graph edges have unit weight. Copying choices, refresh indicators, and fresh fair opinions are independent across sites and times. All vertices update *simultaneously*, using the preceding configuration; the update law is not an asynchronous one-site voter chain. The observed vertex is an endpoint, not an arbitrary interior vertex. The same fixed and known \(\varepsilon\in(0,1)\) is used when comparing paths. The theorem concerns the infinite-time observed frequency, not a finite-sample confidence interval. All comparisons are between finite paths with at least two vertices.

## Proof
**1. Stationarity and the observation limit.** The chain of full binary configurations is finite. At every time, the event that every vertex refreshes to prescribed opinions has probability \((\varepsilon/2)^n>0\), regardless of the previous state. Thus its transition matrix is strictly positive, hence it has a unique stationary law and is irreducible and aperiodic. The ergodic theorem for finite chains, applied to the length-three window of successive states, proves the stated almost-sure convergence from any initial distribution.

**2. Backward genealogy.** In the stationary extension, trace a vertex's opinion backward through the copy arrows until its first refresh. For two observations, if their ancestral paths meet at the same space-time site before either has refreshed, the opinions agree surely; otherwise they are independent fair bits. Consequently, writing \(p_{n,2}\) for that coalescence probability, \(h_n(c)=(1+p_{n,2})/2\).

For \(n\ge3\), the backward path from \((0,t+2)\) must avoid refresh twice (probability \(c^2\)); conditional on this, after two random-walk steps it lies at vertex \(0\) or \(2\), each with probability \(1/2\). At vertex \(0\) it has already met the path from \((0,t)\). At vertex \(2\), the two ancestral paths evolve as independent simple random walks until meeting, and both must survive refresh at each further backward step. If \(\sigma_n\) is their (un-killed) first simultaneous meeting time from \((0,2)\), then
\[
 p_{n,2}=\frac{c^2}{2}\bigl(1+\mathbb E[c^{2\sigma_n}]\bigr).
\]
This formula does not require the paths to be ordered: simultaneous walkers can exchange positions without meeting. For \(P_2\), a two-step neighbor walk from endpoint \(0\) returns deterministically to \(0\), so \(p_{2,2}=c^2\) and \(h_2(c)=(1+c^2)/2\).

**3. An exact planar first-exit representation.** Set \(L=n-1\) and fold \(\mathbb Z\) onto \(\{0,\ldots,L\}\) using the unique \(2L\)-periodic function \(r_L\) satisfying \(r_L(j)=j\) for \(0\le j\le L\) and \(r_L(j)=2L-j\) for \(L\le j\le2L\). Folding a simple random walk on \(\mathbb Z\) produces exactly the non-lazy simple random walk on \(P_n\), including its deterministic endpoint reflections.

Lift the two independent walks from \(0\) and \(2\) to independent nearest-neighbor walks \(A_s,B_s\) on \(\mathbb Z\), starting at those same positions. Their reflected positions agree exactly when \(A_s\equiv B_s\pmod{2L}\) or \(A_s\equiv-B_s\pmod{2L}\). Their parities agree, so the integer pair
\[
 Z_s=\left(\frac{A_s+B_s}{2},\frac{A_s-B_s}{2}\right)
\]
starts at \((1,-1)\) and makes precisely one of the four compass moves with probability \(1/4\). The reflected walks meet precisely when either coordinate of \(Z_s\) is divisible by \(L\). Before that happens, \(Z_s\) stays in \((0,L)\times(-L,0)\), and its first hit of the boundary is its first hit of a multiple-of-\(L\) coordinate. Therefore \(\sigma_n\stackrel d=\tau_L\); the identity for \(h_n\) follows. The equality is pathwise under this coupling, not a diffusion approximation.

**4. Strict ordering and gap.** Use one common planar walk \(Z\) for every \(L\ge2\). The nested rectangles imply \(\tau_L\le\tau_{L'}\) pathwise whenever \(L<L'\). The inequality is strict with positive probability: on the event that the first \(L-1\) steps are all east, of probability \(4^{-(L-1)}\), the walk exits the smaller rectangle at \((L,-1)\) but remains in the larger one, giving \(\tau_L=L-1<\tau_{L'}\). As \(0<c<1\), on this event
\[
 c^{2\tau_L}-c^{2\tau_{L'}}\ge c^{2(L-1)}(1-c^2).
\]
Taking expectations and multiplying by \(c^2/4\) yields, for \(3\le n<m\),
\[
 h_n(c)-h_m(c)\ge \frac{c^2}{4}\left(\frac{c^2}{4}\right)^{n-2}(1-c^2).
\]
For \(n=2\), the square for \(L=2\) is a single interior site, so \(\tau_2=1\) surely and \(h_3(c)=1/2+c^2(1+c^2)/4\). Hence \(h_2(c)-h_3(c)=c^2(1-c^2)/4\). Monotonicity for \(n\ge3\) then gives the stated bound for every \(m>2\). This completes the proof.

## Verification
A standalone standard-library checker `verify.py` recomputes exact rational finite-size values in three ways: the planar square-exit resolvent, a killed two-walker meeting-time resolvent, and the stationary two-spin covariance equations. It also directly solves the full binary configuration chain for small paths and verifies the formula and separation bound. Run `python3 verify.py`; the checked run printed `VERIFY_OK` and completed 38 grouped exact assertions for noise-survival parameters \(c=1/2\) and \(c=2/3\), at lengths \(2\) through \(7\). These checks are finite consistency tests; the theorem for all lengths and noise values follows from the proof above.

## Relationship to prior work
Benjamini, Helman Tov, and Zhukovskii [1] introduce the local lagged-repetition test and the coalescing-genealogy criterion. Their theorems treat complete graphs, cycles, perfect rooted trees with arity at least two, and other families, and explicitly raise the problem of distinguishing trees. Their Theorem 1.4 does **not** include one-ary trees (endpoint-rooted paths), and their Theorem 2.1 supplies the general interpretive framework rather than the monotonic path-length claim. The new contribution here is the all-noise strict order, square-exit coupling, and quantitative separation, not the genealogy mechanism or the ergodic theorem. Mohylevskyy, Newman, and Ravishankar [2] analyze voter genealogy and ergodicity on the infinite one-dimensional lattice, without a finite reflecting-path endpoint ordering. Pymar and Rivera [3] study global density for an asynchronous one-site-update model, not these local synchronous lag-two observations.

## Limitations
No assertion is made for the zero- or full-noise endpoints \(\varepsilon\in\{0,1\}\), for interior observation vertices, for directed/weighted paths, for unknown or different noise parameters, or for arbitrary trees. The gap bound is not claimed optimal. This does not settle the conjectured distinguishability of all non-star graphs. A unique statistical limit does not by itself provide a uniform finite-time sample-complexity bound. Independent mathematical validation and historical priority assessment remain unperformed.

## References
[1] I. Benjamini, H. Helman Tov, and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, arXiv:2207.01224 (first public version 2022-07-04), Annals of Probability 51 (2023), 1963–1992. https://arxiv.org/abs/2207.01224

[2] Y. Mohylevskyy, C. M. Newman, and K. Ravishankar, *Ergodicity and Percolation for Variants of One-dimensional Voter Models*, arXiv:1112.1893 (2011), ALEA 10 (2013), 485–504. https://arxiv.org/abs/1112.1893

[3] R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (first public version 2021-12-02). https://arxiv.org/abs/2112.01478
