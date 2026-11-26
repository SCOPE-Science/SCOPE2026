# Index-two obstruction among shortest induced spheres in the Petersen matching complex

## Finding
Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent exactly when their subsets are disjoint. Let \(K=\mathcal M(P)\) be its **ordinary matching complex**, whose vertices are the fifteen graph edges and whose faces are collections of pairwise endpoint-disjoint graph edges.

The **minimum number of vertices of an induced subcomplex carrying a nonzero class into** \(\widetilde H_2(K;\mathbb Z)\) is six. Exactly **110** six-vertex restrictions have this property; every such restriction is an octahedral two-sphere
\[
K[W]\cong (S^0)^{*3}\cong S^2.
\]
Every one of their oriented fundamental cycles maps to a nonzero **primitive** integral homology class.

Under the natural action of \(S_5\), the 110 spheres form three orbits of sizes **10, 60, 40**. Their fundamental classes span sublattices \(L_{10},L_{60},L_{40}\) of the ambient integral group, and
\[
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^5,\qquad
[\widetilde H_2(K;\mathbb Z):L_{10}]=2,\qquad
L_{60}=L_{40}=\widetilde H_2(K;\mathbb Z).
\]
In particular, the smallest, most symmetric orbit spans rationally but **misses an index-two integral class**, even though each of its individual cycles is primitive. Either of the other two orbits independently generates all integral degree-two homology.

## Assumptions and scope
All homology is reduced simplicial homology over \(\mathbb Z\) unless another ring is specified. An induced subcomplex \(K[W]\) is the restriction of \(K\) to a subset \(W\) of its graph-edge vertices; its homology class is measured by the map induced by the inclusion into \(K\). The orbit-generated lattice is the image in ambient homology of the integer span of all oriented fundamental classes of the orbit. Orientation sign changes do not affect the lattice.

Use lexicographic order on the ten two-subsets of \(\{0,1,2,3,4\}\); form and lexicographically order the fifteen disjoint pairs of these graph vertices as graph edges \(e_0,\ldots,e_{14}\). Orient every matching simplex by increasing graph-edge indices. This fixes all signed boundary matrices and the reproducibility certificate.

The classification is for this single Petersen graph and the ordinary matching complex. The known ambient mixed-dimensional homotopy type is **background**, not part of the claimed novelty.

## Proof
**1. Sharp minimum for flag complexes.** Every matching complex is flag. The following standard inductive support argument is supplied for completeness. Let a flag complex \(Y\) contain an induced subcomplex with nonzero reduced homology in degree \(d\ge0\), and choose an inclusion-minimal vertex subset \(W\) supporting such a class. For \(d=0\), minimal disconnected restrictions have two nonadjacent vertices. For \(d\ge1\), at any vertex \(v\in W\), deletion \(Y[W\setminus\{v\}]\) has zero reduced degree-\(d\) homology. The deletion–link long exact sequence thus forces the link of \(v\) in \(Y[W]\) to have nonzero reduced degree-\((d-1)\) homology. Inductively there are at least \(2d\) link vertices, while \(v\) has a nonneighbor since otherwise \(Y[W]\) would be a cone. Consequently \(|W|\ge2d+2\). In the equality case every vertex has exactly one nonneighbor; otherwise its link cannot have the necessary \(2d\) vertices. Hence the complement of the induced one-skeleton is a perfect matching and, because \(Y\) is flag, \(Y[W]=(S^0)^{*(d+1)}\). For \(d=2\), at least six vertices are required, with equality forcing an octahedral sphere.

**2. Exact classification and orbit structure.** Two vertices of \(K\) are nonadjacent precisely when their underlying graph edges share an endpoint. Therefore six vertices induce an octahedron if and only if the six underlying graph edges break into three incident pairs, with no incidence between different pairs. These are three vertex-disjoint length-two paths in \(P\), using nine of its ten graph vertices. Exhaustively inspect the \(\binom{15}{6}=5005\) six-edge subsets, retaining exactly those whose three incident pairs partition the six chosen edges. Exactly 110 subsets remain. Under the 120 permutations of the five symbols, they split into orbits of cardinalities \(10,60,40\).

The orbit distinction has a graph-theoretic interpretation. Let \(u\) be the unique omitted Petersen vertex and let \(c_1,c_2,c_3\) be the three path centers. Count centers adjacent to \(u\). It is identically **3** on the size-10 orbit, **1** on the size-60 orbit, and **0** on the size-40 orbit. For each of the ten choices of \(u\) there are respectively **1, 6, 4** decompositions of these types. This also identifies the orbits intrinsically, not just by computer-generated labels.

**3. Canonical integral sphere cycles.** For each retained six-edge support, sort its three incident edge pairs \((a_i,b_i)\) lexicographically with \(a_i<b_i\). Define
\[
z_W=(e_{a_1}-e_{b_1})*(e_{a_2}-e_{b_2})*(e_{a_3}-e_{b_3}),
\]
where the star denotes the oriented join of degree-zero chains, with the usual permutation sign when the selected vertex indices are sorted. Expansion gives eight triangles with coefficients \(\pm1\). Since every elementary difference has zero reduced boundary, the oriented join is a cycle; the bundled verifier checks every signed boundary exactly. Each \(z_W\) represents the fundamental cycle of its induced octahedral sphere.

