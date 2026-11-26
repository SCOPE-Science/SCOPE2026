# The projective-plane exception in wheel general-position complexes

## Finding

For every integer \(n\ge3\), let \(W_{n+1}=K_1\vee C_n\) be the unweighted wheel with rim vertices \(0,\ldots,n-1\), center \(h\), and unit graph distances. Let \(X_n\) be the abstract simplicial complex whose faces are vertex sets containing no distinct triple on one graph-geodesic. Then the following is the **complete integral homotopy classification**:

\[
X_n\simeq
\begin{cases}
\{\mathrm{pt}\},&n=3,\\
S^1\vee S^1,&n=4,\\
\mathbb{RP}^2,&n=5,\\
S^2\vee\bigvee^3S^{2k-1},&n=4k\ge8,\\
S^2\vee S^{2k-1},&n=4k+1\ge9,\\
S^2\vee S^{2k},&n=4k+2\ge6,\\
S^2\vee S^{2k+1},&n=4k+3\ge7.
\end{cases}
\]

The exceptional \(X_5\) is actually **homeomorphic** to the standard six-vertex triangulation of \(\mathbb{RP}^2\), not merely homotopy equivalent. In particular its first integral homology is \(\mathbb Z/2\), while all other cases have torsion-free integral homology. The homotopy theorem for the cyclic higher-independence part is an existing result of Deshpande–Singh and is explicitly credited.

## Assumptions and scope

Here \(C_n\) means the simple cycle with \(n\ge3\) rim vertices; \(W_{n+1}\) includes one additional universal center. A three-element vertex subset is forbidden precisely when one element lies on a shortest path between the other two (including paths whose ends lie on the rim). The simplicial complex includes every subset with no forbidden triple. All homotopy equivalences concern ordinary, nonequivariant geometric realizations and integral topology; no equivariant assertion is made. The notation \(\operatorname{Ind}_2(C_n)\) denotes the **higher independence** complex of vertex subsets whose induced cycle subgraph has connected components of order at most two, not the usual independence complex or a matching complex.

## Proof

**1. The exact center–rim decomposition.** For \(n\ge4\), the distance between any two nonadjacent rim vertices is two, using the hub. Hence three rim vertices lie on a common geodesic if and only if they are three cyclically consecutive vertices. Thus the full subcomplex on the rim is precisely \(A_n=\operatorname{Ind}_2(C_n)\). A face containing the hub may contain at most two rim vertices; if there are two, they must be rim-adjacent, since otherwise the hub lies on a geodesic between them. Consequently, as abstract simplicial complexes,

\[
X_n=A_n\cup_{C_n}(h*C_n),\qquad n\ge4.
\]

Here \(C_n\) on the right is the **one-dimensional** rim polygon, included in \(A_n\), and \(h*C_n\) is its simplicial cone. This is exactly the mapping cone of \(i_n:C_n\hookrightarrow A_n\).

**2. The null attaching loop for every \(n\ge6\).** The one-skeleton of \(A_n\) is the complete graph on all rim vertices. A three-vertex subset spans a triangle of \(A_n\) unless it is one of the forbidden triples \(T_j=\{j,j+1,j+2\}\) (indices modulo \(n\)). Fix such a triple. The vertex \(v=j+4\pmod n\) lies outside \(T_j\), and each of the three triples formed by \(v\) together with two vertices of \(T_j\) is permitted for every \(n\ge6\): none is a cyclic run of three vertices (including the wraparound cases at \(n=6\)). Therefore the loop bounding the missing triangle \(T_j\) bounds a simplicial disc of three permitted triangles, coned to \(v\). All three-cycles in the complete one-skeleton are consequently nullhomotopic: present triangles fill themselves, and absent triangles have the explicit cones just constructed. All loops in a complete graph are generated normally by three-cycles; therefore \(\pi_1(A_n)=0\). In particular \(i_n\) is nullhomotopic. The mapping-cone splitting gives

\[
X_n\simeq A_n\vee\Sigma C_n\simeq A_n\vee S^2,\qquad n\ge6.
\]

This establishes the genuinely new wheel-specific splitting, independent of any finite computation.

**3. The known cycle term.** Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, Theorem 4.6 (arXiv:2001.05448, first public January 15, 2020), already prove the integral homotopy types for \(\operatorname{Ind}_r(C_n)\). Specializing their theorem to \(r=2\) (their parameter \(d=4\)) gives

