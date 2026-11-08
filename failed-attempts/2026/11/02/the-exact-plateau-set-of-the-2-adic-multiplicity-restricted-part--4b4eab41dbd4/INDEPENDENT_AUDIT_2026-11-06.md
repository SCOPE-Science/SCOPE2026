# Independent mathematical audit

## correctness

PASS

All n>=0: 0..2 copies of each 3^j are in weight-preserving bijection with an arbitrary number r of ones by unique ternary expansion. Other part sizes remain capped. Thus P(q)=B(q)/(1-q) formally, P(0)=1, P(-1)=0 and P(n)-P(n-1)=B(n). Excluding 1 and 3 from B leaves n=1,3 empty, n=2 singleton 2, and all n>=4 supported: non-3-power n singleton; n=3^k>=9 pair (2,n-2). Independent bounded-multiplicity dynamic-programming tables through n=90 verified equality and the plateau set; finiteness is corroboration, bijection is unrestricted proof.

## originality

FAIL

Decisive prior implication: Merca (2024) Theorem 11 already identifies exactly the same unweighted capped partition count ddot p(n) with unrestricted partitions whose parts avoid N={3,8,9,15,20,21,24,27,...}, while 1 remains allowed. Removing the free part 1 yields positive first-difference coefficients for all n supported by remaining allowed parts. The support is exactly n>=2 except 3: 2,4,5 allowed and generate all integers >=4 (evens from 2; odd n>=5 from 5+2k). Therefore the complete claimed plateau classification is a direct corollary of published Theorem 11. The displayed bounded B(n) identity is an elementary alternative product factorization via classical ternary carrying, not a surviving independently original mathematical advance. The paper does not have to print the same plateau numbers for implication coverage.

## value

FAIL

The exact support/plateau index of this natural function would normally be useful, but the result is an immediate support consequence of the previously published unrestricted-part model (Merca Theorem 11), and the alternative first-difference interpretation follows by a routine base-three/Glaisher factor cancellation. This package adds no motivated structural obstacle, classification beyond that direct corollary, or independently significant new invariant; under the same value bar it is an elementary deduction of a known stronger description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