**4. Integral chain calculations.** Enumeration of all matchings gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(15,75,145,90,6).
\]
Let \(B_2:C_2\to C_1\) and \(B_3:C_3\to C_2\) be their signed integer simplicial boundary matrices. Independent exact modular elimination gives \(\operatorname{rank}(B_2)=61\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_{101}\). The one-skeleton of \(K\) is connected: for any two graph edges sharing a vertex there is a third edge disjoint from both, yielding a two-step path in the one-skeleton. Hence \(\operatorname{rank}(\partial_1)=14\), so \(\operatorname{rank}_{\mathbb Q} B_2\le75-14=61\). The modular lower bound gives equality over \(\mathbb Q\).

Exact Smith reduction over \(\mathbb Z\) of \(B_3\), a \(145\)-by-\(90\) matrix, has **79 nonzero invariant factors, all equal to one**. Therefore \(\operatorname{im} B_3\) is primitive in \(C_2\), and
\[
\widetilde H_2(K;\mathbb Z)=\ker B_2/\operatorname{im} B_3\cong\mathbb Z^{145-61-79}=\mathbb Z^5.
\]
For one representative of each of the three \(S_5\)-orbits, the augmented matrix \([B_3\mid z_W]\) has rank 80 with **only unit Smith invariant factors**. Thus each representative maps to a primitive nonzero homology class. All 110 classes share that property by graph automorphisms.

**5. Precise index-two obstruction.** Augment \(B_3\) with the 10, 60, or 40 columns \(z_W\) in a given orbit. All three augmented matrices have rank 84. Their exact Smith invariant-factor multisets are, respectively,
\[
\begin{array}{c|c}
\text{sphere-orbit size}&\text{nonzero invariant factors}\hline
10&\underbrace{1,\ldots,1}_{83},2\\
60&\underbrace{1,\ldots,1}_{84}\\
40&\underbrace{1,\ldots,1}_{84}
\end{array}
\]
The image \(B_2(C_2)\) is a free rank-61 group. There is an exact sequence
\[
0\longrightarrow \widetilde H_2(K;\mathbb Z)/L_{\mathcal O}
\longrightarrow C_2/(\operatorname{im}B_3+\langle z_W:W\in\mathcal O\rangle)
\xrightarrow{B_2}\operatorname{im}B_2\longrightarrow0.
\]
Since the middle term has free rank 61, its torsion subgroup equals the left-hand finite group. The displayed Smith factors give \(\mathbb Z/2\) for the size-10 orbit and the zero group for each of the other two. This proves the claimed indices and integral generation. Adding all 110 sphere columns also yields 84 unit invariant factors.

## Verification
`verify.py` is a standalone exact enumeration and signed-chain checker, requiring Python and `sympy==1.14.0` from `requirements.txt`. Run `python3 verify.py`. It generates the Petersen graph as a two-subset Kneser graph, all matchings, all 5005 candidate six-edge subsets, all 110 induced octahedra and their signed eight-triangle cycles, and all 120 permutations of the ground set. It checks the full three-orbit classification, the omitted-vertex adjacency invariant, each cycle boundary, all modular ranks, and complete exact integral Smith forms for the original and orbit-augmented degree-three boundaries. It ends with `VERIFY_OK_PETERSEN_SHORTEST_110_OCTAHEDRAL_CARRIERS_10_60_40_INDEX_2_1_1`.

The finite computations are exhaustive for the graph and do not purport to establish a theorem over arbitrary graph families. The proof of the six-vertex minimum is independent of enumeration; exact Smith matrices, not logs or numerical tolerance, establish the integral indices.

## Relationship to prior work
Shareshian and Wachs [1] develop integral matching-complex homology and torsion for complete and complete-bipartite graphs; their general framework motivates integral lattice questions but does not determine the Petersen graph's induced sphere carriers. Barmak [2, Section 5] proves connectivity bounds for independence complexes of claw-free graphs, applying to matching complexes through line graphs; these do not determine local integral spanning indices. Bayer, Goeckner and Jelić Milutinović [3, Sections 2–3] classify matching complexes that themselves are low-dimensional manifolds and identify \(3P_3\) as a graph whose matching complex is an octahedral two-sphere. That explains the local sphere type but does not enumerate its embeddings into the Petersen matching complex or calculate their ambient homology classes.

Two earlier published Petersen-specific computations [4, 5] prove the ambient homotopy type \(\bigvee^5S^2\vee\bigvee^5S^3\). Those entire result texts, including statements of scope and verification, were compared: neither claims to enumerate shortest induced spheres, classify their symmetry orbits, or calculate orbitwise integral indices. In particular, the ambient Betti number five alone **does not imply** the index-two obstruction. Related published calculations of the \(S_5\)-action on the rational homology determine its rational character, not the integral saturation of these three geometrically defined orbit lattices. An unnoticed equivalent description in unindexed literature remains possible.

## Limitations
The index values are intrinsic to the specified orbit-generated lattices in integral degree-two homology; they do not imply a homotopy decomposition, a shortest-chain norm, a classification of all non-induced cycles, or an all-graphs theorem. The precise support size is measured in vertices of the matching complex, not vertices of the original graph. The included Smith computations require `sympy==1.14.0` but use exact integer arithmetic only. Re-running a supplied verifier is not an independent scientific audit, and exhaustive prior-literature uniqueness is not asserted.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, first public 2004-09-03, https://arxiv.org/html/math/0409054v1.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/html/1007.0418v1.
3. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, https://arxiv.org/abs/1906.03328, especially Sections 2–3.
4. *The Petersen matching complex is a wedge of five two-spheres and five three-spheres*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-a-wedge-of-five-two-spheres-and--80050a324367/RESULT.md.
5. *The Petersen matching complex is a wedge of five two-spheres and five three-spheres* (alternate verification), publicly accessible mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-bigvee-5-s-2-vee-bigvee-5-s-3--439d72b660a6/RESULT.md.
