# An edge defect creates five arithmetic clocks in characteristic-three bipartite waves

## Finding

Let \(a,b\ge2\) be integers. Form the labelled graph \(G_{a,b}=K_{a,b}-e\) by deleting exactly one cross-edge from the complete bipartite graph; the choice of edge is immaterial up to graph isomorphism. Let \(N=a+b\), let \(q=3^f\) for any integer \(f\ge1\), and let \(A\) denote the loopless adjacency matrix of \(G_{a,b}\) over \(\mathbb F_q\). On the two-time-level state space \(\mathbb F_q^N\times\mathbb F_q^N\), use the reversible update
\[
T(u,v)=(Au-v,u).
\]
Every state is periodic from time zero. The exact global order is
\[
\begin{array}{c|ccc}
&b\equiv0&b\equiv1&b\equiv2\\\hline
a\equiv0&36&24&20\\
a\equiv1&24&12&12\\
a\equiv2&20&12&20
\end{array}\quad(\bmod3),
\]
with the **single exception** \((a,b)=(2,2)\), whose global order is \(10\) rather than \(20\). Each tabulated order is sharp and attained by some state over every allowed finite field.

The residue class \(a\equiv b\equiv2\pmod3\) admits a complete fixed-space and orbit census. For every positive integer \(k\), writing \([P]\) for the indicator of a proposition \(P\),
\[
\boxed{\#\operatorname{Fix}(T^k)
=q^{\,4[5\mid k]+4[10\mid k]+2(N-4)[4\mid k]}.}
\]
This formula also applies to the exceptional \((2,2)\) case, with \(N-4=0\). For each divisor \(d\) of the global order, the exact number of states of least period \(d\) and of distinct temporal orbits of period \(d\) are, respectively,
\[
P_d=\sum_{e\mid d}\mu(d/e)\#\operatorname{Fix}(T^e),\qquad O_d=P_d/d.
\]
When \(N>4\) in this residue class, a uniformly sampled state has maximal primitive period \(20\) with exact probability
\[
\boxed{(1-q^{-8})(1-q^{-2(N-4)}).}
\]
For \((a,b)=(2,2)\) over \(\mathbb F_3\), the least-period populations are \(P_1=1\), \(P_5=80\), and \(P_{10}=6480\), totaling all \(3^8=6561\) states.

The new fifth-root and twentieth-root temporal sectors are absent from the corresponding complete bipartite graph. The defect does not uniformly increase the clock: the exceptional four-vertex case drops from order \(12\) to order \(10\), while the residue class \((0,0)\) triples it from \(12\) to \(36\).

## Assumptions and scope

All vertex labels are distinct; states are ordered pairs of independent field-valued configurations. There are no loops or weights, and the deleted edge joins one specified vertex in each shore. The matrices and all periods are over \(\mathbb F_{3^f}\), with no graph-automorphism or phase quotient. Global order means the least positive \(k\) satisfying \(T^k=I\) on the entire state space, while the least period of an individual state can be smaller. No assertion about other characteristics or updates is made.

## Proof

**1. Low-rank graph module.** Call the endpoints of the deleted edge \(L_0,R_0\), write \(e_L,e_R\) for their coordinate vectors, and write \(s_L,s_R\) for the sums of the coordinate vectors at the other vertices of their respective shores. The four displayed vectors are independent, even when a shore size is divisible by three. Let \(\alpha=a-1\) and \(\beta=b-1\), as elements of \(\mathbb F_3\). The adjacency action on the four-dimensional subspace \(W\) is exactly
\[
Ae_L=s_R,\quad As_L=\alpha(e_R+s_R),\quad
Ae_R=s_L,\quad As_R=\beta(e_L+s_L).
\]
Every adjacency image belongs to \(W\), and the adjacency has rank four: on either shore its two distinct cross-shore column types are independent. Consequently \(\dim\ker A=N-4\). The characteristic polynomial of \(A|_W\), obtained directly from the displayed four actions, is
\[
p(x)=x^4-(ab-1)x^2+(a-1)(b-1),
\]
with coefficients reduced modulo three. The prior real-spectrum formula for the same graph yields the same quartic but does not determine its modular Jordan structure.

