# A universal isolation–motif covariance phase boundary in fixed-edge random graphs

## Finding

Let \(H\) be any fixed connected simple graph with \(k\ge3\) vertices and \(h\) edges. In \(G(n,m)\), the uniform labeled graph with exactly \(m\) edges, let \(I\) count isolated vertices and \(T_H\) count unordered \(k\)-vertex sets inducing a graph isomorphic to \(H\). Put
\[
N=\binom n2,\quad L=\binom{n-1}2,\quad K=\binom k2,\quad q=K-h.
\]
For all integers \(n\ge k+1\) and \(h\le m\le\min\{L,N-q\}\), both expectations are positive and
\[
\frac{\operatorname{Cov}(I,T_H)}{\mathbb E I\,\mathbb E T_H}=B_{n,k,h}(m)-1,
\qquad
B_{n,k,h}(m)=\frac{n-k}{n}\frac{(N)_{\underline K}}{(L)_{\underline K}}
\frac{(L-m)_{\underline q}}{(N-m)_{\underline q}},
\]
where \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\), with value zero if nonnegative integer \(a<b\). In particular, the normalized covariance depends on \(H\) only through its numbers of vertices and edges, never its isomorphism type.

If \(q=0\) (complete motifs), the covariance is strictly positive throughout the stated feasible range. If \(q\ge1\), the factor \(B_{n,k,h}(m)\) is strictly decreasing while positive and is zero thereafter; hence the covariance signs form a nonincreasing sequence in the order positive, possibly one zero, negative. For every \(n\ge 2k-2\), that sequence has both positive and negative terms, hence **exactly one positive-to-negative transition**. For smaller admissible \(n\), positive terms need not occur.

For fixed \(H\), if \(n\to\infty\), \(m/\binom n2\to p\in(0,1)\), then
\[
\lim_{n\to\infty}n\frac{\operatorname{Cov}(I,T_H)}{\mathbb E I\,\mathbb E T_H}
=\frac{2h-k-k(k-2)p}{1-p}.
\]
Thus every connected noncomplete motif has the universal critical density
\[
p_*(H)=\frac{2h-k}{k(k-2)}\in(0,1).
\]
When \(H\) is any tree on \(k\) vertices, \(p_*(H)=1/k\), independently of tree shape. For fixed \(p\ne p_*(H)\), covariance is eventually positive below the threshold and negative above it.

The fixed-edge conclusion contrasts with \(G(n,p)\): in that independent-edge model, for every connected \(H\) and every \(0<p<1\),
\[
\operatorname{Cov}(I,T_H)=-k(1-p)^{n-1}\mathbb E T_H<0.
\]

## Assumptions and scope

Graphs are finite, simple and labeled on \([n]\). The motif \(H\) is fixed, connected, has \(k\ge3\) vertices and \(k-1\le h\le K\). Each induced copy is counted once per unordered vertex set, even if \(H\) has automorphisms. Let \(c_H=k!/|\operatorname{Aut}(H)|\) be the number of labeled graphs on a specified \(k\)-set isomorphic to \(H\). The covariances are strictly signed only where both expectations are positive. For \(m<h\) or \(m>N-q\), the motif count is zero; for \(m>L\), the isolation count is zero. On those degenerate ranges their covariance vanishes. The stated monotonicity is for the *normalized* covariance factor, not for covariance magnitude.

## Proof

**Exact identity.** By counting admissible edge sets on each chosen \(k\)-set,
\[
\mathbb E T_H=\binom nk c_H\frac{\binom{N-K}{m-h}}{\binom Nm},\qquad
\mathbb E I=n\frac{\binom Lm}{\binom Nm}.
\]
Fix a vertex \(v\) and condition on it being isolated. The remaining \(m\) edges are uniform among the \(L\) edges on the other \(n-1\) vertices. Since \(H\) is connected and \(k\ge3\), an induced copy of \(H\) cannot include \(v\). Therefore
\[
\mathbb E[T_H\mid v\text{ isolated}]
=\binom{n-1}k c_H\frac{\binom{L-K}{m-h}}{\binom Lm}.
\]
Summing over \(v\) and dividing by \(\mathbb E I\,\mathbb E T_H\) gives
\[
\frac{\mathbb E[IT_H]}{\mathbb E I\,\mathbb E T_H}
=\frac{n-k}{n}\,
\frac{(N)_{\underline K}}{(L)_{\underline K}}\,
\frac{(L-m)_{\underline q}}{(N-m)_{\underline q}}=B_{n,k,h}(m),
\]
with zero numerator if \(m>L-q\). Subtracting one proves the covariance identity and shape universality.

