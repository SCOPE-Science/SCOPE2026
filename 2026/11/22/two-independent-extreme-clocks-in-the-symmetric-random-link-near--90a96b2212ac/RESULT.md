# Two independent extreme clocks in the symmetric random-link nearest-neighbor forest

## Finding
Consider the complete graph on \(n\ge2\) labelled vertices, with independent identically distributed atomless edge weights having cumulative distribution function \(F\). Set \(T_e=-\log(1-F(X_e))\); these are independent unit-rate exponential variables and preserve every nearest-neighbor comparison almost surely. For a vertex \(v\), let \(L_v=\min_{e\ni v}T_e\), and let \(\mathcal R_n\) be the set of edges which are minimum incident edges at **both** endpoints. Define
\[
A_n=\max_v L_v,\qquad B_n=\max_{e\in\mathcal R_n}T_e,\qquad
b_n=\log\frac{n(n-1)}{2(2n-3)}.
\]
The set \(\mathcal R_n\) is nonempty, since the globally smallest edge belongs to it. For every pair of real numbers \(x,y\),
\[
\boxed{\lim_{n\to\infty}\Pr\bigl(nA_n-\log n\le x,\ (2n-3)B_n-b_n\le y\bigr)
=\exp(-e^{-x}-e^{-y}).}
\tag{1}
\]
Hence the two normalized maxima converge to **independent standard Gumbel** variables, even though they are computed from the same array of edge weights. More precisely, the numbers of vertices with minimum incident transformed weight exceeding \(u_n(x)=(\log n+x)/n\) and of mutual-nearest-neighbor edges exceeding \(t_n(y)=(b_n+y)/(2n-3)\) converge jointly to independent Poisson variables with means \(e^{-x}\) and \(e^{-y}\).

The proof supplies the exact finite exceedance factorial moments: for any matching \(M\) of \(k\) edges and \(t\ge0\),
\[
\Pr\bigl(\forall e\in M:\ e\in\mathcal R_n,\ T_e>t\bigr)
=\frac{\exp[-k(2n-2k-1)t]}{\prod_{j=1}^{k}(2n-2j-1)},
\quad 0\le k\le\lfloor n/2\rfloor.
\tag{2}
\]
This marked formula follows from a known unmarked simultaneous-pair identity and exponential memorylessness; it is an input to, **not an independently claimed priority contribution of**, the joint limit (1).

## Assumptions and scope
The graph is complete and undirected; each pair shares a single edge weight. All weights are iid with an atomless real-valued distribution. The transform \(T_e=-\log(1-F(X_e))\) is therefore an almost-surely order-preserving probability-integral transform; it provides a distribution-free hazard scale. There are no metric/triangle-inequality assumptions. Formulas (1) and its Poisson assertion concern \(n\to\infty\) with fixed real \(x,y\); for sufficiently large \(n\), both displayed thresholds are nonnegative. Formula (2) holds exactly for all stated finite sizes, with the empty product interpreted as one.

## Proof
**1. Marked matching factorial moments.** Fix a matching \(M\) of \(k\) prescribed edges with \(2k\) endpoints. There are exactly
\[
Q_{n,k}=2k(n-2k)+\binom{2k}{2}=k(2n-2k-1)
\]
other-or-selected edges meeting at least one of these endpoints. If all selected edges are reciprocal minima with weights exceeding \(t\), then every such incident edge has weight exceeding \(t\). This has probability \(e^{-Q_{n,k}t}\). By exponential memorylessness, after this event the residual edge clocks are iid unit exponentials. Uncover the residual edges by increasing value. At the first appearance of an edge touching any of the \(2k\) selected endpoints, the prescribed matching can succeed only if this edge is one of its \(k\) edges, an event of probability \(k/Q_{n,k}=1/(2n-2k-1)\). Remove those two endpoints; repeat on the remaining \(2(k-1)\) selected endpoints. This gives the exact product in (2).

Write \(J_n(t)=\sum_{e\in\mathcal R_n}\mathbf1\{T_e>t\}\). Any two reciprocal edges are vertex-disjoint. Since the number of ordered \(k\)-tuples of disjoint unoriented edges is \((n)_{2k}/2^k\), (2) gives
\[
\mathbb E(J_n(t))_{\underline k}
=\frac{(n)_{2k}}{2^k\prod_{j=1}^{k}(2n-2j-1)}
 e^{-k(2n-2k-1)t}.
\tag{3}
\]
For \(t=t_n(y)\), the \(k=1\) expression is exactly \(e^{-y}\). For each fixed \(k\), divide (3) by \(e^{-ky}\) and use \(t_n(y)=O(\log n/n)\); all remaining factors tend to one. Thus \(\mathbb E(J_n(t_n(y)))_{\underline k}\to e^{-ky}\).

**2. Rare isolated vertices.** Put \(I_n(u)=\sum_v\mathbf1\{L_v>u\}\). For \(r\) distinct specified vertices the condition is that all \(rn-r(r+1)/2\) distinct incident edges exceed \(u\). Therefore
\[
\mathbb E(I_n(u))_{\underline r}
=(n)_r\exp\bigl[-(rn-r(r+1)/2)u\bigr].
\tag{4}
\]
At \(u=u_n(x)\), these factorial moments tend to \(e^{-rx}\), the moments of \(\operatorname{Pois}(e^{-x})\).

