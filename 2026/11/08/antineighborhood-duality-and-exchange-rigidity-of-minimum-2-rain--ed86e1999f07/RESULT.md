# Antineighborhood duality and exchange rigidity of minimum 2-rainbow functions on the Petersen graph

## Finding
Let \(P\) be the Petersen graph, represented as the Kneser graph \(KG(5,2)\). A 2-rainbow dominating function assigns a subset of \(\{1,2\}\) to each vertex so that every empty-labeled vertex sees both colors among its neighbors; its weight counts color incidences, including both incidences of a doubly labeled vertex. Write \(A\) and \(B\) for the supports of the first and second colors. For \(S\subseteq V(P)\), let \(N[S]\) be the union of its closed neighborhoods and let \(\Phi(S)=V(P)\setminus N[S]\).

**Theorem.** The minimum weight is \(5\), and the **entire** family of minimum functions is
\[
\bigl\{(A,\Phi(A)),\ (\Phi(A),A): A\subseteq V(P),\ |A|=2,\ A\text{ is independent}\bigr\}.
\]
There are exactly \(60\) such functions. Each \(\Phi(A)\) is a three-vertex induced path and satisfies \(\Phi(\Phi(A))=A\); thus the 30 independent pairs and 30 induced three-vertex paths are paired by mutual closed-antineighborhood complementation. Every minimum function gives distinct colors to five distinct vertices, with support sizes \(2\) and \(3\) in some order. Under either unrestricted **single-color token jumping** or edge-restricted **single-color token sliding**, all \(60\) minimum functions are isolated: neither color can be moved individually while keeping the weight minimal and the 2-rainbow condition.

## Assumptions and scope
The graph is exactly \(KG(5,2)\), with vertices the ten two-subsets of \(\{1,2,3,4,5\}\), adjacent when disjoint; it is isomorphic to the standard generalized Petersen graph \(GP(5,2)\). The two color supports \(A,B\) may in general overlap, representing vertices labeled with both colors. A legal jump removes one incidence of a specified color from one vertex and adds that incidence at another vertex not already carrying the color. A legal slide is such a jump along an edge of \(P\). Both moves preserve weight automatically, and a move is accepted only if the resulting function is also 2-rainbow dominating. Color names are distinguished; global exchange of the two names produces a separate function. There is no assertion about other graphs, greater-than-minimum weights, or moves that simultaneously change both colors.

## Proof
For a color support \(S\), each vertex outside \(N[S]\) cannot remain empty and must therefore carry the *other* color, unless it already carries the first color, which is impossible outside \(N[S]\). Consequently \(\Phi(S)\) is contained in the opposite color support. The Petersen graph is cubic, triangle-free, and has exactly one common neighbor for any two nonadjacent vertices. Hence a singleton \(S\) has \(|\Phi(S)|=6\); a two-set has \(|\Phi(S)|=4\) if adjacent, and \(|\Phi(S)|=3\) if independent.

Suppose the total weight is at most five. No color support can be empty (then all ten vertices must be nonempty), and neither can have size one: the opposite support would require at least six vertices. Therefore both color-support sizes are at least two. A weight-at-most-four function would have two supports of size exactly two; but \(|\Phi(S)|\ge3\) for either support, contradiction. Thus the minimum weight is at least five.

At weight five the support sizes must be \((2,3)\) or \((3,2)\). Consider the two-vertex support \(A\) and three-vertex opposite support \(B\). Since \(\Phi(A)\subseteq B\), the two vertices of \(A\) cannot be adjacent, for that would give \(|\Phi(A)|=4\). For independent \(A\), \(|\Phi(A)|=3\), forcing \(B=\Phi(A)\). In particular the supports are disjoint and none of the minimum functions doubly labels a vertex.

