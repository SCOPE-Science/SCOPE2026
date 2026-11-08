# Complete Cartier rank profiles for the genus-three Dickson–Chebyshev quotient

## Finding

Let \(p\) be any odd prime other than \(7\), and let \(X_p\) be the smooth projective curve over \(\overline{\mathbb F}_p\) with affine equation
\[
Y^2=(X+2)D_7(X),\qquad D_7(X)=X^7-7X^5+14X^3-7X.
\]
The curve has genus \(3\). Its Cartier operator \(\mathcal C\) on \(H^0(X_p,\Omega^1)\) has the following **complete rank sequences**, indexed by \(r=p\bmod 14\):

| \(r\) | \(\operatorname{rank}\mathcal C^0,\operatorname{rank}\mathcal C^1,\operatorname{rank}\mathcal C^2,\operatorname{rank}\mathcal C^3\) | \(a(X_p)\) | \(p\)-rank |
| --- | --- | --- | --- |
| \(1\) | \((3,3,3,3)\) | \(0\) | \(3\) |
| \(3,5\) | \((3,2,1,0)\) | \(1\) | \(0\) |
| \(9,11\) | \((3,1,0,0)\) | \(2\) | \(0\) |
| \(13\) | \((3,0,0,0)\) | \(3\) | \(0\) |

All later ranks remain equal to the fourth displayed rank. In particular, exactly the primes \(p\equiv13\pmod{14}\) give **superspecial Jacobians**. **Priority qualification:** this last zero-Cartier case already follows by combining Tafazolian–Top's maximality theorem [2] with Garcia–Tafazolian's general Cartier-vanishing theorem for curves maximal over \(\mathbb F_{p^2}\) [5]; it is included for completeness, not claimed as independently new. The new claim is the exhaustive characteristic-wise rank profile, especially the two distinct positive nilpotent ranks for nonmaximal reductions.

## Assumptions and scope

All schemes and differential spaces are considered after extending the prime field to its algebraic closure. The integer coefficients in \(D_7\) are reduced modulo \(p\). The exclusions \(p=2\) and \(p=7\) are necessary: the first is excluded by the double-cover model, while in the second the defining polynomial becomes inseparable. No assumption on a large finite extension is made. Here the \(a\)-number is \(\dim\ker\mathcal C\), and the \(p\)-rank is the stable rank of iterates of \(\mathcal C\). Superspecial means the Jacobian is geometrically isomorphic, as an unpolarized abelian variety, to a product of supersingular elliptic curves; for a Jacobian, \(a=g\) implies this property.

## Proof

**1. A tame quotient and a basis of differentials.** Consider the hyperelliptic genus-six curve
\[
T_p:\quad W^2=Z^{14}+1
\]
and the involution \(\tau(Z,W)=(Z^{-1},W/Z^7)\). It is an automorphism of order two because \(p\ne2,7\). The invariant functions
\[
X=Z+Z^{-1},\qquad Y=(Z+1)W/Z^4
\]
satisfy \(Y^2=(X+2)D_7(X)\), by the identity \(D_7(Z+Z^{-1})=Z^7+Z^{-7}\). Moreover, \(Z\) satisfies \(Z^2-XZ+1=0\) and \(W=YZ^4/(Z+1)\); hence the invariant function field is exactly \(k(X,Y)\), and \(X_p=T_p/\langle\tau\rangle\). The polynomial on the right is squarefree: the 14 roots of \(Z^{14}+1\) are simple and none is \(\pm1\), so the Dickson factor has seven simple roots, disjoint from \(X=-2\). Consequently its degree-eight hyperelliptic model is smooth of genus \(3\). The same quotient and invariant differential construction is present in Tafazolian–Top [2]; it is used here, not claimed as new.

Put \(\omega_j=Z^{j-1}dZ/W\) for \(1\le j\le6\). These form a basis of regular differentials on \(T_p\). A direct substitution gives \(\tau^*\omega_j=-\omega_{7-j}\). Since the degree-two quotient is separable and tame, pullback identifies \(H^0(X_p,\Omega^1)\) with the invariant space, whose basis is
\[
\eta_1=\omega_1-\omega_6,\quad
\eta_2=\omega_2-\omega_5,\quad
\eta_3=\omega_3-\omega_4.
\]

