# Phylogenetic rank of complete multipartite graphs

## Statement

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph, with all \(n_i\ge 1\). Write
\[
q=\#\{i:n_i\ge2\},\qquad s=\#\{i:n_i=1\}.
\]
For the Pachter--Sturmfels phylogenetic rank \(r(G)\), i.e. the minimum number of metric-tree factors whose supremum product contains an isometric copy of the graph metric, one has
\[
\boxed{r(G)=q+\mathbf 1_{\{s\ge2\}}.}
\]

Equivalently, every non-singleton part requires a distinct tree coordinate, while all singleton parts collectively require one extra coordinate if and only if there are at least two of them.

## Proof

Every component of a tree embedding is 1-Lipschitz: if
\(
\iota=(\iota_1,\ldots,\iota_k):G\to T_1\times\cdots\times T_k
\)
is isometric for the supremum metric, then
\[
d_{T_j}(\iota_j(x),\iota_j(y))\le d_G(x,y)
\]
for every coordinate \(j\).

### Upper bound

For every non-singleton part \(P_i\), take a star \(T_i\) with one leaf for each vertex of \(P_i\), every incident edge having length \(1\). Map vertices of \(P_i\) to their corresponding leaves and map every vertex outside \(P_i\) to the center. The induced coordinate distance is then
\[
d_i(x,y)=
\begin{cases}
2,&x\ne y\text{ and }x,y\in P_i,\\
1,&\text{exactly one of }x,y\text{ lies in }P_i,\\
0,&\text{otherwise}.
\end{cases}
\]
If \(s\ge2\), add one more star \(T_0\), whose leaves correspond to the singleton-part vertices and whose incident edges have length \(1/2\). Map all other vertices to its center. Thus \(T_0\) gives distance \(1\) between two singleton-part vertices and distance \(1/2\) between a singleton-part vertex and any other vertex.

The supremum of these coordinate distances is exactly the graph distance. Two vertices in the same non-singleton part have distance \(2\), realized by that part's coordinate. Vertices in different non-singleton parts have distance \(1\), realized by either corresponding part coordinate. A singleton vertex and a vertex in a non-singleton part have distance \(1\), realized by the latter part coordinate. Finally, two singleton-part vertices have distance \(1\), realized by \(T_0\). Hence
\[
r(G)\le q+\mathbf 1_{\{s\ge2\}}.
\]

### Lower bound

For each non-singleton part \(P_i\), choose two distinct vertices \(x_i,y_i\in P_i\). Since \(d_G(x_i,y_i)=2\), some coordinate of any isometric tree product must realize distance \(2\) on this pair. Call one such coordinate \(c(i)\).

If two different non-singleton parts \(P_i,P_j\) used the same coordinate, then in that tree coordinate the quartet \(x_i,y_i,x_j,y_j\) would have
\[
d(x_i,y_i)+d(x_j,y_j)=4,
\]
whereas each of the other two pair sums is at most \(2\), because all cross-part graph distances are \(1\) and the coordinate is 1-Lipschitz. This gives a unique largest four-point sum, impossible for a tree metric. Therefore the coordinates \(c(i)\) are pairwise distinct, so at least \(q\) coordinates are necessary.

Now suppose \(s\ge2\), and choose two singleton-part vertices \(u,v\). Their graph distance is \(1\), so some coordinate \(c_0\) realizes distance \(1\) between them. If \(c_0=c(i)\) for some non-singleton part, then the quartet \(x_i,y_i,u,v\) would have one pair sum equal to
\[
2+1=3,
\]
while each other pair sum is at most \(2\), again violating the four-point condition. Hence \(c_0\) is distinct from all \(c(i)\), and at least \(q+1\) coordinates are necessary. This proves the formula.

The same argument remains valid when some vertices have the same image in a coordinate tree: the pullback tree pseudometric still satisfies the four-point condition.

## Consequences

The formula simultaneously recovers several families that were treated separately in Ashworth--Clarke--Giansiracusa--Jones--Quijas-Aceves--Ren (2026):

