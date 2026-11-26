# The exact extended Hasse polynomial at the double-conic boundary of symmetric Ciani quartics

## Finding

Let \(p\ge5\) be prime, \(m=(p-1)/2\), and \(k=\overline{\mathbb F}_p\). For the quartic pencil
\[
F_a=X^4+Y^4+Z^4+a(X^2Y^2+Y^2Z^2+Z^2X^2),
\]
define \(h_p(a)=[X^{2p-2}Y^{p-1}Z^{p-1}]F_a^{p-1}\) in \(\mathbb F_p[a]\), including at singular parameters. Write \(H_m(t)=\sum_{j=0}^m\binom mj^2t^j\). Then on the whole affine parameter line,
\[
\boxed{h_p(a)=(a-2)^mH_m(-a-1).}
\]

For \(a\notin\{2,-2,-1\}\), \(C_a=V(F_a)\) is a smooth genus-three curve, with Hasse–Witt matrix \(h_p(a)I_3\) in the monomial cohomology basis dual to the canonical monomial basis. The geometric \((p\text{-rank},a\text{-number})\) of its Jacobian is either \((3,0)\) or \((0,3)\). The latter occurs precisely at the roots of \(H_m(-a-1)\) in the smooth locus. They are simple, lie in \(\mathbb F_{p^2}\), and number \(m-\varepsilon_p\), where \(\varepsilon_p=1\) if \(H_m(-3)=0\), and \(0\) otherwise.

At the double-conic parameter \(a=2\), the multiplicity of the extended scalar coefficient is exactly \(m+\varepsilon_p\), and the multiplicity of its cube, the extended determinant, is \(3(m+\varepsilon_p)\). Neither \(a=-2\) nor \(a=-1\) is a zero. For instance the scalar multiplicity is four in characteristic seven, not three.

## Assumptions and scope

All root counts refer to distinct geometric coefficient parameters, not isomorphism classes. Hasse–Witt denotes the \(p\)-linear Frobenius on \(H^1(C_a,\mathcal O_{C_a})\), with the Cartier map dual to it. The coefficient polynomial is defined by the displayed equation independently of smoothness. Its scheme multiplicity uses this extension and is not an intrinsic Hasse invariant of a singular fiber. The indicator \(\varepsilon_p\) is the supersingularity indicator of the Legendre elliptic curve with parameter \(-3\); no classification of the primes with \(\varepsilon_p=1\) is asserted.

## Proof

**1. Smoothness and the scalar matrix.** The derivative with respect to \(X\) is \(2X(2X^2+aY^2+aZ^2)\), and cyclically. One nonzero coordinate cannot give a singular point. With exactly two nonzero coordinates the linear equations in their squares have determinant \(4-a^2\). If all three coordinates are nonzero, subtracting the derivative equations after dividing by the coordinates gives \((2-a)(X^2-Y^2)=0\) and its cyclic analogues. For \(a\ne2\) this forces equal squares and then \(a=-1\). These exceptional fibers are indeed singular: \(a=2\) gives the square of \(X^2+Y^2+Z^2\); the points \([1:1:0]\) and \([1:1:1]\) are singular at \(-2\) and \(-1\), respectively. All other fibers are smooth plane quartics and have genus three.

The plane-curve exact sequence identifies \(H^1(\mathcal O_{C_a})\) with \(H^2(\mathcal O_{\mathbb P^2}(-4))\). In the Čech basis with denominators \(X^2YZ,XY^2Z,XYZ^2\), Frobenius is computed by taking \(p\)-th powers of representatives and multiplying by \(F_a^{p-1}\). In particular the coefficient for the first diagonal entry is the displayed \(h_p\). An off-diagonal entry would require a monomial with an odd exponent, impossible because \(F_a\) has only even exponents and \(p\) is odd. Coordinate permutation makes all diagonal coefficients equal.

**2. Polynomial extraction, including at the boundary.** Put \(u=X^2,y=Y^2,z=Z^2\), so the desired coefficient is \([u^{p-1}y^mz^m](u^2+bu+c)^{p-1}\), with \(b=a(y+z)\) and \(c=y^2+z^2+ayz\). Over a field of characteristic \(p\), for formal roots \(r,s\) we have
\[
[u^{p-1}]\big((u-r)(u-s)\big)^{p-1}
 =\sum_{j=0}^{p-1}r^js^{p-1-j}=(r-s)^{p-1}.
\]
The first equality uses \(\binom{p-1}{j}(-1)^j=1\) in \(\mathbb F_p\); the second is a polynomial identity since multiplying by \(r-s\) gives \(r^p-s^p=(r-s)^p\). As \((r-s)^2=b^2-4c\), the middle coefficient is \((b^2-4c)^m\). This identity holds with polynomial coefficients, for example by proving it over the fraction field with formal \(b,c\) and then specializing. In the present case,
\[
b^2-4c=(a-2)\big((a+2)(y+z)^2-4yz\big).
\]
Thus the explicit coefficient multiplying \((a-2)^m\) is
\[
\begin{aligned}
[y^mz^m]\big((a+2)(y+z)^2-4yz\big)^m
 &=\sum_{j=0}^m\binom mj(a+2)^j(-4)^{m-j}\binom{2j}{j}\\
 &=(-4)^m H_m(a+2).
\end{aligned}
\]
The second equality follows from \(m\equiv-1/2\pmod p\), which gives \(\binom{2j}{j}=(-4)^j\binom mj\) modulo \(p\) for \(0\le j\le m\). For \(0\le k\le m\), Vandermonde's identity gives
\[
[t^k]H_m(1-t)=(-1)^k\binom mk\binom{2m-k}{m-k}=(-1)^m\binom mk^2
\quad\text{in }\mathbb F_p.
\]
Indeed \(2m-k=p-1-k\) and \(\binom{p-1-k}{m-k}\equiv(-1)^{m-k}\binom m{m-k}\). Consequently \((-4)^mH_m(a+2)=4^mH_m(-a-1)=H_m(-a-1)\), since \(4^m=2^{p-1}=1\). No factor depending on \(a\) was inverted. For comparison with the square-completed genus-one quotient, its quartic on the right of \((u+b/2)^2=(b^2-4c)/4\) has the same middle coefficient in its \(m\)-th power because \(4^{-m}=1\) in \(\mathbb F_p\).

