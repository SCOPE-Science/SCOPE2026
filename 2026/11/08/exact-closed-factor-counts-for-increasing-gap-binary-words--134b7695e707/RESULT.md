# Exact closed-factor counts for increasing-gap binary words

## Finding

For every integer \(k\ge1\) and every strictly increasing vector of positive integers \(1\le g_1<g_2<\cdots<g_k\), put \(g_0=0\) and define the finite binary word
\[
W(g_1,\ldots,g_k)=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_k}1.
\]
Let \(C^+(W)\) be the number of **distinct nonempty closed contiguous factors** of \(W\). A nonempty word is *closed* if it is a single letter, or if some nonempty proper factor occurs exactly twice in it, once as a prefix and once as a suffix (overlap is allowed).

The complete closed-factor language of \(W\) is the disjoint union of these four classes:

1. \(0^r\), for \(1\le r\le g_k\);
2. \(0^a1\,0^a\), for \(0\le a\le g_{k-1}\) (including the single letter \(1\));
3. \(0^a1\,0^{g_j}1\,0^b\), for \(1\le j<k\), \(0\le a\le g_{j-1}\), and \(0\le b\le g_j\);
4. \(0^a1\,0^{g_k}1\), for \(0\le a\le g_{k-1}\).

In particular, the exact count is
\[
\boxed{\displaystyle C^+(W)=g_k+2(g_{k-1}+1)+\sum_{j=1}^{k-1}(g_{j-1}+1)(g_j+1).}
\]
The sum is empty for \(k=1\).

The formula yields distinct asymptotic regimes within this single natural word family. With \(g_j=j\), the length is \(n_k=(k+1)(k+2)/2\) and
\[
C^+(W)=\frac{k^3+8k}{3}\sim\frac{2\sqrt2}{3}\,n_k^{3/2}.
\]
For any fixed real \(\alpha\ge1\), the choice \(g_j=\lceil j^\alpha\rceil\) produces
\[
C^+(W)\sim \frac{(\alpha+1)^{(2\alpha+1)/(\alpha+1)}}{2\alpha+1}\,n_k^{(2\alpha+1)/(\alpha+1)},
\]
realizing every exponent in \([3/2,2)\). For every fixed integer \(b\ge2\), the geometric gaps \(g_j=b^{j-1}\) give
\[
\lim_{k\to\infty}\frac{C^+(W)}{n_k^2}=\frac{b-1}{b^3(b+1)}>0.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); only nonempty *distinct* contiguous factors are counted. Gaps are arbitrary strictly increasing positive integers; the theorem makes no claim for repeated gaps, nonmonotone gaps, or other alphabets. Counts include the one-letter closed words but exclude the empty word. The asymptotic corollaries concern the displayed gap schedules as \(k\to\infty\), not uniform asymptotics over all gap vectors.

## Proof

**Uniqueness of two-marker factors.** Any factor containing at least two ones contains a complete zero gap between two consecutive ones. In \(W\) these full gaps have pairwise distinct lengths \(g_j\). Hence any specified factor containing at least two ones occurs at most once in \(W\): a repeated occurrence would repeat one of its full intervening gaps. In particular such a factor cannot itself occur both as the prefix and suffix of a longer word.

**No closed factors with three or more ones.** Suppose \(F\) contains at least three ones and is closed, with a nonempty proper factor \(u\) occurring exactly at the two ends. If \(u\) contains at least two ones, the preceding uniqueness observation precludes two occurrences. If \(u\) contains no one, then \(u=0^a\) for some \(a\ge1\). Its prefix occurrence fits in a zero run *before* the first one of \(F\), while the full zero gap after that first one is strictly longer, providing an internal occurrence of \(u\). Finally suppose \(u=0^a1\,0^b\) contains exactly one one, with \(a,b\ge0\). Its prefix occurrence is centered at the first one of \(F\), and its suffix occurrence at the last. For every intermediate one of \(F\), the preceding full gap is at least \(a\) and the following full gap is at least \(b\): this follows from monotonicity of the gaps and the fact that the prefix occurrence already has \(a\) zeros before and \(b\) zeros after its marker. Thus \(u\) occurs internally, again a contradiction. So any closed factor has at most two ones.

