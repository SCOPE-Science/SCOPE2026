# Mixed-dimensional homotopy of the ordinary three-cut complex of \(KG(6,2)\)

## Finding
Let \(G=KG(6,2)\) have the fifteen two-element subsets of \([6]=\{1,2,3,4,5,6\}\) as vertices, adjacent exactly when disjoint. Let \(X=\Delta_3(G)\) be its ordinary three-cut complex: its facets are the complements of those three-element vertex sets that induce disconnected subgraphs of \(G\). Then
\[
\boxed{X\simeq\bigvee^{10}S^9\ \vee\ \bigvee^{24}S^{10}.}
\]
Consequently \(\widetilde H_9(X;\mathbb Z)\cong\mathbb Z^{10}\), \(\widetilde H_{10}(X;\mathbb Z)\cong\mathbb Z^{24}\), and all other reduced integral homology vanishes. The complex is pure eleven-dimensional with 260 facets and is not shellable.

The proof also identifies a structural decomposition of the combinatorial Alexander dual \(K=X^\vee\), which has \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{24}\) and \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{10}\). This is the first two-subset Kneser graph with triangles; the classification concerns this particular graph and ordinary three-cuts, not every Kneser graph or the total-cut construction.

## Assumptions and scope
Everything is finite, simplicial, and integral unless a coefficient field is explicitly stated. The Alexander dual is taken relative to the entire fifteen-vertex set: \(K=\{\sigma\subseteq V(G):V(G)\setminus\sigma\notin X\}\). Since the facets of \(X\) are complements of disconnected triples, a set \(\sigma\) is in \(K\) precisely when **every** three-element subset of \(\sigma\) induces a connected graph (sets of size at most two are automatically faces).

For a partition \([6]=A\sqcup B\) into two three-element blocks, write \(U_A=\binom A2\) and \(U_B=\binom B2\), regarded as three-element subsets of the fifteen graph vertices. Define \(L_{A|B}=\partial\Delta(U_A)*\partial\Delta(U_B)\), the join of two triangular boundaries. It is an integral simplicial three-sphere with nine tetrahedra and eighteen triangles. There are precisely ten unordered partitions \(A|B\).

## Proof
**1. Exact Alexander-dual faces.** A three-element vertex set of \(G\) is connected exactly when it spans two or three edges. If it spans three, its vertices are three mutually disjoint two-subsets of \([6]\), namely a perfect matching; there are \(15\) such triangles. If it spans exactly two, the two nonadjacent end vertices intersect and have a three-element union \(A\); the middle vertex lies in \(\binom{[6]\setminus A}{2}\). This uniquely assigns the triangle to an unordered partition \(A|([6]\setminus A)\). Every \(L_{A|B}\) contains exactly eighteen such two-edge-path triangles, and the ten blocks are disjoint in their collections of triangles. Thus \(K\) has \(180+15=195\) triangles.

A four-element vertex set with every triple connected has an induced subgraph in \(G\) in which deletion of any vertex leaves a connected graph. If this induced graph contains a triangle, the fourth vertex must be adjacent to at least two triangle vertices. But any three pairwise disjoint two-subsets partition \([6]\); any fourth distinct two-subset can be disjoint from at most one of them. Hence the induced graph is triangle-free, and its vertex-deletion property forces it to be an induced four-cycle. Each such cycle has two opposite nonadjacent pairs of graph vertices. The union of each opposite pair is a three-element ground subset, and the two unions are complementary; hence every four-face occurs in exactly one \(L_{A|B}\). Conversely any choice of two vertices from each of \(U_A,U_B\) produces such a four-cycle. There are \(10\cdot\binom32^2=90\) tetrahedra.

There are no five-element faces. Otherwise each of the five four-subsets would induce a four-cycle with four graph edges. Summing their edge counts counts each graph edge three times, yielding \(5\cdot4=3e\), impossible for integer \(e\). In particular \(K\) has no larger faces. Since every pair is a face, its complete nonempty face vector by dimensions zero through three is
\[
(f_0,f_1,f_2,f_3)=(15,105,195,90),\qquad \widetilde\chi(K)=14.
\]
Moreover, the ten three-spheres \(L_{A|B}\) contain *all* tetrahedra, with pairwise disjoint sets of two-faces. The only two-faces not in those spheres are the fifteen perfect-matching triangles.

**2. Integral homology of the dual.** Because every triangle belongs to at most one \(L_{A|B}\), the simplicial boundary \(\partial_3:C_3(K;\mathbb Z)\to C_2(K;\mathbb Z)\) splits into ten disjoint matrices, one for each three-sphere. Each sphere has nine tetrahedra and \(H_3\cong\mathbb Z\), so each matrix has rank eight and kernel \(\mathbb Z\). Therefore
\[
H_3(K;\mathbb Z)\cong\mathbb Z^{10},\qquad\operatorname{rank}\partial_3=80.
\]
The image of each block boundary is primitive in its corresponding free two-chain group: in a triangulated three-sphere it equals \(\ker\partial_2\), and the kernel of a homomorphism between free abelian groups is primitive. Because the two-face supports of the blocks are disjoint, \(\operatorname{im}\partial_3\) is primitive in \(C_2(K;\mathbb Z)\). Thus \(H_2(K;\mathbb Z)\), a subgroup of the torsion-free quotient \(C_2/\operatorname{im}\partial_3\), has no torsion.

