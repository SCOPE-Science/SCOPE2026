# Unit-order profiles and Tutte reconstruction for radical-square-zero quiver algebras

## Finding
Let \(Q\) be a finite quiver with \(n\ge1\) vertices, \(m\) nonloop arrows and \(h\) loops. Multiple arrows and oriented cycles are allowed. Let \(H\) be the undirected loopless multigraph obtained by retaining every nonloop arrow as an unoriented edge, and set \(A_q=\mathbb F_qQ/J^2\), where \(q=p^f\) and \(J\) is the arrow ideal. For an integer \(d\ge1\) dividing \(q-1\), define
\[
P_H(t,z)=\sum_{S\subseteq E(H)}t^{\kappa(V,S)}z^{m-|S|}(1-z)^{|S|},
\]
where \(\kappa(V,S)\) is the number of connected components of the spanning multigraph \((V,S)\). The following are exact counts in the unit group \(U_q=A_q^\times\):
\[
\#\{u\in U_q:u^d=1\}=P_H(d,q),\qquad
\#\{u\in U_q:u^{pd}=1\}=d^nq^{m+h}.
\]
Moreover, each labelled assignment of \(d\)-th roots of unity to the vertices gives exactly one conjugacy class among the units satisfying \(u^d=1\), of size \(q^{c}\), where \(c\) is the number of nonloop arrows connecting unequal labels. Conjugacy classes from different label assignments are disjoint. In particular, there are exactly \(d^n\) such conjugacy classes.

Every unit has order dividing \(p(q-1)\). For each \(s\mid(q-1)\), the numbers of units of **exact** orders \(s\) and \(ps\) are respectively
\[
C_s(q)=\sum_{d\mid s}\mu(s/d)P_H(d,q),\qquad
C_{ps}(q)=\sum_{d\mid s}\mu(s/d)\bigl(d^nq^{m+h}-P_H(d,q)\bigr),
\]
where \(\mu\) is the number-theoretic Möbius function. Thus the formulas determine the entire element-order distribution, including characteristic two.

Finally, as \(q\) ranges over all prime powers, the complete element-order distributions of \(U_q\) determine \(n\), the number of loop arrows \(h\), and the ordinary two-variable Tutte polynomial of \(H\). They do **not** determine arrow orientations, loop placements, or a unique underlying multigraph.

## Assumptions and scope
All algebras are unital and finite-dimensional, and unit orders are multiplicative orders in \(A_q^\times\). The quiver has no restriction on orientation, connectedness, parallel arrows, or loops. Each loop contributes one independent radical coordinate but no edge of \(H\). The prime \(p\) is the characteristic of \(\mathbb F_q\); the integer \(d\) always divides \(q-1\), so it is prime to \(p\). We count actual units, not units modulo conjugation, except where a conjugacy-class assertion is explicitly made.

## Proof
Write \(A_q=D\oplus J\), with \(D=\bigoplus_{v\in V}\mathbb F_q e_v\cong\mathbb F_q^n\) and \(J^2=0\). A unit has the unique form \(u=\lambda+a\), where each \(\lambda_v\ne0\) and \(a=\sum_{e\in Q_1}a_e e\). For an arrow \(e:i\to j\), the coefficient of \(e\) in \(u^r\), for \(r\ge1\), is
\[
a_e\sum_{k=0}^{r-1}\lambda_i^{r-1-k}\lambda_j^k.
\]
This follows by expanding \((\lambda+a)^r\) and discarding terms with at least two factors in \(J\).

If \(u^d=1\), the diagonal coefficient equation gives \(\lambda_v^d=1\) for every vertex. Because \(d\mid(q-1)\), exactly \(d\) choices are available at each vertex. If \(\lambda_i\ne\lambda_j\), the arrow sum equals \((\lambda_i^d-\lambda_j^d)/(\lambda_i-\lambda_j)=0\), and \(a_e\) is arbitrary. If \(\lambda_i=\lambda_j\), the sum equals \(d\lambda_i^{d-1}\ne0\), hence \(a_e=0\). Thus loops always vanish; a differently labelled nonloop arrow contributes precisely \(q\) possible coefficients. For each label assignment \(c\), the number of units is \(q^{c_H(c)}\). Summing over label assignments proves the first count and the coloring form
\[
P_H(d,q)=\sum_{c:V\to\{1,\ldots,d\}}q^{c_H(c)}.
\]
The polynomial form follows from the identity \(q^{[c_i\ne c_j]}=q+(1-q)[c_i=c_j]\) on every edge: expand the edge product, and a selected edge set \(S\) forces constant labels on each of its \(\kappa(V,S)\) connected components.

For fixed \(c\), conjugation of the diagonal element \(\lambda\) by \(1+x\), \(x\in J\), gives \((1+x)\lambda(1-x)=\lambda+x\lambda-\lambda x\). On an arrow \(i\to j\), the coefficient changes by \((\lambda_j-\lambda_i)x_e\). Exactly the coefficients on unequally labelled arrows can be varied, and they can be varied independently. Therefore the full set counted for \(c\) is one \((1+J)\)-orbit and hence one \(U_q\)-conjugacy class. Conjugation acts trivially on the commutative quotient \(A_q/J\), so distinct diagonal labels cannot be conjugate. This proves the class refinement.

