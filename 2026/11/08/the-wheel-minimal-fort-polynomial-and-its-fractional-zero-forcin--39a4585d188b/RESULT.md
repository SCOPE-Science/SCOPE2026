# The wheel minimal-fort polynomial and its fractional zero-forcing gap

## Finding
For every integer \(n\geq3\), let \(W_{n+1}=K_1\vee C_n\), with a distinguished hub \(h\) and \(n\) individually labelled rim vertices. A *fort* is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Put
\[
M_n(z)=\sum_{F\text{ inclusion-minimal fort of }W_{n+1}}z^{|F|}.
\]
Define
\[
A(x,z)=1-zx^2-z^2x^3,\qquad
B(x,z)=1-zx^2-zx^3-z^2x^4+z^3x^6.
\]
Then the **complete labelled cardinality distribution** is the rational generating function
\[
\boxed{\sum_{n\geq3}M_n(z)x^n=
-x\frac{\partial_xA(x,z)}{A(x,z)}
-zx\frac{\partial_xB(x,z)}{B(x,z)}
-2zx^2-\frac{2z^2x^2}{1-zx^2}.}
\]
In particular, if \(H_n\) counts inclusion-minimal forts *containing the hub*, then
\[
\boxed{\sum_{n\geq3}H_nx^n=
-x\frac{\mathrm d}{\mathrm dx}\log(1-x^2-x^3-x^4+x^6)
-\frac{2x^2}{1-x^2}.}
\]
Its initial values for \(n=3,4,\ldots\) are \(3,4,5,3,14,12,21,25,44,55,78,112,158,\ldots\). The prior literature lists these values but does not give an explicit formula for them [2, Section 5.1].

Let \(Z^*(G)\) be the *fractional transversal number of the minimal-fort hypergraph*, as in [1], and let \(\operatorname{ft}(G)\) be the maximum number of pairwise vertex-disjoint forts. Then for all \(n\geq3\),
\[
\boxed{\operatorname{ft}(W_{n+1})=2,\qquad
Z^*(W_{n+1})=1+\frac{n-\lceil n/3\rceil}{\lceil n/2\rceil},\qquad
Z(W_{n+1})=3.}
\]
Equality \(Z^*(W_{n+1})=\operatorname{ft}(W_{n+1})=2\) occurs exactly for \(n\in\{3,4,5,7\}\). For all \(n\geq8\), the three parameters are strictly ordered \(2<Z^*(W_{n+1})<3\). The additive integrality gap tends to \(2/3\).

The total number of inclusion-minimal forts also obeys
\[
\boxed{M_n(1)\sim\lambda^n,\quad
\lambda=1.40126836793985\ldots,\quad
\lambda^6-\lambda^4-\lambda^3-\lambda^2+1=0,}
\]
where \(\lambda\) is the unique real root larger than \(1\) of maximum modulus among the roots of the displayed polynomial. The leading asymptotic constant is exactly \(1\).

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The symbol \(C_n\) denotes the ordinary simple cycle even for \(n=3\); the vertex \(h\) is adjacent to every rim vertex. An inclusion-minimal fort has no **proper nonempty subset** that is a fort; checking only single deletions is not by itself sufficient in arbitrary graphs. A dominating set \(D\) of a graph means that each vertex outside \(D\) has a neighbor in \(D\). Minimal dominating is inclusion-minimal, not necessarily minimum cardinality.

The fractional parameter is the nonnegative linear-program optimum
\[
Z^*(G)=\min\left\{\sum_{v\in V(G)}w_v:\ 
\sum_{v\in F}w_v\geq1\text{ for every minimal fort }F,\ w_v\geq0\right\}.
\]
It is **not** the distinct three-color-game fractional forcing parameter.

## Proof
**1. Exhaustive classification by hub membership.** Write \(R=V(C_n)\). If \(h\notin F\), then \(F\subseteq R\) and the hub must have at least two neighbors in \(F\), forcing \(|F|\geq2\). An omitted rim vertex must have zero or two neighbors in \(F\). In a nonempty proper rim set, a block of two or more consecutive omitted rim vertices would give an omitted vertex with exactly one neighbor in \(F\), so all omitted vertices are isolated. Conversely, any rim set whose complement is independent is a fort. Inclusion-minimality is equivalent to the omitted set being a maximal independent set of \(C_n\). The same conclusion excludes the nonminimal full-rim set.

