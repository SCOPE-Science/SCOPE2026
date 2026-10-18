# Independent mathematical audit

## correctness

PASS

Elliptic surgeries on hyperbolic g=6 knots give L-space fibered knots. Published bound r≤4g−1=23 and finite surgery denominator at most 2 reduce r>21 to r∈{43/2,22,45/2,23}; Ni–Zhang Table 4 places both half-integer values in genus-seven knot-Floer classes, so only r=22 or 23 remain. For Alexander polynomials, the L-space leading pair t^6−t^5 and alternating nonzero coefficients yield sixteen support patterns; Schmalian–Sivek Proposition 2.4 eliminates five patterns with odd offset of the initial missing term, leaving eleven. Their Corollary 3.7 requires a negative real zero <−1. I independently reimplemented all candidates in SymPy over exact rationals, formed Q=t^6Δ(t), and counted roots <−1 with exact Sturm sign variations: of eleven allowed patterns exactly the support {6,5,3,2,1} has one such root, yielding the displayed degree-12 symmetric polynomial. In addition, the source Remark 1.7 implies the SAME polynomial directly via irreducibility of the degree-ten factor, independently validating correctness (but destroying the originality claim). Source script checks finite support/Sturm only; no inference of existence or knot isotopy.

## originality

FAIL

DECISIVE COVERAGE: Schmalian–Sivek, arXiv:2609.39260v1, Remark 1.7 explicitly states any genus-six knot with a finite surgery of slope 22 or 23 has the SAME monodromy dilatation as P(−2,3,9). Example 3.8 explicitly gives Δ_P(t) and its negative real root −λ. Multiplying by t^6, the cited polynomial factors Q_P(t)=(t²−t+1) f(t), f(t)=t^10−t^8+t^5−t²+1. Exact finite-field factorization certifies f irreducible over Q: modulo 2, factor degrees 2 and 8; modulo 3, factor degrees 5 and 5, all factors square-free/irreducible, leaving no common proper possible rational factor degree. Thus f is the minimal polynomial of −λ. For ANY genus-six elliptic surgery at r>21, the already-published slope facts force r∈{22,23}; Remark 1.7 forces the identical λ, so its monic reciprocal Q_K=t^6Δ_K, of degree 12, is divisible by f. The residual factor is monic reciprocal quadratic t²+c t+1, and Δ_K(1)=1=f(1)·(2+c) forces c=−1. Therefore Q_K=(t²−t+1) f=Q_P. This is precisely the original entire Alexander-polynomial claim, as a short algebraic consequence of the PUBLISHED STRONGER SAME-DILATATION RESULT. It is not novel merely because the source did not display the genus-six coefficient equality separately. The existing finite Sturm enumeration is an alternative verification of a covered conclusion.

## value

FAIL

The genus-six polynomial classification is mathematically interesting, but as a putative new contribution it adds no unknown precise invariant or motivated remaining gap beyond the stronger published genus-six same-dilatation statement. The residual step is elementary factorization plus Δ(1)=1, or a redundant 16-case exact Sturm table. Once published implications are fully compared, neither computation nor alternate proof makes the already-covered target a substantive independently valuable result on this criterion. This does not contest mathematical correctness of the statement or its source relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
