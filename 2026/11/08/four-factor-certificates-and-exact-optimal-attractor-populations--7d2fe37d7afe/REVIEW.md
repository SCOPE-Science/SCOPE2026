# Scientific review: two-run periodic attractors

## Correctness (C): PASS

The result is a single theorem with a factor-certificate equivalence, exact counts and irredundance. For factors of length at least the period, overlapping translated occurrences cover the central interperiod transition; shorter factors are separated into unary, those containing a \(10\), and those of the form \(0^r1^s\). These exhaust every factor. In the pair count, opposite-letter markers are necessary and suffice exactly in the cases classified by their transitions. Singleton-run edge cases are proved separately. The independently implemented checker exhaustively tested 330,960 candidate position subsets and 150 pair-count parameter triples. The infinite proof does not depend on these finite checks.

## Originality (O): PASS, qualified

Banbara et al. (2026) classify Fibonacci, period-doubling and Thue–Morse words, not the general family of two-run powers. Mantaci et al. (2019) give a general power-size inequality and two-run base examples, not all-power optimum counts or the arbitrary-size certificate. Faro et al. (2026) treat Thue–Morse factor certificates. General algorithms are not equivalent to an all-family closed certificate. The alternating subclass and equal-run two-copy subfamily are covered by earlier results and are explicitly not asserted to be new. Unindexed equivalent research remains a genuine priority risk; full access to one comparison preprint was unavailable.

## Value (V): PASS

A four-factor test for arbitrary cardinality replaces a potentially unbounded collection of factor constraints over every power length. The exact counts distinguish two nondegenerate run lengths from singleton-run cases and classify all smallest attractors, a motivated fine-grained repetitiveness parameter beyond the previously known minimum size. This is a complete natural three-parameter family classification, not an arbitrary finite computation.

## Scope and limits

Only finite linear words of the form \((0^a1^b)^t\) with \(a,b\ge1\) and \(t\ge2\) are covered. No minimum number of *arbitrary* alternative test factors is claimed. The certificate proof is symbolic; finite exhaustive checks are corroboration. Independent validation and definitive historical priority have not been established.

Self-review: passed. Independent audit: not yet performed.