**Sign monotonicity and finite existence.** For \(q\ge1\), on \(h\le m\le L-q\), the last ratio is
\[
\prod_{j=0}^{q-1}\left(1-\frac{n-1}{N-m-j}\right),
\]
whose factors lie strictly between zero and one and strictly decrease as integer \(m\) increases. At \(m=L-q+1\), the ratio becomes zero and stays zero through \(m=L\). This terminal \(m\) is admissible because \(L\ge K\), \(q\ge1\), and \(L+1\le N\). Thus negative covariance is attained. At \(m=h\), an induced \(H\) uses all available edges, so every other vertex is isolated and
\[
B_{n,k,h}(h)=\frac{n-k}{n}\frac{(N)_{\underline h}}{(L)_{\underline h}}.
\]
To prove this exceeds one for \(n\ge2k-2\), note that in a graph with \(h\ge k-1\) uniformly sampled edges, the expected number of nonisolated vertices increases with \(h\). At \(h=k-1\), apply the first two terms of inclusion–exclusion to the events that a fixed vertex is incident to each sampled edge. Single- and double-incidence probabilities are \(2/n\) and \(4/[n(n+1)]\). Hence the expected number of nonisolated vertices is at least
\[
2(k-1)-\frac{2(k-1)(k-2)}{n+1}>k
\qquad(n\ge2k-2).
\]
Thus the expected number of isolated vertices is below \(n-k\), making \(B_{n,k,h}(h)>1\). The decrease and terminal negative region prove exactly one sign transition for the stated orders. If \(q=0\), the factor is constant in \(m\). It exceeds one because
\[
\frac{(N)_{\underline K}}{(L)_{\underline K}}
=\prod_{j=0}^{K-1}\left(1+\frac{n-1}{L-j}\right)
>1+\frac{2K}{n-2},
\]
and \((n-k)(1+2K/(n-2))\ge n\) for \(n\ge k+1\), \(k\ge3\). The strict inequality gives positivity.

**Asymptotic phase boundary.** For fixed \(k,h\), as \(n\to\infty\), \(m/N\to p\in(0,1)\), finite-product expansion yields
\[
\frac{n-k}{n}=1-\frac kn,
\quad\frac{(N)_{\underline K}}{(L)_{\underline K}}=1+\frac{2K}{n}+o(n^{-1}),
\quad\frac{(L-m)_{\underline q}}{(N-m)_{\underline q}}=1-\frac{2q}{(1-p)n}+o(n^{-1}).
\]
Multiplication gives the claimed limit because \(2K-k=k(k-2)\). For connected \(H\), \(2h-k\ge k-2>0\); for noncomplete \(H\), \(h<K\), so its critical density is strictly between zero and one. Substituting \(h=k-1\) gives the universal tree threshold \(1/k\).

**Independent-edge contrast.** In \(G(n,p)\), conditioning on a fixed induced copy of connected \(H\) forces its \(k\) participating vertices to be nonisolated, but does not affect isolation probability \((1-p)^{n-1}\) of any outside vertex, as that event depends on edges disjoint from those internal to the copy. Hence \(\mathbb E[I\mid\text{marked induced copy}]=(n-k)(1-p)^{n-1}\), which gives the stated strictly negative covariance.

## Verification

The accompanying standalone Python 3 checker `check.py` independently enumerates every labeled edge subset for seven connected motifs (three- and four-vertex paths, triangle, claw, four-cycle, diamond, four-clique) for all available sizes \(k+1\le n\le6\). It calculates isolation and induced-motif counts directly and compares exact rational covariances with the formula for every edge count. It also checks exact monotonicity on a parameter grid \(3\le k\le12\), \(k+1\le n\le k+24\), \(k-1\le h<K\). In total, **5,483 exact assertions** passed. This finite test does not prove the infinite theorem; the conditional sampling argument, factor monotonicity, Bonferroni inequality, and finite-product asymptotics do.

To reproduce, run `python3 check.py` from the directory containing the extracted artifact. No third-party packages are required.

## Relationship to prior work

Random graphs with a fixed edge count and correlations of directed reachability events were studied by Alm, Janson and Linusson (2009). Reinert and Röllin (2009) calculate covariances for edges, two-stars and triangles in the independent-edge model. Sah and Sawhney (2022) establish local limit theorems for induced-subgraph counts in fixed-edge graphs using graph factors, including density-dependent exceptional sets. These inspected results do not state an exact covariance with the *number of isolated vertices*, a finite-order one-switch classification for every connected induced motif, or the critical density above. A related covariance law for **tree components** concerns copies with all exterior incident edges absent; it does not algebraically give the induced-tree count, which permits exterior incident edges. The result does not claim independent historical priority.

## Limitations

The covariance sign is classified only on the stated nondegenerate edge-count support. At the asymptotic critical density the first-order limit vanishes; finite-order signs are governed by the exact factor, and no second-order critical-window law is claimed. At fixed positive edge density the expected number of isolated vertices decays exponentially in \(n\); the threshold is an exact dependence phenomenon, not a claim of a macroscopic covariance. Exhaustive small-graph tests and literature searches cannot establish historical uniqueness. No independent audit has been performed.

## References

1. S. E. Alm, S. Janson, S. Linusson, *Correlations for paths in random orientations of G(n,p) and G(n,m)*, arXiv:0906.0720 (first posted 3 June 2009), https://arxiv.org/abs/0906.0720.
2. G. Reinert, A. Röllin, *U-statistics and random subgraph counts: Multivariate normal approximation via exchangeable pairs and embedding*, arXiv:0912.3425 (17 December 2009), https://arxiv.org/abs/0912.3425.
3. A. Sah, M. Sawhney, *Local limit theorems for subgraph counts*, Journal of the London Mathematical Society 105 (2022), 950–1011, https://doi.org/10.1112/jlms.12523.
4. R. B. Ellis, J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics 158 (2010), 649–658, https://doi.org/10.1016/j.dam.2009.11.012.
