# One missing hypercube bond creates six-cycles or four-cycles in binary parity dynamics

## Finding

Let \(d\ge2\), \(Q=2^f\) with \(f\ge1\), and \(N=2^d\). Delete any one edge of the ordinary \(d\)-dimensional Boolean cube and let \(B\) synchronously replace the value at every vertex with the sum of its surviving neighbors over \(\mathbb F_Q\). All deleted edges are equivalent under cube automorphisms. The complete Jordan structure is

\[
\begin{array}{ll}
\text{even }d:&B\sim J_2(0)^{\oplus(N/2-2)}\oplus C,\quad
\chi_C(t)=m_C(t)=(t^2+t+1)^2;\\
\text{odd }d:&B\sim J_1(0)^{\oplus2}\oplus J_4(1)
\oplus J_2(1)^{\oplus(N-6)/2}.
\end{array}
\]

Here \(J_j(\lambda)\) is one size-\(j\) Jordan block, and \(C\) is four-dimensional with exact multiplicative order six. For even \(d\), the nilpotent Jordan summand has dimension \(N-4\), and the recurrent subsystem has dimension four; for odd \(d\), these dimensions are two and \(N-2\), respectively. The former all-zero two-block sum is empty for \(d=2\). The sharp maximum first-periodic-entry times are respectively \(0\) at \(d=2\), \(2\) at even \(d\ge4\), and \(1\) at odd \(d\ge3\). The sharp maximum eventual least periods are six and four in the two parity cases.

The exact joint census is particularly simple. For even \(d\), put \(a=N/2-2\). The counts by first-periodic-entry times \(0,1,2\) are
\[
(E_0,E_1,E_2)=(1,Q^a-1,Q^{2a}-Q^a),
\]
while the counts by primitive eventual periods \(1,3,6\) in the invertible component are
\[
(P_1,P_3,P_6)=(1,Q^2-1,Q^4-Q^2).
\]
For odd \(d\), the counts by entry times \(0,1\) are \((1,Q^2-1)\); the recurrent-component period counts for \(1,2,4\) are
\[
(P_1,P_2,P_4)=(Q^{(N-4)/2},\ Q^{N-4}-Q^{(N-4)/2},\ Q^{N-2}-Q^{N-4}).
\]
For either parity, the number of configurations with entry time \(i\) and eventual least period \(j\) is exactly \(E_iP_j\). All populations include labelled vertex assignments, not symmetry-orbit counts. In particular, one missing edge turns the even-dimensional cube's originally nilpotent parity update (all states vanish in at most two steps) into a system with primitive six-cycles, and raises the maximal period of odd-dimensional cubes from two to four.

## Assumptions and scope

The graph is the simple unweighted Cartesian product \(K_2^{\square d}\) minus exactly one undirected edge. The field has characteristic two, and the update is ordinary simultaneous open-neighbor summation, without self-loops. All claims hold for every integer \(d\ge2\) and every integer field extension degree \(f\ge1\). A state is first periodic at time \(s\) if \(s\) is the least nonnegative integer such that \(B^s x\) belongs to some periodic orbit. Its eventual least period is the least positive \(p\) with \(B^{s+p}x=B^sx\). The zero vector has period one. A Jordan decomposition over \(\mathbb F_Q\) is asserted in odd dimensions. In even dimensions, the degree-two factor may be irreducible over \(\mathbb F_Q\); thus the operator \(C\) is specified by its characteristic/minimal polynomials, not by a potentially nonexistent decomposition into field-rational eigenvalue blocks.

## Proof

Write \(A\) for the cube adjacency before removing an edge and \(E\) for the adjacency of the removed single edge, so \(B=A+E\) in characteristic two. Each cube coordinate flip is an involution commuting with the others. Hence \(A^2=dI\), where the integer \(d\) is reduced modulo two. Cube bipartition gives \(A=\left(\begin{smallmatrix}0&H\\H^T&0\end{smallmatrix}\right)\), where \(H\) is an \(m\times m\) binary matrix and \(m=N/2\). Let \(u\) and \(v\) denote the deleted edge's even and odd endpoints (also their coordinate vectors). Deleting that edge replaces \(H\) by \(H'=H+uv^T\). We may assume the removed edge connects the zero word to a coordinate unit word.

