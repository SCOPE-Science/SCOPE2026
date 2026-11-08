# Rational tangent matching and quadratic-point exclusion for minimal space-filling complete intersections

## Finding

**Theorem.** Let \(q\geq2\) be a prime power and let \(C=V(G,F)\subset\mathbb P^3_{\mathbb F_q}\) be a geometrically smooth, geometrically integral, scheme-theoretic complete-intersection curve, where \(G,F\) are nonzero homogeneous forms of degrees \(q+1\) and \(q+2\), respectively. Assume that \(C(\mathbb F_q)=\mathbb P^3(\mathbb F_q)\). Then:

1. The degree-\(q+1\) surface \(S=V(G)\) is smooth. Its defining form is a nondegenerate alternating Frobenius form, and it is projectively equivalent over \(\mathbb F_q\) to
   \[G_0=X_0^qX_1-X_0X_1^q+X_2^qX_3-X_2X_3^q.\]
2. Every rational line \(L\subset\mathbb P^3\) meets \(C\) set-theoretically in precisely the \(q+1\) points of \(L(\mathbb F_q)\). If \(L\not\subset S\), the intersection is reduced, of length \(q+1\); if \(L\subset S\), the intersection has length \(q+2\) and consists of those \(q+1\) rational points, with exactly one of them doubled.
3. The rational tangent lines \(T_PC\), as \(P\) ranges over \(C(\mathbb F_q)\), are **exactly once each** the \((q+1)(q^2+1)\) rational lines lying on \(S\). Equivalently, tangent-line assignment is a perfect matching between the points and lines of the symplectic generalized quadrangle \(W(3,q)\) defined by \(G\).
4. The curve has no closed points of degree two over \(\mathbb F_q\); indeed, no geometric point of \(C\) outside \(C(\mathbb F_q)\) lies on any rational line. Hence
   \[\#C(\mathbb F_{q^2})=\#C(\mathbb F_q)=q^3+q^2+q+1.\]

The genus is \(g(C)=1+\frac{(q+1)(q+2)(2q-1)}2\). Writing its Hasse--Weil numerator as \(P_C(T)=1+c_1T+c_2T^2+\cdots\), all such curves have the same first two coefficients,
\[c_1=q^3+q^2,\qquad c_2=\frac{(q^3+q^2)^2+q^3+q}{2}.\]

## Assumptions and scope

The base field is exactly \(\mathbb F_q\), where \(q\) is an arbitrary prime power, including even characteristic. All embeddings, complete intersections, rational lines, and Frobenius actions are over this field. Geometric smoothness and geometric integrality are assumed; these hypotheses exclude a rational line component. The theorem concerns complete intersections of the minimal possible bidegree \((q+1,q+2)\), not arbitrary space-filling curves or all curves of the same total degree without the complete-intersection property. An \(\mathbb F_q\)-line means a projective line defined over \(\mathbb F_q\), not an arbitrary geometric line. A closed point of degree two is equivalent to a pair of non-rational \(\mathbb F_{q^2}\)-points conjugate over \(\mathbb F_q\).

## Proof

**Line-restriction lemma.** Let \(L\cong\mathbb P^1_{\mathbb F_q}\) be any rational line with rational homogeneous coordinates \([s:t]\). The squarefree binary form
\[\Delta(s,t)=s^qt-st^q\]
vanishes exactly at the \(q+1\) rational points of \(L\), all simply. Because every one of those points belongs to \(C\), both \(G|_L\) and \(F|_L\) vanish there. Divisibility by the product of the \(q+1\) rational linear factors gives
\[G|_L=\lambda_L\Delta,\qquad F|_L=\ell_L\Delta,\]
where \(\lambda_L\in\mathbb F_q\) and \(\ell_L\in\mathbb F_q[s,t]_1\) is a possibly zero linear form. If both coefficients were zero, \(L\subset C\); geometric integrality and \(\deg C=(q+1)(q+2)>1\) exclude this. When \(\lambda_L\ne0\), the scheme-theoretic intersection ideal in \(L\) is \((\Delta)\), so all \(q+1\) points are simple. When \(\lambda_L=0\), one has \(\ell_L\ne0\), and the intersection ideal is \((\ell_L\Delta)\). The linear form \(\ell_L\) has exactly one rational projective root, which is already a simple root of \(\Delta\); this gives the asserted unique doubled point. In both cases there are no additional geometric intersection points. This proves statement 2.

**Alternating form and nondegeneracy.** The homogeneous degree-\(q+1\) component of the ideal of \(\mathbb P^3(\mathbb F_q)\) is spanned by the six forms \(X_i^qX_j-X_iX_j^q\) for \(i<j\) (the standard Frobenius-minor description, recalled in the source). Thus
\[G(X)=\sum_{i<j}a_{ij}(X_i^qX_j-X_iX_j^q),\quad a_{ij}\in\mathbb F_q.\]
Let \(B\) be the alternating bilinear form on \(\mathbb F_q^4\) with these coefficients. For rational independent vectors \(u,v\) representing a line \(L\), direct expansion gives \(G(su+tv)=B(u,v)(s^qt-st^q)\), up to the harmless choice of sign for \(B\). Accordingly \(L\subset S\) precisely when \(B(u,v)=0\). At a rational point represented by \(u\), the differential of \(G\) is, up to sign, \(v\mapsto B(u,v)\). If \(B\) were degenerate, its radical would contain a nonzero rational vector \(u\). The point \([u]\) belongs to \(C\) because \(C\) contains all rational points, but \(dG_{[u]}=0\); the two-row Jacobian of the complete intersection would have rank at most one, contrary to geometric smoothness of \(C\). Hence \(B\) is nondegenerate. Every nondegenerate alternating form of dimension four has a symplectic basis over \(\mathbb F_q\), proving statement 1.

**Rational tangents.** For \(P\in C(\mathbb F_q)\), the tangent line \(T_PC\) is rational and is contained in the tangent plane to \(S\) at \(P\). If \(u\) represents \(P\), the tangent-plane condition on a rational direction \(v\) is \(B(u,v)=0\). The line \(\langle u,v\rangle\) therefore lies entirely in \(S\). Conversely, for any rational line \(L\subset S\), the line-restriction lemma says \(F|_L=\ell_L\Delta\), with \(\ell_L\ne0\); let \(P_L\) be its unique rational root. The intersection multiplicity of \(C\) and \(L\) at \(P_L\) is two, hence \(L=T_{P_L}C\) because \(C\) is smooth at that point. The other rational points on \(L\) are simple intersections, so \(L\) is tangent at precisely one rational point. Every rational tangent belongs to this family and every member occurs exactly once.

For completeness, every rational point of the symplectic projective space lies on \(q+1\) isotropic rational lines (the one-dimensional subspaces of \(u^\perp/\langle u\rangle\)). Every such line contains \(q+1\) rational points. Double-counting point--line incidences gives \((q+1)(q^2+1)=q^3+q^2+q+1\) isotropic lines, proving statement 3 and the claimed perfect matching.

**Quadratic-point and zeta consequences.** If \(Q\in C(\mathbb F_{q^2})\setminus C(\mathbb F_q)\), its Frobenius conjugate \(Q^{(q)}\) is distinct, and the line \(\langle Q,Q^{(q)}\rangle\) is defined over \(\mathbb F_q\). The line-restriction lemma says that its intersection with \(C\) has no non-rational geometric points, a contradiction. Indeed, the lemma rules out any non-rational geometric point lying on any rational line. It follows that both extension counts equal \(N=q^3+q^2+q+1\). Adjunction for a smooth complete intersection in \(\mathbb P^3\) gives \(2g-2=(q+1)(q+2)(2q-1)\). If \(S_n=q^n+1-\#C(\mathbb F_{q^n})\) denotes the \(n\)-th power sum of Frobenius eigenvalues, then \(S_1=-q^3-q^2\) and \(S_2=-q^3-q\). Newton's identities \(c_1=-S_1\), \(2c_2=S_1^2-S_2\) give the displayed zeta coefficients. This proves statement 4 and the corollaries.

## Verification

The theorem for all prime powers is proved above; no finite enumeration is required for its validity. Two independent arithmetic checks were made on the published minimum-degree complete-intersection examples, using ordinary Python without optional dependencies:

- `python3 verify_binary_example.py` enumerates all 15 rational points and all 35 rational lines in \(\mathbb P^3(\mathbb F_2)\). It verifies that the tangent lines at the 15 points are exactly the 15 rational lines contained in the specified degree-three surface and that the curve has precisely 15 points over \(\mathbb F_4\).
- `python3 verify_ternary_example.py` enumerates all 40 rational points and 130 rational lines in \(\mathbb P^3(\mathbb F_3)\). It identifies 40 lines contained in the specified degree-four surface and checks that the curve has precisely 40 points over \(\mathbb F_9\).

The scripts validate point counts and rational line incidences for the two concrete displayed examples, **not** geometric smoothness of those examples or the infinite-\(q\) theorem. Smoothness of the original examples is supplied by the motivating published paper, and the new theorem states smoothness as a hypothesis.

## Relationship to prior work

Campbell, Dedvukaj, McCormick, Moon, and Morales construct geometrically smooth space-filling complete-intersection curves of degrees \((q+1,q+2)\) for \(q\leq7\) and prove the minimum degree within the complete-intersection class. Their Lemma 3.2 supplies the nondegenerate Frobenius surface, Corollary 3.5 gives the minimality bound, and Table 1 displays examples. The elementary Frobenius-minor ideal is also stated in their Section 2. These earlier constructions, minimum-degree bounds, and symplectic form are not claimed as new. The new assertion is the **universal exact scheme-theoretic line-section classification**, its induced **bijection of rational tangent lines with all symplectic isotropic lines**, and the resulting **uniform exclusion of all quadratic closed points with fixed initial zeta coefficients**. The inspected full source does not state these results. They are not implied by a mere example or a minimum-degree bound without the line-restriction argument.

The standard finite-geometric construction of \(W(3,q)\) and the classical factorization of \(s^qt-st^q\) are used as known tools. Related work on space filling curves on \(\mathbb P^1\times\mathbb P^1\), on rational point bounds, and on random complete intersections studies different ambient settings or asymptotic regimes. None of the inspected material supplied the asserted tangent matching for these curves. Complete historical priority remains subject to independent literature review.

## Limitations

No claim is made that all symplectic point--line perfect matchings arise from smooth space-filling complete intersections, that every prime power admits such a curve, or that the full zeta numerator is common to all examples. Existence is established in the cited paper for \(q\leq7\); the theorem is conditional on the presence of a smooth geometrically integral complete intersection of the stated type. No assertions concern lines not defined over \(\mathbb F_q\), curves embedded in \(\mathbb P^n\) for \(n\ne3\), or arbitrary non-complete-intersection space fillers. Independent mathematical and historical-priority audits have not been performed.

## References

1. A. Campbell, F. Dedvukaj, D. McCormick III, H.-B. Moon, and J. Morales, *On algebraic space filling curves*, arXiv:2310.09293v1 (first arXiv posting 2023-10-17), https://arxiv.org/abs/2310.09293 . See Sections 2--5, especially Lemma 3.2, Corollary 3.5, and Table 1.
2. A. Bucur and K. S. Kedlaya, *The probability that a complete intersection is smooth*, J. Théor. Nombres Bordeaux 24 (2012), 541--556, DOI:10.5802/jtnb.810 (general background, not a source of the line-section theorem).
3. M. Homma, point bounds for nondegenerate curves in projective three-space (as cited in reference 1, Theorem 3.4); used only for contextual comparison, not as an input to the proof.
