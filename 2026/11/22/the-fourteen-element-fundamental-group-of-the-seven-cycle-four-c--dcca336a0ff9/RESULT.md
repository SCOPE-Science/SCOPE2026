# The fourteen-element fundamental group of the seven-cycle four-colour quotient

## Finding

Let \(X=\operatorname{Hom}(C_7,K_4)\) denote the Lovász graph-multimorphism complex. The cyclic group \(C_7\) acts by rotating the seven input positions. For the **ordinary geometric quotient** \(Y=|X|/C_7\), the action is free and
\[
\boxed{\pi_1(Y)\cong\mathbb Z/14\mathbb Z},\qquad
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z/14\mathbb Z,&i=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Moreover, the seven-sheeted covering \(|X|\to Y\) has \(\pi_1(|X|)\cong\mathbb Z/2\mathbb Z\). No homotopy equivalence to a lens space or manifold is asserted.

## Assumptions and scope

Write the vertices of \(C_7\) as \(\mathbb Z/7\mathbb Z\) and the target colours as \(\{0,1,2,3\}\). An open \(d\)-cell is a tuple \(A=(A_0,\ldots,A_6)\) of nonempty colour subsets satisfying \(A_i\cap A_{i+1}=\varnothing\) modulo seven, with \(d=\sum_i(|A_i|-1)\). Its closure is the product of four-colour simplices \(\prod_i\Delta(A_i)\), oriented by increasing colours in increasing coordinate order. Quotienting means the geometric orbit space of this finite regular CW complex. The group acts without permuting target colours.

## Proof

**Free action and quotient chain complex.** A nonidentity rotation of seven positions is transitive. Were an open cell setwise fixed, all its seven nonempty colour sets would agree, contradicting adjacency disjointness. Since each point is in a unique open cell, no nonidentity rotation fixes a point. Every orbit of cells therefore has size seven. A rotation by \(k\) coordinates acts on the orientation of a product cell by the Koszul sign \((-1)^{uv}\), where \(u\) and \(v\) are the sums of simplex dimensions in the two coordinate blocks separated by the cut. This determines integral quotient cellular incidence coefficients without dividing by seven.

**Exact cellular model and homology.** Generate all tuples of seven nonempty subsets of \(\{0,1,2,3\}\) with consecutive disjointness. Canonicalize each cyclic orbit lexicographically, with the above orientation sign. The quotient's complete cell counts in degrees zero through five are
\[
(312,1452,2640,2340,1008,168).
\]
For a cell \(A\), delete the \(j\)-th increasing-colour vertex from coordinate \(i\), giving incidence sign \((-1)^{\sum_{h<i}(|A_h|-1)+j}\), followed by the Koszul sign of canonicalization. The accompanying verifier constructs these **entire** integer boundary matrices and confirms each consecutive product is zero. A deterministic integral chain contraction at entries \(\pm1\), using only invertible integer elementary operations and deleting a contractible adjacent-degree pair at each step, performs 3957 valid cancellations, leaving ranks \((1,2,2,1,0,0)\). All remaining boundary matrices vanish except the two-by-two boundary from degree two to degree one. Its four entries have greatest common divisor one, and its determinant has absolute value fourteen. Consequently its integral Smith invariants are \((1,14)\), yielding the asserted homology in every degree.

**Fundamental group.** The complete connected quotient one-skeleton has 312 vertices and 1452 oriented edges. Collapse a breadth-first spanning tree of 311 edges: the standard cellular presentation of \(\pi_1(Y)\) has 1141 generators. Each of the 2640 quotient two-cells contributes its actual oriented attaching word: a triangle when one colour coordinate is a three-element set, or a square when two coordinates are two-element sets. Edges are matched to their rotation orbits, with orientations retained. The verifier checks the abelianized exponent vector of **each** attaching word against the independently built integral cellular boundary. It then applies 1140 elementary Tietze eliminations: whenever one relator contains a generator exactly once, solve for that generator, substitute it in every remaining relator, and delete the solved relator and generator. Cyclic conjugation and free cancellation preserve the presented group throughout. The remaining presentation has one generator \(g\) and 46 relators, each exactly \(g^{14}\) or \(g^{-14}\). Therefore the presented group is \(\langle g\mid g^{14}=1\rangle\cong C_{14}\), not merely a group with abelianization \(C_{14}\).

**The covering group's kernel.** Because the source complex is connected and the rotation action is free, the covering exact sequence identifies \(\pi_1(|X|)\) with the index-seven subgroup of \(C_{14}\). That subgroup is uniquely \(C_2\).

## Verification

The Python-standard-library script `verify_hom_c7_k4.py` in the accompanying package re-enumerates the entire finite complex, constructs every signed quotient boundary, proves \(\partial^2=0\) computationally by exact integer arithmetic, performs the integral unit-pivot chain contractions, constructs all cellular attaching words, checks their abelianizations, and executes the complete sequence of group-preserving Tietze transformations. It stops with assertions if the cell counts, homology invariants, relator checks or final group presentation differ. The reproduced output ends in `ALL_HOM_C7_K4_QUOTIENT_CHECKS_OK`. Unlike a sample computation, the enumeration visits **all** admissible seven-tuples and the proof uses the finite CW presentation of this single object. The script is supplementary to the explicitly specified finite chain and presentation algorithms in the preceding proof.

## Relationship to prior work

Kozlov [1], Theorem 7.2, computes the integral cohomology of the **unquotiented** family \(\operatorname{Hom}(C_m,K_n)\); in this case it gives \(\widetilde H^2(X;\mathbb Z)\cong\mathbb Z/2\) and \(\widetilde H^3(X;\mathbb Z)\cong\mathbb Z\). These cohomology groups do not determine the nonabelian fundamental group of a distinct cyclic orbit space. Babson and Kozlov [2] analyze odd-cycle Hom complexes and reflection-based topological colouring obstructions; the sevenfold rotation quotient's fundamental-group presentation is not supplied there. The published dihedral-orbit calculation for \(\operatorname{Hom}(C_5,K_4)\) [3] instead treats the five-cycle and identifies a different order-twenty dicyclic group; neither its object nor its result contains this seven-cycle quotient calculation. Target-colour relabeling, graph categorical-product independence complexes and matching-complex cyclic quotients are different actions and different spaces. No exact equivalent or stronger covering theorem was identified in the searched sources. Search absence cannot establish publication priority.

## Limitations

This is a complete computation for the seven-cycle with four colours, not an all-odd-cycle formula. The chain contractions determine homology, not the entire homotopy type of the five-dimensional CW quotient. The finite group presentation establishes \(\pi_1\) but does not identify higher homotopy or an equivariant model of the covering space. Independently conducted mathematical review has not occurred. The originality comparison is subject to the possibility of an unindexed equivalent proof.

## References

[1] D. N. Kozlov, *Cohomology of colorings of cycles*, arXiv:math/0507117, first publicly posted 2005-07-06, Theorem 7.2 (p. 21). https://arxiv.org/abs/math/0507117

[2] E. Babson and D. N. Kozlov, *Proof of the Lovász Conjecture*, arXiv:math/0402395, first publicly posted 2004-02-24. https://arxiv.org/abs/math/0402395

[3] *Dicyclic fundamental group of the four-colour pentagon quotient*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dicyclic-fundamental-group-of-the-four-colour-pentagon-quotient--d57eddbf16e9
