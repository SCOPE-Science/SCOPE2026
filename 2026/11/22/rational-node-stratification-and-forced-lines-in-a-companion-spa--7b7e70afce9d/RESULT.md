# Rational-node stratification and forced lines in a companion space-filling surface family

## Finding

**Theorem.** Let \(q\) be an odd prime power, \(b\in\mathbb F_q^\times\), and use the cyclic indexing convention \(X_4=X_0\). Set \(\phi_{ij}=X_i^qX_j-X_iX_j^q\) and
\[
F_b=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(bX_0+X_3)\phi_{30}.
\]
The degree-\(q+2\) surface \(S_b=V(F_b)\subset\mathbb P^3_{\mathbb F_q}\) contains every \(\mathbb F_q\)-rational projective point. Its entire rational singular locus is
\[
\operatorname{Sing}(S_b)(\mathbb F_q)
=\{P_t=[t^{-3}:t:t^{-1}:1]:t\in\mathbb F_q^\times,\;b=t^5-t^3\}.
\]
Each such point has quadratic tangent form
\[
Q_t=b u_0^2-t u_0u_1+t^{-3}u_1^2-t^{-1}u_1u_2+t u_2^2
\]
in local affine coordinates \(X_3=1\), with \(u_i=X_i-(P_t)_i\) for \(0\le i\le2\). Its Hessian determinant is exactly \(2t(2t^2-3)\); therefore it is an ordinary node (type \(A_1\) over an algebraic closure) exactly when \(2t^2\ne3\). In the exceptional case \(2t^2=3\), its tangent cone has corank exactly one and \(S_b\) contains the \(\mathbb F_q\)-line through \(P_t\) with affine direction \((1,t^2,1/2)\).

Across every \(b\in\mathbb F_q^\times\), there are exactly \(q-3\) rational singular parameter-point pairs. Exactly two of these pairs have corank one when \(3/2\) is a nonzero square in \(\mathbb F_q\), and none otherwise. The exceptional parameters are distinct, equal to \(b=(3/4)t\) for the two roots \(t^2=3/2\). In characteristic three no exceptional pair exists.

## Assumptions and scope

All fields have odd characteristic. The parameter \(b\) is nonzero; the corresponding companion matrix is invertible. Rational singular means a singular point whose coordinates lie in \(\mathbb F_q\). This theorem does **not** classify singularities over \(\overline{\mathbb F_q}\) that are not rational. A corank-one quadratic tangent cone does not, on its own, determine the complete higher-order analytic germ. No geometric irreducibility statement is needed.

## Proof

**1. Rational gradient and normalization.** Every \(\phi_{ij}\) vanishes on \(\mathbb F_q\)-rational points, proving the space-filling assertion. Write the four linear coefficients as \(L_0=X_1\), \(L_1=X_2\), \(L_2=X_3\), \(L_3=bX_0+X_3\). At a rational point \(x\), the Frobenius terms have zero formal derivative, and the gradient is the cyclic expression
\[
\partial_{X_k}F_b(x)=L_{k-1}(x)x_{k-1}-L_k(x)x_{k+1},\quad k\pmod 4.
\]
In particular the vanishing equations are
\[
(bx_0+x_3)x_3=x_1^2,\quad x_1x_0=x_2^2,\quad x_2x_1=x_3^2,\quad x_3x_2=(bx_0+x_3)x_0.
\]
They force all four coordinates to be nonzero: if \(x_1=0\), the second and third equations force \(x_2=x_3=0\), and the fourth then gives \(bx_0^2=0\), impossible. If \(x_2=0\), the third forces \(x_3=0\), the second forces \(x_0x_1=0\), and the first then forces \(x_1=0\); if \(x_3=0\), the third forces \(x_1x_2=0\) and the other equations similarly force every coordinate to vanish. If \(x_0=0\), the second forces \(x_2=0\), then the third \(x_3=0\), then the first \(x_1=0\). Each contradicts projectivity.

Normalize \(x_3=1\) and write \(x_1=t\in\mathbb F_q^\times\). The third equation gives \(x_2=t^{-1}\), the second gives \(x_0=t^{-3}\), and the first gives \(b=t^3(t^2-1)=t^5-t^3\). Conversely, for any \(t\in\mathbb F_q^\times\) satisfying this equation, all four displayed gradient equations vanish at \(P_t\); the last is automatic because \(bt^{-3}+1=t^2\). Since \(F_b\) vanishes at all rational points, the claimed rational singular set is exact. The parameter \(t\) is uniquely recovered as \(x_1/x_3\).

