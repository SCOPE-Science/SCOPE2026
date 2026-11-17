# A single missing edge creates sixty-step reversible ternary waves on cliques

## Finding

For each integer \(n\ge3\), form the simple labelled graph \(G_n=K_n-\{\{1,2\}\}\) by deleting exactly one edge from the complete graph. Let \(q=3^f\) for any integer \(f\ge1\), write \(A_n\) for its adjacency matrix over \(\mathbb F_q\), and evolve two vertex-field rows by the reversible rule
\[
 T_n(u,v)=(A_nu-v,u),\qquad (u,v)\in\mathbb F_q^n\times\mathbb F_q^n.
\]
Its exact global temporal order is
\[
 \boxed{L_n=\operatorname{ord}(T_n)=
 \begin{cases}8&n=3,\\24&n\equiv0\pmod3,\ n\ge6,\\60&n\equiv1\pmod3,\\36&n\equiv2\pmod3.\end{cases}}
\]
Thus a single missing edge produces **primitive sixty-step waves already for four vertices**. The distinction between the three residue classes persists for arbitrarily large graphs.

There is also a complete all-times orbit census. For each positive integer \(t\), define \(E_n(t)=\dim_{\mathbb F_q}\ker(T_n^t-I_{2n})\), and write \([Q]\) for the indicator of a statement \(Q\). With \(w_t=3^{\nu_3(t)}\), where \(\nu_3(t)\) is the exponent of three in \(t\), we obtain
\[
 \boxed{E_n(t)=\begin{cases}
 (n-3)(1+[3\mid t])+2[4\mid t]+4[8\mid t],&n\equiv0\pmod3,\\
 (n-3)(1+[3\mid t])+2[4\mid t]+4[10\mid t],&n\equiv1\pmod3,\\
 4[4\mid t]+\min(4,w_t)+(n-4)\min(2,w_t),&n\equiv2\pmod3.
 \end{cases}}
\]
In particular, \(\#\operatorname{Fix}(T_n^t)=q^{E_n(t)}\). For every positive divisor \(d\) of \(L_n\), the exact number of labelled configurations with *least* temporal period \(d\) and the number of their distinct temporal cycles are, respectively,
\[
 \boxed{P_d=\sum_{e\mid d}\mu(d/e)\,q^{E_n(e)},\qquad C_d=P_d/d.}
\]
All other primitive periods are absent, and every state is periodic from its first time level. This is a complete classification for every graph size, every characteristic-three finite field, and every time index, not an extrapolation from small examples.

## Assumptions and scope

Vertices of \(G_n\) remain individually labelled, including the endpoints of the deleted edge. The graph is undirected and loopless; all other edges are present. The two time levels are ordered and may be arbitrary elements of \(\mathbb F_q^n\). The update uses field subtraction and is not an integer-valued oscillator or a Boolean majority rule. The notion of *global order* is the smallest positive \(L\) for which \(T_n^L\) is the identity on every pair of rows; because \(T_n\) is invertible, this order is attained by a state as its least positive period. There is no identification under vertex permutations, time translation, or scalar multiplication in the state counts. The formulas cover \(n=3\) (a three-vertex path) explicitly and require \(n\ge3\).

## Proof

**1. Reversibility and the adjacency polynomial.** In every characteristic, \(T_n^{-1}(u,v)=(v,A_nv-u)\), so there are no transients on the finite state space. Let \(e_1,\ldots,e_n\) be the standard coordinate basis and write
\[
 z=e_1-e_2,\qquad a=e_1+e_2,\qquad b=\sum_{j=3}^n e_j,\qquad
 W=\{x:x_1=x_2=0,\ \sum_{j=3}^n x_j=0\}.
\]
One checks directly, initially over the integers, that
\[
 A_nz=0,\quad A_n|_W=-I,\quad A_na=2b,\quad A_nb=(n-2)a+(n-3)b.
\]
Over the rationals these give a direct sum \(\langle z\rangle\oplus W\oplus\langle a,b\rangle\), and the adjacency characteristic polynomial is the **integer** polynomial
\[
 \chi_{A_n}(Y)=Y(Y+1)^{n-3}\bigl(Y^2-(n-3)Y-2(n-2)\bigr).
\]
Since this identity holds in \(\mathbb Z[Y]\), it holds after reduction modulo three. The integer derivation is not used to assert a direct sum in characteristic three when its summands can intersect.

**2. The nonresonant classes.** If \(n\equiv0\) or \(1\pmod3\), then \(n-2\) is invertible in \(\mathbb F_3\). Hence the three subspaces from Step 1 indeed form a direct sum over \(\mathbb F_q\). The restriction of \(A_n\) to the \(a,b\) plane has matrix \(B=\bigl(\begin{smallmatrix}0&n-2\\2&n-3\end{smallmatrix}\bigr)\). Its characteristic polynomial modulo three is \(Y^2+1\) in residue zero and \(Y^2-Y+2\) in residue one. Both are irreducible over \(\mathbb F_3\). For the four-dimensional two-row wave over this plane, the characteristic polynomial is \(\det(X^2I_2-XB+I_2)\), namely
\[
 \Phi_8(X)=X^4+1 \quad(n\equiv0),\qquad
 \Phi_{10}(X)=X^4-X^3+X^2-X+1\quad(n\equiv1).
\]
These cyclotomic polynomials have four distinct primitive roots of orders eight and ten, respectively, in characteristic three; consequently the entire four-dimensional core has exact order eight or ten, with no fixed vectors at time \(t\) unless the corresponding order divides \(t\). The \(z\)-space produces a two-dimensional wave with polynomial \(X^2+1\) and exact order four. Each of the \(n-3\) dimensions in \(W\) produces a two-dimensional wave with polynomial \(X^2+X+1=(X-1)^2\); it is a *nonscalar* Jordan block \(J_2(1)\) (the two time levels exchange nontrivially), of exact order three. Its time-\(t\) fixed dimension is \(1+[3\mid t]\). Adding the three independent contributions proves the first two formulas for \(E_n(t)\). Their sharp global orders are \(\operatorname{lcm}(8,4,3)=24\) when \(n\ge6\) is divisible by three, \(8\) when \(n=3\), and \(\operatorname{lcm}(10,4,3)=60\) when \(n\equiv1\pmod3\).

**3. The resonant class.** Now suppose \(n\equiv2\pmod3\), necessarily \(n\ge5\). Here \(n-2=0\) in \(\mathbb F_3\), so the direct sum in Step 2 is **not** valid: indeed \(b\in W\). The integer characteristic polynomial instead reduces to \(Y^2(Y+1)^{n-2}\). Solving \(A_nx=0\) gives a two-dimensional kernel: the two endpoint coordinates are arbitrary and every remaining coordinate is their sum. Solving \((A_n+I)x=0\) gives \(x_1=x_2=0\) and zero sum on the remaining coordinates, so its kernel has dimension \(n-3\). Because zero and minus one are distinct eigenvalues in characteristic three, these algebraic and geometric multiplicities uniquely determine the adjacency Jordan structure
\[
 A_n\sim J_1(0)^{\oplus2}\oplus J_2(-1)\oplus J_1(-1)^{\oplus(n-4)}.
\]
Each zero eigenline supplies a two-level wave with polynomial \(X^2+1\) and exact order four, giving four fixed dimensions exactly when \(4\mid t\). On a spatial \(J_j(-1)\), \(j=1,2\), the two-level wave has characteristic polynomial \((X-1)^{2j}\). Its fixed-eigenspace is naturally \(\ker(A_n+I)\) on that spatial block and thus has dimension one; therefore it is a **single** unipotent Jordan block \(J_{2j}(1)\), rather than a direct sum of smaller blocks. Its fixed dimension after \(t\) updates is \(\min(2j,3^{\nu_3(t)})\). Summing the two size-two zero-wave pieces, one \(J_4(1)\), and \(n-4\) copies of \(J_2(1)\) gives the third \(E_n(t)\) formula. Both orders four and nine occur and therefore the sharp global order is \(\operatorname{lcm}(4,9)=36\).

**4. Exact populations and field extensions.** All the preceding matrices have entries in \(\mathbb F_3\). Extending scalars from \(\mathbb F_3\) to \(\mathbb F_{3^f}\) preserves the relevant polynomial identities, kernel dimensions, and exact operator orders; no diagonalization over the extension field is required. The number of points of an \(E\)-dimensional kernel over \(\mathbb F_q\) is \(q^E\), proving the all-time fixed-point formula. As every state has some least period dividing \(L_n\), summing least-period counts over divisors of \(t\) equals the fixed-point count at time \(t\). Möbius inversion yields \(P_d\), and dividing by the least period yields distinct temporal orbits. Finally, a vector attaining the global operator order exists by combining vectors of maximal orders from the independent primary summands (or, equivalently, by elementary rational canonical form), so each displayed \(L_n\) is attained by a genuine primitive temporal cycle. This completes the proof.

## Verification

The included executable programs `proof/verify_matrix.py` and `proof/verify_direct.py` are standalone Python 3 scripts requiring only the standard library. The matrix verifier builds the precise deleted-edge adjacency and the two-level wave over \(\mathbb F_3\), independently computes ranks of \(T_n^t-I\) for **608** combinations of \(3\le n\le18\) and \(1\le t\le L_n\), and checks that the claimed global orders are sharp. The direct verifier separately implements simultaneous neighbor-sum updates and exhausts all \(3^6+3^8+3^{10}=66{,}339\) configurations for \(n=3,4,5\), comparing least-period distributions without matrix nullity calculations. Both programs ran successfully; their stdout outputs `proof/matrix.out` and `proof/direct.out` are embedded in this package. These finite calculations corroborate, but do not replace, the proof for all \(n\), \(f\), and \(t\).

For \(q=3\), the direct primitive-period populations are
\[
\begin{array}{c|l}
n& (\text{period}:\text{number of states})\\\hline
3&(1:1),\ (4:8),\ (8:720)\\
4&(1:3),\ (3:6),\ (4:24),\ (10:240),\ (12:48),\ (20:1920),\ (30:480),\ (60:3840)\\
5&(1:9),\ (3:234),\ (4:720),\ (9:486),\ (12:18720),\ (36:38880).
\end{array}
\]
In particular \(3{,}840/60=64\) distinct primitive sixty-cycles already occur for the four-vertex graph.

## Relationship to prior work

General second-order reversible cellular automata and their first-order linear matrix realizations predate this result; see Macfarlane (2004), Ceccherini-Silberstein--Coornaert (2009), and Vlasov (2013). The present claim is **not** the construction of reversibility itself. The published complete-graph case in the characteristic-three Hamming-graph wave census (a single Hamming factor) has different adjacency and is not an edge-deleted graph. Previously published complete-bipartite characteristic-three wave results apply only to bipartite graphs, whereas \(G_n\) contains triangles for \(n\ge4\). A published complete-multipartite wave theorem includes the graph shape \(G_n\), but assumes characteristic **two**, and its additive-sign behavior differs. Its period formula therefore does not imply the characteristic-three resonance and all-time fixed-space formula here. The new contribution is the interaction of one missing edge with the three-adic modular Jordan structure, resulting in the sharp \(24/60/36\) trichotomy and exact least-period counts for every graph size. Equivalences of the sign convention by linear conjugacy do not change the claim's comparison: the corresponding characteristic-three cycle populations have still not been found in those inspected statements.

## Limitations

The result applies to the precise graph \(K_n\) minus one edge and a reversible, linear, neighbor-sum wave over finite characteristic-three fields. It does not cover other finite characteristics, multiple deleted edges, nonlinear threshold updates, or equivalence classes modulo graph symmetries. Novelty comparisons are bounded by the inspected papers and accessible sources; an earlier unindexed calculation may exist. The generic 2004 linear-automata article was accessed at the abstract and bibliographic level, rather than as a complete text, and this remains a historical comparison risk. There has been no external independent mathematical audit.

## References

1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A **37** (2004), 10791–10814, DOI:10.1088/0305-4470/37/45/006; verified public journal date 2004-10-28.
2. T. Ceccherini-Silberstein and M. Coornaert, *The Garden of Eden theorem for linear cellular automata*, arXiv:0910.0863 (2009), https://arxiv.org/abs/0910.0863.
3. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297 (first submitted 2013-11-18), https://arxiv.org/abs/1311.4297.
4. *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs* (2026), published research record `2026/11/8/SCOPE-a-three-class-wave-clock-and-exact-orbit-census-for-ternary-modu--13302e527b48`.
5. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs* (2026), published research record `2026/11/8/SCOPE-mod-three-resonance-trichotomy-for-reversible-waves-on-complete--167b2c8980f2`.
6. *Twenty-four-step resonances in reversible waves on complete multipartite graphs* (2026), published research record `2026/11/8/SCOPE-twenty-four-step-resonances-in-reversible-waves-on-complete-mult--addc32219e63`.
