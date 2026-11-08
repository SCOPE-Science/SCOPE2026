# Self-review

## Correctness — PASS

The result uses an exact full-run palindrome classification followed by an AM–GM bound on paired run minima, a complete upper bound for shorter-run palindromes, and a balanced-run attaining family. The three- and four-run cases are counted separately with positive-run boundary conditions and integer optimization. `verify.py` independently compares direct subsequence sets with a dynamic count on short words and checks the two finite formulas. The mathematical proof, not finite computations, establishes the unbounded claim. Residual risk is a possible overlooked embedding case; the one-to-one full-run correspondence and the separate lower-run bound address it.

## Originality — PASS with bibliographic qualification

The 2021 full-text paper by Mahalingam and Pandoh studies exactly the scattered-palindrome count, but its general Fibonacci upper bound and alphabet-size extremal formulas do not imply the sharp dependence on a fixed binary run count or the exact three-/four-run equality. The 2009 full-text work of Holub and Saari determines words from their scattered-palindrome sets and studies longest-palindrome and extension-ratio invariants, not run-conditioned cardinality maxima. The 2019 full-text paper by Müllner and Ryzhikov studies longest palindromic subsequences rather than distinct-subsequence enumeration. Searches for run-conditioned maxima, constant-block/paired-run decompositions, and equivalent polynomial leading terms found no covering theorem. Residual bibliographic risk remains from unindexed literature; absence from searches is not a proof of global priority.

## Mathematical value — PASS

For a fixed number of constant-letter runs, the sharp growth changes from the unrestricted exponential upper envelope to a polynomial whose degree and leading coefficient are explicit for every odd run count. The unexpected exact three-/four-run plateau gives a finite-length structural boundary. The result makes run count a natural stratification parameter for the previously studied extremal problem, not an arbitrary isolated numerical slice.

## Closest literature and limits

Mahalingam–Pandoh, arXiv:2108.02729, §§3–5; Holub–Saari (2009), §§2–5; Müllner–Ryzhikov, arXiv:1901.07502, §§1–2. The asymptotic claim fixes the odd run count before allowing length to grow. Only the first even run count beyond the two-run trivial regime is solved exactly; no exact general formula for arbitrary even run counts is asserted.

Self-review: passed. Independent audit: not yet performed.
