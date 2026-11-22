# Asynchronous nucleation of frozen icosahedral Ising caps: an exact trapping law

## Finding

Let \(I\) be the unweighted icosahedral graph with twelve vertices and degree five. At independent rate-one Poisson clocks, update one Ising spin to the strict majority of its five neighbors, with no external field. Each initial spin is independently positive with probability \(p\in[0,1]\). Let \(Q(p)\) be the probability of eventual absorption into a nonunanimous configuration. Set \(q=p(1-p)\). Then

\[
\boxed{Q(p)=\frac{q^3}{85\,050\,000}
\left(739\,236\,313q^2+1\,651\,550\,400q+170\,100\,000\right).}
\]

There are exactly fourteen absorbing states: two unanimous states and twelve complementary six-positive-spin caps, each the closed neighborhood of a vertex. All trajectories almost surely reach one of these states. The strict positive coefficients in the displayed formula imply that \(Q(p)\) has a unique maximum at \(p=1/2\), where

\[
Q(1/2)=\frac{10\,067\,037\,913}{87\,091\,200\,000}\approx0.1155919072535457.
\]

The contrast with **synchronous** neighbor majority on the same graph and the same starting measure is exact. The only synchronous predecessor of any cap is the cap itself, so the synchronous probability of reaching a cap is just \(12q^6\). Thus \(Q(p)>12q^6\) for every \(0<p<1\). At \(p=1/2\), the asynchronous-to-synchronous cap absorption ratio is \(10\,067\,037\,913/255\,150\,000\approx39.45537\). Although every mixed absorbing state contains six positive spins, of the \(\binom{12}{3}=220\) configurations containing only three initial positive spins, 60 reach a mixed cap with probability exactly \(1/30\) each, and the other 160 have probability zero.

## Assumptions and scope

The labelled icosahedral graph has vertices \(0,1,\ldots,11\). Vertex \(0\) is a pole, \(A_i=1+i\) and \(B_i=6+i\) are pentagonal rings for \(i\in\mathbb Z/5\mathbb Z\), and \(11\) is the opposite pole. Its edges are \(0A_i\), \(11B_i\), \(A_iA_{i+1}\), \(B_iB_{i+1}\), \(A_iB_i\), and \(A_iB_{i-1}\) for all five indices. This gives 30 undirected edges and five neighbors per vertex. The twelve cap configurations are the indicator functions of closed vertex neighborhoods \(N[v]\); because every vertex has five neighbors, they have six positive spins. The complement of a cap is another cap.

The Hamiltonian is \(\mathcal H(\sigma)=-J\sum_{uv\in E(I)}\sigma_u\sigma_v\) with \(J>0\). With degree five, there are no local energy ties. In asynchronous dynamics, a site whose spin disagrees with at least three neighbors flips at rate one; all other sites are unchanged when their clocks ring. The process runs for an unbounded time horizon; \(Q(p)\) is the eventual absorption probability, not the finite-time occupation probability. Synchronous dynamics means simultaneous updating of every spin to its neighbor majority at each integer time, not sequentially choosing an update order.

## Proof

**Absorbing configurations and termination.** For a state \(x\in\{0,1\}^{12}\), let \(M(x)\) be the set of vertices with at least three disagreeing neighbors. Define the number of disagreeing edges by \(b(x)=|\{uv\in E(I):x_u\ne x_v\}|\). Flipping a vertex with \(d\in\{3,4,5\}\) disagreeing neighbors changes this count by \(5-2d\in\{-1,-3,-5\}\). Thus the transition graph is a finite directed acyclic graph ordered by decreasing \(b\), and every trajectory almost surely absorbs after at most thirty flips. A complete finite enumeration of the 4096 states, with all 30 edges specified above, proves \(M(x)=\varnothing\) precisely for the two unanimous configurations and the twelve indicator sets \(N[v]\). The complete bounded enumeration and a separately constructed verification are given in `check_rational.py` and `check_independent.py`. The cap sets are stable directly: a pole has all five neighbors in the cap, each other included vertex has at least three included neighbors, and every excluded vertex has at most two included neighbors.

**Exact probability recurrence.** Let \(h(x)\) be the probability of eventual absorption in one of the twelve caps when starting from \(x\). On an absorbing state \(x\), let \(h(x)=1\) for a cap and \(0\) for a unanimous state. Otherwise, the next *successful* clock ring occurs at any of the \(|M(x)|\) flippable vertices with equal probability; hence the exact backward equation is

\[
h(x)=\frac{1}{|M(x)|}\sum_{v\in M(x)}h(x\oplus e_v).
\]

Here \(x\oplus e_v\) flips one bit. The strict decrease of \(b(x)\) proves by finite induction that these equations uniquely define \(h\) without numerical limits, truncations, or an unproved stationary-distribution assumption. Both supplied verification programs solve every equation with arbitrary-precision rational numbers.

For \(k=0,\ldots,12\), set \(c_k=\sum_{|x|=k}h(x)\). The exact values are

