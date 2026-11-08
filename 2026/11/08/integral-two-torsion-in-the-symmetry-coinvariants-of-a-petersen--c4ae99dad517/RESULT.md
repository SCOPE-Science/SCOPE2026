# Integral two-torsion in the symmetry coinvariants of a Petersen line-graph neighborhood complex

## Finding
Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph on the ten two-element subsets of \(\{0,1,2,3,4\}\), where two such subsets are adjacent precisely when disjoint. Let \(H=L(P)\), with fifteen vertices corresponding to the edges of \(P\). The Lovász open-neighborhood complex is \(X=\mathcal N(H)=\{\sigma\subseteq V(H):\sigma\subseteq N_H(v)\text{ for some }v\}\). The natural \(S_5\)-action permutes the underlying five labels.

**Integral equivariant finding.** For the group of coinvariants \(M_{S_5}=M/\langle gm-m:g\in S_5,m\in M\rangle\),
\[
\boxed{H_1(X;\mathbb Z)_{S_5}\cong(\mathbb Z/2\mathbb Z)^2.}
\]
In contrast, \(H_1(X;\mathbb Z)\cong\mathbb Z^{31}\) has no torsion, and \(H_1(X;\mathbb Q)^{S_5}=0\). The rational representation has character values shown below, for the seven cycle types of \(S_5\):

