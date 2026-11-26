# Independent mathematical audit

## correctness

PASS

The canonical word begins in 0, ends in 1, and has n−2 free bits. A one-run is a closed-twin class, with the initial singleton zero joining the first class exactly when a₁=1. Earlier zero vertices distinguish this first condition and later one-runs; zero vertices themselves are pairwise nonadjacent. For n≥3, a one-symbol vertex has degree at least two, and a zero-symbol vertex is a leaf exactly if the only 1 after it is the last symbol. All leaves then share that last vertex. Thus s is the maximum of b₁−1+1_{a₁=1} and the later b_j−1, while t is a_q for b_q=1 and zero otherwise. Splitting into first, interior and final pairs gives A_S, B_S, C_{S,T}. The single-pair words of length at least three split into a=1,b≥2; a≥2,b≥2; and a≥2,b=1, giving the three terms of E_{S,T}. All choices are disjoint, giving the formal power series in the finding, including S or T zero. Zero siblings require a 00 prefix and no adjacent ones; the strings ending in 1 give F_{n−2}. Zero tuft means a final 11 and gives 2^(n−3); the latter is strictly larger for n≥4. For 1≤k≤n−2 the tuft tail is P(t≥k)=2^(−k) from the last k free bits, with extra endpoint P(t≥n−1)=2^(−(n−2)); summing tails and weighted tails gives E[t]=1 and Var(t)=2−2^(3−n). The sibling statistic differs from the longest run of ones by at most one. A union bound and independent disjoint internal blocks prove the log₂ n scale; a half-log cutoff separates the tight tuft marginal from the diverging sibling marginal, giving TV→1. Independent bounded calculations confirmed the graph statistics, generating coefficients and moments.

## originality

FAIL

A distinct indexed exact statement gives the entire rational bounded joint census on the same graphs and parameters and the exact zero-class discrepancy with first failure at n=4. Coefficients and discrete differences of a complete bounded census already determine the finite law and hence its marginals and moments. The asymptotic paragraph is not explicitly stated in the matched summary; it is a direct application of the standard longest-fair-bit-run scale to s (bounded error one), and the elementary endpoint run law to t. In particular the claimed TV separation needs only that a fixed length of ones eventually occurs with probability tending to one and the exact geometric tail bound for the terminal zeros. There is no distinct census or nonroutine limiting law left that would support the submitted package. This is a statement of mathematical coverage and routine consequence, not a determination of publication order or full-text duplication.

## value

FAIL

An exact census for this natural counterclass would be useful if it supplied an unknown distribution. The distinct indexed result already gives the full census and exact discrepancy. The remaining putative contribution follows from the standard longest-run calculation and a one-sided geometric tail, with the TV limit already following by fixed cutoffs; it does not require a new threshold-specific structural theorem or establish a refined limiting distribution beyond those run facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
