# A single pendant vertex creates Fibonacci-many majority oscillations on a cycle

## Finding

Let \(G_n\), for every integer \(n\ge3\), be the labelled simple cycle \(C_n\) on core vertices \(v_0,\ldots,v_{n-1}\), with exactly **one** additional degree-one vertex \(w\) adjacent to \(v_0\). Under synchronous open-neighbor binary majority, with a vertex retaining its previous bit on a tie, let \(F_n\) count fixed configurations and let \(P_n\) count configurations whose **least temporal period is exactly two starting at time zero**. Let Fibonacci numbers be \(f_0=0\), \(f_1=1\), and \(f_{j+2}=f_{j+1}+f_j\). Define \(c_0=4,c_1=2,c_2=2,c_3=-2,c_4=0,c_5=0\), extended with period six. Then

\[
\boxed{P_n=2f_{n-2}+c_{n\bmod6}.}
\]

Furthermore, with Lucas numbers \(L_n=f_{n-1}+f_{n+1}\),

\[
\boxed{F_n=L_n+2\cos(n\pi/3),\qquad
|\operatorname{Fix}(M^2)|=F_n+P_n.}
\]

Every fixed state of the undecorated cycle \(C_n\) extends uniquely to a fixed state of \(G_n\); hence adding the leaf changes **none** of the fixed-state populations. In contrast, on \(C_n\) itself there are exactly \(1+(-1)^n\) initially primitive-two configurations, at most two, while \(G_n\) has a positive primitive-two population precisely when \(n\ge4\). The number of distinct primitive-two temporal orbits on \(G_n\) is \(P_n/2\). With \(\varphi=(1+\sqrt5)/2\),

\[
P_n\sim\frac{2}{\sqrt5\,\varphi^2}\varphi^n,
\qquad
\lim_{n\to\infty}\frac{\log P_n}{n}=\log\varphi,
\qquad
\frac{P_n}{2^{n+1}}\longrightarrow0.
\]

The logarithmic limit is taken along \(n\ge4\). A single vertex of degree one therefore changes the oscillating population from uniformly bounded to exponential while leaving the fixed-state census unchanged.

## Assumptions and scope

All vertices are labelled and all configurations are counted with their actual binary states, not modulo graph automorphisms or global bit complementation. The cycle is simple, so \(n\ge3\). Every update uses the **open** neighborhood; for an even number of neighbors, ties preserve the current bit. All vertices, including the leaf, update simultaneously. Here \(M\) is the deterministic global update, \(F_n=|\operatorname{Fix}(M)|\), and \(P_n=|\operatorname{Fix}(M^2)\setminus\operatorname{Fix}(M)|\). Period two from time zero is distinct from eventual convergence to a two-cycle.

Write \(\operatorname{maj}(a,b,c)\) for the majority bit among three binary inputs; it equals \(a\) when \(a=b\), and otherwise equals \(c\). This notation handles the two-neighbor case with tie retention by including the previous center bit as the third argument.

## Proof

**1. Local two-phase parametrization.** For a state fixed by \(M^2\), let \(a_i\) and \(b_i\) be core bits at times zero and one. The leaf is forced to have bit \(b_0\) at time zero and \(a_0\) at time one, since its only neighbor is \(v_0\). Thus there is no independent leaf choice. The necessary and sufficient constraints, with indices modulo \(n\), are

\[
\begin{aligned}
b_i&=\operatorname{maj}(a_{i-1},a_{i+1},a_i),&
 a_i&=\operatorname{maj}(b_{i-1},b_{i+1},b_i),&&i\ne0,\\
b_0&=\operatorname{maj}(a_{n-1},a_1,b_0),&
 a_0&=\operatorname{maj}(b_{n-1},b_1,a_0).&&
\end{aligned}
\]

Conversely, a cyclic assignment of the core two-phase pairs satisfying these relations, together with leaf bit \(b_0\), produces a state fixed by \(M^2\); its next state has leaf bit \(a_0\). This is a bijection, not merely an upper bound.

**2. Exact finite transfer.** Put \(\mathcal S=\{0,1\}^2\); use the 16 ordered-pair states \((s,t)\in\mathcal S^2\), with \(s=(a_-,b_-)\), \(t=(a,b)\). Define two explicitly determined 0–1 matrices \(A,B\) of order 16. Their only potentially nonzero entry from \((s,t)\) to \((t,u)\), for \(u=(a_+,b_+)\), is one exactly when the following two relations hold:

\[
\begin{array}{c|cc}
 &\text{first condition}&\text{second condition}\\\hline
A&b=\operatorname{maj}(a_-,a_+,a)&a=\operatorname{maj}(b_-,b_+,b)\\
B&b=\operatorname{maj}(a_-,a_+,b)&a=\operatorname{maj}(b_-,b_+,a).
\end{array}
\]

All other entries vanish. The one exceptional vertex uses \(B\) and the remaining cycle vertices use \(A\), hence

\[
Q_n:=|\operatorname{Fix}(M^2)|=\operatorname{tr}(BA^{n-1}).
\]

Direct exact multiplication of these explicitly defined 16-by-16 integer matrices gives the finite identity

\[
A^2\bigl(A^6-2A^5+2A^3-2A^2+I\bigr)=0.
\]