If \(h\in F\), write \(F=\{h\}\cup D\). Every omitted rim vertex already has one neighbor in \(F\), so the fort condition is exactly that \(D\) dominate \(C_n\). Inclusion-minimality under deletion of rim vertices is equivalent to \(D\) being a minimal dominating set, because domination is monotone under addition. The hub is essential precisely when \(D\) alone is *not* a fort. If a dominating \(D\) is a rim-only fort, every omitted vertex has two neighbors in \(D\). Such a vertex can never be a private neighbor of a selected vertex. A minimal dominating set requires each selected vertex to have some private closed-neighborhood witness; therefore every selected vertex must be isolated in \(D\) as its own private witness. Thus \(D\) and \(R\setminus D\) are both independent. This happens only on even cycles, for the two alternating choices. Conversely, those two sets are minimal dominating and rim-only forts. Hence hub-containing minimal forts correspond bijectively to all minimal dominating sets of \(C_n\), except those two alternating sets when \(n\) is even.

**2. Enumeration of hub-free forts.** In a maximal independent set, consecutive selected rim vertices have either one or two omitted vertices between them. Marking the omitted vertices (the fort) by \(z\), the block polynomial is \(zx^2+z^2x^3\). A cyclic list of \(k\) blocks, of total rim order \(n\), labels each set \(n/k\) times after distinguishing one selected vertex. Therefore the generating function of the hub-free distribution, including the nonphysical order-two term, is \(-x\partial_x\log A(x,z)\). The order-two term is \(2zx^2\), which must be removed since the cycle family starts at \(n=3\).

**3. Enumeration of minimal dominating sets.** Between successive vertices of a nonempty minimal dominating set \(D\), let \(g\in\{0,1,2\}\) count omitted vertices; these are all possibilities since a longer omitted run has an undominated vertex. A selected vertex having left and right gaps \((a,b)\) has a private witness if and only if \(a=2\), or \(b=2\), or both \(a\geq1\) and \(b\geq1\). The allowed ordered pairs are consequently
\[
(0,2),(1,1),(1,2),(2,0),(2,1),(2,2).
\]
With row and column states \(0,1,2\), define the weighted transition matrix
\[
T(x,z)=\begin{pmatrix}
0&0&zx^3\\
0&zx^2&zx^3\\
zx&zx^2&zx^3
\end{pmatrix}.
\]
An arc whose next gap is \(b\) contributes \(zx^{1+b}\), marking the selected vertex and its following omitted run. For each \(k\), the trace \(\operatorname{tr}T^k\) counts cyclic gap lists with \(k\) distinguished selected vertices. Thus the minimal-dominating-set enumerator, including an artificial order-two term, is
\[
\sum_{k\geq1}\frac nk[x^n]\operatorname{tr}T^k
=[x^n]\left(-x\frac{\partial}{\partial x}\log\det(I-T)\right).
\]
Direct determinant expansion gives \(\det(I-T)=B(x,z)\). For the actual wheel, multiply this polynomial by \(z\) to mark the hub and exclude the two alternating configurations in every even order. The subtraction \(2z^2x^2/(1-zx^2)\) simultaneously removes the artificial order-two term and, for even \(n\geq4\), the two forbidden hub-containing sets of size \(n/2+1\). Adding the hub-free enumerator proves the displayed rational function.

**4. Fort packing, fractional transversal and integer zero forcing.** The smallest hub-free fort has \(a=\lceil n/2\rceil\) rim vertices: it is the complement of a maximum independent set of \(C_n\). The smallest hub-containing minimal fort has exactly \(b=\lceil n/3\rceil\) rim vertices: this is the domination number of \(C_n\). A minimum dominating set of that size is not a rim-only fort whenever \(n\ne4\), since \(b<a\); at \(n=4\), choose two adjacent rim vertices instead of the alternating pair. This supplies a genuine hub-containing minimal fort of size \(b+1\) for every \(n\geq3\).

Average any feasible fractional transversal over the rotations of the rim. Its total weight is preserved and its weights become \(u\) on each rim vertex and \(v\) at the hub. All fort inequalities reduce exactly to \(au\geq1\) and \(v+bu\geq1\) with \(u,v\geq0\), because all other forts contain at least the corresponding minimum number of rim vertices. Since \(b\leq a<n\), minimizing \(nu+v\) gives \(u=1/a\) and \(v=1-b/a\), proving the fractional formula. The equality cases follow by elementary comparison of the two ceiling functions.

