# Exact primitive-idempotent Jordan-product fibers and a sharp dimension-four saturation threshold

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd cardinality, and let \(V\) be a \(d\)-dimensional vector space, \(d\ge2\), with a nondegenerate symmetric bilinear form \(B\). Put \(Q(v)=B(v,v)\). The spin-factor Jordan algebra \(J=k1\oplus V\) has multiplication
\[
(a,u)\circ(b,v)=(ab+B(u,v),\;av+bu).
\]
Its proper nonzero idempotents, which are primitive, are exactly
\[
e_x=\left(\frac12,\frac x2\right),\qquad Q(x)=1.
\]
For any \((c,w)\in J\), let \(P(c,w)\) count the ordered pairs \((e_x,e_y)\) of primitive idempotents with \(e_x\circ e_y=(c,w)\). The following formulas give **every** prescribed fiber, for every finite field, dimension and form type.

Write \(\chi\) for the quadratic character of \(k\), extended by \(\chi(0)=0\), and \(D=\det B\) modulo squares. For an integer \(j\ge0\), a sign \(\eta\in\{\pm1\}\), and \(a\in k\), define the explicit quadratic representation count
\[
\mathcal R_{j,\eta}(a)=\begin{cases}
\delta(a=0),&j=0,\\
q^{j-1}+\eta q^{j/2-1}\bigl(q\delta(a=0)-1\bigr),&j>0\text{ even},\\
q^{j-1}+\eta q^{(j-1)/2}\chi(a),&j\text{ odd}.
\end{cases}
\]
Here the argument \(\eta\) is immaterial for \(j=0\), and for a nondegenerate \(j\)-dimensional quadratic form it is \(\chi((-1)^{\lfloor j/2\rfloor}\det Q)\).

If \(c\ne2Q(w)\), then \(P(c,w)=0\). For \(c=2Q(w)\), put \(s=4w\) and \(h=1-4Q(w)\). Then
\[
\boxed{P(2Q(w),w)=\begin{cases}
\mathcal R_{d,\,\chi((-1)^{\lfloor d/2\rfloor}D)}(1),&w=0,\\
\mathcal R_{d-1,\,\chi((-1)^{\lfloor(d-1)/2\rfloor}D/Q(s))}(h),&Q(w)\ne0,\\
q\,\mathcal R_{d-2,\,\chi((-1)^{\lfloor(d-2)/2\rfloor}(-D))}(1),&w\ne0,\ Q(w)=0.
\end{cases}}
\]
This is a closed formula; no implicit enumeration or undefined sum remains. The final case is zero when \(d=2\) because \(\mathcal R_{0,\eta}(1)=0\).

**Sharp saturation transition:** For **every** nondegenerate form in dimension \(d\ge4\), and every vector \(w\in V\), the paraboloid target \((2Q(w),w)\) is an actual product of two primitive idempotents. In dimension three the transition is controlled exactly by the discriminant:
\[
\chi(-D)=1\implies \text{every paraboloid target is attained};
\]
whereas if \(\chi(-D)=-1\), precisely \(q^2-1\) paraboloid targets are missing, namely those with \(w\ne0\) and \(Q(w)=0\). Dimension two can also have missing targets. Thus dimension four is the smallest dimension guaranteeing full paraboloid support for every isometry class and every odd field.

## Assumptions and scope
All factors are primitive idempotents, not arbitrary algebra elements or the two trivial idempotents \(0\) and \(1\). The multiplication is the Jordan product, not the associative product of projectors. Input pairs are ordered. The two quadratic-form isometry types are both allowed; the nonzero determinant square class is basis-independent. When \(d=2\), the isotropic-quotient formula uses the defined zero-dimensional representation count. Characteristic two and degenerate bilinear forms are not included.

## Proof
**Idempotent classification.** An element \((a,u)\) is idempotent exactly when \(a^2+Q(u)=a\) and \((2a-1)u=0\). For \(u=0\), only \(a=0,1\) work. Otherwise, \(a=1/2\) and \(Q(2u)=1\). These idempotents are primitive: any decomposition into two nonzero orthogonal idempotents would sum two elements with scalar coordinate \(1/2\), hence have scalar coordinate \(1\), whereas \(e_x\) has scalar coordinate \(1/2\).

**A universal quadratic hyperplane fiber.** If \(e_x\circ e_y=(c,w)\), the vector coordinate gives \(x+y=4w=:s\). Because \(Q(x)=Q(y)=1\), the polarization identity yields \(B(x,y)=(Q(s)-2)/2\), hence the scalar output is \(c=(1+B(x,y))/4=Q(s)/8=2Q(w)\). Thus the paraboloid equation is necessary. Write uniquely \(x=s/2+z\), \(y=s/2-z\). The two norm-one requirements are equivalent to
\[
B(s,z)=0,\qquad Q(z)=1-\frac{Q(s)}4=1-4Q(w)=h.
\]
Conversely any such \(z\) constructs an ordered pair, so the fiber is precisely the number of vectors of norm \(h\) in the perpendicular hyperplane \(s^\perp\).

**Nondegenerate hyperplanes.** For \(s=0\), the perpendicular space is all of \(V\), and the condition becomes \(Q(z)=1\). If \(Q(s)\ne0\), the direct decomposition \(V=ks\oplus s^\perp\) makes \(s^\perp\) nondegenerate of dimension \(d-1\) and determinant square class \(D/Q(s)\). Its norm count is the middle formula.

