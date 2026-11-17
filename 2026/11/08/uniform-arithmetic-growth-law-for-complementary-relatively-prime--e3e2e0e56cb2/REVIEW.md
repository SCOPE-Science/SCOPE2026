# Independent mathematical audit

## correctness

PASS

Every nonempty subset of [n] with gcd g is g times a gcd-one subset of [floor(n/g)], so count f(floor(n/g)). The complement deficits also include the empty subset, yielding A=1+sum_{g>=2,g not dividing n} f(floor(n/g)) and B=1+sum_{g>=2,gcd(g,n)>1} f(floor(n/g)). The smallest admissible gcd is a(n) in A and least prime p(n) in B. Subsets containing 1 give 2^(m-1)<=f(m)<=2^m-1, so the first term controls each sum below and at most n+1 such terms control above; dividing the positive bounds proves exact factor 2(n+1) sandwich. For even n, p=2,a>=3 so h<=floor(n/3)-n/2; for odd n a=2,p>=3 so h>=floor(n/2)-floor(n/3). Exponential gaps dominate the factor n. Independently computed f by the gcd decomposition recurrence, then A,B and both rational inequalities for all 4<=n<=150 in exact integers. The infinite argument is analytic/combinatorial, not finite enumeration.

## originality

PASS

The 2013 primary paper explicitly poses this complementary-deficit quotient's limiting lower and upper behavior as Question 3.3. The later Pongsriiam parity sign theorem compares D and Phi and is weaker/different for their deficits from 2^n. A new uniform exponential sandwich determined by least nondivisor and least prime factor answers the specific limits; an exhaustive novelty guarantee is not claimed because the proof uses elementary known gcd partitions.

## value

PASS

The paper introducing D and Phi explicitly raised these two extremal complementary-deficit limits. Resolving a precise published open quantitative question and giving a uniform pointwise arithmetic exponent h(n) is a motivated and potentially reusable invariant, beyond an elementary parity sign. Its proof is short but the result is genuinely a sharp qualitative even/odd separation and not merely a recomputation of known D(n) tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
