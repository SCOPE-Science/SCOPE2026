# Independent mathematical audit

## correctness

PASS

The raw stationary moment is correct for every integer n >= 0 and 1/2 < p < 1. Following prefixes of a word shows that k is the number of original digits consumed and h the number of prefixed zeroes still present, so the exact word map is 2^(-h) D^k. Reflection counts paths ending at h-k staying above -k by subtracting binomial(n,u+k+1) from binomial(n,u); imposing an attained minimum gives binomial(n,u+k)-binomial(n,u+k+1). When k=0 or h=0 the stricter barrier has no paths, consistent with this difference by binomial symmetry. Independence gives the word weights. On dyadic cells J_j with j >= k, the fractional part is 2^k x and the conditional second moment gives 7*2^k/(3*4^(j+1)). For j < k, integrating x times the sawtooth over equally spaced subintervals gives 3/(4*2^(j+1))+1/(12*2^k). Summing the given stationary masses yields the claimed tails, including the arithmetico-geometric p=2/3 case, and R_0=4(2p-1)/(3(5p-1)). The frozen verify.py and VERIFICATION.md were inspected, not run; the described rational comparisons for n <= 5 are corroboration only.

## originality

FAIL

A distinct indexed Resultary record already provides the same exact stationary all-lag moment by the same path normal form and dyadic moment, and sums it in a generating function. Converting its walk expectation to the reflection-coefficient finite sum does not leave a distinct substantive claim. This is demonstrable equivalent coverage, not evidence that the later-dated catalogue record predates the supplied result or that the proof is incorrect.

## value

PASS

As a scientific result, the exact stationary physical-position correlation over all lags is a natural target left approximate in the motivating published calculation. The order-sensitive reduction from exponentially many words to the distribution of two walk statistics and the evaluated within-cell moment are useful for exact benchmarking and extracting coefficients; that intrinsic value does not make the result a distinct addition to the catalogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
