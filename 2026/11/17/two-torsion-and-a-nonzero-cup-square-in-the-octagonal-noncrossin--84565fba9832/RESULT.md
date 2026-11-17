# Two-torsion and a nonzero cup square in the octagonal noncrossing-matching rotation quotient

## Finding
For a convex octagon, the ordinary rotation quotient of the noncrossing partial-matching complex has integral homology
\[
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z/2,&i=1,\\
0,&\text{otherwise},
\end{cases}
\qquad \pi_1(Y)\cong\mathbb Z/2.
\]
Moreover, its nonzero class \(\alpha\in H^1(Y;\mathbb F_2)\) satisfies \(\alpha\smile\alpha\ne0\). Under the full dihedral action the same complex has *contractible* ordinary geometric quotient. Eight is the first width \(4\le n\le8\) at which the cyclic quotient has integral torsion.

## Assumptions and scope
Place \(n\) distinct labeled points \(0,\ldots,n-1\) clockwise on a circle. A *chord* joins any two labels, including adjacent boundary sides. Let \(K_n\) have one vertex for each chord and faces consisting of finite sets of chords with disjoint endpoint sets and disjoint relative interiors. The groups \(C_n\) and \(D_n\) act through permutations of polygon labels. The spaces are *ordinary* quotient spaces of geometric realizations, not homotopy orbit spaces. This result treats \(n=8\), with a finite cutoff calculation for \(4\le n<8\).

## Proof
**1. Exact quotient cellular chains.** Every nonempty simplex is a noncrossing partial matching. At \(n=8\), their numbers by cardinality \(1,2,3,4\) are respectively \(28,140,140,14\). Take the order complex of the poset of nonempty faces (the first barycentric subdivision). Its simplices are strictly increasing chains of faces. Every group element preserving a chain setwise preserves each member (their cardinalities differ), so the simplicial group action is without inversions and the orbit-chain quotient is a finite CW complex. For each orbit representative of a chain, a codimension-one face is obtained by deleting one entry; the signed cellular boundary has coefficient \((-1)^j\) multiplied by the identification of that subchain's orbit. Thus this construction computes integral homology of the actual ordinary orbit space, including stabilizer effects.

The resulting orbit-cell counts in dimensions \(0,1,2,3\) are \((45,169,168,42)\) for \(C_8\) and \((35,112,105,27)\) for \(D_8\). All boundary compositions are exactly zero over \(\mathbb Z\). Repeated signed unit-pivot cancellations of adjacent chain degrees preserve chain homotopy type over \(\mathbb Z\); they use no nonunit division. For rotations, the cancellation counts in degrees \(1,2,3\) are \((44,124,42)\). The residual chain ranks are \((1,1,2,0)\) with the only nonzero differential an entry of absolute value \(2\) in degree two. This gives the displayed homology, including a single order-two class. For the full dihedral quotient, \((34,78,27)\) unit cancellations leave only one zero-cell; the reduced integral homology vanishes.

**2. Fundamental groups.** Use the same quotient order complex as a two-dimensional CW presentation: choose a spanning tree in the one-skeleton, take each remaining oriented edge as a free generator, and use the oriented triangular boundaries as relators. The exact code reconstructs all edge incidences and triangular relators and performs only legitimate Tietze eliminations: solving a relator in which a generator occurs exactly once, and substituting the resulting word into every other relator. For \(C_8\), \(125\) initial free generators admit \(124\) such eliminations; the remaining presentation has one generator \(g\) with three identical relators \(g^2\). Hence \(\pi_1(Y)=\langle g\mid g^2\rangle\cong\mathbb Z/2\). For \(D_8\), all \(78\) initial generators eliminate with no nonempty relator, so its fundamental group is trivial. The connected, simply connected, integral-acyclic finite dihedral quotient is contractible, by Hurewicz and Whitehead (equivalently, any first nonzero higher homotopy group would give nonzero integral homology).

**3. The cup square.** The universal coefficient theorem and computed homology give \(H^1(Y;\mathbb Z)=0\) and \(H^2(Y;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\). Consider the integral Bockstein \(\beta\) from \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb F_2\to0\). Exactness shows that \(\beta\colon H^1(Y;\mathbb F_2)\to H^2(Y;\mathbb Z)\) maps its nonzero class injectively onto the unique order-two subgroup. Mod-two reduction \(\rho\) does not kill this torsion class, because its kernel is \(2H^2(Y;\mathbb Z)\). The classical identity \(\rho\beta=\operatorname{Sq}^1\), together with \(\operatorname{Sq}^1(\alpha)=\alpha\smile\alpha\) for degree-one classes, proves the nonzero square.

**4. Natural lower-size cutoff.** Identical finite calculations for \(n=4,5,6,7\) leave zero differentials and residual cells \((2,0)\), \((1,1)\), \((1,1,0)\), and \((1,3,0)\), respectively, with no torsion. Thus eight is the first size within this explicitly checked range for which a cyclic polygon quotient of this complex has torsion.

## Verification
Run `python3 VERIFY.py` with an ordinary Python 3 interpreter (standard library only). It builds every chord, face, barycentric flag and group orbit from scratch, checks that every codimension-two boundary vanishes, and performs exact signed integer cancellations. It then independently uses the quotient two-skeleton to construct a spanning-tree presentation and replay all generator eliminations. `CHECK_OUTPUT.txt` gives the exact deterministic output, concluding with `VERIFY_OK`. The matching counts and signed boundaries are derived rather than loaded from a saved table. The computation is finite and exhaustive at the specified polygon sizes; it is not an infinite-family proof.

## Relationship to prior work
The underlying family of polygonal noncrossing matching complexes is discussed in Jakob Jonsson's *Simplicial Complexes of Graphs*, chapter "Noncrossing Graphs," section on noncrossing matchings. Its accessible chapter abstract and bibliographic record do not provide the present integral calculations for ordinary cyclic and dihedral geometric orbit spaces. Braun–Ehrenborg study the *noncrossing-diagonal/associahedral* complex, which permits shared endpoints and therefore is not this matching complex. Aichholzer–Asinowski–Miltzow study a compatibility graph whose vertices are **perfect** matchings, rather than this simplicial complex of **partial** matchings. The noncrossing matching complex in McConville–Mühle's shuffle-lattice work uses a bipartite matching model, not the convex-octagon model. These distinctions preclude direct implication of the present calculations, but do not prove publication priority.

## Limitations
No claim is made about a homeomorphism or complete homotopy type of the cyclic quotient, about sizes above eight, or about the equivariant homotopy type of the original complex. A plausible prior source is Jonsson's subscription-only chapter, whose complete text was not available for review; an indexed search and accessible preview cannot exclude an implicit equivalent computation. The result is self-review, not independently audited.

## References
1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, softcover first published 15 November 2007, chapter "Noncrossing Graphs," pp. 217–231. https://doi.org/10.1007/978-3-540-75859-4_16
2. B. Braun and R. Ehrenborg, "The complex of non-crossing diagonals of a polygon," arXiv:0802.1320 (2008). https://arxiv.org/abs/0802.1320
3. O. Aichholzer, A. Asinowski, and T. Miltzow, "Disjoint compatibility graph of non-crossing matchings of points in convex position," arXiv:1403.5546 (2014). https://arxiv.org/abs/1403.5546
4. T. McConville and H. Mühle, work on noncrossing matching complexes of shuffle lattices, arXiv:2208.13683 (2022). https://arxiv.org/abs/2208.13683
