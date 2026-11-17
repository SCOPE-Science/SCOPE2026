# Triangle sphere summands in scale-two Rips complexes of arbitrary edge subdivisions

## Finding
Let \(G\) be an arbitrary finite connected simple undirected graph. Write \(S(G)\) for the once-edge-subdivided graph with unit-length edges. At inclusive graph-distance threshold two,
\[
K=\operatorname{VR}_{\le2}(S(G))\simeq\operatorname{Cl}(G)\vee\bigvee^{t(G)}S^2,
\]
where \(t(G)\) counts triangles (unordered three-vertex complete subgraphs). This is a homotopy equivalence of spaces, not merely a homology formula. In particular, no new topological classes are created in degrees other than two.

The original vertices induce a canonical subcomplex \(X=\operatorname{Cl}(G)\subset K\). Its integral relative homology is
\[
H_k(K,X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\{\text{triangles of }G\}},&k=2,\\
0,&k\neq2.
\end{cases}
\]
The indicated degree-two lattice has a canonical basis after orienting triangles: an automorphism of \(G\) acts on this basis by permuting triangles and multiplying by the orientation sign of its restriction to each triangle. The existence of the absolute homotopy wedge does not assert an equivariant wedge splitting.

## Assumptions and scope
A finite connected simple graph may have a single vertex. The shortest-path distance is measured in \(S(G)\), each subdivided half-edge having length one. The Vietoris–Rips convention is inclusive: a vertex subset is a simplex when all pairwise distances are at most \(2\). The graph's ordinary clique complex contains a simplex for every complete subgraph. The topological wedge is based at any choice of original vertex, and when \(t(G)=0\) has no sphere factors.

Write \(V\) and \(E\) for the vertices and edges of \(G\), regarding each edge \(e\) as the corresponding new midpoint-vertex of \(S(G)\). Two distinct original vertices are within distance two precisely when adjacent in \(G\); an original vertex and an edge-midpoint are within distance two precisely when incident; and two distinct edge-midpoints are within distance two precisely when their original edges meet. Thus the distance-two graph is the standard total graph \(T(G)\), so \(K=\operatorname{Cl}(T(G))\).

## Proof
**Step 1: classify all cliques.** Every clique in \(T(G)\) consisting only of original vertices belongs to \(X\). Any clique with at least two original vertices and one midpoint must have exactly two original vertices \(u,v\), adjacent in \(G\), and its only possible midpoint is the edge \(e=uv\). With exactly one original vertex \(v\), all midpoints belong to its incident edge set \(E_v=\{e\in E:v\in e\}\). A clique of midpoints consists of pairwise incident edges. In a simple graph, such a family either has a common endpoint or is exactly the three edges of one graph triangle (to see this, select two edges \(ab,ac\); an edge meeting both without containing \(a\) must be \(bc\), and no fourth edge can meet all three). This classifies every simplex of \(K\).

**Step 2: isolate the exceptional disks.** Put
\[
U=X\cup\bigcup_{e=uv}\Delta(\{u,v,e\}),\qquad
W=\bigcup_{v\in V}\Delta(\{v\}\cup E_v),\qquad K_0=U\cup W.
\]
Here \(\Delta(A)\) means the full simplex on vertex set \(A\); the unions include all faces. By Step 1, \(K\) is obtained from \(K_0\) by adjoining, for each unordered triangle \(abc\) of \(G\), the single two-simplex \(D_{abc}=\Delta(\{ab,bc,ca\})\). Its entire one-dimensional boundary was already in \(W\subseteq K_0\), and it is not a face of a higher-dimensional simplex in \(K\).

**Step 3: collapse the intermediate complex.** For each \(v\), order all subsets \(F\subseteq E_v\) with \(|F|\ge2\) by decreasing cardinality, treating each pair of faces \((F,F\cup\{v\})\) as an elementary free-face collapse. These pairs can be processed globally in decreasing \(|F|\). Any \(F\) of at least two distinct edges has at most one common endpoint in a simple graph; any other coface of \(F\) in \(K_0\) is a higher-dimensional face in the same star simplex and has been removed previously. Thus every elementary collapse is valid. What remains of \(W\) is the bipartite incidence graph on original vertices and midpoints, already contained in \(U\). Consequently \(K_0\searrow U\).

Now for every \(e=uv\), collapse the triangle \(\{u,v,e\}\) along its free face \(\{u,e\}\), and then collapse the residual edge \(\{v,e\}\) along the free vertex \(\{e\}\). No other remaining simplex contains the midpoint \(e\). This yields \(U\searrow X\), hence \(K_0\simeq X\) by explicit collapses relative to \(X\). The above argument also covers vertices of degree zero and degree one.

