# Two-colour strong-majority edge colourings of connected cubic graphs and efficient domination

## Finding
For every finite connected simple cubic graph \(G\), denote by \(p(G)\) the number of its *efficient dominating sets*: sets \(D\subseteq V(G)\) such that every closed neighbourhood \(N_G[v]\) contains exactly one member of \(D\). Let \(N_2(G)\) count edge-colourings with the two *named* colours red and blue satisfying the strong-majority condition: for every edge, neither colour occurs on more than half of its adjacent edges (the edge itself is excluded).

Then there is an explicit bijection
\[
\{\text{such red/blue edge-colourings}\}\longleftrightarrow
\{(D,\epsilon):D\text{ efficient dominating},\ \epsilon\in\{\text{red},\text{blue}\}\},
\]
where the colouring corresponding to \((D,\epsilon)\) gives colour \(\epsilon\) to every edge with at least one endpoint in \(D\), and the opposite colour to every other edge. In particular,
\[
N_2(G)=2p(G),\qquad
\operatorname{Maj}'(G)=2\ \Longleftrightarrow\ p(G)>0.
\]
The strong-majority index \(\operatorname{Maj}'(G)\) is the least number of colours in a strong-majority edge-colouring. An immediate order obstruction is \(4\mid |V(G)|\). For bipartite cubic graphs the stronger obstruction \(8\mid |V(G)|\) holds. Neither divisibility condition is asserted to be sufficient.

## Assumptions and scope
All graphs are finite, simple, connected, and \(3\)-regular. The strong-majority condition concerns the \(4\) edges adjacent to each edge of a cubic graph; therefore each named colour must occur *exactly twice* among those \(4\) edges in a valid red/blue colouring. The two colour names are fixed and counted distinctly. A perfect code in the graph-theoretic closed-neighbourhood sense is synonymous here with an efficient dominating set. No statement is made about disconnected graphs, irregular graphs, or the least index when it exceeds two.

## Proof
Encode red by \(+1\) and blue by \(-1\), writing \(x_{uv}\) for the sign of edge \(uv\). Define the signed degree
\[
s(v)=\sum_{e\ni v}x_e\in\{-3,-1,1,3\}.
\]
At any edge \(uv\), the sum of signs on its four *other* incident edges is \(s(u)+s(v)-2x_{uv}\). The two-colour strong-majority requirement is equivalent to having two signs of each kind among these four neighbours, hence exactly
\[
s(u)+s(v)=2x_{uv}.\tag{1}
\]
If \(uv\) is red, equation (1) permits only signed-degree pairs \((3,-1),(-1,3),(1,1)\). If \(uv\) is blue, the permitted pairs are \((-3,1),(1,-3),(-1,-1)\). Consequently no edge joins the two vertex classes
\[
A=\{v:s(v)\in\{3,-1\}\},\qquad B=\{v:s(v)\in\{-3,1\}\}.
\]
Because \(G\) is connected, precisely one of \(A,B\) is all of \(V(G)\).

Suppose first that \(A=V(G)\). Put \(D=\{v:s(v)=3\}\). Every \(v\in D\) is incident with three red edges and each such edge joins \(v\) to a vertex of signed degree \(-1\). Thus \(D\) is independent. Every vertex \(w\notin D\) has signed degree \(-1\), hence exactly one red incident edge. The permitted degree pairs show that this red edge meets \(D\), while its other two incident edges, joining vertices of signed degree \(-1\), are blue. Therefore every vertex outside \(D\) has exactly one neighbour in \(D\). Together with independence of \(D\), this says \(|N_G[v]\cap D|=1\) for every \(v\): \(D\) is efficient dominating. We recover the colouring uniquely from \(D\): edges touching \(D\) are red and all others blue.

If instead \(B=V(G)\), exchange the colour names. The same argument yields the efficient dominating set \(D=\{v:s(v)=-3\}\), with blue on all edges touching \(D\) and red on all remaining edges. Thus *every* successful colouring determines exactly one pair \((D,\epsilon)\).

Conversely, let \(D\) be efficient dominating. It is independent, and each vertex outside it has exactly one neighbour in \(D\). Choose either of the two named colours \(\epsilon\) on the edges touching \(D\), and the other on the remaining edges. A vertex in \(D\) sees three edges of colour \(\epsilon\); a vertex outside \(D\) sees one edge of \(\epsilon\) and two of the opposite colour. The signed degrees are \(3\) and \(-1\) after possibly interchanging signs. An edge touching \(D\) joins these vertex types and satisfies equation (1); any other edge joins two outside vertices and also satisfies (1). Hence every edge has precisely two adjacent edges of each colour, so the constructed colouring is strong-majority. The reconstruction above proves injectivity as well as surjectivity of the correspondence.

A monochromatic one-colour edge-colouring is impossible, since every edge has four neighbours. Therefore the least strong-majority edge index is two precisely when a two-colour colouring exists, which by the bijection is precisely when an efficient dominating set exists. Since the disjoint four-vertex closed neighbourhoods of vertices in \(D\) partition \(V(G)\), the graph order is divisible by four.

Finally, suppose \(G\) is bipartite with classes \(U,W\), of equal size \(m\) by cubic regularity. Writing \(a=|D\cap U|\), \(b=|D\cap W|\), the closed-neighbourhood partition counts the vertices in each class as
\[
a+3b=m,\qquad 3a+b=m.
\]
It follows that \(a=b\) and \(m=4a\), so \(|V(G)|=2m\) is divisible by eight. This proves all claims.

## Verification
The independent finite checker in `verify.py` enumerates every vertex subset that is an efficient dominating set and independently enumerates every assignment of two named colours to all edges, testing the majority condition from the four adjacent edges. It compares the *complete sets of colouring tuples*, not merely their counts, to the predicted bijection. It ran successfully for 19 connected cubic test graphs, including \(K_4\), \(K_{3,3}\), \(Q_3\), the Petersen graph, circular ladders, and labelled regular graphs sampled on 8 and 10 vertices. For \(K_4\) and \(Q_3\), each has exactly four efficient dominating sets and eight named two-colourings; the Petersen graph and \(K_{3,3}\) have none. All comparisons passed with the final marker `VERIFY_OK 19 graph instances`. The unrestricted result is proven symbolically above, not by finite enumeration. Run `python verify.py` with Python 3 and the `networkx` package to reproduce `verify_output.txt`.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority edge colourings in 2026 and established a range of general and class-specific upper bounds [1]. Antoniuk, Prorok and Salia proved broader sufficient upper-colour bounds [2], while Pękała and Przybyło established a three-colour upper bound for minimum degree at least five [3]. None of the inspected relevant theorems identifies the exact two-colour cubic graph class or a counting bijection with efficient domination. Efficient domination and perfect codes in graphs are established independently of this colouring notion [4]. A published exact result for *complete graphs* singles out \(K_4\); this is consistent with, but does not imply, the unrestricted connected-cubic characterization: \(K_4\) is its only complete-graph instance of degree three. The present equivalence connects the low-colour edge-colouring question directly to the graph-theoretic perfect-code existence and counting problems.

## Limitations
The graph must be connected and cubic. The result decides only whether two colours suffice and counts all named two-colourings; it does not determine whether three or more colours are sufficient when no efficient dominating set exists. Divisibility by four (or by eight for bipartite graphs) is necessary, not sufficient. Although the inspected literature does not contain an equivalent theorem, unindexed literature or alternative formulations could potentially establish it independently. No independent external audit was performed.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, “Strong majority colorings of graphs”, arXiv:2605.23828v1, first posted 2026-05-22.
2. S. Antoniuk, M. Prorok, N. Salia, “Strong Majority Edge-Coloring”, arXiv:2607.00212v1, first posted 2026-06-30.
3. P. Pękała, J. Przybyło, “On Strong Majority Edge Colourings with Few Colours”, arXiv:2608.04122v1, first posted 2026-08-04.
4. D. W. Bange, A. E. Barkauskas, P. J. Slater, “Efficient dominating sets in graphs”, *Applications of Discrete Mathematics*, SIAM (1988). This is background for the established efficient domination notion, not a priority claim for strong-majority colourings.
