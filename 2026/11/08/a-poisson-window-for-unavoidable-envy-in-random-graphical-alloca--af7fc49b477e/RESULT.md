# A Poisson window for unavoidable envy in random graphical allocations

## Finding

Let \(G=(V,E)\) be a finite simple undirected graph. Construct a fair-division instance with one indivisible good for each edge and an additive binary valuation for each agent-vertex: \(v_i(e)=1\) if and only if \(i\in e\). For every complete allocation \(A\), let
\[
\mathcal D(A)=|\{i\in V:\exists j\in V,\ v_i(A_j)>v_i(A_i)\}|.
\]
Write \(T(G)\) for the number of connected components which are trees with at least two vertices. Then
\[
\min_{A\text{ complete}}\mathcal D(A)=T(G).
\]
The minimum can be achieved by an allocation in which every edge-good is assigned to an endpoint, hence with maximum possible utilitarian welfare \(|E|\).

For fixed \(c\in\mathbb R\), let \(G_n\) be an Erdős–Rényi graph with independent edges of probability
\[
p_n=\frac{\log n+\log\log n+c}{2n},
\]
for sufficiently large \(n\) so that \(0<p_n<1\). The number of agents who must envy someone, even in an optimal allocation, converges in law:
\[
\min_A\mathcal D(A)=T(G_n)\ \xrightarrow{d}\ \operatorname{Poisson}(e^{-c}/4).
\]
In particular,
\[
\Pr(\text{a complete envy-free allocation exists})\longrightarrow
\exp(-e^{-c}/4).
\]
Thus this sparse-market model has an explicit critical window for zero unavoidable envy, well before the random graph becomes connected.

## Assumptions and scope

Agents are all graph vertices, including isolates. Every undirected edge represents exactly one distinct item, each valued at one by each endpoint and at zero by all other agents; no parallel edges, chores, budgets, transfers or random utilities are allowed. Every good must be assigned to exactly one agent, including possibly a non-endpoint. Envy is strict and ordinary (not EF1 or EFX); an agent is counted once if it envies one or more other agents. The probability space is the labeled simple Erdős–Rényi graph, not randomly selected allocations, and the theorem concerns the optimum number of envious agents. Logs are natural. The random-graph conclusion holds for each fixed real \(c\) as \(n\to\infty\).

## Proof

**Deterministic exact optimum.** Fix a nontrivial tree component \(H\) with \(k\) vertices and \(k-1\) edge-goods. If every vertex of \(H\) were nonenvious, each would have to receive at least one incident edge-good: otherwise, for any incident edge, whoever receives it gets a bundle that vertex strictly values more than its own empty-valued bundle. Because one good cannot supply positive utility to more than one recipient, the \(k\) vertices cannot all receive positive utility from only \(k-1\) goods. This argument remains valid when goods are assigned to agents outside \(H\). Distinct tree components force distinct envious agents, giving \(\mathcal D(A)\ge T(G)\) for every allocation.

Conversely, in every nontrivial tree component, choose a root and orient all edges away from it, assigning each edge-good to its head. All vertices except the root have incoming edges; the root is the only vertex with no positively valued good. In each connected component containing a cycle, orient one fixed cycle cyclically, then orient all the remaining edges of a spanning unicyclic subgraph away from this cycle; assign any surplus edges arbitrarily to an endpoint. Each vertex then has at least one incoming edge. An isolated vertex values no good and envies nobody. In a *simple* graph, an agent values at most one good in any *other* agent's bundle, because at most one edge joins the two corresponding vertices. Accordingly any agent who receives at least one incident good is nonenvious: its own utility is at least one, whereas its value for any other particular agent's bundle is at most one. Exactly one root per nontrivial tree component can be envious, and no other agent is envious. All goods go to endpoints, giving welfare \(|E|\), the maximum possible since an item's social contribution is at most one. This proves the deterministic identity and simultaneous welfare optimality.

**Isolated-edge components and factorial moments.** Put \(\mu_n=np_n\), and let \(Z_n\) count components consisting of one isolated edge and its two endpoints. For each fixed positive integer \(r\), selecting an ordered family of disjoint vertex-pairs and requiring the selected edges to be present and all other edges incident to the \(2r\) selected vertices to be absent gives exactly
\[
\mathbb E[(Z_n)_r]=\frac{(n)_{2r}}{2^r}p_n^r(1-p_n)^{2r(n-r-1)},
\]
where \((x)_r\) is the falling factorial. Because
\[
2\mu_n=\log n+\log\log n+c,
\]
the expression tends to \((e^{-c}/4)^r\). Convergence of all nonnegative integer-valued factorial moments to those of a Poisson law implies
\[
Z_n\xrightarrow{d}\operatorname{Poisson}(e^{-c}/4).
\]
For clarity, the exponent \(2r(n-r-1)\) counts all forbidden edges touching the selected vertices except the \(r\) present paired edges.

