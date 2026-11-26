# Integral homology and a nonzero mod-five cup product in a toroidal hard-square quotient

## Finding

Let \(G=C_4\square C_5\) be the Cartesian product of cycles, let \(X=|\operatorname{Ind}(G)|\), and let \(C_5=\langle t\rangle\) act by \(t(i,j)=(i,j+1)\) on vertices \((i,j)\in\mathbb Z/4\times\mathbb Z/5\). All coordinates in this statement are understood modulo their indicated cycle lengths. For the **ordinary geometric orbit space** \(Y=X/C_5\), the action is free and

\[
H_k(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,4,\\
\mathbb Z/5\mathbb Z,&k=1,\\
\mathbb Z^2,&k=3,\\
0,&\text{otherwise}.
\end{cases}
\]

Its low homotopy groups are \(\pi_1(Y)\cong C_5\), \(\pi_2(Y)=0\), and \(\pi_3(Y)\cong\mathbb Z^2\), with trivial \(C_5\)-action on the third group. If \(\alpha\in H^1(Y;\mathbb F_5)\) is the nonzero class induced by the canonical fivefold covering and \(\beta\) denotes the mod-five Bockstein from \(0\to\mathbb F_5\to\mathbb Z/25\to\mathbb F_5\to0\), then

\[
\alpha\smile\beta(\alpha)\ne0\quad\text{in }H^3(Y;\mathbb F_5).
\]

The space \(Y\) is therefore not homotopy equivalent to a wedge of the degree-one Moore complex \(M(\mathbb Z/5,1)=S^1\cup_5 e^2\) and spheres, even though \(M(\mathbb Z/5,1)\vee S^3\vee S^3\vee S^4\) has exactly the displayed integral homology. This is a cohomological obstruction, not a complete homotopy classification.

## Assumptions and scope

The graph \(G\) has twenty vertices and undirected edges precisely between \((i,j)\) and \((i\pm1,j)\), or between \((i,j)\) and \((i,j\pm1)\). Its independence complex has a simplex for **every nonempty independent vertex set**, including nonmaximal sets. In the topological realization its empty face is not an extra point or a \((-1)\)-cell. The quotient is the ordinary topological orbit space, not the Borel construction or a quotient of the graph before forming its independence complex. All homology is unreduced integral singular homology unless coefficients are displayed; the cellular computations use the simplex-orbit cells with their induced attaching maps.

## Proof

**1. Free action.** Every nonidentity element of \(C_5\) generates the fivefold translation. If an independent face were invariant, then alongside any vertex \((i,j)\) it would contain all five vertices of its horizontal row, including adjacent vertices. This is impossible. A fixed point of the geometric realization would have an invariant nonempty support, so the geometric action is free. In particular, the quotient has a cellular orbit model with one oriented cell for each orbit of nonempty simplices.

**2. Exact cellular boundary computation.** Use the integer index \(5i+j\) for \((i,j)\). Enumerate faces in increasing index order by recursively adjoining an allowed vertex and deleting from subsequent choices its graph neighbors. The respective numbers of original faces in dimensions \(0,\ldots,7\) are

\[
(20,150,540,1010,1020,590,200,30).
\]

Choose the lexicographically least translate of each sorted simplex as the quotient representative. The quotient face numbers are

\[
(4,30,108,202,204,118,40,6).
\]

For an oriented representative \([v_0,\ldots,v_k]\), its boundary is the sum over deleted vertices with coefficient \((-1)^a\), multiplied by the orientation parity of the unique translation taking the deleted face to its chosen sorted orbit representative. Uniqueness uses freeness of the action on nonempty faces. The checker constructs these integer matrices explicitly and tests \(\partial_{k-1}\partial_k=0\) for every applicable dimension. In both the original and the quotient complexes it reduces the matrices by unimodular unit-pivot cancellations; for a pivot \(a=\partial_{r,c}=\pm1\), the remaining boundary block is updated using

\[
\partial'_{i,j}=\partial_{i,j}-\partial_{i,c}a^{-1}\partial_{r,j}.
\]

This is a chain-complex cancellation over \(\mathbb Z\), not a numerical rank approximation. The original complex reduces to one generator in dimension zero, two in dimension three, and one in dimension four, with **all differentials zero**, after 1778 unit cancellations. Thus

\[
H_k(X;\mathbb Z)=\begin{cases}\mathbb Z,&k=0,4,\\\mathbb Z^2,&k=3,\\0,&\text{otherwise}.\end{cases}
\]

The quotient complex reduces after 353 unit cancellations to one generator each in dimensions zero, one, two and four and two generators in dimension three. Its sole nonzero remaining differential is multiplication by \(-5\) from dimension two to dimension one. This proves the stated integral homology of \(Y\), including absence of other torsion. As a cross-check on the unreduced boundary matrices, exact sparse Gaussian elimination modulo \(2,3,5,7\) reproduces the predicted Betti ranks, with additional rank-one mod-five homology in dimensions one and two.

**3. Fundamental groups.** The verifier separately constructs the simplicial \(2\)-skeleton presentations. It collapses a maximal tree in each one-skeleton and uses each oriented triangle to impose an edge-word relation. The original complex begins with 131 generators and 540 triangle relations; 131 valid Tietze eliminations leave no generators or relations, so \(\pi_1(X)=1\). The quotient begins with 27 generators and 108 triangle relations; 26 such eliminations leave one generator and the two equivalent relations \(g^5=1\) and \(g^{-5}=1\). Hence \(\pi_1(Y)\cong C_5\), consistently with \(X\to Y\) being a free fivefold universal cover.

**4. Low homotopy and the cup obstruction.** The preceding computations give \(\pi_1(X)=0\) and \(H_2(X;\mathbb Z)=0\). By the degree-two Hurewicz theorem, \(\pi_2(X)=0\), so \(X\) is two-connected and \(\pi_3(X)\cong H_3(X;\mathbb Z)\cong\mathbb Z^2\). Covering spaces identify \(\pi_k(Y)\cong\pi_k(X)\) for \(k\ge2\). Over \(\mathbb Q\), transfer identifies \(H_3(Y;\mathbb Q)\) with the invariants of the deck action on \(H_3(X;\mathbb Q)\). Both spaces have third Betti number two, so the deck action is the identity on the entire rational two-dimensional module. As \(H_3(X;\mathbb Z)\) is free, its integral action is also the identity.

The universal covering is classified by \(f:Y\to BC_5\). The fibration with homotopy fiber \(X\) and the two-connectedness of \(X\) imply that the pullback of \(H^3(BC_5;\mathbb F_5)\) injects into \(H^3(Y;\mathbb F_5)\): no Serre differential can hit its \((3,0)\)-term. The standard group-cohomology ring is \(H^*(BC_5;\mathbb F_5)\cong\Lambda(a)\otimes\mathbb F_5[b]\), with \(|a|=1\), \(|b|=2\), \(b=\beta(a)\), and \(ab\ne0\). Naturality gives \(\alpha=f^*a\), \(\beta(\alpha)=f^*b\), and \(\alpha\smile\beta(\alpha)=f^*(ab)\ne0\). In a wedge of the two-dimensional Moore complex and spheres of dimension at least three, both degree-one and Bockstein classes come from the Moore summand, where their product vanishes. Spheres of smaller dimension would change the integral homology, so no such wedge can be homotopy equivalent to \(Y\).

## Verification

The reproducible, pure-Python integer computation is `check_toroidal_hard_square.py`. Run it with `python3 check_toroidal_hard_square.py` from the same directory; no external dependencies or data files are used. It enumerates all original faces, exact orbit representatives and boundaries, tests all consecutive boundary compositions, performs integer unit-pivot reductions, independently recomputes homology over four finite fields directly from unreduced matrices, and performs explicit fundamental-group Tietze reductions for both spaces. The terminal success marker is `TOROIDAL_HARD_SQUARE_C4_C5_ROTATION_CHECKS_OK`. The Bockstein-cup conclusion is proved by the covering-space and Serre spectral-sequence argument above; the checker does not implement cochain-level cup products.

## Relationship to prior work

Jonsson's 2006 treatment of toroidal hard squares, including the \(4\)-by-\(5\) torus, determines the alternating independent-set count and shows that the original complex's Euler characteristic is zero for coprime circumferences. That does not determine the quotient's integral homology, fundamental group or cup product. Bousquet-Mélou, Linusson and Nevo studied square-grid independence topology with open or cylindric conditions; Adamaszek's 2012 paper gives explicit reductions primarily for cylinders and a separate recursion for the three-row torus. The present quotient is distinct from the previously recorded fivefold cyclic **chessboard**-complex quotient: chessboard faces are partial matchings of a complete bipartite graph, not independent sets of the toroidal grid. Other recorded computations for five-by-five and four-by-seven hard-square grids use different sizes and do not entail these particular quotient or cup-product statements.

## Limitations

The proof classifies the integral homology, first three homotopy groups, deck action on the third, and one nonzero mod-five cup product for precisely the \(4\)-by-\(5\) toroidal grid under column translation. It does **not** give the entire cohomology ring or full homotopy type, nor a general formula for other grid sizes or other symmetry subgroups. Results for other sizes, and a parallel Bockstein obstruction for a different chessboard complex, leave a residual risk of unlocated equivalent work. The computations are finite and exhaustive for this named complex, not evidence for an infinite family.

## References

1. J. Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, Electronic Journal of Combinatorics **13** (2006), R67, DOI: https://doi.org/10.37236/1093 (public 2006-08-07); primary text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r67/pdf/.
2. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the Independence Complex of Square Grids*, arXiv:math/0701890 (first posted 2007-01-30), https://arxiv.org/abs/math/0701890.
3. M. Adamaszek, *Hard Squares on Cylinders Revisited*, arXiv:1202.1655 (first posted 2012-02-08), https://arxiv.org/abs/1202.1655.
