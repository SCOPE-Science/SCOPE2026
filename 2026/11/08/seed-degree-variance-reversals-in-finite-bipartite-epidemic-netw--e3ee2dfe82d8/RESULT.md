# Seed-degree variance reversals in finite bipartite epidemic networks

## Finding
For an integer \(b\ge3\), consider independent bond percolation on the complete bipartite graph \(K_{2,b}\), each edge retained with probability \(0<p<1\). Let \(X_H\) be the number of vertices in the retained-edge component containing a specified degree-\(b\) vertex (a high-degree seed); let \(X_L\) similarly refer to a specified degree-two vertex (a low-degree seed). Then \(\operatorname{Var}(X_H)-\operatorname{Var}(X_L)\) is **positive for all sufficiently small positive \(p\)** and **negative for all \(p\) sufficiently close to one**. Hence every member of this infinite graph family has at least one genuine seed-dependent outbreak-variance reversal.

Among complete bipartite graphs with both parts of size at least two, the first unequal-degree member, \(K_{2,3}\) (five vertices), has exactly **one** variance crossover in \((0,1)\). It occurs at \(p_*=0.251554055831668\ldots\), the unique solution in \((0,1)\) of
\[
F(p)=20p^9-56p^8+7p^7+56p^6+8p^5-10p^4-42p^3+3p^2-2p+1=0.
\]
Here
\[
\operatorname{Var}(X_H)-\operatorname{Var}(X_L)=p(1-p)^2F(p),
\]
so the difference is positive on \((0,p_*)\) and negative on \((p_*,1)\). Nevertheless the high-degree seed has strictly higher **expected** outbreak size at every positive transmission probability:
\[
\mathbb E X_H-\mathbb E X_L=p(1-p)^2\bigl(1+p+3p^2-2p^3\bigr)>0.
\]
The boundary case \(b=2\) is the four-cycle \(K_{2,2}\): the seed types are interchangeable and both variances are identical for all \(p\).

## Assumptions and scope
The graph is finite, undirected, simple and complete bipartite, with part sizes exactly \(2\) and \(b\). Edge status is independent Bernoulli with common parameter \(p\). An outbreak infects exactly the connected component of its one fixed initial infected vertex; this is the usual independent-edge final-size model, not an assertion for arbitrary temporally correlated SIR dynamics. The result compares the two vertex orbits *within the same graph*, with all other model features identical. No uniqueness claim is made for \(b>3\).

## Proof
Put \(q=1-p\), \(c=1-q^2\), and introduce the probability generating functions \(H_b(z)=\mathbb E[z^{X_H}]\) and \(L_b(z)=\mathbb E[z^{X_L}]\). Directly separating whether the two high-degree vertices are connected through any of the \(b\) low-degree vertices gives the exact identity
\[
H_b(z)=zq^b(1+pz)^b+z^2\bigl[(q^2+cz)^b-(q^2+2pqz)^b\bigr]. \tag{1}
\]
For the first term, no low-degree vertex has both incident edges retained: a vertex joined only to the chosen high-degree seed contributes \(z\), whereas a vertex joined only to the other high-degree seed is not reached. The second term counts configurations in which at least one low-degree vertex joins both high-degree vertices, making both reachable, with each low-degree vertex then reached precisely when at least one of its incident edges is retained. These two cases partition the entire sample space.

For a low-degree seed, its two incident edges are both absent with probability \(q^2\), exactly one retained with total probability \(2pq\), or both retained with probability \(p^2\). In the middle case, the remaining edges form \(K_{2,b-1}\) rooted at a high-degree vertex. In the final case, both high-degree vertices and the seed are connected, and each remaining low-degree vertex joins independently with probability \(c\). Thus
\[
L_b(z)=q^2z+2pq\,zH_{b-1}(z)+p^2z^3(q^2+cz)^{b-1}. \tag{2}
\]
These are exact PGFs for every integer \(b\ge2\), including normalization at \(z=1\).

