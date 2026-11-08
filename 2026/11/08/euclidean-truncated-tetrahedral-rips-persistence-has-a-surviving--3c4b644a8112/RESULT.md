# Euclidean truncated-tetrahedral Rips persistence has a surviving orientation line

## Finding
Let \(P\) be the twelve vertices of a **regular unit-edge truncated tetrahedron** in \(\mathbb R^3\), with **Euclidean chordal distance**, and let \(K_r=\operatorname{VR}_{\le r}(P)\) be the inclusive Vietoris–Rips complex. Its complete integral homotopy sequence is
\[
K_r\simeq\begin{cases}
\text{twelve isolated points},&0\le r<1,\\
\bigvee^3 S^1,&1\le r<\sqrt3,\\
\bigvee^5 S^2,&\sqrt3\le r<2,\\
S^2,&2\le r<\sqrt5,\\
\ast,&r\ge\sqrt5.
\end{cases}
\]
The degree-two map induced by inclusion \(K_{\sqrt3}\hookrightarrow K_2\) is a **split surjection over \(\mathbb Z\)**: a fourteen-triangle integral cycle maps to a primitive generator of \(H_2(K_2;\mathbb Z)\).

Moreover the full tetrahedral symmetry group \(G\cong S_4\) acts on the *reduced rational persistent homology* as follows. Let \(V_{\mathrm{std}}\) denote the standard three-dimensional rational representation, \(\varepsilon\) the permutation-sign representation, and \(\mathbb Q[4]\) the permutation module on four tetrahedral labels. Writing \(U\otimes\mathbf I_{[a,b)}\) for the constant \(G\)-module \(U\) on the indicated half-open persistence interval, with identity structure maps inside and zero outside, the complete positive-degree barcode is
\[
\begin{aligned}
\widetilde H_1(K_\bullet;\mathbb Q)&\cong (\varepsilon\otimes V_{\mathrm{std}})\otimes\mathbf I_{[1,\sqrt3)},\\
\widetilde H_2(K_\bullet;\mathbb Q)&\cong\mathbb Q[4]\otimes\mathbf I_{[\sqrt3,2)}\;\oplus\;\varepsilon\otimes\mathbf I_{[\sqrt3,\sqrt5)}.
\end{aligned}
\]
The reduced degree-zero barcode is the augmentation module on the twelve ordered pairs of distinct tetrahedral labels, supported on \([0,1)\); all other degrees vanish. Thus four of the five sphere classes die at Euclidean scale \(2\), but the orientation-sign class persists until \(\sqrt5\).

## Assumptions and scope
Choose the four original tetrahedral vertices
\[
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)).
\]
Index the twelve truncated vertices by ordered pairs \((a,b)\) with \(a\ne b\in\{0,1,2,3\}\) and set
\[
p_{a,b}=\frac{2A_a+A_b}{\sqrt8}.
\]
The truncation is uniform, and all 18 polyhedral edges have Euclidean length one. The group \(S_4\) permutes the original tetrahedral labels and acts isometrically on this configuration. A simplex belongs to \(K_r\) exactly when every pairwise Euclidean distance is at most \(r\); no factor-of-two radius convention is used. The assertion concerns vertex-point clouds, not the polyhedral surface or intrinsic graph distances.

## Proof
**Distance shells and small stages.** The squared distances between distinct \(p_{a,b}\) are exactly \(1,3,4,5\), with pair counts \(18,24,12,12\), respectively. Consequently there are exactly four positive thresholds, and the complexes are constant between them. The stage at \(r=1\) has face vector \((12,18,4)\); its four triangles are the four truncation triangles. Each has a free edge, so removing four edge–triangle pairs leaves a connected graph with 12 vertices and 14 edges, homotopy equivalent to \(\bigvee^3S^1\).

**The five-sphere stage.** At \(r=\sqrt3\), direct exact face generation gives face vector \((12,42,48,12)\). A deterministic maximal-face elimination, defined and completely checked in the accompanying verifier, matches 54 adjacent-dimensional face pairs and leaves exactly one critical vertex and five critical two-simplices. A topological sort of every directed incidence in the reversed matching Hasse diagram verifies acyclicity (276 incidences). Forman's discrete Morse theorem gives a CW model consisting of one zero-cell and five two-cells, each attached to the point: \(K_{\sqrt3}\simeq\bigvee^5S^2\), integrally. These facts are a finite certificate, not extrapolation from samples.

**The intermediate Euclidean sphere.** At \(r=2\), the twelve missing edges are exactly the pairs at squared distance \(5\). Their graph is the disjoint union of three four-cycles, indexed by the coordinate in which a vertex has absolute unnormalized coordinate \(3\). Accordingly,
\[
K_2=\operatorname{Ind}(C_4\sqcup C_4\sqcup C_4)
=\operatorname{Ind}(C_4)*\operatorname{Ind}(C_4)*\operatorname{Ind}(C_4).
\]
Each \(\operatorname{Ind}(C_4)\) consists of two disjoint edges and retracts simplicially onto two points. Therefore the triple join is homotopy equivalent to \(S^0*S^0*S^0\cong S^2\). At \(r=\sqrt5\) the complex is the full eleven-simplex and contractible.

