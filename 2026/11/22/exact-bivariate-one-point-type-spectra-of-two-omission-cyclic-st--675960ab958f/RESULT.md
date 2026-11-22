# Exact bivariate one-point type spectra of two-omission cyclic standard examples and a negative two-thirds Gaussian correlation

## Finding
Let \(n\ge3\). Define the height-two poset \(Q_n\) on distinct, individually named elements \(a_i,b_j\), \(i,j\in\mathbb Z/n\mathbb Z\), by
\[
a_i<b_j\quad\Longleftrightarrow\quad j\notin\{i,i+1\}\pmod n.
\]
Embed it as an induced finite subposet of the countable universal homogeneous partial order \(\mathbb D\). For every complete nonalgebraic singleton type \(p\) over these parameters, let \(\ell(p)\) and \(u(p)\) be the number of named elements strictly below and above a realization, respectively. Write
\[
P_n(x,y)=\sum_p x^{\ell(p)}y^{u(p)}.
\]
Let
\[
H(x,y)=\begin{pmatrix}1+x&y\\1&y\end{pmatrix},\qquad
E_n(z)=z^n((1+z)^n-1)+n(z^{n-1}+2z^n+z^{n+1}).
\]
Then the **complete bivariate type polynomial** is
\[
\boxed{P_n(x,y)=\operatorname{tr}(H(x,y)^n)+E_n(x)+E_n(y).}
\]
In particular, with \(L_m\) the Lucas numbers \(L_0=2,L_1=1,L_{m+2}=L_{m+1}+L_m\),
\[
\boxed{P_n(1,1)=L_{2n}+2^{n+1}+8n-2.}
\]
Exactly \(L_{2n}-2^{n+1}+1\) types have both a named predecessor and named successor. **The two-sided types first outnumber the one-sided types at exactly \(n=7\), and dominate at every subsequent size.** For a uniformly chosen type, this two-sided event has probability
\[
1-4(2/\varphi^2)^n(1+o(1)),\qquad \varphi=(1+\sqrt5)/2.
\]
If \((X_n,Y_n)=(\ell(p),u(p))\) for a uniformly sampled type, put \(\rho=(5-\sqrt5)/10\). The **joint Gaussian limit** is
\[
\boxed{\frac{(X_n,Y_n)-n(\rho,\rho)}{\sqrt n}\ \Longrightarrow\
N_2\!\left((0,0),\frac{\sqrt5}{25}\begin{pmatrix}3&-2\\-2&3\end{pmatrix}\right).}
\]
In particular the limiting correlation of the predecessor and successor counts is exactly \(-2/3\). The case \(n=3\) is included, with the same formulas and no assumed asymptotic approximation. In the notation of previously studied cyclic-width incidence posets, this family has width \(r=n-2\) after cyclic relabeling; the previously proved short-arc formula assumes \(n\ge 2r+1\), so its stated domain does not include these growing-width cases beyond \(n=3\). The formal extrapolation of that short-arc mixed-type formula first disagrees at \(n=6\): it predicts \(192\) rather than the true \(195\) two-sided types.

## Assumptions and scope
The old poset has exactly the stated comparabilities; its two layers are independent internally. All old elements are named separately, so no quotient by cyclic or dihedral symmetries is taken. Algebraic types equating the new point to a parameter are excluded. For each nonalgebraic singleton type, the homogeneous extension property makes its order-comparison profile finite and complete. The probability law is uniform **over types**, not over vertices in the infinite structure. The normal convergence is as the integer \(n\to\infty\).

## Proof
**1. Types are compatible ideal–filter pairs.** For a new point \(z\), set \(L=\{q\in Q_n:q<z\}\) and \(U=\{q\in Q_n:z<q\}\). The necessary and sufficient conditions on \((L,U)\) are that \(L\) is a downset, \(U\) is an upset, and every element of \(L\) is strictly below every element of \(U\); this last condition includes disjointness. These conditions exactly prevent new transitivity contradictions. Any such finite extension occurs in \(\mathbb D\); homogeneous extension and ultrahomogeneity give one complete nonalgebraic type per pattern.

