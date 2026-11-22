# Sharp universal interval for the cluster-count maximum in site-percolated cactus graphs

## Finding
Let \(G\) be a finite, connected, simple cactus graph with \(n\ge2\) vertices, \(e\) edges, and simple cycles of lengths \(\ell_1,\ldots,\ell_c\), all at least three. Independently retain each vertex with probability \(p\in(0,1)\), retain all edges whose endpoints survive, and let \(N_p\) and \(C_p\) denote respectively the number of surviving vertices and the number of connected components of the induced graph (with zero components when the retained set is empty). Then
\[
\mu_G(p):=\mathbb E[C_p]=np-ep^2+\sum_{j=1}^{c}p^{\ell_j},\qquad
\operatorname{Cov}(N_p,C_p)=p(1-p)\left(n-2ep+\sum_{j=1}^{c}\ell_jp^{\ell_j-1}\right).
\]
With exactly two exceptions, the single-edge graph and the triangle, \(\mu_G\) has a *unique* critical point \(p_G\in(0,1)\), which is its strict global maximum. Equivalently, the displayed covariance is positive for \(0<p<p_G\) and negative for \(p_G<p<1\). In each exceptional graph it is strictly positive for every \(p\in(0,1)\).

Let \(\xi\) denote the unique root in \((2/5,41/100)\) of
\[
4\xi^3-8\xi+3=0, \qquad \xi=0.409279025863337\ldots.
\]
**The sharp, all-cactus extremal bounds are**
\[
\boxed{\xi<p_G\le\frac34.}
\]
The upper equality holds exactly for the three-vertex path. The lower bound is an unattained infimum, approached by a bouquet of \(t\) four-cycles meeting at one common vertex as \(t\to\infty\). Thus four-cycles, rather than triangles, generate the extremal low-density fragmentation peak.

## Assumptions and scope
A cactus graph is connected and has every edge in at most one simple cycle; different cycles may meet at vertices but never share an edge. Every simple cycle of an induced subgraph is a fully retained original cycle. All retention indicators are independent and identically distributed Bernoulli \(p\). The result is about *finite-graph site percolation*, not independent bond percolation or an infinite-volume percolation threshold. The number of vertices is at least two. Cycle lengths may repeat and cycle blocks may overlap at cut vertices. The only exceptional graphs within this domain are the single edge and the triangle.

## Proof
**1. Component identity and expectation.** For every vertex subset \(S\), the induced subgraph \(G[S]\) is a cactus. Its cycle-space rank equals the number of original cycles that are completely contained in \(S\). The Euler identity gives, pointwise,
\[
C_p=N_p-E_p+\sum_{j=1}^{c}I_j,
\]
where \(E_p\) is the number of induced edges and \(I_j\) indicates that every vertex of original cycle \(j\) survives. Taking expectations uses \(\mathbb E[N_p]=np\), \(\mathbb E[E_p]=ep^2\), and \(\mathbb E[I_j]=p^{\ell_j}\), yielding \(\mu_G\).

**2. Covariance/derivative identity.** For *any* statistic \(H\) of a Bernoulli-retained vertex set on \(n\) vertices,
\[
\frac{d}{dp}\mathbb E_p[H]=\frac{\operatorname{Cov}_p(N_p,H)}{p(1-p)}
\]
for \(0<p<1\). Indeed, differentiating the finite sum \(\sum_{S\subseteq V} H(S)p^{|S|}(1-p)^{n-|S|}\) gives a score \((|S|-np)/(p(1-p))\). Set \(H=C_p\), noting that \(H(S)\) is a fixed function of \(S\), and differentiate the preceding polynomial.

