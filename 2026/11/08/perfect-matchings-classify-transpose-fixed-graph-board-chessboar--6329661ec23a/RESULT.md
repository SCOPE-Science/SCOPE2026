# Perfect matchings classify transpose-fixed graph-board chessboard complexes

## Finding

Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\ge1\). On the symmetric rook board
\[
B_G=\{(v,v):v\in V\}\cup\{(u,v),(v,u):\{u,v\}\in E\},
\]
let \(\Delta(B_G)\) be the simplicial complex of placements of nonattacking rooks. Transposition \(\tau(u,v)=(v,u)\) is an involution. Denote the number of perfect matchings of \(G\) by \(p(G)\). Then its **geometric**, rather than just vertexwise, fixed-point space has integral homotopy type
\[
|\Delta(B_G)|^{\langle\tau\rangle}\simeq
\begin{cases}
\text{a point},&n\text{ odd},\
\bigvee^{p(G)}S^{k-1},&n=2k\text{ even}.
\end{cases}
\]
A wedge with zero summands means a point. For even \(n\), the only possibly nonzero reduced integral homology is \(\widetilde H_{k-1}\cong\mathbb Z^{p(G)}\), with the appropriate reduced degree-zero interpretation when \(k=1\).

More precisely, \(\operatorname{Aut}(G)\) acts on this integral group through the signed permutation representation on its perfect matchings: the sign is the parity of the induced reordering of the \(k\) unordered edges of a matching. This determines an actual integral lattice action, not only a rational character.

For the full square board, \(G=K_n\). Thus odd sizes have contractible geometric fixed spaces, while an even board \(n=2k\) has a wedge of \((2k-1)!!\) spheres of dimension \(k-1\). The diagonal \(S_{2k}\)-action on its top fixed-space homology is
\[
\operatorname{Ind}_{(S_2)^k\rtimes S_k}^{S_{2k}}\operatorname{sgn}_{S_k},
\]
where internal flips within the \(k\) pairs act trivially. For example, the full \(6\times6\) board has fixed-space homotopy type \(\bigvee^{15}S^2\), although its underlying ordinary chessboard complex belongs to the family known to have three-torsion.

## Assumptions and scope

All graphs are finite, simple and have at least one vertex. Every diagonal board square is present; off-diagonal squares appear in symmetric pairs corresponding exactly to graph edges. A face contains at most one rook in each row and each column. The geometric fixed-point space consists of fixed points of the **realization** of this complex; it is not the induced subcomplex on diagonal squares alone. The equivariant claim is about integral homology representations, **not** an equivariant wedge-equivalence. Here \(\widetilde H\) denotes reduced integral singular homology.

## Proof

**1. Exact fixed-point triangulation.** The transposition orbits of allowable board squares are the diagonal singletons \(\{(v,v)\}\) and the two-point off-diagonal orbits \(\{(u,v),(v,u)\}\), one for each edge \(\{u,v\}\in E\). A union of these orbits is a nonattacking rook placement if and only if their supports in \(V\), respectively \(\{v\}\) or \(\{u,v\}\), are pairwise disjoint. Within any invariant original simplex, a geometrically fixed point has equal barycentric weight at every point of each transposition orbit. Giving each orbit's barycenter its total orbit weight yields an affine simplex, and these simplices agree on intersections. Consequently the geometric fixed set is **PL-homeomorphic** to the simplicial complex
\[
L(G)=\{\mathcal F:\mathcal F\text{ is a family of pairwise disjoint nonempty subsets of }V,
\;|A|=1\text{ or }( |A|=2\text{ and }A\in E)\}.
\]
In particular, singleton subsets of \(V\) are vertices of \(L(G)\).

**2. A canonical contractible subcomplex.** For each \(v\in V\), let \(s_v\) be the vertex of \(L(G)\) corresponding to the singleton \(\{v\}\). Set
\[
U(G)=\bigcup_{v\in V}\operatorname{st}_{L(G)}(s_v).
\]
The complex \(L(G)\) is flag: a collection of vertices is a face precisely when every pair of supports is disjoint. For every nonempty \(I\subseteq V\), the intersection of the closed stars at \(\{s_v:v\in I\}\) is exactly the closed star of the face \(\{s_v:v\in I\}\). This intersection is nonempty and contractible, being a cone. Their cover nerve is therefore the entire simplex on \(V\). The simplicial nerve lemma proves \(U(G)\) contractible. This includes the one-vertex boundary case.

**3. Identify the missing faces.** A face of \(L(G)\) lies in \(U(G)\) if it either contains a singleton \(s_v\), or its selected supports omit some \(v\in V\), in which case it extends by \(s_v\). The only faces outside \(U(G)\) therefore use only two-element supports and cover every vertex of \(G\): they are exactly the perfect matchings of \(G\). There are none when \(n\) is odd, so in that case \(L(G)=U(G)\) is contractible.