**2. Two-sided part.** When both \(L\) and \(U\) are nonempty, height two forces \(L\subseteq\{a_i\}\) and \(U\subseteq\{b_j\}\). Put an edge between \(a_i\) and \(b_j\) precisely when they are *not* comparable in \(Q_n\), namely \(j=i\) or \(j=i+1\). This forbidden-comparison bipartite graph is a single cycle on \(2n\) vertices. The valid two-sided choices are exactly independent sets of this cycle meeting both color classes, with \(x\) and \(y\) marking the occupied vertices of the two classes. The usual two-state transfer matrix \(M(z)=\left(\begin{smallmatrix}1&z\\1&0\end{smallmatrix}\right)\) gives the full weighted independent-set polynomial
\[
C_n(x,y)=\operatorname{tr}((M(x)M(y))^n)=\operatorname{tr}(H(x,y)^n).
\]
Removing independent sets confined to a single class and restoring the empty set once gives the genuinely two-sided polynomial
\[
C_n(x,y)-(1+x)^n-(1+y)^n+1.
\]

**3. One-sided part.** Let \(I_n(z)\) count ideals of \(Q_n\), weighted by their sizes. Choose the subset \(B\) of upper vertices in the ideal. With \(B=\varnothing\), the lower vertices are all optional, contributing \((1+z)^n\). For nonempty \(B\), taking every lower vertex contributes \(z^n((1+z)^n-1)\). Extra freedom in the lower layer occurs precisely if \(B\) is a singleton, when its two absent predecessor relations permit omission of one or both corresponding lower vertices, or if \(B\) consists of two consecutive upper vertices, when exactly one lower vertex may additionally be omitted. There are \(n\) singleton and \(n\) consecutive-pair choices for \(n\ge3\); a subset of three or more upper vertices has no common incomparable lower vertex. Therefore
\[
I_n(z)=(1+z)^n+z^n((1+z)^n-1)+n(z^{n-1}+2z^n+z^{n+1}).
\]
The map \(a_i\mapsto b_{-i}\), \(b_j\mapsto a_{-j}\), with indices modulo \(n\), is an order-reversing symmetry: a direct check gives \(j\notin\{i,i+1\}\) if and only if \(-i\notin\{-j,-j+1\}\). Thus the filter size polynomial equals \(I_n\). Types with \(U=\varnothing\) or \(L=\varnothing\) contribute \(I_n(x)+I_n(y)-1\). Adding the two-sided part proves the stated formula.

**4. Total counts and dominance.** At \(x=y=1\), the weighted independent-set count of a cycle of length \(2n\) is \(L_{2n}\). Substitution proves the total-count formula. The one-sided type count is \(2I_n(1)-1=2^{n+2}+8n-3\), and the two-sided count is \(L_{2n}-2^{n+1}+1\). Since \(L_{2n}=\varphi^{2n}+\varphi^{-2n}\), and \(\varphi^2>2\), division gives the two-sided concentration and its exact leading failure probability. To locate the sharp finite dominance threshold, put \(\Delta_n=L_{2n}-3\cdot2^{n+1}-8n+4\), the difference between two-sided and one-sided counts. Direct evaluation at \(n=3,4,5,6,7\) gives \(\Delta_n=-50,-77,-105,-106,23\). The identity \(L_{2n+2}=3L_{2n}-L_{2n-2}>2L_{2n}\), valid for \(n\ge2\), gives \(\Delta_{n+1}-2\Delta_n=L_{2n+2}-2L_{2n}+8n-12>0\) for \(n\ge2\). Thus positivity at seven propagates and no earlier size is positive.

