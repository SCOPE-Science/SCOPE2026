# Independent mathematical audit

## correctness

PASS

RESULT.md lines 20–38: F(1)=1 and F(x)≡1 mod x settle the case of an entry 1 and exclude nontrivial loops. For a proposed nontrivial pair with least smaller entry 2≤x<y, the integer z=F(x)/y has 1≤z<x and yz≡1 mod x. Since y is therefore invertible modulo x, y²F(z)=(yz)²−y(yz)+y²≡F(y)≡0 gives x|F(z). Together with z|F(x), this contradicts minimality or, when z=1, x|1. For A(n)=nH(n), grouping by d=n/gcd(n,j) gives ∑_{d|n}dφ(d), a multiplicative function with prime value F(p). At squarefree n, every prime must divide a factor other than its own if H(n) is integral. For two distinct primes this is impossible by the lemma; for general squarefree n, iterating any selection of one such outgoing edge produces a directed cycle in each weak component, necessarily of length at least three. Strongly connected singleton components with incoming or outgoing tails are not the scope of the statement. Independent finite replay tests both congruences for 2≤x<y≤1000 (365 candidates with y|F(x), no mutual pair). The frozen script uses symmetry and prunes impossible y rather than literally enumerating all ordered distinct pairs. Independently, trial division verifies 7,13,43,157 are prime and their product is 614341; the successive target F-values 24493,157,1807,43 are divisible by the source primes 7,157,13,43. The product of the F-values and the direct loop summing 614341/gcd(614341,j) for j=1,…,614341 both give 298791503101, or H=486361. The replay is bounded; the descent proves the universal claim.

## originality

FAIL

Mills's 1953 Theorem 3 and its supporting classification of reciprocal quadratic chains cover the central positive-integer theorem exactly. Its squarefree-semiprime and functional-graph consequences follow directly from that theorem and the already established multiplicative reduction for reciprocal gcd sums. The inspected modern motivating proposition gives only an upper bound, but that does not make the older exact classification new. The later indexed overlap is additional coverage, not a claim about priority between catalogue records.

## value

PASS

The structural obstruction is mathematically useful, because it turns a motivating upper-bound problem into exact exclusion for a natural squarefree class and rules out the shortest dependency cycles while a longer cycle is possible. Value is not assigned to recomputing the already tabulated witness, and the established older coverage prevents acceptance as an original finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
