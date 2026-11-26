# Independent mathematical audit

## correctness

PASS

The admissible coefficients form a nonempty set, and the gcd valuation is the minimum of their valuations. Kummer's theorem identifies these with borrow counts. With both digit parities present, selecting two opposite-parity occupied positions gives a zero-borrow index unless it exhausts N. With just one parity present there must be at least two occupied positions, and selecting p^i+p^(j−1) for occupied i<j borrows exactly once from position j. For the two-unit row, no proper selected index fits digitwise. Exactly one carry would give two positive digit sums with total p+1, so each alternating digit sum for the two summands would have to vanish by divisibility by p+1; a lone carry changes their combined alternating sum by ±(p+1), a contradiction. The indicated witnesses produce exactly two borrows for both adjacent and nonadjacent occupied positions, including p=2. Excluding N=1+p makes p+p² the first admissible such row. The supplied checker was inspected but not executed; the decision rests on the symbolic argument.

## originality

FAIL

An earlier stronger theorem already gives the exact locus and more: Fairfax-Ball, Restricted Binomial GCDs at Primes Congruent to −1, arXiv:2609.37754v1 (29 September 2026), Theorem 1.1, specializes with m=p+1 to the entire finding. This is direct theorem-level coverage, not just overlap in the maximum or a finite instance.

## value

FAIL

The equality locus is a natural invariant, but as submitted it is the direct m=p+1 substitution into a known exact theorem, followed by a digit interpretation and immediate minimization. It supplies no surviving unknown invariant, generalization, or separate substantive proof-method claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
