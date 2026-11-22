# Scientific review: radius-two Kendall balls for repeated-symbol words

## Correctness

**PASS.** The swap-history classification distinguishes disjoint transpositions from overlap three-cycles using the minimal interval on which an output differs. Counting the two overlap histories for three distinct letters, one for an exactly-one-change triple, and zero for an alternating-return or constant triple yields the displayed formula with both endpoint corrections. The two-state polynomial enumerator follows from the equality status of successive adjacent pairs. The binary extremizers, exact mean, Gaussian limit, and rare-collision Poisson limit follow from the same identities. An independent finite breadth-first enumeration checks all 33,730 centers in the declared parameter ranges and verifies the weighted transfer enumerator. The proof, rather than bounded testing, supports arbitrary lengths.

## Originality

**PASS, with priority risk.** The closest available literature establishes radius-one sizes and radius-two bounds for multipermutations (Buzaglo–Yaakobi–Etzion–Bruck, 2013), codes for distinct-label Kendall permutations (Bereg et al., 2023), unrestricted-position swap graphs (Adamson et al., 2023), and star-swap Gray codes (Gregor–Merino–Mütze, 2023). None of the inspected mathematical statements implies the exact per-center correction formula or its full joint-statistic distribution. Searching the terms “radius two ball Kendall multiset permutation exact center size”, “adjacent swap distance at most two q-ary strings exact output-ball size mean variance”, and “radius two balls in Kendall tau metric on multiset permutations arbitrary center” found no equivalent full theorem. This does not exclude earlier unindexed equivalent results, especially as a specialization of an unrecognized general theorem.

## Value

**PASS.** Adjacent-transposition errors on words with repeated symbols are a standard model for rank-modulation and multipermutation coding. Explicit local corrections characterize the exact channel ambiguity for *every center*, while the polynomial law converts them into an all-blocklength census; this provides more information than an extremal size or an asymptotic bound. The two probability regimes reveal a Gaussian fixed-alphabet fluctuation law and a Poisson rare-collision law. No optimal code size or error-correcting decoder is claimed.

## Scope and residual risks

The results concern radius at most two, indexed linear words, and uniformly random labeled words for the stated limits. Prior work could contain an overlooked equivalent expression; mathematical priority requires a broader independent literature review. Computational enumeration checks only finite instances and does not constitute independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
