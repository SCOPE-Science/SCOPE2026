# Every two seed locations on a finite epidemic path have one variance-ranking crossover

## Finding
Let \(P_n\) be the simple path on \(n\ge3\) vertices, and let its \(n-1\) edges be open independently with a common probability \(p\in(0,1)\). Starting from a single prescribed source, infect every vertex in its open-edge connected component. Let \(X_a(p)\) be the final infected count when the source has \(a\) edges to its nearer endpoint and \(m-a\) edges to its farther endpoint, where \(m=n-1\) and \(0\le a\le\lfloor m/2\rfloor\).

**Theorem.** For every integer \(m\ge2\) and every pair of distinct positions \(0\le a<c\le\lfloor m/2\rfloor\), there is exactly one \(p_{m;a,c}\in(0,1)\) such that
\[
\operatorname{Var}(X_a(p_{m;a,c}))=\operatorname{Var}(X_c(p_{m;a,c})).
\]
This crossing is simple. Below it the more central source has **strictly greater** final-outbreak variance, and above it the more peripheral source has **strictly greater** variance:
\[
\begin{aligned}
0<p<p_{m;a,c}&:\quad \operatorname{Var}(X_a(p))<\operatorname{Var}(X_c(p)),\\
p_{m;a,c}<p<1&:\quad \operatorname{Var}(X_a(p))>\operatorname{Var}(X_c(p)).
\end{aligned}
\]
Nevertheless, the more central source has a strictly larger **expected** outbreak for *all* \(0<p<1\):
\[
\mathbb E[X_c(p)]>\mathbb E[X_a(p)].
\]
Reflection-equivalent vertices, with equal nearer-endpoint distance, have identical distributions.

For the six-vertex path and endpoint-versus-middle positions \(a=0\) and \(c=2\), the unique crossing is the root in \((0,1)\) of
\[
Q(p)=p^8+3p^7+6p^6+10p^5+14p^4+7p^3-p^2-3p-1.
\]
More precisely, \(0.53789108<p_{5;0,2}<0.53789109\). At \(p=1/2\), peripheral minus central variance is \(-145/1024\); at \(p=9/10\), it is \(18663573519/10^{10}\).

## Assumptions and scope
The model is independent, homogeneous, **undirected bond percolation** on a finite simple path, used as an idealized final-size epidemic model. There is one deterministic seed; transmission events on distinct path edges are independent. The claimed all-position theorem concerns the variance of final cluster size, not instantaneous infection prevalence, epidemic duration, or the outcome of a general continuous-time SIR model with dependent edge transmissions. The endpoints \(p=0\) and \(p=1\) have zero variance for every seed, and are excluded from strict inequalities.

A position is indexed by the number of edges to the nearer end, not by source degree; most compared positions have the same degree two. The statement is *pairwise* for every \(m,a,c\); it does not claim that all pairs share one common threshold.

## Proof
**1. Reduction to independent truncated geometric runs.** The open component of the source extends until the first closed edge on either side. Write \(G_t\) for the number of consecutive open edges among at most \(t\) successive independent edges. Then
\[
X_a=1+G_a+G_{m-a},
\qquad \mathbb P(G_t\ge j)=p^j\quad(1\le j\le t),
\]
and the two runs use disjoint edge sets and are independent. Therefore, putting \(V_t(p)=\operatorname{Var}(G_t)\),
\[
\operatorname{Var}(X_a)=V_a+V_{m-a},\qquad
\mathbb E[X_a]=1+\sum_{j=1}^a p^j+\sum_{j=1}^{m-a}p^j.
\]

