# Unique Galois-line cover of an osculating plane and its supersolvable incidence

## Finding
Let \(q=2^n\ge4\), \(K=\mathbb F_{q^2}\), and \(Q=q^2\). Higashine classified the Galois lines of the natural embedding of the maximal characteristic-two curve
\[
y^{q+1}=x+x^2+\cdots+x^{q/2},\qquad (x,y)\longmapsto(x:y:1:y^2)
\]
in projective three-space [1]. We determine a new incidence and extremal covering invariant of that classified configuration.

Let \(H_\infty\subset\mathbb P^3_K\) denote the osculating plane \(Z=0\), with coordinates \([X:Y:W]\). The Galois lines contained in this plane are exactly
\[
L_t:\ X+tY+t^2W=0\quad(t\in K),\qquad
M_d:\ Y+dW=0\quad(d\in K).
\]
**Theorem.** Among all Galois lines in the ambient three-space, the unique smallest set of lines whose union contains every point of \(H_\infty(K)\) is
\[
\mathcal A_q=\{L_t:t\in K\}\cup\{M_d:d\in K^\times\}.
\]
Its cardinality is exactly \(2Q-1\). Its projective plane arrangement has precisely \(\binom{Q}{2}\) ordinary triple intersection points and one ordinary \((Q-1)\)-fold point; there are no other intersection points, in particular no nodes. The point of multiplicity \(Q-1\) is modular, so the central arrangement is supersolvable and is free with logarithmic exponents \((1,Q-2,Q)\).

Let \(U_q=H_\infty\setminus\bigcup_{H\in\mathcal A_q}H\). For every integer \(r\ge1\),
\[
\#U_q(\mathbb F_{Q^r})=(Q^r-Q)(Q^r-Q+2),\quad
Z(U_q,T)=\frac{(1-QT)^{2Q-2}}{(1-Q^2T)(1-T)^{Q(Q-2)}}.
\]
In particular, all \(Q^2+Q+1\) points of \(H_\infty(K)\) lie on the selected Galois lines.

## Assumptions and scope
Throughout, \(n\) is any integer at least two, \(K=\mathbb F_{2^{2n}}\), and projective geometric lines are interpreted over an algebraic closure when needed. Covering refers **only** to the \(K\)-rational points of the distinguished osculating plane, not to its geometric points or points over every extension. The complement zeta function uses its natural \(K\)-structure. 'Ordinary' means distinct smooth linear branches with pairwise distinct tangent directions over the algebraic closure.

The line classification and the fact that \(H_\infty\) is osculating are prior results of [1], not original claims here. In its original notation, the lines \(L_t\) are \(\ell_b^{(1)}\) with \(t=b^q\), and \(M_d\) are \(\ell_d^{(3)}\). Since the Frobenius map is a permutation of \(K\) and \(b^{2q}=t^2\), this reparametrization is exact. The remaining Galois lines \(\ell_c^{(2)}\) meet \(H_\infty\) only in the point \([1:0:0]\) [1, Theorem 1].

## Proof
**1. Forced lines and unique minimum.** The point \(P_t=[t:1:0]\in H_\infty(K)\) lies on \(L_t\) and no other \(L_u\), and on no \(M_d\). Nor can an ambient Galois line of type \(\ell_c^{(2)}\) contain it, since such a line meets \(H_\infty\) only at \(N=[1:0:0]\). Therefore every Galois-line covering of \(H_\infty(K)\) contains all \(Q\) lines \(L_t\).

Fix \(d\in K\) and consider the affine row \(R_d=\{[x:d:1]:x\in K\}\). Its points on any \(L_t\) have coordinates \(x=t^2+dt\). For \(d=0\), squaring permutes \(K\), hence \(\{L_t\}\) covers \(R_0\), so \(M_0\) is not needed. For \(d\ne0\), the additive map \(t\mapsto t^2+dt\) has kernel exactly \(\{0,d\}\); therefore its image has \(Q/2\) points and its complement in \(K\) has \(Q/2\) points. Every omitted point of \(R_d\) lies on only the Galois line \(M_d\) among the remaining candidate lines, and it is not \(N\). Thus every \(M_d\) with \(d\ne0\) is forced. The selected \(M_d\) cover all the nonzero rows, the \(L_t\) cover \(R_0\) and the \(Q\) points \(P_t\) at \(W=0\), and every \(M_d\) contains \(N\). This gives a cover of size \(2Q-1\), with each member forced, hence it is the unique minimum even when all ambient Galois lines are allowed.

**2. Complete incidence.** For distinct \(t,u\in K\), direct subtraction in characteristic two gives
\[
L_t\cap L_u=P_{t,u}:=[tu:t+u:1].
\]
This point lies on \(M_{t+u}\), with \(t+u\ne0\). It lies on no third \(L_v\), because the polynomial \(V^2+(t+u)V+tu\) has exactly the two distinct roots \(t,u\). Distinct unordered pairs give distinct points by their elementary symmetric functions. For fixed \(d\ne0\), each intersection \(L_t\cap M_d\) equals \(L_t\cap L_{t+d}\cap M_d\). Thus the \(Q(Q-1)/2\) points \(P_{t,u}\) are exactly all intersections not among the \(M\)-pencil. All \(Q-1\) distinct lines \(M_d\) meet at \(N=[1:0:0]\), and none of the \(L_t\) passes through \(N\). Since each component is a distinct line, its local branches at every crossing are smooth and transverse, yielding the claimed ordinary multiplicities and excluding further intersections. Every crossing other than \(N\) lies on a line \(M_d\) through \(N\); hence \(N\) is a modular point and the line arrangement is supersolvable.

