# Sharp stride-three anti-Niven progressions in twelve exponential even bases

## Finding
For base \(b\ge2\), write \(s_b(n)\) for the ordinary digit sum of a positive integer \(n\). Call \(n\) *anti-Niven in base* \(b\) when \(\gcd(n,s_b(n))=1\). Let \(M_b(3)\) be the maximum length of an arithmetic progression of positive anti-Niven integers of common difference exactly \(3\).

**Theorem.** Every even base \(b\ge6\) satisfies the uniform parity obstruction
\[
 M_b(3)\le 2\lceil b/3\rceil+1.
\]
For each of the twelve exponential bases \(b=3^k+1\), with \(2\le k\le13\), the bound is **sharp**:
\[
 \boxed{M_{3^k+1}(3)=2\cdot3^{k-1}+3.}
\]
Moreover, infinitely many distinct starting integers attain that exact maximal length for each of the twelve bases. In particular, base \(1{,}594{,}324\) has a progression of precisely \(1{,}062{,}885\) anti-Niven terms with step three, and no longer one exists.

This is a bounded finite segment of a natural exponential family. The assertion for all \(k\ge14\) is **not** proved.

## Assumptions and scope
All bases and numbers are ordinary positive integers, with no leading zeros in digit expansions. Progressions contain \(n,n+3,\ldots,n+3(L-1)\). The universal bound concerns *every* even base \(b\ge6\). The equality theorem concerns **exactly** the twelve exponents \(k=2,3,\ldots,13\), not an infinite parameter range. No primality assumption is made for the base or the starting integer. The unbounded family of starting points for each fixed listed base follows by a digit-block and modular-order extension of one certified seed.

## Proof
**1. Universal obstruction.** For an even base \(b\), whenever \(x=bq+r\) is even, its last digit \(r\) is even and hence \(s_b(x)\equiv s_b(q)\pmod 2\). Since an anti-Niven even integer must have *odd* digit sum, its quotient \(q\) must have odd digit sum. There cannot be three consecutive nonnegative integers \(q,q+1,q+2\) with all three digit sums odd: if \(s_b(q)\) and \(s_b(q+1)\) have the same parity, the carry in adding one consumes an odd, positive number of trailing \(b-1\) digits (because \(s_b(q+1)-s_b(q)=1-t(b-1)\)), so \(q+1\) ends in zero and \(s_b(q+2)=s_b(q+1)+1\) has the opposite parity. Thus all the even terms in any anti-Niven progression of difference three, which themselves form a progression of difference six, must lie in at most two adjacent base-\(b\) quotient blocks of combined length \(2b\). An interval of \(2b\) successive integers contains at most \(\lceil b/3\rceil\) terms of any arithmetic progression of difference six. A difference-three progression of length \(L\) contains at least \(\lfloor L/2\rfloor\) even terms; hence \(\lfloor L/2\rfloor\le\lceil b/3\rceil\), proving the upper bound.

**2. Seed certificate lemma.** Suppose \(b=3^k+1\), \(k\ge2\), and an integer \(H=b+h\) with \(1\le h\le b-2\) is chosen. Put \(K=h+1=s_b(H)\), assume \(K\not\equiv0\pmod3\), and define
\[
 U=b^2+(h+2)b+h,\quad n=Hb^2+(b-2)b+(b-3),\quad L=2\cdot3^{k-1}+3.
\]
Assume the following **finite exact divisibility tests** hold:
(i) \(\gcd(n,K+2b-5)=1\);
(ii) neither \(U\) nor \(U+2\) is divisible by any prime \(p\ne3\) satisfying \(p\le K+2b\);
(iii) \(\gcd(U+3,K+3)=1\).
Then the \(L\) integers \(n+3j\), for \(0\le j<L\), are all anti-Niven.

Indeed at \(j=0\) the three visible digit blocks yield \(s_b(n)=K+2b-5\), establishing this case by (i). For \(1\le j<L\) write \(b-3+3j=tb+r\), \(0\le r<b\). Then \(t\in\{1,2,3\}\), with \(t=3\) occurring only at \(j=L-1\). For \(t=1\), the digit sum is \(K+b-1+r\) and
\[
 (n+3j)-s_b(n+3j)=(b-1)U.
\]
For \(t=2\), the digit sum is \(K+1+r\) and the difference is \((b-1)(U+2)\). These digit identities use \(s_b(H+1)=K+1\), valid because \(h\le b-2\). All digit sums are at most \(K+2b\). As \(b-1=3^k\), the congruence \(s_b(v)\equiv v\pmod 3\) and \(n+3j\equiv K\pmod3\) imply every such digit sum is coprime to \(3\). Any common prime factor in either case would therefore be a prime at most \(K+2b\), distinct from \(3\), dividing \(U\) or \(U+2\), contradicting (ii). At the last term, \(r=1\), the digit sum is \(K+3\) and the difference is \((b-1)(U+3)\). Conditions \(3\nmid K\) and (iii) exclude all common prime factors. This proves the seed lemma.

**3. Twelve exact certificates.** The following table lists an independently checkable tuple for every exponent in the theorem. In every row \(U+2\) is the next even translate of the listed \(U\); the short Python checker verifies the exact primality-obstruction test (ii) with an Eratosthenes sieve, the two endpoint gcd tests, all identities, and also **every term** of every witness progression using independent digit-sum and Euclidean computations. The total of the twelve progression lengths is \(1{,}594{,}356\). This finite certificate establishes each stated equality, not the unlisted exponents.

