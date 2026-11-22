# A squarefree quadratic root of the Dwork-quartic Hasse divisor

## Finding
For every prime \(p\ge5\), let \(k=\lfloor(p-1)/8\rfloor\) and let \(\delta\) be \(1\) if \(p\equiv5,7\pmod8\), and \(0\) otherwise. Set \(d=(p-1-4\delta)/2\). The smooth Dwork K3 quartic
\[
X_\lambda:\quad X_0^4+X_1^4+X_2^4+X_3^4-4\lambda X_0X_1X_2X_3=0
\]
has a coefficient-normalized Hasse invariant
\[
H_p(\lambda)=(\lambda^4-1)^\delta Q_p(\lambda)^2,
\qquad Q_p(\lambda)=\sum_{j=0}^{k}\frac{(a)_j(b)_j}{(j!)^2}\lambda^{d-4j},
\]
where \((a,b)=(1/8,3/8)\) if \(\delta=0\), and \((a,b)=(5/8,7/8)\) otherwise. Fractions, rising factorials, and coefficients are reduced in \(\mathbb F_p\). The monic polynomial \(Q_p\) is squarefree and has no common zero with \(\lambda^4-1\).

On the smooth parameter base \(\lambda^4\ne1\), the nonordinary divisor is therefore twice an effective *reduced* divisor consisting of exactly \(d\) geometric coefficient parameters. At these parameters the K3 fibres are supersingular, and every other smooth fibre is ordinary. The count concerns parameter values, not isomorphism classes. In characteristic \(5\), \(d=0\) and the divisor is empty.

## Assumptions and scope
The base field is \(\overline{\mathbb F}_p\), \(p\ge5\) prime; the parameter \(\lambda\) is finite and \(\lambda^4\ne1\). A fibre is smooth exactly under this last condition: simultaneous vanishing of the four partial derivatives forces all coordinates nonzero and \(\lambda^4=1\). The Hasse invariant is normalized as the coefficient of \((X_0X_1X_2X_3)^{p-1}\) in the \((p-1)\)-st power of the displayed quartic equation. This is a choice of trivialization; its vanishing divisor is intrinsic on the smooth base. It should not be confused with the reciprocal-parameter normalization of the Hasse–Dwork polynomial in the references.

## Proof
**1. Coefficient extraction.** Write \(m=\lfloor(p-1)/4\rfloor\). In the multinomial expansion, choose \(j\) copies of each fourth-power monomial and \(p-1-4j\) copies of the product monomial. Wilson's congruence and the multiplication formula for rising factorials give the exact polynomial identity over \(\mathbb F_p\)
\[
H_p(\lambda)=\sum_{j=0}^{m}\frac{(1/4)_j(1/2)_j(3/4)_j}{(j!)^3}\lambda^{p-1-4j}.
\]
Indeed, the multinomial contribution equals \((p-1)!(-4\lambda)^{p-1-4j}/((p-1-4j)!(j!)^4)\). Because \(4j\le p-1\), no denominator in the displayed coefficients vanishes modulo \(p\).

**2. Quadratic hypergeometric reduction.** Clausen's classical formal-power-series identity states
\[
{}_3F_2(1/4,1/2,3/4;1,1;z)={}_2F_1(1/8,3/8;1;z)^2.
\]
Euler's transformation gives the alternative identity
\[
{}_3F_2(1/4,1/2,3/4;1,1;z)=(1-z)\,{}_2F_1(5/8,7/8;1;z)^2.
\]
These rational identities can be reduced coefficientwise modulo \(p\) through degree \(m\), since all relevant denominator factorials have indices below \(p\). In the four residue classes \(p=8k+1,8k+3,8k+5,8k+7\), respectively, one selected upper parameter equals \(-k\) modulo \(p\): it is the first, second, first, or second of the stated pair \((a,b)\). Consequently \({}_2F_1(a,b;1;z)\) agrees modulo \(p\), through degree \(m\), with the polynomial
\[
P_p(z)=\sum_{j=0}^{k}\frac{(a)_j(b)_j}{(j!)^2}z^j.
\]
The degree of \((1-z)^\delta P_p(z)^2\) is at most \(2k+\delta=m\). Comparison of all coefficients through degree \(m\) thus proves the *polynomial* identity
\[
\sum_{j=0}^{m}\frac{(1/4)_j(1/2)_j(3/4)_j}{(j!)^3}z^j=(1-z)^\delta P_p(z)^2
\quad\text{in }\mathbb F_p[z].
\]
Substitute \(z=\lambda^{-4}\), multiply by \(\lambda^{p-1}\), and clear powers. Since \(p-1-4\delta=2d\), this gives exactly \(H_p=(\lambda^4-1)^\delta Q_p^2\); both sides are polynomials, so the identity also holds at \(\lambda=0\).

