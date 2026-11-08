# Scientific review

## Correctness — PASS

A complete proof partitions the factors into zero, one, two, and at least three ones. The two-one factors have exact surrounding-gap constraints, and factors with at least three ones have strictly increasing complete internal gaps. Only the former and one-one factors admit nonpalindromic reversal partners. Their pair-generating functions together with ordinary factor enumeration yield the claimed rational generating function and all six residue formulas. The standalone checker directly enumerated every factor for 124 selected lengths through 250. Remaining correctness risk: the computer tests are finite and independent proof review has not occurred.

## Originality — PASS (qualified)

The full-text source by Allouche et al. [1] introduces the invariant and gives general comparisons, not this explicit triangular-marker evaluation. The 2025 refinement [2] treats eventual-periodicity and minimum-growth classes; the 2026 generalization [3] treats groups of antimorphisms and other word families. The exact period-six formula is not implied by those statements: its proof requires a language-specific classification of reversal partners. Public sequence record [4] lists the underlying triangular-marker word but no such quotient-factor count. Searches of published records and nearby mathematical formulations found no direct equivalent. Residual risk: unindexed specialized literature may contain the result; lack of a retrieved match does not establish absolute novelty.

## Mathematical value — PASS

This gives a complete evaluation of a recently introduced factor-complexity invariant for a natural nonrecurrent sparse word. The nontrivial cancellation between quadratic ordinary complexity and the reversed pairs yields a sharp quadratic quasi-polynomial with least period six and asymptotic ratio \(2/3\), illustrating behavior different from reversal-closed and ultimately reflected-factor-free settings. The exact structural threshold—reversal partners can contain no more than two ones—is the mechanism, not an arbitrary numerical table. It does not attempt a general increasing-gap classification.

## Literature and limitations

[1] Allouche, Campbell, Li, Shallit, Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302.
[2] Dvořáková, Pelantová, *Reflection on the reflection complexity*, arXiv:2511.12358.
[3] Blažek, Dvořáková, Pelantová, *Generalized reflection complexity*, arXiv:2610.14637.
[4] OEIS A076127, https://oeis.org/A076127.

Self-review: passed. Independent audit: not yet performed.
