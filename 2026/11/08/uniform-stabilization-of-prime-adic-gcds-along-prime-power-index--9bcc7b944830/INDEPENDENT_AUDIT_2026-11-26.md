# Independent mathematical audit

## correctness

PASS

Legendre digit sums allow removal of the common p^t from upper, lower and complementary arguments. Write k=p^(a−v)j with p∤j, so its valuation is that of the coefficient C(up^v,uj). The exact minimization at level a is over the disjoint primitive-index levels 1≤v≤a. The first v positions in uj+u(p^v−j)=up^v each carry: the first digit is nonzero in each summand and sums to zero modulo p, and at each subsequent position an incoming carry cannot yield zero without another carry. Equivalently, C(up^v,uj)=(up^v/(uj))C(up^v−1,uj−1) gives valuation at least v. The level-one candidate j=1 has valuation c≥1, so levels v≥c cannot improve that minimum, yielding cutoff R=max(1,c−1), not a claim of least cutoff. Lower exponent gcd valuations can also be recovered from the upper row at exponent R by using only lower indices with k divisible by p^(R−a). Only level 1 can give valuation 1, and Legendre there gives the stated expression. For p=2 it is the digit sum of odd u, equal to 1 exactly when u=1; for p>u, (p−1)u=(u−1)p+(p−u) has digit sum p−1. A separate manual check gives D_1(11,2)=3 and D_2(11,2)=2, the latter using the valuation-2 coefficient C(44,11) and both level lower bounds. The supplied checks were inspected but not run; finite recorded output is corroboration only.

## originality

PASS

Wu's primary text treats the identical restricted gcd and covers the prime-power multiplier special case; the evaluated contribution is the arbitrary-m cutoff and valuation-one characterization, not that special case or the digit-sum/carry formulas. The strongest verified same-object theorems do not cover arbitrary multipliers in the p-power index tower.

## value

PASS

For a fixed multiplier the proof removes dependence on a potentially arbitrarily large prime-power exponent in a natural restricted gcd problem. The primitive-level decomposition explains actual strict valuation drops and makes a nontrivial finite cutoff and complete valuation-one test possible. This is not a fresh calculation of the classical full-row gcd.

The dated certificate retains the supplied scientific assessment, sources and limitations.
