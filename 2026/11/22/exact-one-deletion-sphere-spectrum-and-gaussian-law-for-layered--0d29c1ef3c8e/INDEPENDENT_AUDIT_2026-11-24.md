# Independent mathematical audit

## correctness

PASS

Directly in the layer composition, deleting in a part larger than one decreases its size by one, giving distinct vectors of unchanged part count. Deleting a singleton gives one fewer part; deleting two different singleton positions yields the same vector exactly when all parts from one to the other are singletons. Thus the statistic counts long parts plus runs of singleton parts. The two-component sequence GF gives the stated rational function; normalization is by 2^(n-1). A j-component sequence needs length at least j+floor(j/2); the minimal alternating construction can absorb any surplus, and at the maximum the slack is at most one. Separating the zero-slack placements and the one-unit surpluses gives the three residue counts, including n=1,2. Independent fair cuts give summands X_i(1-X_{i-1}X_{i+1}); summing the boundary and interior covariances gives 7(n-1)/64 for n>=5, with the small cases checked separately. Two gaps between retained blocks of size floor(n^(1/3)) make the block sums independent; the removed centered sum has variance o(n) by two-dependence, so the retained variance is asymptotic to 7n/64. The uniform block bound is o(sqrt(n)), giving Lindeberg and the claimed CLT.

## originality

PASS

Credit the general deletion-bond identity and the established layered class. The supported distinct claim is the conditional exact law, sharp extremal counts and associated moments and normal limit in Av(231,312), not the general identity or the PID channel. Neither the unrestricted theorem nor the closest same-channel indexed records supplies that specialization.

## value

PASS

An all-length law for a natural hereditary source measures the spread of ambiguity after rank-order deletion, not merely the size of the language. It separates the typical layered volume near 3n/8 from nearly n for the unrestricted source, quantifies fluctuations and gives exact finite-block frequencies and extreme multiplicities. The result is useful even though it does not solve a code-packing problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
