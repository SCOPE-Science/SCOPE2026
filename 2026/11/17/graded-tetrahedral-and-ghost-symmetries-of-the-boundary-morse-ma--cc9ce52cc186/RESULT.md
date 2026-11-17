# Graded tetrahedral and ghost symmetries of the boundary Morse-matching complex

## Finding
Write \(B=\mathcal M(\partial\Delta^3)\) for the **ordinary (non-pure)** complex of acyclic Hasse matchings on the nonempty proper faces of the tetrahedron. Vertex relabeling and the incidence-complement involution induce an action of \(G=S_4\times C_2\). Let \(\gamma\) denote the nontrivial element of the second factor. Then the only nonzero reduced rational homology representations, \(\widetilde H_3(B;\mathbb Q)\) and \(\widetilde H_4(B;\mathbb Q)\), have the following **complete graded characters**. Columns correspond to the cycle types of \(\sigma\in S_4\):

| Group element and degree | \(1^4\) | \(2\,1^2\) | \(2^2\) | \(3\,1\) | \(4\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(\chi_3(\sigma,1)\) | 21 | -3 | 1 | 0 | -1 |
| \(\chi_3(\sigma,\gamma)\) | 9 | 1 | -3 | 0 | -1 |
| \(\chi_4(\sigma,1)\) | 24 | -2 | 0 | 0 | -2 |
| \(\chi_4(\sigma,\gamma)\) | 0 | -2 | 0 | 0 | 2 |

Let \(S^\lambda\) be the rational Specht representation of \(S_4\), and let \(E_\pm\) be the two characters of the ghost factor. The multiplicities of \(S^\lambda\boxtimes E_+\) and \(S^\lambda\boxtimes E_-\), respectively, are:

| \(\lambda\) | degree 3: \((+, -)\) | degree 4: \((+, -)\) |
| --- | --- | --- |
| \((4)\) | \((0,0)\) | \((0,0)\) |
| \((3,1)\) | \((2,0)\) | \((1,2)\) |
| \((2,2)\) | \((1,1)\) | \((1,1)\) |
| \((2,1,1)\) | \((2,1)\) | \((2,1)\) |
| \((1,1,1,1)\) | \((1,1)\) | \((1,1)\) |

In particular, the ghost-even and ghost-odd dimensions are \((15,6)\) in degree three and \((12,12)\) in degree four. Neither homology representation contains the trivial \(G\)-character, so the **geometric** quotient \(|B|/G\) has vanishing positive-degree reduced rational homology. The quotient by the tetrahedral rotation group \(A_4\), in contrast, has rational reduced Betti number two in **each** of degrees three and four. The quotient by \(A_4\times\langle\gamma\rangle\) retains one rational generator in **each** of these degrees.

## Assumptions and scope
Here \(\partial\Delta^3\) consists of the fourteen nonempty proper subsets of \(V=\{0,1,2,3\}\). The twenty-four vertices of \(B\) are cover incidences \((a,b)\) with \(a\subset b\) and \(|b|=|a|+1\). A set of incidences is a simplex precisely when no two share an endpoint and reversing the selected cover arrows in the face-poset Hasse digraph leaves it acyclic. There are 4,332 nonempty simplices with face counts in dimensions zero through five equal to \((24,216,896,1692,1248,256)\).

The natural \(S_4\) permutes each vertex label. The *ghost* acts on incidence vertices by \(\gamma(a,b)=(V\setminus b,V\setminus a)\). It preserves inclusion and acyclicity, commutes with relabeling and satisfies \(\gamma^2=1\). There are no other reduced rational homology degrees: the already-established nonequivariant homotopy type is \(B\simeq\bigvee^{21}S^3\vee\bigvee^{24}S^4\) [1]. All quotient assertions use singular homology with rational coefficients of the **geometric quotient** rather than simplicial orbits or group cohomology.

## Proof
**1. Complete chain model and published premise.** Enumerate all subsets of the twenty-four cover incidences, retaining exactly the endpoint-disjoint selections whose reversed Hasse digraph is acyclic. The resulting dimension counts are as displayed above. With all simplex vertices ordered by incidence index, define the oriented simplicial differential by \(\partial[v_0,\ldots,v_q]=\sum_{j=0}^q(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_q]\). The known integral homotopy classification [1] implies that over \(\mathbb Q\) the ranks of the differentials in degrees five, four and three are respectively \(256,968,703\), with other reduced rational homology zero. The standalone program constructs all corresponding matrices from this definition and independently checks ranks \(256,968\) for the degree-five and degree-four boundaries modulo each of the distinct primes 1009 and 10007, and \(703\) for the degree-three boundary in the invariant calculation at the identity.

**2. Exact invariant dimensions.** For a group element \(g\in G\), partition the oriented simplices of each degree into \(g\)-orbits. A cyclic orbit contributes one invariant chain exactly when the orientation sign accumulated around it is positive; then a canonical invariant generator is the signed orbit sum. Its boundary is computed term by term, producing an explicit matrix for the differential between fixed chain spaces. Write \(c_q(g)\) for the number of such generators and \(r_q(g)\) for the rank of \(\partial_q\) on them. The homology fixed-space dimensions are
\[
\dim H_3(B;\mathbb Q)^{\langle g\rangle}=c_3(g)-r_3(g)-r_4(g),\qquad
\dim H_4(B;\mathbb Q)^{\langle g\rangle}=c_4(g)-r_4(g)-c_5(g).
\]
The last identity uses the **injectivity** of \(\partial_5\) from the known homology and complete chain ranks, which remains injective upon restriction to invariant chains. To certify the ranks exactly rather than merely infer rational values from modular experiments, note that \(g\) has order dividing six **or is of order four**; in either case its order is coprime to both chosen primes. Localization at either prime makes averaging over \(\langle g\rangle\) an integral idempotent, so invariant chains and their complements are direct summands preserved by the differential. Reduction modulo the prime cannot increase ranks, and the computed **full** boundary ranks modulo either prime equal their known rational ranks. Therefore no direct-summand rank can drop in reduction, and the computed invariant-boundary ranks equal their rational ranks. This argument applies to every power of every group element. The computations are finite and exhaustive over the ten conjugacy classes and their powers.

**3. Recover traces from fixed dimensions.** Let \(m=\operatorname{ord}(g)\) and \(a_d=\dim H_q(B;\mathbb Q)^{\langle g^d\rangle}\) for \(d\mid m\). The eigenvalue multiplicities are recovered over characteristic zero by the cyclotomic decomposition. For example, for \(m=2\), \(\operatorname{tr}(g)=2a_1-a_2\); for \(m=3\), \(\operatorname{tr}(g)=(3a_1-a_3)/2\); for \(m=4\), \(\operatorname{tr}(g)=2a_1-a_2\); and for \(m=6\), setting \(u=a_1\), \(v=a_2-a_1\), \(w=(a_3-a_1)/2\), and \(z=(a_6-u-v-2w)/2\), one has \(\operatorname{tr}(g)=u-v-w+z\). The expressions for orders two and four share a form but differ in the meaning of \(a_2\); at order two \(a_2=\dim H_q\). Applying these formulas to the finite invariant-rank tables computed by `tetra_boundary_char.py` gives all twenty trace values displayed under Finding.

**4. Independent Lefschetz and character checks.** Independently sum the signed traces of the original oriented simplicial chains, without relying on the invariant-boundary rank calculation. In every one of the ten conjugacy classes the resulting reduced Lefschetz trace agrees with \(\chi_4(g)-\chi_3(g)\). Taking ordinary character inner products with the five rational irreducible characters of \(S_4\), and projecting to the even and odd characters of the commuting involution, gives the complete nonnegative integer multiplicity table above. Dimensions sum to 21 and 24, respectively. As a further external consistency check, the natural tetrahedral virtual character \(\chi_4-\chi_3\) is \((3,1,-1,0,-1)\); subtracting it from the previously computed full-tetrahedron character \((99,1,-1,0,-1)\) gives \((96,0,0,0,0)\), exactly four regular characters as the published relative theorem requires. Since the fixed homology of a finite-group quotient is the invariant rational homology (transfer/averaging in characteristic zero), the quotient ranks follow directly from the absence of the trivial representation and the stated sign multiplicities under \(S_4\) and \(A_4\).

## Verification
Execute `python3 tetra_boundary_char.py` from the directory containing this document. The program uses only the Python 3 standard library. It reconstructs the Hasse digraph and all 4,332 nonempty acyclic matchings; builds oriented simplicial boundaries; checks the full ranks modulo primes 1009 and 10007; constructs the ten group actions and every relevant power; ranks their invariant boundary matrices; recovers the rational traces; verifies them by direct signed Lefschetz sums; and checks all twenty Specht-by-ghost multiplicities. The complete recorded output is `VERIFY_OUTPUT.txt` and the compact machine-readable final character table is `CHARACTER.csv`. The exit marker is `BOUNDARY_TETRAHEDRON_S4xC2_GRADED_CHARACTER_PASS`.

This computation is an exact finite proof **conditional only on the established integral homotopy classification in [1]**, which fixes the rational boundary ranks. It does not extrapolate from a finite range of complex sizes, and no external independent validation is claimed.

## Relationship to prior work
Scoville [1] proves the nonequivariant mixed-dimensional wedge type of this **non-pure** boundary Morse complex but not its graded rational symmetry character. Lin and Scoville [2] determine its automorphism group and ghost involution, not their action on homology. Existing exact character calculations for the **full** tetrahedron Morse complex [3], for the **pure** boundary complex [4], and for **generalized matchings without the acyclicity restriction** [5] concern different chain complexes. The study of geometric fixed-point inclusions for the pair of boundary/full tetrahedral complexes [6] identifies a relative rational module \(\mathbb Q[S_4]^{\oplus4}\), whose vanishing nonidentity *relative* character constrains only the **difference** of the two unknown graded boundary characters; it cannot determine either of them separately. The present calculation resolves their separate characters and the ghost grading on both degrees.

## Limitations
The theorem concerns exactly the ordinary Morse-matching complex of the boundary of a tetrahedron; it does not treat higher simplex boundaries, pure complexes or integral group-ring decompositions. The rational quotient claims do not determine quotient torsion or equivariant homotopy types. The characteristic-zero rank step uses Scoville's established homotopy theorem: the modular matrices by themselves would not exclude exceptional torsion. Results could overlap with an unindexed or unpublished equivalent computation. Independent mathematical audit has not been performed.

## References
[1] N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1, first submitted 2026-04-20. https://arxiv.org/abs/2604.18172

[2] M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907v1, 2019. https://arxiv.org/abs/1904.10907

[3] *The full symmetric-group character of the tetrahedral discrete-Morse complex*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-full-symmetric-group-character-of-the-tetrahedral-discrete-m--792ac3c70a65

[4] *The ghost-involution character of tetrahedral pure Morse complexes*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-ghost-involution-character-of-tetrahedral-pure-morse-complex--ab38cf809efe

[5] *Complete tetrahedral symmetry characters of generalized discrete Morse matching complexes*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-tetrahedral-symmetry-characters-of-generalized-discrete--da1e0162e98f

[6] *Proper-subgroup fixed-point collapses and four regular modules in a tetrahedral Morse-complex pair*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-proper-subgroup-fixed-point-collapses-and-four-regular-modules-i--95cb38f967b2
