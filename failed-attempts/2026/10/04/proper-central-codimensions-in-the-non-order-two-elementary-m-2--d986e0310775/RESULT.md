# Proper central codimensions in the non-order-two elementary \(M_2\) branch
## Finding
Let \(F\) be a field of characteristic zero, let \(G\) be a finite abelian group, and equip \(M_2(F)\) with a nontrivial elementary \(G\)-grading induced by \((g_1,g_2)\). Put \(g=g_1^{-1}g_2\) and assume \(g^2\ne1\). For either admissible graded involution \(*\in\{\gamma_2,\gamma_3\}\), the proper central multilinear codimension is
\[
c_n^{(G,*),\delta}(M_2(F))=\binom{2n}{n}-2^{n-1}
\qquad(n\ge1).
\]
The total multilinear codimension also has the closed form
\[
c_n^{(G,*)}(M_2(F))=\binom{2n+2}{n+1}-2^n.
\]
Thus, with the natural convention \(c_0^{(G,*)}=1\),
\[
c_n^{(G,*),\delta}=c_{n-1}^{(G,*)}
\qquad(n\ge1).
\]
Consequently,
\[
\frac{c_n^{(G,*),\delta}}{c_n^{(G,*)}}\longrightarrow\frac14,
\qquad
\frac{c_n^{(G,*),z}}{c_n^{(G,*)}}\longrightarrow\frac34,
\]
and the proper central exponent is \(4\).

## Assumptions and scope
The result concerns the non-order-two elementary grading branch: \(g=g_1^{-1}g_2\) satisfies \(g^2\ne1\). In this branch the recent classification allows precisely the two graded involutions \(\gamma_2\) and \(\gamma_3\). Characteristic zero is assumed so that the multilinear codimension framework and the source results apply exactly as stated.

Here \(c_n^{(G,*),\delta}\) is the dimension of multilinear central \((G,*)\)-polynomials of degree \(n\), modulo the multilinear identities, while \(c_n^{(G,*),z}\) is the complementary quotient codimension used in the cited paper, so that
\[
c_n^{(G,*)}=c_n^{(G,*),z}+c_n^{(G,*),\delta}.
\]

## Proof
It is enough to treat \(\gamma_2\), because the source gives an exact variable correspondence carrying the identities, normal forms, and central-polynomial description to \(\gamma_3\).

The source's normal-form theorem states that, modulo identities, a multihomogeneous multilinear class can involve only identity-degree variables together with variables of degrees \(g\) and \(g^{-1}\), and that the two off-degree multiplicities differ by at most one. When both off-degree multiplicities are zero, the quotient for each fixed allocation has dimension one. When both are equal to a positive integer \(\ell\), the quotient has dimension two. When they differ by one, the quotient has dimension one. The displayed normal monomials are linearly independent.

The central-polynomial theorem then selects exactly the following central classes. With no off-degree variables, the unique normal class is central exactly when the number of skew identity-degree variables is even. With \(\ell>0\) variables of each off-degree, the two normal classes have exactly one central linear combination. No class from an unbalanced off-degree allocation is central.

The no-off-degree contribution to the proper central codimension is therefore
\[
\sum_{j\text{ even}}\binom nj=2^{n-1}.
\]
For a fixed positive \(\ell\), choosing \(\ell\) variables of degree \(g\), \(\ell\) of degree \(g^{-1}\), and distributing the remaining variables among the two identity-degree symmetry types gives
\[
\frac{n!}{\ell!^2(n-2\ell)!}2^{n-2\ell}
\]
central classes. Hence the balanced positive contribution is
\[
E_n=\sum_{\ell=1}^{\lfloor n/2\rfloor}
\frac{n!}{\ell!^2(n-2\ell)!}2^{n-2\ell}.
\]
The constant-term identity
\[
[x^0](2+x+x^{-1})^n
=[x^n](1+x)^{2n}
=\binom{2n}{n}
\]
shows that the same sum including \(\ell=0\) is \(\binom{2n}{n}\). The \(\ell=0\) term is \(2^n\), so
\[
E_n=\binom{2n}{n}-2^n.
\]
Adding the even-parity no-off-degree contribution gives
\[
c_n^{(G,*),\delta}
=2^{n-1}+E_n
=\binom{2n}{n}-2^{n-1}.
\]

For completeness, the total codimension can be simplified from the same normal-form count. The no-off-degree contribution is \(2^n\); each balanced positive allocation contributes two independent classes; and the neighboring unbalanced allocations contribute one class for each orientation. Put
\[
D_n=[x^1](2+x+x^{-1})^n=\binom{2n}{n-1}.
\]
Then
\[
\begin{aligned}
c_n^{(G,*)}
&=2^n+2(E_n+D_n)\\
&=2\binom{2n}{n}+2\binom{2n}{n-1}-2^n\\
&=\binom{2n+2}{n+1}-2^n.
\end{aligned}
\]
Replacing \(n\) by \(n-1\) in the last formula immediately gives the exact shift identity
\[
c_n^{(G,*),\delta}=c_{n-1}^{(G,*)}.
\]
Finally, the standard central-binomial asymptotic \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) gives the stated limiting ratios and proper central exponent.

## Verification
The derivation uses the source's proven linearly independent normal forms and its complete central-polynomial classification; the counting steps above are exact and do not rely on finite experimentation. The accompanying checker independently evaluates the multinomial sums for \(1\le n\le40\), compares them with the closed forms, and verifies the shift identity throughout that range.

The first values are
\[
(c_n^{(G,*)})_{n\ge1}=4,16,62,236,892,3368,\ldots
\]
and
\[
(c_n^{(G,*),\delta})_{n\ge1}=1,4,16,62,236,892,\ldots,
\]
which display the shift directly.

## Relationship to prior work
Bezerra dos Santos and Reis determine the identities, normal forms, cocharacters, total codimension asymptotics, and central polynomials for this elementary branch. Their abstract and introduction explicitly single out the Klein-group grading as the case for which central and proper central codimensions are explicitly computed. In the non-order-two elementary branch, their Theorems 4.8 and 4.12 state the total asymptotic, while Remark 4.7 and Theorem 4.11 provide exactly the structural data needed for the count above.

Their companion paper on the transpose superinvolution gives an exact formula for the corresponding total codimension and a complete central-polynomial description, but does not state the proper central codimension sequence or the shift identity above. General work on proper central exponents proves existence of the relevant exponential invariant; it does not supply this rank-by-rank formula.

Targeted searches for the closed formula, the shift identity, and equivalent elementary-graded formulations did not locate an earlier statement. The closest directly related published record concerns the order-two elementary grading and square-class forms, a different branch.

## Limitations
The result is restricted to the non-order-two elementary grading branch and to characteristic zero. It does not give new formulas for the order-two elementary branch or the Klein-group grading. The literature comparison cannot exclude an older equivalent formula expressed implicitly through a different normal-form convention; in particular, earlier central-polynomial generator results may contain enough information to rederive the count without stating it.

## References
1. R. Bezerra dos Santos and L. Reis, *Polynomial identities, central polynomials and cocharacters of \(M_2(F)\) with \(G\)-graded involution*, arXiv:2609.20488v1 (2026).
2. R. Bezerra dos Santos and L. Reis, *Polynomial identities, central polynomials and cocharacters of \(M_2(F)\) with transpose superinvolution*, arXiv:2609.20458v1 (2026).
3. D. La Mattina, R. B. dos Santos and A. C. Vieira, *Proper central exponent of superalgebras with graded involution or superinvolution*, Mathematische Zeitschrift 309 (2025), article 59, DOI 10.1007/s00209-025-03689-8.