For any such PGF \(G\), its mean is \(G'(1)\) and its variance is \(G''(1)+G'(1)-G'(1)^2\). Substituting \(b=3\) into (1)-(2), differentiating and cancelling gives the two displayed polynomial identities in the Finding section. For strict mean dominance, note that \(1+p+3p^2-2p^3=1+p+p^2+2p^2(1-p)>0\) when \(0<p<1\).

For uniqueness of the variance transition, set \(t=p/(1-p)\), a bijection from \((0,1)\) to \((0,\infty)\). Algebra gives
\[
(1+t)^9F\bigl(t/(1+t)\bigr)=1+7t+23t^2+7t^3-185t^4-581t^5-775t^6-464t^7-130t^8-15t^9. \tag{3}
\]
The coefficient sequence ordered by increasing degree has exactly one sign change. Descartes' rule therefore gives at most one strictly positive real root counted with multiplicity. The polynomial in (3) is positive at \(t=0\) and negative as \(t\to\infty\), so continuity gives at least one positive root. Thus it has exactly one, proving the phase classification and its strict signs. The root belongs to \(0.25155<p_*<0.25156\) by exact rational substitution into \(F\); the longer decimal above is numerical, not an independent certification of all its digits.

For every integer \(b\ge3\), the weak-transmission and strong-transmission endpoint expansions have a direct combinatorial proof. As \(p\downarrow0\), the event of one retained incident edge has probability \(\deg(v)p+O(p^2)\), whereas two or more retained edges occur with probability \(O(p^2)\). Therefore \(\operatorname{Var}(X_H)=bp+O(p^2)\) and \(\operatorname{Var}(X_L)=2p+O(p^2)\), giving
\[
\operatorname{Var}(X_H)-\operatorname{Var}(X_L)=(b-2)p+O(p^2)>0
\]
for sufficiently small positive \(p\).

As \(q\downarrow0\), the only ways of disconnecting a vertex from the otherwise connected graph with exactly two failed edges are to delete both edges incident to one degree-two vertex: the two high-degree vertices have degree \(b\ge3\), and no other two-edge cut exists. With the high-degree seed, each of the \(b\) such events removes precisely one low-degree vertex from its outbreak, giving variance \(bq^2+O(q^3)\). With a low-degree seed, isolation of the seed itself (one of the two-edge cut events) changes its outbreak size from \(b+2\) to \(1\), a deviation of \(b+1\), while isolation of any of the other \(b-1\) degree-two vertices changes its outbreak size by one. Hence the latter variance is \([(b+1)^2+(b-1)]q^2+O(q^3)=(b^2+3b)q^2+O(q^3)\). Consequently
\[
\operatorname{Var}(X_H)-\operatorname{Var}(X_L)=-b(b+2)q^2+O(q^3)<0
\]
for sufficiently small positive \(q\). The independent edge model makes both variances polynomials in \(p\), hence continuous; the intermediate value theorem supplies a reversal for every \(b\ge3\). For \(b=2\), both vertex classes are a single automorphism orbit, proving equality identically.

## Verification
The attached `verify.py` reconstructs (1)-(2), enumerates all edge states for both seed types on \(K_{2,b}\) with \(b=2,3,4\) (respectively \(16,64,256\) states per type), checks the full bivariate PGFs, obtains the exact \(K_{2,3}\) moment differences and transformed sign polynomial, checks an exact rational root bracket, and independently verifies the variance endpoint coefficients at \(b=3,4,5\). It uses Python 3 and SymPy; it passed in the supplied form. The all-integer endpoint claims above have a mathematical proof independent of finite tests.

For example, at \(p=1/2\) on \(K_{2,3}\), the high-degree seed has mean \(109/32\) and variance \(2007/1024\), whereas the low-degree seed has mean \(101/32\) and variance \(2535/1024\). Thus its higher expected outbreak size coexists with lower variance by exactly \(33/64\).

## Relationship to prior work
Moore and Newman (2000) model bond percolation as epidemic final size and compute mean/variance for small-world networks with a uniformly random source, not an orbitwise comparison on \(K_{2,b}\). Allard and colleagues (2012) supply general finite-graph exact recurrences from which any prescribed finite-graph PGF can in principle be computed. Their general method is a direct computational predecessor of (1)-(2), but their inspected primary text does not provide the infinite biclique endpoint reversal, the minimal asymmetric biclique case, or the analytic unique crossover for \(K_{2,3}\). Accordingly the finding is a structural comparison derived from and compatible with established percolation principles, not a claim to invent PGF techniques.

## Limitations
There is no asserted single crossover for every \(b\ge4\), no assertion about general multipartite graphs, and no empirical disease forecast. Exact small-graph distributions can be computed using pre-existing general algorithms, so prior unindexed worked examples or specialized reliability results are a residual priority risk. An independent scientific audit has not been conducted.

## References
- C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, first public preprint January 26, 2000, https://arxiv.org/abs/cond-mat/0001393 .
- A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau and L. J. Dubé, *Exact solution of bond percolation on small arbitrary graphs*, first public preprint January 20, 2012, https://arxiv.org/abs/1201.4369 .
