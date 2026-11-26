# Independent mathematical audit

## correctness

PASS

The stated initial state and companion matrix give M^7=I+2B. The parity word has least period seven, class 0 mod 7 is excluded mod 4, and the odd normalized increments in class 4 mod 7 give exactly v2(D_(7t+4))=1+v2(t) for t>0. This forces every period to contain the full dyadic factor in the exhibited matrix period, and gives one coincidence per period at k>=2 in this class. In class 5, put u=t+1 and factor the uniformly convergent binomial series as 2uH(u). The initial terms of H sum to -u; the degree-two and degree-three correction coefficients are even, and v2(j!)=j-s_2(j) proves integrality of all later polynomial coefficients. Each later product contains at least two even factors at every 2-adic integer, so both its value and derivative vanish mod 2; the polynomial secant is even for arguments congruent mod 2 by Taylor expansion, and for opposite parities because both values are even. This proves the exact isometry and supplies the unique compatible zero. The first eight terms give H(0)=32 mod 64 and the remaining terms vanish at that precision. The roots 0 and alpha are separated at valuation 5: below this valuation the two valuations agree, while on 32Z_2 exactly one is 5 and the other is at least 6. Counting the resulting residue classes, including the transition at k=12, gives the asserted sharp plateau. Bravo's nonnegative solution list and Theorem 2.3 also confirm that the only ordinary same-index equalities are at 4 and -2; the interpolation agrees with integer powers at negative integers by continuity, so the other root is not an ordinary integer. An independent bounded recurrence calculation reproduced the counts through k=16, using the given initial triples, reducing at each recurrence step modulo 2^k, and counting over 7*2^(k-1) indices. The source check.py was inspected, not executed; the all-k proof does not rely on finite sampling.

## originality

PASS

The known integer equalities and individual-sequence period/lifting results are not credited as new. The surviving contribution is the evaluated dyadic zero statistic of the fixed difference recurrence, including its two-root valuation law. No inspected earlier statement or exact table yields it; there is a specific secondary risk from the incompletely accessible 2024 paper.

## value

PASS

The sequences share a recurrence but have different natural initial conditions. The matching-index invariant separates the growth of the least period from a sharply bounded coincidence count. Identifying and separating the two nearby dyadic roots explains 64 hits in one residue branch and shows why exact integer equalities and marginal valuations miss the effect. This is a complete and reusable arithmetic description of the fixed difference, not just a numerical plateau or a general claim about unrelated sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