**2. An exact Cartier support rule.** Set \(k=(p-1)/2\). Expanding
\[
(W^2)^k=(1+Z^{14})^k=\sum_{m=0}^{k}\binom{k}{m}Z^{14m}
\]
and applying the standard hyperelliptic Cartier formula yields
\[
\mathcal C(\omega_j)=\sum_{i=1}^{6}c_{ij}^{1/p}\omega_i,\qquad
c_{ij}=\begin{cases}
\binom{k}{(pi-j)/14},& (pi-j)/14\in\{0,\ldots,k\},\\
0,&\text{otherwise.}
\end{cases}
\]
For \(1\le i,j\le6\), and \(p\ne2,7\), a nonzero coefficient occurs **if and only if** \(pi\equiv j\pmod{14}\). Indeed the congruence fixes at most one row \(i\) for each column \(j\). The range condition follows from \(p-6\le pi-j\le6p-1\le7(p-1)\) for \(p\ge11\); for \(p=3,5\) the possible congruent pairs can be checked directly and obey the range. Every relevant binomial coefficient is nonzero modulo \(p\), because \(0\le k<p\).

The Cartier operator commutes with pullback by \(\tau\), so its action restricts to the span of the \(\eta_j\). Equivalently, the equality \(\binom{k}{m}=\binom{k}{k-m}\) pairs the two columns in each \(\eta_j\) without cancellation. Consequently its nonzero arrows on the invariant basis, suppressing nonzero scalar factors, are exactly:

| \(p\bmod14\) | Action on \(\eta_1,\eta_2,\eta_3\) |
| --- | --- |
| \(1\) | all three basis directions map nontrivially to themselves |
| \(3\) | \(\eta_3\to\eta_1\to\eta_2\to0\) |
| \(5\) | \(\eta_2\to\eta_1\to\eta_3\to0\) |
| \(9\) | \(\eta_3\to\eta_2\to0\), and \(\eta_1\to0\) |
| \(11\) | \(\eta_2\to\eta_3\to0\), and \(\eta_1\to0\) |
| \(13\) | each basis direction maps to zero |

As all indicated arrows carry nonzero coefficients, these are complete Jordan-chain/rank descriptions. Coefficients lie in \(\mathbb F_p\), so Frobenius semilinearity cannot change the vanishing pattern under iteration.

**3. Invariants and contextual automorphisms.** Reading off the ranks gives the displayed rank profiles. Since \(a=3-\operatorname{rank}\mathcal C\), the \(a\)-numbers follow. The stable rank determines the \(p\)-rank. In the final row, \(\mathcal C=0\), so the Jacobian is superspecial, while in every other row \(a<3\). For the automorphism assertion, when \(p>13\) and \(p\equiv13\pmod{14}\), one has \(7\mid (p+1)/2\), and the exclusions \(13=2\cdot7-1\) and \(27=4\cdot7-1\) are not powers of \(p\). Thus the minimal-automorphism theorem of Borges–Reis [1] applies to exactly this model and gives the full geometric automorphism group \(C_2\). The exceptional prime \(13\) is not included in this automorphism claim. This infinite superspecial/minimal-automorphism family is a *corollary of the cited prior results*, and is not asserted as the new contribution here.

## Verification

The standalone script `verify_dickson7_cartier.py` requires only Python 3. It independently expands the original degree-eight polynomial \(((X+2)D_7(X))^{(p-1)/2}\) modulo each prime \(3\le p\le173\), \(p\ne7\), constructs the direct genus-three Cartier–Manin matrix, and computes the ranks of its first three powers. All 38 primes tested agree with the claimed residue-class rank profiles. It also checks the Kummer quotient polynomial identity over the integers using exact Laurent-polynomial operations. Running `python3 verify_dickson7_cartier.py` prints `CERTIFICATE_OK`. These finite checks are not a substitute for the all-prime proof above.

## Relationship to prior work

