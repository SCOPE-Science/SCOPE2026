# Review: exact first-repeat complexity in a period-doubling fixed point

## Correctness
PASS. Equality of sufficiently long factors forces agreement of starting-position parity because the fixed point has no `0000`. Within each parity the substitution's forced zeros reduce the equality question to shorter factors exactly, not approximately. The first repeated index therefore obeys the proved recurrence; direct base cases yield the closed form and two extremal limit ratios. The independent finite word generator and exact-slice checker agree through factor length 512. No computation is used as an infinite proof.

## Originality
PASS, with residual priority risk. Nicholson–Rampersad (2015, arXiv:1507.08206) gives the same invariant for Thue–Morse, Fibonacci and Tribonacci, not period-doubling. Huang–Zhang (2014, arXiv:1408.5495) and Huang–Wen (2016, arXiv:1606.05150) enumerate recurrence positions or return words of individual period-doubling factors, not the first collision optimized over all factors of fixed length. OEIS A366462/A367184 concern longest no-repeat factor windows at arbitrary starting positions, a demonstrably different invariant. The occurrence-position theory is the closest possible broader coverage and could support a separate derivation, so historical uniqueness is not certified.

## Mathematical value
PASS. The first-repeat index is an established natural initial-complexity invariant; the theorem computes its full dyadic dependence and exact normalized lower/upper limits for a canonical automatic word. The general parity mechanism gives a structural reason for the result and isolates it from generic factor-count tables.

## Limitations
Only the fixed point beginning with zero, not its arbitrary shift or the unrestricted maximum over starting positions, is classified. A finite verification does not imply the universal statement. Historical-priority uncertainty remains, especially with earlier general individual-factor position formulas. Independent mathematical audit has not occurred.

## Closest literature
- Y. Huang and H. Zhang, arXiv:1408.5495, Sections 5–6 (factor occurrence/gap formulas).
- J. Nicholson and N. Rampersad, arXiv:1507.08206 (definition; Thue–Morse/Fibonacci/Tribonacci).
- Y. Huang and Z. Wen, arXiv:1606.05150 (return words for the same fixed point).
- OEIS A366462 and A367184 (best repeat-free windows anywhere).

Self-review: passed. Independent audit: not yet performed.