\[
\begin{aligned}
(c_0,\ldots,c_{12})={}&\bigl(0,0,0,2,\tfrac{742264}{23625},
\tfrac{9896937913}{85050000},\tfrac{7394887513}{42525000},\\
&\tfrac{9896937913}{85050000},\tfrac{742264}{23625},2,0,0,0\bigr).
\end{aligned}
\]

A product Bernoulli starting configuration has probability \(p^{|x|}(1-p)^{12-|x|}\), so

\[
Q(p)=\sum_{k=0}^{12}c_kp^k(1-p)^{12-k}.
\]

Expanding these thirteen Bernstein terms and collecting by \(q=p(1-p)\) yields the exact polynomial in the Finding. The two programs independently construct the coefficient list from different graph representations and different evaluation orders. They also reproduce \(h(x)=1/30\) for exactly sixty states with three positive spins, and zero for the remaining 160.

**Optimization and update-schedule comparison.** All three coefficients of the polynomial in \(q\) are positive. It is strictly increasing for \(q>0\), while \(q=p(1-p)\le1/4\), with equality only for \(p=1/2\). For the synchronous map, direct complete preimage enumeration shows that each of the twelve caps is its own unique predecessor; a symbolic proof of the same fact for this graph is also provided in the published synchronous-majority result cited below. Its Bernoulli cap-basin probability is therefore \(12p^6(1-p)^6=12q^6\). Since \(Q(p)\ge2q^3\) and \(12q^6\le(3/16)q^3\) for \(0<q\le1/4\), strict enhancement under asynchronous updates follows. Both probabilities are zero for \(p\in\{0,1\}\).

For a concrete three-positive-spin nucleation path in the pole-and-ring coordinates, start from the active set \(\{1,2,4\}\). Successively flip vertices \(0,3,5\) to reach the cap \(\{0,1,2,3,4,5\}\). Each step is strictly energy lowering; the complete competing-move calculation gives the total cap absorption probability \(1/30\) for that starting state. This witnesses a physically reachable cap from half its final positive population.

## Verification

Run `python3 check_rational.py` using Python 3.8 or later (standard library only) and `python3 check_independent.py` using Python 3 with NetworkX 2.8 or later. Both programs terminate only after explicit exact assertions have checked the full 4096-state domain. The first builds the graph from pole-and-ring edges, computes all recursive absorption probabilities and algebraically checks the full polynomial. It independently enumerates the synchronous cap predecessors. The second constructs a built-in icosahedral graph, represents states as vertex sets rather than bitmasks, and solves every state in increasing disagreeing-edge count, checking all coefficients again. The two independent representations agree on 14 absorbing states, the exact law, its unbiased value and the 60 positive three-seed probabilities. No simulation or floating-point approximation is used to establish any claim.

## Relationship to prior work

Newman and Stein (1999, first public arXiv submission 1999-04-14) establish blocking and fixation properties of zero-temperature Ising dynamics, including odd-coordinated homogeneous lattice models; their full accessible preprint does not calculate icosahedral absorption basins. Spirin, Krapivsky and Redner (2001, first public 2001-05-02) study freezing after a quench and distinguish energy-lowering spin flips and metastable stripe configurations, but their primary preprint concerns hypercubic and large-lattice systems, not the exact twelve-site icosahedral law.

The previously published *The icosahedral majority landscape: isolated caps and seven oscillation symmetries* determines exactly the same **absorbing cap set for synchronous neighbor-majority**, and proves cap non-nucleation for that synchronous update map. Those static cap and synchronous non-nucleation statements are **not** claimed as new here. This result instead solves the continuous-time asynchronous stochastic cap-hitting problem and establishes its strict comparison with the synchronous cap-basin probability. The earlier Petersen-graph asynchronous Glauber freezing law concerns a different graph and does not imply these coefficients; no graph reduction transporting its absorption probabilities to the icosahedron is known.

## Limitations

The exact polynomial and kinetic contrast concern the unweighted, fixed twelve-site icosahedral graph, zero external field, rate-one independent single-spin clocks, and strictly energy-lowering majority flips. The result is not asserted for larger graph families, biased clocks, positive temperature or arbitrary initial dependence. The two executable enumerations are finite exhaustive proofs, not an analytic universal-lattice theorem. Previously unindexed or inaccessible equivalent exact calculations may exist, and no independent expert audit has been performed.

## References

- C. M. Newman and D. L. Stein, *Blocking and Persistence in the Zero-Temperature Dynamics of Homogeneous and Disordered Ising Models* (1999), arXiv:cond-mat/9904208v1, https://arxiv.org/abs/cond-mat/9904208 (first public 1999-04-14).
- V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets* (2001), arXiv:cond-mat/0105037v1, https://arxiv.org/abs/cond-mat/0105037 (first public 2001-05-02).
- *The icosahedral majority landscape: isolated caps and seven oscillation symmetries*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-icosahedral-majority-landscape-isolated-caps-and-seven-oscil--4b6d7cb731ad.
- Mathematics Subject Classification 2020, category 82C22, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C22.