\[
A_{4k}\simeq\bigvee^3S^{2k-1},\quad
A_{4k+1}\simeq S^{2k-1},\quad
A_{4k+2}\simeq S^{2k},\quad
A_{4k+3}\simeq S^{2k+1},
\]

within the specified valid \(n\)-ranges. Combining with Step 2 gives exactly the four infinite cases. These cycle homotopy types **are not new**; the new classification is the wheel mapping-cone interaction and the small-size exceptional topology.

**4. The exceptional Möbius band at \(n=5\).** The rim complex \(A_5\) has all five vertices and ten edges and exactly the five triangular facets

\[
\{0,1,3\},\quad \{0,2,3\},\quad \{0,2,4\},\quad
\{1,2,4\},\quad \{1,3,4\}.
\]

Each rim edge belongs to exactly one triangle; each of the remaining five edges belongs to exactly two triangles; all vertex links are paths. Thus \(|A_5|\) is a compact connected triangulated surface with one boundary component, precisely the rim five-cycle. Its Euler characteristic is \(5-10+5=0\). Classification of compact connected surfaces with one boundary component and Euler characteristic zero identifies \(|A_5|\) as a Möbius band. Gluing in the cone on its entire boundary produces the real projective plane: \(|X_5|\cong\mathbb{RP}^2\). In particular, \(H_1(X_5;\mathbb Z)\cong\mathbb Z/2\) and its higher positive reduced integral homology vanishes.

**5. The small boundaries.** For \(n=4\), every three-element rim set is a cyclic triple, so \(A_4\) is the one-dimensional complete graph \(K_4\), with first Betti number three. Attaching the cone on the rim four-cycle kills a primitive one-cycle (a simple embedded circuit), leaving a connected two-dimensional CW model homotopy equivalent to \(S^1\vee S^1\). For \(n=3\), the wheel is the complete graph on four vertices; no triple lies on a graph-geodesic, so its general-position complex is a full simplex and is contractible.

## Verification

The accompanying standalone `VERIFY.py` generates graph distances directly by breadth-first search, enumerates forbidden geodesic triples, and verifies the exact center–rim decomposition for \(4\le n\le13\) and the complete simplex at \(n=3\). It checks the explicit three-triangle nullhomotopy construction for every \(6\le n\le80\), and verifies all five Möbius-band facets, edge incidences, vertex links and an independent Smith normal form calculation showing that the six-vertex complex has first homology \(\mathbb Z/2\). For \(6\le n\le16\), critical-cell counts of a cycle-vertex discrete-Morse matching agree with the *published* four-periodic theorem. The infinite assertion follows from Steps 1–3 and the cited published theorem, not extrapolation from the tested finite range. No third-party source is bundled.

## Relationship to prior work

Deshpande–Singh's 2020 cycle-higher-independence homotopy theorem supplies the exact \(A_n\) term; it makes no assertion about the wheel general-position complex, the hub's attaching map, or the projective-plane exception. Yao–He–Ji–Li's February 2020 wheel general-position paper calculates the **maximum cardinality** of general-position sets and observes that the selected rim subsets have no induced three-vertex path, but does not compute their simplicial homotopy type. Iršič–Klavžar–Rus–Tuite's 2024 *General Position Polynomials* develops the face-counting invariant and related graph operations, not the wheel integral homotopy classification. The familiar minimal six-vertex triangulation of \(\mathbb{RP}^2\) is not claimed as new; its concrete realization by graph-geodesic sets of the pentagonal wheel is the new identification. The mapping-cone splitting and all-order wheel classification go beyond the cited results, notwithstanding their use of the known cycle theorem.

## Limitations

This theorem concerns unweighted ordinary wheel graphs and **ordinary** homotopy types. It does not identify the group actions on the sphere summands, arbitrary wheel edge deletions, or analogous complexes for generalized wheels. Mathematical correctness of the result is conditional only on the cited published cycle theorem and the elementary topological steps presented above. No claim of independent examination or publication priority is made. Related unindexed literature may contain equivalent statements.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first submitted 2020-01-15; Theorem 4.6. https://arxiv.org/abs/2001.05448
2. Y. Yao, M. He, S. Ji and G. Li, *On the general position set of two classes of graphs*, arXiv:2002.03108, first submitted 2020-02-08; Section 4. https://arxiv.org/html/2002.03108v1
3. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696, first submitted 2024-01-11. https://arxiv.org/html/2401.05696v1
