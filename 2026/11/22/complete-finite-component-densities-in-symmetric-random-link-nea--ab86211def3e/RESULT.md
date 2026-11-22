# Complete finite-component densities in symmetric random-link nearest-neighbor forests

## Finding

Assign independent identically distributed atomless edge weights to the complete graph on \(n\ge2\) labelled vertices. Each vertex selects its incident edge of least weight, and keep the union of all selected undirected edges. For each integer \(k\ge2\), let \(C_{n,k}\) count connected components containing exactly \(k\) vertices. Then, jointly for every fixed finite collection of sizes,
\[
\frac{C_{n,k}}{n}\xrightarrow[n\to\infty]{L^1}c_k,
\qquad
c_k=\frac{k-1}{2}\int_0^1u e^{-2u}\bigl(1-e^{-u}\bigr)^{k-2}\,du.
\]
In particular,
\[
c_2=\frac{1-3e^{-2}}8,
\qquad c_3=\frac{5-27e^{-2}+16e^{-3}}{36},
\qquad \sum_{k\ge2}c_k=\frac14,
\qquad \sum_{k\ge2} k c_k=1.
\]
A uniformly chosen vertex has component size converging to the proper discrete distribution \(\Pr(S=k)=k c_k\), and a uniformly chosen component has size converging to \(\Pr(T=k)=4c_k\). Both conclusions hold conditionally on the random forest in probability, with convergence in total variation of the discrete component-size distributions. In particular, the largest component has size \(o_{\Pr}(n)\), even though the graph contains a linear number of edges.

## Assumptions and scope

Every unordered pair receives one common undirected weight. Weights are independent, identically distributed and atomless; ties consequently occur with probability zero. Their actual numerical distribution is immaterial because the entire graph depends only on their ranks. A component of size \(k\) means a weak component in the directed nearest-neighbor network, equivalently an ordinary component of the union of chosen edges. There are no singleton components because every vertex chooses an edge. The limit is along integers \(n\to\infty\), with each displayed size \(k\) fixed before that limit. The limiting mass identity is an assertion about the whole family of these fixed-size limits, not a claim of uniform convergence over sizes from the outset.

## Proof

**1. Edge-order equivalence.** Reveal the edge weights in increasing order. Retain an edge exactly if at least one endpoint has not appeared in an earlier revealed edge. That edge is the first (hence minimum) edge incident to each of its previously unseen endpoints. Conversely, every selected minimum incident edge is retained at its first appearance. The retained undirected graph is therefore exactly the original nearest-neighbor graph. Every retained edge connects one or two previously unseen vertices to a component, and no retained edge connects two already seen vertices. Consequently the retained graph is a forest. The first edge joining two unseen vertices creates a component of size two; later retained edges each add a single new vertex to an existing component. Distinct existing components can never merge.

**2. Exact finite-state jump rates.** Apply the common increasing transformation of the edge-weight ranks to independent exponential clocks of rate \(1/n\). Let \(U_n(t)\) denote the number of vertices with no incident clock yet rung, and let \(C_{n,k}(t)\) count the components of size \(k\) already formed. The clocks associated with unrevealed edges remain independent exponential clocks with their original residual rates. Given the current state with \(u\) unseen vertices, an unseen–unseen edge rings at total rate \(u(u-1)/(2n)\) and creates one new size-two component while reducing \(u\) by two. Edges joining an unseen vertex to a component of size \(j\) ring at rate \(uj/n\), reducing \(u\) by one and moving that component from size \(j\) to size \(j+1\). Edges between seen vertices are ignored and change no state. This description is an exact Markov process; its total state-changing rate never exceeds \(n/2\).