**2. Exact polynomial and endpoint behavior.** The integer tail-sum identities give
\[
\mathbb E[G_t]=\sum_{j=1}^t p^j,\qquad
\mathbb E[G_t^2]=\sum_{j=1}^t(2j-1)p^j.
\]
Expanding the square of the first sum and collecting powers yields the finite polynomial
\[
\boxed{V_t(p)=\sum_{j=1}^t j p^j-\sum_{j=t+1}^{2t}(2t+1-j)p^j},
\quad V_0=0.
\]
As \(p\uparrow1\), writing \(q=1-p\), the first failed edge occurs after \(j\) successful edges with probability \(q p^j\) for \(0\le j<t\). Hence
\[
V_t(p)=q\sum_{r=1}^{t}r^2+O_t(q^2).
\]
In particular, \(V_t(0)=V_t(1)=0\).

**3. Three consecutive coefficient-sign regions.** Fix \(0\le a<c\le\lfloor m/2\rfloor\) and write \(d=m-c\), \(b=m-a\), so \(a<c\le d<b\). Let
\[
D(p)=V_a(p)+V_b(p)-V_c(p)-V_d(p)=\sum_{k=0}^{2b}d_k p^k.
\]
For any \(t\ge0\), the coefficient of \(p^k\) in \(V_t\), for \(k\ge1\), is
\[
C_t(k)=\begin{cases}
k,&k\le t,\\
-(2t+1-k),&t<k\le2t,\\
0,&k>2t.
\end{cases}
\]
Thus \(d_k=C_a(k)+C_b(k)-C_c(k)-C_d(k)\). These coefficients have the following *proved* signs:

- For \(k\le a\), all four coefficients coincide and \(d_k=0\). For \(a<k\le c\), the three coefficients \(C_b,C_c,C_d\) equal \(k\), whereas \(C_a\le0\), giving \(d_k<0\).
- For \(c<k\le d\), cancellation of \(C_b=C_d=k\) gives \(d_k=C_a-C_c\ge0\), because for \(t<k\) the expression \(C_t(k)=-\max(0,2t+1-k)\) is nonincreasing with \(t\). For \(d<k\le b\), we additionally have \(C_b=k\) and \(C_d\le0\), making \(d_k>0\).
- For \(k>b\), every index is smaller than \(k\). Write \(H_t=\max(0,2t+1-k)\); then
\[
d_k=(H_c-H_a)-(H_b-H_d).
\]
If \(k\le2d+1\), \(H_b-H_d=2(b-d)=2(c-a)\), while \(0\le H_c-H_a\le2(c-a)\). If \(k>2d+1\), then \(H_c=H_a=0\) and \(H_b-H_d\ge0\). In both cases \(d_k\le0\). The last coefficient is \(d_{2b}=-1\).

**4. Descartes' rule gives one crossover, for every pair.** As each variance vanishes at \(p=1\), \(D(1)=0\) and the polynomial \(U(p)=D(p)/(1-p)\) exists. If \(u_k\) are its coefficients, the polynomial division identity gives \(u_k=\sum_{j=0}^k d_j\). These sums are strictly negative for \(a<k\le c\); are nondecreasing over \(c<k\le b\); and are strictly positive for \(b\le k<2b\), because
\[
u_k=-\sum_{j=k+1}^{2b}d_j>0
\]
throughout the last region (all its summands are nonpositive and \(d_{2b}=-1\)). Thus the nonzero coefficient sequence of \(U\) has **exactly one sign change, from negative to positive**. Descartes' rule implies at most one positive real zero, counted with multiplicity.

On the other hand, \(D(p)<0\) for sufficiently small positive \(p\), since its first nonzero coefficient is \(d_{a+1}=-(2a+1)\). As \(p\uparrow1\), step 2 gives
\[
D(p)=q\bigl[S(a)+S(b)-S(c)-S(d)\bigr]+O_m(q^2),\quad S(t)=\sum_{j=1}^t j^2.
\]
The bracket is strictly positive: \(a<c\le d<b\) and \(a+b=c+d\), while \(S\) is strictly discretely convex because \(S(t)-S(t-1)=t^2\) increases with \(t\). Hence \(D>0\) near \(1\). By continuity there is a root in \((0,1)\); the coefficient-sign bound makes it unique and simple, and establishes the asserted sign directions.