At most two forts can be pairwise disjoint: at most one can contain the hub, and every hub-free fort uses at least \(\lceil n/2\rceil\) rim vertices; for even \(n\), two disjoint hub-free forts exhaust the rim. Two disjoint forts do exist. For even \(n\), use the two alternating rim-only forts. For odd \(n\), take a maximal independent rim set \(I\), and use \(R\setminus I\) and \(\{h\}\cup I\). This proves \(\operatorname{ft}=2\). A hub together with two consecutive rim vertices forces around the rim when \(n\geq4\); for \(n=3\) the wheel is \(K_4\). Conversely, no initial pair can make a first force, since each selected vertex has at least two unselected neighbors. Hence \(Z=3\).

**5. Asymptotics.** At \(z=1\), the weighted transfer determinant is \(B(x,1)=1-x^2-x^3-x^4+x^6\). Its least positive zero \(\alpha\) is \(0.713639173536901\ldots\). The nonnegative irreducible transfer matrix \(T(\alpha,1)\) has Perron eigenvalue \(1\); all its nonzero entries increase with \(x>0\), so this crossing is simple. No other zero has modulus \(\alpha\): equality in the complex-entry spectral-radius bound would force the phases of both self-loop contributions of lengths \(2\) and \(3\) to be \(1\), so the phase of \(x\) must be \(1\). Consequently \(-x\partial_x\log B(x,1)\) has a unique dominant simple pole with residue yielding coefficient \(\alpha^{-n}\). The hub correction is bounded and the hub-free contribution has smaller exponential growth, determined by \(1-x^2-x^3\), whose least positive zero is greater than \(\alpha\). Therefore \(M_n(1)\sim\alpha^{-n}\), with leading coefficient \(1\), as claimed.

## Verification
The independent stand-alone script `verify_wheel_forts.py` constructs each wheel directly, enumerates all nonempty vertex subsets for rim orders \(3\leq n\leq12\), and tests minimality against **all proper nonempty subsets**, not merely one-deletion checks. It compares every cardinality coefficient with two independently coded polynomial recurrences obtained from \(A\) and \(B\). It checks the earlier reported hub-containing sequence, the exact fractional weights as a feasible cover, disjoint fort packing for small orders, the determinant identity and coefficient recurrences through order \(80\). A separate numerical linear-program cross-check with an LP solver was also performed for each rim order \(3\leq n\leq12\); every optimum agreed with the closed fraction. Finite checks support but do not prove the unbounded statements.

For example,
\[
M_3(z)=6z^2,\quad M_4(z)=2z^2+4z^3,\quad
M_5(z)=10z^3,\quad M_6(z)=5z^3+3z^4.
\]

## Relationship to prior work
Cameron, Hogben, Kenter, Mojallal and Schuerger [1] define the fort-hypergraph fractional transversal and tabulate this parameter for several families, including cycles, but not wheels. The result here uses their definition without claiming it as new.

Becker, Cameron, Hanely, Ong and Previte [2, Section 5.1, Corollary 21] give a lower bound for the number of wheel minimal forts, characterize relevant maximal failed zero-forcing configurations, and explicitly list the initial hub-containing sequence. They state that they do not know an explicit formula for that sequence. The structural relationship with maximal independent and minimal dominating rim sets is consistent with their discussion; the new contributions claimed here are the exact all-cardinality wheel minimal-fort polynomial, the rational solution of their listed hub sequence, the exact fractional zero-forcing value and separation from the fort packing number, and the sharp growth constant. Ordinary cycle minimum-domination and independent-set facts are used as standard prior knowledge, not asserted as new.

## Limitations
The same-work mathematical review checks the proof and computations but is not independent certification. An unindexed or later equivalent theorem could affect publication priority. The asymptotic result concerns the labelled wheel family only; it does not assert extremality among graphs of the same order. The parameter \(Z^*\) is specifically the fort-hypergraph LP relaxation and is not the distinct three-color-game variant. The root is specified algebraically and numerically; no closed form in radicals is asserted.

## References
[1] T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904, first posted 2023-10-27, especially Definitions 2.1–2.4, Section 3 and Table 6.1. https://arxiv.org/abs/2310.17904

[2] P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963, first posted 2024-04-09, especially Corollaries 13 and 21, Proposition 20, and Section 5.1. https://arxiv.org/abs/2404.05963
