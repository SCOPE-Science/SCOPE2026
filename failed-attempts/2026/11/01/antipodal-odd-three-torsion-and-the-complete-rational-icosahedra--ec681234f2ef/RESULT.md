# Antipodal-odd three-torsion and the complete rational icosahedral action on matching-complex homology

## Finding
Let \(I\) be the undirected graph of the regular icosahedron, with twelve vertices and thirty edges. Its **ordinary matching complex** \(X=\mathcal M(I)\) has one simplex for every set of pairwise vertex-disjoint edges of \(I\). The full simplicial automorphism action induced by graph symmetries is the action of \(G=\operatorname{Aut}(I)\cong A_5\times C_2\). Write \(z\) for central antipodal inversion, and let \(\varepsilon(z)=-1\) be the sign character of the second factor.

Put \(V_4\) and \(V_5\) for the four- and five-dimensional rational irreducible representations of \(A_5\), and let \(V_6\) denote the six-dimensional rational representation whose extension to \(\mathbb C\) is the sum of the two conjugate three-dimensional irreducibles. The **complete equivariant homology determination** is
\[
\boxed{\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong {}&
(2V_4\oplus4V_5\oplus2V_6)\boxtimes\mathbf1\\
&\oplus(2V_4\oplus2V_5\oplus V_6)\boxtimes\varepsilon,\\
\operatorname{Tor}\widetilde H_3(X;\mathbb Z)\cong {}&
(\mathbb Z/3)\boxtimes\varepsilon.
\end{aligned}}
\]
Here \(A_5\) acts trivially on the integral torsion group, while antipodal inversion acts by multiplication by \(-1\) (that is, by \(2\pmod3\)). In particular, antipodal inversion splits rational third homology into eigenspaces of dimensions \(40\) and \(24\), has trace \(16\), and the entire rotation group fixes no nonzero rational third-homology class. All other reduced rational homology vanishes.

The underlying nonequivariant integral group \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{64}\oplus\mathbb Z/3\) and the corresponding Moore-space wedge homotopy classification were previously determined; **they are context, not new results here**. The new result is the action of all 120 symmetries, including the nontrivial action on integral three-torsion.

## Assumptions and scope
Use the canonical twelve-vertex icosahedral graph, characterized by its regular planar triangulation with five neighbors at every vertex. For reproducibility the program calls `networkx.icosahedral_graph()`, sorts its thirty unordered endpoint pairs lexicographically and identifies a matching with a thirty-bit integer. The program regenerates all \(5888\) augmented simplices and all graph automorphisms; no stored face or group table is supplied.

The graph has exactly 120 automorphisms. Orientation-preserving automorphisms form the rotation group \(A_5\), with conjugacy classes of sizes \(1,15,20,12,12\) and rotation orders \(1,2,3,5,5\); orientation reversal is multiplication by the central antipodal involution. The program determines each automorphism's orientation by checking the cyclic neighbor orders in a planar embedding at **all twelve vertices**. The rational decomposition is over \(\mathbb Q\); the torsion statement is as an integral \(G\)-module. No integral lattice classification of the free rank-64 summand is claimed.

## Proof
**1. A complete reduced Morse model.** Recursively enumerate the face set by adding an edge only when it shares no endpoint with already chosen edges. A sequential matching on the augmented face poset processes the lexicographically sorted graph edges in the deterministic order obtained from Python's `random.Random(209).shuffle` on the list of edge indices. At each stage pair every currently unused face missing the current edge with its extension by that edge whenever both faces remain unused. This is a well-defined acyclic matching: the supplied checker **orients every codimension-one incidence** upwards on matched pairs and downwards otherwise, and topologically sorts the entire augmented Hasse digraph. There are \(2889\) matched pairs and precisely \(87\) critical three-simplices and \(23\) critical four-simplices, with no other critical faces in the augmented model.

For a simplex represented by an increasing edge-index list, the simplicial boundary uses the alternating signs in that order. Eliminate each paired lower three-simplex through the signed boundary of its paired upper four-simplex, following its acyclic gradient-path recursion. The resulting exact integral Morse boundary \(B\colon\mathbb Z^{23}\to\mathbb Z^{87}\) is fully reconstructed by the checker. Its Smith factors are \(22\) units and one factor \(3\). Independently, the checker selects \(23\) rows of \(B\) and checks that the associated integer determinant has absolute value \(3\), while \(\operatorname{rank}_{\mathbb F_3}B=22\). These facts give the claimed Smith form and, in particular, \(\widetilde H_3(X;\mathbb Z)=\mathbb Z^{64}\oplus\mathbb Z/3\), \(\widetilde H_4(X;\mathbb Z)=0\), and no reduced rational homology outside degree three. This nonequivariant calculation is independently reproduced as a prerequisite to the equivariant assertion, not offered as the novel claim.

