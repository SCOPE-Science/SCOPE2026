# Scientific review: exact three-marker palindromic defect

## Correctness — PASS

The claimed domain is all indexed linear binary words with exactly three ones, represented uniquely by four nonnegative zero gaps. The proof partitions distinct palindromic factors into zero-, one-, two-, and three-marker types, treats the coincidence of the two inner gaps separately, and derives the stated defect by exact min/max identities. Its enumeration of defect layers uses an explicit bijection with two inner-gap orientations and a boundary pair of outer slack variables; every generating-function denominator is justified. The limiting law follows from a triple-pole coefficient estimate and a Riemann-sum argument, not from extrapolating a finite table. The independent finite checker passed 52,360 direct indexed words and 104,976 gap quadruples. The proof does not claim that a finite check certifies infinitely many lengths.

## Originality — PASS, with historical-priority risk

Glen–Justin–Widmer–Zamboni, *Palindromic Richness*, arXiv:0801.1656, introduces the class and general defect framework; it does not state the weight-three four-gap formula or its exact defect distribution. Bucci–De Luca–Glen–Zamboni, arXiv:0807.2303, gives general structural equivalents for richness, not a conditioned finite-content count. Vesti, *Extensions of Rich Words*, arXiv:1312.4350, Section 4, records the four shortest unrestricted non-rich binary words at length eight and general counts through length 25; the new minimal family recovers two of those four and extends to all lengths and all positive defects. Results for *privileged* weight-three words concern a distinct recursive property, not palindrome-factor totals, so the earlier formula does not imply the present theorem. Semantic published-record searches and focused web/OEIS searches did not identify an all-length fixed-weight defect theorem. No search can rule out an unindexed specialization; independent priority checking remains advisable.

## Value — PASS

The restriction to exactly three ones is mathematically motivated: every binary word with zero, one or two ones is rich, whereas weight three is the first nontrivial sparsity layer and already contains Vesti's shortest non-rich examples. The theorem resolves every defect value at every length, gives an infinite minimal forbidden-factor family, and finds a nondegenerate scale-normalized defect law with an explicit atom and density. The whole distribution is more informative than an isolated sample length, a single counterexample, or a routine renaming.

## Limits

No claims are made about general Hamming weight, cyclic words, multiplicity-weighted palindromic observations, or a general theorem for all binary strings. No independent mathematical audit has been performed; an implicit equivalent in inaccessible or unindexed work remains possible.

Self-review: passed. Independent audit: not yet performed.