**Even \(d\).** Now \(HH^T=H^TH=0\). Since \(Q_d=K_2\square Q_{d-1}\), with \(d-1\) odd, a two-by-two block presentation of \(A\) using the invertible adjacency \(A_{d-1}\) shows \(\dim\ker A=N/2\), hence \(\operatorname{rank}H=m/2\). Neither standard vector \(u\) nor \(v\) lies in the corresponding image of \(H\) or \(H^T\): vectors in either image have zero self-dot-product because \(H^TH=HH^T=0\), whereas a standard vector has self-dot-product one. The rank-one update therefore gives \(\operatorname{rank}H'=m/2+1\), and \(\operatorname{rank}B=m+2\).

Represent the full-space endpoint vectors by \(e,f\) and put \(p=Ae+f=Be\), \(q=Af+e=Bf\). The four vectors \(e,f,p,q\) are linearly independent for \(d\ge2\). Their span \(W\) is invariant, because \(Be=p\), \(Bf=q\), \(Bp=e+q\), and \(Bq=f+p\). On this explicitly exhibited four-dimensional space \(B\) has characteristic polynomial \((t^2+t+1)^2\), satisfies \(B^3e=f\) and \(B^3f=e\), and satisfies \(B^6=I\) but \(B^3\ne I\); its minimal polynomial is the square of \(t^2+t+1\), not merely the first power. The latter follows also from \(B^3+I\ne0\). Since \(A^2=0\), the image of \(B^2=AE+EA+E^2\) is contained in \(W\). As \(B|_W\) is invertible, this image equals \(W\). The Fitting nilpotent summand is therefore \(\ker B^2\), of dimension \(N-4\), killed by its second update. Its rank under \(B\) is \(\operatorname{rank}B-4=m-2\), so it consists of exactly \(m-2\) blocks \(J_2(0)\). The displayed decomposition follows. The zero-primary entry-time counts come from nullities \(\dim\ker B= m-2\) on this nilpotent summand and \(\dim\ker B^2=2(m-2)\); the two successive fixed-space counts on \(W\) are \(1,Q^2,Q^4\) for exponents one, three and six, giving the stated period populations.

**Odd \(d\).** Now \(HH^T=H^TH=I\). Since \(H_{uv}=1\), the rank-one update has \(\operatorname{rank}H'=m-1\), hence \(\operatorname{rank}B=N-2\). Define \(a=Hv+u\), a nonzero vector supported at the other \(d-1\) neighbors of the deleted odd endpoint. We have \(u^Ta=0\) and \(a^Ta=0\), because \(d-1\) is even. Direct multiplication gives
\[
K:=H'H'^T=I+L,\qquad L=uu^T+au^T+ua^T.
\]
The image of \(L\) is \(\operatorname{span}\{u,a\}\), its rank is two, and \(L^2\) has rank one and is idempotent. Thus \(L\) has one eigenvalue-one simple block, one zero Jordan block of size two, and \(m-3\) additional simple zero blocks. Consequently \(K\) has one simple zero block, one \(J_2(1)\), and \(m-3\) further \(J_1(1)\). The same calculation with \(H'\) transposed gives this Jordan pattern for \(H'^TH'\). It follows that \(B^2\) has precisely two simple zero blocks, two \(J_2(1)\) blocks, and \(2(m-3)\) simple one blocks. Since \(B\) has nullity two, its zero-primary part is \(J_1(0)^{\oplus2}\). The only possible one-primary partitions compatible with this square and dimension are \(J_4(1)\oplus J_2(1)^{\oplus(m-3)}\), or \(J_3(1)^{\oplus2}\oplus J_2(1)^{\oplus(m-4)}\).

To distinguish them, observe that \(\operatorname{im}(B+I)^4=\ker B\) is two-dimensional: all one-primary blocks have size at most four and \(B+I\) acts identically on the zero-primary summand. Choose a second even vertex \(x\ne u\) adjacent to \(v\), possible since \(d\ge3\); then \(Lx=u\). Put \(c=H^Tu+v\) (odd coordinates). Since \(H'^T u=c\), \(H'c=a\), and \((B+I)^2x=Lx=u\), we find \((B+I)^3x=u+c\) but \(B(u+c)=c+a\ne0\). Therefore \(\operatorname{im}(B+I)^3\) is not contained in \(\ker B\), and its rank exceeds two. The two-\(J_3\) option would give rank two, so the size-four option is forced. The recurrent order is exactly four, and the stated fixed-state, primitive-period, and entry-time populations follow by the dimensions of \(\ker(B+I)\), \(\ker(B^2+I)\), and \(\ker(B^4+I)\) on the recurrent component. The zero-primary component is annihilated after one step.

The Fitting decomposition is an actual direct sum of invariant subspaces over \(\mathbb F_Q\); each independent choice of nilpotent and recurrent coordinates determines one configuration. Thus entry times and eventual periods multiply exactly, completing the proof for all field sizes.

## Verification

The independent exact-arithmetic programs `check_direct.py` and `check_block.py` check the claimed matrix ranks and block constraints for dimensions \(2\) through \(7\). The first also enumerates all binary initial configurations at dimensions \(2\), \(3\), and \(4\), compares every entry-time/primitive-period cell with the displayed formulas, and checks ranks of powers of \(B+I\). The second uses a bipartite block construction, distinct from the direct full adjacency calculation. Captured successful output is included as `check_direct_output.txt` and `check_block_output.txt`. Both programs require only the Python standard library. These tests check special cases; the preceding algebra is the proof for every \(d\) and every characteristic-two finite field.

## Relationship to prior work

The general algebraic state-transition framework for additive cellular automata is classical, particularly the work of Martin, Odlyzko and Wolfram (1984), whose article treats finite additive cellular automata and higher-dimensional regular lattices. The 1983 Wolfram review supplies historical context, rather than a defect theorem. The nearest hypercube edge-deletion article inspected, Wu, Zhang, Chen and Wang (2017), is about minimizing the ordinary real adjacency spectral radius by deleting **two, three or four** edges; its full accessible discussion does not address one-edge deletion, characteristic-two Jordan structure or temporal orbit counts. The present claim concerns an exact single-edge defect and all configuration orbits. General finite-field linear-algebra methods are not claimed as new.

A published exact census of neighbor-sum parity dynamics on the **distance-two** Boolean cube uses a different adjacency relation, while an earlier pendant-leaf cube perturbation adds a vertex and an edge instead of deleting an existing edge. The structural implications and recurrent periods of those systems do not imply the present classification. These comparisons are substantive distinctions, not proofs that no unindexed equivalent exists.

## Limitations

The result is restricted to exactly one deleted cube edge, characteristic-two fields, the ordinary binary Hamming cube, and synchronous open-neighbor addition. It does not classify multiple deleted edges or nonlinear excitation rules. Searches and full-text comparison of the closest inspected sources did not identify equivalent coverage, but historical priority cannot be exhaustively guaranteed. The computational checks are finite tests and do not constitute an external or independent audit.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* 55 (1983), 601–644, doi:10.1103/RevModPhys.55.601; published July 1, 1983.
2. O. Martin, A. M. Odlyzko, S. Wolfram, “Algebraic Properties of Cellular Automata,” *Communications in Mathematical Physics* 93 (1984), 219–258, doi:10.1007/BF01223745. Full article: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf .
3. Y. Wu, T. Zhang, S. Chen, T. Wang, “The Minimum Spectral Radius of an Edge-Removed Network: A Hypercube Perspective,” *Discrete Dynamics in Nature and Society* (2017), 1382980, doi:10.1155/2017/1382980.
