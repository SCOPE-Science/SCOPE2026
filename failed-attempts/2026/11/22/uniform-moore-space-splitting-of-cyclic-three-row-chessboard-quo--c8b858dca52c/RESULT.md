# Uniform Moore-space splitting of cyclic three-row chessboard quotients

## Finding
For every integer \(n\ge5\), let \(X_n=\Delta_{3,n}\) be the ordinary three-row, \(n\)-column chessboard complex: its vertices are board squares \((r,c)\in\{0,1,2\}\times\mathbb Z/n\mathbb Z\), and a face consists of squares with no repeated row or column. Let \(C_n\) act by simultaneously shifting all column coordinates by one. For the **ordinary geometric orbit space** \(Y_n=|X_n|/C_n\), there is a homotopy equivalence
\[
\boxed{Y_n\simeq M(\mathbb Z/n\mathbb Z,1)\vee\bigvee^{n^2-6n+7}S^2.}
\]
Here \(M(\mathbb Z/n\mathbb Z,1)=S^1\cup_{\deg n}D^2\) is the standard two-dimensional Moore space. In particular, the column action is free for every \(n\ge5\), and
\[
\pi_1(Y_n)\cong\mathbb Z/n\mathbb Z,\qquad
\widetilde H_j(Y_n;\mathbb Z)\cong
\begin{cases}\mathbb Z/n\mathbb Z,&j=1,\\
\mathbb Z^{n^2-6n+7},&j=2,\\
0,&\text{otherwise}.
\end{cases}
\]
The result is a **homotopy splitting**, not merely a consequence of Euler characteristic and covering-space homology. Its first instance is \(Y_5\simeq M(\mathbb Z/5\mathbb Z,1)\vee S^2\vee S^2\). The preceding four-column complex is a torus, whose cyclic-column quotient is a Klein bottle [5], so \(n=5\) is the first width in this particular two-dimensional Moore-wedge regime.

## Assumptions and scope
The row labels are fixed under the action; only the column labels are translated. The group order is \(n\), not the symmetric group on columns. The quotient is the geometric orbit space of a free simplicial action, retaining different edges and triangles that share the same row-vertex images. It is naturally a finite \(\Delta\)-complex, **not** the ordinary simplicial complex obtained by identifying each row to one vertex and discarding incidence multiplicities. All homotopy equivalences are nonequivariant equivalences of the quotient spaces. The theorem covers all integers \(n\ge5\), including composite \(n\).

## Proof
**1. Freeness and the precise quotient cells.** If a nonidentity column shift setwise preserved a nonempty simplex, it would send a rook to a second rook in the same row. Every face contains at most one rook per row, so this is impossible. Thus the action on the geometric realization is free. Every vertex orbit is determined by its row: there are three quotient vertices. For each of the three pairs of rows and each nonzero column difference \(d\in\mathbb Z/n\mathbb Z\), there is one edge orbit. There are consequently \(3(n-1)\) quotient edges. A triangle orbit has one square in each row. Shift its row-zero column to zero, and write the remaining columns as \(i,j\in\{1,\ldots,n-1\}\), with \(i\ne j\); hence there are \((n-1)(n-2)\) quotient triangles. All shifts preserve the increasing-row orientation. The quotient has no higher cells.

**2. Exact attaching-word presentation.** Orient all edges from lower to higher row. Write \(a_d\), \(b_d\), and \(c_d\) for the edges from row zero to row one, row zero to row two, and row one to row two, respectively, whose second column is displaced by \(d\) from the first. Here \(1\le d\le n-1\), with indices modulo \(n\). Contract the spanning tree comprising \(a_1\) and \(b_1\), so these two letters represent the identity. The quotient is homotopy equivalent to a CW presentation complex with one vertex, the remaining \(3n-5\) edge letters, and one two-cell for each \(1\le i,j\le n-1\), \(i\ne j\), attached along
\[
\rho_{i,j}=a_i c_{j-i}b_j^{-1}.
\]
This attaching word follows from the boundary of the row-ordered triangle with column triple \((0,i,j)\). Every two-cell is accounted for exactly once.

**3. Homotopy-preserving elimination of all but one loop.** The relators with \(j=1\), \(i\ge2\), each have the form \(a_i c_{1-i}\), allowing elimination of all \(a_i\) with \(i\ge2\). Those with \(i=1\), \(j\ge2\), have the form \(c_{j-1}b_j^{-1}\), allowing elimination of all \(b_j\) with \(j\ge2\). Each elimination removes a single one-cell and the associated two-cell through a homotopy-preserving presentation-complex move (substitute that letter in all remaining attaching maps and cancel the now-free cell pair).

Put \(r=i-1\), \(s=j-1\). The remaining relators, for \(1\le r,s\le n-2\), \(r\ne s\), are
\[
 c_{-r}^{-1}c_{s-r}c_s^{-1}=1.
\]
Write \(t=c_1\) and \(u=c_{n-1}^{-1}\). Taking \(r=1\) and \(s=2,3,\ldots,n-2\) gives \(c_s=u c_{s-1}\). Their two-cells successively eliminate \(c_2,\ldots,c_{n-2}\), yielding \(c_s=u^{s-1}t\). Because \(n\ge5\), both \(c_2\) and \(c_3\) occur in this range. The remaining relator with \((r,s)=(n-2,1)\) is \(c_2^{-1}c_3c_1^{-1}\), which after substitution freely reduces to \(t^{-1}u\). This relator eliminates \(u\), forcing \(u=t\), i.e. \(c_{n-1}=t^{-1}\). In total, \(2(n-2)+(n-3)+1=3n-6\) one-cell/two-cell pairs have been removed, leaving **exactly one** one-cell and \((n-2)(n-4)\) two-cells.

