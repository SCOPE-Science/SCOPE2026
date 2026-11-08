# Exact minimum string attractors of increasing-gap binary words

## Finding

For every integer \(k\ge1\) and every strictly increasing tuple of positive integers \(1\le g_1<g_2<\cdots<g_k\), form
\[
W=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_k}1.
\]
Let \(\gamma(W)\) be the minimum number of positions sufficient to intersect an occurrence of every distinct nonempty **contiguous** factor of \(W\). Then
\[
\boxed{\gamma(W)=\left\lceil\frac{k}{2}\right\rceil+1.}
\]
Thus the optimum depends only on the number of strictly increasing gaps, not on their magnitudes. A set attaining this minimum is given below.

## Assumptions and scope

Work over the fixed alphabet \(\{0,1\}\). Positions are indexed from zero. For a position set \(\Gamma\subseteq\{0,\ldots,|W|-1\}\), the factor \(f\) is attracted when some occurrence \(W[a\ldots b]=f\), with \(a\le b\), contains an index of \(\Gamma\). The definition requires an occurrence, not every occurrence, to be intersected. Empty factors are excluded.

Let \(m_0=0\) and \(m_j=\sum_{i=1}^{j}(g_i+1)\), for \(1\le j\le k\). These are exactly the one-symbol positions; the zero gap of length \(g_j\) lies strictly between \(m_{j-1}\) and \(m_j\). Set
\[
Q=\{m_j:1\le j\le k,\ j\text{ odd}\}.
\]
Define
\[
\Gamma=\begin{cases}
Q\cup\{m_{k-1}+1\},&k\text{ odd},\\
Q\cup\{m_k-1\},&k\text{ even}.
\end{cases}
\]
Each added position is a zero in the final gap, and \(|\Gamma|=\lceil k/2\rceil+1\).

## Proof

**Upper bound.** We show that every distinct nonempty factor of \(W\) has an occurrence touching \(\Gamma\).

A factor with at least two ones has an occurrence containing two consecutive ones at indices \(m_{j-1},m_j\) for some \(1\le j\le k\). Exactly one of the consecutive marker indices \(j-1,j\) is odd, so one of those two positions belongs to \(Q\). In particular this same occurrence is already attracted.

Any factor with no ones is \(0^a\), where \(1\le a\le g_k\). It has an occurrence touching the selected zero of the last gap: for odd \(k\), use the first \(a\) zeros of the final run; for even \(k\), use its last \(a\) zeros.

Now consider a factor containing exactly one one, written \(0^a1\,0^b\) for integers \(a,b\ge0\). If \(b\ge1\), that factor has an occurrence centered at \(m_{k-1}\): indeed any occurrence centered at an earlier marker has at most \(g_{k-1}\) zeros to its left and at most \(g_k\) to its right, and these bounds are simultaneously available at \(m_{k-1}\). If \(k\) is even, \(m_{k-1}\in Q\), and the factor is attracted. If \(k\) is odd, choose the occurrence using the first \(b\) zeros after \(m_{k-1}\); it touches \(m_{k-1}+1\in\Gamma\).

If \(b=0\), the factor \(0^a1\) occurs at the final marker \(m_k\). For odd \(k\), that marker lies in \(Q\). For even \(k\), if \(a\le g_{k-1}\) it also occurs at \(m_{k-1}\in Q\); if \(a>g_{k-1}\), its suffix occurrence ending at \(m_k\) crosses the final zero \(m_k-1\in\Gamma\). This exhausts all factors and proves \(\gamma(W)\le\lceil k/2\rceil+1\).

**Lower bound, even \(k\).** Suppose \(k=2r\), where \(r\ge1\). For each \(j\in\{1,3,5,\ldots,2r-1\}\), the factor \(1\,0^{g_j}1\) occurs exactly once, in the interval \([m_{j-1},m_j]\): every pair of consecutive ones has a different zero-gap length. These \(r\) occurrence intervals are pairwise disjoint. The factor \(0^{g_k}\) occurs only in the last zero gap \([m_{k-1}+1,m_k-1]\), disjoint from all those intervals. Any attractor consequently contains at least \(r+1=\lceil k/2\rceil+1\) positions.

