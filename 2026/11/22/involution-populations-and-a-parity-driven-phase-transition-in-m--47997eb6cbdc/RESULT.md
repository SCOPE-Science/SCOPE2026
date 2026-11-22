# Involution populations and a parity-driven phase transition in multivariable finite jet automorphisms

## Finding
For every odd prime power \(q\), all \(d\ge3\), and all \(N\ge4\), put
\[
 A_{d,N}=\mathbb F_q[x_1,\ldots,x_d]/(x_1,\ldots,x_d)^N,
 \qquad G_{d,N}=\operatorname{Aut}_{\mathbb F_q}(A_{d,N}).
\]
An automorphism \(F\) is counted when \(F^2=\operatorname{id}\), including the identity. These automorphisms form **exactly \(d+1\) conjugacy classes**, indexed by the number \(r\in\{0,\ldots,d\}\) of negative tangent eigenvalues. All class sizes and dimensions of fixed subalgebras follow from an explicit coefficient sum.

Write \(s=d-r\); for \(a\ge1\), set \(B_a(j)=\binom{a+j-1}{j}\), and put \(B_0(0)=1\) and \(B_0(j)=0\) for \(j>0\). Define
\[
 E_j(r,s)=\sum_{\substack{0\le h\le j\\h\text{ even}}}B_r(h)B_s(j-h),\qquad
 O_j(r,s)=B_d(j)-E_j(r,s),
\]
\[
 e_r(d,N)=\sum_{j=2}^{N-1}\bigl(rE_j(r,s)+sO_j(r,s)\bigr),
 \qquad f_r(d,N)=\sum_{j=0}^{N-1}E_j(r,s).
\]
For \(g_a(q)=\prod_{i=0}^{a-1}(q^a-q^i)\) (and \(g_0(q)=1\)), the *complete involution fixed-subalgebra spectrum* is
\[
\boxed{\mathcal T_{d,N,q}(z)=
 \sum_{r=0}^{d}\frac{g_d(q)}{g_r(q)g_{d-r}(q)}
 q^{e_r(d,N)}z^{f_r(d,N)}.}
\]
In particular, setting \(z=1\) counts all involutions. The \(r\)-class has precisely \(g_d/(g_rg_{d-r})\,q^{e_r}\) elements and every member fixes a subalgebra of dimension \(f_r\).

For each **fixed \(d\ge3\) and fixed odd \(q\)**, let \(R_N\) be the negative tangent-eigenspace dimension of a uniformly chosen square-one automorphism. There is a sharp parity-dependent phase:
\[
\boxed{
 \Pr(R_N=d)\longrightarrow1\quad(N\to\infty\text{ through odd integers}),
 \qquad
 \Pr\bigl(R_N=\lceil d/2\rceil\bigr)\longrightarrow1
 \quad(N\to\infty\text{ through even integers}).}
\]
The dominant type is **unique already at every odd \(N\ge5\) and even \(N\ge4\)** on the exponent scale \(e_r\). In even dimension it is the balanced split \(r=s\); in odd dimension it has one more negative than positive eigenvalue. The exponent gaps increase without bound on both parity subsequences.

For instance, at \(d=3,N=4\) the four exponents \((e_0,e_1,e_2,e_3)\) are \((0,22,24,18)\), whereas at \(d=3,N=5\) they are \((0,43,48,63)\). Thus the favored tangent involution switches from two negative signs to three negative signs when the jet order changes parity.

## Assumptions and scope
The ideal \((x_1,\ldots,x_d)^N\) contains precisely the monomials of total degree at least \(N\). Algebra automorphisms are unital and fix \(\mathbb F_q\) pointwise. The tangent map is the automorphism on the maximal-ideal quotient \(\mathfrak m/\mathfrak m^2\). The order-dividing-two condition includes the identity; excluding the identity does not change either limiting probability. Characteristic two, \(d\le2\), and jet order \(N\le3\) are outside the new stated domain; no assertion of a new general finite-order linearization theorem is made.

## Proof
**1. Structure of the substitution group.** Every \(F\in G_{d,N}\) is a substitution \(x_i\mapsto F_i\in\mathfrak m\) with invertible linear part. Recursive inversion degree by degree shows every such substitution is an automorphism, and the tangent homomorphism splits:
\[
 G_{d,N}=U_{d,N}\rtimes\operatorname{GL}_d(\mathbb F_q).
\]
Here \(U_{d,N}\) consists of substitutions with identity linear part, and its \(d\) coordinate polynomials have arbitrary higher coefficients. Since degree \(j\) has \(B_d(j)\) monomials,
\[
 |U_{d,N}|=q^D,\qquad D=d\sum_{j=2}^{N-1}B_d(j).
\]

