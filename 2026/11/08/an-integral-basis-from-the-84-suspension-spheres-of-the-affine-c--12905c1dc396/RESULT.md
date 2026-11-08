# An integral basis from the 84 suspension spheres of the affine-cube matroid

## Finding
Let \(V=\mathbb F_2^3\), and let \(K\) be the independence complex of the rank-four affine-geometry matroid \(AG(3,2)\). The 14 affine planes are the four-subsets \(P\subset V\) with \(\bigoplus_{x\in P}x=0\); the 56 other four-subsets are precisely the facets of \(K\). For each affine plane \(P\) and unordered pair \(\{a,b\}\subset V\setminus P\), the induced six-vertex subcomplex on \(P\cup\{a,b\}\) contains the oriented embedded three-sphere
\[
 z_{P;a,b}= [a]*\partial[P]-[b]*\partial[P].
\]
Here \([P]\) is the ascendingly oriented tetrahedron, and \(*\) is the simplicial join of oriented chains, with \(a<b\). There are exactly 84 such supported sphere cycles. They form a single orbit of the 1,344-element affine group \(AGL_3(2)\), each is primitive in integral homology, and they generate the entire free abelian group
\[
 \widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{21}.
\]
More strongly, the 21 cycles indexed by the zero-based positions
\[
 0,1,2,6,7,8,12,13,14,18,19,20,24,25,26,30,31,32,36,37,38
\]
in the lexicographic ordering specified below form an **integral basis**. The least possible vertex-support size of a nonzero three-cycle is six. Every one of the 28 six-vertex induced subcomplexes has integral third homology of rank two and contains exactly three of the indicated suspension spheres, spanning its top homology.

## Assumptions and scope
Vertices are integers \(0,\ldots,7\), interpreted as binary triples, and vector addition is bitwise XOR. All vertex subsets are written increasingly. A plane is an increasing four-subset with zero XOR. A facet is an increasing four-subset with nonzero XOR. Index the 56 facets lexicographically by \(0,\ldots,55\). Index the 84 cycles by lexicographically increasing pairs \((P,(a,b))\), first by plane and then by the increasing two-subset of its complement, starting at zero. Orientation of a simplex is its increasing vertex order. Only ordinary (not Borel) simplicial homology is considered; the automorphism orbit assertion is at the level of oriented cycles up to sign.

## Proof
**Underlying chain complex.** The seven-simplex's full three-skeleton has all 70 tetrahedra. The independence complex \(K\) contains all faces of dimensions at most two, and omits the 14 tetrahedra representing affine planes. If \(P\) is an omitted plane and \(a\notin P\), the simplicial boundary of the formally oriented four-simplex \([a]*[P]\) yields
\[
 \partial[P]=\partial([a]*[P])+[a]*\partial[P].
\]
All tetrahedra appearing in \([a]*\partial[P]\) belong to \(K\): none of their four vertices is an affine plane, since any three distinct points of \(P\) uniquely determine \(P\). Applying the boundary map to the latter three-chain gives \(\partial([a]*\partial[P])=\partial[P]\), because \(\partial^2[P]=0\). Therefore each omitted tetrahedral boundary is an integer linear combination of boundaries of present facets. Thus \(\operatorname{im}\partial_3(K)=\operatorname{im}\partial_3(\operatorname{skel}_3\Delta^7)=\ker\partial_2\), including integrally, by exactness of the augmented full simplex chains. The common image has rank \(\binom73=35\), so \(\ker\partial_3(K)\) is free of rank \(56-35=21\). Integral reduced homology in every other degree vanishes.

**Embedded spheres and support.** For \(P\) and distinct outside points \(a,b\), the eight tetrahedra \([a]*\partial[P]\) and \([b]*\partial[P]\) are in \(K\). Their signed difference is a cycle because the common boundary is \(\partial[P]\). Its abstract support is the suspension of the boundary of a tetrahedron, hence a simplicial three-sphere. The coefficient of every one of its eight tetrahedra is \(\pm1\), so evaluation on any one such facet gives a homomorphism \(H_3(K;\mathbb Z)\to\mathbb Z\) sending the class to \(\pm1\). It is therefore nonzero and primitive.

**Sharp support threshold.** Every five-set contains exactly one affine plane, because the complement has three points and adding their XOR produces the unique four-set avoiding that complement. The induced complex on five points has four tetrahedra whose boundaries are independent (they are four of the five boundaries of a four-simplex). Thus it has zero third homology; smaller induced subcomplexes also have none. Every six-set contains exactly three planes: the block-design counts are 14 planes, seven through each point, and three through each pair, giving \(14-7-7+3=3\) planes avoiding a specified complementary pair. The induced complex consequently has 12 tetrahedra. Every omitted tetrahedral boundary can be expressed using an outside vertex *within that same six-set*, so its boundary map has the same rank 10 as the full three-skeleton on six vertices. Hence its third homology is free of rank two. Its three displayed sphere cycles have pairwise linearly independent reductions modulo two, and thus possess a unimodular two-coordinate minor; they span the local rank-two lattice. These statements can alternatively be checked by exhaustive integer simplex-chain operations in the accompanying verifier.

