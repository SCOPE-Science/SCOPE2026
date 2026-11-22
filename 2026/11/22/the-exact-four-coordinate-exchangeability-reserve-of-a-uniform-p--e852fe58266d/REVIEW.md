# Mathematical review

## Correctness

**PASS.** The claim has exact quantifiers: \(m\ge1\), \(N\ge m\), and uniform random perfect matchings of the complete graph with fixed disjoint designated edges. The probability of retaining prescribed edges follows from double-factorial enumeration. Hypergeometric moment rigidity proves the sharp obstruction; the displayed formal generating-function identity supplies the recurrence needed for the global positivity proof, with no reliance on an unproved numerical extrapolation. The moment inversion establishes the explicit and unique extension; the two small cases are handled separately. The standalone exact checker passed 1,258 assertions, including complete enumeration through six matching edges.

## Originality

**PASS with priority risk.** General signed-mixture representations (Janson–Konstantopoulos–Yuan, 2014), broad positive-extendibility criteria (Konstantopoulos–Yuan, 2015), and perfect-matching intersecting/derangement enumeration (Godsil–Meagher, 2015) were compared at the level of their actual statements. They do not explicitly give this universal four-coordinate horizon or the unique positive extension law. A hidden specialization in older finite-exchangeability literature remains possible. General algorithms to test extendibility are not themselves the evaluated matching-specific theorem.

## Value

**PASS.** The maximum extension size is exact for an infinite family and has a universal additive constant independent of matching order. The support argument gives a sharp impossibility certificate; the positive-coefficient construction supplies a realizable extremal law. The example is motivated by distinguishing ordinary positive dependence and finite/infinite exchangeability, rather than merely tabulating matching counts.

## Scientific limits

No assertion is made for weighted/nonuniform matchings or general indicator families. Historical-priority comparisons are bounded to listed sources and research records; independent confirmation is still needed. Exact finite computations support but do not prove the all-size theorem.

Self-review: passed. Independent audit: not yet performed.
