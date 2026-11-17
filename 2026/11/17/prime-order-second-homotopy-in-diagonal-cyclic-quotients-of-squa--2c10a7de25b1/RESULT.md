# Prime-order second homotopy in diagonal cyclic quotients of square chessboard complexes

## Finding
For every odd prime \(p\ge5\), let \(K_p=\mathcal M(K_{p,p})\) be the chessboard complex of nonattacking rook placements on the square board with row and column sets \(\mathbb Z/p\mathbb Z\). The simultaneous cyclic translation \(t(i,j)=(i+1,j+1)\) acts simplicially. For the **ordinary geometric orbit space** \(X_p=|K_p|/\langle t\rangle\), one has

\[
\pi_1(X_p)=0,\qquad
\pi_2(X_p)\cong H_2(X_p;\mathbb Z)\cong
\begin{cases}
\mathbb Z/3\mathbb Z\oplus(\mathbb Z/5\mathbb Z)^4,&p=5,\\
(\mathbb Z/p\mathbb Z)^{p-1},&p\ge7\text{ prime}.
\end{cases}
\]

Thus a natural simply connected symmetry quotient has arbitrarily large prime-order second homotopy: for each prime \(p\ge7\), the covering chessboard complex has \(H_2=0\), yet its quotient has \(p-1\) independent order-\(p\) classes. The extra \(\mathbb Z/3\) summand at \(p=5\) comes from the known intrinsic three-torsion of the five-by-five chessboard complex.

## Assumptions and scope
A simplex of \(K_p\) is a nonattacking rook placement, i.e. a set of distinct cells \((i,j)\) with no repeated first or second coordinate. The cyclic group has prime order \(p\) and acts by simultaneously adding one modulo \(p\) to both coordinates. The quotient is the topological quotient of the geometric realization, not a quotient of vertex sets, and not the Borel or homotopy orbit space. The first two homotopy groups use any basepoint; basepoint changes are immaterial because the quotient is path connected and simply connected. Integral homology means ordinary singular homology.

The source results used, rather than reproved, are the classical chessboard connectivity theorem and the established integral result \(H_2(K_5;\mathbb Z)\cong\mathbb Z/3\mathbb Z\). For \(p\ge7\), the connectivity bound directly gives \(H_2(K_p;\mathbb Z)=0\). These are statements about the **unquotiented** complexes, and are not claimed as new.

## Proof
**1. All geometric fixed points.** Every board square has a translation orbit of size \(p\). The orbits are precisely
\[
F_a=\{(i,i+a):i\in\mathbb Z/p\mathbb Z\},\qquad a\in\mathbb Z/p\mathbb Z.
\]
Each \(F_a\) is a perfect matching, hence a maximal \((p-1)\)-simplex. If a point of \(|K_p|\) is fixed by a nonidentity translation, its positive barycentric support is an invariant nonempty matching. Since \(p\) is prime, the support must contain an entire vertex orbit of size \(p\). Every matching has at most \(p\) vertices, so its support is exactly one \(F_a\), and invariance of barycentric coefficients forces the point to be its barycenter. Conversely, those \(p\) barycenters are fixed. No other point has nontrivial isotropy.

**2. Local links.** Choose mutually disjoint small invariant closed balls \(B_a\) about the barycenters, contained in the interiors of their maximal simplices. In barycentric coordinates, the action on the tangent space to the simplex is the real reduced permutation representation
\[
V=\{(x_0,\ldots,x_{p-1})\in\mathbb R^p:\sum x_i=0\},
\]
with the \(p\)-cycle permuting coordinates. As a real representation it is the direct sum of complex rotation characters with weights \(1,2,\ldots,(p-1)/2\). Every nonidentity group element acts without fixed vectors on \(V\setminus\{0\}\), so the sphere \(S(V)\cong S^{p-2}\) has a free \(C_p\)-action. Its quotient \(L_p=S(V)/C_p\) is a generalized lens space of dimension \(p-2\ge3\), and
\[
\pi_1(L_p)\cong H_1(L_p;\mathbb Z)\cong\mathbb Z/p\mathbb Z,
\qquad H_2(L_p;\mathbb Z)=0.
\]
The local ball quotient is a cone on \(L_p\).

**3. The free complement.** Let \(U_p\) be the complement of the interiors of the \(p\) chosen balls and write \(Y_p=U_p/C_p\). Removal of those balls does not change \(\pi_1\) or \(H_2\), because the relative groups \(H_j(|K_p|,U_p;\mathbb Z)\) vanish for \(j<p-1\), and attaching/removing cells of dimension at least four does not change fundamental groups. By the chessboard connectivity theorem, \(|K_p|\) is simply connected. Therefore \(U_p\) is simply connected and \(U_p\to Y_p\) is a universal \(p\)-fold covering with
\[
\pi_1(Y_p)\cong H_1(Y_p;\mathbb Z)\cong C_p.
\]
Moreover,
\[
H_2(U_p;\mathbb Z)\cong H_2(K_p;\mathbb Z)=T_p,
\qquad T_p=\begin{cases}\mathbb Z/3\mathbb Z,&p=5,\\0,&p\ge7.\end{cases}
\]
The integral Cartan–Leray spectral sequence for the free action has \(E^2_{a,b}=H_a(C_p;H_b(U_p;\mathbb Z))\). In total degree two, \(H_1(U_p)=0\) and \(H_2(C_p;\mathbb Z)=0\). Thus the sole possible term is \(H_0(C_p;T_p)\). The action on \(T_5=\mathbb Z/3\) is trivial since an order-five automorphism of \(\mathbb Z/3\) must be the identity; other \(T_p\) vanish. The only possible incoming differential to this term, from \(H_3(C_p;\mathbb Z)\cong C_p\), must vanish because its target is zero or a group of order three, coprime to \(p\). It follows that
\[
H_2(Y_p;\mathbb Z)\cong T_p.
\]