**Lower bound, odd \(k\).** For \(k=1\), both symbols occur and each needs a selected position, giving \(\gamma(W)\ge2\). Now let \(k=2r+1\ge3\). The factor \(0^{g_k}\) forces one selected position \(z\) strictly inside the final zero gap. For each \(j=1,\ldots,2r\), the uniquely occurring factor \(1\,0^{g_j}1\) forces a selected position in \(I_j=[m_{j-1},m_j]\). These intervals form a chain: consecutive intervals share exactly their endpoint, and nonconsecutive intervals are disjoint. No position in the final zero gap belongs to any \(I_j\). A position can meet at most two of the \(2r\) intervals, and meeting two requires the shared endpoint. Thus if only \(r+1\) positions were selected in total, the other \(r\) must be exactly \(m_1,m_3,\ldots,m_{2r-1}=m_{k-2}\), the unique perfect pairing of the intervals.

The factor \(0^{g_{k-1}}1\,0\) has exactly one occurrence: the last \(g_{k-1}\) zeros of the penultimate gap, followed by the marker \(m_{k-1}\) and the first zero of the last gap. It contains none of those \(r\) odd-indexed markers, so attracting it forces \(z=m_{k-1}+1\). But the factor \(0^{g_{k-1}}1\) occurs only ending at \(m_{k-1}\) or \(m_k\). The first occurrence ends before \(z\), while the second uses the last \(g_{k-1}\) zeros of the final gap; because \(g_k>g_{k-1}\), it starts strictly after \(z=m_{k-1}+1\). Neither occurrence touches any of the other selected markers. Contradiction. Hence at least \(r+2=\lceil k/2\rceil+1\) positions are required.

The upper and lower bounds agree for every permitted tuple.

## Verification

The standalone Python 3 program `verify_attractors.py` is self-contained and uses no external packages. It directly reconstructs every distinct substring and its covered occurrences. Its checked output is: 465 exhaustive increasing-gap tuples with all gaps at most nine and at most six gaps (118,977 distinct-factor cells counted across instances); 11 independently exhaustive finite minimum-hitting-set instances; and 19 additional larger-parameter explicit-cover checks. All passed. These finite tests verify implementations and boundaries but are not substituted for the proof above.

To reproduce, run `python3 verify_attractors.py` from the directory containing that file. The script explicitly asserts the formula and the specified attractor on every checked instance.

## Relationship to prior work

The definition comes from Prezza's *String Attractors* (2017). Mantaci, Restivo, Romana, Rosone and Sciortino (2019 preprint, later 2021 journal article) give general concatenation and power bounds, and exact results for standard Sturmian, Thue--Morse, and de Bruijn families, not the increasing-gap sequence of unique marker separations here. Schaeffer and Shallit (2020 preprint, revised 2024) compute profiles for automatic sequences and obtain logarithmic or bounded behavior in that category. This binary increasing-gap family is different: for the canonical choice \(g_j=j\),
\[
|W|=1+\frac{k(k+3)}{2},\qquad
\gamma(W)=\left\lceil\frac{k}{2}\right\rceil+1\sim\sqrt{|W|/2}.
\]
Béaur, Gheeraert and Hellouin de Menibus (2024) address attractors of bi-infinite words, not the finite sharp calculation here. Cassaigne and coauthors (2024) study attractor profile complexities of morphic and other infinite words, but their inspected principal results do not supply this all-gap-vector exact value. No claim of universal uniqueness among all possible publications is made.

## Limitations

Strict growth \(g_1<\cdots<g_k\), positivity, two symbols, and the specified leading and trailing marker are essential stated assumptions. The theorem does not determine optimal attractor **multiplicities**, does not address arbitrary permutations of distinct gaps, and does not give the attractor-profile function for every intermediate prefix of the infinite increasing-gap word. Small finite enumerations are only consistency checks. The bibliographic search cannot exclude every unindexed equivalent, and no independent scientific audit has been performed.

## References

- N. Prezza, *String Attractors*, arXiv:1709.05314, first version 2017-09-15. https://arxiv.org/abs/1709.05314
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, first version 2019-07-10; subsequent journal version *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248. https://arxiv.org/abs/1907.04660
- L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, first version 2020-12-12. https://arxiv.org/abs/2012.06840
- P. Béaur, F. Gheeraert, B. Hellouin de Menibus, *String attractors and bi-infinite words*, arXiv:2403.13449, first version 2024-03-20. https://arxiv.org/abs/2403.13449
- J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino, M. Stipulanti, *New string attractor-based complexities for infinite words*, Journal of Combinatorial Theory A 208 (2024), 105936. https://doi.org/10.1016/j.jcta.2024.105936
