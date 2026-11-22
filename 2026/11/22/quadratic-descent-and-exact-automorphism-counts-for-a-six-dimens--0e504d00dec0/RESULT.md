# Quadratic descent and exact automorphism counts for a six-dimensional centrally essential algebra family

## Finding

Let \(K=\mathbb F_q\), \(q=2^m\), \(m\ge1\). For \(\alpha,\beta\in K\), define the unital associative \(K\)-algebra \(R_{\alpha,\beta}\) with basis \(1,a,b,c_1,c_2,w\). Its radical-basis products not forced to vanish are
\[
 a^2=\alpha w,\qquad b^2=\beta w,\qquad ab=w,\quad ba=0,\qquad ac_1=c_1a=bc_2=c_2b=w.
\]
All other products among \(a,b,c_1,c_2,w\) are zero. The radical is \(J=Ka+Kb+Kc_1+Kc_2+Kw\), the center is \(K1+Kc_1+Kc_2+Kw\), and \(R_{\alpha,\beta}\) is noncommutative and centrally essential. Write \(T=\operatorname{Tr}_{K/\mathbb F_2}\) and \(Q_{\alpha,\beta}(x,y)=\alpha x^2+xy+\beta y^2\).

**Theorem (one combined classification and symmetry result).** There are exactly two \(K\)-algebra isomorphism types among the \(q^2\) displayed parameters:
\[
 R_{\alpha,\beta}\simeq_K R_{\alpha',\beta'}\quad\Longleftrightarrow\quad T(\alpha\beta)=T(\alpha'\beta').
\]
The split type, with trace zero, has \(q(q+1)/2\) parameter pairs; the anisotropic type has \(q(q-1)/2\). Moreover
\[
 |\operatorname{Aut}_K(R_{\alpha,\beta})|=
 \begin{cases}2q^7(q-1)^2,&T(\alpha\beta)=0,\\
 2q^7(q^2-1),&T(\alpha\beta)=1,
 \end{cases}
\]
and the number of square-zero elements of \(J\) is, respectively, \(q^3(2q-1)\) or \(q^3\). The automorphism group maps onto the binary orthogonal-similitude group \(\operatorname{GO}(Q_{\alpha,\beta})\) with **every fiber of cardinality \(q^7\)**. In the split case this similitude group is \((K^\times\times K^\times)\rtimes C_2\), with the involution interchanging factors; in the anisotropic case it is \(\mathbb F_{q^2}^{\times}\rtimes C_2\), with the involution acting by \(q\)-Frobenius.

In particular, the two distinct \(\mathbb F_2\)-algebras \(R_{0,0}\) and \(R_{1,1}\) become isomorphic over \(\mathbb F_{2^m}\) **if and only if \(m\) is even**. Their \(\mathbb F_2\)-linear automorphism-group orders are \(256\) and \(768\), respectively. The original binary classification is prior work; the new assertion concerns exact automorphism fibers, arbitrary binary extensions, and their arithmetic descent behavior.

## Assumptions and scope

All automorphisms and isomorphisms in the theorem are **\(K\)-linear unital algebra** maps, not unrestricted ring automorphisms. The stated classification concerns only the displayed six-dimensional family, not all centrally essential algebras over \(K\). The characteristic is exactly two and \(q\) is a positive integer power of two. The term *square-zero* refers to the literal equation \(j^2=0\) in the radical, including \(j=0\). The trace takes values in \(\mathbb F_2\), identified with \(\{0,1\}\). The displayed form has a nonsingular polar pairing for every parameter pair.

## Proof