**3. Squarefreeness and boundary exclusion.** The polynomial \(P_p\) satisfies the Gauss differential equation
\[
z(1-z)P_p''+[1-(a+b+1)z]P_p'-abP_p=0.
\]
The coefficient recurrence proves it also at the top degree, because one upper parameter is \(-k\) modulo \(p\). If \(P_p\) and \(P_p'\) vanished at a point other than \(0,1\), this regular differential equation would successively force all derivatives through degree \(k\) to vanish there. As \(k<p\), the polynomial would be zero, contradicting \(P_p(0)=1\). At \(z=1\), the Chu–Vandermonde identity, with the upper parameter \(-k\), yields \(P_p(1)=(1-\beta)_k/k!\) where \(\beta\) is the other upper parameter. For the four residue classes above, the least positive representative of \(1-\beta\) is, respectively, \(3k+1,3k+2,3k+2,3k+3\), and the ensuing \(k\) factors are strictly between zero and \(p\). Thus \(P_p(1)\ne0\).

If \(\lambda\ne0\), the substitution \(z=\lambda^{-4}\) has nonzero derivative and sends any root of \(Q_p\) to a root of \(P_p\); hence all such roots are simple, and none has \(\lambda^4=1\). At \(\lambda=0\), \(Q_p\) has either a nonzero constant term (\(p\equiv1,5\pmod8\)) or precisely one factor of \(\lambda\) (\(p\equiv3,7\pmod8\)); its leading coefficient at that lower exponent is nonzero by the defining product. Therefore \(Q_p\) is squarefree, has exactly \(d\) geometric roots, and is coprime to \(\lambda^4-1\).

**4. K3 height.** Katz's coefficient criterion identifies \(H_p\ne0\) with ordinary (height-one) reduction. The Dwork quartics have geometric Picard rank at least \(19\) in characteristic zero. Every finite algebraic parameter in characteristic \(p\) with smooth fibre admits a good characteristic-zero lift; the standard specialization injection of Néron–Severi groups gives geometric Picard rank at least \(19\) for the reduction. A finite-height K3 surface of height \(h\) has geometric Picard rank at most \(22-2h\). Thus any nonordinary smooth fibre cannot have finite height \(h\ge2\) and is supersingular (infinite height). This proves the stated dichotomy.

## Verification
The accompanying `verify.py` independently implements the multinomial coefficient expansion, the proposed square factorization and exact polynomial gcd tests modulo each prime from \(5\) through \(211\). This is a finite regression check, **not** the proof for all primes; that proof is the preceding hypergeometric and differential-equation argument. Examples:
\[
Q_5=1,\quad Q_7=\lambda,\quad Q_{11}=\lambda(\lambda^4+4),\quad Q_{13}=\lambda^4+4,\quad Q_{17}=\lambda^8+12\lambda^4+15.
\]
For \(p=11\), the smooth supersingular parameters are \(\lambda=0\) and the four roots of \(\lambda^4+4\); for \(p=13\) there are four roots of \(\lambda^4+4\).

## Relationship to prior work
Grabowski's 2024 public preprint (published in 2025) makes the Hasse–Dwork coefficient polynomial and ordinarity criterion available for Dwork hypersurfaces in a reciprocal normalization, and that ingredient is **not new** here. Doran–Kelly–Salerno–Sperber–Voight–Whitcher (2020) identify the hypergeometric motive and zeta-function decomposition for the symmetric Dwork quartic pencil, likewise **not new**. The assessed addition is the **all-primes explicit square root, its proved squarefreeness and absence of boundary roots, and the precise double-versus-reduced supersingular divisor on the original marked smooth pencil**. A classical Clausen identity supplies the quadratic transformation and is credited rather than claimed.

## Limitations
No assertion is made about singular fibres, the point at parameter infinity, a fine moduli quotient, distinct geometric isomorphism classes, or complete K3 zeta functions. The proof presupposes the standard K3 Picard-rank and specialization/height results described above. Although the located primary sources do not state this full combined divisor theorem, an equivalent older unindexed Hasse/period calculation may exist. Independent external verification has not been performed.

## References
1. P. Grabowski, *Canonical liftings of Calabi–Yau hypersurfaces: Dwork hypersurfaces*, first public version 2024-01-15, arXiv:2401.07945, https://arxiv.org/abs/2401.07945; journal version *manuscripta mathematica* 176 (2025), https://doi.org/10.1007/s00229-025-01625-y.
2. C. F. Doran, T. L. Kelly, A. Salerno, S. Sperber, J. Voight, U. Whitcher, *Hypergeometric decomposition of symmetric K3 quartic pencils*, *Research in the Mathematical Sciences* 7 (2020), https://doi.org/10.1007/s40687-020-0203-3.
3. *K3 mirror symmetry, Legendre family and Deligne's conjecture for the Fermat quartic*, *Nuclear Physics B* (2020), https://doi.org/10.1016/j.nuclphysb.2020.115303 (Picard rank and mirror-family context).
4. Clausen's hypergeometric square identity; Euler's \({}_2F_1\) transformation; Chu–Vandermonde finite identity (standard classical identities).
