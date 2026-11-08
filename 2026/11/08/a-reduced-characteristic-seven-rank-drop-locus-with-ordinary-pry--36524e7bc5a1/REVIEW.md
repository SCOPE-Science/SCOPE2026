# Self-review

## Correctness (C): PASS

The exact objects and quantifiers are the smooth projective normalizations of \(y^3=x^5+tx^3+x\) for all \(t\in\overline{\mathbb F}_7\) with \(t^2\ne4\). A separable quintic discriminant and Kummer Riemann--Hurwitz yield genus four; an involution invariant-function calculation gives the genus-two quotient. Direct differential-basis Cartier extraction gives eigen-coefficients \(t^2+2\), \((t^2+2)(t^2+3)\), and \(4t\pm1\). The diagonalization basis is over \(\mathbb F_7\), so inverse Frobenius semilinearity does not invalidate the stable-rank count. The two anti-invariant coefficients never vanish on the smooth locus, which proves Prym ordinarity; the other two vanish together on the radical ideal \((t^2+2)\) of the rank-at-most-two determinantal scheme (the rank-at-most-three determinant ideal is its square). Distinct exceptional parameters are isomorphic by explicit scaling. Independently reconstructed genus-two Hasse coefficients and point counts check the computations. Both complete verification programs passed from the same files embedded in the package.

## Originality (O): PASS, conditional on independent historical priority review

Compared the equation, its genus-two quotient, Cartier/Hasse aliases and characteristic-seven automorphism signature against published-finding corpus, relevant published entries and principal open literature. Looijenga's 2022 trigonal-moduli result is over complex moduli; Borges--Gonçalves's Fermat-type ranks do not cover the moving trinomial; Kudo--Harashita's genus-four superspecial results do not determine this rank-two exception. The closest cyclic-cover moduli article studies p-rank-zero strata; its headline existence statement assumes primes congruent to two modulo three and its (1,3) signature discussion does not give the explicit parameter classification. No inspected statement implies the simultaneous \((4,0)\)/\((2,2)\) dichotomy, ordinary Prym, reduced rank-at-most-two determinantal locus and double Hasse vanishing. Residual risks: older unindexed equivalent normal forms or uninspected source appendices.

## Mathematical value (V): PASS

The natural involution produces a genus-two quotient and a Prym surface and supplies a geometrically motivated question: can the quotient degenerate while the Prym remains ordinary? The answer completely classifies all smooth parameters in this genus-four cyclic trigonal family, with a single exceptional geometric isomorphism class. The difference between the reduced rank-at-most-two determinantal locus and double Hasse vanishing describes actual scheme geometry, not merely an isolated point count. The statement is confined to this family and does not determine Newton polygons.

## Source and verification limits

Original literature contains general tools and examples, not an independently checked guarantee of priority. Symbolic scripts check polynomial identities in characteristic seven; the infinite-field argument additionally uses the stated geometry and semilinear proof. Independent mathematical audit and validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
