# The exact extended Hasse polynomial at the double-conic boundary of symmetric Ciani quartics

## Finding

For every prime \(p\ge5\), put \(m=(p-1)/2\), work over \(k=\overline{\mathbb F}_p\), and consider the homogeneous quartic pencil
\[
F_a=X^4+Y^4+Z^4+a(X^2Y^2+Y^2Z^2+Z^2X^2).
\]
Define \(h_p(a)\in\mathbb F_p[a]\) to be the coefficient of \(X^{2p-2}Y^{p-1}Z^{p-1}\) in \(F_a^{p-1}\), **also at singular parameters** (where this coefficient is a polynomial extension, not a Hasse invariant of a smooth curve). Let
\[
H_m(t)=\sum_{j=0}^m\binom mj^2t^j\in\mathbb F_p[t].
\]
Then the following identity holds in \(\mathbb F_p[a]\), without removal or inversion of boundary parameters:
\[
\boxed{h_p(a)=(a-2)^mH_m(-a-1).}
\]
For \(a\notin\{2,-2,-1\}\), the smooth genus-three curve \(C_a=V(F_a)\) has Hasse–Witt matrix \(h_p(a)I_3\) in the standard canonical monomial basis. Consequently its Jacobian has either \((p\text{-rank},a\text{-number})=(3,0)\) or \((0,3)\), never intermediate values. The latter occurs precisely at the roots of \(H_m(-a-1)\) away from the excluded parameters. These are simple, lie in \(\mathbb F_{p^2}\), and number exactly \(m-\varepsilon_p\) geometrically, where \(\varepsilon_p=1\) if \(H_m(-3)=0\) and \(0\) otherwise.

At the double-conic boundary \(a=2\), the *extended scalar* polynomial has multiplicity exactly \(m+\varepsilon_p\). In contrast, the other singular parameters \(a=-2,-1\) are not zeros. The extended determinant polynomial is \(h_p(a)^3\), so its multiplicity at \(a=2\) is \(3(m+\varepsilon_p)\). For example, the scalar boundary multiplicity is \(4\) in characteristic seven, rather than the generic value \(3\). It is the actual scheme multiplicity of this specified coefficient polynomial on the affine parameter line; it is not an intrinsic Hasse invariant of the singular fiber.

## Assumptions and scope

The base characteristic is an odd prime at least five. A curve is smooth precisely for \(a\notin\{-2,-1,2\}\); its geometric genus is then three and the canonical linear system is cut out by lines. Hasse–Witt denotes the \(p\)-linear Frobenius matrix on \(H^1(C_a,\mathcal O_{C_a})\) in the conventional plane-quartic monomial basis; the Cartier dual matrix has the same rank. The polynomial coefficient is defined independently of smoothness and is used on the entire affine parameter line. All root counts refer to distinct geometric coefficient parameters, not isomorphism classes of curves. The indicator \(\varepsilon_p\) is equivalent to supersingularity of the elliptic Legendre curve with parameter \(-3\), a classical elliptic property, and no list/classification of all such primes is claimed.

## Proof

**1. Smoothness and scalar Hasse–Witt.** Differentiation gives \(\partial_XF_a=2X(2X^2+aY^2+aZ^2)\) and cyclic analogues. A singular point with exactly two nonzero coordinates requires \(a=\pm2\); a singular point with all three nonzero requires either \(a=2\) or \(a=-1\). These three parameters really are singular. Else the plane quartic is smooth of genus three. The standard plane-curve Hasse–Witt coefficient formula has diagonal entries the coefficients of \(X^{2p-2}Y^{p-1}Z^{p-1}\) and its cyclic analogues in \(F_a^{p-1}\). Since all exponents in \(F_a\) are even and \(p\) is odd, every off-diagonal target has an odd exponent and its coefficient vanishes. Coordinate permutations make the three diagonal entries equal.

**2. An exact factor from the doubled conic.** Write \(Q=X^2+Y^2+Z^2\), \(R=X^2Y^2+Y^2Z^2+Z^2X^2\). Then \(F_a=Q^2+(a-2)R\). In the expansion of \(F_a^{p-1}\), a term with fewer than \(m\) factors \(R\) contains \(Q^p\). In characteristic \(p\), \(Q^p=X^{2p}+Y^{2p}+Z^{2p}\). None of its monomials can contribute to the specified target, whose individual exponents are all smaller than \(2p\). Thus \((a-2)^m\) divides \(h_p(a)\). Moreover \(h_p\) has degree exactly \(2m\), because its top coefficient comes uniquely from \(R^{2m}\) and equals \(\binom{2m}{m}\equiv(-1)^m\pmod p\). Hence \(q_p=h_p/(a-2)^m\) is degree exactly \(m\) with leading coefficient \((-1)^m\).

**3. Elliptic quotient and its cross ratio.** The involution \(X\mapsto-X\) has genus-one quotient. Setting \(Z=1\) and \(v=X^2+\frac a2(Y^2+1)\) gives its equation
\[
v^2=\frac{a^2-4}{4}\left(Y^4+\frac{2a}{a+2}Y^2+1\right).
\]
For a smooth fiber its four branch points are \(\pm r,\pm r^{-1}\), with their usual cross ratio
\[
\lambda=\frac{(r-r^{-1})^2}{(r+r^{-1})^2}=-a-1.
\]
Thus over \(k\) it is a quadratic twist of the Legendre curve with parameter \(\lambda=-a-1\). The invariant holomorphic differential \(X\,dY/(\partial_X F_a)\) descends to \(dY/(4v)\). Therefore the scalar Hasse–Witt entry vanishes on the smooth parameter locus precisely where the quotient elliptic curve is supersingular, namely at the zeros of \(H_m(-a-1)\). (The equality of scalar coefficients with the genus-one quartic coefficient is also directly checked below.) The three symmetric quotients give a degree-eight isogeny from their product to the Jacobian. This isogeny has degree prime to \(p\), so the geometric \(p\)-divisible groups agree and the claimed \(p\)-rank and Cartier \(a\)-number alternatives follow.

