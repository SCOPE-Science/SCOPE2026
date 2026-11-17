# The reduced nonordinary divisor of bielliptic Picard curves for \(p\equiv1\pmod6\)

## Finding

Let \(p=6m+1\) be any prime (\(m\geq1\)), let \(k=\overline{\mathbb F}_p\), and let \(a\in k\) with \(a^2\ne4\). On the smooth genus-three plane quartic
\[
C_a:\quad Y^3Z=X^4+aX^2Z^2+Z^4,
\]
put
\[
B_m(a)=[T^m](T^2+aT+1)^{2m}
=\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{(2m)!}{j!\,(m-2j)!\,(m+j)!}\,a^{m-2j}\in\mathbb F_p[a].
\]
The Hasse--Witt matrix in the plane-cohomology monomial basis is diagonal:
\[
H_a=\operatorname{diag}\!\left(
\binom{4m}{2m}(a^2-4)^m,\quad
B_m(a),\quad
\frac{\binom{4m}{m}}{\binom{2m}{m}}(a^2-4)^m B_m(a)
\right).
\]
The displayed integer binomial coefficients and quotient are interpreted in \(\mathbb F_p\); all denominators are invertible. Consequently,
\[
\big(f_p(\operatorname{Jac}(C_a)),\,a(\operatorname{Jac}(C_a))\big)
=\begin{cases}(3,0)&B_m(a)\ne0,\\\n(1,2)&B_m(a)=0.\end{cases}
\]
Here \(f_p\) is the geometric \(p\)-rank and \(a\) is the Cartier \(a\)-number. The degree-\(m\) polynomial \(B_m\) has exactly \(m\) distinct roots in \(k\); all satisfy \(a^2\ne4\). Thus the marked smooth family has exactly \(m=(p-1)/6\) nonordinary coefficient parameters and no superspecial Jacobian. For its natural elliptic double-cover quotient, the associated Prym abelian surface is **superspecial precisely at those \(m\) parameters**, and ordinary elsewhere. The nonordinary determinant vanishes to exact order two at each exceptional smooth coefficient.

## Assumptions and scope

The prime ranges over **all** primes congruent to \(1\) modulo \(6\), starting with \(p=7\). The field \(k\) is algebraically closed. We count marked coefficients \(a\), not isomorphism classes: \(C_a\simeq C_{-a}\) by scaling the \(x\)-coordinate. The plane quartic is smooth exactly when \(a^2\ne4\). Indeed, the affine equation is a tame cyclic cubic cover of the line branched at four distinct roots of \(x^4+ax^2+1\), and the point at infinity \([0:1:0]\) is smooth since the \(Z\)-derivative is nonzero there.

For an abelian variety \(A/k\), write \(f_p(A)=\dim_{\mathbb F_p}A[p](k)\) and \(a(A)=\dim_k\operatorname{Hom}(\alpha_p,A[p])\). The Cartier \(a\)-number of a curve means that of its Jacobian. A dimension-two abelian variety is superspecial if its \(a\)-number is two.

## Proof

**1. Plane Frobenius coefficients.** Write \(F=Y^3Z-X^4-aX^2Z^2-Z^4\). The standard degree-four plane-curve cohomology basis is indexed by the triples \(e_1=(2,1,1)\), \(e_2=(1,2,1)\), \(e_3=(1,1,2)\). The Hasse--Witt entry from index \(i\) to index \(j\) is the coefficient of
\(X^{pe_{i,1}-e_{j,1}}Y^{pe_{i,2}-e_{j,2}}Z^{pe_{i,3}-e_{j,3}}\) in \(F^{p-1}\). Because the \(Y\)-powers in \(F\) are divisible by three and the quartic part has only even powers of \(X\), every off-diagonal coefficient is zero when \(p=6m+1\). The three diagonal coefficients reduce, without signs (using \(\binom{p-1}{r}\equiv(-1)^r\pmod p\)), to
\[
A_m=[T^{2m}](T^2+aT+1)^{4m},\quad
B_m=[T^m](T^2+aT+1)^{2m},\quad
D_m=[T^{3m}](T^2+aT+1)^{4m}.
\]
We used the reciprocity of \((T^2+aT+1)^N\), which interchanges coefficients \(T^j\) and \(T^{2N-j}\), for the first two entries.

