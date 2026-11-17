# Two-torsion in the Coxeter-rotation quotient of the type-\(B_4\) noncrossing partition complex

## Finding

Let \(W=B_4\) be the Coxeter group of signed permutations of \(\{1,2,3,4\}\), with multiplication by composition and the Coxeter element \(c=(2,3,4,-1)\). Write \(T\) for its set of sixteen reflections, \(\ell_T\) for shortest reflection length, and
\[
NC(W,c)=\{w\in W:\ell_T(w)+\ell_T(w^{-1}c)=4\}.
\]
Equip this set with absolute order \(x\le_T y\) if \(\ell_T(x)+\ell_T(x^{-1}y)=\ell_T(y)\). Let \(X=\Delta(NC(W,c)\setminus\{e,c\})\) and let \(C_8=\langle c\rangle\) act on chains by conjugation. For the **ordinary geometric quotient** \(Y=|X|/C_8\), the complete integral homology is
\[
H_j(Y;\mathbb Z)\cong\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/2\mathbb Z,&j=1,\\
\mathbb Z^9,&j=2,\\
0,&j\ge3.
\end{cases}
\]
In particular, the torsion of this quotient is absent from the underlying shellable rank-four noncrossing-partition complex.

## Assumptions and scope

All statements concern the finite real Coxeter group of type \(B_4\) and its specified Coxeter element, not arbitrary rank, not the poset of orbit representatives, and not a homotopy quotient. Signed permutations are represented by tuples \((a_1,a_2,a_3,a_4)\) with distinct absolute entries \(1,2,3,4\), acting on signed indices by \(w(-i)=-w(i)\). The sixteen generating reflections are the four single-coordinate sign flips and, for each unordered pair of coordinates, their signed exchanges with equal or opposite signs. This set generates the entire order-\(384\) group. All homology is singular homology with integral coefficients.

## Proof

1. **Finite interval.** Breadth-first search of the full Cayley graph on the sixteen reflections determines exact shortest reflection lengths \(\ell_T\), not a heuristic approximation. The length distribution in \(W\) is \((1,16,86,176,105)\) in degrees \(0\) through \(4\). The absolute interval has \(70\) elements with rank distribution \((1,16,36,16,1)\). Its proper part therefore has \(68\) vertices and order-complex chain counts \((68,288,256)\) in dimensions \(0,1,2\). A chain has strictly increasing reflection lengths, so its vertices have distinct ranks.

2. **Genuine quotient cells.** Conjugation by \(c\) preserves reflection length and absolute order. Since every simplex is a totally ordered chain with distinct ranks, a group element mapping a simplex to itself fixes every vertex individually. The action is thus without inversions. The orbit space inherits a regular-orbit-of-open-simplices cellular structure with each chain orbit contributing one cell, and attaching coefficients obtained by taking the alternating boundary of a representative chain, sending each face to its chain-orbit representative. This handles nonfree stabilizers: no division by stabilizer order or averaging is used. The quotient has \((18,72,64)\) cells.

3. **Exact integral boundary computation.** Build the cellular matrices \(\partial_1:\mathbb Z^{72}\to\mathbb Z^{18}\) and \(\partial_2:\mathbb Z^{64}\to\mathbb Z^{72}\) from those alternating face coefficients. Direct integer multiplication gives \(\partial_1\partial_2=0\). Exact Smith normal forms over \(\mathbb Z\) have nonzero diagonal entries \(1\) seventeen times for \(\partial_1\), and \(1\) fifty-four times plus \(2\) once for \(\partial_2\). Thus the quotient is connected and \(H_2=\ker\partial_2\cong\mathbb Z^{64-55}=\mathbb Z^9\). Since \(\partial_1\) has primitive image and is split surjective onto a rank-\(17\) direct summand of \(\mathbb Z^{18}\), the torsion in \(\ker\partial_1/\operatorname{im}\partial_2\) is the nonunit Smith factor \(2\), and its free rank is \((72-17)-55=0\). There are no cells in higher dimensions.

4. **Reproducibility.** Run `python3 verify_b4.py` with Python 3 and SymPy. It builds the complete \(384\)-element signed group and reflection-length breadth-first search, enumerates all interval chains and eightfold orbits, forms the exact integer boundary matrices, asserts their composition vanishes and checks both Smith diagonals. It exits nonzero if any count or group identity disagrees. `CHECKS.txt` records the actual execution output.

## Verification

The checker reports `B4_CYCLIC_NC_QUOTIENT_EXACT_PASS group=384 interval=70 cells=18,72,64` together with the integer Smith-factor multisets \(\{1^{17}\}\) and \(\{1^{54},2\}\). These computations exhaust the explicitly defined finite complex and use exact arithmetic. No unverified finite-to-infinite extrapolation is involved.

## Relationship to prior work

Bessis and Reiner (2007, arXiv:math/0701792) prove cyclic sieving for Coxeter-element conjugation on noncrossing partitions, including enumeration of elements fixed by rotation. Kenny (first arXiv version in 2008, later 2009 journal publication) constructs geometric bases for the homology of noncrossing partition lattices and invokes their known shellability. Both are fundamental input/context. Fixed-element counting and the integral topology of the unquotiented proper-part complex do not determine the integral cellular differential of the geometric orbit space, especially its nonunit Smith factor. Reiner's earlier 1997 classical-type account gives background on the type-\(B\) lattice; only its abstract/index was accessible here. No equivalent statement for this precise quotient was located in the checked literature; this is not proof of global novelty.

## Limitations

This classification gives integral **homology** only, not the integral homotopy type or fundamental group; \(H_1\cong\mathbb Z/2\) by itself does not establish \(\pi_1\cong\mathbb Z/2\). The result treats rank four only. Exhaustive checking certifies the finite combinatorial model conditional on the independently stated standard definitions and the valid no-inversions quotient-cell construction. Source searches cannot exclude an overlooked existing equivalent calculation, especially in unindexed material. No independent external audit has occurred.

## References

- D. Bessis and V. Reiner, *Cyclic sieving of noncrossing partitions for complex reflection groups*, arXiv:math/0701792, first publicly submitted 2007-01-27. https://arxiv.org/abs/math/0701792
- A. Kenny, *Geometrically Constructed Bases for Homology of Non-Crossing Partition Lattices*, arXiv:0806.4151, first publicly submitted 2008-06-25; *Electronic Journal of Combinatorics* 16 (2009), R48, DOI:10.37236/137. https://arxiv.org/abs/0806.4151
- V. Reiner, *Non-crossing partitions for classical reflection groups*, *Discrete Mathematics* (1997), DOI:10.1016/S0012-365X(96)00365-2. Abstract/index consulted; complete text not verified here.
