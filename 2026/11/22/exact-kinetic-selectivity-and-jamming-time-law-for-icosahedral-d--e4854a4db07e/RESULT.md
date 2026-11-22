# Exact kinetic selectivity and jamming-time law for icosahedral dimer adsorption

## Finding
Let \(G\) be the graph of the regular icosahedron, with 12 vertices and 30 edges. Put an independent rate-one exponential arrival clock on every edge. Initially all vertices are vacant. On an edge's first arrival, deposit a dimer if and only if both endpoints are vacant; otherwise reject it. Accepted dimers remain forever. Let \(K\) be their terminal count, \(T\) the time of the last accepted dimer, and \(U\) the terminal uncovered vertex set. The complete terminal geometry law is
\[
\begin{aligned}
\Pr(K=6)&=\frac{3622453}{8026200},\\
\Pr(K=5,\operatorname{dist}(U)=2)&=\frac{11150381}{24078600},\\
\Pr(K=5,\operatorname{dist}(U)=3)&=\frac{103043}{1203930}.
\end{aligned}
\]
Here \(\operatorname{dist}(U)\) is the graph distance between the two uncovered vertices when \(|U|=2\); no other terminal possibilities exist. Consequently \(\Pr(K=5)=4403747/8026200\). Among the 36 possible terminal uncovered pairs, the 30 distance-two pairs each have probability \(11150381/722358000\), and the six antipodal pairs each have probability \(103043/7223580\).

The entire jamming-completion-time distribution is the following finite exponential sum, valid for every real \(t\ge0\):
\[
\Pr(T\le t)=\sum_{r\in\mathcal R}c_r e^{-rt},\qquad
\mathcal R=\{0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,21,30\}.
\]
The exact 17 rational coefficients \(c_r\) are given without truncation in `SPECTRUM.csv` and independently checked by `verifier.py`. In particular,
\[
\mathbb E[T]=\frac{167225267}{144471600}.
\]
The 125 perfect matchings do not have equal probabilities of being selected. The full distribution of *individual perfect-matching probabilities* is:

| Probability of one specified matching | Number of such matchings |
|---|---:|
| \(52/15435\) | 5 |
| \(38999/10749375\) | 10 |
| \(2188741/619164000\) | 20 |
| \(118598/32248125\) | 30 |
| \(92353/25515000\) | 60 |

These five exact classes and multiplicities are independently recomputed by `verifier.py` and also stored in `MATCHING_WEIGHTS.csv`. This constitutes one complete finite-network kinetic finding, not a statement about infinite-size adsorption.

## Assumptions and scope
The substrate is the ordinary undirected icosahedral graph, not the dual dodecahedral graph and not a continuum packing of polyhedral solids. All thirty edges have independent identical, single-use rate-one exponential clocks; every dimer covers exactly the two endpoints of its edge; no desorption, rate heterogeneity, replacement or diffusion occurs. All claims are exact for this twelve-site graph. The terminal distribution depends only on an exchangeable continuous ordering of arrivals, whereas the explicit \(T\)-distribution and its expectation require the specified exponential clocks. Time is measured in reciprocal single-edge arrival-rate units.

## Proof
**Geometry and possible terminal states.** The explicit adjacency list in `verifier.py` describes the unique twelve-vertex icosahedral graph. It has degree five, diameter three, 30 adjacent unordered pairs, 30 distance-two pairs and six distance-three (antipodal) pairs. For a fixed vertex, the vertices at distance two form a five-cycle, and its unique antipode is adjacent to all five of these vertices. Thus any independent set containing the fixed vertex has at most three members; the same argument by transitivity gives \(\alpha(G)=3\), with equality achieved. At terminal jamming the uncovered vertices are independent. Because each accepted dimer removes two vertices, their number is even and at most three, hence zero or two. A pair of uncovered vertices must be distance two or three.

**Embedded-chain recursion.** Identify a set of occupied vertices with a bitmask \(M\). Write \(E(M)\) for the edges whose two endpoints are not in \(M\), and \(d(M)=|E(M)|\). While \(d(M)>0\), an unattempted eligible edge has a rate-one memoryless clock. The next accepted edge is uniform over \(E(M)\), and the waiting time is independent exponential of rate \(d(M)\). Let \(p_M(a)\) be the terminal probability for outcome \(a\in\{\mathrm{perfect},\mathrm{distance\ 2},\mathrm{distance\ 3}\}\). For a terminal \(M\), \(p_M\) is the indicator of its label; otherwise
\[
p_M(a)=\frac1{d(M)}\sum_{e\in E(M)}p_{M\cup e}(a).
\]
The union here adds both endpoints of \(e\). Similarly the expected remaining time is zero at a terminal state and otherwise
\[
\tau(M)=\frac1{d(M)}+\frac1{d(M)}\sum_{e\in E(M)}\tau(M\cup e).
\]
All transitions strictly increase the number of occupied vertices, so these are finite exact-rational recurrences. There are 1,720 reachable occupied-vertex masks. Evaluating from the empty mask gives exactly the three probabilities and the expected time displayed in the finding. A separately organized forward mass-propagation recursion gives the same rational numbers.

