# Scientific review

## Correctness — PASS

The four-term exclusion uses a rigorous descent on the positive progression step: an odd step hits the forbidden class two modulo four, while even steps with admissible terms reduce by two or four. The all-depth three-term count follows from an explicit exhaustive ten-state carry automaton and an exact polynomial-vector identity. In the standalone `CHECK.py` the reachability closure, transition table, polynomial certificate and finite independent cross-checks pass 90,102 exact integer assertions. The proof, rather than finite extrapolation, establishes the infinite identities. Scope includes zero under the original initial-value convention, and the strict dyadic upper bound is tracked by the final carry state.

## Originality — PASS (with limitations)

Baum and Sweet (1976), OEIS A060142/A086747 and Rowland–Yassawi (2012, Example 4.3) define the automatic sequence and its binary recurrence, not the evaluated arithmetic-progression census. The closest same-set research result, *Three exact additive sumsets of the zero-run-even integers*, determines two-summand images and Fibonacci single-set counts; the quantified statements do not imply the triple progression formula. The digital progression census in individual Pascal rows studies a different family of supports. No inspected published result or indexed search establishes the exact rational triple census or the sharp global absence of four-term progressions. Relevant 1976 full text was unavailable, and historical-index coverage is incomplete, so the originality judgment is not a priority certification.

## Mathematical value — PASS

For a sparse classical automatic set, the natural two-point sumset identities do not resolve arithmetic progression abundance. The exact dyadic triple-frequency generating function and the sharp maximal progression length determine the entire length spectrum and all triple counts at natural binary scales. The counting identity is genuinely stronger than observing three isolated allowed indices; it is supported by an exact finite symbolic identity for arbitrarily many digits.

## Prior literature and limits

References: Baum–Sweet, *Annals of Mathematics* 103 (1976), 593–610; OEIS A060142 and A086747; Rowland–Yassawi arXiv:1209.6008v1 (2012); the published exact additive-sumsets and Pascal-row progression results. No full article text was verified for the 1976 source. The count is for intervals \(0\le a<a+d<a+2d<2^L\), not arbitrary endpoints or fixed-step spectra. Day-level verification for the source set begins with the March 5, 2001 OEIS entry, despite the earlier 1976 origin.

Self-review: passed. Independent audit: not yet performed.
