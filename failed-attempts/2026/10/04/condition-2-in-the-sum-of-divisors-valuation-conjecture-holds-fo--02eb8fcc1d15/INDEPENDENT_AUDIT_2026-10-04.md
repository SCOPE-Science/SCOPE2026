# Independent mathematical audit

## correctness

PASS

The source valuation formula and the package's case analysis are valid. For p=3 the only nontrivial order is 2; for p=5 the nontrivial orders are 2 and 4. The p-power part of q+1 is strictly below q, and in the order-4 case the p-power part of q^2+1 is strictly below q^2; together with the elementary exponent bounds this yields the claimed strict size inequality. The q=p case has valuation zero. The packaged finite checker is only corroborative and is not used for the infinite proof.

## originality

FAIL

The claim is correct, but the 2020/2021 primary source already contains enough stronger local structure to imply these two cases routinely. Its Theorem 6.2 proves the floor inequality for every Type-1 prime-power case. For p=3 every q>3 and exponent falls into Type 1. For p=5 every q>5 case is Type 1 except the order-4 exponent a=3 case; there Lemma 6.1 says reaching the ceiling would force sigma(q^3) to be a pure power of 5, impossible because sigma(q^3)=(q+1)(q^2+1) and q+1>1 is not divisible by 5 when q is 2 or 3 mod 5. Thus the audited p=3,5 theorem is a direct corollary of the source's own Theorem 6.2 and Lemma 6.1 plus one elementary factorization, irrespective of whether the later Zhao--Chen paper repeats it.

## value

FAIL

Although the claim is framed as the first two odd-prime cases of a motivated structural conjecture, after reading the source's stronger Section 6 machinery the result reduces to a routine specialization of its Type-1 theorem plus one elementary factorization for the only p=5 exceptional exponent. Under the common value bar this is too close to a mechanically available corollary to constitute a worthwhile independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