Put \(Z_n(t)=U_n(t)/n\), \(X_{n,k}(t)=C_{n,k}(t)/n\), with initial values \(Z_n(0)=1\) and \(X_{n,k}(0)=0\). The predictable drifts satisfy
\[
 b_{Z,n}=-\frac{n-1}{n}Z_n,
\quad b_{2,n}=\frac12 Z_n(Z_n-1/n)-2Z_nX_{n,2},
\]
\[
 b_{k,n}=Z_n((k-1)X_{n,k-1}-kX_{n,k}),\qquad k\ge3.
\]
Each coordinate jump has size at most \(1/n\) (and \(2/n\) for \(Z_n\)). On every bounded time interval \([0,T]\), the squared martingale supremum is \(O(T/n)\) by the predictable quadratic variation and Doob's inequality. For any fixed \(K,T\), the drift functions are Lipschitz on the bounded coordinate domain, with an \(O(1/n)\) discrepancy from their limiting counterparts. The integral equations and Grönwall's lemma therefore give convergence in probability, uniformly for \(t\in[0,T]\), of \((Z_n,X_{n,2},\ldots,X_{n,K})\) to the unique deterministic solution
\[
 z'=-z,\quad z(0)=1;\qquad
 x'_2=\tfrac12z^2-2zx_2;
\quad x'_k=z((k-1)x_{k-1}-kx_k)\ (k\ge3),\quad x_k(0)=0.
\]
The same boundedness upgrades fixed-coordinate convergence to \(L^1\).

**3. Solution by marked growth.** Since \(z(t)=e^{-t}\), size-two components are born at density rate \(e^{-2s}/2\) at time \(s\). Each vertex of a component gives rise to an additional vertex at instantaneous rate \(e^{-t}\) thereafter. Thus, conditional on creation at time \(s\), its population at time \(t\ge s\) follows a linear pure-birth process started from two ancestors. Write
\[
 p_{s,t}=\exp\!\left(-\int_s^t e^{-v}\,dv\right)
=\exp\!\left(-e^{-s}+e^{-t}\right).
\]
The population distribution, verified by the linear birth-process forward equations (or by the product of two geometric generating functions), is
\[
 \Pr\{N_s(t)=k\}=(k-1)p_{s,t}^{2}(1-p_{s,t})^{k-2},\qquad k\ge2.
\]
Superposition of component births yields the unique ODE solution
\[
 x_k(t)=\frac{k-1}{2}\int_0^t e^{-2s}p_{s,t}^2(1-p_{s,t})^{k-2}\,ds.
\]
Letting \(t\to\infty\) and setting \(u=e^{-s}\) produces \(x_k(\infty)=c_k\) as stated.

**4. Passing from finite times to the final graph.** Every vertex is seen in finite time almost surely. Each state-changing edge after time \(T\) uses at least one then-unseen vertex, hence at most \(U_n(T)\) further state-changing edges occur. Each changes any fixed \(C_{n,k}\) by absolute value at most one, so
\[
 |C_{n,k}(\infty)-C_{n,k}(T)|/n\le U_n(T)/n.
\]
The exact drift of \(U_n\), or the probability a specified vertex has no incident exponential clock by time \(T\), gives
\[
 \mathbb E\bigl[U_n(T)/n\bigr]=e^{-(n-1)T/n}.
\]
For fixed \(T\), step 2 gives convergence to \(x_k(T)\) in \(L^1\); taking \(n\to\infty\) and then \(T\to\infty\), using \(x_k(T)\to c_k\) and the preceding bound, proves the first assertion.

