# An integral dihedral lifting obstruction for the rank-four whirl

## Finding
Let \(K\) be the independence complex of the rank-four wheel matroid and let \(L\) be the independence complex of its rank-four whirl relaxation. The inclusion adds exactly one three-simplex, the four-rim-edge facet \(R\). For the canonical dihedral action \(G=D_4\) on the wheel, let \(\lambda:G\to\{\pm1\}\) be the orientation sign on the four rim edges. The resulting short exact sequence
\[
0\longrightarrow\widetilde H_3(K;\mathbb Z)\longrightarrow\widetilde H_3(L;\mathbb Z)\overset{\pi}{\longrightarrow}\mathbb Z_\lambda\longrightarrow0
\]
has **exact equivariant lifting index two**:
\[
\pi\bigl(\{z\in\widetilde H_3(L;\mathbb Z):g z=\lambda(g)z\ \forall g\in G\}\bigr)=2\mathbb Z.
\]
It is therefore non-split over the integers, though split over the rationals. The ordinary reduced integral homology is top-dimensional only, with ranks 14 for \(K\) and 15 for \(L\). These ranks are not the novelty claim.

## Assumptions and scope
Construct a five-vertex wheel with rim vertices \(0,1,2,3\) and hub vertex \(4\). Number its graph edges \(r_i=i\), joining vertex \(i\) to \(i+1\pmod4\), and \(s_i=4+i\), joining vertex \(i\) to the hub. Edge subsets of the wheel matroid are independent precisely when they are graph forests. The whirl changes only the set of independent four-element subsets by adding \(R=\{0,1,2,3\}\). Both associated simplicial complexes have dimension three. Their \(D_4\) action comes from \(i\mapsto a+\epsilon i\pmod4\) on rim vertices for \(a\in\mathbb Z/4\), \(\epsilon\in\{\pm1\}\); this permutes rim and spoke edges consistently. All chain orientations below use increasing edge labels.

The homology map \(\pi\) is the integer coefficient of the oriented facet \([0,1,2,3]\). Its target carries \(\lambda(g)=\operatorname{sgn}(g\vert_R)\). All statements concern this indicated eight-element dihedral subgroup, not an unverified assertion about the full matroid automorphism group.

## Proof
**1. Exactness and integral homology.** The pair \((L,K)\) has one relative three-cell and no other relative cells. It gives a long exact sequence whose relevant portion is
\[
0\to\widetilde H_3(K;\mathbb Z)\to\widetilde H_3(L;\mathbb Z)\overset{\pi}{\to}\mathbb Z_\lambda\to\widetilde H_2(K;\mathbb Z).
\]
Independence complexes of rank-four matroids are shellable and are wedges of three-spheres, so the last group vanishes. Enumeration of the wheel-independent faces yields cardinalities \((1,8,28,52,45)\), including the empty face. Adding the rim facet changes the last count to 46, giving top reduced homology ranks 14 and 15. This observation proves exactness, not equivariant splitting.

**2. Every equivariant lift has even coefficient.** Let \(\rho\in D_4\) be the reflection of rim vertices \(i\mapsto1-i\pmod4\). It fixes the rim edges \(r_0,r_2\), exchanges \(r_1,r_3\), and pairs all four spoke edges into two orbits. Consequently \(\lambda(\rho)=-1\). Let \(\sigma=R\setminus\{r_0\}=\{r_1,r_2,r_3\}\). The induced action of \(\rho\) on the orientation of \(\sigma\) is also \(-1\). For a chain \(z\) with \(\rho z=-z\), the contributions to the coefficient of \(\sigma\) in \(\partial z\) from the four cofaces \(\sigma\cup\{s_i\}\) occur in equal signed pairs; their sum is even. The only other coface of \(\sigma\) in \(L\) is \(R\). Writing its coefficient as \(a\), the vanishing of \(\partial z\) gives \(a\equiv0\pmod2\). This applies to all \(\lambda\)-equivariant three-cycles.

**3. An equivariant cycle with coefficient minus two.** For each four-element face \(F\) having a consistent \(\lambda\)-signed dihedral orbit, let \(\mathcal O(F)\) be the integer chain whose coefficient at the increasing orientation of \(gF\) is \(\lambda(g)\) times the sorting sign of the ordered edge list \(gF\). This is well-defined precisely when all stabilizers satisfy the compatibility condition. Set
\[
\begin{aligned}
Z={}&-2\mathcal O(0123)+\mathcal O(0124)+\mathcal O(0147)\\
&-\mathcal O(0246)+\mathcal O(0467).
\end{aligned}
\]
Here each four-digit string denotes a subset of edge labels, not an integer. The signed orbits in this formula have sizes \(1,8,8,4,8\). Direct expansion has 29 distinct supported oriented facets, satisfies \(\partial Z=0\) integrally, is \(\lambda\)-equivariant under all eight group elements, and has rim coefficient \(-2\). The accompanying standalone verifier rebuilds the graph, lists all faces and signed orbits, and checks these identities using exact integer arithmetic. Thus \(2\mathbb Z\) is achieved and the parity bound is sharp.

**4. Nonsplitting.** An integral module section of \(\pi\) must map the orientation generator of \(\mathbb Z_\lambda\) to a \(\lambda\)-equivariant class having coefficient one, which step 2 excludes. Over \(\mathbb Q\), equivariant averaging of an ordinary section over the finite group produces a section, so the extension is rationally split.

## Verification
Run the standalone file `VERIFY.py` with Python 3; no third-party modules are required. It enumerates the wheel's independent faces, checks that the relaxed face is the only new top facet, constructs the eight graph automorphisms, forms the five signed orbit chains with the displayed coefficients, checks the exact signed boundary and all group actions, and verifies that the relevant reflection pairs all four completing spokes. The independent parity argument and the explicit cycle are both needed for the exact index conclusion. Recorded output is supplied as `VERIFY_OUTPUT.txt`.

## Relationship to prior work
Wheel and whirl matroids and the relaxation operation are classical; the structural 2012 Strong Splitter Theorem treats them as exceptional 3-connected matroids. Lu–Xie–Yang (2018) calculate the wheel and whirl Kazhdan–Lusztig and \(Z\)-polynomials, which do not determine the integral equivariant splitting class here. Moci–Pezzoli (2020) give general complex-coefficient equivariant homology correspondences for matroids; complex representations do not resolve this integral extension. Denham–Schulze–Walther (2021, Example 2.26) supply an explicit wheel/whirl description in their study of configuration hypersurfaces, not the stated integral signed rim-facet lift. The exact index-two obstruction is the claim being distinguished from these sources.

## Limitations
The proved index is for the rank-four wheel-to-whirl inclusion and its specified dihedral subgroup. The calculation does not establish an all-rank parity theorem, determine the full automorphism representation, or provide independent peer verification. Search cannot exclude uncatalogued equivalent results. The result is about integral equivariant homology, not about matroid Kazhdan–Lusztig or \(Z\)-polynomials.

## References
- S. R. Kingan and M. Lemos, *Strong Splitter Theorem*, first arXiv version dated 2012-01-21, arXiv:1201.4427.
- L. Lu, M. H. Y. Xie and A. L. B. Yang, *Kazhdan-Lusztig polynomials of fan matroids, wheel matroids and whirl matroids*, 2018-02-11, arXiv:1802.03711, especially Sections 4.3 and 6.3.
- L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, 2020-01-11, arXiv:2001.03760, particularly Section 4.
- G. Denham, M. Schulze and U. Walther, *Matroid connectivity and singularities of configuration hypersurfaces*, 2021, DOI:10.1007/s11005-020-01352-3, especially Example 2.26.
