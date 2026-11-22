# Scientific review

## Correctness — PASS
The maximum of \(13\) is the orbit bound from the \(26\) non-self-negative ternary triples; a displayed word attains it. Every maximum cycle chooses exactly one triple from each of \(13\) complementary pairs, and such a choice supports precisely its Euler-circuit realizations. The package exhausts all \(8192\) choices, finds \(60\) connected balanced digraphs, uses exact integer directed-tree cofactors and the BEST theorem to obtain \(288\) cycles, and separately tests all \(1,594,323\) indexed words to obtain the same count. The independent direct test also produces the \(72\) symmetry orbits. The computation is a finite complete proof; no infinite conclusion is inferred from sampling.

## Originality — PASS against the inspected accessible evidence
Mitchell and Wild (arXiv:2603.25286, first posted 2026-03-26) establish the period and existence but do not enumerate all maximum ternary span-three cycles. The inspected published span-two involution classification has a strictly shorter window length and does not count maximizers. The inspected ternary order-three orientable-cycle classification pairs windows by reversal rather than modular negation and counts length-nine cycles, whereas the present cycles have length thirteen. Actual searches for negative-avoiding ternary optimizer enumeration and its complementary-window and Euler-tour aliases found no equivalent result. Residual risk: an unindexed enumeration could establish the same integer or a stronger classification.

## Value — PASS
A maximal negative-avoiding cycle uses every admissible observed three-window class once, a natural extremal design problem for phase/location encoding. The motivating recent paper proves existence but leaves the size and symmetry of this design space undetermined. Determining all \(288\) optimal cyclic designs, their \(72\) symmetry classes and the graph-degree/tour-count spectrum is a complete natural classification at the smallest span beyond the separately understood two-window setting. It is not presented as a new period bound, an asymptotic improvement, or a claim of practical optimization. The restriction to one alphabet and span is explicit.

## Sources and remaining limits
Primary source: Mitchell and Wild, *Negative Avoiding Sequences*, arXiv:2603.25286, especially Definitions 1.3 and 3.3, Theorems 3.2 and 4.1, Example 4.1 and Sections 5–8. Closest published comparisons: *Sharp length of involution-avoiding cyclic two-window words* (2026-10-18) and *Complete classification of maximum ternary order-three orientable cycles* (2026-11-08), whose complete result statements were read. This is an exhaustive finite computation, not an all-length theorem. Unindexed equivalent work and human verification remain open risks.

Self-review: passed. Independent audit: not yet performed.