**1. Algebra structure and intrinsic quotients.** Let \(V=Ka+Kb\), \(F=Kc_1+Kc_2\), and \(W=Kw\), so \(J=V\oplus F\oplus W\). Identify \(F\) with \(V^*\) through \(vf=fv=f(v)w\) when \(f\in F\), \(v\in V\) (that is, \(c_1(a)=1,c_1(b)=0,c_2(a)=0,c_2(b)=1\)). The radical multiplication is
\[
 (v,f,z)(u,g,z')=\bigl(B_{\alpha,\beta}(v,u)+f(u)+g(v)\bigr)w,
\]
where \(B_{\alpha,\beta}((x,y),(x',y'))=\alpha xx'+xy'+\beta yy'\). Since \(J^2=W\) and \(JW=WJ=0\), all triple products in \(J\) vanish; adjoining a unit proves associativity. The commutator is \([v,u]=(xy'+x'y)w\), so \([R,R]=W\ne0\), while \(J^2=W\), \(J^3=0\) and \(Z(R)\cap J=F\oplus W\). These quotients and \(W\) are characteristic. The algebra is centrally essential: a radical element with a nonzero \(a\)- or \(b\)-coefficient multiplies a suitable central \(c_i\) to a nonzero element of \(W\); a nonzero central element multiplies \(1\) to itself; and an element with nonzero scalar part multiplies \(w\) to a nonzero central element. This proves the required property for all nonzero elements.

**2. Necessary and sufficient linear condition.** Any \(K\)-algebra isomorphism induces \(L\in\operatorname{GL}(V)\) on \(J/(Z(R)\cap J)\), and a map \(w\mapsto t w'\). The nondegenerate alternating commutator shows \(t=\det L\). Since the square of \(v+f+z\) equals \(Q_{\alpha,\beta}(v)w\), necessarily
\[
 Q_{\alpha',\beta'}(Lv)=(\det L)\,Q_{\alpha,\beta}(v)\quad(\forall v\in V).
\tag{1}
\]
Conversely, suppose \(L\) satisfies (1), set \(t=\det L\), and map the central quotient \(F\) to \(F'\) by \(S=t(L^{-1})^*\), so \((Sf)(Lv)=t f(v)\). Choose arbitrary maps \(z:V\to W'\) and \(s:F\to W'\). Images of \(v\) have the shape \(Lv+h(v)+z(v)w'\); images of \(f\) have the shape \(Sf+s(f)w'\). The remaining requirement for products of \(V\)-elements is
\[
 h(v)(Lu)+h(u)(Lv)=tB_{\alpha,\beta}(v,u)+B_{\alpha',\beta'}(Lv,Lu).
\tag{2}
\]
The right-hand bilinear form has zero diagonal by (1), hence is alternating. In dimension two, any alternating bilinear form is determined by its value on the pair \((a,b)\). The left side induces a nonzero linear functional on the four-dimensional space \(\operatorname{Hom}_K(V,F')\), because \(L\) is invertible. Thus (2) has exactly \(q^3\) solutions \(h\). The free maps \(z\) and \(s\) each have \(q^2\) choices. Every resulting map is triangular with invertible diagonal blocks \(L,S,t\), hence an isomorphism; conversely every algebra isomorphism arises in this manner. Therefore each admissible \(L\) has exactly \(q^{3+2+2}=q^7\) lifts.

**3. Form classes and similitude counts.** The polar form of \(Q_{\alpha,\beta}\) is \(\langle (x,y),(x',y')\rangle=xy'+x'y\). The standard two-dimensional nonsingular quadratic-form classification in characteristic two, or a direct change-of-symplectic-basis calculation, gives the Arf class \(\alpha\beta\) modulo \(\{u^2+u:u\in K\}\). Over \(\mathbb F_{2^m}\), this additive image is precisely the trace-zero subspace, so (1) has a solution precisely when the two traces agree. A linear isometry of forms has determinant one because it preserves the polar form; hence it also satisfies (1). Counting parameter pairs gives \(q\) choices with \(\alpha=0\) and \((q-1)q/2\) choices with \(\alpha\ne0\) and \(T(\alpha\beta)=0\), proving the two claimed multiplicities.

For the split plane, choose coordinates with \(Q(x,y)=xy\). A similitude must either preserve or swap its two isotropic coordinate lines; there are \((q-1)^2\) of each, hence \(2(q-1)^2\). For the anisotropic plane identify \(V\) with \(\mathbb F_{q^2}\) and \(Q\) with the norm to \(K\). The similitudes are exactly \(z\mapsto uz\) or \(z\mapsto uz^q\), \(u\in\mathbb F_{q^2}^\times\), hence \(2(q^2-1)\). Combining with the lift count yields the automorphism formulas.

**4. Square-zero fibers and field descent.** For \(j=v+f+z\), \(j^2=Q(v)w\) and the possible \((f,z)\) constitute \(q^3\) choices. A split binary plane has exactly \(2q-1\) zeros, while an anisotropic binary plane has only zero, proving the square-zero counts. On extension of scalars from \(\mathbb F_2\), the form of \(R_{1,1}\) has Arf representative \(1\), with absolute trace \(m\bmod2\); the form of \(R_{0,0}\) has trace zero. Hence the claimed parity criterion holds. As a concrete isomorphism over \(\mathbb F_4=\mathbb F_2(\omega)\), \(\omega^2+\omega+1=0\), from the split source \((a,b,c_1,c_2,w)\) to the parameter-one target \((A,B,C_1,C_2,W)\), one may take
\[
 a\mapsto\omega A+B,\quad b\mapsto\omega^2 A+B+\omega^2C_2,\quad c_1\mapsto C_1+\omega^2 C_2,\quad c_2\mapsto C_1+\omega C_2,\quad w\mapsto W.
\]
Direct multiplication confirms the defining relations and invertibility; `verify.py` checks all basis products.

## Verification

The accompanying standard-library `verify.py` represents \(\mathbb F_2\), \(\mathbb F_4\) and \(\mathbb F_8\) by bit-polynomial arithmetic and enumerates every invertible two-by-two linear map to check the similarity condition, square-zero counts and scalar-extension parity. It also tests all 16 parameter pairs over \(\mathbb F_4\), including the predicted ten split and six anisotropic cases. It exhaustively checks radical associativity for \(q=2\), every possible \(q=2\) automorphism lift of the specified normal form (exactly 256 or 768), and basis multiplication for selected \(q=4\) lifts and the explicit \(\mathbb F_4\)-isomorphism. The \(q=4\) predicted automorphism count is \(294912\) for each of the two displayed models; complete enumeration of that many full algebra maps is not asserted. Reproduce with `python3 verify.py`; the literal stdout is in `verification_output.txt` and terminates `VERIFY_OK`. The infinite-field-size statements are proved above algebraically; finite checks alone would not prove them.

## Relationship to prior work

Abyzov, Lyubimtsev and Tuganbaev introduced these minimal-size centrally essential ring families in their October 2026 preprint and, in their November 2026 complete classification, proved the two isomorphism types of **Family 2 over \(\mathbb F_2\)**, including the two quadratic-form types and the 24-versus-8 square-zero-element contrast. Those facts are not presented as new. The present theorem treats the precisely specified scalar-extension family over every finite field of characteristic two and counts **every algebra automorphism** by a \(q^7\)-fold lift of quadratic similitudes. The field-extension parity criterion and the parameter census follow in this broader setting. Standard binary quadratic-form classification, including the Arf invariant and orthogonal groups, is classical; the ring-level fiber and automorphism formulas are the contribution assessed here.

## Limitations

This is a result for a single natural six-dimensional family, not a classification of all centrally essential rings in higher order. It concerns \(K\)-linear automorphisms; field-semilinear ring automorphisms are not counted. No claim is made that the binary Arf distinction, the original order-64 examples, or general orthogonal-group formulas were discovered here. Older results phrased in the language of five-dimensional nilpotent algebras, symmetric dual modules, or bilinear-form extensions may still cover some formulas; absence from searched records is not a proof of worldwide priority. Independent mathematical review has not been performed.

## References

1. A. Abyzov, O. Lyubimtsev, and A. Tuganbaev, *Finite Non-Commutative Centrally Essential Rings of Minimal Order*, arXiv:2610.36174v1, first posted 2026-10-26, https://arxiv.org/abs/2610.36174.
2. A. N. Abyzov, O. V. Lyubimtsev, and A. A. Tuganbaev, *Minimal Finite Non-Commutative Centrally Essential Rings*, arXiv:2611.16086v1, first posted 2026-11-11, especially Section 3, Lemma 3.3 and Proposition 3.4, https://arxiv.org/abs/2611.16086.
3. A. A. Tuganbaev, *Centrally Essential Rings and Semirings*, Mathematics 10 (2022), 1867, https://doi.org/10.3390/math10111867.