**Zero and one marker.** The all-zero factors are precisely \(0^r\), \(1\le r\le g_k\); every one is closed. A factor with exactly one one has shape \(0^a1\,0^b\). For \(a=b\), it is a complete return to \(0^a\) when \(a\ge1\), or is the single letter \(1\) when \(a=0\). When \(a\ne b\), no border containing a one is possible and any nonempty all-zero border appears internally within the longer of the two end runs. Thus it is open. Such a factor exists exactly for \(0\le a\le g_{k-1}\), because the longest available pair of zero runs surrounding a marker is \((g_{k-1},g_k)\). This proves classes 1 and 2.

**Two markers.** Every factor with exactly two ones uniquely has shape \(F=0^a1\,0^{g_j}1\,0^b\) for some \(1\le j\le k\). The available left context gives \(0\le a\le g_{j-1}\); the available right context gives \(0\le b\le g_{j+1}\) when \(j<k\), while \(b=0\) when \(j=k\). Since \(a\le g_{j-1}<g_j\), any nonempty zero-only border occurs internally inside the middle run \(0^{g_j}\). A border containing one one exists precisely when \(b\le g_j\), in which case \(0^a1\,0^b\) occurs exactly at the two marker positions of \(F\), and \(F\) is closed. For \(j<k\), the inequalities \(g_{j+1}>g_j\) leave exactly \((g_{j-1}+1)(g_j+1)\) allowed pairs \((a,b)\). For \(j=k\) there are exactly \(g_{k-1}+1\) choices. These factors are all distinct: the full central gap determines \(j\), then the two end-zero lengths determine \(a,b\). This proves classes 3 and 4 and the claimed sum.

**Asymptotics.** The ramp sum is \(\sum_{j=1}^{k-1}j(j+1)=k(k-1)(k+1)/3\). For \(g_j=\lceil j^\alpha\rceil\), \(n_k\sim k^{\alpha+1}/(\alpha+1)\) and the product sum is asymptotic to \(k^{2\alpha+1}/(2\alpha+1)\); the other terms are lower order. For geometric gaps, \(n_k\sim b^k/(b-1)\) while the product sum is asymptotic to \(b^{2k-3}/(b^2-1)\), yielding the displayed positive quadratic-density constant. All assertions follow.

## Verification

Run the bundled standard-library script `verify.py` with `python3 verify.py`. It independently constructs the distinct-factor set of each word, tests each factor by explicitly enumerating border occurrences, and compares the result against the four-class construction and the count formula. All \(4095\) vectors with \(1\le k\le6\) and entries chosen increasingly from \(\{1,\ldots,13\}\) passed (\(797251\) closed-factor instances across those cases). The ramp polynomial was also checked for \(1\le k\le15\). These tests are finite corroboration; the proof above establishes the quantifiers for unbounded integers.

## Relationship to prior work

Badkobeh, Fici and Lipták established general lower bounds and quadratic-order examples for distinct closed factors, as well as extremal-poor characterizations. Parshina and Zamboni computed per-length closed complexity for uniformly recurrent Arnoux–Rauzy words. Parshina and Postic studied periodicity through open and closed complexity; Parshina and Puzynina later determined the sharp asymptotic maximal \(n^2/6\) closed-factor count and rich-word classes. None of those inspected statements gives this complete language or its exact gap-dependent count. Here the markers have strictly increasing separations and the associated infinite word is not uniformly recurrent, so the Arnoux–Rauzy formulas do not apply. The result evaluates a different restricted family, not a new global upper bound.

## Limitations

No classification is asserted for arbitrary gap permutations, equal gaps, or arbitrary binary words. The comparison with the literature is based on inspected open-access versions and searches and cannot exclude an unindexed equivalent. Although the proof is elementary, the asserted mathematical contribution is the complete multivariate classification and the family of distinct scaling regimes, not a claim to solve the global extremal closed-rich problem. No independent scientific audit has been performed.

## References

- G. Badkobeh, G. Fici, Z. Lipták, *On the Number of Closed Factors in a Word*, first public arXiv version 2013-05-28, arXiv:1305.6395, https://arxiv.org/abs/1305.6395.
- O. Parshina, L. Q. Zamboni, *Open and closed factors of Arnoux–Rauzy words*, first public arXiv version 2018-10-12, arXiv:1810.05472, https://arxiv.org/abs/1810.05472.
- O. Parshina, M. Postic, *Open and closed complexity of infinite words*, first public arXiv version 2020-05-13, arXiv:2005.06254, https://arxiv.org/abs/2005.06254.
- O. Parshina, S. Puzynina, *Finite and infinite closed-rich words*, first public arXiv version 2021-11-01, arXiv:2111.00863, https://arxiv.org/abs/2111.00863.
