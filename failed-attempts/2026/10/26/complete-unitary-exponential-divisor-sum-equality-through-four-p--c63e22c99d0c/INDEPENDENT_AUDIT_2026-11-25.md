# Independent mathematical audit

## correctness

PASS

Multiplicativity forces a mix of singleton and repeated primes, leaving precisely p^2q, p^3q, pqr^2. For the first two, q(p−1)=p^a+1 implies p−1 divides 2 and gives exactly 20 and 45, with sums 30 and 60. For pqr^2, order the singleton primes p<q. The ratio forces r<p<q, so p,q are odd and p+1<q. Reduction modulo q forces q | r²+1; pq>r²+1 rules out p | r²+1, so p | q+1. With t=(r²+1)/q and k=(q+1)/p≥2, cancellation gives t(k+1)=r−1. Hence t | gcd(r−1,2); r=2 is impossible, while odd r forces t=2. Then k=(r−3)/2≥2 and r−3 divides 12; the only prime r≥7 is 7, giving q=25. This is unbounded, includes all exponent shapes, and allows n=1 only by the stated convention. The frozen VERIFICATION.md and verify.py were inspected, not executed; the finite sieve and congruence scan are corroboration only.

## originality

FAIL

A distinct indexed record (439fe6387317) proves the identical theorem, including the structural obstruction, with n=1 also allowed. Both records carry the same UTC date; the evidence does not establish within-day priority, but equivalent coverage is decisive for distinctness. The proof variants use the same factorization and the same terminal restriction that the repeated prime minus 3 divides 12; a distinct substantive remainder is not established.

## value

PASS

As mathematics, the cutoff is motivated by the infinitude problem and is the first one to require a three-distinct-prime obstruction. The structural proof is more informative than a census. This intrinsic value does not make a second statement of the covered classification a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
