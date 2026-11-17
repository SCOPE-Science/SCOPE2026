# Quarter-turn fixed chessboard complexes and the sharp emergence of integral three-torsion

## Finding

Let \(\Delta_{n,n}\) be the classical simplicial chessboard complex of nonattacking rook placements on an \(n\)-by-\(n\) board, and let \(\rho(i,j)=(j,n-1-i)\) be the quarter-turn of the board. For \(m\geq0\), let \(M_m\) denote the matching complex of the complete graph on \(m\) labeled vertices, and \(\operatorname{Infl}_2(M_m)\) its twofold vertex inflation: each matching edge has two mutually exclusive copies. The geometric quarter-turn fixed-point spaces satisfy the following exact PL classifications:
\[
|\Delta_{2m,2m}|^{\langle\rho\rangle}\cong_{\mathrm{PL}}|\operatorname{Infl}_2(M_m)|\quad(m\geq1),
\]
\[
|\Delta_{2m+1,2m+1}|^{\langle\rho\rangle}\cong_{\mathrm{PL}}|\operatorname{Cone}(\operatorname{Infl}_2(M_m))|\quad(m\geq0).
\]
For \(m=0,1\), the inflation has no vertices; its augmented empty-face complex is used so that its cone is one point. The even-board fixed set is empty when \(m=1\) and otherwise has the stated ordinary realization.

**Sharp integral-torsion threshold.** For every \(1\leq n<14\), the quarter-turn geometric fixed space has torsion-free integral homology, including the empty fixed space at \(n=2\). At \(n=14\), the first torsion occurs, with precisely
\[
\widetilde H_1(|\Delta_{14,14}|^{\langle\rho\rangle};\mathbb Z)\cong\mathbb Z/3\mathbb Z,\qquad
\widetilde H_2(|\Delta_{14,14}|^{\langle\rho\rangle};\mathbb Z)\cong\mathbb Z^{461}.
\]
All other reduced integral homology groups of this fourteen-board fixed space vanish. The classification of geometric fixed spaces holds for every board order, not just the finite cutoff.

## Assumptions and scope

Rows and columns are indexed by \(0,\dots,n-1\). A face of \(\Delta_{n,n}\) is a subset of board squares with no two in a common row or column. The group acts by permuting simplicial vertices, but its fixed points are taken in the **geometric realization**, which can include orbit barycenters and is not merely the subcomplex on individually fixed squares. Twofold inflation means a face selects at most one of two copies of each edge of \(K_m\), and the underlying chosen edges must form a matching. Reduced integral homology is meant in nonnegative degrees; the empty geometric realization at board order two has no nonnegative homology.

The first source date is February 1, 1994, the verified original publication of the foundational chessboard-complex paper, not a modern revision or later paper's publication date. The structural inflation theorem and the integral matching-complex homology below are established prior results, explicitly not claimed as new.

## Proof

**1. Orbit-barycenter triangulation.** Let a finite simplicial complex \(X\) admit an action by a finite group \(G\) permuting its vertices. Form the orbit complex whose vertices are orbits \(O\) that themselves are faces of \(X\); its faces are collections of these orbits whose unions are faces of \(X\). Every geometrically fixed point of \(|X|\) has a unique invariant set of barycentric coordinates; the coordinate is constant on each group orbit. Each admissible orbit thus contributes its orbit-barycenter with the total weight of its original vertices. On each invariant simplex this gives an affine homeomorphism to the simplex spanned by orbit-barycenters, compatible across simplex intersections; its inverse distributes each orbit weight equally over the original vertices. Therefore this orbit complex is PL-homeomorphic to \(|X|^G\). This construction includes geometric fixed points that are not original vertices.

