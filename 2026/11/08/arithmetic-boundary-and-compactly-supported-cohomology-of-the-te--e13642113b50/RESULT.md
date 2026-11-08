# Arithmetic boundary and compactly supported cohomology of the ternary Fermat degree-two del Pezzo surface

## Finding

Let \(X/\mathbb F_3\) be the smooth degree-two del Pezzo surface
\[
X:\quad w^2=x^4+y^4+z^4\subset\mathbb P(1,1,1,2),
\]
and let \(D\subset X\) be the reduced union of **all** \(56\) geometric exceptional curves, with \(U=X\setminus D\). Every component of \(D\) is defined over \(\mathbb F_9\), but no individual component is defined over \(\mathbb F_3\). The geometric singularities of \(D\) are exactly \(28\) two-branch tangencies of contact order \(2\) and \(126\) ordinary fourfold crossings. All these points are defined over \(\mathbb F_9\).

For each integer \(m\ge1\), put \(q=3^m\). The complete extension-field point counts are
\[
\#D(\mathbb F_q)=\begin{cases}10,&m\text{ odd},\\56q-350,&m\text{ even},\end{cases}
\qquad
\#U(\mathbb F_q)=\begin{cases}q^2-9,&m\text{ odd},(q-9)(q-39),&m\text{ even}.\end{cases}
\]
Thus \(U\) is point-free exactly over \(\mathbb F_3\) and \(\mathbb F_9\), and over no other extension of \(\mathbb F_3\).

For each prime \(\ell\ne3\), the nonzero compactly supported étale cohomology of \(U_{\overline{\mathbb F}_3}\) has the following geometric Frobenius eigenvalues:

| Cohomological degree | Eigenvalues and multiplicities | Dimension |
| --- | --- | --- |
| \(2\) | \(+1\) (171), \(-1\) (180) | 351 |
| \(3\) | \(+3\) (24), \(-3\) (24) | 48 |
| \(4\) | \(+9\) (1) | 1 |

All other compactly supported cohomology groups vanish. In particular,
\[
Z(U/\mathbb F_3,T)=\frac{(1-3T)^{24}(1+3T)^{24}}{(1-9T)(1-T)^{171}(1+T)^{180}},
\qquad
Z(D/\mathbb F_3,T)=\frac{(1-T)^{170}(1+T)^{180}}{(1-3T)^{28}(1+3T)^{28}}.
\]
The divisor is anticanonically equivalent to \(D\sim-28K_X\) and has arithmetic genus \(p_a(D)=757\).

## Assumptions and scope

