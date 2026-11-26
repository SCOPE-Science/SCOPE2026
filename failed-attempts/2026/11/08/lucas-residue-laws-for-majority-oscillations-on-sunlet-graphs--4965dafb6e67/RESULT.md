# Lucas-residue laws for majority oscillations on sunlet graphs

## Finding

Let \(S_n=C_n\odot K_1\) be the **sunlet graph** obtained by attaching one distinct leaf to each vertex of a cycle of length \(n\ge 3\). Give each of its \(2n\) labelled vertices a binary opinion and synchronously replace every opinion by the strict majority among its neighbors. Every vertex has odd degree, so no tie convention is needed. Write \(M_n\) for the update map, \(F_n=|\operatorname{Fix}(M_n)|\), \(P_n=|\operatorname{Fix}(M_n^2)|\), and \(Q_n\) for the number of period-two **states** in which every vertex flips at every update (not the number of orbits). Let \(L_0=2\), \(L_1=1\), and \(L_{k+2}=L_{k+1}+L_k\) be Lucas numbers. Define the six-periodic function \(\epsilon_n=2\cos(n\pi/3)\), which takes successive values \(2,1,-1,-2,-1,1\), and the three-periodic function \(\delta_n=2\cos(2n\pi/3)\), which takes successive values \(2,-1,-1\).

**Exact classification.** For every integer \(n\ge3\), all eventual periods divide two and
\[
F_n=L_n+\epsilon_n,\qquad Q_n=L_n+\delta_n,
\]
\[
P_n=\begin{cases}
L_{2n}+\delta_n,&n\text{ odd},\\
L_{2n}+3-2L_n,&n\equiv2,4\pmod6,\\
L_{2n}+6+4L_n,&n\equiv0\pmod6.
\end{cases}
\]
There are exactly \((P_n-F_n)/2\) primitive two-cycles, of which exactly \(Q_n/2\) have every vertex flipping. There are no longer primitive cycles.

Write \(\varphi=(1+\sqrt5)/2\). The asymptotic laws are
\[
\frac{P_n-F_n}{2}\sim \tfrac12\varphi^{2n},\quad
\frac{Q_n}{P_n-F_n}\sim\varphi^{-n},\quad
\frac{P_n}{4^n}\sim\left(\frac{\varphi^2}{4}\right)^n.
\]
Thus two-cycles grow exponentially, but a uniformly sampled configuration is immediately periodic with exponentially vanishing probability; among period-two states, full-vertex oscillations form an exponentially vanishing fraction. By contrast, binary majority on the undecorated cycle \(C_n\) has zero primitive two-cycles for odd \(n\), and exactly one for even \(n\). Attaching one leaf at each cycle vertex changes an at-most-one two-cycle phenomenon into \(\sim\varphi^{2n}/2\) two-cycles.

## Assumptions and scope

The cycle vertices are indexed by \(i\in\mathbb Z/n\mathbb Z\) and have opinions \(a_i\); their distinct attached leaves have opinions \(b_i\). All opinions are in \(\{0,1\}\). The rule on \(S_n\) is exactly
\[
M_n(a,b)=\bigl(c,a\bigr),\qquad c_i=\operatorname{maj}(a_{i-1},a_{i+1},b_i),
\]
where \(\operatorname{maj}(x,y,z)\) is the majority of three bits. The cyclic indices and the labels are retained in the counts; no quotient by graph symmetries is taken. For a period-two state, *pure* means that all \(2n\) opinions flip at each update. The result does not classify transient-entry times or basin sizes.

## Proof

**Period bound.** Replace the bits by spins \(s_i(t)\in\{-1,1\}\), and put \(h_i(t)=\sum_{j\sim i}s_j(t)\). Each degree is odd, so \(h_i(t)\ne0\) and \(s_i(t+1)=\operatorname{sgn}h_i(t)\). The integer-valued energy
\[
E(t)=-\sum_i\sum_{j\sim i}s_i(t)s_j(t-1)
\]
satisfies, by symmetry of the graph,
\[
E(t+1)-E(t)
=-\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)h_i(t)\le0.
\]
Each summand on the right is zero precisely when \(s_i(t+1)=s_i(t-1)\), and otherwise equals \(-2|h_i(t)|\). Since the energy takes finitely many integer values, it eventually stops decreasing, at which point the next state equals the previous state two steps earlier. Thus every orbit eventually has period one or two; no assertion about a uniform transient bound is needed.

