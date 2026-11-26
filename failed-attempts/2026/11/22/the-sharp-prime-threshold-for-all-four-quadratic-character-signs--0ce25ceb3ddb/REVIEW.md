# Independent mathematical audit

## correctness

PASS

Reviewed RESULT.md:3–48, VERIFICATION.md and verify_square_index_patterns.py. The indicator in x contributes 16 for a matching word with all arguments nonzero, at most 8 for each of at most eight inputs having a zero argument, and at most 16 for the excluded x=0. For any nonempty subset of the four distinct nonzero shifts at p>=5, the product of the quadratic factors is squarefree: each root is simple and the factors have no shared root. The quadratic Weil bound gives (2|S|−1)sqrt(p) for the character sum, with coefficients totaling 49, so 16N_p^×>=p−49sqrt(p)−80. At 2579, (2579−80)^2>49^2*2579 and 2579−80>0; the lower bound increases thereafter. Independent replay: python3 /workspace/branches/replay_frozen_review.py 1 uses trial division, a residue table from successive odd differences of squares and scans the cyclic windows rejecting zeros. It exhausts all 373 primes 5<=p<2579, reproducing the exact 24 primes and their missing-word counts and the full mask fingerprint ae46170c708cc49792a01577a3ce855d0f2c54dda0f6a570596d42045a6d44aa. At 193 the mask is 0x7fff, at 197 it is 0xffff, and at 5 no valid window remains. The enumeration and proven tail together establish the classification, including that 197 is the first prime after the last exception.

## originality

FAIL

The exact exception list is mechanically recoverable from a prior complete finite six-word support generator and its proved infinite tail. An accepted square-start four-sign word is exactly an R-leading nonwrapping five-word; for p>=7 its occurrence is equivalent to occurrence as either the five-prefix or five-suffix of an occurring six-word. The earlier six-word record's published checker computes the full 64-bit support at all odd primes below 16384, including every bridge prime, and its theorem gives full support at p>=461. Project both ends, keep the R-leading words, and handle the empty case p=5. This yields the entire claimed prime-to-mask classification, not merely a large-prime existence statement. Separately, Buchaev–Tsfasman's July 2026 Theorem 2 already gives exact multiplicities for all these five-words. The decimal cutoff/list need not have been printed for the prior coverage to be decisive.

## value

FAIL

This exact cutoff is natural and the standalone verification is useful, but as a narrow proposed new invariant it is mechanically determined by the earlier finite six-pattern certificate and infinite theorem. The extraction needs only the two end projections and deletion of words starting with N. The frozen result supplies no further structural consequence or distinct non-covered invariant, so it is a correct repackaging rather than a surviving valuable new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
