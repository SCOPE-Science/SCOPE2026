# The integral graph-metric Rips filtration and dihedral homology of the Bidiakis cube

## Finding
Let \(B\) denote the twelve-vertex Bidiakis cube, with unit graph-edge lengths, shortest-path metric \(d\), and inclusive Vietoris–Rips complex
\[K_t=\{\sigma\subseteq V(B):d(u,v)\le t\text{ for all }u,v\in\sigma\}.\]
Its complete integral homotopy filtration, stated by constant parameter intervals, is
\[
K_t\simeq\begin{cases}
\bigsqcup^{12}\{*\},&0\le t<1,\\
\bigvee^7 S^1,&1\le t<2,\\
S^2,&2\le t<3,\\
\{*\},&t\ge3.
\end{cases}
\]
Over \(\mathbb Z\), the reduced persistent groups have precisely eleven \([0,1)\) degree-zero bars, seven \([1,2)\) degree-one bars, and one \([2,3)\) degree-two bar. Unreduced homology also has one infinite degree-zero bar.

The full symmetry group \(\operatorname{Aut}(B)\cong D_4\) has generators \(r(i)=i+3\) and \(s(i)=-i\) modulo \(12\). Put \(\lambda_{a,b}(r)=a\), \(\lambda_{a,b}(s)=b\) for signs \(a,b\in\{\pm1\}\), and let \(\rho\) be its standard two-dimensional rational irreducible. At the only positive-degree stages,
\[
\widetilde H_1(K_1;\mathbb Q)\cong \lambda_{-1,-1}\oplus 2\lambda_{+1,-1}\oplus2\rho,
\qquad
\widetilde H_2(K_2;\mathbb Q)\cong\lambda_{-1,-1}.
\]
Thus the degree-two integral generator changes sign under both the quarter-rotation and the specified reflection. This distinguishes the symmetry of the emergent sphere from its nonequivariant homotopy type.

## Assumptions and scope
The graph vertices are the residues \(0,1,\ldots,11\) modulo \(12\). Its edges are \(\{i,i+1\}\), together with \(\{i,i+d_i\}\) for \(d_i=(6,4,-4)\) repeated four times, all indices modulo \(12\). Since \(-6\equiv6\pmod{12}\), this is the standard LCF notation \([-6,4,-4]^4\) for the Bidiakis cube. All Vietoris–Rips thresholds use \(d(u,v)\le t\), not a strict inequality or a doubled radius. The bar endpoints are therefore exact integer thresholds. Integral homotopy statements concern geometric realizations of finite simplicial complexes. Group decompositions in degree one are over \(\mathbb Q\); no integral irreducible-lattice splitting is claimed.

## Proof
Breadth-first search in the explicitly defined graph gives diameter exactly \(3\), and its \(18\) edges form a connected, triangle-free cubic graph. Because all graph distances are integral, the filtration only changes at \(0,1,2,3\). At \(0\) there are twelve points. At \(1\), the Rips complex is the triangle-free graph itself, hence a connected graph with first Betti number \(18-12+1=7\), homotopy equivalent to seven circles. At \(3\), every pair of vertices has distance at most \(3\); the complex is an eleven-simplex.

For the nontrivial scale \(2\), exhaustive evaluation of the diameter predicate on every nonempty bitmask from \(1\) through \(4095\) gives the face vector \((12,46,68,36,4)\), a total of \(166\) nonempty simplices. Define a deterministic partial matching: initially all nonempty faces are available; for each pivot vertex in the order \(0,1,\ldots,11\), visit available faces by increasing cardinality and then integer bitmask, and whenever both \(\sigma\) and \(\sigma\cup\{v\}\) are available with \(v\notin\sigma\), match the two and remove them. This yields exactly \(82\) disjoint codimension-one pairs, with only one critical vertex and one critical triangle. The directed Hasse diagram orients each unmatched cover downward and each matched cover upward. An exhaustive Kahn topological ordering visits all \(166\) faces and all \(460\) cover relations, proving the matching is acyclic. By Forman's discrete Morse theorem the complex is homotopy equivalent to a CW complex with exactly a point and one two-cell. Its attaching map to the point is trivial, hence \(K_2\simeq S^2\) integrally. Independent mod-two chain ranks \((11,35,32,4)\) in boundary degrees \(1\) through \(4\) corroborate the homology, but are not substituted for the homotopy proof.

