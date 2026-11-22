# Five Weil spectra and a doubled Hasse divisor in a characteristic-eleven dihedral genus-four pencil

## Finding
Let \(C_a\) be the smooth projective curve over \(\mathbb F_{11}\) with affine equation
\[
C_a:\quad y^2=x^{10}+a x^5+1,\qquad a\in\mathbb F_{11},\quad a^2\ne4.
\]
There are nine smooth coefficient-marked members. Their Jacobian Weil numerators are exactly \(L(C_a,T)=Q_a(T)^2\), where the following table gives the five distinct \(Q_a\), with \(a\) considered up to sign:

| \(a\) | \(Q_a(T)\) | Number of marked members | \(\#C_a(\mathbb F_{11})\) | \(\#C_a(\mathbb F_{121})\) |
| --- | --- | ---: | ---: | ---: |
| \(0\) | \(1-4T+6T^2-44T^3+121T^4\) | 1 | 4 | 114 |
| \(\pm1\) | \(1+6T+26T^2+66T^3+121T^4\) | 2 | 24 | 154 |
| \(\pm3\) | \(1+T+21T^2+11T^3+121T^4\) | 2 | 14 | 204 |
| \(\pm4\) | \(1+T+11T^2+11T^3+121T^4\) | 2 | 14 | 164 |
| \(\pm5\) | \((1-2T+11T^2)^2\) | 2 | 4 | 194 |

Consequently, these marked curves realize five distinct \(\mathbb F_{11}\)-isogeny classes of Jacobians. The sole class with the fourth power of an elliptic Weil polynomial is \(a=\pm5\), whose Jacobian is \(\mathbb F_{11}\)-isogenous to \(E^4\), for \(E:y^2=u^3+u+10\). Taking both quadratic twists of these five spectral types produces ten distinct Weil numerators.

Over \(k=\overline{\mathbb F}_{11}\), every smooth fiber of the same pencil has an ordinary Jacobian except at the six distinct roots of
\[
(5-a^2)(5a^4-3a^2-1)=0.
\]
All six exceptional fibers have Jacobian \(11\)-rank two and Cartier \(a\)-number two. The six parameters comprise two rational points \(a=\pm4\) and one degree-four Frobenius orbit. The Hasse determinant is the square of the displayed degree-six equation, so it vanishes to multiplicity two at each exceptional geometric parameter. None of the smooth fibers has Jacobian \(11\)-rank zero.

## Assumptions and scope
The finite Weil-spectrum assertion is about the nine monic coefficient-marked equations over \(\mathbb F_{11}\), not a census of all genus-four curves, geometric isomorphism classes, or all possible scalar twists. The geometric Hasse statement concerns every \(a\in k\) with \(a^2\ne4\). The curve denotes the smooth projective completion of the displayed affine equation. All isogenies and Weil polynomials are over the stated base field. The elliptic curve \(E\) is over \(\mathbb F_{11}\).

## Proof
**Smoothness and genus.** Set \(f_a(x)=x^{10}+ax^5+1\). In characteristic eleven its derivative is \(5x^4(2x^5+a)\); a repeated root exists precisely when \(a^2=4\). Otherwise \(f_a\) is squarefree of degree ten. The smooth completion has genus four and two rational points above infinity, since the leading coefficient is one.

**The genus-two quotient and squared numerator.** The involution \(\tau:(x,y)\mapsto(x^{-1},y/x^5)\) commutes with the hyperelliptic involution and, together with \(\sigma:(x,y)\mapsto(\zeta_5x,y)\), gives a tame dihedral action defined over \(\mathbb F_{11}\), since \(\mu_5\subset\mathbb F_{11}\). Put \(t=x+x^{-1}\). Because \(x^5+x^{-5}=t^5-5t^3+5t\), the quotient by \(\tau\) has the genus-two model
\[
D_a:\qquad v^2=(t+2)(t^5-5t^3+5t+a).
\]
For example, the function \(v=y(t+2)(t^2-t-1)/(x^5+1)\) is invariant under \(\tau\) and obeys this equation: \(t^5-5t^3+5t+2=(t+2)(t^2-t-1)^2\). The six branch points (counted over an algebraic closure) are simple when \(a^2\ne4\), as also follows from the quotient's genus by Riemann–Hurwitz.

For any auxiliary prime \(\ell\ne2,5,11\), the \(\sigma\)-invariant part of \(H^1(C_a,\mathbb Q_\ell)\) vanishes because \(C_a/\langle\sigma\rangle\) has genus zero. The four nontrivial characters of \(\langle\sigma\rangle\) occur in inverse-character pairs, interchanged by \(\tau\). The \(\tau\)-invariants are precisely \(H^1(D_a,\mathbb Q_\ell)\). Frobenius commutes with both group elements; on every inverse-character pair it has two conjugate, hence equal, characteristic polynomials. Therefore \(L(C_a,T)=L(D_a,T)^2\). Tate's isogeny theorem gives \(\operatorname{Jac}(C_a)\sim\operatorname{Jac}(D_a)^2\) over \(\mathbb F_{11}\). The equality of zeta numerators is also verified by direct counts in degrees one and two, independently of this representation argument.

**Exact arithmetic census.** For each of the nine values \(a\), enumerate \(\mathbb F_{11}\) and \(\mathbb F_{121}\), computing \(\#D_a(\mathbb F_q)=q+2+\sum_{t\in\mathbb F_q}\chi_q((t+2)(t^5-5t^3+5t+a))\), where \(\chi_q(0)=0\). For a genus-two curve with \(N_1,N_2\) points, put \(s_1=12-N_1\) and \(s_2=122-N_2\). Then
\[
Q_a(T)=1-s_1T+\frac{s_1^2-s_2}{2}T^2-11s_1T^3+121T^4.
\]
The exhaustive values are exactly the table above. The substitution \(x\mapsto2x\) sends \(a\) to \(-a\), because \(2^5=-1\) and \(2^{10}=1\) in \(\mathbb F_{11}\). The five listed polynomials are pairwise distinct. The elliptic curve \(E:y^2=u^3+u+10\) has ten rational points, hence numerator \(1-2T+11T^2\); \(Q_{\pm5}\) is its square, whereas none of the other four values equals the square of any integral elliptic Weil polynomial. Quadratic twisting replaces \(T\) by \(-T\); the ten resulting polynomials are pairwise distinct.

**Cartier and geometric parameters.** With differential basis \(dx/y,x\,dx/y,x^2\,dx/y,x^3\,dx/y\), the Cartier–Manin matrix has entry the coefficient of \(x^{11i-j}\) in \(f_a(x)^5\). Every nonzero exponent in \(f_a^5\) is divisible by five. As \(1\le i,j\le4\), the matrix is diagonal. Exact multinomial expansion gives
\[
H_a=\operatorname{diag}(h_1,h_2,h_2,h_1),\quad h_1=5-a^2,\quad h_2=5a^4-3a^2-1.
\]
The polynomial \(h_2/5=a^4-5a^2+2\) is irreducible over \(\mathbb F_{11}\): it has no root and none of the 121 monic quadratic polynomials divides it; these tests are reproduced in the attached exact verifier. Its four distinct roots are not roots of \(h_1\) and do not lie at \(a=\pm2\). The two roots of \(h_1\) are \(a=\pm4\) in \(\mathbb F_{11}\), and are not roots of \(h_2\). Over an algebraically closed field, the semilinear Cartier operator is thus diagonal with either four nonzero entries or exactly two; its iterates have the same stable rank. Hence the stable Cartier ranks (equivalently Jacobian \(11\)-ranks) are four or two, and the Cartier \(a\)-numbers are zero or two. Finally \(\det H_a=(h_1h_2)^2\), giving the asserted multiplicities.

## Verification
Run `python3 verification/check_dihedral11.py` with Python 3 standard library. It checks the Cartier coefficients directly by multinomial expansion; tests irreducibility of the quartic; counts points on both the genus-two quotient and genus-four curve over \(\mathbb F_{11}\) and over two independently represented copies of \(\mathbb F_{121}\); verifies the five complete genus-two Weil polynomials, the elliptic trace and the ten twist spectra. It exits successfully with `DIHEDRAL11_WEIL_AND_CARTIER_VERIFIED`. These finite computations verify the bounded census and polynomial identities; the geometric rank classification and full Weil-factor relation follow from the proofs above, not from sampling.

## Relationship to prior work
Ohashi–Kudo describe genus-four hyperelliptic families with large automorphism groups, including this dihedral normal form, and study superspecial members; the normal form and automorphism structure are not claimed here as new. Bruin–Kulkarni investigate Jacobians isogenous to squares of genus-two Jacobians; the square-decomposition mechanism is likewise background, not the claimed arithmetic novelty. The separate literature on genus-four order-six hyperelliptic curves studies another family. The contribution assessed here is the joint complete \(\mathbb F_{11}\) Weil-isogeny spectrum, its unique elliptic fourth-power type, and the explicitly factored characteristic-eleven Hasse divisor and Frobenius splitting. Related results for this dihedral pencil in characteristics three, seven and forty-one, and for distinct genus-four dihedral pencils in characteristic eleven, do not determine this characteristic-eleven census.

## Limitations
This is a marked finite-field classification, not a classification of all genus-four curves or their full automorphism groups. Equality of Weil numerators means isogeny of Jacobians over the base field, not isomorphism of curves or polarized Jacobians. Historical priority cannot be exhaustively established: an unindexed equivalent field-specific calculation could exist. The self-review has not been independently audited. No assertion is made about all quadratic or higher twists beyond the two stated quadratic twist types.

## References
- R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858, first public 2023-12-28, https://arxiv.org/abs/2312.16858.
- N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959, first public 2023-09-05, https://arxiv.org/abs/2309.01959.
- M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing \(C_6\)*, arXiv:2210.14822, first public 2022-10-26, https://arxiv.org/abs/2210.14822.
