# The seven-point wheel threshold for integral torsion in five-clique-free type compatibility

## Finding
Let \(\mathcal H_5\) be the countable homogeneous universal graph omitting \(K_5\). For a finite induced parameter graph \(G\subseteq\mathcal H_5\), let \(\mathcal T(G)\) be the set of all complete nonalgebraic one-point types over its individually named vertices. Define the symmetric integer matrix \(M_G\), indexed by \(\mathcal T(G)\), by putting \(M_G(S,T)=1\) exactly when distinct realizations of these two types can be adjacent, and zero otherwise.

**Sharp theorem.** For every nonempty parameter graph \(G\) of order at most six, \(\operatorname{coker}_{\mathbb Z}M_G\) has no finite torsion. The same holds for every seven-vertex parameter graph except the wheel consisting of a six-cycle and a hub adjacent to every rim vertex, denoted here by \(W_7=K_1\vee C_6\). For that unique seven-vertex isomorphism class, there are \(128\) one-point types and
\[
 \operatorname{SNF}_{\mathbb Z}(M_{W_7})=\operatorname{diag}(I_{22},2,0_{105}).
\]
Hence seven is the sharp parameter threshold for nonunit Smith factors, and the first torsion is a single \(\mathbb Z/2\mathbb Z\). The rational rank for the wheel is \(23\); its rank in characteristic two is \(22\), and its rank in every other characteristic is \(23\).

## Assumptions and scope
Graphs are finite, simple, and loopless, with their parameter vertices named individually. They are induced subgraphs of the \(K_5\)-free homogeneous graph. A nonalgebraic type is a distinct new vertex with a prescribed neighborhood \(S\subseteq V(G)\), and such a type exists precisely when \(G[S]\) contains no \(K_4\). In particular the admissible type set is the hereditary family \(\mathcal F(G)=\{S\subseteq V(G):G[S]\text{ is }K_4\text{-free}\}\).

Pairwise feasibility is existential: no simultaneous realization of three or more prescribed new vertices is claimed. The zero diagonal of the adjacency relation is irrelevant here, because the two realizations must be distinct and even two copies of the same one-point type may be adjacent.

## Proof
For \(S,T\in\mathcal F(G)\), adjoining two adjacent new vertices to \(G\) violates \(K_5\)-freeness exactly when their common old neighborhood \(S\cap T\) contains a triangle. The homogeneous graph realizes every permitted finite extension. Thus
\[
 M_G(S,T)=f_G(S\cap T),\qquad
 f_G(U)=\begin{cases}1&\text{if }G[U]\text{ is triangle-free},\\0&\text{otherwise}.\end{cases}
\]

On the hereditary type family, put \(Z_{S,U}=\mathbf1_{\{U\subseteq S\}}\), and define the integer Möbius coefficient
\[
 w_G(U)=\sum_{V\subseteq U}(-1)^{|U|-|V|}f_G(V)
 =(-1)^{|U|}\sum_{\substack{V\subseteq U\\G[V]\text{ triangle-free}}}(-1)^{|V|}.
\]
Ordering types by increasing size makes \(Z\) a square lower-unitriangular integer matrix. Möbius inversion yields the **exact unimodular congruence**
\[
 M_G=Z\operatorname{diag}(w_G(U):U\in\mathcal F(G))Z^{\mathsf T}.
\]
Consequently the integer cokernel's finite cyclic factors are the nonunit absolute values among the nonzero \(w_G(U)\), subject to the usual divisibility reordering; all factors are units if every coefficient belongs to \(\{-1,0,1\}\). To determine the first nonunit coefficient it suffices to classify \(w_H(V(H))\) over all \(K_4\)-free graphs \(H\) with at most seven vertices, because every admissible \(U\) induces such an \(H\), even if the complete base \(G\) itself contains \(K_4\).

The exhaustive certificate `census.cpp` examines **all labelled simple graphs**, not a selected graph catalogue. On \(n\) vertices it traverses each of the \(2^{\binom n2}\) edge masks, discards graphs containing any four-clique, enumerates every three-clique, and computes the alternating sum above over all \(2^n\) vertex masks. For \(n=1,2,3,4,5,6,7\), the numbers of labelled \(K_4\)-free graphs are respectively \(1,2,8,63,958,27626,1486597\). The numbers having \(|w_H(V(H))|>1\) are respectively \(0,0,0,0,0,0,420\). Every one of the \(420\) exceptions has coefficient \(2\), one universal vertex, and six vertices of degree three. Removing the universal vertex leaves a two-regular graph on six vertices. A pair of disjoint three-cycles would create a \(K_4\) with the hub, so the rim must be a single six-cycle. Conversely the labelled wheel has \(7!/12=420\) representations, accounting for every exception. This is a fully bounded exact exhaustive proof, with standalone source and checks, not an inference from sampled examples.