**3. Joint factorial-moment factorization.** Fix integers \(r,k\ge0\). Consider an ordered \(r\)-tuple of candidate isolated vertices and an ordered \(k\)-tuple of distinct candidate reciprocal edges. First suppose the two candidate vertex sets are disjoint. Condition on the \(r\) vertices being isolated at \(u_n(x)\). The edge weights among their complement of \(m=n-r\) vertices remain independent unit exponentials, while every edge touching the conditioned vertices exceeds \(u_n(x)\). Whenever the selected reciprocal edge weights are at most \(u_n(x)\), their reciprocal status in the full graph is equivalent to reciprocal status within this complement.

Given the \(k\) selected edges are reciprocal in the complement and all exceed \(t_n(y)\), the successive times of the selected matching edges, after \(t_n(y)\), have waiting-time increments with rates \(j(2m-2j-1)\) for \(j=k,k-1,\ldots,1\). (At each step, the next edge touching the remaining selected endpoints must be the next prescribed edge.) Thus the expected largest selected weight minus \(t_n(y)\) is at most \(\sum_{j=1}^k[j(2m-2j-1)]^{-1}=O_k(1/n)\). Since \(u_n(x)-t_n(y)\sim(\log n)/(2n)\), Markov's inequality shows that the conditional probability of any selected reciprocal edge exceeding \(u_n(x)\) is \(O_k(1/\log n)\). Consequently, the prescribed joint probability differs by a relative \(o(1)\) from the product of its isolated-vertex probability and the marked matching probability for \(K_m\). Replacing \(m=n-r\) by \(n\) in the latter incurs relative \(o(1)\) by (2). Summing over disjoint configurations therefore gives \(e^{-rx-ky}+o(1)\).

For configurations in which an isolated vertex is also an endpoint of a prescribed reciprocal edge, that edge must itself exceed \(u_n(x)\). The preceding waiting-time bound, now applied in \(K_n\), makes this conditional event \(o(1)\) relative to the marked matching event. The remaining isolated-vertex candidates must have all edges to the \(n-O_{r,k}(1)\) wholly unmarked vertices exceeding \(u_n(x)\). Those edges are disjoint from the edges that determine the prescribed reciprocal matching, so their combined probability is at most \(O(n^{-(r-j)})\) when \(j\ge1\) candidate isolated vertices belong to matching endpoints. There are \(O(n^{r+2k-j})\) corresponding configurations and the marked matching probability is \(O(n^{-2k})\). Therefore the total overlapping contribution is \(o(1)\).

Together, for each fixed \(r,k\),
\[
\mathbb E[(I_n(u_n(x)))_{\underline r}(J_n(t_n(y)))_{\underline k}]
\longrightarrow e^{-rx-ky}.
\tag{5}
\]
These are the mixed factorial moments of independent Poisson variables, a moment-determinate law. Thus the asserted joint Poisson convergence holds. Finally, \(A_n\le u\) iff \(I_n(u)=0\), and \(B_n\le t\) iff \(J_n(t)=0\). Taking the joint zero probability gives (1). The proof is entirely finite-expectation and asymptotic-moment reasoning; no simulations are used to infer the infinite limit.

## Verification
The standalone Python-standard-library script `VERIFY.py` checks the exact unmarked matching formula by exhaustive edge-ranking enumeration for \(2\le n\le4\), independently checks falling-factorial moments, the number of distinct touched edges, the two-pair threshold identity, the isolated-vertex incidence count, and numerical normalization for growing \(n\). Its deterministic report is `VERIFY_OK 4123 deterministic assertions`. The proof above, not a finite sample, establishes the limiting joint distribution.

## Relationship to prior work
Cooper and Frieze (1995) introduce the symmetric random-weight nearest-neighbor graph and analyze its edge count and connectivity; their Theorems 1–4 do not state the two calibrated extremal clocks or their joint law. The publicly available *Exact mutual-nearest-neighbor component law in symmetric random-link graphs* gives precisely the unmarked simultaneous-pair probability, recovered from (2) at \(t=0\); that identity and the complete finite unmarked component distribution are **prior work**, not new here. Gupta and Iyer (initial arXiv posting 2006-04-27) establish Gumbel limits for longest nearest-neighbor links in **spatial geometric** point clouds, not iid edge-weight complete graphs and not joint reciprocal-edge/isolated-vertex limits. The marginal Gumbel law for the last isolated vertex in the exponential-edge Erdős–Rényi process is classical. The distinctive claim here is the coupled, distribution-free random-link two-clock law (1), with a mixed-factorial-moment proof establishing independence.

## Limitations
The result does not cover nonidentically distributed or dependent edge weights, geometric distances satisfying triangle inequalities, or growing numbers of extreme statistics. It proves weak convergence but no explicit finite-sample total-variation error rate for the bivariate law. The finite marked moment formula is a direct consequence of a known unmarked formula and memorylessness; it is not claimed as a separate discovery. Standard random-graph-process results might implicitly yield an equivalent joint statement, and the historical-priority search cannot establish uniqueness. Independent external validation has not been performed.

## References
1. C. Cooper and A. Frieze, *On the Connectivity of Random k-th Nearest Neighbour Graphs*, Combinatorics, Probability and Computing 4 (1995), 343–362. Full author manuscript: https://www.math.cmu.edu/~af1p/Texfiles/ok.pdf
2. B. Gupta and S. K. Iyer, *Criticality of the Exponential Rate of Decay for the Largest Nearest Neighbor Link in Random Geometric Graphs*, first publicly posted 2006-04-27, arXiv:math/0604599. https://arxiv.org/abs/math/0604599
3. *Exact mutual-nearest-neighbor component law in symmetric random-link graphs*, published mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-mutual-nearest-neighbor-component-law-in-symmetric-random--f51047a8a8b8
