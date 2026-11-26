# Independent mathematical audit

## correctness

PASS

The replacement claim is the exact almost-sure digit law for three independent fair ternary {0,1} streams added in Z₃. With incoming carry c=0,1 and raw multiplicities 1,3,3,1, the carry transition rows are (7,1)/8 and (4,4)/8; the conditional digit rows are (2,3,3)/8 and (3,2,3)/8. The stationary carry probabilities are (4/5,1/5). The Markov occupation-time theorem and the bounded martingale-difference law apply from carry zero, giving frequencies (11,14,15)/40, not just these expectations. The measurable event defined by this limit is Haar-null by the iid uniform Haar digit law. Conditioning on two inputs proves non-atomicity, and all prescribed finite prefixes can occur with positive probability and no carries, proving full support. I checked the revised proof and ran the replacement rational checker, which also compared digit marginals through eight positions to ordinary integer prefix histograms. There was no mathematical error in the removed energy statements: with a difference carry, the reduced transition matrix in row order 0 and |c|=1 is [[20,2],[15,6]]. A free terminal carry gives E₀=1,E₁=22 with characteristic polynomial x²−26x+90. Depth-k mass normalization uses 8^k ordered triples, so the collision mass is E_k/64^k and gives the stated dimension and χ² rate. A separate finite reproduction gave folded energies 1,22,482,10552 through k=3 and continued through k=7. This part was removed for coverage, not because of a correctness failure.

## originality

PASS

PASS is for the narrowed exact almost-sure frequency claim. The frozen claim's originality FAILS in material part: distinct indexed record a30ba852d85c supplies the exact carry transfer for the very same finite ordered input triples. The frozen modular energy is a direct terminal-sum evaluation of that matrix; the same root gives the same exponent. This is demonstrated coverage, not a priority order inferred from same-day dates. I removed the energy, dimension and χ²-rate claims, rather than retaining them with a priority disclaimer. The same inspected result's matrix compares two sums and does not encode a single sum's output digit frequencies. The strongest new comparison for the repaired claim, the real torus convolution of Fong–Hare–Johnstone, treats folded prefix masses and local dimensions of the real quotient, not this typical digit vector or equivalent numerical digit statistics in the available passages. Exact narrower Resultary search found the frozen self-match and a material but different X+2Y result, not coverage of the retained vector. This judgment is bounded to the comparisons below.

## value

PASS

The triple is the first convolution of these streams for which carry feeds back into the next digit; at two summands the raw sum never exceeds two. The revised claim gives the exact typical bias in this natural first case, rather than recomputing a known exponent or simply showing non-uniformity. The vector describes an explicit Haar-null set of full convolution mass even though every finite cylinder has positive mass. It is a quantitative description of how digit smoothing fails after carries first arise, and a benchmark for distinguishing this law from the already compared two-input convolution. The retained value is attached to the exact almost-sure statistic, not to the support or atomlessness observations separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