The standalone `checks/check_symbolic.py` constructs \(A,B\) from the 64 possible local triples and verifies every entry of this identity using integer arithmetic. Consequently, for \(n\ge3\), \(Q_n\) satisfies the order-six recurrence

\[
Q_{n+6}-2Q_{n+5}+2Q_{n+3}-2Q_{n+2}+Q_n=0.
\]

The same exact transfer evaluation yields the six initial values

\[
(Q_3,Q_4,Q_5,Q_6,Q_7,Q_8)=(2,8,16,30,42,64).
\]

**3. Fixed states.** At a fixed state the leaf must equal \(v_0\). Then the majority rule at \(v_0\) reduces to \(\operatorname{maj}(a_{n-1},a_1,a_0)=a_0\), exactly the tie-retaining rule on the bare cycle. The other core vertices already obey that same rule. Thus fixed states correspond bijectively to cyclic binary words with no isolated bit (no local patterns 010 or 101). Using the pair-state transfer \((a,b)\to(b,c)\) allowed precisely if \(b=\operatorname{maj}(a,c,b)\), its characteristic polynomial is

\[
(X^2-X-1)(X^2-X+1).
\]

Its trace at power \(n\) equals \(L_n+2\cos(n\pi/3)\), proving the fixed-state formula. For the undecorated cycle, the two-phase transfer is \(A\), with characteristic polynomial

\[
X^{10}(X-1)(X+1)(X^2-X-1)(X^2-X+1).
\]

For \(n\ge3\), therefore, \(\operatorname{tr}(A^n)-F_n=1+(-1)^n\), yielding the bounded comparison.

**4. Closed form.** Define the candidate \(\widetilde Q_n=F_n+2f_{n-2}+c_{n\bmod6}\). The polynomial of the order-six recurrence factors as

\[
X^6-2X^5+2X^3-2X^2+1
=(X-1)(X+1)(X^2-X-1)(X^2-X+1).
\]

Both \(F_n\) and the Fibonacci term are annihilated by the relevant quadratic factors. The periodic correction satisfies the same order-six recurrence; this follows directly from its six residues (or from \(c_n=1+(-1)^n+2\cos(n\pi/3)+(2/\sqrt3)\sin(n\pi/3)\)). The six starting values agree with the exact transfer counts. Uniqueness of solutions to the recurrence proves \(Q_n=\widetilde Q_n\) for every \(n\ge3\). Subtracting \(F_n\) gives the displayed formula for \(P_n\).

**5. Positivity and asymptotics.** The formula gives \(P_3=0\), \(P_4=2\), \(P_5=4\); for \(n\ge6\), \(2f_{n-2}\ge6\) and \(c_{n\bmod6}\ge-2\). Thus the existence threshold is exactly \(n\ge4\). Since \(c_n\) is bounded and \(f_{n-2}=(\varphi^{n-2}-(-\varphi^{-1})^{n-2})/\sqrt5\), the claimed exponential asymptotic and limiting fraction follow. Every least-period-two orbit contains exactly two labelled states.

## Verification

The complete integer-matrix construction, annihilating identity, polynomial factors and six recurrence seeds are verified in `checks/check_symbolic.py` and `checks/symbolic_output.txt`. An independent direct implementation of synchronous majority updates (not the transfer matrix) examines **all** \(2^{n+1}\) labelled initial states for each \(3\le n\le13\), verifying the fixed population and primitive-two formula; it also exhausts the undecorated cycles for the same lengths. See `checks/check_direct.py` and `checks/direct_output.txt`. These finite experiments are supplementary: the infinite result uses the proved bijection, the explicitly checkable finite matrix identity, and recurrence induction.

## Relationship to prior work

The 2004 analysis by Tošić and Agha characterizes period-two behavior for one-dimensional regular majority automata and thus covers the **undecorated** ring but not the irregular one-leaf graph. Kaaser, Mallmann-Trenn and Natale (2015) prove general convergence-time bounds rather than graph-specific initial periodic-state counts. Nakar and Ron (2022) analyze periodic structures of homogeneous one-dimensional majority automata; their results do not incorporate a single exceptional graph vertex with a private leaf. A related previous exact census for **every** cycle vertex carrying a leaf has a different graph and growth exponent, \(2\log\varphi\), and does not determine the present sparse one-leaf census. The new statement concerns a single defect, not a repeated decoration or a consequence of the bare-cycle formulas. Exact historical priority outside inspected and indexed sources is not certified.

## Limitations

The count is for initially periodic states, not transient basins, first-entry times, stochastic initial conditions, or equivalence classes under spatial rotation. It assumes an open-neighbor majority and tie retention, not a self-inclusive majority on every vertex. The general two-periodic convergence theorem is background and is not used to infer that finite computations prove the infinite census. The asymptotic concerns the family \(n\to\infty\), not time evolution of a single graph. No independent external validation has been performed.

## References

1. Dominik Kaaser, Frederik Mallmann-Trenn, and Emanuele Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first publicly posted 2015-08-14, https://arxiv.org/abs/1508.03519.
2. Predrag T. Tošić and Gul A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, pp. 861–870, DOI:10.1007/978-3-540-30479-1_89. Author-hosted full text: https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
3. Yonatan Nakar and Dana Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972v1 (2022-05-18), https://arxiv.org/abs/2205.08972.