**4. Every surviving attaching degree is zero or \(n\).** The substitutions are now explicit:
\[
 c_k=t^{e(k)},\qquad
 e(k)=\begin{cases}k,&1\le k\le n-2,\\-1,&k=n-1,\end{cases}
\]
where all subscripts are reduced modulo \(n\) into \(1,\ldots,n-1\). A surviving relator from the pair \((r,s)\) is the loop \(t^{E(r,s)}\) with
\[
 E(r,s)=e(s-r)-e(-r)-e(s).
\]
As \(e(k)\equiv k\pmod n\), its exponent is divisible by \(n\). Moreover \(1\le s\le n-2\) and \(-1\le e(k)\le n-2\), so \(-2n+3\le E(r,s)\le n-2\). Consequently **every** exponent is either \(-n\) or zero. The relator \((r,s)=(2,1)\), distinct from every relator already eliminated when \(n\ge5\), has exponent \(-n\) exactly. Thus the surviving attaching-degree vector consists of at least one \(-n\) and otherwise entries in \(\{0,-n\}\).

A CW complex with one circle and \(q\) two-cells attached by integer degrees \((d_1,\ldots,d_q)\) is the homotopy cofiber of a map \(\bigvee^q S^1\to S^1\). Precomposing with Nielsen equivalences of the source wedge realizes elementary unimodular operations on that degree vector without changing the cofiber's homotopy type. Elementary operations therefore reduce the vector \((0,-n,-n,\ldots)\) to \((n,0,\ldots,0)\). Its cofiber is \(M(\mathbb Z/n\mathbb Z,1)\vee\bigvee^{q-1}S^2\). Since \(q=(n-2)(n-4)\), the number of spheres is \(q-1=n^2-6n+7\), as asserted. This also proves every group statement in the Finding without relying on numerical experiments.

## Verification
`verification/verify.py` is a standalone Python 3 standard-library checker. For each width \(5\le n\le100\), it verifies the exact algebraic relator indices, the remaining two-cell count, and that every surviving attaching degree belongs to \(\{0,-n\}\) with at least one \(-n\). For widths five through ten it additionally enumerates **all original nonattacking rook faces**, checks that every nonempty face orbit has exactly \(n\) members, constructs the two signed quotient boundary matrices, verifies \(\partial_1\partial_2=0\), and checks their finite-field ranks for five characteristics. Execute with `python3 verification/verify.py`; its final line is `THREE_ROW_CYCLIC_QUOTIENT_CHECKS_OK`. These bounded computations independently stress-test the definitions; the infinite family follows from Proof steps 1–4, not from extrapolation.

## Relationship to prior work
Friedman and Hanlon [1] compute rational Betti numbers of ordinary chessboard complexes, and Shareshian and Wachs [2] develop integral homology and connectivity methods. Neither inspected primary text establishes the homotopy type of **cyclic-column geometric quotients**. Prior work on the three-by-four torus and its column-subgroup quotients [5] covers only the immediately preceding width. Work on four-by-five and five-by-five cyclic-column quotients [3,4] finds, respectively, a nontrivial Bockstein product in dimension three and mixed-prime homology; those spaces have different row counts and do not imply the present two-dimensional splitting. The column-rotation quotient of *capacity-two* three-row matching complexes [6] has fundamentally different higher-dimensional cells and torsion. Generic covering-space arguments and the old connectivity results would yield the fundamental group and integral Betti numbers, but **not** the displayed Moore-space wedge decomposition; that additional homotopy statement comes from the explicit uniformly valid two-cell eliminations above.

## Limitations
No equivariant homotopy classification of the covering complexes and no description of arbitrary column-subgroup or full symmetric-group quotients is asserted. The precise splitting is for three rows and the full cyclic column shift at widths at least five. An independently discovered equivalent splitting or a broad previously unindexed presentation-complex theorem might cover it; database searches and inspected relevant literature cannot establish absolute publication priority. The included finite checker is not offered as an infinite-dimensional or all-width proof, and no independent scientific audit has been performed.

## References
1. J. Friedman and P. Hanlon, *On the Betti Numbers of Chessboard Complexes* (PDF dated 1997-05-14), Sections 1–3, https://www.cs.ubc.ca/~jf/pubs/web_stuff/newchess.pdf.
2. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, first public posting 2004-09-03, especially Theorem 1.1 and introduction, https://arxiv.org/pdf/math/0409054.
3. *A nontrivial mod-five Bockstein cup product in the cyclic chessboard quotient*, repository record `2026/10/25/SCOPE-a-nontrivial-mod-five-bockstein-cup-product-in-the-cyclic-chessb--19b7184f8768`, https://github.com/published-finding corpus/2026/.
4. *Mixed-prime homology and a purely modular symmetry class in a cyclic chessboard quotient*, repository record `2026/10/25/SCOPE-mixed-prime-homology-and-a-purely-modular-symmetry-class-in-a-cy--4a438b4ca94c`, https://github.com/published-finding corpus/2026/.
5. *All column-symmetry quotients of the three-by-four chessboard torus: six surface types*, repository record `2026/11/8/SCOPE-all-column-symmetry-quotients-of-the-3-times4-chessboard-torus-s--36c320104144`, https://github.com/published-finding corpus/2026/.
6. *Cyclic quotient torsion and the parity threshold for three-row two-matching complexes*, repository record `2026/10/18/SCOPE-cyclic-quotient-torsion-and-the-parity-threshold-for-three-row-t--e5952a573c96`, https://github.com/published-finding corpus/2026/.
