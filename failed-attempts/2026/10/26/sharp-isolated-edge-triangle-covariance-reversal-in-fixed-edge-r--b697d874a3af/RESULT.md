# Sharp isolated-edge/triangle covariance reversal in fixed-edge random graphs

## Finding
For every integer \(n\ge5\), sample a labeled simple graph uniformly from \(G(n,m)\), where \(0\le m\le\binom n2\). Let \(S\) count components consisting of a single edge and its two endpoints (isolated edges, or \(K_2\)-components), and let \(T\) count copies of the triangle \(K_3\), whether or not those triangles form components.

Set \(M=\binom{n-2}{2}\) and \(h_n=\lfloor(n+3)/2\rfloor\). Then the **complete covariance-sign classification** is
\[
\operatorname{sgn}\!\left(\operatorname{Cov}_{G(n,m)}(S,T)\right)=\begin{cases}
-1,&3\le m<h_n,\\
+1,&h_n\le m\le M+1,\\
0,&\text{otherwise}.
\end{cases}
\]
Both nonzero-sign ranges are strict; in particular, there is no nontrivial zero-covariance edge count. An exact rational expression is supplied below.

In contrast, for every \(0<p<1\) the independent-edge model satisfies
\[
\operatorname{Cov}_{G(n,p)}(S,T)
=-\binom n2(n-2)^2p^4(1-p)^{2n-4}<0.
\]
Thus matching the expected number of edges by setting \(p=m/\binom n2\) gives opposite covariance signs for every integer \(h_n\le m\le M+1\).

Moreover, whenever the integer sequence \(m=m(n)\) satisfies \(2m/n\to c\in(0,\infty)\),
\[
\operatorname{Cov}_{G(n,m)}(S,T)\longrightarrow
\frac12c^3(c-1)e^{-2c}.
\]
The sharp finite threshold therefore converges to the mean-degree-one regime in sparse random graphs.

## Assumptions and scope
Graphs are simple, undirected, labeled on \([n]\); \(S\) counts isolated **edge components**, not edges absent from triangles or isolated vertices. \(T\) counts all noninduced triangles, including triangles attached to other edges. For \(n<5\), these two counts cannot both be nonzero for the same edge count, so their covariance vanishes throughout; the stated nonzero classification begins at \(n=5\). The binomial coefficient \(\binom ab\) is zero for an out-of-range lower index. Write \((a)_r=a(a-1)\cdots(a-r+1)\) for the falling factorial.

## Proof
**1. Exact moments.** Set \(N=\binom n2\), \(M=\binom{n-2}{2}\), and \(Q=\binom Nm\). Fix an unordered pair \(e\) of vertices. The event that \(e\) is an isolated edge forces \(e\) present, all other edges incident to either endpoint absent, and the other \(m-1\) edges chosen from the \(M\) pairs among the remaining vertices. Hence
\[
\mathbb ES=N\frac{\binom M{m-1}}Q.
\]
For a fixed triangle all three edges must be present, and the other edges are arbitrary, so
\[
\mathbb ET=\binom n3\frac{\binom{N-3}{m-3}}Q.
\]
A triangle that shares even one vertex with an isolated edge is impossible. For disjoint vertex sets, the four required edges are the isolated edge and the triangle's three edges; the other \(m-4\) edges must lie in the remaining \(M-3\) pairs. Therefore
\[
\mathbb E(ST)=N\binom{n-2}{3}\frac{\binom{M-3}{m-4}}Q.
\]
These identities determine the covariance for **every** admissible \(n,m\), including all boundary cases, by subtraction.

**2. Strict sign and cutoff.** For \(n\ge5\) and \(3\le m\le M+1\), both \(\mathbb ES\) and \(\mathbb ET\) are positive. Conditional on a fixed isolated edge, the residual graph is exactly \(G(n-2,m-1)\). Thus
\[
\frac{\mathbb E[T\mid e\text{ isolated}]}{\mathbb ET}
=\frac{\binom{n-2}{3}}{\binom n3}
  \frac{(m-1)_3}{(m)_3}\frac{(N)_3}{(M)_3}
=K_n\frac{m-3}{m},
\qquad
K_n=\frac{(n+1)(n^2-n-4)}{(n-1)(n^2-5n+2)}.
\]
The identity also holds at \(m=3\), where the conditional triangle count is zero. By exchangeability,
\[
\operatorname{Cov}(S,T)=\mathbb ES\,\mathbb ET
\left(K_n\frac{m-3}{m}-1\right).
\]
For \(n\ge5\), \(K_n>1\). The sign changes at the real number
\[
\tau_n=\frac{3K_n}{K_n-1}
=\frac{3(n+1)(n^2-n-4)}{2(3n^2-6n-1)}.
\]
For even \(n\ge6\), direct subtraction gives
\[
\tau_n-\frac n2=\frac{(n-3)(3n+2)}{3n^2-6n-1}>0,
\qquad \tau_n-\frac{n+2}{2}=-\frac{n+5}{3n^2-6n-1}<0.
\]
For odd \(n\ge5\), it gives
\[
\tau_n-\frac{n+1}{2}=\frac{(n+1)(3n-11)}{2(3n^2-6n-1)}>0,
\qquad\tau_n-\frac{n+3}{2}=-\frac{3n^2-4n+9}{2(3n^2-6n-1)}<0.
\]
Consequently \(\tau_n\) lies strictly between consecutive integers and the first positive-covariance value is \(m=h_n\). If \(m<3\), no triangle occurs; if \(m>M+1\), an isolated edge cannot occur. These are precisely the remaining zero cases.

