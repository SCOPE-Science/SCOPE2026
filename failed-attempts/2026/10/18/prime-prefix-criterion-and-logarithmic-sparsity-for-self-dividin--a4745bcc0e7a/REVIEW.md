# Independent mathematical audit

## correctness

PASS

R(n) is coprime to 10; the least prime p dividing a qualifying n>1 must be 3, since otherwise the nontrivial order of 10 modulo p divides both n and p-1. For each p_i>3 all prime factors of its order are smaller than p_i, giving the required prefix including exponents. Conversely, the tests imply ord_{p_i}(10)|n and it is prime to p_i. Odd-prime LTE supplies v_{p_i}(R(n))>=e_i+1 and v_3(R(n))=v_3(n); n=1 is separate. The exact two-prime condition follows. The primitive orders can also be checked without exceptions from Bang–Zsigmondy: for b=10^{3^{a-1}}, b^2+b+1 has 3-adic valuation one and gcd with b-1 equal to 3, hence has a prime q>3 with order 3^a for 10. Odd orders force all prime divisors into the stated quadratic splitting set, including 3. Squaring the containing set's Euler product gives zeta(s)L(s,chi)(1-2^{-s})(1-5^{-s}) times the product over chi(p)=-1; the regular factor at s=1 is positive and gives C_40 after taking its square root and dividing by Gamma(1/2). Multiplication by 3 bijects this semigroup with its multiples of 3, giving the factor 1/3. A separate bounded replay factored n and compared the prefix tests with pow(10,n,9*n)==1 over 1..120000: 27 agreements on hits and no mismatches; four seed primes with three exponents each were also checked. This is finite corroboration, not the proof. No asymptotic equality for A(X) is asserted.

## originality

FAIL

Established prior coverage, not an access issue. Smyth's general Lucas-index classification specializes mechanically to the prime-prefix and two-support descriptions. The same count A(X) is a direct case of Alba González–Luca–Pomerance–Shparlinski, whose Theorem 1.1 gives O(X/log X), already o(X/sqrt(log X)); their Lucas-specific Theorem 1.2 is stronger still. The exact constant of the larger containing set does not recover an original bound on A(X).

## value

FAIL

The subject is natural, but the exact arithmetic classification is a mechanical Lucas specialization, and the claimed logarithmic upper bound is substantially weaker than the existing estimate for the same A(X). The exact coefficient measures only an elementary containing semigroup, not the sought lengths or a sharp obstruction for them. The two-prime family is a useful illustration of the rule but follows immediately from classical primitive divisors and does not leave an independently valuable new claim to repair here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
