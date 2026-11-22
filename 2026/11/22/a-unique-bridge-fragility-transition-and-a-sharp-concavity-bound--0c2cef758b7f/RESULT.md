# A unique bridge-fragility transition and a sharp concavity boundary on theta networks

## Finding

Let \(G=\Theta(a,b,c)\) consist of three internally vertex-disjoint paths of lengths \(a,b,c\ge2\) joining the same two terminals, and let \(m=a+b+c\). Retain each edge independently with probability \(0<p<1\). Let \(M\) count retained edges and let \(B\) count the retained edges that are bridges in the retained spanning subgraph. Write \(d_{12}=a+b\), \(d_{13}=a+c\), and \(d_{23}=b+c\).

**Exact joint law.** With \(d_{ij}\) ranging over these three pairwise path sums and \(\ell_{ij}=m-d_{ij}\), the full bivariate probability generating polynomial is
\[
\begin{aligned}
\mathbb E[s^M t^B]={}&(1-p+pst)^m\\
&+\sum_{ij\in\{12,13,23\}}(ps)^{d_{ij}}(1-t^{d_{ij}})
 \left[(1-p+pst)^{\ell_{ij}}-(pst)^{\ell_{ij}}\right]\\
&+(ps)^m(1-t^m).
\end{aligned}
\]
In particular,
\[
\operatorname{Cov}(M,B)=p(1-p)
\left[m-(a+b)^2p^{a+b-1}-(a+c)^2p^{a+c-1}-(b+c)^2p^{b+c-1}+m^2p^{m-1}\right].
\]
This covariance has **exactly one zero** \(p_*\in(0,1)\); it is positive for \(0<p<p_*\) and negative for \(p_*<p<1\), for all integer lengths \(a,b,c\ge2\).

**Sharp conditional concavity boundary.** Conditional on \(M=k\), every \(k\)-edge subset is equally likely, and
\[
f(k):=\mathbb E[B\mid M=k]
=k-\sum_{ij\in\{12,13,23\}}d_{ij}\frac{\binom{k}{d_{ij}}}{\binom m{d_{ij}}}
+m\mathbf1_{\{k=m\}},\qquad 0\le k\le m,
\]
where \(\binom{k}{d}=0\) for \(k<d\). All second forward differences \(f(k+2)-2f(k+1)+f(k)\) with \(0\le k<m-2\) are nonpositive, but the final one equals
\[
\boxed{f(m)-2f(m-1)+f(m-2)=
\frac{6abc-a^2(a-1)-b^2(b-1)-c^2(c-1)}{m(m-1)}.}
\]
Thus the complete fixed-edge regression is discretely concave **if and only if** \(6abc\le a^2(a-1)+b^2(b-1)+c^2(c-1)\); otherwise a *single terminal upward curvature reversal* occurs. For three equal paths \(a=b=c=L\ge2\) it always occurs, while \(\Theta(2,2,5)\) exhibits it and \(\Theta(2,2,6)\) does not.

For the equilateral case \(a=b=c=L\), the unique covariance transition satisfies
\[
1=L p_*^{2L-1}(4-3p_*^L),\qquad
1-p_*=\frac{\log(4L)}{2L}+O\!\left(L^{-3/2}+L^{-2}(\log L)^2\right)
\quad(L\to\infty).
\]

## Assumptions and scope

The host is a finite undirected *simple* theta graph. Each path has at least two edges; its internal vertices do not belong to either other path. Each edge is independently present with a common Bernoulli parameter \(p\). A bridge means a present edge whose deletion increases the number of connected components of the entire retained spanning graph; bridges in disconnected components are included. The fixed-edge conditional law is uniform on all subsets of exactly \(k\) of the host's \(m\) edges. No independence or connectedness is imposed after thinning. No claim is made about general noncactus graphs or unequal probabilities.

## Proof

**1. Path-completeness identity.** Label the three paths \(P_1,P_2,P_3\). Let \(I_{ij}\) indicate that *every* edge on both \(P_i\) and \(P_j\) is open, and let \(I_{123}\) indicate that all host edges are open. The only cycles of a theta graph are the unions of two entire terminal-to-terminal paths. A present edge is nonbridging exactly when it lies on at least one of these surviving cycles. If fewer than two paths are completely open, all present edges are bridges. If exactly paths \(i,j\) are complete, precisely their \(d_{ij}\) edges are nonbridging. If all three are complete, every edge is nonbridging, whereas the sum over the three pairwise cycle lengths counts each edge twice. Consequently, *for every edge configuration*,
\[
B=M-\sum_{ij\in\{12,13,23\}}d_{ij} I_{ij}+m I_{123}. \tag{1}
\]

**2. Entire bivariate law.** The initial generating polynomial \((1-p+pst)^m\) treats all open edges as bridges. On configurations with exactly two fully open paths \(i,j\), replace the factor \(t^{d_{ij}}\) by \(1\). Those configurations have weight \((ps)^{d_{ij}}[(1-p+pst)^{\ell_{ij}}-(pst)^{\ell_{ij}}]\), since the third path is incomplete. These three cases are disjoint. The all-open configuration separately requires replacement of \(t^m\) by \(1\). This yields the claimed generating polynomial without overcounting.

