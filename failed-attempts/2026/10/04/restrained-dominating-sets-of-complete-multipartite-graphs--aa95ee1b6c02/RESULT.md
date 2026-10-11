# Restrained dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), parts \(X_1,\ldots,X_r\), and \(N=\sum_i n_i\). For a proper vertex set \(S\subsetneq V(G)\), let \(s(S)\) be the number of parts met by \(S\), and \(c(S)\) the number of parts met by \(V(G)\setminus S\). Then \(S\) is restrained dominating if and only if \(c(S)\ge2\) and either \(s(S)\ge2\) or \(S=X_i\) for some part \(X_i\). The whole vertex set is always restrained dominating. Consequently, with \(R_G(z)=\sum_{S\text{ restrained dominating}}z^{|S|}\), if \(r=2\) then \[R_G(z)=z^N+\prod_{i=1}^2\big((1+z)^{n_i}-1-z^{n_i}\big),\] whereas for \(r\ge3\), \[R_G(z)=(1+z)^N-\sum_i(1+z)^{n_i}+(r-1)-\sum_i z^{N-n_i}\big((1+z)^{n_i}-z^{n_i}\big)+\sum_i z^{n_i}.\] In particular, if \(r=2\) then \(\gamma_r(G)=2\) when both parts have size at least two and \(\gamma_r(G)=N\) otherwise; if \(r\ge3\), then \(\gamma_r(G)=1\) exactly when a singleton part exists, and \(\gamma_r(G)=2\) otherwise. The number of minimum restrained dominating sets is respectively \(n_1n_2\), \(1\), the number of singleton parts, or \(|E(G)|+|\{i:n_i=2\}|\) in those four cases.

## Assumptions and scope
All graphs are finite and simple. A restrained dominating set \(S\) is a dominating set such that every vertex outside \(S\) has a neighbor outside \(S\). The graph \(G=K_{n_1,\ldots,n_r}\) is connected, so \(r\ge2\) and every \(n_i\ge1\). The polynomial \(R_G(z)\) is defined here only as the ordinary size enumerator of restrained dominating sets.

## Proof
Let \(S\subsetneq V(G)\). A vertex outside \(S\) has a neighbor outside \(S\) exactly when the complement \(V(G)\setminus S\) meets another part. Therefore the restraint condition is equivalent to
\[
c(S)\ge2.
\]

For domination, if \(S\) meets at least two parts, then every vertex outside \(S\) is adjacent to a selected vertex in a different part, so \(S\) dominates. If \(S\) meets exactly one part \(X_i\), vertices of \(X_i\setminus S\) have no neighbor in \(S\); hence domination holds exactly when \(S=X_i\). The empty set is not dominating. This proves the all-set criterion.

For \(r=2\), a proper restrained dominating set must meet both parts and its complement must also meet both parts. Thus each part contributes a nonempty proper subset independently, which gives
\[
R_G(z)=z^N+\prod_{i=1}^2\big((1+z)^{n_i}-1-z^{n_i}\big).
\]

Assume \(r\ge3\). Start from all \((1+z)^N\) subsets. The subsets meeting at most one part have enumerator
\[
A(z)=\sum_i(1+z)^{n_i}-(r-1).
\]
The subsets whose complement meets at most one part have enumerator
\[
B(z)=z^N+\sum_i z^{N-n_i}\big((1+z)^{n_i}-z^{n_i}\big).
\]
For \(r\ge3\), these two bad families are disjoint: a set cannot meet at most one part while its complement also meets at most one part. Hence the sets satisfying both support conditions contribute \((1+z)^N-A(z)-B(z)\). The whole vertex set, removed by \(B(z)\), must be restored, and the exceptional proper dominating sets with one-part support are precisely the full parts \(X_i\); each is restrained because its complement meets the other \(r-1\ge2\) parts. Restoring these terms yields the displayed formula.

The minimum cases now follow from the classification. For \(r=2\), a proper set exists exactly when both parts have a nonempty proper choice; then the smallest choice uses one vertex from each part and there are \(n_1n_2\) such sets. Otherwise only \(V(G)\) works. For \(r\ge3\), a singleton part itself is a size-one restrained dominating set, and every size-one restrained dominating set must be such a part. If there is no singleton part, size one is impossible, while every cross-part pair is restrained dominating; additionally, a whole part of size two is restrained dominating. Thus the minimum-set count is \(|E(G)|+|\{i:n_i=2\}|\).

## Verification
The included checker constructs each complete multipartite graph from its part labels and tests the restrained-domination definition directly for every vertex subset. It independently compares the accepted subsets with the structural criterion, the entire coefficient vector with the two polynomial formulas, and the minimum value and minimum-set count with the stated case distinction. All complete multipartite isomorphism types of orders two through ten are checked.

## Relationship to prior work
Brešar and Henning study restrained domination as an active domination parameter and prove the sharp cubic-graph bound \(\gamma_r(G)\le2|V(G)|/5\). Their full article develops structural arguments for cubic and special subcubic graphs; targeted full-text searches found no complete multipartite or complete bipartite treatment and no restrained-dominating-set enumerator. The earlier restrained-domination survey literature records exact values for complete graphs, paths, cycles, and several bondage variants, but the inspected survey section does not state the complete-multipartite all-set classification or polynomial above.

Targeted database searches for restrained domination together with complete multipartite graphs returned results for other domination variants on complete multipartite graphs, not this parameter. Exact web searches likewise did not locate the displayed formulas.

## Limitations
The formulas are specific to connected complete multipartite graphs. The finite exhaustive verification is corroborative only and does not replace the proof. The notation \(R_G(z)\) is introduced locally as a size enumerator and is not claimed to be a standardized polynomial name. Literature search cannot exclude differently phrased or non-indexed prior work.

## References
1. B. Brešar, M. A. Henning, “Best possible upper bounds on the restrained domination number of cubic graphs,” arXiv:2403.17129v1, submitted 25 March 2024; Journal of Graph Theory 106 (2024), 763–815, DOI 10.1002/jgt.23095.
2. J.-M. Xu, “On Bondage Numbers of Graphs: A Survey with Some Comments,” International Journal of Combinatorics 2013, Article 595210, DOI 10.1155/2013/595210.