Every independent pair is equivalent under the natural \(S_5\) action to \(A=\{12,13\}\) (notation denotes two-element subsets). Directly from disjointness adjacency,
\[
\Phi(\{12,13\})=\{14,15,23\}=B,\quad
\Phi(B)=\{12,13\}.
\]
Here \(B\) induces the path \(14-23-15\), and the five empty-labeled vertices are \(24,25,34,35,45\). They meet both supports in their neighborhoods: respectively, they see the pairs \((13,15),(13,14),(12,15),(12,14),(12,23)\). Thus \((A,B)\) is valid. Relabeling \(\{1,2,3,4,5\}\) proves validity, the reverse-complement identity, and the induced-path property for all independent pairs. There are \(\binom{10}{2}-15=30\) independent pairs. As the graph is triangle-free and cubic, each induced three-vertex path has a unique middle vertex, so there are also \(10\binom{3}{2}=30\) such paths. The reverse-complement identity makes the correspondence a bijection. Swapping the color names gives exactly \(2\cdot30=60\) functions, which attain weight five.

Finally the second support is uniquely forced by the first: if one support has size two the other equals its closed antineighborhood; if one support has size three it is an induced path and its opposite support equals its closed antineighborhood. Any one-color move leaves the other support unchanged but would replace the uniquely determined partner. No distinct minimum function can arise. All single-color jumps, and hence all slides, are impossible. This completes the proof.

## Verification
The standalone dependency-free program `check_kneser.py` checks all 30 independent pairs, their three-vertex complementary paths, both complement identities, all 60 constructed configurations, and the absence of single-color jumps. Independently, `check_petersen_exhaustive.py` builds \(GP(5,2)\) with outer cycle, five spokes and inner pentagram, examines all \(4^{10}\) vertex labelings, and verifies the minimum weight, support distribution, total count, and all single-color jumps and slides. Both programs were executed from the paths embedded here; `kneser_output.txt` and `petersen_output.txt` contain their standard outputs. The proof does not rely solely on these enumerations.

## Relationship to prior work
Brešar and Kraner Šumenjak (2007) relate 2-rainbow domination to ordinary domination of \(G\square K_2\) and establish generalized Petersen bounds; Tong, Lin, Yang and Luo (available online March 9, 2009) prove the exact 2-rainbow number for the entire \(GP(n,2)\) family, including the **already known** value five for \(GP(5,2)\). That numerical minimum is not claimed new. The present result is the exhaustive *classification of all* optimum assignments as the independent-pair/induced-path antineighborhood duality, with the associated exact immobility under individual color relocation. Gabrovšek, Peperko and Žerovnik (2020) instead study **independent** rainbow functions, with a distinct value six for \(GP(5,2)\); this stronger feasibility restriction cannot imply our configurations. Brezovnik and collaborators (2021, 2023) give number-focused results for generalized Petersen families, rather than this fixed-graph optimum-state classification. The general product equivalence does not itself enumerate optimum dominating sets of the Petersen prism.

## Limitations
The claim concerns one ten-vertex graph and fixes colored labels and single-color relocation; it provides no asymptotic theorem or simultaneous two-color relocation result. Historical priority is subject to the possibility of unindexed computations or an uninspected detailed passage of Tong et al. (2009), whose publicly visible author-hosted material supplied the abstract, introduction, and publication record but not an independently inspected complete paper. A similarly small graph might have been exhaustively classified elsewhere. No independent scholarly audit is claimed.

## References
1. B. Brešar and T. Kraner Šumenjak, *On the 2-rainbow domination in graphs*, Discrete Applied Mathematics 155 (2007), 2394–2400, DOI: 10.1016/j.dam.2007.07.018.
2. C. Tong, X. Lin, Y. Yang and M. Luo, *2-rainbow domination of generalized Petersen graphs P(n,2)*, Discrete Applied Mathematics 157 (2009), 1932–1937, DOI: 10.1016/j.dam.2009.01.020. Online March 9, 2009.
3. B. Gabrovšek, A. Peperko and J. Žerovnik, *Independent Rainbow Domination Numbers of Generalized Petersen Graphs P(n,2) and P(n,3)*, Mathematics 8 (2020), 996, DOI: 10.3390/math8060996.
4. S. Brezovnik et al., *On 2-Rainbow Domination Number of Generalized Petersen Graphs P(5k,k)*, Symmetry 13 (2021), 809, DOI: 10.3390/sym13050809.
5. S. Brezovnik, D. Rupnik Poklukar and J. Žerovnik, *On 2-Rainbow Domination of Generalized Petersen Graphs P(ck,k)*, Mathematics 11 (2023), 2271, DOI: 10.3390/math11102271.
