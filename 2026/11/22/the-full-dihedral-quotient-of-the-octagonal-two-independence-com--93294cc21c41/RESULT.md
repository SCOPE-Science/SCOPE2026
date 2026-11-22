# The full dihedral quotient of the octagonal two-independence complex is a homotopy three-sphere

## Finding
Let \(C_8\) be the cycle on \(\mathbb Z/8\mathbb Z\), and let \(K=\operatorname{Ind}_2(C_8)=\mathcal D(C_8;P_3)\). Its faces are exactly those vertex subsets with no three cyclically consecutive vertices. The full dihedral group \(D_8=\langle r,s\mid r^8=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\). The **ordinary geometric orbit space** satisfies
\[
\boxed{|K|/D_8\simeq S^3.}
\]
In particular its integral homology is \(H_0\cong H_3\cong\mathbb Z\) and \(H_j=0\) for all other \(j\ge1\), and its fundamental group is trivial. This is a homotopy classification, not a homeomorphism or manifold assertion.

## Assumptions and scope
Only the eight-cycle and the full order-sixteen dihedral action are covered. A face is a bitmask \(m\in\{1,\ldots,255\}\) with no cyclic triple \(\{i,i+1,i+2\}\subseteq m\). The group acts on vertices and therefore on chains of faces. Quotients identify **geometric points**, not merely vertices of the original simplicial complex. All chain computations use exact integers, not modular or floating-point arithmetic. Established nonequivariant sphere-wedge results are inputs.

## Proof
**1. The correct orbit-cell complex.** Barycentrically subdivide \(K\). A simplex of the subdivision is a strictly increasing chain \(F_0\subsetneq\cdots\subsetneq F_d\) of nonempty faces. The action preserves face cardinality, so a group element stabilizing a chain fixes every chain vertex individually. Consequently the quotient has a finite CW cell decomposition with one \(d\)-cell for each orbit of such chains, oriented by its increasing order. Its exact integral cellular boundary is
\[
\partial[F_0<\cdots<F_d]=\sum_{j=0}^{d}(-1)^j[F_0<\cdots<\widehat{F_j}<\cdots<F_d],
\]
where brackets mean orbit classes, and repeated orbit classes are added with their signs. This accounts for all identifications of boundary faces, including coefficients of absolute value greater than one. There are 130 nonempty faces of \(K\); enumeration of chains under all 16 symmetries gives the number of orbit cells in dimensions zero through four as
\[
(c_0,c_1,c_2,c_3,c_4)=(15,81,183,177,60).
\]

**2. Exact integral cancellation.** The standalone program `verify_octagon_quotient.py` independently reconstructs the face list and the complete orbit-chain complex. It verifies \(\partial^2=0\) at every cell and implements the following unimodular chain cancellation: if \(x\in C_d\) has boundary coefficient \(p=\pm1\) at \(y\in C_{d-1}\), replace every other degree-\(d\) boundary column \(\partial z\) with \(\partial z-(\langle\partial z,y\rangle/p)\partial x\), then delete the contractible pair \((x,y)\), with its corresponding higher-boundary coordinate removed. This is an exact integral chain-homotopy-equivalence step; it is **not** claimed to be a topological elementary collapse. The checker finds 257 such valid cancellations, leaving one degree-zero and one degree-three generator with zero differential. Therefore the complete **integral** homology is precisely \(\mathbb Z\) in degrees zero and three, zero otherwise, without torsion.

**3. Simple connectivity.** A known classification gives \(K\simeq\bigvee^3 S^3\), hence \(K\) is simply connected. For every even-axis reflection \(r^{2a}s\), some vertex is fixed, hence the reflection fixes a point of \(|K|\). For each odd-axis reflection \(r^{2a+1}s\), there is a swapped adjacent pair \(\{a,a+1\}\), which is a face of \(K\), and its midpoint is fixed. Thus all eight reflections have nonempty geometric fixed sets. Reflections generate \(D_8\). Armstrong's orbit-space fundamental-group theorem therefore yields \(\pi_1(|K|/D_8)=D_8/D_8=1\).

**4. Homotopy classification.** Since the quotient is simply connected with \(H_2=0\), Hurewicz implies \(\pi_2=0\) and \(\pi_3\cong H_3\cong\mathbb Z\). A map \(S^3\to |K|/D_8\) representing the degree-three Hurewicz generator is an integral homology isomorphism. The homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence.

## Verification
Invoke `python3 verify_octagon_quotient.py` with Python 3 and only the standard library. It regenerates 130 nonempty faces and the full 516 orbit cells, compares the dimensional vector with \((15,81,183,177,60)\), independently checks every matrix identity \(\partial_{d-1}\partial_d=0\), and verifies that exactly 257 integral unit-pivot cancellations leave chain dimensions \((1,0,0,1,0)\) with all remaining boundaries zero. A successful run prints `OCTAGON_DIHEDRAL_QUOTIENT_INTEGRAL_HOMOLOGY_OK`. All of these finite cases are exhausted, not sampled; the separate fundamental-group argument and Whitehead theorem supply the homotopy classification, which chain algebra alone cannot establish.

## Relationship to prior work
Taylan's 2015 cycle devoid-complex calculation and Deshpande–Singh's higher-independence classification establish the unquotiented three-sphere wedge. A published complete dihedral **rational** character calculation further gives one surviving rational top class at eight vertices; it does not determine whether there is integral torsion or a nontrivial quotient fundamental group. A separate dihedral **subgroup-fixed-space** classification proves geometric fixed-space formulas for all subgroup types, but does not calculate the integral homology or homotopy type of the orbit space. The exact 257-step integral cancellation and corresponding homotopy conclusion are the new statements. These comparisons are between implications: neither rational invariants nor fixed-space types alone assert an integral homotopy equivalence of this orbit space. The cyclic-polytope nonmatching construction involves a different complex and does not imply this classification.

## Limitations
Only the complete dihedral quotient of the octagon is classified. The calculation gives an integral homotopy equivalence rather than an equivariant equivalence, homeomorphism, PL sphere, or a family formula for other cycle lengths. The integral computation has a reproducible finite program and is not an independently audited mathematical certificate. Equivalent unindexed work may exist; no claim of exhaustive bibliographic priority is made.

## References
1. Demet Taylan, *Matching Trees and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, first posted 2015-01-27; Theorem 5.2. https://arxiv.org/abs/1501.06754.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15; Theorem 4.6. https://arxiv.org/abs/2001.05448.
3. *Dihedral homology characters and rational quotient topology of cycle two-independence complexes*, published 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dihedral-homology-characters-and-rational-quotient-topology-of-c--c6fb124adaa6.
4. *Dihedral subgroup fixed spaces of two-independence complexes of cycles*, published 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dihedral-subgroup-fixed-spaces-of-two-independence-complexes-of--efdae8142d23.
5. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. **64** (1968), 299–301. https://doi.org/10.1017/S0305004100042845.
