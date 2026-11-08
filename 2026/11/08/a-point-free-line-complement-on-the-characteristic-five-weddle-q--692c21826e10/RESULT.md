# A point-free line-complement on the characteristic-five Weddle quartic

## Finding

Let \(k=\mathbb F_5\), and let \(W\subset\mathbb P_k^3\) be the Weddle quartic associated with the six points of the twisted cubic \([s:t]\mapsto[s^3:s^2t:st^2:t^3]\) indexed by \(\mathbb P^1(k)\). In homogeneous coordinates \([a:b:c:d]\), an equation is
\[
 f=a^2bd-a^2c^2-ab^2c+acd^2+b^4-b^2d^2-bc^2d+c^4=0.
\]
Let \(D\subset W\) be the reduced union of the fifteen secant lines joining two of these six points and the ten residual lines obtained by intersecting the planes spanned by complementary triples. Let \(U=W\setminus D\).

**Theorem.** The surface \(W\) has exactly six geometric singularities, all \(k\)-rational ordinary double points. Its \(k\)-rational projective lines are exactly the twenty-five components of \(D\). Every point of \(W(k)\) lies on \(D\), and its line-incidence profile consists of six points on five lines and sixty points on exactly two lines. Thus \(\#U(k)=0\), although \(U\) is a nonempty open surface. For all integers \(n\ge1\), putting \(Q=5^n\),
\[
\#U(\mathbb F_{5^n})=Q^2-13Q+4(-1)^nQ+60.
\]
In particular \(\#U(\mathbb F_{25})=460\), and the Hasse–Weil zeta function is
\[
 Z(U/\mathbb F_5,T)=
 \frac{(1-5T)^{13}}{(1-T)^{60}(1-25T)(1+5T)^4}.
\]
The projective surface itself has
\[
 Z(W/\mathbb F_5,T)=
 \frac1{(1-T)(1-25T)(1-5T)^{12}(1+5T)^4}.
\]

## Assumptions and scope

All point and line counts refer to the explicitly defined characteristic-five fiber and the displayed \(k\)-model. A \(k\)-rational line is a projective line defined over \(k\) and contained in \(W\). The theorem does not assert that the twenty-five lines are all geometric lines after scalar extension. Each zeta function is defined by \(Z(V/k,T)=\exp(\sum_{n\ge1}\#V(\mathbb F_{5^n})T^n/n)\). The open subscheme \(U\) is formed by deleting the reduced twenty-five-line divisor, not by resolving the nodes.

## Proof

**1. The Weddle determinant.** In \(k[a,b,c,d]\) take
\[
 q_1=ac-b^2,\quad q_2=ad-bc,\quad
 q_3=bd-c^2,\quad q_4=cd-ab.
\]
The first three vanish on the twisted cubic. Under its parametrization, the fourth restricts to \(st^5-s^5t\), whose zero divisor is precisely \(\mathbb P^1(k)\), with six distinct points. Six evaluations on the seven-dimensional vector space of binary sextics impose six independent conditions, so these four quadrics span the complete web through the six points. The Weddle locus of vertices of singular quadrics in this web is the determinant of their gradient matrix, which is \(2f\). This establishes the stated equation.

**2. The six nodes, including the geometric assertion.** Exact Gröbner-basis calculations modulo five on the projective affine charts \(a=1\) and \(d=1\) give, respectively, the full Jacobian ideals
\[
 (b-d^3,\ c-d^2,\ d^5-d)
 \quad\text{and}\quad
 (a-c^3,\ b-c^2,\ c^5-c).
\]
There are no projective singular points on \(a=d=0\), since there the remaining partial derivatives include \(4b^3\) and \(4c^3\). Hence the geometric singular set is precisely \([1:t:t^2:t^3]\) for \(t\in k\), together with \([0:0:0:1]\). The determinant of the three-variable affine Hessian is \(2\in k^\times\) at each of these six points, proving that all are ordinary double points. In particular the quartic is geometrically reduced and irreducible: any nontrivial factorization would force a positive-dimensional singular locus.

**3. Lines and the complete rational incidence.** The fifteen secants and ten complementary-triple intersections are lines on the Weddle surface (they can also be checked by direct substitution in \(f\)). The lines are distinct and all defined over \(k\). A direct exhaustive classification of projective \(k\)-lines proves that there are no others: the 156 normalized points of \(\mathbb P^3(k)\) generate exactly 806 distinct six-point sets of the form \(\mathbb P(L)(k)\), and exactly twenty-five of these sets are wholly contained in \(W(k)\). Because a binary quartic over \(k\) vanishing at all six rational points of a \(k\)-line vanishes identically, this is a complete classification of all \(k\)-lines on \(W\), not a numerical heuristic. The provided pure-Python certificate reconstructs these finite sets and identifies them with the fifteen secants and ten residual lines.

The same complete incidence calculation gives six common vertices lying on five secants each, and sixty other points lying on exactly one secant and exactly one residual line. The sixty points are distinct, and these are *all* pairwise intersections of the twenty-five lines, even geometrically: two distinct lines defined over a field that intersect over its algebraic closure have their intersection point defined over the field. Thus
\[
 \#D(k)=6+60=66,
 \qquad
 \#D(\mathbb F_{5^n})=25(Q+1)-[6(5-1)+60(2-1)]=25Q-59.
\]
The additional assertion \(W(k)=D(k)\) follows from the exact \(\#W(k)=66\) established next. It is independently checked by exhaustive substitution into \(f\).

**4. Counts on the Weddle quartic through the Kummer surface.** Let \(C/k\) be the genus-two curve \(y^2=x^5-x\), whose branch points are precisely the above six \(k\)-points. The standard odd-characteristic Weddle/Kummer correspondence gives a birational map defined over \(k\) between \(W\) and \(K=\operatorname{Jac}(C)/\{\pm1\}\): the discriminant quartic of the quadric web is the Kummer surface, and the generic singular quadric is mapped to its unique vertex. Both normal quartics have only ordinary double points; their minimal resolutions are K3 surfaces. The birational map consequently induces an isomorphism of these minimal models over \(k\).

The curve has \(\#C(k)=6\). Over \(\mathbb F_{25}\), for \(x\notin k\), the nonzero element \(u=x^5-x\) obeys \(u^5=-u\), hence \(u^4=-1\) and \(u^{12}=-1\), so it is not a square. For \(x\in k\) the right-hand side vanishes. Including infinity gives \(\#C(\mathbb F_{25})=6\). Its genus-two Weil polynomial is therefore
\[
 L_C(T)=(1-5T^2)^2.
\]
The four Frobenius eigenvalues on the Jacobian are two copies each of \(\sqrt5\) and \(-\sqrt5\).

For each \(n\), write \(\Phi_n\) for the \(n\)-th power of Frobenius on the Jacobian. Rational points of the quotient by inversion arise from geometric points with \(\Phi_n(P)=P\) or \(\Phi_n(P)=-P\). Counting both cases, with the common two-torsion correctly included, gives
\[
 \#K(\mathbb F_{5^n})=\frac12\left(\det(1-\Phi_n)+\det(1+\Phi_n)\right)
 =\begin{cases} Q^2-2Q+1,&n\text{ odd},\\ Q^2+6Q+1,&n\text{ even}.\end{cases}
\]
All sixteen two-torsion points are \(k\)-rational because all six Weierstrass points are, and the Kummer quartic has sixteen rational nodes. Its resolution replaces each rational node by a rational projective line, adding \(16Q\) to its point count. The Weddle quartic has exactly six rational nodes, whose resolution adds \(6Q\). Since the resolutions are isomorphic,
\[
 \#W(\mathbb F_{5^n})=\#K(\mathbb F_{5^n})+10Q
 =\begin{cases}Q^2+8Q+1,&n\text{ odd},\\Q^2+16Q+1,&n\text{ even}.\end{cases}
\]
In particular \(\#W(k)=66\) and \(\#W(\mathbb F_{25})=1026\), in agreement with independent exact enumeration.

**5. The open complement.** Subtracting \(\#D(\mathbb F_{5^n})=25Q-59\) from the Weddle count yields
\[
 \#U(\mathbb F_{5^n})=Q^2-13Q+4(-1)^nQ+60.
\]
Exponentiating the defining generating series of this formula proves the displayed zeta function. At \(n=1\) the count is zero; at \(n=2\) it is \(460>0\), so \(U\) is nonempty.

## Verification

Run `python3 verify.py` (Python standard library only) to enumerate all 156 projective points, all 806 projective lines, the twenty-five contained lines, the complete incidence table, and the 16,276 points of \(\mathbb P^3(\mathbb F_{25})\). The code implements \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-2)\) directly. Its final line is `VERIFY_OK` and its recorded output is `verify_output.txt`.

Run `python3 verify_singular.py` (SymPy at least version 1.12) for the exact integral determinant identity, the two characteristic-five Gröbner bases and the nonzero Hessian determinants. It also terminates with `VERIFY_OK`, recorded in `verify_singular_output.txt`. These are finite exhaustive or symbolic checks, not substitutes for the Kummer correspondence or the infinite-extension-degree argument in the proof.

## Relationship to prior work

Bolognesi (2006, §§4.2 and 5.1) establishes the classical Weddle/Kummer relation and the fifteen-plus-ten line geometry. Dolgachev (2024, §2) explains the quadric-web construction and its odd-characteristic Kummer interpretation. Shimada (2012) and Katsura–Kondō–Shimada (2013) study the supersingular K3 surface of Artin invariant one in characteristic five. Those sources supply geometric context, but the inspected portions do not state the particular characteristic-five exhaustion \(W(k)=D(k)\), the exact number of its rational lines, or the zeta function of the twenty-five-line complement. The 2026 paper on Weddle schemes was located, but its full text was not accessible in the present source inspection; its abstract addresses more general interpolation constructions. This leaves a historical-coverage risk, not a claim of proved uniqueness.

## Limitations

The assertion that there are exactly twenty-five lines concerns lines defined over \(\mathbb F_5\); no complete geometric line classification over \(\overline{\mathbb F}_5\) is asserted. The point-count formula uses the stated Weddle/Kummer correspondence in odd characteristic. The special configuration is associated with all six points of \(\mathbb P^1(\mathbb F_5)\), not an arbitrary six-point choice. The literature search cannot certify that no earlier implicit or explicitly tabulated arithmetic description exists.

## References

1. M. Bolognesi, *On Weddle Surfaces and Their Moduli*, arXiv:math/0601251, first posted 2006-01-11, especially §§4.2 and 5.1. https://arxiv.org/abs/math/0601251
2. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, Bulletin of the London Mathematical Society (2024), §2 (including the odd-characteristic Weddle description). https://doi.org/10.1112/blms.13033
3. I. Shimada, *Projective models of the supersingular K3 surface with Artin invariant 1 in characteristic 5*, arXiv:1201.4533, first posted 2012-01-22. https://arxiv.org/abs/1201.4533
4. T. Katsura, S. Kondō and I. Shimada, *On the supersingular K3 surface in characteristic 5 with Artin invariant 1*, arXiv:1312.0687, first posted 2013-12-03. https://arxiv.org/abs/1312.0687
5. L. Chiantini et al., *Weddle schemes*, arXiv:2606.25060, first posted 2026-06-23 (abstract inspected; full text not inspected). https://arxiv.org/abs/2606.25060
