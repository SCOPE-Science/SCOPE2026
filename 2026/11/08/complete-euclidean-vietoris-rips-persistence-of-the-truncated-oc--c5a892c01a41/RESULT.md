# Complete Euclidean Vietoris–Rips persistence of the truncated-octahedral vertex set

## Finding

Let \(P\subset\mathbb R^3\) be the 24 vertices of a regular truncated octahedron, in the normalization
\[
P=\{(x_1,x_2,x_3): (|x_1|,|x_2|,|x_3|)\text{ is a permutation of }(0,1,2)\}.
\]
Write \(K_r=\operatorname{VR}_{\le r}(P)\) for the **inclusive ambient-Euclidean** Vietoris–Rips complex, with all vertices present from scale zero. For every real \(r\ge0\), the complete integral homotopy classification is
\[
K_r\simeq
\begin{cases}
\bigvee^{23}S^0,&0\le r<\sqrt2,\\
\bigvee^{13}S^1,&\sqrt2\le r<2,\\
\bigvee^{7}S^1,&2\le r<\sqrt6,\\
\bigvee^{9}S^2,&\sqrt6\le r<2\sqrt2,\\
S^2,&2\sqrt2\le r<4,\\
\bigvee^{5}S^4\vee\bigvee^{2}S^5,&4\le r<3\sqrt2,\\
S^{11},&3\sqrt2\le r<2\sqrt5,\\
\ast,&r\ge2\sqrt5.
\end{cases}
\]
Here \(\bigvee^{23}S^0\) denotes a discrete set of 24 points. Although separate simplicial changes occur at the intermediate Euclidean distances \(\sqrt{10}\), \(2\sqrt3\) and \(\sqrt{14}\), they induce no additional homology births/deaths. A single fixed geometric triangulation \(S\) of the truncated-octahedral boundary is contained in the complex from \(r=\sqrt6\) onwards, and **each** complex at squared scales \(8,10,12,14\) simplicially collapses onto this same \(S\).

More precisely, the complete nonzero persistent homology intervals over \(\mathbb Z\) are: one degree-zero \([0,\infty)\) interval; 23 additional degree-zero \([0,\sqrt2)\) intervals; six degree-one \([\sqrt2,2)\) and seven degree-one \([\sqrt2,\sqrt6)\) intervals; eight degree-two \([\sqrt6,2\sqrt2)\) and one degree-two \([\sqrt6,4)\) interval; five degree-four and two degree-five \([4,3\sqrt2)\) intervals; and one degree-eleven \([3\sqrt2,2\sqrt5)\) interval. No other intervals occur. Thus the six square faces cause six of the 13 original circle classes to die at Euclidean distance 2, strictly before the remaining seven die at \(\sqrt6\).

## Assumptions and scope

Distance means ordinary Euclidean chord distance in \(\mathbb R^3\), **not** graph shortest-path distance along the truncated octahedron. A subset is a simplex exactly when every pair of its vertices is at distance at most the stated \(r\). All homotopy equivalences and homology are integral. The classification includes threshold equality (left-closed intervals). The persistent interval assertion concerns the inclusion maps among the complexes, not just individual Betti numbers.

The ten positive squared Euclidean pair distances and their unordered-pair multiplicities are
\[
(2,36),(4,12),(6,48),(8,24),(10,24),(12,24),(14,48),(16,12),(18,36),(20,12).
\]
Let \(T\) denote the three-regular 36-edge graph of nearest-neighbor pairs (squared distance two). Computing shortest-path distances in \(T\) gives the exact correspondence
\[
\begin{array}{c|c}
\text{distance in }T & \text{allowed squared Euclidean shells at that distance}\\\hline
1&2\\2&4,6\\3&8,10,12\\4&14,16\\5&18\\6&20.
\end{array}
\]
In particular, Euclidean Rips complexes at squared scales \(2,6,12,16,18,20\) coincide **as labeled simplicial complexes** with the graph-metric Rips complexes at integer scales \(1,2,3,4,5,6\), respectively.

## Proof

