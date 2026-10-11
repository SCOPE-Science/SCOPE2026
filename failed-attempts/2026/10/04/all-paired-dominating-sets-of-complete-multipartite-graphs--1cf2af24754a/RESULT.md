# All paired-dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\) and \(N=\sum_i n_i\). For \(S\subseteq V(G)\), write \(s_i=|S\cap X_i|\) and \(|S|=2t\). Then \(S\) is paired dominating if and only if \(t\ge1\) and \(\max_i s_i\le t\). Consequently, the number \(p_{2t}(G)\) of paired-dominating sets of size \(2t\) is \[p_{2t}(G)=\binom{N}{2t}-\sum_{i=1}^r\sum_{j=t+1}^{\min(n_i,2t)}\binom{n_i}{j}\binom{N-n_i}{2t-j}.\] All odd coefficients vanish. Moreover, the inclusion-minimal paired-dominating sets are exactly the two-vertex sets meeting two different parts. Hence \(\gamma_{\rm pr}(G)=\Gamma_{\rm pr}(G)=2\), and the number of minimal paired-dominating sets is \(|E(G)|=\sum_{i<j}n_i n_j\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\) and every \(n_i\ge1\). A paired-dominating set is a dominating set \(S\) such that \(G[S]\) contains a perfect matching. A paired-dominating set is inclusion-minimal when none of its proper subsets is paired dominating.

## Proof
Put \(s_i=|S\cap X_i|\) and \(m=|S|\). If \(S\) is paired dominating, then \(m\) is even; write \(m=2t\). In any perfect matching of the complete multipartite graph \(G[S]\), a selected vertex in part \(X_i\) must be matched to a selected vertex outside \(X_i\). Therefore \(s_i\le t\) for every \(i\).

Conversely, suppose \(m=2t\ge2\) and \(\max_i s_i\le t\). These inequalities force \(S\) to meet at least two parts, so \(S\) dominates all of \(G\). It remains to show that \(G[S]\) has a perfect matching. More generally, a complete multipartite graph of even order \(2t\) has a perfect matching whenever its largest part has size at most \(t\). This follows by induction on \(t\): choose one vertex from each of two largest nonempty parts and match them. After deleting this pair, the new largest part has size at most \(t-1\), so induction applies. Hence the stated condition is also sufficient.

For fixed size \(2t\), a subset fails the matching condition exactly when one part contains more than \(t\) selected vertices. Two different parts cannot both contain more than \(t\) vertices of a \(2t\)-set, so these bad events are disjoint. For part \(i\), choosing exactly \(j>t\) selected vertices there and the remaining \(2t-j\) outside contributes
\[
inom{n_i}{j}inom{N-n_i}{2t-j}.
\]
Subtracting all such disjoint bad families from the \(inom N{2t}\) total subsets gives the formula.

Finally, any two vertices from distinct parts form a paired-dominating set: they are adjacent, their edge is a perfect matching, and together they dominate every vertex. Every paired-dominating set with more than two vertices contains such a cross-part pair, so it cannot be inclusion-minimal. Thus the minimal paired-dominating sets are exactly the edges, yielding both paired-domination parameters equal to two and exactly \(|E(G)|\) minimal sets.

## Verification
The included checker independently constructs each complete multipartite graph from part labels. For every vertex subset it tests domination directly and searches recursively for a perfect matching without using the multipartite matching criterion. It then compares the full size distribution with the coefficient formula and tests minimality by scanning proper subsets. Every complete multipartite isomorphism type of orders two through nine is checked.

## Relationship to prior work
Jiang, Wu, Zhang, and Rao study upper paired domination, where one maximizes the cardinality of an inclusion-minimal paired-dominating set, and establish hardness results even on restricted bipartite graphs. Their accessible publisher material defines the same minimality notion and does not state a complete-multipartite classification. Exact literature searches for paired domination together with complete multipartite graphs did not locate the all-set criterion or coefficient formula above.

The result explains why the upper paired-domination problem collapses on this dense family: every paired-dominating set contains a dominating matching edge. At the same time, the size enumerator retains the nontrivial Hall-type obstruction that no selected part may hold more than half of the selected vertices.

## Limitations
The counting formula is specific to complete multipartite graphs. The verification is finite corroboration and does not replace the all-orders proof. Search coverage cannot exclude differently phrased or non-indexed prior enumerations.

## References
1. H. Jiang, P. Wu, J. Zhang, Y. Rao, “Upper paired domination in graphs,” AIMS Mathematics 7(1) (2022), 1185–1197, DOI 10.3934/math.2022069; published online 21 October 2021.