**5. Complete normalization and typical-component limits.** With \(q(u)=1-e^{-u}\), monotone convergence and the geometric generating identities
\[
 \sum_{k\ge2}(k-1)q^{k-2}=(1-q)^{-2},\qquad
 \sum_{k\ge2}k(k-1)q^{k-2}=2(1-q)^{-3},
\]
show
\[
 \sum_{k\ge2}c_k=\frac12\int_0^1u\,du=\frac14,\qquad
 \sum_{k\ge2}k c_k=\int_0^1u e^u\,du=1.
\]
Every sample partitions all \(n\) vertices, so \(\sum_{k\ge2}kC_{n,k}/n=1\). Fixed-size convergence together with \(\sum_{k\ge2}k c_k=1\) implies convergence in \(\ell^1\) in probability of the random probability mass function \(kC_{n,k}/n\) to \(k c_k\): for any \(K\), the total tail in either mass function is one minus the first \(K\) terms, and these finitely many terms converge. Likewise \(\sum_{k>K} C_{n,k}/n\le1/(K+1)\) shows \(\sum_k C_{n,k}/n\to1/4\), so the empirical component-uniform size distribution \(C_{n,k}/\sum_j C_{n,j}\) tends in total variation to \(4c_k\). Finally, for any fixed \(\varepsilon>0\), a component of size at least \(\varepsilon n\) would force at least \(\varepsilon\) of the empirical vertex mass above every fixed \(K\); the established tightness makes that probability vanish. Thus the largest component is \(o_{\Pr}(n)\).

## Verification

`VERIFY.py` requires only Python's standard library. It independently enumerates every strict edge ordering of the complete graphs on two through four vertices and checks the expected component-size counts against the exact unseen-vertex Markov recurrence. It verifies exact mass conservation and the previously known total-component expectation at sizes two through twenty-two, and performs deterministic numerical-quadrature comparisons between the finite Markov recurrence and the displayed limiting densities at sizes 350 and 700. It checks numerical versions of the two normalization identities and the explicit value of \(c_2\). The saved invocation returned `VERIFY_OK 121 assertions`. Enumeration and quadrature corroborate finite and limiting formulas but do not replace the infinite-size martingale/ODE proof.

## Relationship to prior work

Cooper and Frieze (1995, publicly available author manuscript) define precisely the same independent-edge nearest-neighbor model as their \(k=1\) graph, and prove its approximately \(3n/4\) edge count. Their theorem statements then address connectivity for \(k\ge2\), rather than a size-resolved \(k=1\) component census. Berikkyzy and coauthors (first arXiv posting August 1, 2016) describe the equivalent edge-order forest-building process and give complete-graph total-component information, the complete-bipartite component-count law, and the general expectation formula. Their full text does not state the limiting size-by-size component densities or their all-mass normalization. The published result *Exact mutual-nearest-neighbor component law in symmetric random-link graphs* gives the complete **number**-of-components distribution for the symmetric model, not the distribution of individual component sizes; neither its total-count moments nor the known mean alone determine the present size profile. Kozakova, Meester and Nanda (2006) study component sizes in Euclidean Poisson nearest-neighbor graphs, where edge lengths are geometrically dependent, so that model is not equivalent to the complete-graph independent random-link model. The new claim is limited to the size-resolved law and its directly proved conditional sampling consequences. Historical priority beyond these comparisons has not been independently certified.

## Limitations

The full result uses the complete graph, a common shared undirected weight for each edge, and independent identically distributed atomless edge weights. It does not address geometric nearest-neighbor graphs, independently directed weights, nonidentical edge distributions, or the exact order of the largest component (only sublinearity is proved). A component-size distribution from an earlier unlocated general theorem could overlap with these conclusions.

## References

1. C. Cooper and A. Frieze, *On the connectivity of random k-th nearest neighbour graphs*, Combinatorics, Probability and Computing 4 (1995), 343–362. Lawful author manuscript dated June 15, 1995: https://www.math.cmu.edu/~af1p/Texfiles/ok.pdf
2. Z. Berikkyzy, S. Butler, J. Cummings, K. Heysse, P. Horn, R. Luo, and B. Moran, *A forest building process on simple graphs*, arXiv first submitted August 1, 2016: https://arxiv.org/abs/1608.00335
3. *Exact mutual-nearest-neighbor component law in symmetric random-link graphs*, published mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-mutual-nearest-neighbor-component-law-in-symmetric-random--f51047a8a8b8
4. I. Kozakova, R. W. J. Meester, and S. Nanda, *The size of components in continuum nearest-neighbor graphs*, Annals of Probability 34 (2006), 528–538, https://doi.org/10.1214/009117905000000729