**Local two-period constraint.** If \(M_n^2(a,b)=(a,b)\), the leaf coordinates after two updates force the first updated rim to equal \(b\). The other half of the condition then requires the next rim update to equal \(a\). Explicitly,
\[
b_i=\operatorname{maj}(a_{i-1},a_{i+1},b_i),\qquad
 a_i=\operatorname{maj}(b_{i-1},b_{i+1},a_i).
\]
The identity \(x=\operatorname{maj}(u,v,x)\) holds exactly when \(x\in\{u,v\}\). Hence the condition is equivalent, for every \(i\), to
\[
b_i\in\{a_{i-1},a_{i+1}\},\qquad
a_i\in\{b_{i-1},b_{i+1}\}.
\tag{1}
\]
This reduction is an equivalence, not merely a necessary condition.

**Finite transfer identity.** Label the four possible site-pairs \(q_i=(a_i,b_i)\) by integers \(0,1,2,3\), in lexicographic order. Define a \(16\times16\) zero-one matrix \(T\) with row index \((p,c)\) and column index \((c',r)\), where \(p,c,c',r\in\{0,1,2,3\}\). The entry is one precisely if \(c=c'\) and, denoting the two bits of any symbol \(w\) by \(a(w),b(w)\),
\[
b(c)\in\{a(p),a(r)\},\qquad a(c)\in\{b(p),b(r)\}.
\]
Then length-\(n\) closed walks of this transfer graph correspond bijectively to labelled cyclic choices of \(q_i\) satisfying (1), including repeated-site patterns. Therefore \(P_n=\operatorname{tr}(T^n)\), without division by \(n\). Exact finite polynomial arithmetic gives
\[
\det(xI-T)=(x-1)^2(x+1)^2(x^2-3x+1)(x^2+x+1)
(x^8+3x^6+8x^4+3x^2+1).
\tag{2}
\]
This determinant identity is reproducibly certified by the embedded `code/transfer_certificate.py`, which constructs all entries from (1) and derives all characteristic coefficients using integer Newton identities; it is also checkable directly by determinant expansion.

**Evaluation of the trace.** The quadratic \(x^2-3x+1\) has roots \(\varphi^2,\varphi^{-2}\). The octic factor in (2) is
\[
\bigl(x^4+\varphi^2x^2+\varphi^4\bigr)
\bigl(x^4+\varphi^{-2}x^2+\varphi^{-4}\bigr).
\]
Its eight complex roots are \(\varphi^{\pm1}e^{\pm i\pi/3}\) and \(\varphi^{\pm1}e^{\pm 2i\pi/3}\). Thus its contribution to the trace of the \(n\)-th power is
\[
2(\varphi^n+\varphi^{-n})
\bigl(\cos(n\pi/3)+\cos(2n\pi/3)\bigr).
\]
This vanishes for odd \(n\), equals \(-2L_n\) for \(n\equiv2,4\pmod6\), and equals \(4L_n\) for \(6\mid n\). The other factors in (2) contribute \(L_{2n}+2+2(-1)^n+\delta_n\). This proves the asserted three-case formula for \(P_n\).

**Fixed and pure cycles.** A fixed state must have \(b_i=a_i\); the remaining condition says \(a_i\in\{a_{i-1},a_{i+1}\}\), so its cyclic binary string has no isolated bit. The corresponding four-state de Bruijn transfer matrix \(U\), with entries \(U_{(p,c),(c,r)}=1\) iff \(c=p\) or \(c=r\), has
\[
\det(xI-U)=(x^2-x-1)(x^2-x+1).
\]
The two factors yield \(F_n=L_n+\epsilon_n\). A pure period-two state is exactly one with \(b_i=1-a_i\) for every \(i\). Substitution into (1) says that \(a\) contains no cyclic triple of identical bits. The corresponding four-state transfer matrix \(V\), with entries \(V_{(p,c),(c,r)}=1\) iff \(p,c,r\) are not all identical, has
\[
\det(xI-V)=(x^2-x-1)(x^2+x+1),
\]
so \(Q_n=L_n+\delta_n\). Every pure state is nonfixed. Since every nonfixed state fixed by the second iterate lies in an orbit of size two, the two-cycle counts follow.

**Asymptotics and comparison.** As \(L_k=\varphi^k+(-\varphi^{-1})^k\), the exact formulas give \(P_n=\varphi^{2n}+O(\varphi^n)\), \(F_n=\varphi^n+O(1)\), and \(Q_n=\varphi^n+O(1)\), with constants independent of \(n\). Division proves the asymptotics. On \(C_n\) without leaves, each equal adjacent opinion-pair remains fixed forever. A nontrivial two-cycle cannot contain a fixed vertex adjacent to a toggling vertex: at one phase the fixed neighbor would prevent that toggling vertex from changing back. Connectivity therefore forces every vertex to toggle; only the alternating cyclic word works, and it exists only for even \(n\). This proves the comparison.

## Verification

The attached `code/direct_census.cpp` independently implements the simultaneous majority rule on the actual graph, enumerates all \(4^n\) configurations for every \(3\le n\le11\), and checks the fixed, second-iterate-fixed, and pure-two-cycle populations against the formulas. Its largest case contains \(4^{11}=4,194,304\) states. It is not used as a proof for all \(n\).

The attached `code/transfer_certificate.py` constructs the three integer transfer matrices from the local constraints, calculates their exact characteristic polynomials by Newton identities, and verifies the trace evaluations for \(3\le n\le30\). It also checks the parity/integrality and containment relations. This finite certificate verifies the only nontrivial fixed-size symbolic computation in the universal transfer-matrix proof; the logical bijections and spectral evaluations are proved above. Captured matching outputs accompany both sources in `results/`.

For example, the first five values of \((F_n,P_n,Q_n,(P_n-F_n)/2)\), at \(n=3,4,5,6,7\), are \((2,20,6,9)\), \((6,36,6,15)\), \((12,122,10,55)\), \((20,400,20,190)\), and \((30,842,28,406)\), respectively.

## Relationship to prior work

The general period-at-most-two property for finite symmetric threshold networks is classical (Goles–Olivos, 1980 and 1981). Kuhlman, Mortveit, Murrugarra and Kumar (arXiv:1108.2974v1, 2011) prove related synchronous bi-threshold restrictions and include a reconstruction of the earlier threshold proof, but their special graph-family results concern different threshold mechanisms and do not evaluate the sunlet periodic-state trace. Tošić and Agha (2004) study ordinary one-dimensional majority cellular automata, including fixed and two-cycle patterns on the undecorated line/ring; their transfer is not the paired rim-and-leaf constraint (1). Nakar–Ron (2022) study ordinary one-dimensional radius-based majority configurations; Turau (2022) treats trees. Neither contains the sunlet family. The fixed-word Lucas factor is classical; the asserted contribution is the full sunlet second-iterate count, pure-cycle count, and resulting exponential oscillation contrast, not the general period restriction or a generic transfer-matrix method.

## Limitations

The formulas count **initially periodic** configurations and primitive cycles, not the sizes of their attraction basins or transient-length distributions. Nothing is asserted for non-sunlet graph attachments, higher opinion alphabets, asynchronous updates, or graph automorphism orbit classes. The linear-algebra determinant is finite and exactly reproduced, not an independently checked external formal proof. Searches and inspected publications do not establish absolute historical priority; a missed equivalent derivation could exist, particularly in the literature on synchronous majority automata with memory. Independent validation has not been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1 (first posted 2011-08-15), https://arxiv.org/abs/1108.2974.
3. P. T. Tošić and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI, LNCS 3305 (2004), 861–870. DOI: 10.1007/978-3-540-30479-1_89. Accessible full text: https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
4. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata*, arXiv:2205.08972v1 (2022), https://arxiv.org/abs/2205.08972.
5. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (2022), https://arxiv.org/abs/2202.01580.
6. E. W. Weisstein, *Sunlet Graph*, MathWorld, https://mathworld.wolfram.com/SunletGraph.html (graph definition).