All statements concern the **specified** model over \(\mathbb F_3\), rather than its arbitrary quadratic twists. Its exceptional curves are geometric smooth rational curves of self-intersection \(-1\). A rational point of their union need not belong to any component defined over the field of that point. The zeta function of a finite-type \(\mathbb F_3\)-scheme \(Y\) is \(Z(Y/\mathbb F_3,T)=\exp(\sum_{m\ge1}\#Y(\mathbb F_{3^m})T^m/m)\). Geometric Frobenius conventions are used for the cohomological eigenvalues.

## Proof

**The Hermitian tangent configuration.** Smoothness follows by the partial derivatives \(2w,-x^3,-y^3,-z^3\). The branch quartic \(Q:\,x^4+y^4+z^4=0\) is the nondegenerate Hermitian curve over \(\mathbb F_9\). It has \(28\) points in \(\mathbb P^2(\mathbb F_9)\). For \(P=[p_0:p_1:p_2]\in Q(\mathbb F_9)\), its tangent line is \(\ell_P:\sum p_i^3X_i=0\). Choose \(V\in\ell_P(\mathbb F_9)\setminus\{P\}\). In characteristic three, expansion on this line gives
\[
\sum_i(sp_i+tv_i)^4=t^4\sum_i v_i^4,
\]
since \(\sum p_i^4=0\), \(\sum p_i^3v_i=0\), and \(\sum p_iv_i^3=(\sum p_i^3v_i)^3=0\). The scalar \(\sum v_i^4\) is nonzero and lies in \(\mathbb F_3^\times\), hence is a square in \(\mathbb F_9\). Consequently the inverse image of \(\ell_P\) on \(X\) is the union of two \(\mathbb F_9\)-rational smooth rational curves meeting at the one ramification point. Each has anticanonical degree one and self-intersection \(-1\) by adjunction. The standard count of \(28\) bitangents and \(56\) exceptional curves on a smooth degree-two del Pezzo in odd characteristic shows that these are all the components of \(D\).

**No rational exceptional component.** An \(\mathbb F_3\)-rational Hermitian point must have all three homogeneous coordinates nonzero; there are exactly four such points. Its tangent line is defined over \(\mathbb F_3\). Writing \(P=(1,a,b)\) with \(a,b\in\{1,-1\}\), take \(V=(1,-a,0)\) on the tangent. Then \(\sum v_i^4=2\), which is not a square in \(\mathbb F_3\). The two components above that line are therefore exchanged by \(\mathbb F_3\)-Frobenius. If \(P\notin Q(\mathbb F_3)\), the Hermitian polar tangent \(\ell_P\) is not defined over \(\mathbb F_3\), so neither component above it is individually defined there. Thus all \(56\) components appear over \(\mathbb F_9\), but none over \(\mathbb F_3\).

**Crossings and arithmetic boundary points.** The Hermitian unital has \(28\) isotropic and \(63\) anisotropic points in \(\mathbb P^2(\mathbb F_9)\). Every anisotropic point lies on exactly four of the \(28\) tangent lines: its Hermitian polar line meets \(Q\) at four points. Its inverse image consists of two \(\mathbb F_9\)-rational points, where the double cover is étale; four distinct tangent directions give an ordinary fourfold crossing at each. This accounts for \(126\) fourfold points. Above each of the \(28\) isotropic points, the two exceptional branches have local equation \(w^2=c t^4\), with \(c\ne0\); they meet tangentially to order two. No other crossings are possible because all intersections of distinct tangent lines have been accounted for.

For even \(m\), every component and every crossing is defined over \(\mathbb F_q\). Inclusion–exclusion then yields \(56(q+1)-126\cdot3-28=56q-350\). For odd \(m\), Frobenius has no invariant component. An \(\mathbb F_q\)-rational point on \(D\) is therefore contained in at least two components, hence belongs to the \(\mathbb F_9\)-rational singular support of \(D\). Since \(\mathbb F_{3^m}\cap\mathbb F_9=\mathbb F_3\), it lies in \(D(\mathbb F_3)\). The thirteen projective \(\mathbb F_3\)-points in the base plane consist of three with one nonzero coordinate, six with two, and four with three. On these strata \(x^4+y^4+z^4\) equals respectively \(1,2,0\). The double plane therefore has \(2\cdot3+4=10\) rational points, all on the boundary (the six coordinate lifts are fourfold crossings; the four branch lifts are tangencies). This proves the odd-degree boundary count.

**Surface and open counts.** Over an algebraic closure, the Picard group of a degree-two del Pezzo has rank eight, is generated by exceptional curves, and realizes its entire degree-two étale cohomology. Since all exceptional curves are \(\mathbb F_9\)-rational, normalized Frobenius on the Picard group is an involution. The Lefschetz trace formula and \(\#X(\mathbb F_3)=10\) give \(10=3^2+1+3\operatorname{tr}(\mathrm{Frob}|\operatorname{Pic})\). Hence the trace is zero and the two eigenvalues \(\pm1\) each have multiplicity four. For every \(m\),
\[
\#X(\mathbb F_{3^m})=\begin{cases}q^2+1,&m\text{ odd},\\q^2+8q+1,&m\text{ even}.\end{cases}
\]
Subtracting the boundary counts gives the two formulas for \(U\). The only zero of the odd formula with \(m\ge1\) occurs at \(m=1\), and the even formula vanishes only at \(m=2\).

**The full compact-support Frobenius spectrum.** The normalization of \(D\) is the disjoint union of \(56\) projective lines. The quotient of the constant-sheaf normalization map at a singular point with \(r\) branches has dimension \(r-1\), independently of tangency order. The total dimension of these quotients is \(28+3\cdot126=406\). Since the tangent-line incidence graph is connected, the normalization sequence gives \(\dim H^1(D)=406-56+1=351\). Every component and every branch over every singular point is \(\mathbb F_9\)-rational, so Frobenius on this weight-zero group has order dividing two. The trace formula for the proper curve \(D\), using \(\#D(\mathbb F_3)=10\), \(H^0(D)=\mathbb Q_\ell\), and the fact that \(H^2(D)\) consists of \(28\) swapped pairs with Frobenius trace zero, gives \(\operatorname{tr}(\mathrm{Frob}|H^1(D))=-9\). Thus its \(+1\)- and \(-1\)-eigen multiplicities are \(171\) and \(180\).

The localization exact sequence for \(D\hookrightarrow X\) identifies \(H^i_c(U)\) in terms of \(H^i(X)\) and \(H^i(D)\). The map \(H^2(X)\to H^2(D)\) is injective: its coordinates are intersection numbers with all exceptional curves, whose classes span the nondegenerate Picard lattice over \(\mathbb Q_\ell\). Therefore \(H^2_c(U)\cong H^1(D)\), \(H^3_c(U)\cong\operatorname{coker}(H^2(X)\to H^2(D))\), and \(H^4_c(U)\cong\mathbb Q_\ell(-2)\). Frobenius on \(H^2(D)\) has eigenvalues \(+3\) and \(-3\), each \(28\) times; subtracting the \(4+4\) eigenvalues from \(H^2(X)\) yields \(24+24\) for \(H^3_c(U)\). The other compact-support groups vanish. The cohomological determinant formula establishes both displayed zeta functions.

Finally \(D\sim-28K_X\), since each of the \(28\) bitangent inverse images lies in \(|-K_X|\). By adjunction and \(K_X^2=2\), \(p_a(D)=1+\tfrac12(-28K_X)(-27K_X)=757\). Equivalently, the local delta invariants contribute \(28\cdot2+126\cdot6=812\) against \(56\) normalization components.

## Verification

Run `python3 check_boundary.py` in a directory containing the standalone Python program. It uses standard-library exact finite-field arithmetic over \(\mathbb F_9\) and \(\mathbb F_{27}\). It enumerates all \(91\) plane points over \(\mathbb F_9\), checks the \(28+63\) Hermitian partition and all tangent incidences, checks nonsquare splitting on the four rational tangents, and independently computes \(\#X(\mathbb F_3)=10\), \(\#X(\mathbb F_9)=154\), and \(\#X(\mathbb F_{27})=730\). The expected final output is `CHECK_OK`; the actual stdout is embedded as `verification_output.txt`. Finite checks corroborate the argument but do not replace the proof for all extension degrees or the cohomology computation.

## Relationship to prior work

Kaplan's 2013 thesis, Proposition 70, identifies the same \(\mathbb F_9\)-split Fermat double-plane model and its maximal count. Knecht and Reyes (2015), Theorem 4.1, identify its \(28\) hyperflex tangents, the nine fourfold base incidences per tangent, and fullness over \(\mathbb F_9\). Those geometric facts, and the resulting absence of \(U(\mathbb F_9)\), are antecedents, not new claims. They also determine the even-extension count once the incidence structure is inserted into inclusion–exclusion.

The additional assertion assessed here is the **complete arithmetic descent** to the fixed \(\mathbb F_3\)-model, especially that all exceptional components are nonrational over \(\mathbb F_3\) while their union has exactly ten points over *every odd-degree extension*, together with the induced full compactly supported Frobenius representation of its complement. The examined primary sources do not state this result or supply the nonsquare tangent-splitting argument. Historical priority remains provisional.

## Limitations

The result does not treat arbitrary twists of the Fermat model or del Pezzo surfaces of other degrees. The two smallest point-free extensions and the \(\mathbb F_9\)-geometric incidence are already covered by prior results and should not be independently credited as discoveries. The exact finite-field program is not a substitute for proofs for all field extensions. Specialist historical coverage may be incomplete.

## References

1. N. Kaplan, *Rational Point Counts for del Pezzo Surfaces over Finite Fields and Coding Theory*, Harvard dissertation (2013), Proposition 70. Public repository record dated September 30, 2013: https://dash.harvard.edu/entities/publication/73120378-b816-6bd4-e053-0100007fdf3b .
2. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621 (first posted October 15, 2015), Sections 2 and 4, Theorem 4.1: https://arxiv.org/abs/1510.04621 .