**Isotropic hyperplanes.** Suppose \(s\ne0\) with \(Q(s)=0\). Choose an isotropic partner \(t\) such that \(B(s,t)=1\) and \(Q(t)=0\), possible by first choosing a partner and subtracting a suitable multiple of \(s\). The Gram determinant of their hyperbolic plane is \(-1\). The orthogonal complement \(W\) has dimension \(d-2\) and determinant square class \(-D\). Since \(s^\perp=ks\oplus W\) and the quadratic form is independent of the coordinate on \(ks\), every \(W\)-solution has exactly \(q\) lifts. Here \(h=1\), giving the last displayed formula, including dimension two.

**Explicit representation numbers.** For any nondegenerate quadratic form \(Q_j\), diagonalize its Gram matrix. For a nontrivial additive character \(\psi\), the product of one-variable Gaussian sums gives \(\sum_x\psi(tQ_j(x))=\chi(t)^j\chi(\det Q_j)G^j\), where \(G^2=\chi(-1)q\). Additive Fourier inversion on the equation \(Q_j(x)=a\) gives exactly \(\mathcal R_{j,\eta}(a)\) above. The empty vector space contributes only at zero. This proves the complete fiber formula in every odd prime-power field.

**Full-support boundary.** A nondegenerate form in at least two variables represents every nonzero finite-field element, and every nondegenerate form in at least three variables represents zero nontrivially. If \(d\ge4\), the perpendicular space at nonisotropic \(s\) has dimension at least three and represents every \(h\); for nonzero isotropic \(s\), its nondegenerate quotient has dimension at least two and represents \(1\). The \(s=0\) case is also nonempty. Thus every paraboloid target occurs.

For \(d=3\), a nonisotropic perpendicular plane always represents \(h\), and the zero-vector target occurs. But for nonzero isotropic \(s\), the quotient is one-dimensional and represents \(1\) precisely when its determinant is a square, that is, when \(\chi(-D)=1\). If it does, the fiber contains exactly \(2q\) ordered pairs; otherwise none. Every nondegenerate ternary form has exactly \(q^2-1\) nonzero isotropic vectors (the zero-level count is \(q^2\)); hence precisely that many targets are missing in the negative-sign case. Finally, a hyperbolic form in dimension two has nonzero isotropic \(s\), for which the quotient is dimension zero and cannot represent \(1\), proving sharpness of the dimension-four universal guarantee.

## Verification
The attached `verify_idempotent_products.py` constructs all norm-one vectors, independently multiplies every ordered pair of their associated primitive idempotents, and compares actual multiplicities at **every** possible target to the formula. Complete target enumeration passed in eighteen cases, including odd prime fields \(q=3,5,7\) in dimensions from two through five as available, and the independently implemented extension field \(\mathbb F_9\) in dimensions two and three. Both discriminant classes are tested where indicated; the observed support threshold agrees with the proof. Run `python verify_idempotent_products.py` (standard Python only). The contemporaneous output is `idempotent_output.txt`. Finite checks supplement the all-field argument and do not prove it by themselves.

## Relationship to prior work
Kaygorodov, Lopatin and Popov (2015) give the spin-factor multiplication and discuss derivations, not prescribed primitive-idempotent products. The published finite-field Peirce-incidence study for symmetric \(2\times2\) Jordan matrices counts how many primitive idempotent **multiplication images** contain a given matrix, not how many ordered primitive-idempotent pairs have a given product; it covers only a three-dimensional Jordan algebra. A published all-arity rank-one **associative** matrix-idempotent product census counts \(P_1P_2\cdots P_r\), not the symmetrized Jordan product, and does not imply the displayed arbitrary-dimensional spin-factor fibers by its stated formulas. The recent Gogić–Tomašević preprint on Jordan idempotent words concerns representability and minimal word length, and its publicly available abstract confines its spin-factor conclusions to quadratically closed fields. Its complete original text could not be accessed for a detailed comparison, so it remains a priority risk. Previously known spin-factor square-root counts do not determine the primitive-idempotent restricted pair distribution by an unrestricted polarization convolution. The present exact perpendicular-hyperplane fiber law, exceptional isotropic support obstruction, and sharp universal dimension-four boundary are the assessed contribution.

## Limitations
The theorem concerns exactly two proper primitive-idempotent factors and odd finite fields with nonsingular quadratic forms. It does not address idempotent words of greater length, arbitrary factors, characteristic two, or degeneracy. The low-dimensional symmetric-matrix Peirce incidence problem is related but has a different incidence condition. Exhaustive novelty searches do not prove bibliographic uniqueness; an unidentified older projective-quadric secant-count identity might imply the result. In particular, the full text of the 2026 Gogić–Tomašević idempotent-word preprint remained inaccessible; it might contain a related factorization lemma. Independent historical-priority and mathematical audit are not performed.

## References
- I. Kaygorodov, A. Lopatin, Y. Popov, *Jordan algebras admitting derivations with invertible values*, arXiv:1511.00742v1, first publicly posted 2015-11-02, https://arxiv.org/abs/1511.00742.
- *The finite-field Peirce-incidence obstruction for symmetric Jordan matrices*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-finite-field-peirce-incidence-obstruction-for-symmetric-jord--0430690c0891.
- *Exact all-arity product fibers of rank-one idempotents over finite fields*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-all-arity-product-fibers-of-rank-one-idempotents-over-fini--dfb5f1d17166.
- I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581 (2026), abstract available at https://arxiv.org/abs/2609.23581; original full text not obtained.
- R. Lidl and H. Niederreiter, *Finite Fields*, background quadratic-character and Gaussian-sum formulas.
