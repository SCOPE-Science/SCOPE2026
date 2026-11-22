# Review of the Markov-source random-minimizer density theorem

## Correctness

**PASS.** Four overlapping \(k\)-mer positions can have repeats only through periods one, two and three. Under the no-`11` constraint all thirteen collision contexts are explicitly classified, their charged probabilities checked against direct order rankings, and their stationary Markov weights summed. The two alternating boundary cases cancel by reversibility. The all-length formula, the special one-letter case, the sharp phase comparison and the golden-mean resonance are proved directly; the included exact finite checks validate, but do not replace, the proof.

## Originality

**PASS, with historical-priority risk.** The closest inspected primary theorem is Golan--Shur's 2024 iid uniform-source random-minimizer density formula. It provides a general charge identity, which is credited, but not the source-dependent Markov evaluation or its asymptotic sign transition. Zheng--Kingsford--Marçais 2020 also assumes independent letters. The related golden-mean lexicographic-order result is different because no average over orders is taken. Semantic searches for equivalents and stronger results yielded no covering statement. An unindexed weighted-input derivation may exist.

## Value

**PASS.** Exact sketching density across the entire nondegenerate forbidden-`11` Markov family exposes a sharp transition in the direction of the finite-length correction; the natural maximal-entropy measure is the boundary and has an exact period-three coefficient pattern. This answers a source-sensitive computational-sketching question beyond a small enumeration and supplies a baseline for correlated inputs without claiming optimality or practical genomic performance.

## Verification and limitations

The standard-library checker compares direct orders and source probabilities over all 6,752 admissible contexts of block length \(k+3\) for \(1\le k\le13\) at five rational transition parameters, checks the complete exceptional context list through \(k=80\), and numerically verifies the golden-mean reduction at high precision. The mathematical proof extends the conclusion to all integer \(k\) and all real \(0<p<1\). Individual-order fluctuations, nonstationary sources and windows other than three lie outside scope.

Self-review: passed. Independent audit: not yet performed.
