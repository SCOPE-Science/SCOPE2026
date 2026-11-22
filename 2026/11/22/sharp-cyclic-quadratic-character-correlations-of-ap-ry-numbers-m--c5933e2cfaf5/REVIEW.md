# Mathematical review: cyclic quadratic-character correlations of Apéry numbers modulo seven

## Correctness — PASS

The exact integer binomial definition of Apéry numbers gives a Lucas digit-product modulo seven, using Lucas's binomial congruence and the low-digit carry exclusion. The seven digit values are \(1,5,3,3,3,5,1\), hence the sign vector is \(1,-1,-1,-1,-1,-1,1\). The proof computes the seven carry coefficients by finite sums, and every correlation follows recursively with the correct cyclic wrap. The induction separately handles shifts divisible by seven, interior nonzero lower digits, and both carry-boundary cases, including equality shifts. Inversion of the four sign moments proves all ordered pair frequencies. No probabilistic or finite-only argument is used for the all-depth statement. The standalone exact checker passed 3,098 assertions, which corroborate but do not replace the proof.

## Originality — PASS (with stated historical risk)

Gessel (1982) and Malik–Straub (2015) give the previously known Apéry Lucas factorization and digit residues; they do not provide this sharp finite cyclic all-shift correlation classification. Fan–Konieczny (2018) treat general digit-multiplicative sequences and unwrapped correlation uniformity, but the asserted finite cyclic extrema and exact equality shifts are not consequences explicitly stated there. Related signed correlation results for different arithmetic sequences cannot transfer their coefficient vectors or equality conditions to this Apéry sequence. The closest overlap risk is an implicit specialization of a general correlation-transducer result; the precise finite cyclic theorem was not recovered in the inspected material.

## Mathematical value — PASS

The nonvanishing Apéry congruence modulo seven produces a natural, nonconstant signed digital arithmetic sequence. For that sequence the theorem solves a complete all-shift, all-depth finite cyclic correlation problem, with an unexpectedly moving positive extremizer and a fixed negative extremizer, exact sharp values, and every ordered two-sign fiber. Those sharp equality classifications are not the automatic statement of the Lucas digit product, and they quantify a meaningful extremal distinction between different shift scales.

## Scientific limitations and references

The proof concerns quadratic characters of Apéry numbers modulo seven on cyclic blocks of length \(7^r\). It does not establish modulo-49 or full nonzero-residue distributions, nor an equivalent statement for unwrapped windows. Relevant primary literature: Gessel (1982), doi:10.1016/0022-314X(82)90071-3; Malik and Straub (2015), arXiv:1508.00297, including Example 6.1; Fan and Konieczny (2018), arXiv:1806.04267, on digit-multiplicative correlations. General-formulation priority remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
