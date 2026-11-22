# Integral sphere-wedge topology of toroidal ordinary four-cut complexes

## Finding
For each integer \(n\ge6\), let \(G_n=C_4\mathbin{\square}C_n\) be the Cartesian product of the four-cycle and the \(n\)-cycle, with \(N=4n\) vertices. Let \(\Delta_4(G_n)\) be the **ordinary four-cut complex**: its facets are the complements of disconnected induced four-vertex sets. Its combinatorial Alexander dual \(K_n=\Delta_4(G_n)^\vee\), on the full \(N\)-vertex set, has the integral homotopy type
\[
K_n\simeq \bigvee^{\binom{4n-1}{3}-70n}S^2\ \vee\ \bigvee^{3n}S^3.
\]
Consequently the original ordinary four-cut complex has full reduced integral homology
\[
\widetilde H_j(\Delta_4(G_n);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{3n},&j=4n-6,\\
\mathbb Z^{\binom{4n-1}{3}-70n},&j=4n-5,\\
0,&\text{otherwise}.
\end{cases}
\]
It is pure of dimension \(4n-5\) and not shellable. For \(n=6\), the two nonzero ranks are \(18\) and \(1351\), respectively. All statements concern ordinary, not total, cut complexes; the wedge equivalence concerns the Alexander dual, not the original cut complex.

## Assumptions and scope
Here \(C_m\) denotes the simple cycle graph on \(m\) vertices. We label vertices of \(G_n\) as \((a,b)\in\mathbb Z/4\mathbb Z\times\mathbb Z/n\mathbb Z\); adjacent vertices differ by one in exactly one coordinate. For a finite complex \(\Delta\) on \(V\), its Alexander dual is \(\Delta^\vee=\{F\subseteq V:V\setminus F\notin\Delta\}\). Homotopy equivalences and homology groups are integral. An elementary simplicial collapse removes a free face and its unique maximal coface. The lower bound \(n\ge6\) ensures that the graph has exactly the coordinate four-cycles and four-cycle fibers, without additional length-five periodic identifications in the local certificate.

## Proof
**1. Faces of the Alexander dual.** A subset \(F\) lies in \(K_n\) exactly when *every* four-element subset of \(F\) induces a connected graph. Hence its complete two-skeleton is present. There is no five-element face: any induced five-vertex bipartite graph all of whose four-vertex deletions remain connected has minimum degree at least two. Such a graph contains \(K_{2,3}\) as a subgraph (a bipartition of sizes two and three is forced, together with all six cross edges). But any two vertices in the Cartesian product share at most two common neighbors; therefore \(G_n\) is \(K_{2,3}\)-free. Thus \(K_n\) is three-dimensional, with tetrahedra exactly the connected induced four-sets.

**2. Exact face count.** Since \(G_n\) is triangle-free and 4-regular, a connected induced four-vertex subgraph is an induced three-star, a four-vertex path or a four-cycle. Their counts are, respectively, \(16n\), \(52n\) and \(5n\). For the path count, the \(4n\) possible starts have \(4\cdot3\cdot3\) oriented nonbacktracking three-step walks each, so there are \(72n\) unoriented paths before removing \(4\) paths from each of the \(5n\) four-cycles. Thus the face vector is
\[
(f_0,f_1,f_2,f_3)=\left(4n,\binom{4n}{2},\binom{4n}{3},73n\right).
\]
The four-cycles are the \(4n\) coordinate squares plus the \(n\) four-cycle fibers.

**3. The local eight-vertex cube.** Let \(B\) be the three-dimensional simplicial complex on vertices of the graph \(Q_3=C_4\square K_2\), with complete two-skeleton and one tetrahedron for each connected induced four-set. It has \(8\) vertices, \(56\) triangles and \(38\) tetrahedra. The signed tetrahedral boundary matrix has exact rational rank \(35\) and contains a \(35\)-by-\(35\) integer minor of determinant \(-1\). A specific list of its rows and columns, with lexicographic simplex ordering, and a dependency-free exact computation occur in `verify.py`. Therefore its image is a primitive rank-\(35\) sublattice of the \(35\)-rank two-cycle group of the full two-skeleton. Its integral homology is \(\widetilde H_3(B)=\mathbb Z^3\) and zero otherwise; it is simply connected. A simply connected three-complex with free homology concentrated in degree three is homotopy equivalent to \(\bigvee^3S^3\).

**4. Glue cube blocks in a circle.** For each \(b\in\mathbb Z/n\mathbb Z\), let \(B_b\) be the restriction of \(K_n\) to the eight vertices of columns \(b,b+1\), and put \(Y=\bigcup_bB_b\). Every \(B_b\) is a copy of \(B\). Neighboring blocks intersect in the full three-simplex on their common column; nonneighboring blocks are disjoint and triple intersections are empty. Their intersection nerve is a cycle, and the shared simplices are contractible. Gluing simply connected wedge-of-three-spheres blocks along this cyclic pattern gives
\[
Y\simeq S^1\vee\bigvee^{3n}S^3,
\quad H_2(Y;\mathbb Z)=0,\quad H_3(Y;\mathbb Z)=\mathbb Z^{3n}.
\]
There are \(37n\) tetrahedra in \(Y\): the \(38n\) cube-block tetrahedra have precisely \(n\) duplicated column-fiber tetrahedra. Therefore \(K_n\) has exactly \(36n\) tetrahedra outside \(Y\).

**5. A cyclic elementary-collapse certificate.** The accompanying verifier includes exactly \(36\) ordered pairs of four-vertex and three-vertex coordinate templates, named `PATS`. Each pair is translated by all \(n\) cyclic column shifts. At each stage the translated three-faces are distinct, lie in no cube block, and each is contained in precisely its paired tetrahedron among the tetrahedra that still remain. The pairs may therefore be removed by elementary collapses. After all \(36n\) moves, precisely the \(37n\) tetrahedra of \(Y\) remain. Exhaustive exact checks establish these assertions for every \(6\le n\le13\).

For \(n\ge13\), these checks also establish the **unbounded parameter claim**, by locality: each connected four-vertex set is contained in at most four consecutive columns and every possible coface of a chosen triangle belongs to such a local four-vertex set. All incidences relevant to a template's being free, and all possible coincidences of translated templates, consequently occur within a window of at most seven consecutive columns. No such window acquires a new periodic identification after cycle length thirteen; its incidence data are exactly those checked for length thirteen. Hence the same ordered \(36n\) collapses are valid for every larger cycle, not merely those enumerated. Let \(K'_n\) be the remaining complex. It contains the whole subcomplex \(Y\), has no three-faces outside \(Y\), and was obtained from \(Y\) by attaching only cells of dimension at most two.

