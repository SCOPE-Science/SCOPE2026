# Convex-order optimality of balanced specialist support under exchangeable food-web removals

## Finding

**Theorem (majorization and all convex survivor-risk criteria).** Let \(a,b\ge2\) be integers, \(N=a+b\), and let \(m=(m_1,\ldots,m_a)\) be nonnegative integers summing to \(b\). Build a rooted, two-level directed food web with an undeletable basal source, \(a\) intermediary taxa each depending on the source, and \(m_i\) terminal specialist taxa each depending exclusively on intermediary \(i\). Expose the \(N\) removable taxa to an arbitrary *exchangeable* initial-retention law, identical for every support allocation. Retained intermediaries survive; a retained specialist survives if and only if its supporting intermediary is retained. Let \(Z_m\) count all surviving removable taxa after these secondary extinctions.

If \(m'\) majorizes \(m\), then for every convex function \(\phi:\mathbb R\to\mathbb R\),
\[
\mathbb E\phi(Z_m)\le\mathbb E\phi(Z_{m'}).
\]
The means agree, so this is ordinary **convex order**, not just increasing-convex order. Thus the allocation with specialist counts as equal as possible is universally least variable in convex order, and \((b,0,\ldots,0)\) is universally greatest. This holds separately for every fixed count \(r\) of initially retained taxa, i.e. under uniform sampling *without replacement*, and for any mixture over \(r\).

Write \(R\) for the random initial-retention count, \(q_j=\mathbb E[(R)_j]/(N)_j\), \((s)_j=s(s-1)\cdots(s-j+1)\), and \(T(m)=\sum_i\binom{m_i}{2}\). The exact common mean and variance-gap law are
\[
\mathbb E Z_m=aq_1+bq_2,
\qquad
\operatorname{Var}(Z_{m'})-\operatorname{Var}(Z_m)
=2\bigl[T(m')-T(m)\bigr](q_3-q_4).
\]
For non-permutation profiles with \(m'\) majorizing \(m\), the variance gap is strictly positive **if and only if** the retention count assigns positive probability to \(3\le R<N\). Otherwise their survivor-count laws coincide. The conclusion applies equally to losses \(N-Z_m\), since convex order is invariant under affine sign reversal.

## Assumptions and scope

There is one energy source that cannot be removed; it connects to each intermediary. Each terminal taxon has exactly one supporting intermediary and no alternative food source. All \(N=a+b\) non-basal taxa are initially present, then an exchangeable random subset is initially retained. In a finite exchangeable binary law, conditional on \(R=r\) every \(r\)-element subset has probability \(1/\binom Nr\). If a retained specialist loses its sole supporting intermediary, it experiences bottom-up secondary extinction. No other biological or dynamical extinction mechanism is assumed.

For a profile \(m\), let \(X_i\) indicate initial retention of intermediary \(i\), and \(Y_{ij}\) retention of its \(j\)-th specialist. Then
\[
Z_m=\sum_{i=1}^a X_i\left(1+\sum_{j=1}^{m_i}Y_{ij}\right).
\]
All labels are exchangeable, but their indicators need not be independent; under fixed \(R\) they are generally negatively correlated. Majorization means that descendingly ordered coordinates of \(m'\) have at least the corresponding prefix sums of \(m\), with equal total sum. The theorem does not compare arbitrary incomparable profiles or pointwise upper/lower-tail probabilities.

## Proof

**1. A concentration transfer increases every convex expectation.** It is sufficient, by the elementary integer majorization decomposition, to move one specialist from a group of size \(s\ge1\) to a group of size \(h\ge s\). Before the transfer, these groups have sizes \((h,s)\); afterward they have sizes \((h+1,s-1)\). Assign the movable specialist label the indicator \(Y\), the two support indicators \(X_1,X_2\), and let \(A\) and \(B\) count initially retained other specialists in the respective groups (of sizes \(h\) and \(s-1\)). Let \(W\) count surviving taxa in every other group. The two survivor totals differ only when \(Y=1\) and exactly one of \(X_1,X_2\) is one. Writing \(\Delta\phi(z)=\phi(z+1)-\phi(z)\), their expectation difference is
\[
\begin{split}
\mathbb E[\phi(Z_{(h+1,s-1)})-\phi(Z_{(h,s)})]
={}&\Pr(X_1=1,X_2=0,Y=1)\\[-2pt]
&\cdot\mathbb E[\Delta\phi(W+1+A)-\Delta\phi(W+1+B)\mid X_1=1,X_2=0,Y=1].
\end{split}
\]
Here the negative-contribution configuration \((X_1,X_2,Y)=(0,1,1)\) has been relabeled by interchanging the two support indicators; the equality of the conditional distributions follows from full exchangeability of initial retention. The other labels, including \(W\), are unchanged by this interchange.

Condition further on the initial indicators outside the two specialist pools, including those determining \(W\), and on the total \(K\) retained among their \(h+s-1\) labels. Exchangeability makes the retained subset uniform conditional on \(K\). The count \(A\) has a hypergeometric distribution counting membership in a fixed \(h\)-element subset; \(B\) counts membership in a fixed \((s-1)\)-element subset of the same population. Because \(h\ge s-1\), the two hypergeometric marginals admit a coupling in which \(A\ge B\): nest any \((s-1)\)-subset inside an \(h\)-subset and sample the same uniformly chosen \(K\)-element set. As \(\Delta\phi\) is nondecreasing for convex \(\phi\), the displayed difference is nonnegative. Summing over every conditioning value proves the concentration-transfer inequality, and chaining such transfers proves the asserted convex order for every exchangeable law.

**2. The common mean.** Every intermediary survives with probability \(q_1\). Every specialist survives exactly when its own label and parent are retained, with probability \(q_2\). Summing gives \(aq_1+bq_2\), independent of the allocation profile.

**3. Exact variance gap and strictness.** Expand the covariance of the \(a\) single-indicator terms \(X_i\) and \(b\) two-indicator terms \(X_iY_{ij}\). Every covariance category has a profile-independent multiplicity except pairs of distinct specialists attached to the same parent; there are \(T(m)\) such unordered pairs. Each such pair has joint-survival probability \(q_3\), whereas a pair attached to distinct parents has joint-survival probability \(q_4\). Both pair categories have marginal-survival product \(q_2^2\). Hence changing the allocation changes the variance by exactly \(2\Delta T(q_3-q_4)\). Under proper majorization, \(T(m')>T(m)\). For fixed \(R=r\),
\[
q_3-q_4=\frac{(r)_3}{(N)_3}\left(1-\frac{r-3}{N-3}\right)
\]
for \(r\ge3\), and zero for \(r<3\). Therefore this quantity is strictly positive exactly when \(3\le r<N\). For a general exchangeable law it is positive exactly when this interval has positive probability. If no such mass exists, only \(R\in\{0,1,2,N\}\) occurs; the survivor-count law for each of these initial counts is independent of the allocation: for \(R=2\), the only profile-dependent-looking event is retention of a matched parent-specialist pair, but its count is always \(b\). This proves the stated equality classification.

## Verification

The standalone `verify.py` uses exact integer and rational arithmetic, implements the coefficient-generating function and an independent complete enumeration of uniform initially retained subsets, and checks convex stop-loss inequalities and the variance identity across all allocation profiles with \(2\le a\le5\), \(2\le b\le7\) and all initial-retention counts. On execution it reports 1,244 verified histograms, 354 comparable distinct majorization pairs, 44,829 stop-loss inequalities, 3,945 exact variance differences and 2,529 strict interior-stage variance gaps. These finite computations corroborate but do not replace the preceding general proof.

The exact fixed-count distribution can also be reconstructed by extracting the coefficient of \(u^r z^k\) from
\[
\prod_{i=1}^a\left[(1+u)^{m_i}+uz(1+uz)^{m_i}\right]
\]
and dividing it by \(\binom Nr\). For \(a=2,b=3,r=3\), the frequencies of \(Z=0,1,2,3\) are \((1,1,4,4)\) for balanced \(m=(2,1)\) and \((1,3,0,6)\) for concentrated \(m'=(3,0)\), out of ten equally likely retained subsets. Both means are \(21/10\), while the latter variance exceeds the former by \(2/5\).

## Relationship to prior work

Dunne, Williams and Martinez (2002) established the biological motivation for studying robustness under primary species removal and subsequent secondary extinctions. Allesina, Bodini and Pascual (2009) studied the functional versus redundant food-web links, while Allesina and Pascual (2009) analyzed species-importance rankings for cascading coextinction. These models motivate the special two-level network considered here; their inspected results do not provide an allocation-majorization comparison of *every* convex survivor-count risk under fixed-count random removal.

A particularly relevant mathematical precedent is Bäuerle and Müller (1998), Theorem 3.2, giving stop-loss order under majorization of group sizes for risk portfolios with independent group-specific and individual-specific factors, conditional on a global environment. Its aggregation principle is close to the present conclusion. The assumptions do not directly cover the present fixed-count experiment: for \(0<r<N\), distinct initially retained indicators have covariance \(-r(N-r)/(N^2(N-1))<0\), whereas the specified independent-factor group model, with identically distributed individual risks, has nonnegative covariance between distinct groups under a shared environmental mixture. Moreover, intermediaries are themselves counted as survivors in the present model. Thus the all-exchangeable fixed-count extension and exact variance/equality law require separate argument. This contrast is an inapplicability argument, not an assertion that no alternate general stochastic-order theorem could imply the result.

## Limitations

Only a rooted two-level specialist model with a protected basal source and exclusive specialist dependencies is treated. The conclusion does not automatically hold with alternative resources, consumer competition, dynamic rewiring, nonexchangeable primary removals, more trophic levels or adaptive responses. Convex order is a dispersion ordering at a common mean: it does not say that every individual extinction-tail probability is monotone, and it does not establish empirical ecosystem outcomes. The priority comparison is grounded in the specified sources but is not an exhaustive survey of all historical dependence-order literature. Independent validation has not been performed.

## References

- Dunne, J. A., Williams, R. J. & Martinez, N. D. (2002), *Network structure and biodiversity loss in food webs: robustness increases with connectance*. Ecology Letters 5, 558–567. https://doi.org/10.1046/j.1461-0248.2002.00354.x (first public online date confirmed as 2002-07-10).
- Allesina, S., Bodini, A. & Pascual, M. (2009), *Functional links and robustness in food webs*. Philosophical Transactions of the Royal Society B 364, 1701–1709. https://doi.org/10.1098/rstb.2008.0214.
- Allesina, S. & Pascual, M. (2009), *Googling Food Webs: Can an Eigenvector Measure Species' Importance for Coextinctions?* PLOS Computational Biology 5, e1000494. https://doi.org/10.1371/journal.pcbi.1000494.
- Bäuerle, N. & Müller, A. (1998), *Modeling and comparing dependencies in multivariate risk portfolios*. ASTIN Bulletin 28, 59–76, Theorem 3.2. https://doi.org/10.2143/AST.28.1.519079.