| Cycle type | \((1,1,1,1,1)\) | \((2,1,1,1)\) | \((2,2,1)\) | \((3,1,1)\) | \((3,2)\) | \((4,1)\) | \((5)\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Class size | 1 | 10 | 15 | 20 | 20 | 30 | 24 |
| \(\chi_1\) | 31 | 1 | -5 | 1 | 1 | -1 | 1 |

The corresponding \(\mathbb Q S_5\)-module decomposes as
\[
H_1(X;\mathbb Q)\cong S^{(4,1)}\oplus S^{(3,2)}\oplus3S^{(3,1,1)}\oplus S^{(2,1,1,1)}.
\]
Here \(S^\lambda\) denotes the usual rational Specht module indexed by the partition \(\lambda\). The nonequivariant homotopy equivalence \(X\simeq\bigvee^{31}S^1\) is a known consequence of general square-free neighborhood-complex results and is stated for context, **not as the new contribution**.

## Assumptions and scope
All graphs are finite, simple and undirected. No geometric embedding or alternate directed-neighborhood convention is used. Integral homology is ordinary unreduced singular homology; in positive dimensions reduced and unreduced agree. The \(S_5\)-action is specifically the natural action on subsets of five labels, inducing graph automorphisms of \(P\), \(H\), and simplicial automorphisms of \(X\). Coinvariants are taken after integral homology, **not** homology of the topological quotient \(X/S_5\), which is a different construction.

## Proof
**1. Enumerated combinatorics and an equivariant graph spine.** Enumerate the ten vertices of \(P\) lexicographically as two-element subsets, and its fifteen edges as ordered-index pairs of disjoint subsets. Then \(H\) has fifteen vertices, thirty edges and valency four. An exhaustive check of the \(\binom{15}{2}\) pairs of \(H\)-vertices shows no pair has two common neighbors; hence \(H\) has no four-cycle. Its neighborhood complex has face counts \((15,90,60,15)\) in dimensions zero through three.

Let \(B\) be the bipartite double cover of \(H\): it has left vertices \(v_L\) and right vertices \(v_R\), and an edge \(v_Lw_R\) whenever \(vw\) is an edge of \(H\). Each left-star \(F_v\) in \(B\) is a contractible cone at \(v_L\), and these stars form an \(S_5\)-stable simplicial cover. Any intersection of two or more distinct stars is empty or a **single right vertex**, since distinct \(H\)-vertices have at most one common neighbor. Their nerve is exactly \(X\), because a set of centers spans a face precisely if all share a neighbor. The equivariant simplicial nerve theorem applies to this cover and yields \(X\simeq_{S_5}B\). The latter is connected: \(H\) contains a triangle (from the three edges meeting at any vertex of \(P\)), and the bipartite double cover of a connected nonbipartite graph is connected. Thus \(B\) has thirty vertices and sixty edges, so
\[
H_1(X;\mathbb Z)\cong H_1(B;\mathbb Z)\cong\mathbb Z^{60-30+1}=\mathbb Z^{31}.
\]

**2. Exact integer action and Smith calculation.** Orient all sixty edges of \(B\) from their left endpoint to their right endpoint. Choose a breadth-first-search spanning tree rooted at the first left vertex, with neighbor edges in lexicographic order. There are twenty-nine tree edges and thirty-one chords. For each chord, form its unique integral fundamental cycle, with chord coefficient \(+1\) and signed return path in the tree. These thirty-one cycles give an integral basis of \(H_1(B;\mathbb Z)\), because \(B\) is a connected graph.

Let \(s=(0\,1)\) and \(t=(0\,1\,2\,3\,4)\) act on the original five labels. They generate all of \(S_5\), since conjugates of \(s\) under powers of \(t\) generate adjacent transpositions. Apply each permutation to the sixty oriented edges, then express each image fundamental cycle in the chosen basis simply by extracting its chord coefficients. This yields two exact \(31\times31\) matrices \(A_s,A_t\). The full integral coinvariant presentation is the \(31\times62\) matrix
\[
R=[\,A_s-I_{31}\mid A_t-I_{31}\,].
\]
A verified all-integer row/column Euclidean reduction, using only unimodular operations and with divisibility checks at each pivot, yields the **entire** Smith diagonal
\[
\operatorname{SNF}(R)=\operatorname{diag}(\underbrace{1,\ldots,1}_{29},2,2)
\]
(with thirty-one extra zero columns). This proves the claimed coinvariants: two independent classes of order two, no free component, and no other prime-primary torsion. The accompanying standard-library verifier reconstructs everything, tests every fundamental-cycle boundary, and performs the integer Smith reduction on the generated matrix rather than accepting a prestored matrix or output log.

**3. Character and rational decomposition.** The equivariant graph-chain exact sequence for connected \(B\) gives, for any \(g\in S_5\),
\[
\operatorname{tr}(g\mid H_1(B;\mathbb Q))=1-2f(g)+a(g),
\]
where \(f(g)\) counts fixed vertices of \(H\) and \(a(g)\) counts fixed directed edges of \(H\). This gives the seven displayed character values. As a separate check, enumerate all 120 label permutations and compute the alternating signed fixed-simplex Lefschetz trace on the 180 nonempty faces of \(X\); it agrees with the double-cover graph trace for **every** group element. Inner products with the standard irreducible character table of \(S_5\) give the Specht multiplicities \(1,1,3,1\) shown above, with total dimension \(4+5+3\cdot6+4=31\). The trivial and sign multiplicities vanish.

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. It exhaustively enumerates the Petersen and line graphs, their neighborhood faces, four-cycle condition, a full acyclic simplicial Morse matching (74 matched pairs, one critical vertex and thirty-one critical edges), the bipartite graph and its spanning tree, integral fundamental cycles and two group-action matrices, exact Smith invariants, and all 120 independent signed Lefschetz checks. The accompanying `verification_output.txt` is the actual captured output. Every assertion must pass. There is no finite-to-infinite extrapolation: all statements concern these explicitly finite graphs and the finite group \(S_5\).

## Relationship to prior work
The thirty-one-circle **nonequivariant** homotopy type follows from square-free graph-neighborhood methods (Kamibeppu, 2008) and is not advanced as a new theorem. The more recent graph-like neighborhood-complex classification supplies a broader nonequivariant context but explicitly does not assert equivariant structure. Shukla's results concern graphs of maximum degree at most three or four-regular circulants, and Goyal–Shukla–Singh concern clique complexes of line graphs rather than Lovász open-neighborhood complexes. None of these inspected statements gives the exact \(S_5\)-homology character or, in particular, the integral \((\mathbb Z/2)^2\) coinvariant group. The latter cannot be recovered from the rational character alone: integral lattices with the same rational character can have different coinvariants. Publication-priority uncertainty remains for literature that is not indexed or accessible.

## Limitations
This is an exact calculation for one canonical fifteen-vertex graph and its specified label-permutation group, not a classification for arbitrary line graphs. It does not identify the whole integral \(\mathbb Z S_5\)-module up to isomorphism, the homology of the orbit space, a universal equivariant circle-wedge splitting, or arbitrary larger symmetric graph families. The character is a rational invariant, while the displayed coinvariants retain specific integral information.

## References
1. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first posted 2018-02-13), https://arxiv.org/abs/1802.04526.
2. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles* (2008), Theorem 3, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
3. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first posted 2020-09-25), https://arxiv.org/abs/2009.12130.
4. *Graph-like neighborhood complexes with edge-disjoint four-cycles* (published research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d.
5. *Homotopy equivalent boundaries of cube complexes*, Geometriae Dedicata, Theorem 2.8 (equivariant simplicial nerve theorem), https://doi.org/10.1007/s10711-023-00877-w.
