# Sharp exchangeability boundaries for richness–pair-diversity covariance

## Finding

For a sample \(X_1,\ldots,X_n\), \(n\ge2\), with values in a categorical alphabet, let \(N_a=\#\{i:X_i=a\}\), let the observed richness be \(K_n=\#\{a:N_a>0\}\), and let the unbiased pairwise Gini–Simpson diversity statistic be
\[
G_n=\frac{1}{\binom n2}\sum_{1\le i<j\le n}\mathbf 1\{X_i\ne X_j\}
=1-\frac{\sum_a\binom{N_a}{2}}{\binom n2}.
\]
The following boundary statements all concern this same richness–diversity covariance.

**Finite-sample sharp boundary.** For every probability law on categorical samples of size \(2\le n\le6\), without any independence or exchangeability assumption,
\[
\operatorname{Cov}(K_n,G_n)\ge0.
\]
For every integer \(n\ge7\), there exists an exchangeable law on samples using only three labels with \(\operatorname{Cov}(K_n,G_n)<0\). In particular, when \(n=7\), choosing with equal probability a uniformly rearranged occupancy profile \((3,4,0)\) or \((5,1,1)\) gives exactly
\[
\operatorname{Cov}(K_7,G_7)=-\frac1{84}.
\]
For a two-label alphabet, nonnegative covariance holds at every sample size and under every law. Thus seven observations and three available labels are simultaneously minimal for a negative covariance under arbitrary finite exchangeability.

**Infinite-exchangeability boundary.** For any infinitely exchangeable sequence using at most two labels, \(\operatorname{Cov}(K_n,G_n)\ge0\) for every \(n\ge2\). In contrast, define an infinitely exchangeable three-label sequence by first choosing with equal probabilities one of the two categorical laws
\[
P=(1/2,1/2,0),\qquad Q=(9/10,1/20,1/20),
\]
and then taking all observations conditionally independent and identically distributed from that chosen law. This sequence has
\[
\operatorname{Cov}(K_{22},G_{22})=
-\frac{3412690498811343615664816319}{16777216000000000000000000000000}<0,
\]
and
\[
\lim_{n\to\infty}\operatorname{Cov}(K_n,G_n)=-\frac{63}{800}.
\]
No assertion is made that \(22\) is the smallest sample size admitting a negative covariance among *all* infinitely exchangeable three-label laws.

## Assumptions and scope

An exchangeable sample of finite length has a joint distribution invariant under permuting observation indices. Infinite exchangeability means that the whole infinite sequence is invariant under every finite permutation. These notions differ: the uniformly rearranged fixed-count profiles used above need not extend to an infinite exchangeable sequence.

All alphabets may contain unused labels, and all counts \(N_a\) are finite. The result is distribution-free for the universal finite-sample and two-label conclusions. The infinite-exchangeability counterexample is a concrete two-point mixture of categorical product laws. A pairwise Gini–Simpson diversity of one means all observed pairs have different labels; zero means all observations are equal.

## Proof

**Step 1: exact deterministic ranges at fixed richness.** Put
\[
C=\sum_a\binom{N_a}{2},\qquad G_n=1-C/\binom n2.
\]
If exactly \(k\) positive integer counts sum to \(n\), convexity of \(u\mapsto\binom u2\) shows that the minimum collision count is attained by balancing the counts, while its maximum is attained by one count \(n-k+1\) and \(k-1\) singleton counts. Writing \(n=kq+r\), \(0\le r<k\), gives the sharp bounds
\[
C_{\min}(n,k)=(k-r)\binom q2+r\binom{q+1}2,
\qquad C_{\max}(n,k)=\binom{n-k+1}2.
\]
For every \(2\le n\le6\) and every \(1\le k<n\), these formulas give
\[
C_{\min}(n,k)\ge C_{\max}(n,k+1).
\]
For completeness, the sequences \((C_{\min},C_{\max})\) for consecutive \(k=1,\ldots,n\) are:
\[
\begin{array}{c|l}
n&\text{intervals for }C\\\hline
2&(1,1),(0,0)\\
3&(3,3),(1,1),(0,0)\\
4&(6,6),(2,3),(1,1),(0,0)\\
5&(10,10),(4,6),(2,3),(1,1),(0,0)\\
6&(15,15),(6,10),(3,6),(2,3),(1,1),(0,0)
\end{array}
\]
Consequently, whenever two realized samples have \(K_n<K_n'\), they must have \(G_n\le G_n'\). With an independent copy \((K_n',G_n')\), the identity
\[
2\operatorname{Cov}(K_n,G_n)
=\mathbb E[(K_n-K_n')(G_n-G_n')]
\]
proves the claimed nonnegativity for every law, including nonexchangeable laws.

**Step 2: the sharp finite exchangeable counterexamples.** For \(n\ge7\), mix with equal probability the uniform random orderings of the count vectors
\[
(\lfloor n/2\rfloor,\lceil n/2\rceil,0)
\quad\text{and}\quad(n-2,1,1).
\]
Their richness values are respectively \(2\) and \(3\). Their collision counts are
\[
C_2=\binom{\lfloor n/2\rfloor}2+\binom{\lceil n/2\rceil}2,
\qquad C_3=\binom{n-2}2.
\]
For \(n=2h\), \(C_3-C_2=(h-1)(h-3)>0\) when \(h\ge4\). For \(n=2h+1\), \(C_3-C_2=h^2-3h+1>0\) when \(h\ge3\). Thus
\[
\operatorname{Cov}(K_n,G_n)=
-\frac{C_3-C_2}{4\binom n2}<0.
\]
At \(n=7\), \(C_3-C_2=1\) and the covariance is \(-1/84\). With at most two available labels, \(K_n\in\{1,2\}\), and \(G_n=0\) whenever \(K_n=1\). Hence
\[
\operatorname{Cov}(K_n,G_n)=
\Pr(K_n=1)\Pr(K_n=2)\mathbb E[G_n\mid K_n=2]\ge0
\]
(with the evident interpretation if one event has probability zero), proving minimality of the alphabet size.

**Step 3: infinite exchangeability on two labels.** An infinitely exchangeable binary sequence is, by the de Finetti representation, conditionally iid with a random success parameter \(U\in[0,1]\). At every fixed \(U=u\), the preceding two-label argument gives \(\operatorname{Cov}(K_n,G_n\mid U=u)\ge0\). Moreover,
\[
\mathbb E[K_n\mid U=u]=2-u^n-(1-u)^n,
\qquad \mathbb E[G_n\mid U=u]=2u(1-u).
\]
Both are nondecreasing functions of \(v=u(1-u)\in[0,1/4]\). Indeed, by symmetry we may take \(u\le1/2\), where both functions are nondecreasing in \(u\). The covariance of two nondecreasing functions of the same real random variable is nonnegative, by the independent-copy identity. The law of total covariance now gives the binary infinite-exchangeability conclusion.

**Step 4: the three-label infinite mixture.** Conditional on a categorical mass vector \(p=(p_1,p_2,p_3)\), write \(s_2=\sum_i p_i^2\). The exact conditional moments are
\[
k_n(p)=\mathbb E[K_n\mid p]=\sum_i\bigl[1-(1-p_i)^n\bigr],
\qquad g(p)=\mathbb E[G_n\mid p]=1-s_2,
\]
and
\[
c_n(p)=\operatorname{Cov}(K_n,G_n\mid p)
=\sum_i p_i(1-p_i)^{n-2}\bigl[2s_2-(1+s_2)p_i\bigr].
\]
The last identity follows directly by conditioning one of the pair indicators in \(G_n\) on the presence of each label, or from the exact iid occupancy–pair statistic calculation in the cited source. For an equal mixture of \(P\) and \(Q\), the law of total covariance therefore yields the exact rational expression
\[
\operatorname{Cov}(K_n,G_n)=
\frac{c_n(P)+c_n(Q)}2+
\frac{[k_n(P)-k_n(Q)][g(P)-g(Q)]}{4}.
\]
Substitution at \(n=22\) gives the stated negative rational value (the standalone exact checker evaluates this same quantity independently by full multinomial count-vector summation). In the limit, \(K_n\) tends almost surely to the number of positive masses in the selected component, and \(G_n\) tends almost surely to that component's population Gini–Simpson diversity. Since both statistics are bounded under the three-label model, their covariance converges to that of the limiting two-point vector, whose possible values are \((2,1/2)\) and \((3,37/200)\). Thus the limit is
\[
\frac14(2-3)(1/2-37/200)=-63/800.
\]
This completes the proof of each asserted boundary.

## Verification

Run `python check.py` with Python 3 and no third-party dependencies. It checks all integer positive-count profiles up to sample size six against the sharp deterministic bounds, verifies 114 further finite exchangeable constructions through size 120, and evaluates both the direct multinomial-count formula and the independent conditional-covariance formula exactly for sample sizes 2 through 26. The checker also confirms the explicit \(n=22\) rational, its sign, the \(n=7\) covariance, and the limiting rational. These computations corroborate the analytic proof; finite tests are not the proof of the universal assertions.

## Relationship to prior work

Barbour (2009) develops occupancy richness and frequency-count distribution approximations in the iid allocation model, not the finite-exchangeability covariance sign threshold. Favaro, Lijoi, and Prünster (2013) give a de Finetti representation and conditional results for exchangeable Gibbs-type partitions, not the claimed sharp \(n=7\) obstruction or the three-label two-component mixture. Lande (1996) establishes classical richness and unbiased Simpson sampling formulas and community diversity partitioning, without the sharp joint covariance robustness classification. Kvålseth (2024) studies richness–evenness dependence across randomly generated abundance distributions; the available abstract, introduction and conclusion do not provide the present sample-level exchangeability transition.

The published published-finding corpus finding **“Universal positive covariance of sample richness and unbiased Gini–Simpson diversity”** proves positivity under a fixed iid categorical law; its exact covariance formula agrees with \(c_n(p)\) in Step 4. That result is not re-claimed. The present finding identifies the sharp point at which dropping independence can reverse the sign and separates finite from infinite exchangeability. Its 3-label construction does not contradict any fixed-law iid positivity theorem: mixing components adds a potentially negative between-component covariance.

## Limitations

The binary case is universal; the negative finite exchangeable cases need not be infinitely extendible. The infinite-exchangeable example demonstrates negativity at sample size 22 and asymptotically, not the globally earliest negative sample size for arbitrary three-label de Finetti mixtures. The universal positive threshold is exactly sample size six only for unrestricted finite sample laws. Historical literature on occupancy and diversity might contain an implicit equivalent exchangeability boundary; the cited primary comparisons and repository checks are not an independence or priority certificate.

## References

1. A. D. Barbour, “Univariate approximations in the infinite occupancy scheme,” arXiv:0902.0879v1, first submitted 2009-02-05. https://arxiv.org/html/0902.0879v1
2. S. Favaro, A. Lijoi, and I. Prünster, “Conditional formulae for Gibbs-type exchangeable random partitions,” arXiv:1309.1335, first submitted 2013-09-05. https://arxiv.org/abs/1309.1335
3. R. Lande, “Statistics and partitioning of species diversity, and similarity among multiple communities,” *Oikos* 76 (1996), 5–13. https://pdodds.w3.uvm.edu/files/papers/others/1996/lande1996a.pdf
4. “Universal positive covariance of sample richness and unbiased Gini–Simpson diversity,” published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-universal-positive-covariance-of-sample-richness-and-unbiased-gi--e84114bd4ba0
5. T. O. Kvålseth, “Diversity analysis: Richness versus evenness,” *Ecology and Evolution* 14 (2024), e70275, first published 2024-09-23. https://doi.org/10.1002/ece3.70275