**2. Every involution is conjugate to its tangent matrix.** Suppose \(F^2=\operatorname{id}\) and its linear part is \(A\), hence \(A^2=I\). Define, coordinate by coordinate, the polynomial substitution
\[
 h(X)=\tfrac12\bigl(X+A^{-1}F(X)\bigr).
\]
Its linear part is the identity, so \(h\in U_{d,N}\). Although averaging algebra homomorphisms would not be valid, this is simply the average of their coordinate substitution polynomials, which is a valid automorphism because its linear part is invertible. Direct composition gives \(h\circ F=A\circ h\), since \(F^2=A^2=I\). Hence \(F=h^{-1}Ah\). The converse holds. An involution tangent to the identity must therefore be the identity. Since \(q\) is odd, tangent involutions are semisimple and their \(\operatorname{GL}_d(q)\)-conjugacy classes are precisely the diagonal signs \(A_r=\operatorname{diag}(-I_r,I_s)\), indexed by \(r\). This proves the claimed \(d+1\) conjugacy classes in \(G_{d,N}\).

**3. Centralizer index and exact class sizes.** Fix \(A_r\). The number of degree-\(j\) monomials with an even total exponent in the \(r\) negative coordinates is \(E_j(r,s)\), and those with an odd total exponent number \(O_j(r,s)\). A coordinate substitution commutes with \(A_r\) exactly when every negative output contains odd-parity monomials only, and every positive output contains even-parity monomials only. Thus
\[
 |C_{U_{d,N}}(A_r)|=
 q^{\sum_{j=2}^{N-1}(rO_j+sE_j)}.
\]
The \(U_{d,N}\)-conjugacy class above the specific tangent matrix \(A_r\) has index
\[
 |U_{d,N}:C_{U_{d,N}}(A_r)|=q^{e_r(d,N)}.
\]
There are \(g_d/(g_rg_s)\) tangent matrices similar to \(A_r\). These fibers are disjoint. This proves the exact class-size formula, including \(r=0\) with one identity element.

**4. Fixed-subalgebra dimension.** The fixed space of the linear diagonal substitution \(A_r\) on \(A_{d,N}\) is spanned by monomials having an even number of negative-coordinate factors. In degrees \(j=0,\ldots,N-1\), their number is \(E_j(r,s)\); their sum is \(f_r\). If \(F\) is conjugate to \(A_r\) through an algebra automorphism, its fixed algebra is isomorphic to that of \(A_r\), so its dimension is also \(f_r\). This gives \(\mathcal T_{d,N,q}(z)\), not merely the total count.

**5. Strict dominance at odd jet orders.** Put \(N=2L+1\) and compare \(r<d\) with \(r=d\). For the scalar-negative map \(-I_d\), only even total degrees contribute noncommuting nonlinear substitution coefficients, giving
\[
 e_d=d\sum_{k=1}^{L}B_d(2k).
\]
If \(1\le r<d\), choose one negative variable \(x\) and one positive variable \(y\). In each pair of degrees \((2k-1,2k)\), multiplication by \(x\) injects even-parity monomials of degree \(2k-1\) into odd-parity monomials of degree \(2k\), and injects odd-parity monomials into even-parity monomials. Consequently
\[
 E_{2k-1}+E_{2k}\le B_d(2k),\quad
 O_{2k-1}+O_{2k}\le B_d(2k).
\]
The second inequality is strict: the positive-only monomial \(y^{2k}\) is even and not divisible by \(x\), hence lies outside both sets counted on its left. After multiplying by \(r\) and \(s\), the excess of scalar-negative noncommuting coefficients is at least \(s\) per pair. Degree \(1\), which is not counted in \(e_r\), contributes \(2rs\ge0\) to the competitor's paired count, strengthening the bound. Therefore
\[
 e_d-e_r\ge sL\xrightarrow[L\to\infty]{}\infty.
\]
For \(r=0\), \(e_0=0\), whereas \(e_d\to\infty\). Since the tangent similarity-class factors do not depend on \(N\), the odd-order limiting probability follows.

**6. Strict dominance at even jet orders.** Let \(N=2L\) with \(L\ge2\), and set
\[
 C_j=[t^j](1-t)^{-s}(1+t)^{-r}=E_j-O_j,
 \quad S=\sum_{j=2}^{2L-1}C_j.
\]
The identity \(E_j+O_j=B_d(j)\) gives
\[
 e_r=\frac{D-(s-r)S}{2}.
\]
Summing the generating function through degree \(2L-1\) and subtracting its degree-zero and degree-one coefficients gives
\[
 S=H-(1+s-r),\qquad
 H=[t^{2L-1}](1-t)^{-(s+1)}(1+t)^{-r}.
\]
If \(r\le s-1\), write \(k=s+1-r\ge2\). Then
\(H=[t^{2L-1}](1-t^2)^{-r}(1-t)^{-k}>k\),
so \(S>0\) and \(s-r>0\); therefore \(e_r<D/2\). Moreover \(H\ge\binom{k+2L-2}{2L-1}\to\infty\), so the deficit grows.

