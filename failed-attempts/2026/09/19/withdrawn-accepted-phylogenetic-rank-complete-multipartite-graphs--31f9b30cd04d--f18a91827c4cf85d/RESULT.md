# Phylogenetic rank of complete multipartite graphs

## Result

Let
\[
G=K_{n_1,\dots,n_r}
\]
be a nontrivial connected complete multipartite graph, with \(r\ge 2\). Define
\[
q=\#\{i:n_i\ge 2\},\qquad s=\#\{i:n_i=1\}.
\]
Write \(r_{\mathrm{phy}}(G)\) for the phylogenetic rank: the least number of metric-tree factors whose supremum product contains the graph metric of \(G\) isometrically.

Then
\[
\boxed{
r_{\mathrm{phy}}(K_{n_1,\dots,n_r})
=
\max\!\left\{1,\ q+\mathbf 1_{\{s\ge2\}}\right\}.
}
\]

Equivalently:

- if every part is a singleton, so \(G\) is complete, then \(r_{\mathrm{phy}}(G)=1\);
- if at least one part is non-singleton and there are at most one singleton parts, then \(r_{\mathrm{phy}}(G)=q\);
- if at least one part is non-singleton and at least two parts are singletons, then \(r_{\mathrm{phy}}(G)=q+1\).

Thus, within complete multipartite graphs,
\[
r_{\mathrm{phy}}(G)\le k
\]
has the exact structural criterion
\[
\max\!\left\{1,\ q+\mathbf 1_{\{s\ge2\}}\right\}\le k.
\]

## Context

Ashworth, Clarke, Giansiracusa, Jones, Quijas-Aceves and Ren introduced a systematic graph-theoretic study of the Pachter--Sturmfels phylogenetic rank in 2026. They compute several infinite families, including
\[
r_{\mathrm{phy}}(K_{m,n})=2\qquad(m,n\ge2),
\]
and show that \(K_N\) minus a perfect matching has rank \(N/2\). They also ask for structural characterizations of graphs of rank at most \(k\) for \(k\ge2\).

The theorem above gives an exact answer on the whole complete-multipartite class. It contains both cited families as special cases:
\[
K_{m,n}:\ q=2,\ s=0,
\]
and
\[
K_{2,2,\dots,2}=K_N-\text{(perfect matching)}:\ q=N/2,\ s=0.
\]
It also identifies a phenomenon not visible in either special case: two or more singleton parts require exactly one additional tree coordinate, regardless of how many singleton parts there are.

## Proof

The graph metric of a connected complete multipartite graph has the simple form
\[
d_G(u,v)=
\begin{cases}
2,&u\ne v\text{ lie in the same part},\\
1,&u,v\text{ lie in different parts}.
\end{cases}
\]

### Upper bound

For each non-singleton part \(P_i\), construct a metric star \(T_i\) having one leaf for every vertex of \(P_i\), with all leaf edges of length \(1\). Map vertices of \(P_i\) to their corresponding leaves and map every vertex outside \(P_i\) to the center. The induced coordinate pseudometric \(d_i\) satisfies
\[
d_i(u,v)=
\begin{cases}
2,&u,v\in P_i,\ u\ne v,\\
1,&|\{u,v\}\cap P_i|=1,\\
0,&u,v\notin P_i.
\end{cases}
\]

If \(s\le1\), the supremum of these \(q\) coordinate metrics is exactly \(d_G\). Indeed, a same-part pair in a non-singleton part is realized with distance \(2\) in its own coordinate, and every pair from two different parts has distance \(1\) in at least one non-singleton-part coordinate.

If \(s\ge2\), add one more metric star \(T_0\), with one leaf for each singleton vertex and all leaf edges of length \(1/2\). Map every singleton vertex to its leaf and every non-singleton vertex to the center. This coordinate gives singleton--singleton distance \(1\), singleton--non-singleton distance \(1/2\), and non-singleton--non-singleton distance \(0\). Taking the supremum with the \(q\) previous coordinates therefore recovers \(d_G\) exactly.

If \(q=0\), then \(G=K_r\), and one star with \(r\) leaves of edge length \(1/2\) realizes its metric. Hence
\[
r_{\mathrm{phy}}(G)\le
\max\{1,q+\mathbf 1_{\{s\ge2\}}\}.
\]

### Lower bound

In every tree embedding
\[
\iota:G\longrightarrow T_1\times\cdots\times T_k
\]
with the supremum metric, each coordinate map is \(1\)-Lipschitz:
\[
d_{T_j}(\iota_j(u),\iota_j(v))\le d_G(u,v).
\]

