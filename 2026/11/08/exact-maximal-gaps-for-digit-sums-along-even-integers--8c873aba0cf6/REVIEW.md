# Review of exact maximal digit-sum gaps

## Correctness — PASS

The quantifiers cover every integer base \(q\ge2\), every target residue, and all consecutive hits. For even \(q\), the no-carry identity for \(2k+1\), aligned-block permutation, and explicit \(2k\) with \(q-2\) consecutive carry interactions yield the sharp \(2q-1\) gap. For odd \(q\), parity lifts the residue to its unique even class modulo \(2q\); each two-digit block omits at most one residue and two adjacent blocks cannot omit the same one. The three-digit prefix witness supplies equality and arbitrarily many translated witnesses. Boundary cases \(q=2,3\) and every residue are included. Independently calculated finite examples agree; finite checks are not substituted for the proof.

## Originality — PASS (qualified)

Boreico–El-Baz–Stoll, arXiv:1305.1017, studies the same digit-sum sequence, proves discrepancy sign oscillation, and gives Fourier-counting formulas; its inspected full text does not address maximal recurrence gaps. The exact parity-dependent consecutive-gap formula is neither a corollary of their stated discrepancy inequalities nor a direct evaluation of their block-count formulas, because the conclusion demands *all local intervals* and sharp carry witnesses. No exact covering claim was found in the research-index and public-literature searches. A generalized-Thue–Morse gap result outside the accessible searches remains a genuine priority risk; the original 1983 Dekking paper was not read in full.

## Mathematical value — PASS

The exact longest-gap constant is a natural local invariant of the same sequence whose global discrepancy was studied in the originating literature. It measures the strongest possible absence of any fixed digit-sum class and supplies a complete all-base/all-residue classification. The odd/even transition from quadratic to linear growth, with sharp infinitely repeating witnesses, is substantive and cannot be inferred from a density statement or an asymptotic counting error bound alone.

## Limitations

The result is for multiplier two and reduction modulo the base. It makes no claim about arbitrary multipliers, the finer return-time histogram, or the distribution of extremal starts. Historical priority is qualified by the uninspected Dekking original and possible equivalent formulations in word combinatorics.

Self-review: passed. Independent audit: not yet performed.