**1. Nearest neighbors and the first Euclidean subdivision.** The nearest-neighbor graph \(T\) is connected, with 24 vertices and 36 edges, giving \(K_{\sqrt2}\simeq\bigvee^{13}S^1\). At squared threshold four, exactly twelve new edges appear: the two diagonals of each of six mutually vertex-disjoint square faces. Every square four-tuple spans a tetrahedron, and no other new triangles or tetrahedra appear. Consequently this stage is the original graph with six tetrahedra glued along the six four-edge square boundaries (including their diagonals). Within each tetrahedron, elementary collapses remove the tetrahedron, its interior triangles and diagonals, leaving a three-edge tree in place of that square. The resulting connected graph has 24 vertices and 30 edges, hence first Betti number seven and homotopy type \(\bigvee^7S^1\). The explicit complete 24-pair elementary-collapse certificate appears in `collapse_pairs.json` and is verified in `verify.py`.

Every newly introduced diagonal at threshold four is homotopic within its tetrahedron to a two-edge path in the original square boundary. Therefore the inclusion-induced map on first integral homology from the squared-two to the squared-four stage is surjective, with free kernel of rank six. At squared threshold six, first homology is zero.

**2. Geometry of the surviving two-sphere.** The six planar square faces are the sections \(x_i=\pm2\), and the eight regular hexagonal faces are the sections \(\epsilon_1x_1+\epsilon_2x_2+\epsilon_3x_3=3\), with \(\epsilon_i\in\{-1,1\}\). Triangulate each square by two triangles along a diagonal. For each cyclically ordered hexagon \((v_0,\ldots,v_5)\), use the central triangle \((v_0,v_2,v_4)\) and the three triangles \((v_0,v_1,v_2)\), \((v_2,v_3,v_4)\), \((v_4,v_5,v_0)\). This yields a geometric triangulation \(S\) of the boundary, with face vector \((24,66,44)\). It is homeomorphic to \(S^2\). Every edge of these triangles has squared length at most six, so \(S\subseteq K_{\sqrt6}\).

For each squared threshold \(t\in\{8,10,12,14\}\), the entire \(K_{\sqrt t}\) **simplicially collapses onto the same subcomplex \(S\)**. The respective numbers of verified elementary collapse pairs are \(212,452,812,5740\). Each sequence consists of faces \(\sigma\subset\tau\) with \(\dim\tau=\dim\sigma+1\), where \(\sigma\) has exactly one remaining coface, namely maximal \(\tau\). All pairs, in deletion order, are encoded by vertex-subset masks in `collapse_pairs.json`. The standalone program `verify.py` constructs each complex and checks every deletion and the exact final remainder. Thus the inclusion maps between the squared-eight, -ten, -twelve and -fourteen stages induce isomorphisms in every integral homology degree, via the shared generator \([S]\).

**3. Endpoints supplied by the known graph-metric calculation.** A published complete graph-metric calculation for this same truncated-octahedral graph establishes
\[
\operatorname{VR}^{\rm graph}_{\le2}(T)\simeq\bigvee^9S^2,
\qquad
\operatorname{VR}^{\rm graph}_{\le4}(T)\simeq\bigvee^5S^4\vee\bigvee^2S^5.
\]
By the exact distance-shell correspondence in the preceding section, these are exactly the Euclidean complexes at squared thresholds six and sixteen. This previously established homotopy information is used **as a cited theorem**, not asserted here to be a new homotopy classification or independently reproved by the included program. The included code does independently check the labeled metric coincidence and all nonzero mod-two homology ranks at these stages.

At squared threshold eighteen, the only absent edges are the twelve antipodal pairs \(\{v,-v\}\). Their complement-clique complex is the join of twelve copies of \(S^0\), hence \(S^{11}\). At squared threshold twenty all pairs are edges, so the complex is a simplex.