If \(u^{pd}=1\), its diagonal components are \(d\)-th roots of unity because \(\mathbb F_q^\times\) has order prime to \(p\). Conversely, every unit with those diagonal components has \(u^d\in1+J\), and \((1+x)^p=1\) for all \(x\in J\). Hence all \(m+h\) arrow coordinates are free, giving the second count. In particular, the exponent of \(U_q\) divides \(p(q-1)\). Möbius inversion on the divisor lattice of \(q-1\), separately for orders with and without their factor \(p\), yields the two exact-order formulas.

To prove the reconstruction assertion, note that for each integer \(d\ge1\) there are infinitely many prime powers \(q\equiv1\pmod d\): take powers of any fixed prime not dividing \(d\) with exponents divisible by its multiplicative order modulo \(d\), with the case \(d=1\) immediate. The order profile at such \(q\) gives \(P_H(d,q)\). For fixed \(d\), these infinitely many values uniquely determine the polynomial \(P_H(d,z)\), and varying \(d\) over positive integers uniquely determines \(P_H(t,z)\). Now \(P_H(t,1)=t^n\) recovers \(n\), and \(\deg_zP_H(t,z)=m\), since for integer \(t\ge n\) there is a proper vertex coloring and its highest-degree coefficient is nonzero. The invertible formal substitution
\[
Z_H(t,v)=(1+v)^mP_H\bigl(t,(1+v)^{-1}\bigr)
=\sum_{S\subseteq E(H)}t^{\kappa(V,S)}v^{|S|}
\]
recovers the Fortuin–Kasteleyn polynomial. Its standard rank-nullity transform determines the ordinary Tutte polynomial. Finally, the order profile gives \(\#\{u:u^p=1\}=q^{m+h}\), so after recovering \(m\), it also recovers \(h\). This argument reconstructs polynomial invariants, not the orientation or graph isomorphism type.

## Verification
A standalone Python 3 checker, `torsion_tutte_checker.py`, enumerates actual units of \(\mathbb F_qQ/J^2\) using arrow-basis multiplication. It directly computes their orders, compares with the two Möbius-inversion formulas, and checks total-group order. Across \(49\) quiver/field cases (twelve quivers over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), plus the five-cycle over \(\mathbb F_3\)), including loops, parallel and opposing arrows, triangles, and different orientations, it prints `ALL_DIRECT_UNIT_ORDER_CASES_PASSED 49`. The small extension field is realized explicitly with a degree-two irreducible polynomial.

For example, with \(q=3\) and arrows \(1\to2\to3\), the exact order counts are \(C_1=1\), \(C_2=31\), \(C_3=8\), and \(C_6=32\), totaling \(72=(3-1)^3\cdot3^2\). For any orientation of the five-cycle over \(\mathbb F_3\), the exact order counts are \(1,991,242,6542\) in orders \(1,2,3,6\), with total \(7776\). This five-cycle is not a comparability graph, so it also illustrates scope beyond earlier incidence-algebra coloring formulas. These finite tests supplement, but do not replace, the all-field proof.

## Relationship to prior work
Iovanov and Sistko develop the quiver-with-relations and radical-splitting framework for basic algebras; their analysis concerns maximal subalgebras, not unit-group element-order distributions. Qureshi and Reis develop power-map functional graph methods for abelian and flower groups, including selected cyclic semidirect products; that scope does not directly provide a unit-order census for arbitrary quivers. Sokal's Fortuin–Kasteleyn/Tutte identities are classical and used here without a novelty claim. The new combination is the exact torsion-conjugacy and element-order distribution for every square-zero quiver algebra, with reconstruction of its underlying loopless graph's Tutte polynomial. Some special graph/field cases may already be derivable from earlier group-theoretic results.

## Limitations
The claimed scope is the square-zero radical quotient only; higher radical powers require additional terms in unit powers. The formulas are not a graph-isomorphism classification and cannot recover arrow orientations or individual loop placements. The recovery theorem uses the order profiles over an infinite family of field sizes and does not assert recovery from a single field. A mathematically equivalent torsion count might appear in earlier semidirect-product or finite-algebra literature not identified in the inspected sources. Independent verification beyond the supplied proof and finite enumerations has not been performed.

## References
1. M. C. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762 (first public version 2017-05-02), especially §4.1.
2. C. Qureshi and L. Reis, *On the Functional Graph of the Power Map over Finite Groups*, arXiv:2107.00584 (first public version 2021-07-01), especially §§2.4, 3, 4.2.
3. A. D. Sokal, *The Multivariate Tutte Polynomial (Alias Potts Model) for Graphs and Matroids*, arXiv:math/0503607 (2005), especially §§1–2.3; standard background identity.