**A primitive persistent class.** Number the ordered pairs lexicographically, beginning with \((0,1),(0,2),(0,3),(1,0),\dots\). The following oriented integer two-chain, with \([i,j,k]\) denoting the oriented simplex on increasing vertex indices, is supported in \(K_{\sqrt3}\):
\[
\begin{aligned}
z={}&-[0,1,3]+[0,1,6]-[0,2,6]+[0,2,9]\\
&-[0,3,5]-[0,5,9]+[1,3,7]-[1,6,7]\\
&+[2,6,11]-[2,9,11]+[3,5,7]-[5,7,11]\\
&+[5,9,11]+[6,7,11].
\end{aligned}
\]
An integral boundary calculation gives \(\partial z=0\). Retract \(K_2\) to the octahedral two-sphere by sending each vertex to the sign of its unique coordinate of absolute value \(3\), on one of the three coordinate axes. In the image of \(z\), the coefficient of the oriented \((+x,+y,+z)\) facet is exactly \(+1\). A two-cycle on the octahedral sphere has this coefficient equal to its degree. Thus the inclusion sends \([z]\) to a *primitive generator*; the integral map is split surjective. Rationally its rank is one, so four two-dimensional bars die at \(2\), and one continues to \(\sqrt5\).

**Symmetry and equivariant bars.** For a permutation \(g\in S_4\), let \(f(g)\) count fixed original tetrahedral labels and let \(\varepsilon(g)\) be its sign. An exhaustive *signed* simplicial Lefschetz count over all 24 symmetries gives traces
\[
\begin{array}{c|c}
\text{homology group}&\text{trace of }g\\\hline
\widetilde H_1(K_1;\mathbb Q)&\varepsilon(g)(f(g)-1)\\
\widetilde H_2(K_{\sqrt3};\mathbb Q)&f(g)+\varepsilon(g)\\
\widetilde H_2(K_2;\mathbb Q)&\varepsilon(g).
\end{array}
\]
All other reduced homology at these stages vanishes, so the Lefschetz counts determine the indicated characters. Since rational representations of a finite group are semisimple, character equality identifies the first group as \(\varepsilon\otimes V_{\mathrm{std}}\), the second as \(\mathbb Q[4]\oplus\varepsilon\), and the third as \(\varepsilon\). The orientation action on the octahedral join also directly gives \(\varepsilon\): permuting three axes contributes the sign of the axis permutation, while the product of the three axis-sign changes is \(+1\). Because the inclusion is equivariant and surjective, it restricts to an isomorphism on the unique sign summand; its kernel is \(\mathbb Q[4]\). This proves the asserted rational equivariant barcode, including the interstage map.

## Verification
The standalone verifier `verify_euclid_tt.py` uses only Python's standard library. It regenerates all 66 exact squared distances, all simplices, the 54-pair matching, all 276 Hasse incidences and their directed acyclicity, the three complementary four-cycles, the integral boundary of \(z\), the primitive degree-one image, and all 24 signed Lefschetz formulas at three scales. An independent mod-two filtered boundary reduction returns eleven finite degree-zero bars \([0,1)\), three degree-one bars \([1,\sqrt3)\), four degree-two bars \([\sqrt3,2)\), and one degree-two bar \([\sqrt3,\sqrt5)\). This modular computation is corroboration; the integral homotopy and primitive map follow from the explicit Morse, join and chain arguments above.

## Relationship to prior work
Saleh, Titz Mite and Witzel (2023, 2024) classify the Vietoris–Rips complexes of the *five Platonic solids* and explicitly identify Archimedean solids as a direction for extension. Their theorem does not include truncated tetrahedra. Saleh's 2023 dissertation studies those Platonic cases and samples of general spherical point clouds, but its inspected contents and Archimedean discussion do not supply the present exact tetrahedral filtration.

A published mathematical record titled *The graph-metric Rips filtration of the truncated tetrahedron* establishes the same twelve-point **intrinsic graph-distance** stages at integer thresholds \(1,2,3\). This accounts for the three circles and five two-spheres, but it does **not** cover the Euclidean chordal threshold \(2\), its two-sphere, the primitive transition map, or the sign line persisting to \(\sqrt5\). A separate record on the same graph gives the full rational \(S_4\)-representation at the two intrinsic stages; those isolated representation formulas are also **not** claimed new. The separate Euclidean cuboctahedron record concerns a different Archimedean vertex configuration and different distance shells. The new statement is the full *Euclidean* interval decomposition and its persistent symmetry refinement.

## Limitations
This result applies to the canonical exact regular truncated tetrahedron of edge length one, with Euclidean chordal distance and inclusive thresholds. It makes no claims for deformed tetrahedra, surface-geodesic distances, other Archimedean solids, integer-coefficient equivariant persistence splittings, or Borel equivariant cohomology. The originality assessment compares the most relevant accessible published material and indexing aliases; unidentified equivalent calculations remain possible. No independent external review has been performed.

## References
1. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), DOI 10.2140/iig.2024.21.17. https://arxiv.org/pdf/2302.14388
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral dissertation (2023), DOI 10.22029/jlupub-17950. https://jlupub.ub.uni-giessen.de/items/0a69b981-1372-4ab7-9e75-03b44faa5f67
3. *The graph-metric Rips filtration of the truncated tetrahedron*, publicly accessible mathematical research record (2026), identifier 51e8cc219376.
4. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, publicly accessible mathematical research record (2026), identifier c10ad684de7e.
