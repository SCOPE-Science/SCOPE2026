# Parity-controlled reversal of isolation and odd-degree dependence in binomial random graphs

## Finding

Let \(G\sim G(n,p)\) be the independent-edge simple graph on \(n\ge2\) labeled vertices, with \(0<p<1\). Let \(I\) be the number of isolated vertices and \(O\) the number of vertices of odd degree. Then

\[
\operatorname{Cov}(I,O)=-\frac n2(1-p)^{n-1}\left[1+(1-2p)^{n-2}(2np-1)\right].
\]

For every even \(n\ge2\), the covariance is strictly negative at every \(0<p<1\). For each odd \(n\ge3\), there is exactly one \(p_n\in(1/2,1)\) satisfying

\[
(2p_n-1)^{n-2}(2np_n-1)=1.
\]

The covariance is strictly negative for \(0<p<p_n\), zero at \(p=p_n\), and strictly positive for \(p_n<p<1\). As odd \(n\to\infty\),

\[
1-p_n=\frac{\log(2n)}{2n}+O\!\left(\frac{(\log n)^2}{n^2}\right).
\]

More precisely, for each fixed real \(s\), take \(p=1-[\log(2n)+s]/(2n)\). Along odd \(n\to\infty\),

\[
\frac{2\operatorname{Cov}(I,O)}{n(1-p)^{n-1}}\longrightarrow e^{-s}-1.
\]

## Assumptions and scope

The graph has one independent Bernoulli-\(p\) edge indicator for each unordered pair of distinct vertices, with no loops. All statements about covariance are exact for integer \(n\ge2\) and real \(p\in(0,1)\). The unique-crossing assertion concerns odd \(n\ge3\); for even \(n\) there is no interior crossing. The asymptotic statements concern odd integers tending to infinity, and the critical-window profile has fixed, finite \(s\). The normalized quantity in the last display is a scaled covariance, not a Pearson correlation coefficient.

## Proof

Write \(A_v=\mathbf{1}\{\deg(v)=0\}\), \(B_v=\mathbf{1}\{\deg(v)\text{ odd}\}\), and \(t=1-2p\). The elementary parity identity for a binomial random variable gives

\[
\mathbb E A_v=(1-p)^{n-1}=:a,\qquad
\mathbb E B_v=\frac{1-t^{n-1}}2=:b.
\]

The events \(A_v\) and \(B_v\) are disjoint, whence \(\operatorname{Cov}(A_v,B_v)=-ab\). For distinct \(u,v\), conditioning on \(A_v=1\) forces the edge \(uv\) absent and leaves the other \(n-2\) edges incident to \(u\) independent and Bernoulli-\(p\). Consequently,

\[
\mathbb E[A_vB_u]=\frac a2(1-t^{n-2}),\qquad
\operatorname{Cov}(A_v,B_u)=-ap\,t^{n-2}.
\]

Summing the \(n\) diagonal and \(n(n-1)\) off-diagonal terms yields

\[
\begin{aligned}
\operatorname{Cov}(I,O)
&=-nab-n(n-1)ap\,t^{n-2}\\
&=-\frac{na}{2}\left[1-t^{n-1}+2(n-1)p\,t^{n-2}\right]\\
&=-\frac{na}{2}\left[1+t^{n-2}(2np-1)\right].
\end{aligned}
\]

It remains to classify the sign of the bracket \(F_n(p)=1+(1-2p)^{n-2}(2np-1)\). When \(2np-1\ge0\) and \(1-2p\ge0\), it is at least one. When \(0<p<1/(2n)\), the second term is greater than \(-1\), since \(0<1-2p<1\) and \(-1<2np-1<0\). This proves \(F_n(p)>0\) for \(0<p\le1/2\) (including \(n=2\)). For \(p>1/2\), if \(n\) is even, \((1-2p)^{n-2}\ge0\) and \(2np-1>0\); hence \(F_n(p)>0\). If \(n\) is odd, putting \(q=2p-1\in(0,1)\) gives