**2. Exact coefficient factorizations.** For integers \(N\geq0\) and \(0\leq K\leq2N\), set \(Q_{N,K}=[T^K](T^2+aT+1)^N\). Directly expanding with the multinomial theorem gives
\[
Q_{N,K}(a)=\sum_{\substack{r,j\geq0\\r+2j=K}}
\frac{N!}{j!\,r!\,(N-j-r)!}\,a^r,
\]
where terms with negative factorial arguments are omitted. Its successive coefficients satisfy
\[
(r-K)(r-(2N-K))c_r=4(r+1)(r+2)c_{r+2}.
\]
Thus, as a polynomial identity with integer coefficients,
\[
(a^2-4)Q_{N,K}''+(1-2N)aQ_{N,K}'+K(2N-K)Q_{N,K}=0.\tag{1}
\]
Set \(S=a^2-4\). For \((N,K)=(4m,2m)\), the candidate \(S^m\) has differential-equation residual \(-8m(6m+1)S^{m-1}\), hence solves (1) modulo \(p=6m+1\). For \((N,K)=(4m,3m)\), using (1) for \(B_m=Q_{2m,m}\) shows that \(S^mB_m\) has residual \(-8m(6m+1)S^{m-1}B_m\), again zero modulo \(p\). Each equation has at most one polynomial solution of degree at most \(K\) for a specified leading coefficient: its coefficient recurrence descends uniquely because \(K<p\), \(2N-K<p\), and neither factor \(r-K\) nor \(r-(2N-K)\) vanishes modulo \(p\) for \(0\leq r<K\). Comparing the leading coefficients \(\binom{4m}{2m}\), \(\binom{4m}{m}\) and \(\binom{2m}{m}\) yields
\[
A_m=\binom{4m}{2m}S^m,\qquad
D_m=\frac{\binom{4m}{m}}{\binom{2m}{m}}S^mB_m
\quad\text{in }\mathbb F_p[a].\tag{2}
\]
Every factorial involved has argument strictly smaller than \(p\). This proves the displayed Hasse--Witt matrix.