**4. Coning off the lens links.** The space \(X_p\) is obtained from \(Y_p\) by adjoining a cone on each of its \(p\) boundary components \(L_p\). For each component, the map \(\pi_1(L_p)\to\pi_1(Y_p)\) is an isomorphism: pull back the universal cover \(U_p\to Y_p\) to that component, obtaining the connected universal sphere covering \(S^{p-2}\to L_p\) with the same deck group \(C_p\). Van Kampen therefore yields \(\pi_1(X_p)=0\).

Mayer–Vietoris, using \(H_2(L_p)=0\) and contractibility of every cone, gives an exact sequence
\[
0\longrightarrow T_p\longrightarrow H_2(X_p;\mathbb Z)
\longrightarrow (\mathbb Z/p\mathbb Z)^p
\overset{\varphi}{\longrightarrow}\mathbb Z/p\mathbb Z
\longrightarrow 0.
\]
Every coordinate map of \(\varphi\) is an isomorphism (up to multiplication by a unit) because it is induced by the corresponding link inclusion on fundamental groups. Consequently \(\varphi\) is surjective and \(\ker\varphi\cong(\mathbb Z/p\mathbb Z)^{p-1}\). If \(p\ge7\), then \(T_p=0\) and this determines \(H_2(X_p)\). If \(p=5\), there is a short exact sequence with kernel \(\mathbb Z/3\) and quotient \((\mathbb Z/5)^4\); it splits as an abelian-group extension because its primary components have coprime orders. Finally, \(X_p\) is simply connected, so the degree-two Hurewicz isomorphism identifies \(\pi_2(X_p)\) with \(H_2(X_p;\mathbb Z)\). This establishes the complete claim for all odd primes at least five.

## Verification
Two independent standard-library Python programs accompany this result. `verify.py` exhaustively generates the nonempty chessboard faces for \(p=5\) and \(p=7\), verifies the expected face counts, and checks that exactly the \(p\) complete translation orbits are invariant, with none in smaller dimensions. It also checks the reduced-representation weight list and orbit Euler characteristics. `check_modular.py` independently builds the barycentric-subdivision quotient flag-complex chain groups for \(p=5\) (313, 3200, 8640, 8640 cells in dimensions zero through three) and computes boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). It finds \(H_1=0\) over all three fields and \(\dim H_2=(0,1,4)\), respectively, agreeing with the claimed integral groups. The universal-prime theorem rests on the preceding topological proof, not on extrapolation from those finite tests.

## Relationship to prior work
Shareshian and Wachs prove the classical connectivity bound and the intrinsic three-torsion result; Jonsson gives a computer-free derivation of the five-by-five \(\mathbb Z/3\) group. These apply to the unquotiented chessboard complex. A published result on **column-only** fivefold translation computes a free cyclic quotient with nontrivial \(H_1\); the present action translates **both** rows and columns and has isolated fixed points, producing a simply connected quotient with new \(p\)-torsion in \(H_2\). A result classifying fixed-point sets under transitive side-preserving bipartite symmetries encompasses the count of \(p\) fixed points, but does not determine local lens links, quotient fundamental groups, or second homotopy groups. A transpose quotient concerns a different group and a three-local invariant. None of these inspected statements implies the displayed prime-uniform quotient calculation.

## Limitations
No homotopy groups above degree two, full integral homology in higher degrees, cohomology ring, or composite-board-size analogue is determined. The local lens spaces are used only through their low-dimensional homology and fundamental group. Finite computations for \(p=5,7\) corroborate but do not certify infinitely many prime cases. Publication priority outside inspected and indexed literature remains open.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first public arXiv version 2004-09-03, arXiv:math/0409054v1, especially Theorems 1.1 and 1.7, Table 1.2. https://arxiv.org/html/math/0409054v1
2. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644v1, publicly posted 2012-03-26, especially Section 3. https://arxiv.org/abs/1203.5644
3. *Mixed-prime homology and a purely modular symmetry class in a cyclic chessboard quotient*, published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-mixed-prime-homology-and-a-purely-modular-symmetry-class-in-a-cy--4a438b4ca94c
4. *Transitive bipartite symmetry forces discrete geometric matching-complex fixed spaces*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-transitive-bipartite-symmetry-forces-discrete-geometric-matching--8fda4c3956ce
5. *Three-local torsion cancellation in the transpose quotient of the five-by-five chessboard complex*, published research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-local-torsion-cancellation-in-the-transpose-quotient-of-th--62667cf31b8c