Now enumerate graph automorphisms by adjacency-preserving backtracking on all twelve vertices. It returns exactly eight maps. The permutations \(r(i)=i+3\) and \(s(i)=-i\) are graph automorphisms satisfying \(r^4=s^2=1\) and \(srs=r^{-1}\), and their eight products \(r^a s^b\) are distinct, proving they form the full group. Every such map acts simplicially on every Rips stage. For a permutation \(g\), the simplicial Lefschetz number is the alternating sum of signs of induced vertex permutations on faces preserved setwise. Because \(K_1\) is connected with positive homology only in degree one, \(\operatorname{tr}(g|H_1(K_1;\mathbb Q))=1-L(g;K_1)\). Because \(K_2\simeq S^2\), \(\operatorname{tr}(g|H_2(K_2;\mathbb Q))=L(g;K_2)-1\).

In the order \((a,b)=(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)\), these traces in degrees \(1\) and \(2\) respectively are
\[
(7,-3,1,-1,-1,-3,1,-1),\qquad(1,-1,-1,1,1,-1,-1,1).
\]
Taking inner products with the four linear dihedral characters and the standard two-dimensional character gives exactly the displayed rational decomposition. For the rank-one integral \(H_2\), each automorphism acts by an integer sign, and its rational trace determines that sign. Inclusions from \(K_1\) to \(K_2\) and from \(K_2\) to \(K_3\) kill the respective positive-dimensional homology because the target groups vanish in the same degree. This determines the complete integral barcodes; no torsion can occur by the identified wedge/sphere/simplex homotopy types.

## Verification
Run `python3 verify_bidiakis_rips.py` with Python 3.9 or later, using only the standard library. `bidiakis_rips_verification.txt` records the exact expected output. The code reconstructs the graph by LCF chords, all pairwise distances, each finite simplex set, the two complete acyclic matchings, raw mod-two boundary ranks, all eight group elements, the full automorphism census, the signed Lefschetz table, character decomposition, and barcode endpoints. The last output line must be `BIDIAKIS_RIPS_EQUIVARIANT_CERTIFICATE_PASS`. Every finite claim is verified exhaustively; the mathematical implications of acyclic matching and Lefschetz theory are stated in the proof.

## Relationship to prior work
Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (first publicly posted April 3, 2011), identifies shortest-path Vietoris–Rips complexes with clique complexes of graph powers and establishes general collapse criteria, including a girth threshold and a criterion for graph squares. The Bidiakis cube has girth \(4\), below the threshold \(7\) required for his radius-two girth-collapse theorem. The general theorems do not calculate this named polyhedral graph or its full dihedral homology. The paper's six-cycle example has a two-sphere graph-square complex but is a different graph and does not supply the present twelve-vertex classification or character. Weisstein's Bidiakis cube graph entry supplies the named LCF construction, not its Rips topology.

Related calculations for other twelve-vertex cubic graphs, larger convex-polyhedral graphs, and matching complexes of the Bidiakis cube have distinct underlying graphs or distinct simplex criteria and do not imply this vertex-metric Rips filtration. The present contribution is the complete **integral** filtration and full symmetry character, not the abstract fact that a six-cycle can yield a two-sphere. Publication priority beyond inspected sources is not certified.

## Limitations
This is a fixed twelve-vertex result, not a theorem for all cubic polyhedral graphs. The rational representation decomposition at scale one is not an integral lattice decomposition. The argument determines the equivariant homology characters and ordinary homotopy types, not a \(D_4\)-equivariant homotopy equivalence to a standard sphere with a linear group action. The exact computer-exhaustive certificate is finite and reproducible; it is not an infinite-family proof. Independent external mathematical audit and exhaustive publication-priority confirmation are not provided.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first posted 2011-04-03, https://arxiv.org/abs/1104.0433 .
2. E. W. Weisstein, *Bidiakis Cube*, Wolfram MathWorld, https://mathworld.wolfram.com/BidiakisCube.html (undated entry; consulted for graph identity and LCF notation).
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem).