**3. The reduced exceptional divisor.** The polynomial \(B_m\) has degree \(m\), with nonzero leading coefficient \(\binom{2m}{m}\). At the two excluded parameters, \(B_m(2)=\binom{4m}{m}\) and \(B_m(-2)=(-1)^m\binom{4m}{m}\), both nonzero in \(\mathbb F_p\). Equation (1) for \(B_m\) becomes
\[
S B_m''+(1-4m)aB_m'+3m^2 B_m=0.\tag{3}
\]
A multiple root \(\lambda\notin\{2,-2\}\) would satisfy \(B_m(\lambda)=B_m'(\lambda)=0\); (3) then forces \(B_m''(\lambda)=0\). Repeated differentiation forces all higher derivatives to vanish at \(\lambda\), contradicting \(\deg B_m=m<p\) and the nonzero leading coefficient. Thus all \(m\) roots are distinct and smooth. By (2) the determinant is a nonzero constant times \(S^{2m}B_m^2\); it has multiplicity exactly two along each nonordinary parameter on the smooth base.

**4. Cartier rank, stable rank and the Prym.** Since \(S\ne0\), the diagonal matrix has rank three if \(B_m\ne0\) and rank one otherwise. Each nonzero diagonal entry remains nonzero under every positive Frobenius iterate, hence the stable semilinear Frobenius rank equals the matrix rank. The two pairs \((f_p,a)\) follow. The involution \((x,y)\mapsto(-x,y)\) has genus-one quotient \(E_a\) given by \(y^3=u^2+au+1\), equivalently \(v^2=4y^3+S\). This \(j=0\) elliptic curve is ordinary for \(p\equiv1\pmod3\): its Hasse coefficient is a nonzero multiple of \(\binom{3m}{2m}S^m\). The degree-two covering yields a prime-to-\(p\) isogeny \(E_a\times P_a\to\operatorname{Jac}(C_a)\), where \(P_a\) is its two-dimensional Prym. Consequently, the Prym has \((p\text{-rank},a)=(2,0)\) outside \(B_m=0\), and \((0,2)\) on \(B_m=0\). An abelian surface of \(a\)-number two is superspecial. This completes the proof.

## Verification

A self-contained Python 3 script, `verify.py`, independently expands all three relevant coefficients and their factorized expressions modulo each of the fifteen primes \(7,13,19,31,37,43,61,67,73,79,97,103,109,127,139\). It recomputes all nine plane Hasse--Witt entries using the defining exponent formula, verifies the diagonal form, the leading coefficient, squarefreeness through Euclidean polynomial gcd, and nonvanishing at both excluded parameters. It prints `VERIFY_BIELLIPTIC_PICARD_OK 15 primes` on success. These finite tests do **not** prove the theorem for infinitely many primes; the algebraic coefficient identities, recurrence, and differential-equation argument above do.

For example, when \(p=7\) we obtain \(B_1=2a\), giving one nonordinary coefficient \(a=0\). When \(p=13\), \(B_2=6a^2+4\), giving two simple nonordinary coefficients over \(\overline{\mathbb F}_{13}\).

## Relationship to prior work

Laga and Shnidman, *The geometry and arithmetic of bielliptic Picard curves* (arXiv:2308.15297, first posted August 29, 2023), establish the natural genus-three family, the elliptic quotient and quaternionic Prym geometry; the inspected full text does not provide the above explicit characteristic-\(p\) Hasse divisor or its simple-root count. Their *Ceresa cycles of bielliptic Picard curves* (arXiv:2312.12965, first posted December 20, 2023) treats the same marked family with a different arithmetic invariant. General Picard-curve Hasse--Witt coefficient recipes, such as those cited by Nourozi and Rahmati (arXiv:2306.07823, §3), do not themselves give the factorizations (2) or the exact reduced divisor. In particular, the uniform ordinary conclusion in Theorem 3.1 of that preprint, when read with its displayed hypotheses, is incompatible with the explicit smooth nonordinary examples here; this note makes no claim about alternative unstated hypotheses or later corrections. Kazemifard and Tafazolian (2015) analyze the fixed Fermat-type curves \(y^3=x^4-1\) and \(y^3=x^4-x\), not the complete deformation divisor. Earlier work by Estrada-Sarlabous (1991) gives general ordinary/supersingular tests by Hasse--Witt matrices; the full text was not inspected, so priority of an equivalent specialization remains uncertain. Petkova and Shiga (2011) describe a complex Picard-hypergeometric realization of the discriminant-six Shimura curve; a finite-characteristic equivalent statement may exist in the wider Shimura-curve literature.

## Limitations

The theorem covers only \(p\equiv1\pmod6\), not primes \(p\equiv5\pmod6\), and the stated root count is for marked coefficients, not isomorphism classes. It does not determine Frobenius fields of definition of the roots, full zeta functions, or Newton polygons outside the ordinary/superspecial Prym dichotomy. No claim is made that all prior Shimura-curve literature has been exhaustively inspected; an older equivalent hypergeometric Hasse-invariant formula is a residual priority risk. No independent mathematical audit has been performed.

## References

1. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297, first version 2023-08-29, https://arxiv.org/abs/2308.15297.
2. J. Laga and A. Shnidman, *Ceresa cycles of bielliptic Picard curves*, arXiv:2312.12965, first version 2023-12-20, https://arxiv.org/abs/2312.12965.
3. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823, first version 2023-06-13, https://arxiv.org/abs/2306.07823.
4. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107--122, https://doi.org/10.1016/j.ffa.2014.12.002.
5. R. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic p > 0*, Mathematische Nachrichten 152 (1991), https://doi.org/10.1002/mana.19911520125.
6. M. Petkova and H. Shiga, *A new interpretation of the Shimura curve with discriminant 6 in terms of Picard modular forms*, Archiv der Mathematik 96 (2011), 335--348, https://doi.org/10.1007/s00013-011-0235-4.