**3. One-crossing classification.** Put \(f_G(p)=\mu_G'(p)=n-2ep+\sum_j\ell_jp^{\ell_j-1}\). Its second derivative is
\[
f_G''(p)=\sum_j\ell_j(\ell_j-1)(\ell_j-2)p^{\ell_j-3}\ge0
\]
(strict for any cycle and \(p>0\)). If \(b\) is the number of bridge edges, the cactus block decomposition gives \(e=b+\sum_j\ell_j=n-1+c\), hence \(f_G(0)=n>0\) and \(f_G(1)=1-b-c\). For a tree with \(n\ge3\), \(f_G(1)=2-n<0\); for any cactus with \(b+c\ge2\), \(f_G(1)<0\). Convexity and the endpoint signs give exactly one zero in \((0,1)\), with a positive-to-negative sign change. The remaining cycle-only cases have \(G=C_\ell\) and \(f_G(p)=\ell(1-2p+p^{\ell-1})\). When \(\ell\ge4\), \(f_G(1)=0\) but \(f_G'(1)=\ell(\ell-3)>0\), so \(f_G<0\) immediately to the left of 1; convexity again gives exactly one interior crossing. For \(\ell=3\), \(f_G(p)=3(1-p)^2>0\). For the single edge, \(f_G(p)=2(1-p)>0\). These exhaust connected cacti with at least two vertices.

**4. The sharp lower bound.** Express \(n=1+b+\sum_j(\ell_j-1)\) and \(e=b+\sum_j\ell_j\). Then
\[
f_G(p)=1+b(1-2p)+\sum_j g_{\ell_j}(p),\qquad
 g_\ell(p)=\ell-1-2\ell p+\ell p^{\ell-1}.
\]
The polynomial \(g_4(p)=3-8p+4p^3\) has exactly one zero \(\xi\) in \((2/5,41/100)\), since its derivative is negative on this interval and the endpoint values have opposite signs. At \(p=\xi\), \(g_4(\xi)=0\) and \(1-2\xi>0\). For \(\ell=3,5\), \(g_\ell\) is decreasing on \([0,41/100]\) and direct rational substitution gives \(g_3(41/100)>0\) and \(g_5(41/100)>0\). For every \(\ell\ge6\),
\[
g_\ell(\xi)=\ell(1-2\xi+\xi^{\ell-1})-1 > 6\left(1-2\frac{41}{100}\right)-1=\frac2{25}>0.
\]
Therefore \(f_G(\xi)\ge1>0\); each admissible interior root obeys \(p_G>\xi\). For a bouquet of \(t\) four-cycles, \(n=3t+1\), \(e=4t\), and \(f_G(p)=1+t g_4(p)\). Its sole interior zero tends to \(\xi\), proving sharpness of the infimum.

**5. The sharp upper bound.** At \(p=3/4\), \(1-2p=-1/2\), \(g_3(p)=-13/16\), and for every \(\ell\ge4\), \(p^{\ell-1}\le27/64<1/2\), hence \(g_\ell(p)<-1\). Consequently,
\[
f_G(3/4)\le1-\frac b2-\frac{13c}{16}.
\]
When \(c=0\), a nonexceptional tree has \(b=n-1\ge2\), so this is nonpositive, with equality exactly at the three-vertex path. When \(c\ge2\), it is strictly negative; when \(c=1,b\ge1\), it is strictly negative. When \(c=1,b=0\), the graph is a pure cycle, and for \(\ell\ge4\) the stronger estimate \(f_G(3/4)=1+g_\ell(3/4)<0\) applies. The triangle is already excluded. The unique root therefore satisfies \(p_G\le3/4\), with the asserted equality case.

## Verification
The accompanying standard-library Python file `checker.py` exhaustively evaluates induced vertex subsets and exact polynomial coefficients on 746 connected cactus graphs, drawn from every labeled graph through five vertices plus a deterministic sample of six-vertex graphs. It verifies the component expectation and Bernoulli-score covariance identities using integer arithmetic. It also checks the predicted root intervals numerically on bouquets of four-cycles with 2 through 59 blocks; these finite numerical tests are ancillary, not a proof of the sharp infinite-family limit. The script was run directly from the delivered file contents and completed successfully.

## Relationship to prior work
Tittmann, Averbouch and Makowsky introduced the full subgraph-component polynomial, including the vertex-failure model and a cycle recurrence; it contains the information needed in principle to compute these moments graph by graph. Liao and Hou established graph-reconstruction properties for cycles, tadpoles, and friendship graphs from that polynomial. Those foundational results are not claimed as new. The present statement extracts a direct cactus-wide exact first moment and proves a shape-independent **single-crossing classification and sharp all-cactus extremal interval**, including its four-cycle infimum. It is different from bond-percolation bridge-count laws and from fixed-number-of-balls occupancy on a tree. A generic generating function's existence alone does not give the claimed extremal theorem. No claim of priority beyond the inspected sources is made.

## Limitations
The result requires independent homogeneous site retention and a connected cactus host; it does not assert comparable unimodality for arbitrary graphs. For example, on \(K_4\) the expected component count is \(1-(1-p)^4\), strictly increasing throughout \((0,1)\), demonstrating that the cactus restriction matters. The maximizer of the **expected** component count is not a critical probability for a giant component or a typical sample-path event. The joint distribution and variance of the component count generally retain further graph-structure dependence. Historical originality needs independent review; a missing older equivalent identity remains possible.

## References
1. P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, public arXiv posting 2008-12-22, arXiv:0812.4147, https://arxiv.org/abs/0812.4147; European Journal of Combinatorics 32 (2011), 954–974.
2. Y. Liao, Y. Hou, *Note on the Subgraph Component Polynomial*, arXiv:1311.6856 (first public 2013-11-27), Electronic Journal of Combinatorics 21(3) (2014), P3.27; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v21i3p27.
