# Universal covariance signs for two-hop paths in randomly oriented graphs

## Finding

In the random orientation of the binomial graph \(G(n,p)\), **the sign of the covariance of two two-hop reachability indicators depends only on how the two directed requests meet**, for every graph order and every positive edge density. The five distinct-request types are classified completely:

| Ordered requests | Vertices needed | Covariance sign |
|---|---:|---|
| \(a\to b\), \(b\to a\) (reverse) | \(n\ge2\) | Strictly negative |
| \(a\to b\), \(b\to c\) (chain) | \(n\ge3\) | Strictly negative |
| \(a\to b\), \(a\to c\) (common source) | \(n\ge3\) | Strictly positive |
| \(a\to b\), \(c\to b\) (common target) | \(n\ge3\) | Strictly positive |
| \(a\to b\), \(c\to d\) (four distinct endpoints) | \(n\ge4\) | Strictly positive |

All letters shown as distinct in each row are required to be distinct. Reversing the two requests or simultaneously reversing all arcs does not change the corresponding covariance. If two requests are identical, their covariance is their strictly positive Bernoulli variance. At \(p=0\) all covariances are zero.

A key consequence is a **reachability-horizon sign reversal**. The exact two-hop chain covariance is negative for every \(n\ge3\), \(0<p\le1\), yet for every fixed \(p>1/2\) the corresponding *unrestricted* directed-path covariance is positive for all sufficiently large \(n\), by the established theorem of Alm, Janson and Linusson. Thus directed paths of length at least three are essential to the latter positive correlation.

## Assumptions and scope

Let \(n\ge2\), \(0<p\le1\), and independently for each unordered pair \(\{u,v\}\subset[n]\), put no edge with probability \(1-p\), orient the edge \(u\to v\) with probability \(p/2\), or orient it \(v\to u\) with probability \(p/2\). Multiple edges and directed loops are excluded. This is the annealed randomly oriented \(G(n,p)\) model, not the model of independent antiparallel arcs.

For distinct vertices \(a,b\), define \(R_{ab}=1\) exactly if an oriented path of **one or two** edges exists from \(a\) to \(b\), and \(F_{ab}=1-R_{ab}\). Write

\[
q=1-\frac{p^2}{4},\qquad r=1-\frac{p^2}{2},\qquad f=1-\frac{p^2}{2}+\frac{p^3}{8},\qquad A=1-\frac p2.
\]

Then \(\Pr(F_{ab}=1)=Aq^{n-2}\), and \(\operatorname{Cov}(R_{ab},R_{cd})=\operatorname{Cov}(F_{ab},F_{cd})\). For two distinct requests define \(J=\Pr(F_{ab}=F_{cd}=1)\); the entire finite law needed for the covariance is:

\[
\begin{aligned}
J_{\rm reverse}&=(1-p)r^{n-2},\\
J_{\rm chain}&=\frac{3p^3-2p^2-8p+8}{8}\,r^{n-3},\\
J_{\rm fork}&=A^2 f^{n-3},\\
J_{\rm disjoint}&=\frac{(2-p)^2(p^4+2p^3-8p^2+8)}{32}\,q^{2n-8}.
\end{aligned}
\]

The common-source and common-target cases both use \(J_{\rm fork}\). For each case \(\operatorname{Cov}=J-A^2q^{2n-4}\). The exponent ranges apply only when that case's minimum vertex count holds; hence there are no negative powers at small valid \(n\).

## Proof

**Marginal.** The direct arc \(a\to b\) is absent with probability \(A\). For every third vertex \(w\), the event \(a\to w\to b\) has probability \(p^2/4\); the edges for distinct \(w\) and the direct arc are disjoint. Thus \(\Pr(F_{ab}=1)=Aq^{n-2}\).

**Separate the endpoints from the external vertices.** Fix the at most four endpoints of two requests. The edge states on those endpoints are independent of those on all external vertices. Contributions from distinct external vertices factor, because their sets of edges to the endpoints are disjoint. For reverse or chain requests a single external vertex cannot supply both two-edge witnesses, so its simultaneous nonwitness probability is \(r\). For common-source/common-target requests, the two witness events overlap in a shared single arc with joint probability \(p^3/8\), so the simultaneous nonwitness probability is \(f\). For disjoint requests, their external edge sets are disjoint, so it is \(q^2\).

**Exact endpoint factors.** An absent edge has weight \(1-p\), and either specified oriented present edge has weight \(p/2\). The reverse case has one endpoint edge and requires its complete absence, contributing \(1-p\). The chain case has a triangle of endpoint edges; counting admissible oriented configurations with respectively \(0,1,2,3\) present edges gives \((1,4,3,1)\), hence the endpoint polynomial