If \(r=s\), the factor \(s-r\) vanishes and \(e_r=D/2\). If \(r=s+1\), then \(H=[t^{2L-1}](1-t^2)^{-(s+1)}=0\), while \(1+s-r=0\), again giving \(e_r=D/2\). Only one of these equalities can occur for fixed \(d\), namely \(r=\lceil d/2\rceil\).

If \(r\ge s+2\), write \(k=r-s-1\ge1\). Then
\[
 H=[t^{2L-1}](1-t^2)^{-(s+1)}(1+t)^{-k}.
\]
Every coefficient in this convolution at odd degree is strictly negative; in fact \(H<-k\), because the degree-zero contribution from the first factor gives a term of magnitude at least \(k\), and the degree-two term gives another strictly negative contribution. Thus \(S=H+k<0\), while \(s-r<0\), and again \(e_r<D/2\). Its deficit tends to infinity: the odd-degree convolution contains at least \(k\sum_{u=1}^{L-1}\binom{s+u}{u}\to\infty\) in absolute value. Hence the balanced-negative type uniquely maximizes \(e_r\) and all other exponent gaps diverge. Because the similarity class factors are constant as \(N\) grows, the even-order limiting probability follows.

## Verification
The included standalone \(\texttt{verify.py}\) computes truncated coordinate substitutions and composes them modulo the truncation ideal; its independent finite checks appear in \(\texttt{verify-output.txt}\). They include exhaustive \(q=3,d=2,N=3\) substitution tests as a boundary regression; independent coefficient-equation rank and centralizer comparisons for \(q=3,d=3,N=3\); direct centralizing monomial tests in five cases extending through \(d=5,N=6\); 192 independently composed nonlinear conjugates for \(q=3,d=3,N=4\); and finite parity-exponent checks for \(d=3,\ldots,7\) and \(N=4,\ldots,12\). All passed. The two boundary regressions are deliberately *not* asserted to establish the new theorem. Finite checks supplement the unrestricted proofs in Steps 1–6.

## Relationship to prior work
Brochero Martínez, *Groups of germs of analytic diffeomorphisms in (C²,0)* (first public 2002-07-31), proves in Proposition 3.1 that finite formal diffeomorphism groups over the complex numbers are linearizable. O'Farrell and Zaitsev, *Formally-Reversible Maps of C²* (first public 2011-11-29), give a related averaging linearization in Lemma 2.1, Section 2.2. The present proof credits this known general mechanism; it is **not** the novelty claim, nor do these characteristic-zero sources evaluate finite-field jet involution populations.

The published *Parity-switching involution classes in finite two-variable jet automorphism groups* gives complete class sizes and a parity switch for **two variables**, but not the higher-variable similarity strata or the balanced-negative higher-dimensional limit. Cubic truncation at \(N=3\) is excluded: its degree-three-and-higher coefficient constraints are absent and cannot imply the present higher-jet centralizer calculation. The present result changes both parameters in a controlled, intrinsically motivated way: it determines the entire fixed-subalgebra spectrum for arbitrary higher embedding dimension and proves the unique parity-sensitive dominating tangent signature. The statements in the inspected comparisons do not imply these formulas. General finite group linearization alone also does not evaluate the centralizer indices or establish the sign inequalities in Steps 5–6.

## Limitations
The result is restricted to characteristic different from two. In characteristic two, the tangent involution classification and averaging argument change. The uniform probability limits keep \(q\) and \(d\) fixed; no joint growth of field size and dimension is claimed. The formulas are exact for all stated parameters but do not classify the full invariant-subring *isomorphism types* beyond the conjugacy of the involutions. The existing literature may contain an unidentified more general finite-jet enumeration whose specialization implies the present counts; the inspected sources and searches do not resolve all historical-priority possibilities. Independent validation is not claimed.

## References
1. F. E. Brochero Martínez, *Groups of germs of analytic diffeomorphisms in (C²,0)*, first posted 2002-07-31, Proposition 3.1, https://arxiv.org/abs/math/0207297 ; searchable full text https://arxiv.org/html/math/0207297v1 .
2. A. G. O'Farrell and D. Zaitsev, *Formally-Reversible Maps of C²*, first posted 2011-11-29, Section 2.2, Lemma 2.1, https://arxiv.org/abs/1111.6984 ; open journal PDF https://journals.sns.it/index.php/annaliscienze/article/download/341/331/560 .
3. *Parity-switching involution classes in finite two-variable jet automorphism groups*, published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-switching-involution-classes-in-finite-two-variable-jet-a--391410cf76e4 .
