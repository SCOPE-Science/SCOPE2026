# Universal chords in random circle graphs: exact hub counts and conditional crossing fluctuations

## Finding

Let \(\mathcal M_n\) be a uniformly random perfect matching of \(2n\) cyclically ordered labeled endpoints, with \(n\ge1\), and form its chord-intersection graph. Let \(U_n\) count **universal chords**, meaning chords crossing all \(n-1\) other chords, and let \(X_n\) count unordered crossing pairs. Then the full finite distribution of \(U_n\) is determined by

\[
\mathbb E\binom{U_n}{k}
=\frac{n}{k(2n-1)!!}
\sum_{\substack{s_1+\cdots+s_k=n-k\\s_i\ge0}}
\prod_{i=1}^k s_i!,\qquad 1\le k\le n.
\]

In particular, \(\mathbb EU_n=2^n/\binom{2n}{n}\), the value \(U_n=n-1\) is impossible for \(n\ge2\), and

\[
\Pr(U_n\ge1)=\frac{2^n}{\binom{2n}{n}}\bigl(1+O(n^{-1})\bigr)
\sim\frac{\sqrt{\pi n}}{2^n},\qquad
\Pr(U_n\ge2\mid U_n\ge1)=O(n^{-1}).
\]

Condition on the *specified* diameter \(\{1,n+1\}\) being universal and put \(N=n-1\). All other chords are then encoded by a uniform permutation \(\pi\in S_N\), and exactly

\[
X_n=N+\binom N2-\operatorname{inv}(\pi),\qquad
U_n=1+\sum_{j=1}^{N}\mathbf1\{\pi(j)=j,\ \pi([j-1])=[j-1]\}.
\]

Consequently, under this specified-chord conditioning,

\[
\mathbb EX_n=N+\frac12\binom N2,\qquad
\operatorname{Var}(X_n)=\frac{N(N-1)(2N+5)}{72}.
\]

The same central limit theorem holds when conditioning only on the **existence** of at least one universal chord:

\[
\left.\frac{X_n-\bigl(N+\frac12\binom N2\bigr)}{n^{3/2}}
\ \right|\ (U_n\ge1)
\xrightarrow{\ d\ }\mathcal N(0,1/36).
\]

In particular, the crossing-density law shifts from \(X_n/n^2\to1/6\) in probability without conditioning to \(X_n/n^2\to1/4\) in probability when a universal chord exists.

## Assumptions and scope

The \(2n\) endpoints are distinguishable, placed in fixed cyclic order \(1,\ldots,2n\), and uniformly paired into \((2n-1)!!=(2n)!/(2^n n!)\) perfect matchings. Two chords cross exactly when their four endpoints alternate in cyclic order. The graph has one vertex per chord; graph-theoretic universality includes the single-vertex case \(n=1\). The diameter \(\{i,i+n\}\), \(1\le i\le n\), joins opposite positions, not a metric-dependent random chord. The probability statements refer to this matching distribution. The limit \(n\to\infty\) is over integers with no other scaling parameter.

The stated full law is recoverable from its binomial moments by
\[
\Pr(U_n=j)=\sum_{k=j}^n(-1)^{k-j}\binom kj\mathbb E\binom{U_n}{k},
\qquad 0\le j\le n.
\]

## Proof

**1. Geometric obstruction.** If a chord crosses all others, its two open circular arcs must each contain exactly one endpoint of each of the remaining \(n-1\) chords. Both arcs therefore contain \(n-1\) endpoints, and the universal chord must equal one of the \(n\) diameters \(\{i,i+n\}\). Conversely, a present diameter is universal precisely when every remaining matching edge joins its two complementary open semicircles.

**2. Exact joint forcing.** Choose \(k\) of the \(n\) candidate diameters, in cyclic order. They divide the circular endpoint set into \(2k\) sectors, with opposite sectors containing the same respective numbers \(s_1,\ldots,s_k\) of unused endpoints and \(\sum_i s_i=n-k\). A further chord crosses all selected diameters if and only if its two endpoints lie in a pair of opposite sectors. (The sign vector recording which side of each selected diameter contains the endpoint must be reversed in every coordinate; among the \(2k\) sectors, precisely the opposite sector has that sign vector.) Each opposite pair of sectors can be perfectly cross-paired in \(s_i!\) ways, independently, giving \(\prod_i s_i!\) compatible matchings.

To sum over selected diameter sets, choose a starting candidate diameter in \(n\) ways and choose the nonnegative cyclic gap tuple \((s_1,\ldots,s_k)\) summing to \(n-k\). Every unordered selected set is represented exactly \(k\) times. Division by \((2n-1)!!\) yields the displayed binomial moment formula. The claim that exactly \(n-1\) universal chords cannot occur follows because the sole remaining pair of endpoints must form the last diameter; in fact there is exactly one matching with all \(n\) diameters.

**3. Conditional permutation graph.** Fix \(c=\{1,n+1\}\), and require that it be universal. Number the \(N\) endpoints in the arc between its endpoints by \(A_1,\ldots,A_N\), and those in the complementary arc in the same cyclic direction by \(B_1,\ldots,B_N\). All other matching edges are \(\{A_j,B_{\pi(j)}\}\) for a bijection \(\pi\), and every such bijection is equiprobable. For \(i<j\), these edges cross exactly when \(\pi(i)<\pi(j)\), proving the crossing identity with the usual inversion count. An edge \(\{A_j,B_{\pi(j)}\}\) is an additional universal chord exactly when \(\pi(j)=j\), every index less than \(j\) maps to a value less than \(j\), and every index greater than \(j\) maps to a value greater than \(j\). This is equivalent to \(\pi([j-1])=[j-1]\) and \(\pi(j)=j\), the singleton direct-sum block property. The identities also hold for \(N=0\) with empty sums.

