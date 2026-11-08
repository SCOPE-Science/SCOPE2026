# Exact minimum string attractors for dyadic prefixes of the powers-of-two indicator

## Finding
Let \(k\ge2\) be an integer, let \(P_k=p_0p_1\cdots p_{2^k-1}\) be the binary word defined by \(p_i=1\) if and only if \(i+1\) is a power of two, and let \(\gamma(P_k)\) be the minimum cardinality of a set of zero-based positions meeting an occurrence of every distinct nonempty **contiguous** factor of \(P_k\). Then
\[
\gamma(P_k)=\left\lfloor\frac{k+1}{2}\right\rfloor+1.
\]
In fact the following explicit positions form a minimum attractor:
\[
S_k=\{2^j-1:1\le j<k,\ j\text{ odd}\}\cup\{2^{k-1}-1,\,2^k-2\}.
\]
The statement determines exact *offline* minima at all dyadic prefix lengths, not an online greedy-attractor statistic.

## Assumptions and scope
All factors are contiguous, nonempty substrings; their occurrences are half-open intervals \([a,b)\) of zero-based positions, and one position must lie inside at least one occurrence of each distinct factor. The word has ones precisely at \(2^j-1\), \(0\le j\le k\), and between the ones at \(2^j-1\) and \(2^{j+1}-1\) there are exactly \(2^j-1\) zeros. Only the dyadic prefixes \(2^k\), \(k\ge2\), are claimed.

## Proof
**Upper bound.** The displayed \(S_k\) has \(\lfloor(k+1)/2\rfloor+1\) positions. All its elements are valid and it contains the penultimate one \(2^{k-1}-1\) and the last zero \(2^k-2\). For any factor containing at least two ones, every occurrence contains a full consecutive-one pair at positions \(2^j-1\) and \(2^{j+1}-1\), for some \(0\le j<k\). If \(j\) is odd, the first endpoint lies in \(S_k\); if \(j\) is even and \(j<k-1\), the second endpoint lies in \(S_k\); if \(j=k-1\) is even, the first endpoint is the specially included penultimate one. Hence this factor has an occurrence meeting \(S_k\). A factor consisting only of zeros occurs ending at the last zero \(2^k-2\), because the final gap of \(2^{k-1}-1\) zeros is the longest. A factor containing exactly one one is \(0^a10^b\). If \(b>0\), it occurs at the penultimate one: among the first \(k\) ones this has the greatest zero-run on each side, namely \(2^{k-2}-1\) before and \(2^{k-1}-1\) after, so it realizes any feasible \((a,b)\) with positive \(b\). The same is true for \(b=0\) and \(a\le2^{k-2}-1\). If \(b=0\) and \(a>2^{k-2}-1\), such a factor must end at the final one and necessarily contains the selected immediately preceding zero. Thus every factor is attracted by \(S_k\).

**Lower bound.** For each even \(j\) with \(0\le j\le k-2\), the factor \(10^{2^j-1}1\) occurs exactly once, on the interval \([2^j-1,2^{j+1})\). These intervals are mutually disjoint (the indices \(j\) differ by at least two). If \(k\) is even, additionally the factor \(0^{2^{k-2}}1\) occurs exactly once, ending at the final one on interval \([2^k-1-2^{k-2},2^k)\), which is disjoint from all those pair intervals. There are exactly \(k/2+1\) pairwise disjoint required intervals. If \(k\) is odd, retain the even-\(j\) pairs only for \(j\le k-3\), and add the two uniquely occurring factors \(0^{2^{k-3}}10\) (around the penultimate one, ending at \(2^{k-1}\)) and \(0^{2^{k-2}}1\) (ending at the final one). Their occurrence intervals and the preceding pair intervals are all mutually disjoint; the first of the two cannot occur earlier because earlier preceding zero runs are shorter or at the final one because it has no following zero. The final factor cannot occur before the final one because all preceding zero runs are shorter. We obtain \((k-1)/2+2\) pairwise disjoint obligatory intervals. Any attractor must select a separate position in each, giving the claimed lower bound in both parity cases.

## Verification
A standalone Python script `verify_power.py` generates each word independently, constructs every nonempty distinct contiguous factor, verifies an occurrence crosses the proposed upper witness, and checks that each proposed lower-bound factor has an occurrence-coverage set disjoint from all the others. Exhaustive comparisons passed for \(2\le k\le8\), containing respectively 8, 27, 93, 337, 1273, 4937, and 19433 distinct factors. The general theorem rests on the preceding proof, not on those finite tests.

## Relationship to prior work
Schaeffer and Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (first posted December 12, 2020), Theorem 8, treat exactly the same powers-of-two characteristic word and construct logarithmic-size attractors for ranges of prefix lengths; they expressly state that this provides only an upper bound, and that matching lower bounds require other techniques. The present theorem resolves the matching optimum for all dyadic prefixes \(2^k\) by the explicit disjoint-factor obstruction. General prefix-attractor growth and complexity results, including Cassaigne et al.'s *New string attractor-based complexities for infinite words* (2023 preprint), do not provide this exact dyadic optimum. A previously established greedy-attractor formula is for a different, online selection objective; it does not imply this offline minimum.

## Limitations
The result does not determine minima for non-dyadic prefix lengths, classify every minimum attractor, or imply a new general theorem for all automatic words. The originality assessment is literature-relative, not a proof of global novelty; independent scientific review has not been performed.

## References
- L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, initial version December 12, 2020, especially Theorem 8, pages 9–10, https://arxiv.org/abs/2012.06840.
- J. Cassaigne and coauthors, *New string attractor-based complexities for infinite words*, open author manuscript https://orbi.uliege.be/bitstream/2268/309672/1/String_attractors__journal_version_%20%282%29.pdf, Section 3.