**3. Free exponents.** Put \(m=Q-1\). The pencil \(\{M_d:d\ne0\}\) consists of \(m\) lines through \(N\). Add the lines \(L_t\) in any order. Every new \(L_t\) avoids \(N\) and meets the existing \(M_d\) in exactly \(m\) different points. Every intersection with a previously added \(L_u\) is already one of these, since \(L_t\cap L_u\in M_{t+u}\) and \(t+u\ne0\). Thus the restriction to each newly added \(L_t\) consists of precisely \(m\) distinct points. The pencil is free with central exponents \((0,1,m-1)\); the rank-two restriction has exponents \((1,m-1)\). The addition–deletion theorem for hyperplane arrangements, valid over the base field in arbitrary characteristic, first gives \((1,1,m-1)\) after the first \(L_t\), then successively \((1,r,m-1)\) after \(r\) of the \(L_t\), for every \(1\le r\le Q\). Hence the final central arrangement is free with exponents \((1,Q,Q-2)\), as asserted. This proves freeness without assuming characteristic-zero intersection formulas.

**4. Extension-field counts and zeta function.** Every crossing of the reduced divisor is \(K\)-rational, and the same incidence and transverse multiplicities persist over all extensions. Put \(E=Q^r\). Each of the \(2Q-1\) lines has \(E+1\) rational points. To count the union without double counting, subtract \(Q-2\) at the \((Q-1)\)-fold point and subtract \(2\) at each of the \(\binom Q2\) triple points. Therefore
\[
\#D_q(\mathbb F_E)=(2Q-1)(E+1)-(Q-2)-2\binom Q2.
\]
Subtract this from \(\#\mathbb P^2(\mathbb F_E)=E^2+E+1\) to obtain \(\#U_q(\mathbb F_E)=(E-Q)(E-Q+2)\). Exponentiating \(\sum_{r\ge1}\#U_q(\mathbb F_{Q^r})T^r/r\) gives the stated zeta function. In particular the characteristic polynomial of the central arrangement factors as \((T-1)(T-Q)(T-Q+2)\). No infinite claim rests on finite numerical experiments.

## Verification
The standalone standard-Python program `verify_galois_cover.py` implements exact binary-field arithmetic, checks the complete rational point-incidence multiplicity profile and deletion witnesses over \(\mathbb F_{16}\) and \(\mathbb F_{64}\), and checks pair intersections, all pairwise distinct triple points, and exact row-image sizes over \(\mathbb F_{16}\), \(\mathbb F_{64}\), and \(\mathbb F_{256}\). The complete incidence check is finite and does not replace the four uniform proof steps above. Run `python verify_galois_cover.py` (standard library only). Its expected final output is `All exact finite checks passed. General validity follows from the proof, not these tests.`

## Relationship to prior work
Higashine [1] supplies the full Galois-line classification and Galois group labels. This theorem instead solves the finite-plane extremal covering problem and determines a new intrinsic arrangement profile for the Galois lines; those covering, intersection, supersolvability, freeness, and extension-field statements are not asserted in [1]. Kühne–Szemberg–Tutaj-Gasińska [2] construct different characteristic-two line arrangements supported on projected finite projective geometries, each having only triple intersections, whereas the present arrangement has one high-multiplicity modular point and is characterized by the maximal-curve's Galois lines. Dimca–Sticlaru [3] discuss supersolvability in characteristic zero, providing general context but not the positive-characteristic family or cover. The argument explicitly proves the distinction and does not infer novelty from search absence alone.

## Limitations
The theorem is a consequence of the classified line families plus new finite-geometric analysis; it is not an independent classification of Galois projections. Its covering conclusion is over the specific field \(K\) and the specified osculating plane. Supersolvable freeness is proved using the standard addition–deletion theorem in arbitrary characteristic; we do not claim projective or logarithmic rigidity beyond the stated exponents. Earlier unindexed equivalent finite-geometry formulations remain a residual originality risk. This work has not undergone independent mathematical validation.

## References
[1] Kazuki Higashine, *Galois lines for the maximal curve with the second largest genus in characteristic two*, arXiv:2611.08810v1, first publicly submitted 2026-11-06, https://arxiv.org/abs/2611.08810 .

[2] Lukas Kühne, Tomasz Szemberg, Halszka Tutaj-Gasińska, *Line arrangements with many triple points*, Rend. Circ. Mat. Palermo (2) 73 (2024), 2501–2512, https://doi.org/10.1007/s12215-024-01047-x .

[3] Alexandru Dimca, Gabriel Sticlaru, *On supersolvable and nearly supersolvable line arrangements*, arXiv:1712.03885, https://arxiv.org/abs/1712.03885 .
