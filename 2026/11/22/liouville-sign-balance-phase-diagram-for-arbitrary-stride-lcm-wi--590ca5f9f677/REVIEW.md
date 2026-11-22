# Review of the Liouville arbitrary-stride sign-balance theorem

## Correctness
**PASS.** The exact prime-local valuation identity proves periodicity and CRT factorization. At odd primes, the relevant sign sum is taken over an odd number of residues, hence cannot vanish. At two, even/odd window splitting establishes the binary recurrence; an induction on adjacent means with opposite-parity numerators proves the zero locus and the unit-magnitude locus. Conditioning on the starting index's two-adic valuation yields the exact stride mixture, whose three cases are solved exhaustively. The standard-library checker passed 128834 exact assertions, including actual product/LCM calculations over small complete periods. Its finite tests are only supplemental to the proof.

## Originality
**PASS, qualified.** Huang–Yang (arXiv:2611.15379v1) gives least periods for multiplicative-function progression quotients, not sign-density zero sets. Hong–Qian (arXiv:0903.0530v3) gives exact integer-quotient periods. The publicly accessible published-finding corpus fixed-progression histogram gives all individual value frequencies and may be used to construct conditional distributions, but it does not state the **uniform all-strides zero-set classification**. The known stride-one Liouville result covers the odd-stride branch only. Key residual risk: a mathematically equivalent unindexed corollary from the general value-frequency machinery may exist; search cannot prove uniqueness.

## Mathematical value
**PASS.** The invariant is naturally attached to a standard LCM quotient, and the classification is complete for every positive stride and window length. The previously unclassified positive-density balance cases \(\nu_2(c)=1,2\) and the sharp exclusion at \(\nu_2(c)\ge3\) identify a structural threshold rather than a mere sample computation. Exact bias magnitudes, minimal sign periods, and noninteger step variants are not claimed.

Self-review: passed. Independent audit: not yet performed.