**2. Exact adjacency minimal polynomials.** Write \(m_A(x)\) for the monic minimal polynomial. Its exact value is
\[
\begin{array}{c|l}
\{a\bmod3,b\bmod3\}&m_A(x)\\\hline
\{0,0\}&x(x^4+x^2+1)\\
\{0,1\}&x^3(x^2+1)\\
\{0,2\}&x(x^4+x^2-1)\\
\{1,1\}&x^3\\
\{1,2\}&x^3(x^2-1)\\
\{2,2\}&x(x^4+1)
\end{array}
\]
except that \((a,b)=(2,2)\) has \(m_A(x)=x^4+1\).

Here is a direct proof of both annihilation and minimality, avoiding a complex-spectrum or diagonalizability assumption. When \(\alpha\beta\ne0\), the four vectors \(e_L,Ae_L,A^2e_L,A^3e_L\) span \(W\), since
\[
Ae_L=s_R,\quad A^2e_L=\beta(e_L+s_L),\quad A^3e_L=\alpha\beta e_R+\beta(1+\alpha)s_R.
\]
Thus \(A|_W\) is cyclic with minimal polynomial \(p\). Since \(p(0)=\alpha\beta\ne0\), its action on \(W\) is invertible, and the full vertex module is \(W\oplus\ker A\). This gives \(m_A=p\) if \(N=4\), and \(m_A=xp\) if \(N>4\). The first case occurs only when \(a=b=2\).

If \(\alpha=\beta=0\), the four actions imply \(A^3=0\) on the entire vertex module. For any nonhub coordinate vector \(\ell\) on the left, \(A\ell=e_R+s_R\), \(A^2\ell=s_L\ne0\). Therefore \(m_A=x^3\).

Finally, suppose \(\alpha=0\), \(\beta\ne0\), without loss of generality. On \(W\), the cyclic chain generated by \(e_L\) has minimal polynomial \(x(x^2-\beta)\), while \(e_R\mapsto s_L\mapsto0\) requires \(x^2\); hence \(m_{A|_W}=p=x^2(x^2-\beta)\). Since \(A(V)\subseteq W\), \(Ap(A)=0\). But for the single nonhub vector \(\ell\), direct substitution into the displayed actions gives
\[
p(A)\ell=-\beta s_L\ne0.
\]
Therefore the full minimal polynomial is exactly \(xp=x^3(x^2-\beta)\). Interchanging shores covers the other case. Reducing \(\alpha,\beta\) gives the six listed polynomials. This establishes the modular nilpotent indices, including the exceptional four-vertex boundary.

**3. From adjacency blocks to temporal blocks.** The matrix of \(T\) is \(\left(\begin{smallmatrix}A&-I\\I&0\end{smallmatrix}\right)\); its inverse is \(\left(\begin{smallmatrix}0&I\\-I&A\end{smallmatrix}\right)\), and \(T+T^{-1}=\operatorname{diag}(A,A)\). For any cyclic adjacency summand \(\mathbb F_q[x]/(f(x))\) of dimension \(d=\deg f\), the corresponding two-level module is
\[
\mathbb F_q[x,t]/\bigl(f(x),t^2-xt+1\bigr)
\cong\mathbb F_q[t]/\bigl(t^d f(t+t^{-1})\bigr).
\]
Indeed \(t\) is invertible because its quadratic equation has constant term one, so \(x=t+t^{-1}\); both sides have dimension \(2d\). As the largest adjacency invariant factor is \(m_A\), the **exact**, not merely annihilating, minimal polynomial of the temporal operator is
\[
R(t)=t^{\deg m_A}m_A(t+t^{-1}).
\]
This module identity also ensures that a state realizes the full order of \(T\).

**4. Cyclotomic factorization and sharp clocks.** In \(\mathbb F_3[t]\), the six temporal polynomials, with \(\Phi_j\) denoting the ordinary \(j\)-th cyclotomic polynomial reduced modulo three, are
\[
\begin{array}{c|l|c}
\{a\bmod3,b\bmod3\}&R(t)&\operatorname{ord}(T)\\\hline
\{0,0\}&(t^2+1)(t-1)^4(t+1)^4&36\\
\{0,1\}&(t^2+1)^3(t^4+1)&24\\
\{0,2\}&(t^2+1)\Phi_{20}(t)&20\\
\{1,1\}&(t^2+1)^3&12\\
\{1,2\}&(t^2+1)^3(t^2-1)^2&12\\
\{2,2\}&(t^2+1)\Phi_5(t)\Phi_{10}(t)&20.
\end{array}
\]
For \((2,2)\), drop the \((t^2+1)\) factor from the final row, giving order \(10\). The roots of \(t^2+1\), \(t^4+1\), \(\Phi_5\), \(\Phi_{10}\), and \(\Phi_{20}\) have respective multiplicative orders \(4,8,5,10,20\). In characteristic three, a primary factor of multiplicity \(r\) needs the additional power \(3^{\lceil\log_3 r\rceil}\) to kill its nilpotent part. Taking the least common multiple of these primary orders gives the table, including the size-four exception. The cyclic module in step three establishes attainability.

