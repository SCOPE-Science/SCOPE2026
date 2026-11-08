# The unique square-zero Cartier fiber in a characteristic-three cyclic quintic family

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). For every \(\lambda\in k\setminus\{0,1\}\), let \(C_\lambda\) denote the smooth projective model of
\[
y^5=x(x-1)(x-\lambda).
\]
These are genus-four curves. Let \(\mathcal C_\lambda\) be their (inverse-Frobenius-semilinear) Cartier operator on the four-dimensional space \(H^0(C_\lambda,\Omega^1)\). Then
\[
\operatorname{rank}\mathcal C_\lambda=2,\qquad \mathcal C_\lambda^3=0,
\]
and the **complete rank-squared stratification** is
\[
\operatorname{rank}\mathcal C_\lambda^2=
\begin{cases}
0,&\lambda=-1,\\
1,&\lambda\notin\{0,1,-1\}.
\end{cases}
\]
In particular, every Jacobian has \(3\)-rank zero and \(a\)-number \(2\), but the Cartier nilpotence index jumps from \(3\) on the punctured generic locus to \(2\) at the unique smooth parameter \(\lambda=-1\). The corresponding ranks of successive iterates, starting with the identity, are respectively \((4,2,1,0)\) and \((4,2,0,0)\).

## Assumptions and scope

The ground field \(k\) is **algebraically closed**, hence perfect, of characteristic exactly \(3\). The parameter ranges over every element of \(k\setminus\{0,1\}\); no finite-field or genericity restriction is imposed. For excluded parameters the affine branch polynomial has a repeated root, and the assertion about a smooth genus-four cover does not apply. The operator \(\mathcal C_\lambda\) is additive and satisfies \(\mathcal C_\lambda(c\omega)=c^{1/3}\mathcal C_\lambda(\omega)\). Its \(n\)-th iterate means functional composition, not ordinary multiplication of a coefficient matrix.

## Proof

**Genus and regular differentials.** Write \(f(x)=x(x-1)(x-\lambda)=x^3-(1+\lambda)x^2+\lambda x\), and \(u=1+\lambda\). For \(\lambda\ne0,1\), the three roots \(0,1,\lambda\) are distinct. The map \(x:C_\lambda\to\mathbb P^1\) has degree \(5\), with tame total ramification at those three points and at infinity. Riemann--Hurwitz gives
\[
2g-2=5(-2)+4(5-1)=6,
\]
so \(g=4\). At a finite branch point, \(y\) is a local parameter, so \(\operatorname{ord}(dx)=4\) and \(\operatorname{ord}(y)=1\). At the unique point above infinity, the valuations of \(x,y,dx\) are \(-5,-3,-6\). Consequently the following four regular one-forms are linearly independent and, since \(g=4\), form a basis:
\[
e_1=\frac{dx}{y^2},\quad e_2=\frac{dx}{y^3},\quad
 e_3=\frac{dx}{y^4},\quad e_4=\frac{x\,dx}{y^4}.
\]

