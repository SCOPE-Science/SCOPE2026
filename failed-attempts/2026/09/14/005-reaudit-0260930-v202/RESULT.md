# Empty reducible q-locus for symmetric half-exponent Heun at t=2 (Kovacic Case 1)

## Context and motivation

Consider

H(2,q): y'' + (1/2)(1/z + 1/(z-1) + 1/(z-2)) y'
       + (z/16 - q)/(z(z-1)(z-2)) y = 0,

with gamma=delta=epsilon=1/2, alpha=beta=1/4, t=2 and q in C. This is a symmetric half-exponent Lamé/Heun slice. Reducibility of the Lamé family is part of established differential-Galois theory; the purpose here is to specialize the Kovacic Case-1 criterion to this entire accessory line and give a short explicit certificate.

## Definitions

A Kovacic Case-1 solution is a hyperexponential solution whose logarithmic derivative is rational. Equivalently, the associated Riccati equation has a solution in C(z), or the rank-two differential module is reducible over C(z).

Write p(z) for the coefficient of y' and r(z) for the coefficient of y. Passing to normal form gives

Y'' = sY,  s=p'/2+p^2/4-r.

## Result

For every q in C, H(2,q) has no Kovacic Case-1 solution. Equivalently, the complete reducible/Borel Case-1 q-locus on this t=2 symmetric half-exponent line is empty.

This is an explicit specialization and certificate inside the known Lamé-family differential-Galois framework; it is not a claim that reducibility of the Lamé family was previously unstudied.

## Proof and evidence

Exact rational arithmetic gives

s = N(q,z) / [16 z^2 (z-1)^2 (z-2)^2],

where

N(q,z) = -4z^4+15z^3-26z^2+24z-12
         + q(16z^3-48z^2+32z).

The q-dependent part is 16q z(z-1)(z-2), so it vanishes at every finite singular point. Therefore

N(q,0)=-12,  N(q,1)=-3,  N(q,2)=-12,

and the double-pole coefficients are

b_0=b_1=b_2=-3/16.

The leading z^4 coefficient is -4 for every q, so the pole at infinity also has order two, with

b_infinity=-1/4.

Kovacic Case 1 therefore gives the finite-point alpha set {1/4,3/4} and the singleton alpha_infinity={1/2}. Every candidate degree has the form

1/2 - alpha_0 - alpha_1 - alpha_2,

so the only possible values are

-1/4, -3/4, -5/4, -7/4.

None is a nonnegative integer. Hence Case 1 has no candidate for any q, proving that the reducible/Borel q-locus is empty.

The same conclusion can be read directly from rational logarithmic derivatives. A Case-1 solution would have logarithmic derivative whose local residues correspond to the two finite exponents, plus P'/P for a polynomial P. The degree balance at infinity forces the same four negative fractional degrees, which is impossible.

## Limitations

Only Kovacic Case 1 is classified. The result does not exclude special q values in Kovacic Cases 2 or 3, does not treat t other than 2, and does not classify non-symmetric exponents. The result is a concrete specialization of established Lamé-family reducibility theory rather than a new family-level classification.

## Reproducibility

Run `python3 artifacts/kovacic_case1_normalform.py` with SymPy. It prints the exact normal-form numerator and denominator, verifies the q-independent double-pole data, and enumerates all eight Case-1 candidate degrees, ending with `CERTIFICATE OK`.

## References

- F. Loray, M. van der Put, and F. Ulmer, *The Lamé family of connections on the projective line*, Ann. Fac. Sci. Toulouse 17 (2008), 371-409, doi:10.5802/afst.1187.
- J. J. Kovacic, *An algorithm for solving second order linear homogeneous differential equations*, J. Symbolic Comput. 2 (1986), 3-43, doi:10.1016/S0747-7171(86)80010-4.
- DLMF Chapter 31, especially §§31.2 and 31.8.
- Hounkonnou-Ronveaux, *Generalized Heun and Lamé equations: factorization*, arXiv:0902.2991.
