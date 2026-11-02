# Independent mathematical audit

## correctness

PASS

The source Catalan-gap decomposition gives T(x)=x^4 C(x)^4/(1-x C(x)^2) and coefficient binom(2n-5,n-4) for n>=4, with zero below 4 and mean n(n+1)(n-3)/(8(2n-1)(2n-3)). Independent direct enumeration of noncrossing restricted-growth words through n=9 verified the exact totals 1,5,21,84,330,1287 for n=4..9. Moreover a direct bijection independently confirms the all-n identity by reducing each marked 1122 to a marked 12 ascent via deleting one copy of each consecutive equal pair; the inverse duplicates each element of a marked adjacent ascent.

## originality

FAIL

The exact claimed total is ALREADY IMPLIED by Shattuck, Enumeration of non-crossing partitions according to subwords with repeated letters (2025), Corollary 3: for pattern 12 (the m=1 case of 1^m2), the total number of marked adjacent ascending pairs among NC_r equals binom(2r-1,r+1). There is a canonical reversible marked-occurrence bijection from 1122 in NC_n to 12 in NC_{n-2}, duplicating/deleting one adjacent copy of each of the two block labels. Taking r=n-2 gives binom(2n-5,n-1)=binom(2n-5,n-4), exactly the audited formula. Thus prior literature covers the target as an immediate corollary despite not listing the word 1122. This is decisive logical coverage, not merely a search match or shared numbers.

## value

FAIL

Although the count is correct and the statistic natural, the only asserted contribution (a first moment and mean) is obtained by a two-letter duplication bijection followed by the published adjacent-ascent count. No additional theorem, unexpected boundary, classification, or motivated new invariant beyond this immediate known special case survives. The correct but already implied binomial identity fails the required independent mathematical-value bar; neither a disclaimer nor an additional finite check makes it a new valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