**2. Classification of quarter-turn orbits.** Let \(\bar i=n-1-i\), and call \(\{i,\bar i\}\) an antipodal pair of row or column labels. A quarter-turn orbit of a square \((i,j)\) is
\[
O(i,j)=\{(i,j),(j,\bar i),(\bar i,\bar j),(\bar j,i)\},
\]
with repeated elements removed. If \(n\) is odd, \((m,m)\) is the unique singleton orbit; all remaining orbits have four squares. If \(n\) is even, all orbits have four squares. A four-square orbit is a nonattacking rook placement if and only if the four indices \(i,j,\bar i,\bar j\) are distinct. Equivalently, \(i\) and \(j\) belong to **two different** noncentral antipodal pairs. This rules out in particular all orbits lying on a central row or column in an odd board.

For each unordered pair \(\{A,B\}\) of distinct noncentral antipodal label-pairs, there are four possible square choices \((i,j)\) with \(i\in A\), \(j\in B\). Taking the quarter-turn orbits identifies these choices in pairs; hence exactly **two** distinct admissible orbits correspond to \(\{A,B\}\). The choice of the first versus second is a two-color label; its naming is immaterial. The rows occupied by an admissible orbit are exactly \(A\cup B\), and so are its columns. Consequently two distinct admissible orbit vertices can coexist precisely when their underlying antipodal-pair edges are disjoint. This is the defining face condition of \(\operatorname{Infl}_2(M_m)\).

For an even board this exhausts the admissible orbits, proving the first PL identification. For an odd board the central singleton orbit is compatible with every other admissible orbit, and there are no additional admissible orbits. The orbit complex is therefore the simplicial cone on \(\operatorname{Infl}_2(M_m)\), proving the second PL identification and contractibility for all odd board orders.

**3. Existing inflation theorem and integral splitting.** Björner–Wachs–Welker, Theorem 6.2 and Corollary 6.3, compute the homotopy and integral homology of a vertex-inflated simplicial complex. For connected \(M_m\), here \(m\geq5\), their twofold case gives a nonequivariant homotopy decomposition
\[
|\operatorname{Infl}_2(M_m)|\simeq|M_m|\ \vee\!\bigvee_{r=1}^{\lfloor m/2\rfloor}\ \bigvee^{\frac{m!}{2^r r!(m-2r)!}}\Sigma^r|M_{m-2r}|,
\]
where for the empty matching complex on zero or one graph vertices, suspension is interpreted using the usual augmented simplicial convention. An \(r\)-edge matching has link \(M_{m-2r}\), and its inflation multiplicity is \((2-1)^r=1\), which proves this specialization of the cited theorem. The integral homology direct-sum formula remains valid even for disconnected small bases, by the cited Corollary 6.3.

**4. Exact threshold and ranks.** For \(m\leq6\), every matching complex \(M_{m-2r}\) appearing in this decomposition has torsion-free integral homology: \(M_2\) is one point, \(M_3\) consists of three isolated points, \(M_4\) of three contractible components, while \(M_5\) and \(M_6\) are graphs up to homotopy, with ranks six and sixteen in degree one. The augmented complexes on zero or one vertices contribute only conventional free rank-one terms. The integral splitting therefore gives torsion-freeness for every even board smaller than fourteen. Combined with contractibility on all odd boards this proves the lower cutoff.

For \(m=7\), the established exact integral homology is \(\widetilde H_1(M_7;\mathbb Z)=\mathbb Z/3\mathbb Z\) and \(\widetilde H_2(M_7;\mathbb Z)=\mathbb Z^{20}\). It appears both in the earlier matching-complex torsion literature and by an explicit integral computation in Mondal–Mukherjee–Saha. Every nonempty-matching summand is a two-sphere wedge, with multiplicity
\[
\binom72\cdot6+\frac{7!}{2^2\,2!\,3!}\cdot2+\frac{7!}{2^3\,3!\,1!}
=21\cdot6+105\cdot2+105=441.
\]
Indeed the one-edge links are \(M_5\simeq\bigvee^6 S^1\); the two-edge links are \(M_3\simeq\bigvee^2S^0\); and the three-edge links contain only the augmented empty face, whose third suspension is \(S^2\). Thus the inflation adds exactly \(441\) degree-two free generators to the original \(20\), without changing its degree-one torsion. This yields the displayed \(\mathbb Z^{461}\) and \(\mathbb Z/3\mathbb Z\), and proves vanishing of every other reduced group.

