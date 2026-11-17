# Independent mathematical audit

## correctness

PASS

Strictly increasing complete zero gaps g_j provide a unique full intermarker gap to every substring containing >=2 ones. Hence no closed factor with >=3 ones: a repeated border with >=2 ones is impossible, a border with one one also occurs at an intermediate one, and an all-zero border recurs internally in a longer gap. Unary zero factors are 0^r, r<=g_k; one-marker factors are exactly 0^a1 0^a with 0<=a<=g_{k-1}. Two-marker factors centered on g_j are closed precisely when the trailing zero context b<=g_j, with a<=g_{j-1}, and at the last pair b=0. These disjoint four classes yield g_k+2(g_{k-1}+1)+sum_{j=1}^{k-1}(g_{j-1}+1)(g_j+1), including k=1. Growth analysis gives ramp cubic k and n^(3/2), polynomial-gap exponents and positive-density geometric cases. A separate brute enumeration checked 98 strict gap vectors; universal proof is the gap-uniqueness/return classification.

## originality

PASS

Best-of-knowledge the four-class closed-factor language and multivariate count for arbitrary strictly increasing gaps are not covered by closed-rich global bounds, recurrence-based word classes or the prior two-marker special family. The known k=1 exact count is acknowledged as a boundary case, not asserted novel alone.

## value

PASS

PASS: The family has a naturally increasing sequence of intermarker distances. The complete multivariate factor-language classification exposes which returns are possible and makes precise a continuum of growth exponents and a positive quadratic-density limit, beyond general closed-rich upper bounds or finite enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