**Cartier calculation.** In characteristic \(3\), on the rational function field \(k(x)\), the Cartier rule is
\[
\mathcal C\bigl( a(x)^3 x^{3m+2}\,dx\bigr)=a(x)x^m\,dx,
\]
while monomials with exponent not congruent to \(2\) modulo \(3\) contribute zero. For \(j\in\{2,3,4\}\), choose \(j'\in\{1,2,3,4\}\) satisfying \(3j'\equiv j\pmod5\), and set \(s=(3j'-j)/5\). Then the identity \(y^{3j'}=y^j f^s\) gives the rule
\[
\mathcal C\bigl(h(x)\,dx/y^j\bigr)=y^{-j'}\mathcal C\bigl(h(x)f(x)^s\,dx\bigr).
\]
For \(j=2,3,4\), the pairs \((j',s)\) are \((4,2),(1,0),(3,1)\). Since \([x^2]f^2=\lambda^2\), \([x^5]f^2=u\), \([x^2]f=-u\), and \([x^2](xf)=\lambda\), the operator is exactly
\[
\begin{aligned}
\mathcal C(e_1)&=\lambda^{2/3}e_3+u^{1/3}e_4,\\
\mathcal C(e_2)&=0,\\
\mathcal C(e_3)&=-u^{1/3}e_2,\\
\mathcal C(e_4)&=\lambda^{1/3}e_2.
\end{aligned}
\]
All fractional powers refer to the **unique** roots in the perfect field \(k\).

**Exact rank profiles.** Since \(\lambda\ne0\), the image of \(e_1\) is nonzero and lies in the span of \(e_3,e_4\). Also \(\mathcal C(e_4)\ne0\) lies in the independent span of \(e_2\). Therefore \(\operatorname{rank}\mathcal C=2\). Every second iterate other than that of \(e_1\) is zero. Semilinearity gives
\[
\mathcal C^2(e_1)=\Bigl[-\lambda^{2/9}u^{1/3}+u^{1/9}\lambda^{1/3}\Bigr]e_2.
\]
The ninth power of the bracket, using the characteristic-three Frobenius binomial identity, is
\[
-\lambda^2u^3+u\lambda^3
=-\lambda^2(1+\lambda)(\lambda-1)^2.
\]
Because \(\lambda\notin\{0,1\}\), this vanishes exactly when \(\lambda=-1\). Hence the second-iterate rank is \(0\) at \(-1\) and \(1\) elsewhere. The image of \(\mathcal C^2\) lies in \(k e_2\), which \(\mathcal C\) kills, proving \(\mathcal C^3=0\) for all parameters. The \(3\)-rank equals the eventual Cartier stable rank, hence is zero; the \(a\)-number is \(g-\operatorname{rank}\mathcal C=2\).

**Geometric meaning of the exceptional parameter.** At \(\lambda=-1\), \(f(x)=x^3-x\) and the covering acquires the involution \((x,y)\mapsto(-x,-y)\), permuting the branch points \(1,-1\) while fixing \(0,\infty\). The exceptional parameter is the harmonic four-point configuration, a natural symmetry point rather than an arbitrarily selected field element.

## Verification

The standalone script `verify_cartier_quintic_char3.py` contains an exact symbolic calculation over \(\mathbb F_3[\lambda]\) of the ninth-power identity, independently rebuilds the Cartier matrix from coefficients of \(f\), \(f^2\), and \(xf\), and verifies twisted semilinear composition over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It checks all smooth parameters in these fields, including the exceptional parameter; the symbolic identity, **not** finite-field sampling, proves the assertion for every algebraically closed characteristic-three field. To replay, run `python3 verify_cartier_quintic_char3.py` in a directory containing the embedded script. Its expected final marker is `CYCLIC_QUINTIC_CHAR3_CARTIER_PASS`.

## Relationship to prior work

Cavalieri and Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public August 28, 2023), Example 6.2 and Section 6.1, study the same covers and identify their special-family label \(M[11]\). Their displayed mass formula for this family is conditioned on \(p\equiv1\pmod5\), not the characteristic-three exceptional-locus calculation made here.

Li, Mantovan, Pries and Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914, Sections 6.2 and 7, give generic \(\mu\)-ordinary information for \(M[11]\) at primes congruent to \(2\) or \(3\) modulo \(5\), including the Dieudonné symbol \(N_{4,2}\), and list a supersingular basic Newton-polygon possibility. Those results do **not** identify which cross-ratios make the square of Cartier zero in characteristic \(3\). In particular, existence or permitted polygon lists do not imply the exact singleton parameter locus established here.

Lin, Mantovan and Singhal, *Abelian covers of the projective line of \(p\)-ordinary Ekedahl--Oort type*, arXiv:2303.13350, and *Non-\(\mu\)-ordinary smooth cyclic covers of the projective line*, arXiv:2406.09632, develop general stratum methods. The relevant explicit degree-five guarantee in the latter work assumes \(p>15\), so it does not determine this \(p=3\) locus. The later explicit-equations paper of Streng, arXiv:2501.14902, treats different Moonen families \(M[6],M[8],M[16]\), not the present \(M[11]\) parameter classification.

## Limitations

The result records the full sequence of Cartier iterate ranks, \(a\)-numbers, and \(3\)-ranks only for this particular cyclic quintic family in characteristic \(3\). It does not claim a complete Ekedahl--Oort classification of the associated \(3\)-torsion group scheme, nor a new classification of Newton polygons, nor a general formula in other characteristics. Historical-priority risk remains: an equivalent condition may exist in older cyclic-cover or Hasse--Witt calculations under different parameterizations, and no independent audit has been performed.

## References

1. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891, first posted August 28, 2023. https://arxiv.org/abs/2308.14891
2. W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914, first posted May 17, 2018. https://arxiv.org/abs/1805.06914
3. Y. Lin, E. Mantovan and D. Singhal, *Abelian covers of the projective line of p-ordinary Ekedahl--Oort type*, arXiv:2303.13350, first posted March 23, 2023. https://arxiv.org/abs/2303.13350
4. Y. Lin, E. Mantovan and D. Singhal, *Non-mu-ordinary smooth cyclic covers of the projective line*, arXiv:2406.09632, first posted June 13, 2024. https://arxiv.org/abs/2406.09632
5. M. Streng, *Explicit supersingular cyclic curves*, arXiv:2501.14902, first posted January 24, 2025. https://arxiv.org/abs/2501.14902