For every non-singleton part \(P_i\), choose distinct vertices \(a_i,b_i\in P_i\). Since
\[
d_G(a_i,b_i)=2,
\]
some coordinate must realize their full distance \(2\).

No one tree coordinate can realize the distance-\(2\) pairs belonging to two distinct non-singleton parts. Suppose a coordinate realized both
\[
d(a_i,b_i)=2,\qquad d(a_j,b_j)=2
\]
for \(i\ne j\). All four cross distances are at most \(1\), because those pairs are adjacent in \(G\). The three four-point sums in that tree coordinate would therefore include
\[
d(a_i,b_i)+d(a_j,b_j)=4,
\]
while each of the other two sums is at most \(2\). This gives a unique largest four-point sum, contradicting the four-point condition for tree metrics. Consequently the \(q\) non-singleton parts require \(q\) distinct coordinates.

Now suppose \(s\ge2\), and choose singleton vertices \(x,y\). Since \(d_G(x,y)=1\), some coordinate realizes
\[
d(x,y)=1.
\]
Such a coordinate cannot also realize \(d(a_i,b_i)=2\) for any non-singleton part \(P_i\). Otherwise the four-point sum
\[
d(a_i,b_i)+d(x,y)=3
\]
would be strictly larger than each of the other two sums, which are at most \(2\), again violating the four-point condition. Therefore the singleton pair requires a coordinate distinct from the \(q\) coordinates forced above.

Hence
\[
k\ge q+\mathbf 1_{\{s\ge2\}}
\]
whenever \(q\ge1\). If \(q=0\), the nontrivial complete graph has rank at least \(1\). This matches the construction and proves the formula.

## Consequences and examples

The formula yields, for example,
\[
r_{\mathrm{phy}}(K_{2,2,2})=3,\qquad
r_{\mathrm{phy}}(K_{3,4,1})=2,
\]
\[
r_{\mathrm{phy}}(K_{5,1,1})=2,\qquad
r_{\mathrm{phy}}(K_{2,2,1,1})=3.
\]
In particular, arbitrarily many universal singleton vertices impose only one extra coordinate once there are at least two of them.

For rank two, the complete-multipartite graphs are exactly those satisfying
\[
q+\mathbf 1_{\{s\ge2\}}\le2
\]
apart from complete graphs, which have rank one. This supplies a closed structural slice of the general rank-\(\le k\) characterization problem.

## Verification

A standalone exact-integer verifier enumerates every connected complete multipartite isomorphism type of orders \(2\) through \(12\), a total of \(259\) integer partitions with at least two parts. For each type it:

1. constructs the stated star-coordinate metrics;
2. checks pairwise that their supremum is exactly the graph metric;
3. checks the four-point condition for every constructed coordinate pseudometric; and
4. checks the numerical four-point incompatibility certificates used in the lower bound.

The verifier reports all checks passing. This finite computation supports the proof but is not used in place of the general argument.

## Originality and limitations

To the best of our knowledge, the exact complete-multipartite formula above is not in the existing literature. The 2026 source paper explicitly gives complete bipartite graphs and complements of perfect matchings as separate known families, but does not state a complete-multipartite theorem; its accessible full text contains no occurrence of “multipartite”. Searches using “phylogenetic rank”, “tree rank”, “complete multipartite”, “product of metric trees”, “supremum metric”, and equivalent metric-embedding formulations did not locate the formula.

The four-point condition itself is classical, and the rank notion predates the 2026 graph paper; neither is claimed new. The complete-bipartite case, the complete-graph case, and the complement-of-perfect-matching case are prior results and are credited as such.

The main residual originality risk is Pachter and Sturmfels, *Algebraic Statistics for Computational Biology* (2005), Section 3.5, which is the original tree-rank source and was not fully inspectable in the available web preview. Metadata and secondary descriptions were checked, and the 2026 graph paper cites that section while still presenting complete bipartite graphs and complements of perfect matchings as separate graph-family results. No evidence of the complete-multipartite formula was found, but full-text absence cannot be certified. Very recent or not-yet-indexed parallel work is an additional residual risk.

## References

1. F. Ashworth, O. Clarke, J. Giansiracusa, J. Jones, J. Quijas-Aceves, Y. Ren, *The phylogenetic rank of a graph*, arXiv:2609.19372 (2026). https://arxiv.org/abs/2609.19372
2. P. Buneman, *A note on the metric properties of trees*, Journal of Combinatorial Theory, Series B 17 (1974), 48--50. https://doi.org/10.1016/0095-8956(74)90047-1
3. L. Pachter, B. Sturmfels (eds.), *Algebraic Statistics for Computational Biology*, Cambridge University Press (2005), Section 3.5. https://doi.org/10.1017/CBO9780511610684