**Step 4: null-homotopic attaching maps.** Consider the attaching boundary of \(D_{abc}\), the midpoint triangle \(ab\to bc\to ca\to ab\) inside \(K_0\). Its edges are homotopic, using the triangles \(\{b,ab,bc\},\{c,bc,ca\},\{a,ca,ab\}\) in \(W\), to the six-cycle
\[
ab\to b\to bc\to c\to ca\to a\to ab.
\]
Using the triangles \(\{a,b,ab\},\{b,c,bc\},\{c,a,ca\}\) in \(U\), this six-cycle is homotopic to the original triangle loop \(a\to b\to c\to a\). The last loop bounds the simplex \(\{a,b,c\}\in X\), so every attaching map is null-homotopic *already in* \(K_0\). Since \(K_0\) is connected, adjoining these independently null-homotopic two-cells gives the CW homotopy type \(K_0\vee\bigvee^{t(G)}S^2\), and the claimed wedge follows from \(K_0\simeq X\). This does not require any assumption about higher homotopy groups of \(X\).

**Step 5: relative integral homology and symmetry.** The relative simplicial chain complex \(C_*(K,K_0;\mathbb Z)\) is freely generated in dimension two by the oriented exceptional midpoint triangles \(D_{abc}\), with no other relative generators or differentials. By the relative homology long exact sequence for the triple \((K,K_0,X)\), and since \(K_0\searrow X\), this identifies \(H_2(K,X;\mathbb Z)\) canonically with the free abelian group on oriented graph triangles, and annihilates other relative homology groups. Every graph automorphism preserves \(X\) and \(K_0\), and permutes the exceptional triangles with their orientation signs. The correspondence between vertex-triangle orientations and the complementary-edge midpoint orientations is equivariant under the permutation group on three letters (its sign character is unchanged), proving the asserted integral automorphism action.

## Verification
The standard-library checker `verify_total_rips.py` exhaustively tests every connected labeled simple graph of orders one through five (respectively \(1,1,4,38,728\) graphs, totaling \(772\)). For each graph it constructs both the explicit subdivided graph and the proposed total graph, verifies every distance-two adjacency, enumerates all simplices, computes reduced homology over \(\mathbb F_2\) with exact binary elimination, compares with the predicted ranks, and replays every free-face collapse in Steps 2–3. It reports `TOTAL_GRAPH_SCALE_TWO_RIPS_COLLAPSE_PASS`. The finite check illustrates and probes the construction; the proof of the universal assertion is the five-step combinatorial argument above, not the finite test.

## Relationship to prior work
Larrión–Pizaña–Villarroel-Flores (2009, Corollary 5.4) established that the clique complexes of a connected graph and its total graph have isomorphic fundamental groups, without identifying the full homotopy type or the new integral two-dimensional relative module. Their paper discusses an earlier homology comparison of Prisner (1991) principally for first homology. Goyal–Shukla–Singh (2020, Lemma 3.2) identified a related homotopy type for the ordinary line graph; that is a different construction and does not yield the extra triangle spheres here. A separately established classification for the subdivision of a complete graph gives the special case of \(t(G)=\binom{n}{3}\) but not the arbitrary-graph or signed integral-module assertion. These comparisons concern mathematical implications, not title matching.

## Limitations
The theorem does not classify the *entire* Vietoris–Rips filtration of \(S(G)\) at scales other than two, nor does it say \(K\) is a sphere wedge when \(\operatorname{Cl}(G)\) is not one. The homotopy wedge is not constructed equivariantly. The 1991 article of Prisner remains a material literature-access risk because its complete text was not available for checking; its mention in the 2009 inspected paper does not resolve what other homology results might occur in that original article. An equivalent unindexed theorem cannot be ruled out. The displayed classification has not undergone independent mathematical validation.

## References
1. F. Larrión, M. A. Pizaña, R. Villarroel-Flores, *The fundamental group of the clique graph*, European Journal of Combinatorics 30 (2009), 288–294, DOI: `10.1016/j.ejc.2007.12.006`. Open author manuscript: `https://xamanek.izt.uam.mx/map/papers/Fundame06w.pdf`.
2. S. Goyal, S. Shukla, A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:`2009.12130` (2020), `https://arxiv.org/pdf/2009.12130`.
3. E. Prisner, *Homology of the line graph and of related graph-valued functions*, Archiv der Mathematik 56 (1991), 400–404, DOI: `10.1007/BF01198228`. Full text not inspected.