- \(K_n\) has rank \(1\);
- \(K_{a,b}\) with \(a,b\ge2\) has rank \(2\);
- \(K_{2,\ldots,2}=K_{2q}\) minus a perfect matching has rank \(q\);
- \(K_4\setminus e=K_{2,1,1}\) has rank \(2\).

It also yields the complete rank spectrum inside this graph class. For every \(n\ge2\), the phylogenetic ranks attained by connected complete multipartite graphs on \(n\) vertices are exactly
\[
\boxed{\{1,2,\ldots,\lfloor n/2\rfloor\}.}
\]
Indeed, the formula gives \(r(G)\le\lfloor n/2\rfloor\). Conversely, rank \(1\) is realized by \(K_n\); and for each \(2\le k\le\lfloor n/2\rfloor\), take \(k\) non-singleton parts, begin with sizes \(2,\ldots,2\), and add the remaining \(n-2k\) vertices to one part.

Within complete multipartite graphs, rank one occurs exactly for complete graphs and stars: if every part is a singleton, the graph is complete; otherwise the formula gives rank one only for one non-singleton part together with exactly one singleton part, which is a star.

## Relation to prior literature

Ashworth, Clarke, Giansiracusa, Jones, Quijas-Aceves and Ren, *The phylogenetic rank of a graph*, arXiv:2609.19372v1 (2026), define the graph parameter used here. Their Proposition 3.5 proves rank \(2\) for every complete bipartite graph with both parts nontrivial; Theorem 3.3 includes \(K_n\) minus a perfect matching among the rank-\(n/2\) families; Example 3.6 gives \(K_4\setminus e\) rank \(2\); and Theorem 3.7 classifies rank-one graphs. The current accessible full text contains no occurrence of “multipartite” and does not state the formula above for arbitrary complete multipartite graphs.

Cartwright and Chan, *Three notions of tropical rank for symmetric matrices*, arXiv:0912.1411 / Combinatorica 32 (2012), study a different tropical tree-rank notion. Their paper explicitly notes that their definition differs from the tree-rank notion in Pachter--Sturmfels, Chapter 3, and their Proposition 13 characterizes their own tree rank of 0/1 dissimilarity matrices by covers with complete multipartite graphs. This superficially similar result therefore does not supply the supremum-product metric formula proved here.

The original Pachter--Sturmfels source, *Algebraic Statistics for Computational Biology* (Cambridge University Press, 2005), Section 3.5, is foundational for the rank notion and is the most important residual originality risk. The book's bibliographic record and table of contents were checked, and the 2026 source's statements about Section 3.5 were inspected, but the full text of Section 3.5 was not inspected here. It could contain a special metric decomposition equivalent to some or all of this theorem. Accordingly, originality is claimed only to the best of our knowledge.

## Verification

`artifacts/verify_phylogenetic_rank_complete_multipartite.py` directly constructs the displayed coordinate pseudometrics for every connected complete-multipartite isomorphism type of orders \(2\) through \(10\), checks every pair against the graph metric, checks the four-point condition for every coordinate, and checks the quartet certificates used in the lower bound. It covers 128 multipartite types. The computation is supporting evidence; the proof above is general and does not depend on finite enumeration.

## References

1. F. Ashworth, O. Clarke, J. Giansiracusa, J. Jones, J. Quijas-Aceves, Y. Ren, *The phylogenetic rank of a graph*, arXiv:2609.19372v1, 2026. https://arxiv.org/abs/2609.19372
2. D. Cartwright, M. Chan, *Three notions of tropical rank for symmetric matrices*, Combinatorica 32 (2012), 55--84; arXiv:0912.1411. https://arxiv.org/abs/0912.1411
3. L. Pachter, B. Sturmfels (eds.), *Algebraic Statistics for Computational Biology*, Cambridge University Press, 2005, Section 3.5, ISBN 9780521857000. https://doi.org/10.1017/CBO9780511610684
