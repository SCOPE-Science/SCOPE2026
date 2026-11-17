# Independent mathematical audit

## correctness

PASS

Partitioning legal subsets by whether their largest index is used proves B_n=B_(n−1)∪(c_n+B_(n−2)). The independent bitset computation on the pinned arithmetic recurrence verified all 8,147 integers from 9084 to U41=17230 and all 9,439 from 9084 to U42=18522, with 9083 absent from B45 and c45=8911≤9083<c46=9316. The source checker uses a second boolean-array DP for finite exhaustion; its complete Python source was inspected. For every n≥43, inequalities U_n−U_(n−2)≤c_n and U_(n−1)+1≥9084+c_n, U_n=⌊n³/4⌋, ensure overlapping/touching intervals and induction to unbounded U_n. Independent numerical checks of inequalities to 5000 only supplement their elementary symbolic proof.

## originality

PASS

Pollock/Kureš proves at most eleven centered-nonagonal summands with repetition, and OEIS A352349 lists largest obstruction 2648 for sums of DISTINCT centered nonagonal numbers without forbidding adjacent indices. Neither permits the exact inversion of the stricter nonconsecutive-index subset constraint. Dantas e Moura et al. S-legal index-difference theorem concerns a specially greedily built sequence, not the fixed quadratic c_j; its full paper Definition 1.9 was inspected. No exact 9083 obstruction table for this indexed quadratic sequence was found in independent indexed searches.

## value

PASS

The ban on adjacent indices is a natural representation constraint from Zeckendorf-style legal sums; the complete finite complement cutoff for a standard centered polygonal sequence is an exact independent invariant, not an arbitrary tiny numerical slice. It quantifies a nontrivial distinction between unrestricted, distinct-only, and index-gap-restricted additive coverage. Finite computation supports a provable infinite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
