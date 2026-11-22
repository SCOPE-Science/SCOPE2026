# Geodetic and edge-geodetic sets coincide on bipartite girth-six diameter-three graphs

## Finding
Let \(G\) be a finite, connected, simple bipartite graph with at least one edge, diameter at most three, and no cycle of length four. A subset \(S\subseteq V(G)\) is geodetic if and only if it is edge-geodetic. Here geodetic means that every vertex lies on *some* shortest path between vertices of \(S\); edge-geodetic means that every edge lies on *some* such path. The witnessing shortest paths need not be chosen consistently for different edges. Consequently, the two entire families of successful vertex sets, their cardinality polynomials, and their inclusion-minimal sets coincide.

In particular, this equivalence holds for the point–line incidence graph of **every** finite projective plane (of order at least two). For the Fano plane's incidence graph \(H\) (the Heawood graph), the inclusion-minimal edge-geodetic sets admit the following exhaustive geometric classification. A *flag* is an incident point–line pair \((p,L)\), and a *nonflag* is a nonincident pair.

| Class | Selected vertices | Count | Size |
|---|---|---:|---:|
| Flags | The two points of \(L\setminus\{p\}\), and the two lines through \(p\) other than \(L\) | 21 | 4 |
| Off-incident families | A line \(L\) together with all four points not on it; or dually a point \(p\) together with all four lines not through it | 14 | 5 |
| Nonflags | The three points on \(L\) and three lines through \(p\), for \(p\notin L\) | 28 | 6 |
| Full shores | All seven points, or all seven lines | 2 | 7 |

Thus the inclusion-minimal set enumerator is
\[
\mathcal M_H(z)=21z^4+14z^5+28z^6+2z^7.
\]
The complete cardinality polynomial for **all** edge-geodetic (equivalently geodetic) sets is
\[
\begin{split}
\mathcal E_H(z)={}&21z^4+224z^5+931z^6+1962z^7+2394z^8\\
&+1862z^9+987z^{10}+364z^{11}+91z^{12}+14z^{13}+z^{14}.
\end{split}
\]
The upper edge-geodetic number (largest cardinality of an inclusion-minimal edge-geodetic set) is seven. The minimum cardinality four and its 21 flag bases are **previously established** by the general projective-plane geodetic-basis result listed in the references; they are not claimed as new. The general all-set equivalence and the higher-size minimal-set classification are the asserted contributions.

## Assumptions and scope
All graphs are undirected, unweighted, finite, connected, simple, and have at least one edge. Distances are shortest-path lengths. For \(a,b\in V(G)\), let \(I[a,b]\) denote the set of all vertices on at least one \(a\)–\(b\) geodesic; let \(I_E[a,b]\) be the analogous set of edges. For \(S\subseteq V(G)\), the vertex (respectively edge) geodesic hull at one step is the union of \(I[a,b]\) (respectively \(I_E[a,b]\)) for distinct \(a,b\in S\). A set is geodetic when its vertex union is \(V(G)\), and edge-geodetic when its edge union is \(E(G)\). This is *not* strong geodeticity, where one geodesic must be fixed for each selected pair, and *not* monitoring edge-geodeticity, which involves mandatory edge passage through all geodesics.

## Proof
**General equivalence.** If every edge is covered by selected-endpoint geodesics, every vertex, being incident to at least one edge, is covered too. Hence edge-geodetic implies geodetic.

Conversely assume \(S\) geodetic. Every vertex \(v\notin S\) lies internally on an \(S\)-endpoint geodesic. Since the diameter is at most three, the witness has two or three edges, so \(v\) has a neighbor \(w(v)\in S\): choose the selected endpoint immediately adjacent to \(v\) along a witness. Now fix an arbitrary edge \(uv\).

If \(u,v\in S\), the one-edge path \(uv\) is a selected-endpoint geodesic. If \(u\in S\) and \(v\notin S\), let \(w=w(v)\). When \(w=u\), the selected-endpoint witness path through \(v\) includes \(uv\): its endpoint \(u\) is adjacent to \(v\), and a shortest path containing both consecutive vertices can use no detour between them. More simply, if a witness is rooted at \(u\) and contains \(v\), its first step must be \(uv\), since any return to \(v\) after another first step would contradict shortestness. If \(w\ne u\), the two-edge path \(u-v-w\) is geodesic because bipartiteness forbids the edge \(uw\). The symmetric mixed case is identical.

Finally, when neither endpoint belongs to \(S\), choose selected neighbors \(x=w(u)\) and \(y=w(v)\). The path \(x-u-v-y\) has three edges, distinct vertices, and endpoints on opposite sides of the bipartition. If \(x\) and \(y\) were adjacent, these edges would form a four-cycle; by hypothesis they are not. Their graph distance is therefore an odd integer at least three, and the displayed three-edge path is geodesic. Thus \(uv\) is covered in all cases, proving the equivalence.

