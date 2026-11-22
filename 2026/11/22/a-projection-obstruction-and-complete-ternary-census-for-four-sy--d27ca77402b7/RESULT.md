# A projection obstruction and complete ternary census for four-symbol comma-free substitution-correcting codes

## Finding
Let \(q\ge2\) be an integer, let \(\Sigma\) be a labeled alphabet of size \(q\), and let \(C\subseteq\Sigma^4\) be a comma-free code with pairwise Hamming distance at least \(3\). Then
\[
|C|\le \left\lfloor\frac{2q^2}{3}\right\rfloor.
\]
For \(q=3\), the exact maximum is \(5\), and there are precisely \(1548\) labeled maximum-size codes. Under simultaneous permutation of the three symbols and reversal of all codewords, the \(1548\) codes form precisely \(129\) equivalence classes, all of cardinality \(12\). One maximum code is
`0001 0110 0222 1121 2012`.

## Assumptions and scope
A code here is a **set** of length-four indexed words over a finite labeled alphabet; there is no restriction on symbol composition. Hamming distance at least \(3\) means that any distinct codewords differ in at least three of the four coordinates. For all \(x,y\in C\), possibly equal, and each \(i\in\{1,2,3\}\), the four-symbol factor
\[
\operatorname{splice}_i(x,y)=x_{i+1}\cdots x_4y_1\cdots y_i
\]
must not belong to \(C\). This is the ordinary comma-free condition, **not** the stronger cross-bifix-free/non-overlapping condition. Every distinct pair of codewords can correct one substitution at an already known block boundary. Comma-freeness provides exact-frame recognition in an error-free concatenation; no claim of one-error correction at an unknown frame is made.

## Proof
**All-alphabet projection bound.** Put \(m=|C|\). Let \(P\subseteq\Sigma^2\) and \(S\subseteq\Sigma^2\) be the sets of initial and terminal two-symbol blocks of codewords. Since any two codewords sharing either initial or terminal two coordinates have Hamming distance at most two, the two projections are both injective; hence \(|P|=|S|=m\).

Let \(T=P\cap S\), with \(r=|T|\). Inclusion-exclusion in \(\Sigma^2\) yields \(r\ge 2m-q^2\). Exactly \(r\) codewords have their initial two-symbol block in \(T\), and exactly \(r\) codewords have their terminal two-symbol block in \(T\). These two subfamilies are disjoint. Otherwise a word \(z\in C\) would have \(z_1z_2\in S\) and \(z_3z_4\in P\). There would be codewords \(x,y\in C\) with \(x_3x_4=z_1z_2\) and \(y_1y_2=z_3z_4\); then \(\operatorname{splice}_2(x,y)=z\), contradicting comma-freeness. Consequently \(2r\le m\). Combining the two inequalities gives \(2(2m-q^2)\le m\), so \(3m\le2q^2\), and integrality proves the bound. The argument also works if \(P\cap S\) is empty.

**Sharp finite ternary result.** The finite exhaustive certificate `scripts/verify_census.py` enumerates the \(3^4=81\) possible four-symbol words, removes every word which is a nontrivial rotation of itself (exactly nine), and considers every subset of the remaining \(72\) words compatible with pairwise distance at least \(3\). An increasing-index recursion generates a possible codeword only after its distance compatibility with all existing codewords is verified. At each recursion node it tests the full comma-free condition against all ordered pairs of present codewords and all three frame shifts, including repeated words. Since Hamming compatibility and comma-freeness are hereditary under taking subsets, no valid code can be excluded by the pruning. Conversely every listed node satisfies both conditions, and the increasing-index rule lists each unordered code exactly once.

The exactly reproduced counts by nonempty code size \(1,2,3,4,5\) are \(72,1410,7398,9042,1548\), and the recursion has no valid node of size at least six. The explicitly displayed five-word code passes the same full tests, hence the maximum is exactly five. The program next forms the group action from all \(3!=6\) global alphabet relabelings and word reversal, computes the orbit of every optimal codebook, and verifies that there are exactly \(129\) orbits, each of size \(12\). A separately implemented standard C++17 verifier `scripts/verify_census.cpp` independently constructs and tests codebooks and computes the same orbit count, with identical size histogram. The two implementations do not share generated search data.

## Verification
From the directory containing the two scripts, run `python3 scripts/verify_census.py`. Optionally run `g++ -O2 -std=c++17 scripts/verify_census.cpp -o /tmp/cf4_verify && /tmp/cf4_verify`. Both checks complete without specialized libraries. Expected certificate values are \(72\) primitive candidates, \(1530\) compatible Hamming-distance-three pairs, \(1548\) size-five maxima, and \(129\) size-twelve symmetry classes. The infinite-\(q\) bound is a direct projection argument, not an extrapolation from these finite computations.

## Relationship to prior work
Golomb, Gordon and Welch (1958) establish the ordinary comma-free model and primitive-rotation bound; they report \(W_4(3)=18\) **without** any Hamming-distance restriction. Their theorem for length-two comma-free codes classifies a different object; the projection argument above uses a related initial/terminal-block partition but imposes simultaneous Hamming injectivity. Blackburn (first public arXiv version 2013) studies cross-bifix-free codes, a more restrictive class in which prefix/suffix collisions themselves are forbidden, and gives exact unrestricted optima for block lengths at most three. Yang and Ding (2025 publicized, 2026 journal) study bounded prefix-suffix overlaps, also a different restriction. Neither their stronger-class bounds nor the unrestricted classical rotation bound imply this exact distance-three ternary census. Existing classifications of three-symbol comma-free Hamming-distance codes have different block length. Potential equivalences in older coding classifications remain an originality risk.

## Limitations
The all-alphabet bound is an upper bound, not claimed to be attained for alphabets other than the investigated ternary example. The exhaustive census is restricted to a labeled three-symbol alphabet, length four, and Hamming distance at least three; it does not prove a general formula for the count of optimal codes at larger alphabet sizes or lengths. Although a direct finite exhaustive certificate is reproducible, there has been no independent external mathematical audit. No claim of novelty is made for the classical unrestricted comma-free length-four optimum, the Singleton bound, or the general cross-bifix-free theory.

## References
- S. W. Golomb, B. Gordon, and L. R. Welch, *Comma-Free Codes*, Canadian Journal of Mathematics **10** (1958), 202–209, https://doi.org/10.4153/CJM-1958-023-9 ; open PDF https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B78C35132E2BCD4A14459BE6A142FF30/S0008414X00045296a.pdf/comma-free-codes.pdf
- S. R. Blackburn, *Non-overlapping codes*, first public arXiv version March 5, 2013, arXiv:1303.1026, https://arxiv.org/html/1303.1026v3
- H. Yang and Y. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, IEICE Transactions on Fundamentals, publicized September 22, 2025; DOI:10.1587/transfun.2025EAL2050, https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.2025EAL2050/_f