## Verification

The standalone program `verify.py` (Python 3.10 or newer; SymPy 1.14 for exact integer Smith forms) independently constructs original board-square orbits, tests whether each is a nonattacking placement, verifies the face compatibility against the two-color matching model, and computes face counts for every board size \(1\leq n\leq14\). At \(n=14\), it gives 42 fixed-orbit vertices and face counts \((42,420,840)\) in dimensions zero through two. On the **un-inflated** matching complex \(M_7\), it produces face counts \((21,105,105)\), augmented integer boundary ranks \((1,20,85)\), and precisely one nonunit Smith invariant factor, equal to three. The direct Smith computation corroborates the published integral result, independently of field-only rank calculations. Corresponding small-complex Smith forms for \(2\leq m\leq6\) have exclusively unit nonzero factors.

Run `python verify.py` with SymPy installed; exact recorded output is `verification_output.txt`, ending in `QUARTER_TURN_CHESSBOARD_EXACT_CHECK_PASS`. These are finite computations and do **not** prove the uniform PL identification for all board orders: that is established by the explicit orbit argument above. They also do not substitute for the published general inflation theorem.

## Relationship to prior work

The classical papers of Björner–Lovász–Vrećica–Živaljević and Shareshian–Wachs establish the underlying chessboard and matching complexes, their connectivity and matching-complex torsion. Björner–Wachs–Welker establish the **general** homotopy splitting for vertex inflations, including its integral homology consequence. These established results determine the homology **after** the new geometric quarter-turn identification, so no new inflation theorem or new calculation of \(M_7\) homology is claimed. The specific comparison is the identification of the genuine geometric quarter-turn fixed spaces with a **twofold** inflation of complete-graph matching complexes, and the resulting sharp **board-size** torsion threshold.

Published indexed fixed-space examples for chessboard complexes under **transposition** of rows and columns have different orbit types and yield torsion-free sphere wedges; they do not imply the quarter-turn identification. Another indexed result concerns the **fourfold** inflation of \(M_7\) arising as a doubled cross-polytope boundary, which shares the underlying \(M_7\) torsion but is not a quarter-turn fixed chessboard. The literature comparisons distinguish the actual group action, ambient simplicial complex, inflation multiplicity, and final fixed-space conclusions. An older equivalent under terminology such as rotational rook configurations remains a genuine originality risk.

## Limitations

The uniform statement is a PL classification of geometric fixed spaces under the subgroup generated by one quarter-turn; it is not a classification of every subgroup action, their restriction maps, or the full equivariant homotopy type of the chessboard complex. The fourteen-board integral homology result relies on the published inflation theorem and established matching-complex homology, with independent finite checks provided. It does not assert a wedge-of-spheres homotopy decomposition of \(M_7\) (which has torsion), and it does not determine integral homology at every larger even board order in closed form. An equivalent unindexed prior publication cannot be ruled out. No independent audit has been performed.

## References

1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society **49** (1994), 25–39. First public February 1, 1994. https://doi.org/10.1112/jlms/49.1.25.
2. A. Björner, M. Wachs and V. Welker, *Poset Fiber Theorems*, Theorem 6.2 and Corollary 6.3, dated July 25, 2002; published in Transactions of the AMS. https://www.math.miami.edu/~wachs/papers/fibers.pdf.
3. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first posted September 3, 2004. https://arxiv.org/abs/math/0409054.
4. R. Mondal, S. Mukherjee and K. Saha, *Topology of Matching Complexes of Complete Graphs via Discrete Morse Theory*, arXiv:2305.02973, first posted May 4, 2023, including an integral \(M_7\) calculation. https://arxiv.org/abs/2305.02973.