**6. Integral homology and homotopy.** The relative cellular chains of \((K'_n,Y)\) vanish in dimensions three and above. The long exact sequence gives
\[
H_3(K'_n;\mathbb Z)\cong H_3(Y;\mathbb Z)=\mathbb Z^{3n},
\]
and injects \(H_2(K'_n;\mathbb Z)\) into the free group \(H_2(K'_n,Y;\mathbb Z)\). Thus \(H_2(K'_n;\mathbb Z)\) is torsion-free. Because the original \(K_n\) contains the full two-skeleton of a simplex, it is simply connected, as is the collapsed \(K'_n\). The face count gives
\[
\widetilde\chi(K_n)=\binom{4n-1}{3}-73n.
\]
With \(H_1=0\) and the rank of \(H_3\) above, the rank of \(H_2\) is exactly \(\binom{4n-1}{3}-70n\). A simply connected three-dimensional CW complex with these free integral homology groups is homotopy equivalent to the stated wedge of two- and three-spheres: choose homotopy classes mapping to bases of \(H_2\) and \(H_3\), use the simply connected Hurewicz/Whitehead exact sequences to obtain sphere maps, then apply the homology version of Whitehead's theorem.

**7. Return by Alexander duality.** Combinatorial Alexander duality on the \(4n\) vertices gives \(\widetilde H_j(\Delta_4(G_n);\mathbb Z)\cong\widetilde H^{4n-j-3}(K_n;\mathbb Z)\). Since the dual homology is free, the universal coefficient theorem gives the displayed groups in degrees \(4n-6\) and \(4n-5\). Every original facet has \(4n-4\) vertices, so the original complex is pure of dimension \(4n-5\). Its nonzero next-to-top homology obstructs shellability.

## Verification
Execute `python3 verify.py` using the standard Python 3 library. Its lexicographically ordered cube boundary matrix has size \(56\)-by-\(38\), exact rational rank \(35\), binary rank \(35\) and the specified integral minor determinant \(-1\). The program reconstructs the graph and all connected induced four-sets independently for each \(6\le n\le13\), checks the exact \(73n\) tetrahedron count, confirms \(37n\) belong to cube blocks, and verifies every free-face incidence of the \(36n\) collapses in its actual current simplicial complex. It checks that every removed triangle lies outside the entire cube-block union. The emitted `TOROIDAL_FOUR_CUT_VERIFIED` line signals that all executable checks succeeded. These finite checks certify the local identities; the all-parameter result depends on the explicit locality proof in Step 5.

## Relationship to prior work
Bayer et al. introduced and studied ordinary cut complexes [1]; their sequel [2] treats path-grid and squared-path complexes, not this four-cut cyclic product. The closest published square-cylinder result [3] computes only an exact next-to-top rank for \(C_4\square P_m\), with an open boundary, and does not establish the closed-torus wedge decomposition or its additional top-degree homology. The published periodic-grid calculations [4,5] concern **three-cut** complexes, whose Alexander dual admits connected triples rather than the connected four-sets here. The general four-cut girth-at-least-five sphere-wedge theorem [6] cannot apply to the present graph, which has many four-cycles. Our conclusion does not follow by merely replacing a path by a cycle in the square-cylinder result: the cyclic block intersection creates an extra fundamental loop before the nonlocal two-cells attach, and the complete homotopy statement requires an integral cyclic collapse.

## Limitations
The statement starts at \(n=6\): no claim is made for the shorter periodic cases, other cycle widths, total cut complexes, equivariant representations, or the homotopy type of the *original* cut complex. The certificate establishes the parameter-uniform local collapse through a finite window argument, not by treating finite computations as an infinite proof. Novelty has been checked against identified primary papers and published records; an uncatalogued equivalent theorem is possible. Independent mathematical validation has not been performed.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public version 2023-04-26), https://arxiv.org/abs/2304.13675.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public version 2024-07-11), https://arxiv.org/abs/2407.08158.

[3] *Exact next-to-top homology of four-cut complexes of square cylinders*, public mathematical record `4f68bb556153`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-next-to-top-homology-of-four-cut-complexes-of-square-cylin--4f68bb556153.

[4] *Toroidal three-cut complexes retain an integral fundamental-surface class*, public mathematical record `4a74053b5bd8`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-toroidal-three-cut-complexes-retain-an-integral-fundamental-surf--4a74053b5bd8.

[5] *A signed integral sphere lattice at the four-cycle boundary of toroidal three-cut complexes*, public mathematical record `4d5dde862e76`, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-signed-integral-sphere-lattice-at-the-four-cycle-boundary-of-t--4d5dde862e76.

[6] *Homotopy classification of four-cut complexes at the pentagonal girth boundary*, public mathematical record `94b36fd5471f`, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-homotopy-classification-of-four-cut-complexes-at-the-pentagonal--94b36fd5471f.
