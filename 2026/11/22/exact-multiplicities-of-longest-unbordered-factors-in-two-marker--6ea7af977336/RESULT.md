# Exact multiplicities of longest unbordered factors in two-marker binary words

## Finding

A *border* of a nonempty word is a nonempty proper prefix that is also a suffix. An *unbordered factor* is a contiguous factor with no border. Let \(L(W)\) denote the greatest length of an unbordered factor of \(W\), and let \(Q(W)\) be the **number of occurrence intervals** having this length and being unbordered (not the number of distinct factor strings).

For every integer \(n\ge 2\), every binary length-\(n\) word with exactly two ones is uniquely
\[
W=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\qquad a+b+c=n-2.
\]
Write \(m=\max(a,c)\). Its complete maximum-length and multiplicity classification is
\[
(L(W),Q(W))=
\begin{cases}
(b+m+2,\;\mathbf1_{\{a=m\}}+\mathbf1_{\{c=m\}}),&m>b,\\
(b+1,\;2+\mathbf1_{\{a=b\}}+\mathbf1_{\{c=b\}}),&m\le b,\ b>0,\\
(1,2),&(a,b,c)=(0,0,0).
\end{cases}
\]
Thus \(Q\) takes only values \(1,2,3,4\); four maximizing occurrences arise precisely for \(a=b=c\ge1\), giving exactly one such word at each length \(n\ge5\) congruent to \(2\pmod3\).

Let \(C_q(n)\) count these weight-two words with \(Q(W)=q\), and let
\[
A(z)=\frac{z^3(1+z^2)}{(1-z)(1-z^2)(1-z^3)},\quad
B(z)=\frac{z^4}{(1-z^2)(1-z^3)},\quad
D(z)=\frac{z^5}{1-z^3}.
\]
The **complete all-length multiplicity enumerator** is
\[
\sum_{n\ge2}\sum_{q=1}^4 C_q(n)z^n v^q
=2vA(z)+v^2\big(A(z)+B(z)+z^2\big)+2v^3B(z)+v^4D(z).
\]
Equivalently, put
\[
B_n=\left\lfloor\frac{n-2}{2}\right\rfloor-\left\lfloor\frac{n-2}{3}\right\rfloor,\quad
D_n=\mathbf1_{\{n\ge5,\ n\equiv2\pmod3\}},\quad E_n=\mathbf1_{\{n=2\}},
\]
\[
A_n=\frac{\binom n2-3B_n-D_n-E_n}{3}.
\]
Then the four multiplicities are exactly
\[
(C_1(n),C_2(n),C_3(n),C_4(n))=(2A_n,\;A_n+B_n+E_n,\;2B_n,\;D_n).
\]

There is also a *joint* sparse-source limit law. Choose \(W_n\) uniformly among the \(\binom n2\) weight-two words. Let \(Y_n=L(W_n)/n\) and \(Q_n=Q(W_n)\). For \(0\le t\le1\), writing \(x_+=\max(x,0)\),
\[
\lim_{n\to\infty}\Pr(Y_n\le t,Q_n=2)
=\frac13\sum_{j=0}^3(-1)^j\binom3j(1-jt)_+^2,
\]
\[
\lim_{n\to\infty}\Pr(Y_n\le t,Q_n=1)
=(2t-1)_+^2-\frac13(3t-2)_+^2.
\]
The limiting probabilities of \(Q_n=3\) and \(Q_n=4\) are zero. In particular, \(\Pr(Q_n=1)\to2/3\), \(\Pr(Q_n=2)\to1/3\), and \(\mathbb E Q_n\to4/3\). The conditional mean normalized lengths converge to \(29/36\) and \(11/18\) for multiplicities one and two respectively. The marginal limiting mean \(20/27\) is included for comparison but is **not claimed to be new independently** of the known weight-two longest-border distribution.

## Assumptions and scope

Only finite ordinary binary strings of Hamming weight exactly two are treated; outer or inner zero gaps may vanish. Occurrences are indexed contiguous intervals, so identical factor strings at different positions count separately. Limits are taken with a uniformly random two-element subset of positions in \(\{1,\ldots,n\}\). The finite enumeration is valid at every integer \(n\ge2\), without asymptotic qualification. The two-variable series is a formal power series, not a statement about numerical convergence.

