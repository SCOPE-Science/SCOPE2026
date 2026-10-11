# Exact logical depth of complete bipartite graphs
## Finding
Let \(1\le a\le b\). In the usual first-order language of finite simple graphs, write \(D(G)\) for the least quantifier rank of a sentence defining \(G\) up to isomorphism among all finite graphs. Then
\[
D(K_{a,b})=
\begin{cases}
3,&(a,b)=(1,1),\\
b+1,&\text{otherwise}.
\end{cases}
\]
Thus, apart from the two-vertex complete graph, the logical depth of a biclique is exactly one more than the size of its larger part.

## Assumptions and scope
Graphs are finite, nonempty, simple, and undirected. The language has equality and a single irreflexive symmetric adjacency relation. Quantifier rank means maximum nesting depth of quantifiers. The claim concerns definability of the individual graph \(K_{a,b}\) against arbitrary finite graphs, not merely distinguishability inside the class of complete bipartite graphs.

## Proof
Assume first that \(b\ge2\).

For the lower bound, compare \(G=K_{a,b}\) with \(H=K_{a,b+1}\). Fix a correspondence between their two bipartition classes so that the classes of size \(a\) correspond and the class of size \(b\) in \(G\) corresponds to a \(b\)-element subset of the class of size \(b+1\) in \(H\). Duplicator can preserve this side correspondence for \(b\) rounds of the Ehrenfeucht--Fraisse game: on the equal \(a\)-sides there is never a shortage, and on the larger sides at most \(b\) distinct vertices can be demanded in \(b\) rounds. Equality and adjacency are then preserved because two distinct vertices are adjacent exactly when they lie in opposite sides. Hence \(D(K_{a,b})\ge b+1\).

For the matching upper bound, use three kinds of sentences. First, there is a sentence \(\Beta\) of quantifier rank \(3\) saying that the graph is complete bipartite with both sides nonempty. One convenient formulation says: there is an edge; the relation
\[
R(x,y)\;:\Longleftrightarrow\;x=y\text{ or }\neg E(x,y)
\]
is transitive; and there is no triangle. Reflexivity and symmetry of \(R\) are automatic. Transitivity makes its classes independent sets with every pair of distinct classes completely adjacent; triangle-freeness leaves at most two classes; and the existence of an edge leaves exactly two.

Second, for \(k\ge1\), let \(\Alpha_k\) say that there are \(k\) pairwise distinct, pairwise nonadjacent vertices. It has quantifier rank \(k\), and on \(K_{u,v}\) it holds exactly when \(\max\{u,v\}\ge k\).

Third, let \(\Mu_k\) say that every vertex has at least \(k-1\) distinct other nonneighbors. It can be written with one universal quantifier followed by \(k-1\) existential quantifiers, so its quantifier rank is \(k\). On \(K_{u,v}\), it holds exactly when \(\min\{u,v\}\ge k\).

Now let \(H\not\cong K_{a,b}\). If \(H\) is not complete bipartite, \(\Beta\) distinguishes the two with rank \(3\le b+1\). Otherwise write \(H=K_{c,d}\) with \(1\le c\le d\). If \(d>b\), then \(\Alpha_{b+1}\) distinguishes them; if \(d<b\), then \(\Alpha_b\) does. If \(d=b\) but \(c<a\), then \(\Mu_a\) distinguishes them; if \(d=b\) but \(c>a\), then \(\Mu_{a+1}\) does. Every one of these ranks is at most \(b+1\). Therefore \(D(K_{a,b})\le b+1\), completing the proof for \(b\ge2\).

Finally, \(K_{1,1}=K_2\). Duplicator survives two rounds on \(K_2\) versus \(K_3\), so rank \(2\) does not define \(K_2\). A rank-3 sentence can say that the graph is complete, has at least two vertices, and has at most two vertices. Hence \(D(K_2)=3\).

## Verification
A standalone finite checker exhaustively tested the rank-3 characterization \(\Beta\) on every labeled graph with at most five vertices (1099 graphs total). It also directly solved the Ehrenfeucht--Fraisse game for the lower-bound pairs \(K_{a,b}\) versus \(K_{a,b+1}\) for \(1\le a\le b\le4\), confirming that Duplicator survives \(b\) rounds and loses in \(b+1\) rounds. The recorded output was `VERIFY_OK class_cases=1099 lower_pairs=10`. These finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work
Pikhurko, Veith, and Verbitsky developed the logical-depth invariant and proved general bounds in terms of the largest similarity class. Their Theorem 4.1 gives the exact value \(D(G)=\sigma(G)+1\) when the largest similarity class is sufficiently dominant and inclusion-maximal homogeneous. For \(K_{a,b}\) with \(a\le b\), this already gives \(D=b+1\) when \(b\ge a+2\), but it leaves the balanced and one-off-balanced cases \(b=a\) and \(b=a+1\) within a one-unit gap. The argument above closes those boundary cases and yields one formula for every biclique. The later survey by Pikhurko and Verbitsky reviews logical depth and its known classwise bounds; a full-text search found no complete-bipartite exact formula there.

## Limitations
The result is only for ordinary first-order logic without counting quantifiers. It does not determine logical width or formula length, and it does not claim a corresponding formula for complete multipartite graphs with three or more parts. The literature search did not locate an earlier statement of this exact biclique formula, but an unindexed textbook exercise, note, or folklore observation remains a residual priority risk.

## References
1. O. Pikhurko, H. Veith, O. Verbitsky, “The First Order Definability of Graphs: Upper Bounds for Quantifier Rank,” arXiv:math/0311041, first posted 2003-11-04; journal version: *Discrete Applied Mathematics* 154 (2006), 2511--2529, DOI 10.1016/j.dam.2006.03.002.
2. O. Pikhurko, O. Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865, 2010.
