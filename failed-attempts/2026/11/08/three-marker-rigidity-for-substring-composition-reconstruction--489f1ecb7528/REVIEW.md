# Independent mathematical audit

## correctness

PASS

For a word 0^a1 0^b1 0^c1 0^d, the length enumerators for two and three ones follow from independent choices of left and right extensions of a fixed consecutive marker span. Q0 second differences give positive gap multiplicities and the complement to four gives the zero-gap count. The first and last exponents in Q3 and its value at 1 give b+c, a+d and (a+1)(d+1), hence the unordered endpoint pair; multiset subtraction then gives the internal pair. After fixing endpoint orientation, swapping the internal pair changes Q2 by t²(t^(d+1)−t^(a+1))(t^b−t^c)/(1−t)², nonzero exactly when both pairs are unequal. The equal-pair cases coincide up to reversal. Palindromes have a central one and one occupied mirror pair, giving the stated reversal-orbit count. The named four-one words really collide and are not reversals. The three-channel recovery theorem is true, but equivalent to full-data recovery, since at each length the four counts sum to n−ℓ+1. Independent finite check via `python /workspace/reproductions/check_discrete_claims.py 5`: 3876 words of lengths 3 through 18, using even just Q2,Q3, checking the reversal-orbit counts and the actual quoted four-one pair. The frozen script tests its bitwise complement, which gives the same collision after relabeling, but not the literal witness. These finite checks are not the all-length proof.

## originality

FAIL

Earlier indexed work gives strictly stronger two-channel recovery for all finite weight-three words; the full-spectrum count follows immediately and the collision is published. Removing that redundancy or dropping Q0 as well leaves no distinct contribution of the claim under review.

## value

FAIL

The inverse problem is meaningful, but the claimed version discards a redundant count and is weaker than an existing all-length two-channel theorem. The orbit count is immediate from that theorem, and the four-one boundary witness is already published. No new mathematical information remains in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