**3. Roots, ranks and multiplicities.** The classical Deuring theorem gives \(m\) distinct roots of \(H_m\), all in \(\mathbb F_{p^2}\); these are the supersingular Legendre parameters. Also \(H_m(0)=1\) and \(H_m(1)=\binom{2m}{m}=(-1)^m\) in \(\mathbb F_p\). The excluded parameters \(-2,-1\) map to \(1,0\), respectively, and \((a-2)^m\) is nonzero there. The excluded parameter \(2\) maps to \(-3\); simplicity of the Deuring roots therefore gives exactly the stated multiplicity there and the stated number of distinct smooth zeros. Cubing triples the multiplicity. At \(p=7\), \(H_3(-3)=28=0\) in \(\mathbb F_7\).

On a smooth fiber, a nonzero scalar gives an invertible semilinear Frobenius and full stable rank three, while a zero scalar gives zero Frobenius and stable rank zero. The stable rank is the geometric \(p\)-rank; the dimension of the Cartier kernel is the \(a\)-number. In the respective cases the Cartier kernel has dimension zero or three. This proves both alternatives without making any Hasse–Witt assertion about singular fibers.

## Verification

The companion `verify_extended_hasse.py` compares the coefficient vectors from expansion of \(F_a^{p-1}\), the transformed Deuring polynomial, and the square-completed quartic for the genus-one quotient for \(p\in\{5,7,11,13,17,19,23,29\}\). It uses Python 3's standard library and is intended to print `EXTENDED_CIANI_HASSE_OK`. It tests the coefficient normalization at those primes; the general identity follows from the extraction and binomial identities above.

## Relationship to prior work and limitations

Badr and Saleem study Weierstrass points of the same symmetric Kuribayashi family [1]. Simplicity, splitting over \(\mathbb F_{p^2}\), and the elliptic supersingularity interpretation are classical Legendre facts, as recorded by Auer and Top [2]. Ohashi gives explicit Legendre models of elliptic quotients of general smooth Ciani curves and the degree-eight isogeny and smooth superspecial criterion [3]; those smooth geometric consequences are not the novelty claimed here.

Existing low-characteristic calculations recover instances of this coefficient. In characteristic five, the quotient equations in [4] on the symmetric diagonal yield \(a^4-a^3+2\). In characteristic seven, specializing the displayed Hasse–Witt entry in [5] to the symmetric line gives \(2a(a-2)^4(3a+2)\), recovering even the extended multiplicity four. The characteristic-eleven two-parameter calculation [6] likewise specializes to \(2a(a-2)^5(5a^2+4a+4)(a^2+10a+10)\). These are particular-prime overlaps, not independent evidence of the uniform identity. The double-conic boundary also appears in the stable-reduction and monodromy calculation [7], which concerns a different invariant. The result here is the uniform identity and resulting boundary multiplicity for the specified full-line coefficient. It makes no claim of priority for the individual characteristic computations, of a basis-independent invariant at the singular fiber, or of a formula for arbitrary Ciani pencils.

## References

1. E. E. Badr and M. A. Saleem, *Classification of 1-Weierstrass points on Kuribayashi quartics, I (with two parameters)*, arXiv:1212.2708v1, https://arxiv.org/abs/1212.2708.
2. R. Auer and J. Top, *Legendre elliptic curves over finite fields*, arXiv:math/0106273v1, Sections 2–3, https://arxiv.org/abs/math/0106273.
3. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1, Section 3, https://arxiv.org/abs/2201.12996.
4. *Six rational low-5-rank curves in the characteristic-five Ciani family*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-six-rational-low-5-rank-curves-in-the-characteristic-five-ciani--38e95fbca73c.
5. *Five Hasse-divisor components and seven transverse superspecial parameters for a characteristic-seven Ciani quartic family*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-five-hasse-divisor-components-and-seven-transverse-superspecial--37fdc8ec2df8.
6. *Eight Hasse components and 25 reduced superspecial parameters in characteristic eleven*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-eight-hasse-components-and-25-reduced-superspecial-parameters-in--bcd036ddc1d1.
7. *The octahedral hyperelliptic limit and exact quadratic monodromy at the double-conic Ciani boundary*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-the-octahedral-hyperelliptic-limit-and-exact-quadratic-monodromy--272edc07ef21.
