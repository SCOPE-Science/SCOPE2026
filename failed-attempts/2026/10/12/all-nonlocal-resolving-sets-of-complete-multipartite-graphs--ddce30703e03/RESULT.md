# All nonlocal resolving sets of complete multipartite graphs
## Finding
Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge2,\qquad N=\sum_{i=1}^r n_i,
\]
with partite classes \(V_1,\ldots,V_r\). A set \(S\subseteq V(G)\) is nonlocal resolving if and only if
\[
|V_i\setminus S|\le1
\]
for every non-singleton part \(V_i\).

Consequently,
\[
\dim_{n\ell}(G)=N-r.
\]
If \(s=|\{i:n_i=1\}|\), then the complete cardinality enumerator is
\[
R_{n\ell}(G;z)
=
\sum_{\substack{S\subseteq V(G)\\S\text{ nonlocal resolving}}}z^{|S|}
=
z^{N-r}(1+z)^s\prod_{i:n_i\ge2}(n_i+z).
\]
The minimum nonlocal resolving sets omit exactly one vertex from every non-singleton part and omit every singleton vertex. Hence the number of nonlocal metric bases is
\[
\prod_{i:n_i\ge2}n_i,
\]
with the empty product interpreted as \(1\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. A set \(S\subseteq V(G)\) is nonlocal resolving if every two nonadjacent vertices \(u,v\) are distinguished by some landmark \(w\in S\):
\[
d(w,u)\ne d(w,v).
\]
The theorem applies to arbitrary connected complete multipartite graphs, including complete graphs, complete bipartite graphs, stars, and Turán graphs.

## Proof
In a complete multipartite graph, two distinct vertices are nonadjacent exactly when they lie in the same part. Fix distinct \(u,v\in V_i\).

If \(w\notin\{u,v\}\) lies in \(V_i\), then
\[
d(w,u)=d(w,v)=2.
\]
If \(w\) lies in a different part, then
\[
d(w,u)=d(w,v)=1.
\]
Thus every third vertex has equal distance to \(u\) and \(v\). Only the endpoints themselves can distinguish the pair, since
\[
d(u,u)=0\ne2=d(u,v),
\]
and symmetrically for \(v\).

Therefore \(S\) resolves all nonadjacent pairs inside \(V_i\) exactly when \(S\cap V_i\) meets every two-element subset of \(V_i\), equivalently
\[
|S\cap V_i|\ge n_i-1.
\]
Singleton parts impose no condition. The partwise constraints are independent, so
\[
\dim_{n\ell}(G)=\sum_i(n_i-1)=N-r.
\]

For the enumerator, a singleton part contributes \(1+z\). A part of size \(n_i\ge2\) contributes
\[
n_i z^{n_i-1}+z^{n_i}
=
z^{n_i-1}(n_i+z),
\]
because a valid set selects either all vertices of the part or all but one. Multiplication gives the displayed polynomial.

Minimum size requires selecting exactly \(n_i-1\) vertices in every non-singleton part and no singleton vertex. Each non-singleton part contributes \(n_i\) choices for its omitted vertex, proving the basis count.

## Verification
The included verifier constructs every connected complete multipartite isomorphism type of orders \(2\) through \(10\), computes all-pairs distances by breadth-first search, and tests every vertex subset directly against the nonlocal-resolving definition. It separately checks the structural criterion, every coefficient of the product formula, the dimension, and the basis count.

## Relationship to prior work
Nonlocal metric dimension was introduced in 2022. The defining paper proves general bounds and characterizations and shows that an \(n\)-vertex connected graph has nonlocal metric dimension \(n-2\) exactly when it is complete bipartite. Its proof already observes the endpoint-only distinguishing phenomenon inside each bipartition class.

The same source does not treat arbitrary complete multipartite graphs in its searchable full text. The present theorem extends the complete-bipartite mechanism to every number and profile of parts and strengthens the scalar conclusion to a complete classification of all nonlocal resolving sets, a factored cardinality enumerator, and an exact basis count.

Targeted searches using complete multipartite, complete \(r\)-partite, Turán, and nonlocal-resolving terminology did not locate an arbitrary-part-size theorem equivalent to this statement.

## Limitations
The theorem uses the standard vertex nonlocal metric-dimension definition. It does not address local metric dimension, ordinary metric dimension, doubly resolving sets, multiset variants, or edge-based variants.

The complete-bipartite scalar case is prior work and is recovered as a specialization. The originality claim is the arbitrary complete-multipartite all-set classification, enumerator, and basis description.

The exhaustive computation through order \(10\) is corroborative only. The theorem for arbitrary part sizes follows from the endpoint-only distinguishing argument.

## References
1. S. Klavžar, D. Kuziak, “Nonlocal metric dimension of graphs,” arXiv:2211.10614v1, 19 November 2022; Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), Article 57, DOI 10.1007/s40840-022-01459-x.
