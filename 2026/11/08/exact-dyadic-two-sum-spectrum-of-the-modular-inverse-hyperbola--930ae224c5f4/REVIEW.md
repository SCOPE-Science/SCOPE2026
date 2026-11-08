# Scientific review

## Correctness — PASS

The exact fiber reduction is a two-way equivalence: for a nonzero target with equal coordinate valuation \(h\), every ordered representation corresponds to one square root of \((s/2)^2-(s/2^h)(t/2^h)^{-1}\) modulo \(2^{k-h}\), with exactly \(2^h\) lifts. The proof separately establishes the zero fiber, odd/even discriminant square counts, the disjoint valuation-shell count, and Haar continuity. Direct independent enumeration in `verify.py` checks all target fibers through \(k=9\). No finite computation is used to justify infinite quantifiers.

## Originality — PASS with historical risk

The closest full primary text is Gong–Veys–Wan (arXiv:1306.4104), which explicitly determines the dyadic fourth moment in its \(n=4\) case. That result is **not** counted as new. It determines the sum of squared multiplicities, not their pointwise values or their zero/nonzero support. Bower–Evans–Luo–Miller (arXiv:1212.2930) treats one-coordinate sums of modular hyperbola points, rather than the simultaneous vector sum of two points. Both works were compared by implications and the relevant sections read. Searches of mathematical literature, published result records, and accessible prior research claims found no stronger full dyadic two-sum representation spectrum; residual priority risk remains.

## Mathematical value — PASS

The exact joint two-coordinate sumset and full ordered multiplicity function are natural invariants of a canonical modular hyperbola. The all-exponent count gives the non-obvious asymptotic ambient density \(1/96\) in \(\mathbb Z_2^2\), which is not determined by either the known scalar coordinate sumsets or the known aggregate fourth moment. The valuation-shell decomposition explains the arithmetic obstruction structurally, rather than merely reporting a finite table.

## Limits

Only the unit inverse graph over powers of two is treated. The work does not assert priority over any unseen equivalent source and makes no claim that the existing fourth moment is new. The included program checks bounded moduli; the proof handles all exponents. No independent audit has taken place.

Self-review: passed. Independent audit: not yet performed.