**The whole jamming-time law.** Let \(f_M(t)\) denote the probability that the occupied set is exactly \(M\) at time \(t\). Its Kolmogorov equation is
\[
f'_M(t)=-d(M)f_M(t)+\sum_{N\to M} f_N(t),
\]
where the sum runs over predecessor states obtained by deleting the two endpoints of one accepted edge. The initial state has \(f_{\varnothing}(t)=e^{-30t}\). Along any transition \(N\to M\), \(d(N)>d(M)\), since at least the accepted edge disappears. Consequently every solution is a sum of pure integer-rate exponentials without resonant polynomial factors. For each \(k\ne d(M)\), its coefficient satisfies
\[
(d(M)-k)c_{M,k}=\sum_{N\to M}c_{N,k},
\]
with \(c_{M,d(M)}\) fixed by \(f_M(0)=0\) for noninitial states. Summing \(f_M(t)\) over the terminal states yields the exact 17-term coefficient list `SPECTRUM.csv`. Since the terminal set is absorbing, this sum is precisely \(\Pr(T\le t)\). Normalization gives \(c_0=1\) and \(\sum_r c_r=0\). Integrating the survival function gives \(\mathbb E T=-\sum_{r>0}c_r/r\), equal to the independent backward mean.

**Perfect-matching selectivity.** Enumerate the 125 perfect matchings by pairing the least unpaired vertex with each still-unpaired neighbor, recursively. For a specified perfect matching \(Q\), exactly its six edges must be chosen, in some order. Therefore its probability is
\[
\Pr(\text{output }Q)=\sum_{\pi\in S_6}\prod_{j=0}^{5}\frac{1}{d(M_j^\pi)},
\]
where \(M_j^\pi\) consists of endpoints of the first \(j\) edges in ordering \(\pi\). Evaluating this exact finite sum for each of the 125 matchings gives the five probabilities and class sizes listed above. Their weighted sum recovers \(\Pr(K=6)\), independently of the terminal-state recursion.

## Verification
Running `python3 verifier.py` beside `SPECTRUM.csv` and `MATCHING_WEIGHTS.csv` requires only the Python standard library. It checks the icosahedral adjacency structure, independence number, 125 perfect matchings, all 36 possible two-vertex vacancy locations, and every claimed exact fraction. Independently implemented backward and forward occupied-mask recursions agree. A triangular forward master-equation calculation reconstructs all 17 exponential coefficients; five separate rational Laplace-transform identities from a backward first-step recursion agree. Finally an edge-permutation recursion assigns probabilities individually to all 125 perfect matchings, recovering the five classes and their weighted total. All computations use exact fractions, not fitted floating-point values.

## Relationship to prior work
Penrose and Sudbury (2005) define the same irreversible edge-arrival dimer model on graphs and derive general forward equations and explicit regular-tree calculations. Gamarnik and Goldberg (2008) study randomized greedy matchings with degree-and-girth bounds, asymptotics and concentration results; their matching theorem is stated for girth at least four, whereas the icosahedral graph has triangles. The icosahedral graph and its distance geometry are standard. The present result specifies previously unprovided, on the examined evidence, exact icosahedral terminal-vacancy geometry, all-time completion distribution and nonuniform weights of its individual perfect matchings. General process algorithms alone do not list these numerical invariants, although they can be used to compute them.

## Limitations
This is a complete exact result for one natural finite graph, not a theorem for all triangulated networks or a thermodynamic limit. Clock-rate heterogeneity, correlated arrivals, desorption and multiple depositions per edge are excluded. The listed individual matching probabilities do not constitute a uniform Gibbs distribution. An earlier exact calculation in an unindexed reference cannot be ruled out; the full Pippenger (1989) article was not available during comparison, although its accessible description concerns distinct graph regimes. The computations are finite and rest on a formal finite recurrence argument.

## References
- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889, arXiv:math/0503519 (first public arXiv version 24 March 2005). https://arxiv.org/abs/math/0503519
- D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277 (first public 8 July 2008). https://arxiv.org/abs/0807.1277
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401. https://doi.org/10.1137/0402034
- E. W. Weisstein, *Icosahedral Graph*, MathWorld. https://mathworld.wolfram.com/IcosahedralGraph.html
