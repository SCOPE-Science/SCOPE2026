# Independent mathematical audit

## correctness

PASS

Condition on the three assigned images. Each of the three forced edges removes one vertex in total when deleting fully forced cycles and contracting open paths. The remaining out- and in-stubs correspond to the same n-3 blocks, whose completions are uniform permutations, adding H_{n-3} to the expected forced-cycle count G. This works even at n=3. With D=n(n-1)(n-2), D E[G]=3n(n-2)+2. Fixed-point counts at source s are binom(n-s,2), (s-1)(n-s), or binom(s-1,2) according to the assigned rank. The swaps of the first two, outer two, and last two positions respectively contribute n-a-1 to 213, n-a-2 to 231 and a-1 to 312, and a to 132; all other completions of those swaps have pattern 321. Only 231 and 312 have forced three-cycles. Thus 6D Cov=6(F+M+J)-3n(n-2)-2, giving the four affine numerators; conjugation by order reversal also pairs 132 with 213 and 231 with 312 at the reflected start n-a-1. At n=3 the numerators in the original order are 1,-5,1,-5, as follows also from the cycle counts of the six permutations. The denominators are positive, the affine signs and n^2-scaled limits follow, and summing the two rows of either orientation pair gives -4/(6D). The zeros of the affine functions need not be admissible integer starts. The frozen verification files were read, not executed; their finite tests supplement the all-size proof.

## originality

FAIL

The four stated rows are exactly covered by a distinct indexed result giving all six positional rows, and also by a distinct conditional-expectation formulation. Those exact matches are later-dated, so they do not show earlier availability or derivation. There is independently a genuine earlier implication: Féray's exact Ewens injection formula gives the frozen mixed-moment identity by differentiation and summation, leaving just elementary counts of forced cycles in a length-three window. The older aggregate peak/descent results alone would not decide the oriented claim.

## value

FAIL

The local orientation effect and the peak/valley cancellation are mathematically interpretable, but no distinct contribution survives the exact stronger positional table. Moreover the earlier Ewens identity specializes to the counting formula via a single derivative and the elementary triplet counts, with no new general method. The determination is about the frozen narrow invariant under documented coverage, not about the utility of positional covariance as a statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