**3. Independent-edge contrast.** In \(G(n,p)\), a prescribed pair is an isolated edge with probability \(p(1-p)^{2n-4}\). A fixed triangle disjoint from that pair occurs independently, whereas one meeting the pair cannot occur simultaneously. There are \(\binom n3-\binom{n-2}{3}=(n-2)^2\) intersecting triangles for each possible isolated edge. Summing covariance contributions over all edge/triangle pairs proves the displayed strictly negative formula.

**4. Sparse limit.** If \(2m/n\to c>0\), conditioning on a selected edge gives the exact identity
\[
\Pr(e\text{ is isolated})=\frac mN\prod_{j=0}^{m-2}\frac{M-j}{N-1-j}.
\]
Since \(m=O(n)\), \(M=N-(2n-3)\), and the logarithm of the product tends to \(-2c\), the fixed-edge hypergeometric probabilities give \(\mathbb ES/n\to(c/2)e^{-2c}\). Directly, \(\mathbb ET=\binom n3(m)_3/(N)_3\to c^3/6\). Algebraically \(K_n=1+6/n+O(n^{-2})\), while \(3/m=6/(cn)+o(n^{-1})\). Hence
\[
n\left(K_n\frac{m-3}m-1\right)\to6\left(1-\frac1c\right).
\]
Multiplying the three limits in the exact covariance factorization yields \(c^3(c-1)e^{-2c}/2\). No claim of convergence in distribution is made.

## Verification
Run `python CHECK.py` using Python 3.10 or newer; no external libraries are required. The script enumerates every labeled graph through six vertices and compares the exact moments \(\mathbb ES\), \(\mathbb ET\), \(\mathbb E(ST)\) and covariance against direct binomial counting formulas. It also checks the sign and rational factorization across selected edge counts for every \(2\le n<55\). In the recorded execution, **3,955 exact assertions passed**. This is supplementary finite verification, not a substitute for the all-integer proof above. For example, at \(n=5\) the covariance is \(-1/48\) at \(m=3\) and \(2/63\) at \(m=4\).

## Relationship to prior work
Classical random-graph methods count triangles and small subgraphs and study their deviations. Kim–Vu (2004) studies large triangle-count deviations; Ellis–Ferry (2010) develops subgraph-overlap variance formulas under independent edges; Goldschmidt–Griffiths–Scott (2019) treats noninduced subgraph-count deviations under both fixed and independent edge numbers. These tools provide background but the inspected material does not state the present **component-count versus triangle-count finite sign classification**. The component indicator is not the noninduced count of \(K_2\): it requires all incident exterior edges absent. A published identity concerning covariance of the *total* component count with triangle count under independent bond percolation likewise does not imply this component-size-specific fixed-edge result. Novelty concerns the explicit threshold and contrast, not the elementary random-graph sampling model or binomial counting identities.

## Limitations
The result addresses covariance only, not monotone stochastic ordering or a joint limit theorem. Positivity does not mean positive dependence in every stronger sense. All analytic statements are proved for the specified models; historical priority remains provisional because older general covariance/component-count literature could contain an equivalent result. Some historical publisher articles were not accessible in complete full text. Nothing here constitutes independent mathematical certification.

## References
1. Kim, J. H., and Vu, V. H. (2004). *Divide and conquer martingales and the number of triangles in a random graph*. Random Structures & Algorithms 24, 166–174. DOI: `10.1002/rsa.10113` (publisher first-public date 2004-01-14).
2. Ellis, R. B., and Ferry, J. P. (2010). *Variance of the subgraph count for sparse Erdős–Rényi graphs*. Discrete Applied Mathematics 158, 649–658. DOI: `10.1016/j.dam.2009.11.012`.
3. Goldschmidt, C., Griffiths, S., and Scott, A. (2019). *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*. `arXiv:1902.06830` (first posted 2019-02-18).
