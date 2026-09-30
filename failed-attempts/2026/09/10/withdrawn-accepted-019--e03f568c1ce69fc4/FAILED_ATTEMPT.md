# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/10/019`  
Independent audit date: 2026-09-28 (UTC)  
Task: `e07fc1d40020eb1144b5ef587cb17567`

The finite computation is mathematically valid, but the central e2(A7) surjectivity/width claim was already established by stronger prior results; the current package therefore fails originality and research-value review.

## Correctness retained

The finite computation is correct: the stored census has positive classwise preimage counts for all nine A_7 classes, so e_2(A_7)=A_7, and therefore width two follows trivially. The character-table/Frobenius calculation is consistent with E=G and yields N(g)=2520. The exact per-element counts form a valid computational invariant.

## Decisive prior-art issue

The central theorem is prior art. Martínez Carracedo's work on Engel words in alternating groups proves width bounds, and the 2019 computational paper 'A Computational Approach to Verbal Width for Engel Words in Alternating Groups' states that for 5<=n<=14 every element of A_n is an Engel word of arbitrary length. Taking n=7 and Engel length 2 already gives e_2(A_7)=A_7. The record's claim that no such surjectivity/width theorem was recorded beyond A_5/A_6 is therefore false. The detailed fiber-count table may be a new numerical refinement, but it does not rescue the originality of the packaged headline.

## Consequence

This package is relocated as a failed research attempt rather than silently deleted. Its computational artifacts may remain useful as verification/example material, but the headline must not be represented as an independently validated new finding.

## Literature

- [Martínez Carracedo, Engel Words in Alternating Groups](https://doi.org/10.1142/S0219498817500219): Establishes Engel-word width results in alternating groups.
- [A Computational Approach to Verbal Width for Engel Words in Alternating Groups](https://www.mdpi.com/2073-8994/11/7/877): States that every element of A_n for 5<=n<=14 is an Engel word of arbitrary length; this includes e_2-surjectivity on A_7.