Tafazolian–Top [2], Theorem 1.4, studies **the same** \((X+2)D_d(X)\) family for odd \(d\), proves the exact maximality criterion over quadratic finite-field extensions, and gives the quotient model and invariant differential basis employed above. In particular, for \(d=7\) it already proves maximality over \(\mathbb F_{p^2}\) exactly when \(p\equiv13\pmod{14}\). These are prior results. They do not state the complete Cartier rank profile, or the finer \(a\)-number distinctions among the other four residue classes. The superspeciality for the maximal residue class is already implied by Garcia–Tafazolian [5], Theorem 3.3, because maximality over \(\mathbb F_{p^2}\) forces \(\mathcal C=0\). Therefore the maximal row and its combination with Borges–Reis [1] are **covered prior implications**; no novelty is claimed for those corollaries. For \(r=3,5\), one moreover has \(p^3\equiv-1\pmod{14}\), so maximality over \(\mathbb F_{p^6}\) and [5] already give \(\mathcal C^3=0\); what is new is the *exact* intermediate sequence \((3,2,1,0)\). For \(r=9,11\), powers of \(p\) cycle among \(1,9,11\) and never equal \(-1\pmod{14}\), so this maximality route supplies no nilpotence statement, whereas the explicit calculation gives \(\mathcal C^2=0\) and rank one. The nonmaximal classes, including the ordinary \(r=1\) case, are not completely determined by the earlier maximality theorems. Novoselov [3] computes Cartier–Manin matrices for related Dickson-quotient families, but its reported explicit cases do not state this rank profile. Kazemifard–Tafazolian–Torres [6] constructs further Chebyshev maximal covers, without giving the complete rank sequence for this model. Dias–Tafazolian–Top [4] treats nearby Chebyshev maximality questions; its available abstract does not establish the present full characteristic-wise Cartier rank classification, although the publisher PDF could not be inspected completely. The stronger general formulae remain a possible priority risk. The 2025 superspecial genus-three enumeration [7] counts a finite range of superspecial curves, and does not give the displayed nonmaximal rank-power table for this Dickson family.

## Limitations

This theorem is specific to \(d=7\). It does not determine the full Ekedahl–Oort type of the Jacobian, its endomorphism algebra or all higher-genus Dickson quotients. Superspeciality is established, but no polarization-preserving decomposition is asserted. The automorphism assertion for \(p>13\) depends on the cited 2026 theorem. Independent mathematical validation has not been performed. Historical-priority review remains qualified by inaccessible full text of [4] and possible general results on Kummer-quotient Cartier modules.

## References

[1] H. Borges and L. Reis, *Maximal Curves with Few Automorphisms*, arXiv:2610.37777v1, first public October 27, 2026. https://arxiv.org/abs/2610.37777

[2] S. Tafazolian and J. Top, *On certain maximal hyperelliptic curves related to Chebyshev polynomials*, arXiv:1902.06262v2 (2019), Theorem 1.4 and its proof. https://arxiv.org/abs/1902.06262

[3] S. A. Novoselov, *Counting points on hyperelliptic curves of type* \(y^2=x^{2g+1}+ax^{g+1}+bx\), *Finite Fields and Their Applications* 2020, DOI:10.1016/j.ffa.2020.101757; arXiv:1902.05992. https://arxiv.org/abs/1902.05992

[4] G. Dias, S. Tafazolian and J. Top, *On certain maximal curves related to Chebyshev polynomials*, *Finite Fields and Their Applications* 101 (2025), 102521. DOI:10.1016/j.ffa.2024.102521.

[5] A. Garcia and S. Tafazolian, *Certain maximal curves and Cartier operators*, *Acta Arithmetica* 135 (2008), 199–218, Theorem 3.3. https://doi.org/10.4064/aa135-3-1

[6] A. Kazemifard, S. Tafazolian and F. Torres, *On maximal curves related to Chebyshev polynomials*, *Finite Fields and Their Applications* 52 (2018), 200–213. https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2017-15.pdf

[7] R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi and K. Nuida, *Listing superspecial curves of genus three using Richelot isogeny graphs*, *Research in Number Theory* 11 (2025), article 76. https://doi.org/10.1007/s40993-025-00657-3