**5. Complete census in the doubly-two residue class.** If \(a\equiv b\equiv2\pmod3\), \(A|_W\) is invertible with polynomial \(x^4+1\), so \(V=W\oplus\ker A\). On the eight-dimensional two-level module over \(W\), the temporal characteristic and minimal polynomial are \(\Phi_5(t)\Phi_{10}(t)\): the two squarefree degree-four factors contribute fixed dimensions \(4[5\mid k]\) and \(4[10\mid k]\). On \(\ker A\times\ker A\), the two-level update is \((u,v)\mapsto(-v,u)\), every nonzero state having exact period four; its fixed dimension is \(2(N-4)[4\mid k]\). Add the dimensions and exponentiate by \(q\) to obtain the asserted formula. If \(N>4\), a state has least period twenty precisely when both its \(W\)-component and its zero-adjacency component are nonzero. These components are independently uniform, giving \((1-q^{-8})(1-q^{-2(N-4)})\). At \(N=4\), the zero-adjacency component vanishes, explaining the exceptional clock. Möbius inversion gives the stated orbit census. \(\square\)

## Verification

The included `check_minpoly.py` also performs 49 exact modular adjacency-minimal-polynomial calculations and 49 symbolic temporal-polynomial factorizations against the claimed tables, with recorded results in `minpoly_output.txt`. The included `check_wave.py` contains independent, standard-library computations on the actual adjacency matrices, not an implementation of the symbolic module proof. It tests all 49 ordered pairs \(2\le a,b\le8\): for each, the claimed order power is the identity and every prime-divisor reduction is nonidentity. It compares the fixed-space dimensions against the closed formula for 360 combinations with \(a,b\in\{2,5,8\}\) and \(1\le k\le40\). It also exhaustively iterates all \(3^8=6561\) states for \((a,b)=(2,2)\) and obtains the displayed period populations. The file `check_output.txt` records the successful execution. These finite checks are corroborative and are not substituted for the unrestricted proof above.

## Relationship to prior work

Vlasov (arXiv:1311.4297, initial version 2013-11-18, §3) states the general reversible two-time-level construction, not these graph-specific periods. Liu and Weng (arXiv:1601.07012, initial version 2016-01-26, Proposition 2.6 and Theorem 3.1) explicitly study the identical single-edge-deleted bipartite graph and give its ordinary adjacency spectrum and spectral uniqueness; the quartic in proof step one is consistent with their spectrum. Their real spectral statement does not specify the characteristic-three Jordan indices or temporal update periods. A published exact census for the **intact** complete bipartite graph gives global periods eight or twelve and cannot be applied unchanged after deleting an edge: the defect's adjacency rank increases from two to four, and an additional fifth-root factor appears. Finite searches found no stronger prior claim covering the defect's six residue/boundary cases; this is evidence of noncoverage in inspected records, not a guarantee of worldwide novelty.

## Limitations

Only one cross-edge is deleted, both shores have at least two vertices, the field characteristic is three, and the recurrence has previous-state subtraction. A complete every-time fixed-space formula is proved only when both shore sizes are congruent to two modulo three; other residue classes are classified by their sharp **global** periods but not by all primitive-period counts here. The literature and database searches cannot rule out unindexed or inaccessible equivalent results. Independent mathematical validation has not been performed.

## References

- A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, initial version 2013-11-18, §3. https://arxiv.org/abs/1311.4297
- C.-a. Liu and C.-w. Weng, *Spectral characterizations of two families of nearly complete bipartite graphs*, arXiv:1601.07012, initial version 2016-01-26, Proposition 2.6 and Theorem 3.1. https://arxiv.org/abs/1601.07012
- *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, published result and proof, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-mod-three-resonance-trichotomy-for-reversible-waves-on-complete--167b2c8980f2/RESULT.md