**5. Mean-risk comparison.** Since \(c-a=b-d>0\),
\[
\mathbb E[X_c]-\mathbb E[X_a]
=\sum_{j=a+1}^{c}p^j-\sum_{j=d+1}^{b}p^j>0,
\]
because the two sums have equal numbers of terms and every exponent in the first is smaller than its paired exponent in the second, for \(0<p<1\).

This completes the proof.

## Verification
Run `python3 verify_path_variance.py` (Python standard library only). The standalone checker independently constructs exact first and second moment polynomials by enumerating every possible set of open edges on paths with 3 through 12 vertices. It compares 75 seeded moment polynomials with the analytical formula, representing 45,052 individual source-edge configurations. It additionally checks the quotient-coefficient single-sign-change certificate on 2,870 distinct source-position comparisons through 41 vertices and verifies the two rational six-vertex contrasts. These are finite consistency checks; the universal theorem for unbounded path length follows from the coefficient argument above, not from enumeration.

For the six-vertex numerical root bracket, substituting the exact rational values \(p=53789108/10^8\) and \(p=53789109/10^8\) into \(Q\) yields respectively negative and positive signs; uniqueness is analytical.

## Relationship to prior work
The basic identification of epidemic outbreak clusters with bond percolation and exact cluster-size generating functions is classical; see Moore and Newman (2000). The path-run model is a finite, seeded specialization of that framework. Lančić and colleagues (2009) analyze the epidemic-range and final-size distributions in a tree model; Šikić and colleagues (2011) demonstrate parameter-dependent *mean-impact* ranking in other network topologies; Sharkey and colleagues (2013) provide exact Markovian SIR tree equations. Those results establish broader modeling methods or different rankings, but their inspected statements and derivations do not supply the present **all-pairs, exactly-one-crossing theorem for final-size variance on finite paths**.

A neighboring calculation on a uniformly random seed on paths addresses covariance between infection indicators, not variance ranking conditional on a prescribed seed. A related high-versus-low-degree variance reversal for complete bipartite epidemic networks concerns a different graph family, lacks the path all-pairs comparison, and does not logically imply the theorem here. The result is a specific structural comparison within a standard model, not a claim of priority over every unindexed historical source.

## Limitations
No claim is made about the relative order of **distributions** in convex order, about a universal common threshold across different vertex pairs, or about arbitrary trees or networks with cycles. The variance crossing is compatible with strict mean-outbreak dominance by central sources; it is not a reversal in expected outbreak size. Independent undirected edge retention is essential to the two-run decomposition. In continuous-time Markovian SIR, multiple transmissions from one infectious individual can be correlated, so the theorem does not transfer to that model without additional assumptions. Historical literature beyond the inspected works might contain an equivalent result; independent priority and scientific validation remain outstanding.

## References
1. C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, arXiv:cond-mat/0001393 (first public: 2000-01-26), Physical Review E 62 (2000), 7059–7064. https://arxiv.org/abs/cond-mat/0001393
2. A. Lančić, N. Antulov-Fantulin, M. Šikić, and H. Štefančić, *Phase diagram of epidemic spreading—unimodal vs. bimodal probability distributions*, arXiv:0912.0630 (2009-12-03), Physica A 390 (2011), 65–76. https://arxiv.org/abs/0912.0630
3. M. Šikić, A. Lančić, N. Antulov-Fantulin, and H. Štefančić, *Epidemic centrality—is there an underestimated epidemic impact of network peripheral nodes?*, arXiv:1110.2558 (2011-10-12). https://arxiv.org/abs/1110.2558
4. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, and P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs*, Bulletin of Mathematical Biology 77 (2015), 614–645, first online 2013-12-18. https://doi.org/10.1007/s11538-013-9923-5