**4. Persistence maps.** The graph argument in step 1 gives the surjection \(\mathbb Z^{13}\twoheadrightarrow\mathbb Z^7\) at squared threshold four, with free kernel \(\mathbb Z^6\). By the cited graph-metric theorem, the squared-six stage has \(H_2\cong\mathbb Z^9\), and its first homology has vanished. Because \(S\subseteq K_{\sqrt6}\) and the squared-eight complex collapses onto \(S\), the image of \(H_2(K_{\sqrt6};\mathbb Z)\to H_2(K_{2\sqrt2};\mathbb Z)\cong\mathbb Z\) includes the generator \([S]\), so this map is a split surjection of rank one with free kernel rank eight. The common surface retract makes all subsequent degree-two maps through squared threshold fourteen isomorphisms. Its image vanishes at squared threshold sixteen, where the target has \(H_2=0\). At the remaining transitions all positive-degree homology lies in distinct dimensions, so the stated bars follow. Surjections between these free abelian groups split, yielding the claimed integral interval decomposition.

## Verification

The files `verify.py`, `collapse_pairs.json` and `verification_output.txt` are an independently runnable exact certificate for **the new Euclidean assertions**. Run `python3 verify.py` with all three files in the same directory. Standard-library integer operations suffice; no floating-point comparison, package installation or third-party executable is needed. The verifier reconstructs all 24 integer-coordinate vertices, 276 pair distances and the graph-metric shell partition, enumerates the face vectors at every squared threshold through sixteen, constructs the 44-triangle polyhedral surface, checks its containment already at squared threshold six, replays all 24+212+452+812+5740 elementary-collapse pairs, and checks full mod-two boundary ranks at the eight enumerated stages. It also verifies the antipodal description at squared threshold eighteen. The expected final line is `VERIFY_OK`.

The computer proof is finite because it enumerates the complete 24-vertex complexes at every relevant intermediate scale and validates each local elementary collapse. The cited graph-metric theorem provides the separately established integral mixed-sphere endpoint; the modular rank checks alone are **not** substituted for that theorem.

## Relationship to prior work

Saleh, Titz Mite and Witzel, *Vietoris–Rips complexes of Platonic solids* (2023 first public version), provides the motivating geometric classification problem, specifically identifying Archimedean solids as an extension; its theorem covers the five Platonic solids, not the truncated octahedron. The closest direct previous result, *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph* (2026), fully determines the **intrinsic graph shortest-path metric** for this same 24-vertex set. It already gives the homotopy types at squared Euclidean thresholds \(2,6,12,16,18,20\) through the exact shell equivalence. These covered homotopy endpoints are expressly **not new claims**.

The new content is the **ambient-Euclidean** continuous-scale filtration: the distinct six-square and remaining-seven-circle deaths at distances \(2\) and \(\sqrt6\), the exact stable polyhedral-surface retract throughout the Euclidean squared-distance shells \(8,10,12,14\), and the complete inclusion-induced integral persistence barcode. The graph-metric theorem cannot imply the intermediate \(7\)-circle stage or these same-surface collapse maps without additional geometric work. The four-letter permutahedral result indexed in the mathematical records uses adjacent-swap distance, and a separate permutahedral Rips approximation paper studies lattice-based approximations rather than the exact finite orbit filtration here. No inspected prior theorem or exact table implies the complete new Euclidean statement.

## Limitations

The theorem is specific to this 24-point integer-coordinate realization, up to similarity, and uses ambient Euclidean chord distance; it does not assert a corresponding classification for other Archimedean solids, all permutahedra, arbitrary deformations or the spherical/geodesic metric. The quoted graph-metric theorem is an external mathematical premise for the squared-six and squared-sixteen integral wedge claims. The verifier supplies complete new elementary-collapse certificates and independent mod-two corroboration but does not re-establish that earlier theorem's integral Morse boundary. Unindexed or inaccessible equivalent Euclidean computations remain an originality risk; no independent audit of this new result has yet been performed.

## References

1. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28, primary MSC 55N31. https://arxiv.org/abs/2302.14388
2. *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph*, publicly indexed 2026-10-11, full result and verification available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8
3. A. Choudhary, M. Kerber and S. Raghvendra, *Polynomial-Sized Topological Approximations Using the Permutahedron*, first public arXiv:1601.02732, https://arxiv.org/abs/1601.02732, published in *Discrete & Computational Geometry* (2019).
