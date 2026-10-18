# Three visibility polynomials of complete multipartite graphs
## Finding
Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge2,\qquad N=\sum_{i=1}^r n_i,
\]
with partite classes \(V_1,\ldots,V_r\). Let \(\mathcal V(G;z)\), \(\mathcal V_{\rm o}(G;z)\), and \(\mathcal V_{\rm d}(G;z)\) count ordinary mutual-, outer mutual-, and dual mutual-visibility sets by cardinality.

If every \(n_i=1\), then \(G\) is complete and
\[
\mathcal V(G;z)=\mathcal V_{\rm o}(G;z)=\mathcal V_{\rm d}(G;z)=(1+z)^N.
\]

Assume at least one part is non-singleton. Then
\[
\mathcal V(G;z)
=(1+z)^N-z^N-
\sum_{i:n_i\ge3}\sum_{j=1}^{n_i-2}\binom{n_i}{j}z^{N-j},
\]
\[
\mathcal V_{\rm o}(G;z)
=(1+z)^N-z^N-
\sum_{i:n_i\ge2}\sum_{j=1}^{n_i-1}\binom{n_i}{j}z^{N-j},
\]
and
\[
\mathcal V_{\rm d}(G;z)
=(1+z)^N-z^N-
\sum_{i:n_i=2}z^{N-2}-
\sum_{i:n_i\ge3}\sum_{j=1}^{n_i}\binom{n_i}{j}z^{N-j}.
\]

Equivalently, for \(Y=V(G)\setminus X\):

- \(X\) is an ordinary mutual-visibility set exactly when \(Y\) meets at least two parts, or nonempty \(Y\subseteq V_i\) satisfies \(|V_i\setminus Y|\le1\).
- \(X\) is an outer mutual-visibility set exactly when \(Y\) meets at least two parts, or \(Y=V_i\) for one part.
- \(X\) is a dual mutual-visibility set exactly when \(Y\) meets at least two parts, or \(Y\) is a singleton in a part of size at most two.

The empty complement \(Y=\varnothing\) is valid exactly in the complete-graph case.

Consequently, outside complete graphs,
\[
\mu(G)=\mu_{\rm d}(G)=
\begin{cases}
N-1,&\min_i n_i\le2,\\
N-2,&\min_i n_i\ge3,
\end{cases}
\qquad
\mu_{\rm o}(G)=
\begin{cases}
N-1,&\min_i n_i=1,\\
N-2,&\min_i n_i\ge2.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. Vertices \(u,v\) are \(X\)-visible if some shortest \(u,v\)-path has no internal vertex in \(X\). Ordinary mutual visibility requires this for pairs inside \(X\); outer mutual visibility additionally requires it for pairs with one endpoint in \(X\) and one outside; dual mutual visibility additionally requires it for pairs outside \(X\). The total visibility polynomial is not part of this claim.

## Proof
Put \(Y=V(G)\setminus X\). Vertices from distinct partite classes are adjacent and hence automatically \(X\)-visible. The only nonadjacent pairs are distinct vertices in one part \(V_i\). Every shortest path between such a pair has length two and uses one internal vertex from \(V(G)\setminus V_i\). Therefore a same-part pair is \(X\)-visible exactly when
\[
Y\setminus V_i\ne\varnothing.
\tag{1}
\]

For ordinary mutual visibility, condition (1) is required for \(V_i\) exactly when \(|X\cap V_i|\ge2\). If \(Y\) meets at least two parts, (1) holds for every part. If nonempty \(Y\subseteq V_i\), the only possible failure is in \(V_i\), and validity is equivalent to \(|V_i\setminus Y|\le1\). If \(Y=\varnothing\), all parts must be singletons.

For outer mutual visibility, condition (1) is required for each non-singleton \(V_i\) containing a selected vertex: either two selected vertices form a required pair, or a selected and an unselected vertex do. Thus when nonempty \(Y\subseteq V_i\), validity forces \(X\cap V_i=\varnothing\), equivalently \(Y=V_i\). Complements meeting at least two parts always work.

For dual mutual visibility, condition (1) is required for \(V_i\) when either \(|X\cap V_i|\ge2\) or \(|Y\cap V_i|\ge2\). If nonempty \(Y\subseteq V_i\), validity therefore requires both \(|X\cap V_i|\le1\) and \(|Y|\le1\), so \(Y\) is a singleton and \(n_i\le2\). Complements meeting at least two parts again always work.

The polynomial identities follow by subtracting invalid complements from all subsets, weighted by \(z^{N-|Y|}\). For ordinary visibility the invalid complements are \(Y=\varnothing\) and nonempty \(Y\subseteq V_i\) of size at most \(n_i-2\) for \(n_i\ge3\). For outer visibility they are \(Y=\varnothing\) and all nonempty proper subsets of non-singleton parts. For dual visibility they are \(Y=\varnothing\), the whole two-vertex part when \(n_i=2\), and every nonempty subset of \(V_i\) when \(n_i\ge3\). Nonempty subsets from different parts are distinct, so no further inclusion-exclusion is needed.

## Verification
The included checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(9\). For every vertex subset \(X\), it tests visibility directly by comparing the original shortest-path distance with the shortest-path distance after deleting \(X\setminus\{u,v\}\) as possible internal blockers. It independently tests ordinary, outer, and dual pair requirements, then compares the entire valid-set family and all polynomial coefficients with the theorem.

## Relationship to prior work
The ordinary mutual-visibility problem was introduced in 2021. The total, outer, and dual variants were systematized in 2023; that source develops their relations, complexity, and several graph families but contains no complete-multipartite treatment in its searchable text.

A 2024 diameter-two study includes cographs, hence supplies broader scalar context for complete multipartite graphs. It does not enumerate all valid sets by cardinality.

Visibility polynomials were introduced in 2025. That paper gives all four polynomials for balanced complete bipartite graphs \(K_{n,n}\) and notes that general complete bipartite graphs can be handled similarly. The three formulas above specialize exactly to those balanced-bipartite expressions and extend the ordinary, outer, and dual enumerations to arbitrary multipartite part sizes.

A 2026 game paper determines the ordinary mutual-visibility number of arbitrary complete multipartite graphs and describes maximal ordinary sets relevant to the game. This agrees with the degree of \(\mathcal V(G;z)\), but does not provide the three all-cardinality enumerators here.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The total visibility polynomial is deliberately excluded because it has separate existing coverage. The 2025 balanced-bipartite formulas are a strong precursor, and the 2026 paper covers the ordinary scalar maximum on arbitrary complete multipartite graphs. The originality claim is specifically the arbitrary-part-size all-set classification and cardinality enumeration for ordinary, outer, and dual visibility. Finite computation is corroborative only.

## References
1. G. Di Stefano, “Mutual Visibility in Graphs,” arXiv:2105.02722v1, 6 May 2021.
2. S. Cicerone, G. Di Stefano, L. Drožđek, J. Hedžet, S. Klavžar, I. G. Yero, “Variety of mutual-visibility problems in graphs,” arXiv:2304.00864v1, 3 April 2023; Theoretical Computer Science 974 (2023), 114096.
3. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, “Mutual-visibility problems on graphs of diameter two,” European Journal of Combinatorics 120 (2024), 103995, DOI 10.1016/j.ejc.2024.103995.
4. C. Bujtás, S. Klavžar, J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” Aequationes Mathematicae 99 (2025), 1883–1901, DOI 10.1007/s00010-025-01197-y.
5. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan, J. Tian, “Builder-Blocker Mutual-Visibility Game,” Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), Article 89, DOI 10.1007/s40840-026-02083-9.
