# Independent mathematical audit

## correctness

PASS

In a uniformly ordered list of labelled endpoint pairs, a particular set of k left labels and the complementary right labels admits 2(2k)!(2n-2-2k)! endpoint permutations with the tagged interval isolated. The two block orders are independent uniform orders conditional on the partition; without the partition the law is a mixture. Normalizing the weights by (2n-2)! gives the ratio (2k+1)/(2m-2k-1), m=n-1. The two next-to-extreme weights each equal 1/(2m-1), and the remaining nonextreme mass is O(m^-2) by a geometric bound through m/4 and monotonicity to m/2. This gives the split probability and the TV upper bound by retaining the exact G_m law on the one-sided event. Given the split, the mean edge deficit is (2/3)[m+K(m-K)]; under isolation the mean of K(m-K) equals m(m-1)C_n/p_n, by the two-side multinomial count conditional on the exterior gaps. This proves the covariance sign and normalization, including -4/9 for n=2. The same ratio estimate with the weight k(m-k) gives E[K(m-K)|I_1=1]→1/2: k=1,m-1 give the limit, k=2,m-2 give O(m^-1), and k≥3 up to the middle have total unweighted mass O(m^-3). Since n²p_n→1, this also yields n⁴C_n→1/2 and Cov(Z_n,E_n)→-2/3; Markov gives Z_n→0 in probability. Independently enumerated all (2n)!/2^n labelled endpoint-pair orders for n=2,…,5 and checked the split weights, conditional edge-count convolutions for fixed label sets, and covariance (-4/9,-2/3,-16/21,-748/945).

## originality

FAIL

There is a distinct indexed companion on component–edge covariance with the same model. Its displayed single-cut independent-uniform matching law and joint cut probabilities already mechanically yield the tagged-isolation block law and covariance by two adjacent cuts. This is a statement-level mathematical implication, not a numerical match of the limiting constants, an assertion that component count equals isolate count, or a claim about which same-day record appeared first. I find no separate substantive result beyond this specialization and its weight estimates in the frozen finding.

## value

PASS

The conditional labelled graph law is a natural structural description of deletion after a connectivity defect. The isolate count going to zero while its covariance with the growing edge count does not highlights a genuine distinction between total variation and unscaled moment control. That interpretation is useful independently of the originality failure for the mathematical specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