There is also a direct calculation of the exceptional coefficient. Without the hub, all rim subsets are triangle-free and contribute \((1-1)^6=0\) to the alternating sum. With the hub, the chosen rim vertices must be independent in \(C_6\), whose independence polynomial is \(1+6z+9z^2+2z^3\), taking value \(2\) at \(z=-1\). Therefore \(\sum_{V\subseteq W_7,\,G[V]\text{ triangle-free}}(-1)^{|V|}=-2\), and \(w_{W_7}(V(W_7))=2\).

The independent exact checker `verify_wheel.py` constructs the complete \(128\)-by-\(128\) compatibility matrix and applies Boolean finite differences to its rows and columns, an explicit unimodular congruence. It finds precisely \(105\) zeros, \(12\) entries equal to \(-1\), \(10\) entries equal to \(1\), and the single entry \(2\) in the resulting diagonal. This proves the displayed full Smith form, not merely the existence of a mod-two rank drop.

## Verification
Compile `census.cpp` with `g++ -O3 -std=c++17 -o census census.cpp` and execute `./census`. It prints the complete labelled-graph histogram for each vertex count and must terminate with `EXHAUSTIVE_CENSUS_OK`. The search range is exactly \(1\le n\le7\), including all \(2^{21}\) labelled graphs at the last size, before rejecting the four-clique-containing cases. No graph-isomorphism library or precomputed graph table is used.

Run `python3 verify_wheel.py` (Python 3 standard library only). It must report `WHEEL_VERIFY_OK` after checking all \(16384\) entries of the integer-congruence matrix against its diagonal shape. The finite computation establishes the sharp seven-point classification; the Möbius identity establishes the logical and integer-linear reduction for every finite base. No result above size seven is claimed.

## Relationship to prior work
Conant's 2014 paper [1], especially Section 3, records the Fraïssé setting, complete types and finite \(K_n\)-free extension criteria; it does not state Smith invariant factors or a seven-vertex torsion threshold. The higher clique-free complex \(\operatorname{CF}_3(G)\), consisting of triangle-free induced vertex subsets, is an existing topological-combinatorial object; Ghosh and Selvaraja [2] investigate shellability of such complexes and broader structural classes, not the specific finite universal coefficient cutoff here. A published exact computation for the twelve-vertex icosahedral \(\operatorname{CF}_3\) complex [3] concerns a different graph and its integral homotopy type; it does not imply uniqueness of a seven-vertex wheel obstruction. Existing general Möbius-incidence diagonalization principles explain the reduction to alternating subset sums but, without the exhaustive sharp cutoff, do not imply this classification.

The equivalent purely finite combinatorial statement is that among all \(K_4\)-free graphs of order at most seven, the only ones with an absolute alternating triangle-free vertex-subset sum exceeding one are seven-vertex six-rim wheels, and the sum there is \(-2\). That equivalence makes historical priority search under clique-free complex, incidence matrix and Euler-characteristic terminology essential. The claim of noncoverage is limited to inspected and searched sources, rather than an absolute guarantee of publication priority.

## Limitations
The parameter-size minimum and uniqueness are proved only through seven named vertices; larger graphs may have other torsion factors. The result concerns adjacency feasibility of two one-point types in the \(K_5\)-free homogeneous graph, not higher-order joint realizations or full type counts. The finite uniqueness step is computer-assisted by an exhaustive standalone enumerator. Independent mathematical audit has not been performed and literature priority could change if an equivalent earlier table or theorem is found.

## References
[1] Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first posted 2014-01-08, https://arxiv.org/abs/1401.1570.

[2] Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first posted 2026-02-10, https://arxiv.org/abs/2602.09623.

[3] *A Moore space from the triangle-free vertex subsets of the icosahedral graph*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-moore-space-from-the-triangle-free-vertex-subsets-of-the-icosa--51b9079b1da6/RESULT.md.
