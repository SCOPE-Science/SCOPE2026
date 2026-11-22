# Binary tetrahedral fundamental group of the alternating-color pentagon quotient

## Finding
Let \(X=|\operatorname{Hom}(C_5,K_4)|\) be the geometric realization of the usual graph-multimorphism cell complex of proper four-colorings of a pentagon. Relabeling the four target colors by the alternating group \(A_4\) acts **freely** on \(X\). The ordinary orbit space \(Y=X/A_4\) is a closed connected orientable three-manifold, with universal cover \(S^3\), and
\[
\boxed{\pi_1(Y)\cong 2T\cong\operatorname{SL}_2(\mathbb F_3),}
\]
where \(2T\) is the binary tetrahedral group of order \(24\). Its complete integral homology is
\[
\boxed{H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z/3\mathbb Z,&i=1,\\
0,&\text{otherwise}.
\end{cases}}
\]
These are invariants of the **ordinary geometric quotient**, not the Borel construction. No particular geometric realization of the covering action on the standard round three-sphere is claimed.

## Assumptions and scope
The source graph \(C_5\) has vertices \(\mathbb Z/5\mathbb Z\) with edges joining consecutive residues. The target graph \(K_4\) has colors \(\{0,1,2,3\}\). An open cell of the regular CW complex \(\operatorname{Hom}(C_5,K_4)\) is determined by five nonempty subsets \((A_0,\ldots,A_4)\) such that \(A_i\cap A_{i+1}=\varnothing\) for every index modulo five. The closed cell is the product \(\prod_i\Delta(A_i)\) and has dimension \(\sum_i(|A_i|-1)\). The group \(A_4\) acts only on the target-color labels, not on the five source positions. Homology coefficients are integral unless otherwise specified.

## Proof
**1. Freeness of even-color relabeling.** Every nonidentity element of \(A_4\) has cycle type \((3,1)\) or \((2,2)\), hence exactly two orbits on the four colors. Suppose such an element fixes a point of \(X\). Since the open cells form a disjoint partition and the group permutes them, it preserves the unique open cell containing that point. Each of its five nonempty color sets must therefore be a union of full color orbits. No set can contain both orbits, since it would be the entire color set, leaving its neighbor empty. Thus every position receives exactly one of two disjoint palette orbits. Adjacent positions must receive different orbits, giving a two-coloring of the odd cycle \(C_5\), a contradiction. Hence all nonidentity elements act without fixed points. In particular, every open cell has an orbit of cardinality twelve and the quotient is a regular twelve-sheeted covering.

**2. Three-manifold and universal covering.** The 2005 theorem of Csorba–Lutz and the homeomorphism theorem of Schultz establish \(X\cong\mathbb{RP}^3\cong SO(3)\). Thus \(X\) is a closed connected orientable three-manifold with universal cover \(S^3\) and \(\pi_1(X)=\mathbb Z/2\mathbb Z\). Each color permutation in the freely acting \(A_4\) preserves orientation: if a self-homeomorphism of \(\mathbb{RP}^3\) reversed orientation, its rational Lefschetz number would be \(1-(-1)=2\), contradicting the fixed-point-free Lefschetz theorem. Consequently the quotient \(Y\) is closed, connected and orientable. The composite covering \(S^3\to X\to Y\) is universal and gives a central extension
\[
1\longrightarrow C_2\longrightarrow E:=\pi_1(Y)
\longrightarrow A_4\longrightarrow1,
\]
with \(|E|=24\); centrality follows from the trivial automorphism group of \(C_2\).

**3. Integral quotient homology.** Give every product cell the orientation obtained by ordering source positions from zero to four and using increasing target colors inside each simplex. Removing the \(j\)-th color of the \(i\)-th factor contributes the cellular boundary sign \((-1)^{\sum_{h<i}(|A_h|-1)+j}\), with \(j\) indexed from zero. When a face is moved by an even color permutation to its lexicographically least orbit representative, its induced orientation changes by the product of the permutation signs on the ordered color subsets. Because the group action is free, this gives an unambiguous integral cellular chain complex of the quotient.

Exhaustive generation of all disjoint adjacent five-tuples gives \(2160\) nonempty cells in \(X\), distributed by dimension as \((240,780,840,300)\), and exactly \((20,65,70,25)\) quotient cells in degrees zero through three. The standalone program `verify.py` constructs the three integral boundary matrices, checks \(\partial_1\partial_2=\partial_2\partial_3=0\), and performs exact Smith reductions over \(\mathbb Z\). Their invariant factors are, respectively,
\[
(1^{\times19}),\qquad(1^{\times45},3),\qquad(1^{\times24}).
\]
The boundary ranks are \((19,46,24)\). Since \(\ker\partial_1\) is a primitive lattice of rank \(46\), the single factor \(3\) in \(\partial_2\) gives \(H_1(Y;\mathbb Z)=\mathbb Z/3\mathbb Z\). Since \(\operatorname{im}\partial_3\) is primitive of the same rank \(24\) as \(\ker\partial_2\), \(H_2=0\). Finally \(H_3\cong\mathbb Z\) and connectedness gives \(H_0\cong\mathbb Z\). There are no cells in higher degrees.