**Larger tree components vanish.** Let \(N_{n,k}\) count tree components of order \(k\ge3\). Cayley's formula and independence give
\[
\mathbb E N_{n,k}=\binom nk k^{k-2}p_n^{k-1}
(1-p_n)^{k(n-k)+\binom k2-k+1}.
\]
For each fixed \(k\in\{3,4\}\), this is
\[
O\bigl(n\mu_n^{k-1}e^{-k\mu_n}\bigr)=o(1).
\]
For \(5\le k\le n/2\), discarding the required absences inside the selected set and using \(\binom nk\le(en/k)^k\) gives
\[
\mathbb E N_{n,k}\le\frac{n}{\mu_n k^2}
\left(e\mu_n e^{-\mu_n/2}\right)^k.
\]
Since \(e\mu_n e^{-\mu_n/2}=O(n^{-1/4}(\log n)^{3/4})\), the sum of this bound from \(k=5\) to \(\lfloor n/2\rfloor\) is \(o(1)\). If \(k>n/2\) and a \(k\)-set forms a tree component, its induced subgraph has exactly \(k-1\) edges. Yet this induced edge count has binomial mean \(\binom{k}{2}p_n=\Omega(n\log n)\). A binomial lower-tail Chernoff bound is \(\exp[-\Omega(n\log n)]\), uniformly over such \(k\)-sets. The union bound over at most \(2^n\) vertex sets shows there is no such component with probability tending to one. Therefore \(\mathbb E\sum_{k\ge3}N_{n,k}\to0\), and
\[
T(G_n)-Z_n\xrightarrow{p}0.
\]
Combining with the Poisson limit for \(Z_n\) proves the distributional result. Since the random variables are integer-valued, convergence to the discrete Poisson law also gives convergence of the zero-event probabilities.

## Verification

The accompanying standalone `verify_envy.py` independently computes the number of nontrivial tree components and the minimum envious-agent count via direct bundle comparisons. It exhausts all \(1099\) labeled simple graphs through five vertices under edge-endpoint allocations and all \(75\) labeled simple graphs through four vertices under *arbitrary complete* good-to-agent allocations; all comparisons passed. Further sampled random graphs and exact finite factorial moments support the scale of the limiting law. These finite experiments are not a proof of the infinite claim: the preceding factorial-moment and uniform component bounds are the proof.

To reproduce: run `python verify_envy.py` using Python 3 without third-party dependencies. The computational checks are independent of the random-graph limit proof.

## Relationship to prior work

Misra and Sethia, *Envy-Free and Efficient Allocations for Graphical Valuations* (arXiv:2410.14272, first public 2024-10-18), already give the binary graphical envy-free **existence** condition, including the non-tree-component criterion and its constructive orientation. That deterministic existence criterion, the graph orientation device and the idea of assigning all items to endpoints are **not claimed as new**. The additional deterministic content here is the exact optimal count of envious agents when EF existence fails and simultaneous welfare attainment. The main contribution is the ensuing Poisson law and explicit critical window for that count in random simple graphs.

Manurangsi, *Envy-Free Allocations for Random Non-Additive Valuations* (arXiv:2610.34434, first public 2026-10-25), studies fixed-agent random-permutation valuations and an existence law with the number of goods tending to infinity. It motivates the random-market question but does not concern the present growing-agent random binary graph model. Classical Erdős–Rényi isolated-component/Poisson methods underlie the random-graph step. The full text of Manurangsi's paper was not available for inspection; only its public metadata and abstract were compared. No priority or comprehensive novelty claim beyond the specified contribution is asserted.

## Limitations

The count identity depends critically on binary symmetric edge goods and a simple graph. With parallel edges, a vertex can value multiple goods in one other agent's bundle, invalidating the nonenvy argument. The probability theorem studies graph randomness and **optimal**, not random, good assignments. It does not extend to arbitrary additive valuations, correlated random graphs, weighted edges, EFX, or strategic mechanisms. The deterministic envy-free existence criterion predates this work, and the probability calculation uses standard random-graph techniques; equivalent unindexed critical-window results remain an originality risk. Independent validation has not been performed.

## References

- N. Misra and A. Sethia, *Envy-Free and Efficient Allocations for Graphical Valuations* (2024), arXiv:2410.14272, https://arxiv.org/abs/2410.14272.
- P. Manurangsi, *Envy-Free Allocations for Random Non-Additive Valuations* (2026), arXiv:2610.34434, https://arxiv.org/abs/2610.34434.
- G. Bénadè, D. Halpern, A. Psomas and P. Verma, *On the Existence of Envy-Free Allocations Beyond Additive Valuations* (2023), arXiv:2307.09648, https://arxiv.org/abs/2307.09648.
- B. Bollobás, *Random Graphs*, 2nd edition, Cambridge University Press (2001): classical Poisson convergence of small isolated tree component counts; the specialized calculation above is included in full.
