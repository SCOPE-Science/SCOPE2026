# Independent mathematical audit

## correctness

PASS

With t=q+1, h=q−1, m=t/2 and D=d(q−1), bijectivity implies gcd(r,2h)=1 by restriction to a fiber of x↦x^D. The induced permutation on μ_m gives B^D=1, where B=a^m−(−1)^m≠0. If a=0 then B=−(−1)^m is in F_q^×. Otherwise both a^m and B lie in μ_{2h}, so Frobenius takes either to itself or its negative. The nonzero difference (−1)^m between them precludes a negative Frobenius sign on a^m, by considering both possibilities for B. On the t cosets of F_q^×, even block sizes kill the block permutation sign, and the common internal power map's signs cancel because t is even. The remaining translations have product (g^t)^{q(r−1)/2}B², since g^D traverses μ_m twice in the product of coset representatives. Its quadratic character is (−1)^((r−1)/2). The fixed zero does not change sign. Independent arithmetic and inversion counts reproduced 707 even and 544 odd permutations among 12,372 parameters; 81 of these had a=0. In the F_9 example, listing pairs (a,b) lexicographically for a+bu, the two image lists on labels 0–8 were [0,7,5,4,3,2,8,1,6] and [0,5,7,4,2,3,8,6,1], of signs +1 and −1.

## originality

FAIL

The distinct Resultary theorem 008dae091151 covers the full parity claim, including zero. Frozen record 4 covers precisely its nonzero part. Their dates do not fix priority; the exact matching scopes are demonstrable regardless of within-day order. The two F_9 examples illustrate the signs but are not a distinct general mathematical result.

## value

FAIL

The invariant is mathematically natural, but the exact all-coefficient result is already present in a distinct indexed statement. The monomial edge case adds no uncovered structure and the two checked nine-element examples are routine instances, not a separately motivated new finding. No surviving valuable narrowing is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