**2. Exact rational character.** Every graph automorphism permutes the thirty vertices of \(X\) (the edges of \(I\)). If an augmented face \(F\) is preserved setwise, the induced signed simplex permutation contributes \((-1)^{|F|-1}\operatorname{sgn}(g|_F)\) to its augmented Lefschetz number. Thus
\[
\operatorname{tr}\bigl(g\mid\widetilde H_3(X;\mathbb Q)\bigr)
=-\sum_{F\in X}(-1)^{|F|-1}\operatorname{sgn}(g|_F)
\quad\text{(only invariant faces contribute)}.
\]
The empty face contributes \(-1\). Summing over the entire actual face set gives, for the four distinct **rotation-order** groups \(1,2,3,5\), the character values \((64,0,-2,-1)\). For the antipodal multiples of these rotations, the values are \((16,0,-2,1)\). The two conjugacy classes of order-five rotations each give the same listed value; the program checks all 120 individual automorphisms, not only representatives. The exact integer sums imply the even and odd characters, respectively,
\[
(40,0,-2,0,0),\qquad (24,0,0,-1,-1)
\]
on the five conjugacy classes of \(A_5\). Taking the ordinary character inner products with \(V_4\), \(V_5\) and the rational \(V_6\) (the latter counting each complex three-dimensional constituent once) yields \((2,4,2)\) and \((2,2,1)\), establishing the displayed rational decomposition. The trivial character occurs with multiplicity zero.

**3. Exact integral torsion action.** The Morse matrix has a one-dimensional right kernel modulo three and no integral kernel. Choose the unique generator of this mod-three kernel normalized by setting its first free coordinate to one. The checker lifts it to an **actual mod-three simplicial four-cycle** by recursively correcting its boundary along all paired three-to-four gradient arrows in topological order; the resulting cycle has \(1009\) nonzero simplex coefficients. The correction's boundary is checked to vanish on *every* three-simplex modulo three. A separate reduction of original four-chains to critical four-cells along paired four-to-five arrows defines a chain map in degree four; the checker verifies the commuting boundary identity on **every one of the 1482 four-simplices**. Consequently this projection detects the unique line \(\widetilde H_4(X;\mathbb F_3)\cong\mathbb F_3\).

Apply each of the 120 actual induced signed edge permutations to the lifted four-cycle, project, and compare the resulting vector with the normalized kernel generator. All sixty orientation-preserving symmetries act by \(+1\) on that line; all sixty orientation-reversing ones act by \(-1\). The natural universal coefficient isomorphism
\[
\widetilde H_4(X;\mathbb F_3)
\cong \operatorname{Tor}(\widetilde H_3(X;\mathbb Z),\mathbb F_3)
\]
is valid because \(\widetilde H_4(X;\mathbb Z)=0\). It respects graph automorphisms. The action on the unique integral \(\mathbb Z/3\) torsion summand is therefore trivial on \(A_5\) and negative under antipodal inversion, as claimed.

## Verification
Run `python3 verify_equivariant_icosahedron.py` with `networkx` and `sympy` installed. The program regenerates graph, faces, matching, entire Hasse orientation, Morse matrix, an integer minor of determinant \(-3\), all 120 automorphisms, signed Lefschetz characters, the mod-three four-cycle, chain-map checks and its full symmetry action. Exact integer and finite-field operations are used throughout; no stochastic numerical approximation is used. The only pseudorandom operation is a fixed-seed permutation specifying the matching. The exact successful output is embedded as `verification_output.txt`.

The character calculation uses the entire face set and is independent of Morse gradient paths, while the torsion calculation uses a separate explicitly lifted cycle and verifies chain-map commutation. These are complementary computations, not independent external certification.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *General polygonal line tilings and their matching complexes* (first public 2022-11-22), develop ordinary matching-complex topology for polygonal chains. Their theorem does not encompass the icosahedral graph and does not compute its symmetry action. Mondal, Mukherjee and Saha, *Topology of matching complexes of complete graphs via discrete Morse theory* (first public 2023-05-04), study complete graphs and give related Morse methods, but no icosahedral representation.

The most pertinent published previous exact calculation, *Three-torsion in the icosahedral matching complex: a planar counterexample* (public 2026-10-11), establishes the nonequivariant homotopy equivalence \(\mathcal M(I)\simeq(\bigvee^{64}S^3)\vee M(\mathbb Z/3,3)\). Its `RESULT.md` was compared directly. A nonequivariant wedge decomposition does not determine the homology action of \(A_5\times C_2\); the complete rational character and orientation-sign action on the integral order-three summand are the substantive additions here. Published icosahedral neighborhood- and distance-complex symmetry calculations concern different simplicial complexes, not \(\mathcal M(I)\).

## Limitations
This is an exact finite graph-specific result. It does not characterize the integral free rank-64 \(\mathbb Z[A_5\times C_2]\)-lattice, equivariant homotopy type, or arbitrary matching complexes. The full icosahedral group is used as the graph automorphism group, and the torsion action is computed on the characteristic torsion subgroup of ordinary third homology. The computational proof relies on standard discrete Morse chain-equivalence and the naturality of the universal coefficient theorem. An equivalent equivariant computation in unindexed literature remains possible; no independent audit is represented.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first public 2022-11-22, https://arxiv.org/abs/2211.12559 .
2. A. Mondal, S. Mukherjee, K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, first public 2023-05-04, https://arxiv.org/abs/2305.02973 .
3. *Three-torsion in the icosahedral matching complex: a planar counterexample*, published 2026-10-11, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a/RESULT.md .
4. *2020 Mathematics Subject Classification*, 55N91 (equivariant homology and cohomology), https://mathscinet.ams.org/mathscinet/msc/msc2020.html .