The complete one-skeleton of \(K\) is that of the fourteen-simplex. Every **missing** triangle has at most one edge in \(G\), so its three two-subsets of \([6]\) have union of size at most four. Choose a two-subset \(w\) of the complementary ground elements. It is a vertex of \(G\) adjacent to all three missing-triangle vertices. Coning the missing triangle to \(w\) gives three *present* two-simplices in \(K\), filling its boundary. Since the complete two-skeleton of a simplex is simply connected and every omitted triangle boundary is likewise null-homotopic in \(K\), \(\pi_1(K)=0\) and \(H_1(K;\mathbb Z)=0\). Connectivity is immediate from the complete one-skeleton.

Using \(\widetilde\chi(K)=14\), \(\widetilde H_3(K)=\mathbb Z^{10}\), and \(\widetilde H_1(K)=0\), one obtains \(\widetilde H_2(K)=\mathbb Z^{24}\). There is no homology above degree three or below degree two.

**3. Alexander duality and homotopy type.** Integral combinatorial Alexander duality for a complex on fifteen vertices says
\[
\widetilde H_i(X;\mathbb Z)\cong\widetilde H^{12-i}(K;\mathbb Z).
\]
The computed integral homology of \(K\) is free, so universal coefficients give the two nonzero homology groups of \(X\) exactly as stated. Since \(K\) has no face of size five, every subset of at most ten vertices belongs to \(X\): its complement contains a disconnected triple. Hence \(X\) contains the complete nine-skeleton of the fourteen-simplex and is eight-connected.

The Hurewicz map \(\pi_9(X)\to H_9(X;\mathbb Z)\) is an isomorphism. The next Hurewicz map \(\pi_{10}(X)\to H_{10}(X;\mathbb Z)\) is surjective by the Whitehead exact sequence for an eight-connected CW complex. Choose maps of ten nine-spheres and twenty-four ten-spheres representing integral homology bases. Their wedge induces an integral homology isomorphism to \(X\). Both spaces are simply connected, so the homological Whitehead theorem makes this map a homotopy equivalence. This proves the displayed integral wedge decomposition without extrapolating from finite-field ranks.

Finally, every facet of \(X\) has twelve vertices, so it is pure eleven-dimensional. Its nonzero homology in degrees nine and ten precludes shellability of a pure eleven-dimensional complex.

## Verification
Run `python3 verify.py` using Python 3 and no third-party packages. It checks all \(2^{15}=32768\) vertex subsets against the disconnected-triple rule; independently enumerates connected triples; identifies the ten partition-block joins and the fifteen perfect-matching triangles; checks that every missing triangle admits the required three-triangle cone; verifies the full nine-skeleton of \(X\); and performs exact modular elimination of the complete simplicial boundary matrices in characteristics two, three, five and seven. Each characteristic gives dual boundary ranks \((14,91,80)\) in degrees one through three, corroborating integral Betti ranks \((1,0,24,10)\) by the independent structural proof.

The script's field calculations are corroborative; the torsion-freeness, infinite-homotopy-group steps, and integral sphere-wedge conclusion follow from the explicit structural argument above, not from modular sampling. `verify_output.txt` contains the recorded complete verifier output, ending in `VERIFY_OK`.

## Relationship to prior work
Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue [1] introduce ordinary cut complexes and classify several graph families. Their Corollary 6.6 treats the **two-cut** complexes of triangle-free Kneser graphs \(K(m,r)\) with \(m<3r\); here \(m=6=3r\), the first triangle-bearing case, and the parameter is three. Their Theorem 6.1 requires a complete next-to-top skeleton, whereas \(X\) has missing ten-faces corresponding to the ninety tetrahedra of \(K\). Their other listed graph-family theorems do not determine this complex.

Nilakantan and Singh [2] compute the **open neighborhood** complex of Kneser graphs, obtaining nineteen two-spheres for this graph. The 2025 treatment of induced independent-set graphs [3] concerns neighborhood and total-cut constructions. Those are different complexes; neither a common underlying graph nor a shared use of Alexander duality implies the new result. Two previously recorded calculations on the same graph concern the scale-two intrinsic Čech complex [4] and the rational character of the open-neighborhood complex [5], respectively, rather than this ordinary three-cut complex. Their full result statements were inspected and compared on definitions, face predicates, and dimensions.

The 2025 cut-complex realizability and reconstruction study [6] establishes general recognition and uniqueness results, not these homology or homotopy groups. Exact searches for the graph under its two-subset-disjointness aliases and for the proposed two-dimensional sphere wedge did not identify a prior theorem implying the claim. An unindexed equivalent calculation cannot be categorically excluded.

## Limitations
The classification is for the **single** first triangle-bearing two-subset Kneser graph, not for all \(KG(n,2)\), higher cut parameters, or equivariant homotopy actions. The dual's ten sphere blocks intersect along vertices and edges; the claim does not assert an equivariant decomposition of those intersections. No independent external audit has been performed. Novelty is relative to the specifically inspected sources and searches, and a previously unindexed equivalent result remains possible.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, first public 2023-04-26; Sections 6 and 7, especially Theorem 6.1 and Corollary 6.6.

[2] N. Nilakantan, A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(KG_{2,k}\)*, arXiv:1802.05848v1, 2018-02-16, Theorem 1.3.

[3] Y. Shen, Z. Song, F. Yu, W. Zhou, J. Zhuang, *Neighborhood Complexes of Induced \(k\)-Independent Graphs*, arXiv:2512.09674v1, 2025-12-10.

[4] *The scale-two Čech complex of \(KG(6,2)\): 64 spheres and a multiplicity-free \(S_6\)-character*, public mathematical-record identifier `a413c6a778e4`.

[5] *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, public mathematical-record identifier `6890383e239b`.

[6] Y. Shen, Z. Song, F. Yu, W. Zhou, J. Zhuang, *Realizations and Uniqueness of Cut Complexes of Graphs*, arXiv:2512.12933v1, 2025-12-15.
