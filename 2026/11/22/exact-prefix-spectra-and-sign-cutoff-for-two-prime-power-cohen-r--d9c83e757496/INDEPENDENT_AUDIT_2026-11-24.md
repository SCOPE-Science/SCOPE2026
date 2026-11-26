# Independent mathematical audit

## correctness

PASS

Only four divisors contribute, with coefficients H, −HP, −HQ, HPQ and respective divisibility conditions H, HP, HQ, HPQ. For t=floor(n/H) in 0,…,PQ−1, summing yields F(n)=H((t mod P)−Q floor(t/Q)). Each block [jQ,(j+1)Q) contains every residue modulo P since Q>P; its band is disjoint from the next because P−1<Q. The number of t of residue r is the difference of the floors at ((j+1)Q−1−r)/P and (jQ−1−r)/P, and each t accounts for H indices. This proves the exact multiplicities and both extrema. The first band is nonnegative and the remaining ones are strictly negative; this cutoff is within one period. The full-period term at n=HPQ makes F(HPQ)=0, and periodicity of the summands then gives period HPQ. A proposed period d with HQ≤d<HPQ contradicts F(d)<0=F(0); one with d<HQ would force all values to be nonnegative. The inspected verifier's recorded 103 tuples and 1,138,338 indices are finite corroboration, not an independent runtime reproduction or the basis of the proof.

## originality

PASS

The divisor identity and study of extrema of these prefixes are prior art. The supported distinct result is the full fixed-modulus two-prime-power classification, including per-value counts, exact extrema and a sharp one-period sign cutoff. It is not a specialization of the prefix norm lower bound or the modulus-summed explicit formula in the primary sources checked.

## value

PASS

Prefix extrema are an existing question for Cohen sums. The full distribution over the first modulus family with two distinct primes gives exact signed benchmarks and determines where a prefix can be nonnegative without enumerating its period. This is an infinite parameter result about a natural cumulative invariant; the separated bands and single cutoff, not the divisor formula itself or the k=6 example, provide the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