When \(n=2k\), each perfect matching is a simplex of dimension \(k-1\) whose entire proper boundary lies in \(U(G)\). Distinct such maximal simplices intersect only within \(U(G)\). Thus \(L(G)\) is obtained by attaching exactly \(p(G)\) simplices of dimension \(k-1\) along maps into a contractible subcomplex. Since this is a CW subcomplex inclusion, collapse of the contractible \(U(G)\) is a homotopy equivalence, and the resulting quotient is a wedge of \(p(G)\) copies of \(S^{k-1}\). For \(k=1\), this is interpreted as a wedge of \(p(G)\) copies of \(S^0\), i.e. \(p(G)+1\) connected components; its reduced zeroth homology has rank \(p(G)\). This proves every homotopy and homology assertion.

**4. Integral action.** Every graph automorphism permutes singleton stars and hence preserves \(U(G)\). The relative simplicial chain group \(C_{k-1}(L(G),U(G);\mathbb Z)\) has as its canonical oriented basis the perfect-matching faces and no other nonzero relative groups. The reduced long exact sequence of the pair identifies it, integrally and \(\operatorname{Aut}(G)\)-equivariantly, with \(\widetilde H_{k-1}(L(G);\mathbb Z)\). When an automorphism sends a perfect matching to another, its oriented simplex acquires precisely the sign of the permutation of the \(k\) two-element support vertices. For \(G=K_{2k}\), the stabilizer of a matching is \((S_2)^k\rtimes S_k\), and this sign is trivial on \((S_2)^k\) and equals the usual sign on \(S_k\). Induction gives the stated integral permutation lattice.

## Verification

The provided dependency-free Python program `check_transpose.py` independently builds all invariant original rook faces for complete boards of orders \(1\) through \(7\), comparing them to the orbit-union complex; it reconstructs the full models through order \(8\). Binary boundary-matrix reduction gives zero reduced homology at each odd order and the predicted unique Betti ranks \(1,3,15,105\) at even orders \(2,4,6,8\), respectively.

The same program tests **1,339 labelled graph patterns**: all graphs on at most five vertices and a deterministic sample on six vertices. For each it recomputes the mod-two homology and the exact number of perfect matchings. It also checks all permutation actions on perfect-matching facets for the full-board orders \(2,4,6\), verifies cocycle composition on exhaustive or deterministic subsets of group pairs, and tests the stabilizer's internal flips and pair swaps. The recorded output is `check_output.txt`, with the terminal marker `TRANSPOSE_FIXED_GRAPH_BOARD_HOMOLOGY_AND_SYMMETRY_CHECKS_OK`.

These bounded computations corroborate the explicit all-graph proof. They do not substitute for it and do not by themselves establish integral torsion-freeness, which is established by the contractible-subcomplex quotient argument.

## Relationship to prior work

The October 27, 2026 preprint of Limonchenko and Yu establishes nonequivariant homotopy results for generalized chessboard complexes and three-torsion for ordinary square chessboard complexes in every order at least five. Its definitions, stated main results, relevant homology arguments and concluding square-case criterion do not contain this transpose-fixed geometric homotopy classification. Standard chessboard-complex connectivity and matching-complex homology results, including Björner–Lovász–Vrećica–Živaljević and Shareshian–Wachs, study the underlying complexes and do not imply a fixed-point homotopy type without additional equivariant information. The exact graph-board model here also differs from the literature on Boolean Coxeter involution complexes, which uses Coxeter-word posets rather than mutually disjoint monomer/dimer supports.

The statement follows from an explicit orbit triangulation and a contractible-star cover, not from a reinterpretation of those previously established homology ranks. It also gives a naturally compatible integral automorphism representation. An unindexed equivalent theorem under alternative 'loops', 'partial matchings' or 'symmetric rook placements' terminology cannot be ruled out by available searches.

## Limitations

The result requires all diagonal squares and a symmetric off-diagonal board. It gives a nonequivariant wedge homotopy type and an integral homology action, but does not construct an equivariant wedge decomposition. It does not determine the original chessboard complex's full \(\mathbb Z/2\)-equivariant homotopy type, restriction maps among subgroup-fixed spaces, or fixed loci for other row-column involutions. The identified novelty is conditional on accessible and searchable published literature; independent review has not been performed.

## References

1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1, first public October 27, 2026, https://arxiv.org/abs/2610.37827.
2. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard complexes and matching complexes*, Journal of the London Mathematical Society 49 (1994), 25–39, https://doi.org/10.1112/jlms/49.1.25.
3. J. Shareshian and M. L. Wachs, *Torsion in the matching complex and chessboard complex*, Advances in Mathematics 212 (2007), 525–570, https://doi.org/10.1016/j.aim.2006.10.014.
4. A. Hultman and V. Umutabazi, *Boolean complexes of involutions*, arXiv:2109.05832, a different Coxeter-poset construction, https://arxiv.org/abs/2109.05832.