**4. Rare-event control.** With \(D=(2n-1)!!\), one fixed candidate diameter is universal in exactly \((n-1)!\) matchings, so \(\mathbb EU_n=n(n-1)!/D=2^n/\binom{2n}{n}\). For \(N\ge1\), the preceding permutation representation gives
\[
\mathbb E[U_n-1\mid c\text{ universal}]
=\frac1N\sum_{r=0}^{N-1}\binom{N-1}{r}^{-1}
=\frac2N+O(N^{-2}).
\]

The estimate follows by separating the two boundary terms, the two next-to-boundary terms, and bounding all interior reciprocal binomial coefficients by \(2/((N-1)(N-2))\) for large \(N\). By size-biased counting of pairs of universal chords,
\[
\frac{\mathbb E\binom{U_n}{2}}{\mathbb EU_n}
=\frac12\mathbb E[U_n-1\mid c\text{ universal}]=O(n^{-1}).
\]

Bonferroni's bounds \(\mathbb EU_n-\mathbb E\binom{U_n}{2}\le\Pr(U_n\ge1)\le\mathbb EU_n\), and \(\Pr(U_n\ge2)\le\mathbb E\binom{U_n}{2}\), imply the announced rare-event probabilities; the asymptotic equivalent uses Stirling's formula.

**5. Conditional normality and density.** For a uniform permutation of \(N\) elements, the inversion count is a sum of independent random variables uniformly distributed on \(\{0,\ldots,j-1\}\), \(1\le j\le N\), via its inversion sequence. Its mean is \(\frac12\binom N2\) and its variance is \(N(N-1)(2N+5)/72\). Lindeberg's theorem applies because each summand is bounded by \(N\) while the standard deviation grows like \(N^{3/2}/6\). This proves the fixed-diameter conditional Gaussian limit.

For a rotation-invariant statistic, the distribution conditioned on a fixed candidate diameter being universal equals that under the *size-biased matching law* with weight proportional to \(U_n\). The size-biased law and the matching law conditioned on \(U_n\ge1\) have total-variation distance \(O(n^{-1})\), because their Radon–Nikodym ratio is \(U_n/\mathbb E[U_n\mid U_n\ge1]\), while \(\mathbb E[U_n-1\mid U_n\ge1]=O(n^{-1})\) by the preceding bounds. As \(X_n\) is rotation-invariant, the same Gaussian limit follows under existence conditioning. In particular its normalized limit is \(1/4\). Unconditionally, each pair of chords crosses with probability \(1/3\), so \(\mathbb EX_n=\binom n2/3\); using independent endpoint pairs labeled by chord, crossing indicators for disjoint *pairs of chords* are independent, leaving only \(O(n^3)\) potentially dependent indicator pairs. Thus \(\operatorname{Var}(X_n)=O(n^3)\), and Chebyshev gives \(X_n/n^2\to1/6\) in probability.

## Verification

Run `python3 verify.py` from this file's directory. The standalone checker enumerates all perfect matchings through seven chords and all cross-semicircle permutations through eight chords, calculating graph crossings from alternating endpoints independently of the factorial-moment and inversion formulas. It verifies all finite binomial moments, the impossibility of \(n-1\) universal chords, the exact specified-hub conditional identities, and exact mean/variance. This supplies finite diagnostic checks, not an infinite proof; the preceding combinatorial arguments and Lindeberg analysis cover general sizes and limits.

## Relationship to prior work

Acan's 2015 work establishes the random chord-intersection graph model and studies the limiting degree of one randomly chosen chord; its length inequality already implies that universal chords must be diameters. That single-chord observation and the first-moment probability are not claimed as independently new. Flajolet and Noy establish unconditional crossing-number normality and component limits. Acan and Pittel study a different regime, conditioning on an unusually small *total* crossing count to analyze giant components. The present theorem instead counts **all maximum-degree vertices simultaneously**, including their exact finite distribution, and identifies the distinct permutation structure and Gaussian fluctuations under the exponentially rare *existence of a universal vertex*. A previously published marked-chord conditional regression also gives the conditional *mean* when a fixed chord crosses all others; that mean is credited, while the full conditional law, variance, and rare-event transfer are evaluated together with the universal-count theorem. A previously published marked-chord conditional regression also gives the conditional *mean* when a fixed chord crosses all others; that mean is credited, while the full conditional law, variance, and rare-event transfer are evaluated together with the universal-count theorem. A previously published marked-chord conditional regression also gives the conditional *mean* when a fixed chord crosses all others; that mean is credited, while the full conditional law, variance, and rare-event transfer are evaluated together with the universal-count theorem. Known inversion-number formulas are used as standard inputs, not claimed as new.

## Limitations

The finding concerns uniformly paired cyclic endpoints and the maximum possible crossing degree, not the entire upper-degree spectrum or nonuniform endpoint-matching laws. The full finite universal-count law is an explicit composition sum, not a closed elementary expression for every point probability. The Gaussian statement is a weak limit, with no quantitative Berry–Esseen error asserted. The historical-priority comparison is bounded by available primary material; general permutation-pattern or circular-matching enumeration literature may contain equivalent counts under another formulation.

## References

- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, publicly posted 2015-01-07. https://arxiv.org/abs/1501.01489
- H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867v1, publicly posted 2014-06-11. https://arxiv.org/abs/1406.2867
- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, in *Formal Power Series and Algebraic Combinatorics*, 2000, pp. 191–201. https://doi.org/10.1007/978-3-662-04166-6_17