**Unimodular global basis.** In the 56-row signed tetrahedral chain matrix whose 84 columns are \(z_{P;a,b}\), select the 21 columns listed in the Finding and the 21 zero-based row positions
\[
 0,1,2,4,5,6,8,12,13,14,16,20,24,28,29,30,32,36,40,44,48.
\]
The exact determinant of this 21-by-21 minor is \(-1\). The signed entry formula and exact integral Bareiss determinant computation are completely specified and reproduced by `verify.py`. Therefore these 21 cycles generate a primitive rank-21 direct summand of the full degree-three chain group. Since they lie in the rank-21 kernel of \(\partial_3(K)\), their span equals that kernel: a finite-index proper subgroup would contradict saturation in the ambient free chain group. All 84 sphere cycles therefore generate the whole integral top homology.

**Symmetry orbit.** The affine group has \(8\lvert GL_3(2)\rvert=8\cdot168=1344\) elements and permutes the affine planes and their outside pairs. It acts transitively on planes, and a plane stabilizer acts as all permutations of the complementary four points, hence transitively on their six unordered pairs. Thus the 84 cycles form one orbit up to orientation sign. The verifier independently enumerates all 1344 transformations and checks the orbit size.

## Verification
Run `python3 verify.py` in the same directory as `verification_output.txt` (standard Python library only). The program checks all 84 integer boundary identities, each eight-tetrahedron support, all 56 five-vertex cases, all 28 six-vertex cases including local rank, the specified integral determinant \(-1\), and all 1344 affine transformations on a chosen cycle label. Its printed output is preserved verbatim in `verification_output.txt`. The determinant certificate, unlike finite sampling of an infinite statement, exhausts this entire eight-vertex instance; the chain-level proof supplies the topological interpretation.

## Relationship to prior work
The 14 circuit-hyperplanes of \(AG(3,2)\), its identification with the unique Steiner quadruple system \(S(3,4,8)\), and its Tutte polynomial were already described by Merino, Ramírez-Ibáñez and Rodríguez-Sánchez (2012). In particular the Betti rank 21 and wedge-of-spheres property are **not** claimed as novel. The matroid is also self-dual up to isomorphism, and goes by the binary-affine-cube or tipless-spike descriptions. General equivariant matroid-homology constructions of Moci and Pezzoli, and the classical affine Steinberg-module literature, may imply its abstract representation. The present assertion is instead about **a specific primitive 84-cycle geometric orbit, a sharp six-vertex homology carrier, and an explicit unimodular integral basis**. These finer integral chain/support statements do not follow merely from a representation dimension or a generic matroid shellability theorem.

## Limitations
This is a finite-rank result for \(AG(3,2)\). It does not classify all affine geometries, provide an integral character decomposition, or claim first discovery of the rank, matroid, equivariant homology framework, or affine Steinberg representation. An inaccessible potentially relevant classical monograph on affine Steinberg modules remains a priority risk; its full chapter was not inspected. The work has not received independent mathematical audit.

## References
1. C. Merino, M. Ramírez-Ibáñez, G. Rodríguez-Sánchez, “The Tutte Polynomial of Some Matroids,” *International Journal of Combinatorics* (first available 2012-10-04), https://doi.org/10.1155/2012/430859 . Section 4 gives the fourteen affine planes and Steiner-system identification.
2. L. Moci and G. Pezzoli, “Representations of automorphism groups on the homology of matroids,” arXiv:2001.03760, https://arxiv.org/abs/2001.03760 . General equivariant context, not the stated integral sphere-cycle basis.
3. SageMath, “Database of matroids,” https://doc.sagemath.org/html/en/reference/matroids/sage/matroids/database_matroids.html . Alternative affine-geometry labels and duality.
4. G. Lusztig, *The Discrete Series of GLn over a Finite Field*, Chapter 2, “The Affine Steinberg Module,” https://doi.org/10.1515/9781400881765 . Potential abstract representation overlap; full chapter not accessible.
5. A. Hartman, “Quadruple systems containing AG(3,2),” *Discrete Mathematics* 39 (1982), 293–299, https://doi.org/10.1016/0012-365X(82)90151-0 . Classical Steiner quadruple context.