**3. Covariance and unique sign transition.** Taking expectations in (1) gives
\[
\mathbb EB=mp-\sum_{ij}d_{ij}p^{d_{ij}}+mp^m. \tag{2}
\]
For any statistic \(H\) on the edge configurations, differentiating its finite Bernoulli mixture shows
\[
\frac d{dp}\mathbb E_p H=\frac{\operatorname{Cov}_p(M,H)}{p(1-p)}.
\]
Applying this to (2) proves the covariance formula. Set
\[
Q(p)=m-\sum_{ij}d_{ij}^2p^{d_{ij}-1}+m^2p^{m-1}.
\]
Since \(a,b,c\ge2\), every exponent \(d_{ij}-1\) lies strictly between zero and \(m-1\). After merging coincident powers, \(Q\) has positive constant and leading coefficients and only negative coefficients between them. Thus its nonzero coefficient sequence has exactly two sign changes. Descartes' rule of signs gives at most two positive zeros counted with multiplicity. But \(Q(0)=m>0\), \(Q(1)=m-a^2-b^2-c^2<0\), and \(Q(p)\to+\infty\) as \(p\to\infty\). Hence there is one positive zero in \((0,1)\) and another in \((1,\infty)\); by the multiplicity bound, both are simple and there are no others. Since \(p(1-p)>0\), the covariance changes from positive to negative exactly once in the physical interval.

**4. Conditional curvature.** Given \(M=k\), the chance that the \(d_{ij}\) designated edges of a pair of paths are all selected equals \(\binom{k}{d_{ij}}/\binom m{d_{ij}}\). The all-open event has probability \(\mathbf1_{\{k=m\}}\). Taking conditional expectations in (1) gives the formula for \(f(k)\). Pascal's identity twice gives, for \(0\le k\le m-2\),
\[
\Delta^2 f(k)=-\sum_{ij}\frac{d_{ij}\binom{k}{d_{ij}-2}}{\binom m{d_{ij}}}+m\mathbf1_{\{k=m-2\}}. \tag{3}
\]
For \(k<m-2\), (3) is nonpositive. At \(k=m-2\), use
\(\binom{m-2}{d-2}/\binom md=d(d-1)/[m(m-1)]\) and \(d_{ij}=m-a_k\). Multiplication by \(m(m-1)\) reduces the numerator to
\[
m^2(m-1)-\sum_{i=1}^3(m-a_i)^2(m-a_i-1)
=6abc-\sum_{i=1}^3a_i^2(a_i-1),
\]
proving the sharp criterion. For \(a=b=c=L\), the numerator equals \(3L^2(L+1)>0\). For \((a,b,c)=(2,2,h)\), it is \(-h^3+h^2+24h-8\), positive at \(h=5\) and negative at \(h=6\).

**5. Equal-arm asymptotic.** With \(a=b=c=L\), the interior root equation reduces to \(1=Lp^{2L-1}(4-3p^L)\). Its solution \(p_L\) tends to one: for any fixed \(\varepsilon>0\), the bracketed expression tends to zero uniformly when \(p\le1-\varepsilon\). Because \(1\le4-3p_L^L\le4\), the root equation implies \(p_L^{2L-1}\asymp L^{-1}\); thus \(1-p_L=O(\log L/L)\) and \(p_L^L=O(L^{-1/2})\). Taking logarithms gives
\[
-(2L-1)\log p_L=\log L+\log(4-3p_L^L)
=\log(4L)+O(L^{-1/2}).
\]
Dividing by \(2L-1\) and using \(1-e^{-u}=u+O(u^2)\) yields the asserted error term.

## Verification

The standalone `verify_theta.py` exhaustively enumerates all \(2^m\) edge configurations for ten graphs including equal and asymmetric arm lengths, identifies each bridge independently by removing it and testing endpoint connectivity, and checks the exact two-variable generating-polynomial coefficients, conditional means for every edge budget, and covariances at three distinct rational retention probabilities per graph. It also checks both sides of the final-curvature boundary. Running the supplied script with Python's standard library produced:

`PASS: 163 exact comparisons, 8640 exhaustive edge subsets, 10 theta graphs`

These finite tests cross-check identities, while the argument in Proof gives the all-size statements, the root uniqueness, and asymptotics. The checker is not an independent external audit.

## Relationship to prior work

Elçi, Weigel, and Fytas (2015) develop general edge-bridge identities in the random-cluster model, including bond percolation, and characterize maximum fragility via derivative/bridge-load conditions. Those general identities motivate the covariance question and are not claimed as new. Their inspected full-text treatment does not give this theta-specific exact joint polynomial, its Descartes two-root certificate, or its fixed-edge concavity boundary. Allard and collaborators (2012) give exact iterative calculations for component-size distributions of finite percolated graphs, rather than the bridge count jointly with the open-edge count. A separately published cactus-graph bridge-count result establishes an exactly concave fixed-edge conditional regression on edge-disjoint cycle networks; its hypothesis excludes these overlapping-cycle theta networks. The present terminal upward curvature is a precise boundary of that cactus conclusion.

## Limitations

The graph must have exactly three internally disjoint terminal paths, each of integer length at least two, and equal independent bond probabilities. General multicyclic graphs may exhibit other sign patterns. The numerical checks are finite; no inference of the infinite-length asymptotic is made from enumeration. The previously published general bridge-derivative identities are not new. Historical priority is not independently certified; a broader earlier reliability-polynomial treatment may imply some special cases. One potentially relevant lengthy thesis on network reliability was not fully inspectable and remains a residual historical-comparison risk. Independent mathematical audit has not been performed.

## References

- E. M. Elçi, M. Weigel, and N. G. Fytas, *Bridges in the random-cluster model*, arXiv:1509.00668, first posted 2015-09-02, https://arxiv.org/abs/1509.00668.
- A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau, and L. J. Dubé, *Exact solution of bond percolation on small arbitrary graphs*, arXiv:1201.4369, first posted 2012-01-20, https://arxiv.org/abs/1201.4369.
- X. Xu et al., *Geometric structure of percolation clusters*, arXiv:1309.7244, first posted 2013-09-27, https://arxiv.org/abs/1309.7244.
- *Bridge-count phase transition in Bernoulli percolation on cactus graphs*, published research record (2026-11-08), catalog identifier `165dfc9cb694`.