## Proof

**Step 1: classify all eligible maximizing intervals.** Every unbordered factor with zero ones has length one. A factor with precisely one one has form \(0^u1\,0^v\), and is unbordered precisely when \(u=0\) or \(v=0\), as otherwise the first and last zeros form a border. The largest one-marker unbordered factors have lengths at most \(1+\max(a,b,c)\).

A factor containing both ones has form \(0^u1\,0^b1\,0^v\), with \(0\le u\le a\) and \(0\le v\le c\). If both \(u,v>0\), it has a one-letter zero border. If both vanish, it has a one-letter one border. In the remaining case \(v=0\), the only potential proper prefix ending in a one is \(0^u1\); it is also a suffix precisely when \(u\le b\). Consequently \(0^u1\,0^b1\) is unbordered iff \(u>b\). Symmetrically, \(1\,0^b1\,0^v\) is unbordered iff \(v>b\). The maximum candidate is therefore \(b+m+2\) when \(m>b\), which strictly exceeds every one-marker candidate; its interval occurs once for each outer zero run of length \(m\).

When \(m\le b\), there are no unbordered two-marker factors, and the maximum is \(b+1\). For \(b>0\), the intervals \(1\,0^b\) and \(0^b1\) around the central gap always occur, with one extra interval immediately before the first one if \(a=b\) and one after the second one if \(c=b\). In the degenerate word \(11\), exactly its two singleton intervals maximize. This proves the stated \((L,Q)\) classification with all boundary cases.

**Comparison with least period.** A proper border of the full word either contains no ones, and then has length at most \(\min(a,c)\), or contains exactly one one. In the latter case its length is forced to be \(a+c+1\) and its two occurrences fit precisely when \(a,c\le b\). No proper border can contain both ones. Thus the longest proper border has length \(a+c+1\) when \(m\le b\) and \(\min(a,c)\) otherwise. Subtracting from \(n\) shows \(L(W)=\pi(W)\), its least period. This observation explains why the already known longest-border length spectrum also covers the marginal length distribution; it does not specify the number or locations of maximizing unbordered occurrences.

**Step 2: complete finite census.** In the regime \(m\le b\), \(b>0\), if both outer gaps are below \(b\) there are two maximizing intervals. These words have generating series
\[
A(z)=\sum_{b\ge1}z^{b+2}\left(\sum_{r=0}^{b-1}z^r\right)^2
=\frac{z^3(1+z^2)}{(1-z)(1-z^2)(1-z^3)}.
\]
Exactly one outer gap equal to \(b\) gives three maximizing intervals and generating series \(2B(z)\), where
\[
B(z)=\sum_{b\ge1}z^{2b+2}\sum_{r=0}^{b-1}z^r
=\frac{z^4}{(1-z^2)(1-z^3)}.
\]
Both outer gaps equal to \(b\) give four occurrences and series \(D(z)=\sum_{b\ge1}z^{3b+2}\).

In the regime \(m>b\), equal outer gaps \(a=c=m\) give two maximizing intervals; their series is again \(B(z)\), with \(m\) replacing the previous parameter \(b\). Unequal outer gaps yield one maximizing interval: choose the side attaining \(m\) in two ways, choose \(0\le b<m\), and the opposite outer gap \(0\le r<m\). Its series is \(2A(z)\), with \(m\) replacing the previous \(b\). Finally \(11\) contributes \(z^2v^2\). Adding the six disjoint classes proves the complete enumerator and shows that their total is \(z^2/(1-z)^3\), as required for the \(\binom n2\) possible words.

The coefficient of \(z^n\) in \(B(z)\) counts integers \(m\) with \(0\le n-2-2m<m\), hence equals \(B_n\). The coefficient of \(D(z)\) equals \(D_n\). Since the four classes partition \(\binom n2\) words, \(3A_n+3B_n+D_n+E_n=\binom n2\), which proves the stated explicit closed counts.