**5. Joint central limit.** For \(x,y\) near \(1\), the eigenvalues of \(H(x,y)\) solve
\[
\lambda^2-(1+x+y)\lambda+xy=0.
\]
The larger eigenvalue \(\lambda_+(x,y)=\tfrac12(1+x+y+\sqrt{(1+x+y)^2-4xy})\) is positive, simple, analytic near \((1,1)\), and at that point equals \(\varphi^2\), whereas the smaller eigenvalue equals \(\varphi^{-2}\). The correction polynomials \(E_n(x)+E_n(y)\), in a fixed complex neighborhood of \((1,1)\), are exponentially smaller than \(\lambda_+(x,y)^n\) in absolute value. Consequently the joint moment-generating function of \((X_n,Y_n)\) has the uniform local form
\[
\mathbb E[e^{sX_n+tY_n}]
=\left(\frac{\lambda_+(e^s,e^t)}{\lambda_+(1,1)}\right)^n(1+O(\eta^n))
\]
for some \(0<\eta<1\), whenever \(s,t\) lie in a sufficiently small complex neighborhood of zero. Differentiation of \(\log\lambda_+(e^s,e^t)\) at the origin yields gradient \((\rho,\rho)\) and Hessian
\[
\Sigma=\frac{\sqrt5}{25}\begin{pmatrix}3&-2\\-2&3\end{pmatrix}.
\]
The eigenvalues of \(\Sigma\) are \(\sqrt5/25\) and \(\sqrt5/5\), both positive. Setting \(s,t\) to order \(n^{-1/2}\) and subtracting the linear term, the logarithm of the characteristic function tends to the quadratic form \(-\tfrac12(s,t)\Sigma(s,t)^\top\). Lévy's continuity theorem gives the asserted nondegenerate bivariate normal limit; covariance normalization gives correlation \(-2/3\). This proves the claim. \(\square\)

## Verification
The executable `verify.py` enumerates the independent three-way comparison status of every old vertex, checks both transitivity directions against the exact incidence matrix, and compares every coefficient of its bivariate polynomial against an independently computed transfer recurrence and explicit correction terms. Checks at \(n=3,4,5,6\) yield respectively \(56,109,225,496\) types and agree in every bidegree. The checker also compares the total to the Lucas closed form. Symbolic differentiation of the analytic eigenvalue formula verifies the stated gradient and Hessian; those calculations can be reproduced with the elementary derivative expressions in the proof, independently of the finite enumerator. This finite computation does not replace the infinite central-limit proof.

## Relationship to prior work
Standard-example posets and their dimension theory are classical; Biró, Hamburger and Pór (2013) study order dimension and contain no extension-type polynomial or Gaussian limit. The ideal/filter model for finite-poset singleton extensions and the complexity of counting them are existing tools, not asserted as new. A published uniform cyclic-incidence theorem treats cyclic-width \(r\) posets under the explicit hypothesis \(n\ge2r+1\), used to make a unique shortest cyclic arc. After cyclic relabeling, the present dense family is its width \(r=n-2\) boundary regime, outside that theorem's hypotheses for all \(n\ge4\). The published short-arc mixed-type expression is not generally valid in this regime (already failing at \(n=6\)). Its fixed-width three-incidence specialization is different for growing \(n\), and does not imply the exact dense-regime polynomial or Gaussian law. An existing exact pair-type calculation over ordinary standard examples with only one missing matching edge per lower point addresses a different base and the ungraded ordered-pair invariant. The classical cycle independence polynomial and transfer-matrix method are reused openly, with no claim of novelty for the Lucas sequence or hard-core central-limit technique. The proposed contribution is the exact complete two-variable **logical type profile for co-crowns**, including all one-sided corrections, together with its precise two-sided dominance and jointly normalized predecessor/successor law.

## Limitations
The results apply only to this explicit fixed two-omission cyclic family and to nonalgebraic singleton types; higher-arity type spectra and arbitrary posets are not classified. The normal limit concerns uniformly sampled types, not randomly sampled points of \(\mathbb D\). Closely related independent-set and generalized-crown literature may contain an equivalent formulation not identified here; a historical-priority review remains necessary. The proof is self-contained apart from standard Fraïssé homogeneity and characteristic-function convergence; no independent mathematical audit has been performed.

## References
1. C. Biró, P. Hamburger and A. Pór, *Standard Examples as Subposets of Posets*, arXiv:1311.6518v1, 26 November 2013, https://arxiv.org/html/1311.6518v1.
2. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892 (2010), https://arxiv.org/abs/1009.2892.
3. W. T. Trotter Jr., *Dimension of the crown \(S_n^k\)*, Discrete Mathematics 8 (1974), 85–103, https://doi.org/10.1016/0012-365X(74)90113-7.
4. *Uniform cyclic-incidence one-type spectra and a sharp algebraic growth law*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-uniform-cyclic-incidence-one-type-spectra-and-a-sharp-algebraic--11e9e11c0647.
5. *Silver-ratio one-point type spectrum and linear two-sided cuts of cyclic triple-incidence posets*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-silver-ratio-one-point-type-spectrum-and-linear-two-sided-cuts-o--508681ae39af.