**Projective-plane consequence.** In a finite projective plane of order \(q\ge2\), two points share a unique line, two lines share a unique point, and a nonincident point–line pair is connected by a three-edge shortest path. The incidence graph is bipartite, has diameter three, and has no four-cycle because distinct points cannot share two lines. Therefore the theorem applies for every order and for non-Desarguesian planes as well.

**Fano classification and complete counts.** Label the seven points \(p_i\) and seven lines \(\ell_j\), with indices modulo seven and incidence \(p_i\in\ell_j\) exactly when \(i-j\in\{0,1,3\}\). This produces a cubic connected bipartite graph with diameter three and 21 edges. To certify **exhaustively** the stated finite classification, enumerate the 16,384 subsets of its 14 vertices, and for every pair \(a,b\) of chosen vertices mark all vertices and edges on *all* shortest \(a\)-to-\(b\) paths. A selected set is successful if its union covers all 21 edges; it is inclusion-minimal precisely when deleting each individual selected vertex destroys that property (monotonicity justifies single-deletion testing).

The independent implementations described next agree that there are exactly 65 inclusion-minimal sets, in the counts \(21,14,28,2\) at cardinalities four through seven. A separate explicit constructor enumerates all four displayed projective families, checks they contain 65 *distinct* masks, and compares their masks for exact equality with the independently found minimal masks. This is exhaustive enumeration of a finite set, not inference from sampled configurations. The same enumeration counts *every* successful subset to obtain the stated complete polynomial.

The size-four flag classification and lower bound are also available from the prior general projective-plane theorem. They are reproduced here solely for the completeness of the new higher-cardinality classification.

## Verification
Two independent standalone checkers are included. Run `python3 verify_fano.py` and compile/run `g++ -O2 -std=c++17 -Wall -Wextra verify_fano.cpp -o verify_fano && ./verify_fano`. The Python checker constructs shortest paths directly by breadth-first search and depth-first shortest-path traversal, unions their vertices and edges, enumerates every subset, and matches 65 minimal masks against all four geometrically defined families. The C++ checker instead calculates an all-pairs Floyd–Warshall distance matrix, uses \(d(a,u)+1+d(v,b)=d(a,b)\) or its reverse to test edge inclusion on a geodesic, and independently exhausts all subsets. Both assert all eleven nonzero all-set coefficients and the four minimal-cardinality counts. Both executed successfully as part of the preparation of this result.

## Relationship to prior work
The fundamental edge-geodetic definition and standard inequalities come from Santhakumaran and John, *Edge geodetic number of a graph* (print volume 2007; publisher's online entry June 3, 2013), and their subsequent work on upper edge-geodetic numbers (2009). The accessible full texts address complete bipartite graphs and general upper-bound properties, but do not state the girth-six/diameter-three whole-family equivalence or the Heawood 65-set classification.

A previously published indexed mathematical result on ordinary geodetic bases of all finite projective-plane incidence graphs already proves the smallest cardinality \(2q\) and classifies its minimum sets, and therefore covers the Heawood flag bases. That older result does not state that every ordinary geodetic set is also edge-geodetic, or give the additional 44 minimal Heawood sets of sizes five through seven. Results on *strong* geodetic, *edge-metric* resolving, or *monitoring* edge-geodetic configurations do not imply equality of the present two set families because their predicates differ.

## Limitations
The theorem deliberately assumes both the diameter and girth restrictions. A necessary contrast is \(K_{3,3}\): choose two vertices from each shore. This four-vertex set is geodetic, but the edge between its two unchosen vertices cannot belong to a shortest path between chosen endpoints, so the edge-geodetic property fails. Thus the no-four-cycle assumption cannot simply be deleted. The calculation of the Heawood polynomial is a complete finite verification, not a closed formula for arbitrary projective-plane orders. Some earlier research records, inaccessible relevant historical material, and unindexed calculations could still affect priority; the originality assessment is not an independent certification.

## References
1. A. P. Santhakumaran and J. John, *Edge geodetic number of a graph*, Journal of Discrete Mathematical Sciences and Cryptography **10** (2007), 415–432; publisher online posting June 3, 2013. DOI: https://doi.org/10.1080/09720529.2007.10698129 ; available full text: https://connectjournals.com/file_full_text/14403H_jdmsc174_415-432.pdf
2. A. P. Santhakumaran and J. John, *The upper edge geodetic number and the forcing edge geodetic number of a graph*, Opuscula Mathematica **29** (2009), 427–441. DOI: https://doi.org/10.7494/OpMath.2009.29.4.427 ; full text: https://bibliotekanauki.pl/articles/255845.pdf
3. *Geodetic bases of finite projective-plane incidence graphs: flag rigidity and a sharp simultaneous-exchange threshold* (previously published mathematical finding, October 18, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-geodetic-bases-of-finite-projective-plane-incidence-graphs-flag--25deca33c37d ; source inspection was limited to the indexed mathematical summary.