**Step 3: joint limit.** The scaled weak gap compositions \((a,b,c)/n\) converge in distribution to the uniform distribution \((X,Y,Z)\) on the two-dimensional simplex \(X+Y+Z=1\). Away from zero-area equality planes, the maximizing occurrence count is two exactly when \(Y>\max(X,Z)\), and one otherwise; the limiting normalized maximum is \(Y\) on that event and \(Y+\max(X,Z)=1-\min(X,Z)\) on its complement. By simplex symmetry, the probability of \(Y\) being the greatest coordinate and at most \(t\) is one-third of the probability that all three simplex coordinates are at most \(t\). Inclusion-exclusion gives \(\sum_{j=0}^3(-1)^j\binom3j(1-jt)_+^2\).

For the one-occurrence event, write \(s=1-t\). The event that \(1-\min(X,Z)\le t\) is \(X,Z\ge s\), whose simplex area probability equals \((1-2s)_+^2\). Removing the subevent on which \(Y\) is the greatest coordinate gives a deduction of \((1-3s)_+^2/3\): after subtracting \(s\) from each coordinate, the residual simplex is symmetric and the \(Y\)-greatest region occupies one-third. This proves both joint CDF formulas. Their totals at \(t=1\) are \(1/3\) and \(2/3\). Integrating the respective survival functions gives conditional normalized means \(11/18\) and \(29/36\); the mean count converges to \(1(2/3)+2(1/3)=4/3\). Boundedness of these observables justifies convergence of expectations.

## Verification

The standalone standard-library program `verify_direct.py` computes the prefix-function border array of every suffix of every binary word with exactly two ones through length \(46\). It determines \(L\) and counts all maximizing intervals without using the asserted run-gap formulas, checking \(16{,}215\) words in total. The separately implemented `verify_series.py` groups the disjoint run classes and checks the exact joint length–multiplicity counts and rational-series coefficients for every length \(2\) through \(180\). The saved outputs are `verify_direct.out` and `verify_series.out`. Both scripts were executed from the package paths before delivery. Finite checks corroborate, but do not replace, the general combinatorial proof and simplex integration.

## Relationship to prior work

Mieno's 2026 linear-time algorithm reports all occurrences of globally longest unbordered factors for arbitrary strings. This establishes efficient computation of each instance, not an exact closed multiplicity spectrum or sparse-source joint distribution. Cording, Gagie, Knudsen, and Kociumaka analyze longest unbordered factors under a uniform independent-letter source; conditioning on exactly two ones has vanishing probability in that model and produces a different limiting regime. The previously reported exact weight-two *longest-border* spectrum determines the marginal maximum-length distribution here, because these particular words satisfy \(L(W)=\pi(W)\), where \(\pi\) is the least period. Accordingly neither the maximum-length marginal nor its expectation is asserted as independently new. The original contribution claimed here is the full occurrence-interval classification, the four-valued all-length multiplicity enumerator and the joint law of normalized maximum length with occurrence multiplicity. A previously reported weight-three unbordered-factor length spectrum studies a different fixed-content family and does not provide these occurrence counts.

## Limitations

No claim is made for binary words with more than two ones, for uniformly random unrestricted binary strings, or for the number of distinct maximizing factor *strings*. This is a combinatorial output-multiplicity law, not a faster worst-case algorithm. The literature comparison cannot exclude an unindexed earlier equivalent classification; independently conducted peer review has not been performed.

## References

1. T. Mieno, *Longest Unbordered Factors in Linear Time*, arXiv:2611.12146, first publicly submitted 2026-11-09. https://arxiv.org/abs/2611.12146
2. P. H. Cording, T. Gagie, M. B. T. Knudsen and T. Kociumaka, *Maximal Unbordered Factors of Random Strings*, arXiv:1704.04472, 2017. https://arxiv.org/html/1704.04472v2
3. S. Sekizaki and T. Mieno, *Longest Unbordered Factors on Run-Length Encoded Strings*, arXiv:2507.16285, first submitted 2025-07-22. https://arxiv.org/abs/2507.16285
4. *A sharp border spectrum and limit law for two-marker binary words*, public research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-border-spectrum-and-limit-law-for-two-marker-binary-word--823f52624582
5. *Exact longest-unbordered-factor spectrum of binary three-marker words and its Dirichlet limit law*, public research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-longest-unbordered-factor-spectrum-of-binary-three-marker--38db91c119b6
