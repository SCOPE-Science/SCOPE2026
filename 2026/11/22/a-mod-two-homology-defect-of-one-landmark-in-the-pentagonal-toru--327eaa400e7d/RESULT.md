# A mod-two homology defect of one landmark in the pentagonal torus general-position complex

## Finding
Let \(G=C_5\square C_5\), and let \(X\) be the simplicial complex of all graph-geodesic general-position subsets of \(V(G)\). Set \(Y=X[V(G)\setminus\{v\}]\), the induced subcomplex after discarding any one vertex \(v\) as an admissible landmark, **without recomputing the metric**. With coefficients in \(\mathbb F_2\), the only nonzero reduced homology is
\[
\begin{array}{c|rrr}
& j=2&j=3&j=4\\\hline
\dim\widetilde H_j(X)&50&86&20\\
\dim\widetilde H_j(Y)&44&85&12\\
\operatorname{rank}\bigl(\widetilde H_j(Y)\longrightarrow\widetilde H_j(X)\bigr)&44&74&12\\
\dim H_j(X,Y)&6&12&19
\end{array}
\]
All other reduced homology of \(X\) and \(Y\) and all other relative homology vanish. In degree three, adding the missing landmark kills an eleven-dimensional subspace of classes and creates twelve linearly independent classes. This is not detectable from the almost equal degree-three Betti numbers alone. Translation symmetry makes the result independent of \(v\).

## Assumptions and scope
Write \(V(G)=\{(i,j):0\le i,j<5\}\). The metric is the shortest-path metric of the intact toroidal graph,
\[
d((i,j),(a,b))=\min(|i-a|,5-|i-a|)+\min(|j-b|,5-|j-b|).
\]
A vertex set \(S\) is a face if no three distinct members \(a,b,c\) satisfy \(d(a,c)=d(a,b)+d(b,c)\), under any ordering of the three. This property is hereditary. In particular, \(Y\) is a vertex-induced subcomplex of \(X\), not the general-position complex of the graph obtained after deleting a graph vertex. Only \(\mathbb F_2\) coefficients and this 25-vertex graph are claimed; neither an integral homology decomposition nor a homotopy type is asserted.

## Proof
We give a complete finite certificate in `verify_result.py`, whose arithmetic consists solely of exact integers and bitwise operations. First, encode the vertex \((i,j)\) by \(5i+j\). For each unordered triple of vertices, mark it forbidden exactly when one member lies on a shortest path joining the other two, as determined by the displayed metric. A candidate simplex is a face precisely when it contains no forbidden triple. Build every face in increasing size by extending an admissible face by a larger-index vertex, rejecting extensions containing forbidden triples. Independently enumerate all subsets by size, retaining a set when all codimension-one subsets are faces. The two methods give exactly the same simplices and show that no faces have more than six vertices.

For dimensions \(0,1,2,3,4,5\), the exact face vectors of \(X\) and \(Y\) are respectively
\[
(25,300,1400,2450,1360,50),\qquad
(24,276,1232,2058,1088,38).
\]
Over \(\mathbb F_2\), a simplicial boundary column is the indicator vector of the codimension-one faces of a simplex. Gaussian elimination using highest-set-bit pivots computes the ranks of \(\partial_j\), for \(1\le j\le5\), as
\[
(24,276,1074,1290,50)\quad\text{for }X,
\qquad(23,253,935,1038,38)\quad\text{for }Y.
\]
An independent transposed, row-wise elimination produces the same ranks. Each composite of two consecutive boundary maps is checked to vanish. The reduced Betti ranks follow exactly from the chain dimensions and these ranks (subtracting one in reduced degree zero).

The quotient chain complex \(C_*(X,Y)\) has the simplices containing the removed vertex as its basis and retains only boundary terms containing that vertex. Its face vector is \((1,24,168,392,272,12)\), and the ranks of its positive-degree boundary maps are \((1,23,139,241,12)\). Therefore the relative homology dimensions in degrees \(2,3,4\) are \((6,12,19)\), and zero in all other degrees.

Finally, the inclusions on homology are computed *directly at chain level*, not inferred from dimensions alone. For each \(j\in\{2,3,4\}\), exact elimination produces a basis for the kernel of \(\partial_j^Y\). Embed these cycles into \(C_j(X)\). The difference between the rank of the span of their images together with the columns of \(\partial_{j+1}^X\), and the rank of \(\partial_{j+1}^X\) alone, is precisely the image rank of \(\widetilde H_j(Y)\to\widetilde H_j(X)\). The resulting exact ranks are \(44,74,12\). The kernel and cokernel in degree three thus have dimensions \(85-74=11\) and \(86-74=12\). Because graph translations preserve the metric, any vertex may serve as the removed landmark. This proves the stated result.

## Verification
Run `python3 verify_result.py` with Python 3; no third-party packages or network access are needed. It checks independently computed breadth-first-search distances against the closed metric expression, two complete face enumerations, full boundary compositions, column and transposed row ranks, relative chain ranks, and directly constructed homology inclusion images. All assertions passed on the packaged file. Every possible simplex is covered: the algorithm examines all 25 vertices and every admissible extension through seven vertices; absence of seven-vertex faces excludes all larger faces by heredity.

## Relationship to prior work
Klavžar, Patkós, Rus and Yero introduced and studied geodesic general-position sets in Cartesian products, including toroidal graphs; the inspected work determines extremal cardinalities and related enumerators, not the mod-two simplicial homology or puncture-induced maps calculated here. Previous work on the general-position complexes of ladder graphs concerns a distinct path-by-edge product rather than the pentagonal torus. Consequently those cited results do not entail these chain ranks or the nontrivial middle-degree map. Search cannot rule out unindexed equivalent results.

## Limitations
The result is finite, at \(C_5\square C_5\), and over \(\mathbb F_2\); it does not prove a general torus-family formula, integral torsion-freeness, sphere-wedge decompositions, or stability under actual graph-vertex deletion with recomputed distances. Exact finite enumeration is a complete proof only because all simplices and full chain boundaries are exhaustively checked, not because of a sample or an extrapolation.

## References
- S. Klavžar, B. Patkós, G. Rus, I. G. Yero, *On general position sets in Cartesian products*, arXiv:1907.04535 (first public version 10 July 2019), https://arxiv.org/abs/1907.04535; full text https://arxiv.org/html/1907.04535v4.
- P. Manuel and S. Klavžar, *A general position problem in graph theory*, Bull. Aust. Math. Soc. 98 (2018), 177–187. Cited for the original graph-geodesic general-position framework.
- *Integral homology of general-position complexes of ladder graphs*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-homology-of-general-position-complexes-of-ladder-graphs--5fa650315627. Used for scope comparison, not as a source for the numerical claims.
