# Self-review

## Correctness

PASS. The finite theorem counts all \(2^{23}=8{,}388{,}608\) words, not a sample. The first enumerator's additive fingerprint has the one-way invariant that equal complete profiles must map to one bucket; the algorithm's size-one and reversal-pair shortcuts are justified by direct reversal symmetry, and other buckets are split by complete exact composition vectors. The independent second enumerator uses distinct prefix-sum logic and labels, and agrees on all three class-size counts and all 160 explicit four-word groups. The Python verifier checks full exact profiles, factorization among divisors of \(24\), closure, and complement pairing. Both full integer enumerations and downstream checks passed after packaging. There is no unproved infinite extrapolation or assumed collision resistance.

## Originality

PASS, subject to historical priority review. The closest primary original and expanded papers establish polynomial equivalence and interleaving; they explicitly show that the *first existence* of noninterleaved confusion is at length \(23\), with one example. They do not give the exhaustive \(4{,}096/4{,}191{,}936/160\) fiber-size distribution, exactly eight indecomposable four-word classes, four complement pairs, or the resulting optimal noiseless codebook size. The 2022 Gupta–Mahdavifar full-composition paper addresses algorithms and specific large codebooks rather than an exact all-word census. Dedicated searches of published research records and local prior claims found nearby work only on length-two or bounded read observations, not on this full length-23 spectrum. The general factorization theorem supplies a possible method but does not imply these specific totals without new finite calculation. Unindexed computational tables and later unpublished work remain priority risks.

## Value

PASS. Length \(23\) is the known **first** length where all confusions need not come from interleaving, not an arbitrary parameter selected after computation. A complete count of the first exceptional class families and the exact best reconstruction codebook size resolves a natural and historically motivated finite boundary. The eight explicit indecomposable classes quantify the failure of the earlier normal construction mechanism and provide concrete regression data for polynomial-factorization reconstruction algorithms.

## Closest literature, evidence, and limits

Acharya et al., arXiv:1403.2439v1 (2014), sections 10–11, and their expanded SIAM manuscript, section 11, contain the general methods and a particular 23-bit noninterleaving pair; these are credited, not repackaged as new. Gupta–Mahdavifar, arXiv:2201.09955, focuses on reconstruction algorithms and codebooks. Reproducibility is supplied in `exact_census.cpp`, `independent_census.cpp`, `verify.py`, and `FOUR_CLASSES.txt`. The result is finite, exact and self-reviewed, **not** independently certified.

Self-review: passed. Independent audit: not yet performed.
