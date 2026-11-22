# Two order-two classes in the four-by-four bishop symmetry quotient

## Finding
For an ordinary nonperiodic four-by-four chessboard, let \(\mathcal B_4\) be the simplicial complex of all pairwise nonattacking bishop placements. Let \(D_4\) be the group of all eight rotations and reflections of the square. For the *ordinary geometric quotient* \(Y=|\mathcal B_4|/D_4\),
\[
\pi_1(Y)=1,\qquad
\widetilde H_j(Y;\mathbb Z)\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^2,&j=2,\\
\mathbb Z,&j=3,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, a quotient of a space previously known to have torsion-free homology has two independent degree-two order-two torsion classes. This is an integral homology and fundamental-group classification, **not** a determination of the complete homotopy type.

## Assumptions and scope
The sixteen squares have coordinates \((r,c)\), \(0\le r,c\le3\). Distinct bishops at \((r,c)\) and \((u,v)\) attack precisely when \(|r-u|=|c-v|\). Every valid nonempty set of squares is a simplex; the empty face is included. The full dihedral group acts by Euclidean board symmetries, with no periodic identifications. The quotient is the topological orbit space of the geometric realization, not a quotient of the graph or the naive face-orbit poset.

The prior nonequivariant classification gives \(|\mathcal B_4|\simeq\bigvee^9 S^3\) (see the third reference). It alone cannot determine the integral homology of the orbit space.

## Proof
**A correct regular quotient cell structure.** Barycentrically subdivide \(\mathcal B_4\). Its simplex vertices are nonempty faces of the original complex, and each simplex is a strict inclusion flag \(F_0\subsetneq\cdots\subsetneq F_k\). Every stabilizer of such a flag fixes each face individually because their cardinalities are distinct; therefore it fixes the entire barycentric simplex pointwise. Consequently the orbits of barycentric flags form a regular CW decomposition of \(Y\). Its cellular boundary is computed by deleting the \(i\)-th flag vertex with coefficient \((-1)^i\). Different deletions have different sets of face cardinalities and hence cannot be identified by the group, so these incidence coefficients really are units.

Exhaustive generation from the coordinate attack rule produces 728 nonempty original faces, with numbers by size \(1,\ldots,6\) equal to \((16,92,232,260,112,16)\). There are exactly 158,328 nonempty barycentric flags. Canonicalizing flags under the eight actual square permutations yields the quotient-cell vector (dimensions \(0,\ldots,5\))
\[
(100,1210,4530,7260,5280,1440).
\]
An independent Burnside calculation counts group-fixed inclusion flags recursively and reproduces every entry of this vector. Its alternating sum is zero.

**Topological reduction and exact integral chains.** The embedded checker constructs every flag orbit, each boundary face, and all immediate coface incidences. It removes 9,064 actual elementary free-face pairs, checking at each step that the larger regular cell is maximal and the smaller is incident to exactly one such cell. The resulting deformation retract has cell vector \((60,419,786,427)\) in dimensions \(0\) through \(3\), with no higher-dimensional cells. Direct signed boundary multiplication verifies \(\partial^2=0\).

On this retract, exact unimodular unit-pivot reductions cancel 59 pairs in degrees \((1,0)\), 360 pairs in degrees \((2,1)\), and 424 pairs in degrees \((3,2)\). Each pivot is checked to be \(\pm1\). At every cancellation, the remaining columns are updated by integral elementary operations and both neighboring differentials are updated, so integral homology is preserved. The final chain complex has \(C_0\cong\mathbb Z\), \(C_1=0\), \(C_2\cong\mathbb Z^2\), \(C_3\cong\mathbb Z^3\), and no higher terms. Up to basis order and signs its only nonzero differential has matrix
\[
\partial_3=\begin{pmatrix}2&4&0\\0&2&0\end{pmatrix},
\]
whose Smith invariant factors are \(2,2\). This proves the complete claimed integral homology. Independent finite-field rank calculations on the *pre-algebraic-reduction* cellular complex give boundary ranks \((59,360,424)\) over \(\mathbb F_2\) and \((59,360,426)\) over each of \(\mathbb F_3,\mathbb F_5\), agreeing with the result.

**Fundamental group.** Bishop attacks preserve the parity of \(r+c\), so the original complex splits as the simplicial join of its two eight-square color subcomplexes. Each color subcomplex is path connected: the nonattacking-pair one-skeleton connects all eight squares (verified by exhaustive adjacency traversal). The join of two path-connected complexes is simply connected. Apply the standard finite-group orbit-space fundamental-group theorem to the action on this connected, simply connected finite complex: \(\pi_1(Y)\cong D_4/N\), where \(N\) is generated normally by elements having fixed points in the realization. The reflection \((r,c)\mapsto(c,r)\) fixes the square \((0,0)\). The reflection \((r,c)\mapsto(3-r,c)\) fixes the midpoint of the allowed bishop-placement edge \(\{(0,0),(3,0)\}\). These two reflections generate \(D_4\), hence \(N=D_4\) and \(\pi_1(Y)=1\).

## Verification
Run `python3 verify_bishop4_quotient.py` with a standard Python 3 interpreter. It has no external package, network, saved-state, or randomness dependencies. It reconstructs the attack graph, checks all eight symmetries, enumerates all faces and inclusion flags, checks Burnside orbit counts independently, verifies every topological collapse, checks the integer chain identities, computes ranks over three finite fields on the unreduced differential, performs exact unit-pivot contractions, and checks the residual integral Smith reduction. The captured `verification_output.txt` ends in the exact marker `BISHOP4_D4_INTEGRAL_QUOTIENT_OK` as its opening line.

## Relationship to prior work
Clark and Zeckner (arXiv:1008.4525, first publicly posted August 26, 2010) study Ferrers-board rook complexes and the triangular Stirling complex, including homotopy and homology of specific shapes. Each bishop-color independence complex can be understood as a rook-placement complex on a diagonal-incidence board, but the cited work does not give integral homology of a square-dihedral quotient interchanging the two colors. Its triangular-board theorems do not cover this symmetry-quotient statement.

Harris, Perkins, Roach and Jones (2013) analyze bishop independence *numbers*, including ordinary rectangular boards and other surface boundary conditions. The full article's results are extremal counts, not homology of spaces of all placements and not quotients of those spaces.

A previously published finite-board calculation gives \(\mathcal B_4\simeq\bigvee^9 S^3\), which is credited rather than repeated as a discovery. This nonequivariant statement does not determine the quotient's integral two-torsion. Adamaszek's 2015 results concern dismantling and homotopy for chordal-graph independence complexes, not arbitrary symmetry-quotient homology; the bishop attack graph has induced four-cycles and is not chordal. Standard general results on finite-group quotients and Smith normal forms are used as tools, not claimed as new.

## Limitations
The result applies exactly to the ordinary four-by-four board and full eight-element geometric symmetry group. No homotopy equivalence to a proposed wedge of Moore spaces is asserted from the chain reduction: algebraic unit cancellation establishes homology, not automatically a homotopy-preserving CW cancellation. The calculation is exhaustive for this finite complex and includes reproducible code, not a proof of a pattern for all even boards. No independent mathematical audit has been performed. Unindexed equivalent research and stronger results not encountered during the documented comparison remain possible.

## References
1. E. Clark and M. Zeckner, *Simplicial Complexes of Triangular Ferrers Boards*, arXiv:1008.4525v1, posted 2010-08-26, https://arxiv.org/abs/1008.4525.
2. L. H. Harris, S. Perkins, P. A. Roach and S.-K. Jones, *Bishop Independence*, British Journal of Mathematics and Computer Science 3 (2013), 835–843, published 2013-09-05, https://doi.org/10.9734/BJMCS/2013/5760.
3. *A mixed-dimensional homotopy transition in even-board bishop complexes*, 2026 record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-mixed-dimensional-homotopy-transition-in-even-board-bishop-com--5a9e9824a08d.
4. M. Adamaszek, *A note on independence complexes of chordal graphs and dismantling*, arXiv:1508.02426v1, posted 2015-08-10, https://arxiv.org/abs/1508.02426.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
6. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301.