**4. The binary tetrahedral extension.** Let \(E'=[E,E]\). By the computed first homology, \(E/E'\cong C_3\), so \(|E'|=8\). The projection \(E\to A_4\) sends \(E'\) onto \(A_4'=V_4\); thus \(E'\) is exactly the inverse image of the normal Klein four subgroup, and \(E'/C_2\cong V_4\). By the Schur–Zassenhaus theorem, \(E\) has a subgroup \(C_3\) complementing its normal order-eight subgroup \(E'\). Conjugation by its generator cyclically permutes the three nonzero elements of \(E'/C_2\).

The group \(E'\) cannot be abelian: in that case the commutator subgroup of \(E'\rtimes C_3\) would be the image of the map \(u\mapsto tut^{-1}u^{-1}\) on \(E'\), with size at most four because the central \(C_2\) lies in the kernel. This contradicts \(E'=[E,E]\) of order eight. The only nonabelian groups of order eight are the dihedral group \(D_8\) and the quaternion group \(Q_8\). The former has a characteristic cyclic subgroup of order four, whose nonzero image in \(D_8/C_2\cong V_4\) would be fixed by every automorphism; that is incompatible with the indicated three-cycle. Therefore \(E'\cong Q_8\). The order-three complement cycles its three cyclic subgroups of order four, identifying
\[
E\cong Q_8\rtimes C_3\cong 2T\cong\operatorname{SL}_2(\mathbb F_3).
\]
This proves the claimed nonabelian fundamental group, not merely its abelianization.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. The source and the actual output `verification_output.txt` are included in this package. The verifier regenerates all cells from the defining adjacency-disjointness predicate, all twelve even permutations, checks every open-cell orbit has twelve members, constructs orientation-aware quotient cellular boundaries, verifies both boundary compositions vanish, and computes the Smith factors exactly. The group identification in Step 4 is a separate finite-group proof relying on the verified first homology, not an inference from numerical ranks alone.

## Relationship to prior work
Csorba–Lutz (2005) and Schultz (2005) establish the underlying \(\mathbb{RP}^3\) topology. Dover–Özaydın (2013) establish an equivariant homeomorphism for one **source** reflection, not for target-color \(A_4\). A published joint color/source character theorem determines the rational \(D_5\times S_n\)-representations but not this quotient's integral first homology or its nonabelian fundamental group. A published \(D_5\) **source-position** quotient has dicyclic fundamental group of order twenty; neither its action nor its result is the \(A_4\) target-color quotient considered here. The published alternating-target-color formula for \(\operatorname{Hom}(K_m,K_n)\) applies to a complete **source** graph, not the pentagon. The new comparison is the specific free target-color action and its binary-tetrahedral extension; none of these cited statements determines it.

## Limitations
The theorem classifies the abstract fundamental group and integral homology and identifies the universal covering space; it does not specify a unique geometric or metric model for the deck group action on \(S^3\). The Smith calculation is exact and exhaustive for this finite four-color object, but it is not a parameter-uniform statement for other target-color counts or other source graphs. The mathematical argument uses the established Stiefel homeomorphism. A bibliographic search cannot exclude equivalent unpublished or unindexed classifications; no independent audit has been performed.

## References
1. P. Csorba and F. H. Lutz, *Graph coloring manifolds*, arXiv:math/0510177, first public 2005-10-09, https://arxiv.org/abs/math/0510177 .
2. C. Schultz, *Small models of graph colouring manifolds and the Stiefel manifolds \(\operatorname{Hom}(C_5,K_n)\)*, arXiv:math/0510535, first public 2005-10-25, especially Theorem 5.2, https://arxiv.org/abs/math/0510535 .
3. J. Dover and M. Özaydın, *Stiefel manifolds and coloring the pentagon*, arXiv:1302.2831, first public 2013-02-12, especially the Main Theorem and Question 5.6, https://arxiv.org/html/1302.2831v1 .
4. *Joint color and pentagon symmetry of graph-coloring manifolds*, published result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-joint-color-and-pentagon-symmetry-of-graph-coloring-manifolds--72253c7af9d3 .
5. *Dicyclic fundamental group of the four-colour pentagon quotient*, published result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dicyclic-fundamental-group-of-the-four-colour-pentagon-quotient--d57eddbf16e9 .
6. *Alternating-color quotients of complete-graph Hom complexes are integral sphere wedges*, published result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-alternating-color-quotients-of-complete-graph-hom-complexes-are--4ac9843326aa .