**2. Quadratic tangent form.** In characteristic \(p>2\), one has \(q\ge3\). Around a rational point the degree-at-most-two contribution of \(\phi_{i,i+1}\) is the *linear* expression \((P_t)_i u_{i+1}-(P_t)_{i+1}u_i\), since the other Frobenius terms have degree at least \(q\). Multiplying by the linear parts of the \(L_i\), and setting \(u_3=0\), yields
\[
Q_t=(t^5-t^3)u_0^2-tu_0u_1+t^{-3}u_1^2-t^{-1}u_1u_2+tu_2^2.
\]
Its symmetric Hessian and determinant are
\[
H_t=\begin{pmatrix}
2(t^5-t^3)&-t&0\\
-t&2t^{-3}&-t^{-1}\\
0&-t^{-1}&2t
\end{pmatrix},\qquad
\det H_t=2t(2t^2-3).
\]
The lower-right entry \(2t\) is nonzero. At a zero of the determinant, the lower-right two-by-two minor also remains invertible: it is \(4t^{-2}-t^{-2}=3t^{-2}\), and the equation \(2t^2=3\) cannot hold in characteristic three. Thus the exceptional corank is *exactly one*. Elsewhere the nondegenerate quadratic term yields an ordinary double point by the formal Morse lemma in odd characteristic.

**3. Incidence census.** The condition \(b\ne0\) excludes precisely \(t=\pm1\) from \(\mathbb F_q^\times\), giving \(q-3\) ordered pairs \((b,P_t)\). The equation \(2t^2=3\) has either two nonzero roots or none. Characteristic three gives none. If roots exist, \(t^5-t^3=t^3/2=3t/4\), so the two exceptional \(b\)'s are opposite and nonzero.

**4. Lines at the exceptional boundary.** Assume \(2t^2=3\). Direct multiplication shows \(H_t(1,t^2,1/2)^{\mathsf T}=0\). Let \(L_t\subset\mathbb P^3\) be the line spanned by the rational vectors \(P_t=(t^{-3},t,t^{-1},1)\) and \(v_t=(1,t^2,1/2,0)\). Its \(q+1\) rational points all lie on \(S_b\), since \(S_b\) is space-filling. The restriction of the homogeneous degree-\(q+2\) form \(F_b\) to \(L_t\cong\mathbb P^1\) vanishes to order at least **three** at \(P_t\): the constant and linear terms vanish by singularity and the quadratic term vanishes in the Hessian-kernel direction. It vanishes at each of the other \(q\) rational points as well. A nonzero homogeneous form of degree \(q+2\) on a projective line cannot have at least \(q+3\) zeros counted with multiplicities. Hence \(F_b|_{L_t}=0\) identically. This proves the asserted containment for every odd prime power, not only the fields tested computationally.

## Verification

The accompanying standalone `CHECK.py` expands the ten monomials of \(F_b\), computes all first and second partial derivatives directly, enumerates all rational projective points independently for prime fields \(\mathbb F_p\) with \(p\in\{3,5,7,11,13,19\}\), checks the predicted singular-point lists and Hessians, and tests all rational points of the exceptional lines. It passed for all six prime fields, with singular incidence totals \(0,2,4,8,10,16\) and exceptional incidence totals \(0,2,0,0,0,2\), respectively. The proof above supplies the infinite-prime-power argument; finite tests are not substitutes for it.

## Relationship to prior work

Bourgeois-Conti, Moon, Perez, and Warren give this companion construction, show that some parameters avoid rational singularities, and derive the necessary parameter relation in their Proposition 7.2 and Theorem 7.4. The present contribution is a converse and **complete rational incidence classification in projective dimension three**, together with the exact Hessian/node criterion, a two-point exceptional boundary, and the forced contained lines. The earlier plane-filling-curve study of Asgarli and Ghioca and the complete-intersection space-filling-curve study of Campbell and collaborators treat different geometric families; their statements do not imply this companion-surface singularity stratification. Existing calculations on other finite-field surfaces may share similar counting methods, but not this claim.

## Limitations

Only \(\mathbb F_q\)-rational singular points are enumerated; additional singularities over extension fields or \(\overline{\mathbb F_q}\) may occur. The exceptional points are proved to have Hessian corank one and a contained line, but their full analytic singularity types are not determined. No claim of geometric smoothness, absolute irreducibility, a complete line census, or optimality of a parameter choice is made. Indexed searches and inspection of the most directly relevant papers cannot guarantee exhaustive publication priority.

## References

1. V. Bourgeois-Conti, H.-B. Moon, E. Perez, and A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (first publicly posted 2026-11-11), especially §§4, 7–8. https://arxiv.org/html/2611.15768v1
2. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (2023). https://arxiv.org/html/2307.03072v1
3. [C. Campbell and coauthors], *On algebraic space filling curves*, arXiv:2310.09293v1 (2023). https://arxiv.org/html/2310.09293v1