\[
(1-p)^3+4\frac p2(1-p)^2+3\left(\frac p2\right)^2(1-p)+\left(\frac p2\right)^3=\frac{3p^3-2p^2-8p+8}{8}.
\]

For a fork, absence of both direct arcs automatically excludes any internal two-step witness, hence its endpoint factor is \(A^2\). For disjoint requests, counting admissible configurations on the complete graph of four endpoints with \(0,\ldots,6\) present edges gives \((1,10,37,66,62,30,6)\). Their weighted polynomial simplifies to

\[
\sum_{j=0}^{6}c_j\left(\frac p2\right)^j(1-p)^{6-j}
=\frac{(2-p)^2(p^4+2p^3-8p^2+8)}{32}.
\]

These endpoint factors and the external factors yield all four displayed joint formulas.

**Strict signs.** For \(p>0\), \(0<r<q^2\) (except at \(p=0\)) and \(f>q^2\), with

\[
q^2-r=\frac{p^4}{16},\qquad f-q^2=\frac{p^3(2-p)}{16}.
\]

For the reverse case, \(1-p<A^2\), hence \((1-p)r^{n-2}<A^2q^{2n-4}\). For the chain case the endpoint comparison is exactly

\[
A^2q^2-\frac{3p^3-2p^2-8p+8}{8}
=\frac{p^3(p^3-4p^2-4p+8)}{64}>0.
\]

The parenthesized polynomial decreases throughout \([0,1]\) and equals \(1\) at \(p=1\). Combining this inequality with \(r<q^2\) yields strict negative chain covariance. For forks, \(f>q^2\) and \(q<1\) imply \(A^2 f^{n-3}>A^2q^{2n-4}\). Finally, for disjoint requests,

\[
\operatorname{Cov}(R_{ab},R_{cd})
=\frac{p^3(2-p)^2}{1024}q^{2n-8}
\bigl(64-64p+16p^3-p^5\bigr)>0.
\]

Indeed \(64-64p+16p^3-p^5=64(1-p)+p^3(16-p^2)>0\) on \((0,1]\). This exhausts the symmetry types of two distinct directed requests. The unrestricted-path sign contrast invokes Theorem 2.1 of Alm, Janson and Linusson, which covers all directed path lengths.

## Verification

A standard-library-only checker independently enumerates all orientations/absences on \(K_n\) for \(2\le n\le5\) at \(p\in\{0,1/4,1/2,3/4,1\}\), compares rational marginal and joint probabilities against the formulas for every eligible request type, and verifies two critical polynomial identities at one hundred additional positive rational densities. It also checks the triangle and four-vertex endpoint-configuration counts. Execute \(\texttt{python check.py}\). All **488** checks passed in the delivered package. Exhaustive small-order computation is a cross-check and not a substitute for the all-order algebraic proof.

## Relationship to prior work

Alm, Janson and Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)* (first public version 3 June 2009), analyze full, unrestricted directed reachability. Their Theorem 2.1 establishes the large-\(n\) chain sign transition at \(p=1/2\), but does not state the two-hop finite-size formulas or the all-density negative two-hop chain law. Leander and Linusson, *Correlation of paths between distinct vertices in a randomly oriented graph* (2013), address unrestricted reachability with four distinct endpoints, rather than two-hop probabilities. Narayanan, *Connections in randomly oriented graphs* (2016), proves positive association for certain unrestricted reachability events from a common source on a fixed graph. It gives useful context but does not imply the negative two-hop chain result. The common-source sign by itself is not claimed as new.

## Limitations

The exact theorem is for at most two directed edges and for independent, **unbiased** orientations of each present edge in the binomial \(G(n,p)\) model. It does not assert a corresponding sign table for the fixed-edge-count \(G(n,m)\) model, heterogeneous orientation biases, or three-hop reachability. The connection with full-path reachability relies on an earlier theorem and is not a new proof of that result. Literature comparison supports a best-knowledge novelty assessment, not an exhaustive priority certification. Independent external validation has not been performed.

## References

1. S. E. Alm, S. Janson and S. Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)*. arXiv:0906.0720 (first submitted 2009-06-03), Random Structures & Algorithms 39 (2011), 486–506. https://arxiv.org/html/0906.0720v2
2. M. Leander and S. Linusson, *Correlation of paths between distinct vertices in a randomly oriented graph*. arXiv:1303.3961 (first submitted 2013-03-16), Mathematics Scandinavica 116 (2015), 287–300. https://arxiv.org/pdf/1303.3961
3. B. Narayanan, *Connections in randomly oriented graphs*. arXiv:1609.01003 (first submitted 2016-09-05), Combinatorics, Probability and Computing 27 (2018), 667–671. https://arxiv.org/abs/1609.01003