**4. Endpoints and roots.** The quotient's scalar polynomial can be calculated before any parameter specialization as
\[
h_p(a)=4^{-m}(a-2)^m\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m!}{j!^2(m-2j)!}(a+2)^{2j}(2a)^{m-2j}.
\]
The coefficient identity is obtained by taking \([Y^{p-1}]\) in the \(m\)-th power of the displayed quartic; the factorial quotients are integers because they are multinomial coefficients. In particular, \(q_p(-2)=(-1)^m\ne0\). At \(a=-1\), the quartic in parentheses in Step 3 becomes \((Y^2-1)^2\), so \(h_p(-1)=(-3/4)^m\ne0\); hence \(q_p(-1)\ne0\). The classical Deuring polynomial \(H_m\) has exactly \(m\) distinct zeros, all in \(\mathbb F_{p^2}\), and neither \(0\) nor \(1\) is a zero. Therefore exactly \(m-\varepsilon_p\) of its transformed zeros lie on the smooth parameter line. Every such zero is also a zero of \(q_p\); conversely, every zero of \(q_p\) away from \(2,-2,-1\) must be a Deuring zero, by Step 3. Since \(q_p\) has degree \(m\) and neither \(-2\) nor \(-1\) is a zero, the remaining root, if \(\varepsilon_p=1\), must be \(a=2\). All the roots are therefore the \(m\) distinct roots of \(H_m(-a-1)\). Comparing their leading coefficients, both \((-1)^m\), proves the boxed *polynomial identity* including the full boundary multiplicity. This is an argument about polynomials on the parameter line, not a claim that singular curves have Hasse–Witt matrices.

## Verification

The standalone `verify_extended_hasse.py` enumerates the exact multinomial coefficient of \(F_a^{p-1}\), builds the transformed Deuring polynomial independently, and checks equality for every prime in the explicit test set \(\{5,7,11,13,17,19,23,29\}\). It also independently calculates the scalar coefficient from the elliptic quotient formula. The script is standard-library Python and prints `EXTENDED_CIANI_HASSE_OK` if all checks succeed. These finite computations test formulas and normalization; the uniform statement is proved by the divisibility, elliptic quotient, degree and root arguments, not by extrapolation.

## Relationship to prior work

Badr and Saleem (first public December 12, 2012) explicitly introduce the same one-parameter symmetric Kuribayashi quartic and analyze Weierstrass points, but not the extended Hasse polynomial. Auer and Top (2001), following classical Deuring theory, record the simple degree-\(m\) Legendre supersingular-parameter polynomial and its \(\mathbb F_{p^2}\) splitting: these elliptic facts are prior knowledge. Ohashi (2022) proves the general smooth Ciani criterion, elliptic quotient isogeny and superspeciality implications. Those smooth-fiber consequences are credited and not separately claimed as novel. A published computation of a characteristic-five Ciani coefficient-space rank census, and a characteristic-seven two-parameter Hasse divisor, are narrower or different families and do not state the all-prime *polynomial identity including the singular double-conic multiplicity*. A separate explicit stable-reduction study of this same double-conic boundary computes quadratic monodromy but not this extended Hasse polynomial. The contribution here is the uniform, integral-in-parameter factorization of the canonical Hasse coefficient and the precise collision of its roots with the double-conic boundary, rather than a newly discovered elliptic supersingular criterion.

## Limitations

There is no Hasse–Witt matrix attached to the singular fiber at \(a=2\) by the smooth-curve construction; the boundary multiplicity is defined only for the stated polynomial extension and chosen natural equation and basis. The result is for the displayed symmetric one-parameter family in prime characteristic at least five, not arbitrary Ciani quartics or arbitrary coefficient coordinate changes. The smooth superspecial criterion is already implied by general elliptic-quotient theory. No classification of prime values for which \(H_m(-3)=0\) is asserted, and historical priority of the polynomial identity still requires independent specialist review.

## References

1. E. E. Badr and M. A. Saleem, *Classification of 1-Weierstrass points on Kuribayashi quartics, I (with two parameters)*, arXiv:1212.2708v1, 2012-12-12, https://arxiv.org/abs/1212.2708.
2. R. Auer and J. Top, *Legendre elliptic curves over finite fields*, arXiv:math/0106273v1, 2001-06-22, https://arxiv.org/html/math/0106273v1, Section 3.
3. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1, 2022-01-31, https://arxiv.org/html/2201.12996v1, Sections 2–4.
4. *The octahedral hyperelliptic limit and exact quadratic monodromy at the double-conic Ciani boundary*, published finite-field geometry calculation, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-octahedral-hyperelliptic-limit-and-exact-quadratic-monodromy--272edc07ef21.
5. *Exact parity-dependent p-rank strata of characteristic-five Ciani quartics*, published coefficient-space calculation, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-parity-dependent-p-rank-strata-of-characteristic-five-cian--4f47b96584ec.
6. *Five Hasse-divisor components and seven transverse superspecial parameters for a characteristic-seven Ciani quartic family*, published coefficient-space calculation, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-five-hasse-divisor-components-and-seven-transverse-superspecial--37fdc8ec2df8.