| \(k\) | \(b\) | \(H\) | \(K\) | \(U\) | \(n\) | \(L\) |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 10 | 17 | 8 | 197 | 1787 | 9 |
| 3 | 28 | 37 | 10 | 1101 | 29761 | 21 |
| 4 | 82 | 115 | 34 | 9627 | 779899 | 57 |
| 5 | 244 | 365 | 122 | 89669 | 21789929 | 165 |
| 6 | 730 | 797 | 68 | 583337 | 425253467 | 489 |
| 7 | 2188 | 2381 | 194 | 5214197 | 11403451217 | 1461 |
| 8 | 6562 | 6589 | 28 | 43250169 | 283764365395 | 4377 |
| 9 | 19684 | 19699 | 16 | 387794499 | 7632959143513 | 13125 |
| 10 | 59050 | 59429 | 380 | 3509400929 | 207226615515947 | 39369 |
| 11 | 177148 | 177437 | 290 | 31432964261 | 5568255320120801 | 118101 |
| 12 | 531442 | 531713 | 272 | 282575683301 | 150172303709698451 | 354297 |
| 13 | 1594324 | 1594429 | 106 | 2542039609749 | 4052832216735449353 | 1062885 |


**4. Infinitely many maximizing starts.** In each certified row write \(H=b+h\). The lower part \(t=hb^2+(b-2)b+(b-3)\) satisfies \(0<t+3(L-1)<b^3\), and the original seed is \(n=b^3+t\). Put \(S_j=s_b(n+3j)\). For the finite set of primes \(p\) dividing at least one of the \(S_j\), choose any positive common multiple \(T\) of the multiplicative orders of \(b\pmod p\) for those primes \(p\nmid b\) (taking \(T=1\) if none exist). For all integers \(m\ge3\) with \(m\equiv3\pmod T\), set \(n_m=b^m+t\). No carries occur into the leading digit, so \(s_b(n_m+3j)=S_j\). For primes \(p\nmid b\), \(b^m\equiv b^3\pmod p\); for primes dividing \(b\), both powers vanish modulo \(p\). Thus \(n_m+3j\equiv n+3j\pmod p\) for every prime \(p\mid S_j\). Coprimality of the seed transfers to every \(n_m+3j\). Since \(m\) may grow arbitrarily, these are infinitely many distinct maximizing progressions.

Combining the universal upper bound, the twelve certificates, and the lifting argument proves the theorem. \(\square\)

## Verification
The standalone standard-library program `verification/check.py` reconstructs each row from its parameters, performs a full sieve-based roughness certificate, verifies the endpoint tests, and independently checks all \(1{,}594{,}356\) progression integers with exact digit-sum and gcd arithmetic. Its expected terminal line is `VERIFY_OK bases=12 terms=1594356`. The finite computation proves only the twelve certificate assertions, not the universal obstruction or infinitude; those are proved symbolically above.

## Relationship to prior work
Blau, Harrington, Lohrey, Sosis, and Wong (2023, arXiv:2308.05228v1) introduce anti-Niven arithmetic progressions, prove general upper bounds, and in their Theorem 3.4 address odd strides in even bases; their exact discussion and open sharpness questions motivate the present stride-three case. Our universal parity argument gives the simple bound \(2\lceil b/3\rceil+1\), while the explicit twelve-base certificates prove its attainment in a natural growing family. That paper does not contain these twelve equality claims or the compact rough-twin certificate method. The related indexed results for odd bases with even strides, odd bases with step \(b-1\), and ternary base with step two do not imply the present even-base stride-three equalities. The universal obstruction alone is an elementary strengthening in some congruence classes and is **not** advanced as a separate research contribution; its significance here is the matching certified extremal family.

## Limitations
Sharpness beyond \(k=13\) is not proved. The twelve examples do not establish an infinite collection of bases, nor do they classify all maximizing starts for any base. The source-date and priority assessment rests on available publications and indexed records; an unindexed equivalent result is possible. The review is not an independent mathematical audit. The finite certificates are reproducible with basic integer arithmetic, but no general bound on the least maximizing starting point for other bases follows.

## References
1. Ryan Blau, Joshua Harrington, Sarah Lohrey, Eliel Sosis, and Tony W. H. Wong, *Arithmetic Progressions of Integers that Are Relatively Prime to Their Digital Sums*, arXiv:2308.05228v1, first posted 9 August 2023. https://arxiv.org/abs/2308.05228 . Especially the even-base odd-stride bounds and the subsequent sharpness questions.
2. *Sharp anti-Niven progressions for short even strides in odd bases*, public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-anti-niven-progressions-for-short-even-strides-in-odd-base--f890edbf6d9b . This is the parity-disjoint odd-base/even-stride case.
3. *Sharp length 38 for difference-two ternary anti-Niven progressions*, public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-length-38-for-difference-two-ternary-anti-niven-progressio--0d529a702409 . This treats base three and difference two.
4. *Long fixed-step anti-Niven progressions in every odd base*, public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-long-fixed-step-anti-niven-progressions-in-every-odd-base--1e0d4a4b2e61 . This treats odd bases and difference \(b-1\).
