# Independent mathematical audit

## correctness

PASS

For 3|N=3n, Legendre/Kummer gives v2 binom(N,t)=s2(t)+s2(N-t)-s2(N). A binomial has valuation 0 precisely when t is a nonempty proper subset of the 1-bits of N; multiples of 3 are characterized by even-minus-odd bit-position counts modulo 3. When s2(N)>=4 an appropriate proper zero-sum bit subset exists. When weight=3 (all bits same parity), explicit t=2^i+2^(j-1) gives 1 carry. When weight=2 (one even, one odd), every admissible partition has total Hamming weight>=4, while the displayed construction reaches two carries. The n=1 empty gcd case is excluded. Independent direct integer-binomial GCD values checked for n=2..35, and independent Kummer digit-sum minima for n=2..300; inspected source verifier checks direct GCDs through n=200.

## originality

FAIL

FAIL: Fairfax-Ball 2026-09-29, arXiv:2609.37754, Restricted Binomial GCDs at Primes Congruent to -1 gives a more general exact p-adic formula for the SAME restricted Pascal-row gcd when p congruent -1 mod m. Setting m=3, p=2, N=3n yields this very s2-weight trichotomy, including 2 for two bits of opposite parity, 1 for three bits all of one parity, 0 otherwise. The audited paper cites a different Fairfax-Ball October preprint yielding only sharp universal upper bound, missing this earlier stronger formula. No new unrestricted result remains beyond direct special case.

## value

FAIL

FAIL: although a correct and neat special-case proof, this is the direct elementary specialization of an earlier exact theorem on the identical natural invariant; a standalone restatement of the already classified m3,p2 case is not substantively new or useful enough as an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
