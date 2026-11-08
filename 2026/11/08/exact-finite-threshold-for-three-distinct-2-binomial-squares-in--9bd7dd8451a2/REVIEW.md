# Scientific review

## Correctness — PASS

For halves of equal length, 2-binomial equivalence is equivalent to equality of zero count and scattered \(01\)-subsequence count. The one-letter extension recurrence adds only newly completed suffixes, and pruning at four distinct square strings is monotone. Full-layer enumeration at lengths \(43\) and \(44\) gives respectively four and zero admissible words; the four explicit witnesses have exactly three square types. Two executable standard-library implementations reproduce the result using different binomial-equivalence computations and enumeration orders. The upper bound is thus a finite exhaustive certificate, not an extrapolation.

## Originality — PASS with priority limitation

Rao, Rigo and Salimov's 2013/2015 primary paper defines the exact repetition notion and states in Section 4, Fact 1, that an *infinite* binary word cannot have only three distinct 2-binomial squares. The inspected PDF does not state the sharp finite bound \(43\) or classify length-\(43\) extremizers. Rigo and Salimov's second paper studies 2-binomial factor complexity, not a finite distinct-square maximum. Gabric and Shallit consider ordinary squares, which are a strict subclass of 2-binomial squares. Targeted historical and indexed-claim comparisons did not disclose a theorem covering the cutoff or extremizer classification; unindexed computational enumerations remain a live but nondecisive priority risk.

## Value — PASS

This is the natural extremal finite-length counterpart of the published three-square impossibility statement. It resolves how long the exceptional configuration can persist, gives the sharp obstruction length, and classifies all maximizers. The result is not an arbitrary tabulated prefix or numerical increment: the cutoff is the maximum of an explicitly motivated finite avoidance problem and the certificate is exhaustive.

## Limits and comparison

The proof is computer-assisted via two included exhaustive Python programs, with the recurrence and safe pruning justified mathematically. There is no claim about the optimal finite cutoff for four or more square types, or about independent certification. An earlier unindexed enumeration could affect historical originality.

Self-review: passed. Independent audit: not yet performed.
