# Independent mathematical audit

## correctness

PASS

Friedman–Hoşten–Rosana Theorem 3.5 gives finite count [x^k] product_i(1+x^(s_i)) for the full Jordan partition. A finite discriminant critical set must have at least one size>=2 block, since diagonalizable repeated eigenvalues lead to infinity. Splitting a block a+b into a,b adds x^a+x^b coefficientwise, hence the largest possible coefficient occurs for partition (2,1^(n-2)), yielding binom(n-2,k)+binom(n-2,k-2), deficit 2binom(n-2,k-1). Complex symmetric N=[[i,1],[1,-i]] squares to zero and realizes the extremal block; direct sums with pairwise distinct eigenvalues meet the cited finiteness condition. n=2,k=1 correctly gives empty finite critical set. Independent exact small-n binomial/Jordan checks agree. The bound is mathematically correct.

## originality

FAIL

FAIL: prior Friedman–Hoşten–Rosana 2026 Theorem 3.5 already determines the exact finite critical count for EVERY complex symmetric Q, depending on its Jordan blocks. The assigned maximum and forbidden interval follow immediately by the coefficientwise splitting of factors (1+x^(a+b)) <=_coeff (1+x^a)(1+x^b), a one-line routine monotonicity consequence. The prior all-partitions statement mathematically dominates the entire claimed result despite not printing the same extremal number. This is not a separate independently novel classification.

## value

FAIL

FAIL: Although the discriminant gap is a natural quantity, the present package merely optimizes an exact previously published all-data counting formula by a coefficientwise elementary inequality. There is no additional independently motivated structural theorem or nontrivial method beyond this routine already-implicit extremal evaluation; exactness and a witness alone do not make it a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