\[
F_n(p)=1-q^{n-2}(n-1+nq).
\]

The function \(q\mapsto q^{n-2}(n-1+nq)\) is continuous and strictly increasing on \((0,1)\), from zero to \(2n-1>1\). There is exactly one zero of \(F_n\); since the covariance has sign opposite to \(F_n\), the claimed signs follow.

For the asymptotics, set \(h=2n(1-p)\); then \(q=1-h/n\). At \(h=\log(2n)+s\), for fixed \(s\),

\[
\begin{aligned}
\log\!\left[(1-h/n)^{n-2}(2n-h-1)\right]
&=(n-2)\log(1-h/n)+\log(2n-h-1)\\
&=-s+O\!\left(\frac{(\log n)^2}{n}\right).
\end{aligned}
\]

Therefore the factor inside the logarithm is \(e^{-s}[1+O((\log n)^2/n)]\). For odd \(n\), the bracket \(F_n\) is one minus this factor, giving the normalized critical-window limit. Monotonicity shows the unique root has \(h=\log(2n)+o(1)\). Substituting into the same expansion at the root and solving \(0=-[h-\log(2n)]+O((\log n)^2/n)\) gives \(h=\log(2n)+O((\log n)^2/n)\), which is the asserted threshold expansion.

## Verification

The accompanying standalone `verify.py` checks the exact formula against independent exhaustive enumeration of all labeled simple graphs for \(2\le n\le6\), at five rational edge probabilities for each size. It also numerically tests critical-window convergence and finite-size threshold values. Run `python3 verify.py` with Python 3.9 or later; its expected output records 25 exact graph-law comparisons and 16 numerical window comparisons. These finite checks supplement the analytical proof and are not claimed to establish its universal quantifiers.

## Relationship to prior work

Goldstein's study of fixed-degree vertex counts (first arXiv release 2010-05-24) and Ghosh–Goldstein–Raič's study of isolated-vertex concentration (first arXiv release 2011-05-31) supply the classical random-graph context and related marginal statistics. Their inspected arguments do not evaluate the mixed dependence between isolated vertices and the aggregated count of all odd-degree vertices. Alarfaj–Taylor–Bogachev (2023) examine correlations of the numerical degrees of two vertices; this is not the covariance of the two nonlinear graph counts here. Janzer–Yip (2025) use parity constraints in random graphs at \(p=1/2\), without a general edge-probability sign threshold of the present form. The independent-edge model and binomial degree parity formula are standard; no novelty is claimed for those ingredients themselves.

## Limitations

The sign reversal occurs in an extremely dense regime for odd \(n\), and the unscaled covariance is exponentially small there. Thus the theorem is a structural dependence result, not evidence of a practically large measurable correlation or a new random-graph connectivity threshold. It says nothing about conditioning on the entire degree sequence, arbitrary dependence between edges, or a central limit theorem. Earlier literature may contain an implicit equivalent through broader joint-degree generating functions; the priority assessment is necessarily provisional pending additional independent review.

## References

1. L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390, first released 2010-05-24. https://arxiv.org/abs/1005.4390
2. S. Ghosh, L. Goldstein and M. Raič, *Concentration of measure for the number of isolated vertices in the Erdős–Rényi random graph by size bias couplings*, arXiv:1106.0048, first released 2011-05-31. https://arxiv.org/abs/1106.0048
3. B. Alarfaj, C. Taylor and L. Bogachev, *The joint node degree distribution in the Erdős–Rényi network*, arXiv:2303.05138, first released 2023-03-09. https://arxiv.org/abs/2303.05138
4. O. Janzer and F. Yip, *The Probability That a Random Graph is Even-Decomposable*, *Random Structures & Algorithms* (2025), doi:10.1002/rsa.70034. https://doi.org/10.1002/rsa.70034
