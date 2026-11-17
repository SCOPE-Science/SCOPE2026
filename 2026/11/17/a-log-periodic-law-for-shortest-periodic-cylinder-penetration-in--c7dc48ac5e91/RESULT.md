# A log-periodic law for shortest periodic cylinder penetration in a zero-entropy shift

## Finding

There is a natural countable binary subshift with dense periodic points and exact factor complexity \(p(n)=2n\), whose uniformly sampled length-\(n\) cylinders have **no limiting distribution of shortest periodic penetration periods after normalization by \(n\)**. In fact, the entire empirical law has an explicitly computable, nonconstant phase profile, and its normalized mean has the sharp accumulation interval \([2/3,3/4]\).

Let \(X\) be the two-sided subshift obtained by closing the union of all shifts of the periodic binary configurations \(x^{(j)}\) having a \(1\) exactly at multiples of \(2^j\), for integers \(j\geq0\). For each length-\(n\) admissible word \(w\), let \(\eta(w)\) be the least positive period of a periodic configuration of \(X\) whose coordinates \(0,\ldots,n-1\) equal \(w\). Let \(W_n\) be uniform on the length-\(n\) language, and put \(N=2^{\lfloor\log_2 n\rfloor}\) and \(r=n-N\). Then the *exact* histogram is

\[
\#\{w:\eta(w)=d\}=\begin{cases}
2,&d=1,\\
d,&d\in\{2,4,\ldots,N\},\\
2r,&d=2N,\\
0,&\text{otherwise},
\end{cases}
\]

where any zero entry at \(d=2N\) is omitted. In particular, for every \(n\geq1\),

\[
p(n)=2n,\qquad
\mathbb E[\eta(W_n)]=\frac{(4N^2+2)/3+4Nr}{2n},\qquad
\mathbb E[\eta(W_n)^2]=\frac{(8N^3+6)/7+8N^2r}{2n}.
\]

If \(n/N\to t\in[1,2]\), the probability laws of \(\eta(W_n)/n\) converge weakly to

\[
\nu_t=\frac{t-1}{t}\,\delta_{2/t}
+\sum_{k=0}^{\infty}\frac{2^{-k}}{2t}\,\delta_{2^{-k}/t}.
\]

The profile is nonconstant for \(1<t<2\) and satisfies \(\nu_1=\nu_2\). In particular,

\[
\liminf_{n\to\infty}\frac{\mathbb E[\eta(W_n)]}{n}=\frac23,
\qquad
\limsup_{n\to\infty}\frac{\mathbb E[\eta(W_n)]}{n}=\frac34.
\]

The complete set of subsequential limits of the normalized means is exactly \([2/3,3/4]\). The corresponding normalized variance has phase profile

\[
\lim\frac{\operatorname{Var}(\eta(W_n))}{n^2}
=\frac{40}{21t^3}-\frac{16}{9t^4},
\]

along the same phase-convergent subsequences.

## Assumptions and scope

All shifts are left shifts on \(\{0,1\}^{\mathbb Z}\) with the product topology. The orbit of \(x^{(j)}\) consists of the \(2^j\) configurations having consecutive \(1\)'s separated by exactly \(2^j\) positions. Their union's closure also contains the all-zero point and the isolated-single-\(1\) configurations. Thus periodic points are dense in \(X\), and its periodic points are exactly the listed cycles and the all-zero point. A cylinder is specified by a contiguous block on indices \(0,\ldots,n-1\), and the probability distribution is uniform over **distinct words**, not over cycles or periodic points.

The claims quantify all integers \(n\ge1\); the weak-limit statement quantifies arbitrary sequences of \(n\to\infty\) with \(n/2^{\lfloor\log_2 n\rfloor}\to t\in[1,2]\). Both endpoints represent the same law. No mixing, irreducibility, finite-type, or fixed invariant sampling measure is assumed.

## Proof

**1. Exact periodic points.** If a sequence of shifted configurations with periods \(2^{j_k}\) converges and the indices \(j_k\) are bounded, a subsequence has constant period and stabilizes at one of the listed periodic points. If \(j_k\to\infty\), every fixed finite window contains at most one \(1\), so any limit has at most one \(1\) on all of \(\mathbb Z\). Conversely, each singleton and zero sequence is a limit of shifted dyadic periodic sequences. A sequence with exactly one \(1\) is not periodic. Therefore no other periodic point contributes to \(\eta\).

**2. Exact word census.** Fix \(N=2^K\le n<2^{K+1}=2N\) and \(r=n-N\). For every dyadic period \(d<N\), a window of length \(n\ge2d\) contains at least two \(1\)'s, and its \(d\) cyclic phases yield \(d\) distinct words. The gap between consecutive \(1\)'s uniquely forces least possible periodic extension period \(d\); a different dyadic period cannot realize the word. For period \(d=N\), all \(N\) cyclic phases remain distinct, of which exactly \(r\) have two \(1\)'s and \(N-r\) have a single \(1\). A single-\(1\) word at position \(i\) belongs to a period-\(N\) cycle exactly when \(r\le i\le N-1\). Of the \(n\) possible single-\(1\) positions, the remaining \(2r\) first appear in a cycle of period \(2N\), so have \(\eta=2N\). All bigger dyadic cycles introduce no new words, because their windows contain at most a singleton \(1\) (or only zeroes). The all-zero word has \(\eta=1\). In the case \(N=1\), the period-one all-ones word contributes one more word at \(\eta=1\). This proves the displayed histogram, including all degenerate boundary cases. Summing multiplicities yields

\[
1+\sum_{j=0}^K2^j+2r=1+(2N-1)+2r=2n.
\]

**3. Exact moments.** Multiply the histogram by \(d\) and \(d^2\), respectively. The geometric-sum formulas yield

\[
1+\sum_{j=0}^K4^j+2r(2N)
=\frac{4N^2+2}{3}+4Nr,
\]
\[
1+\sum_{j=0}^K8^j+2r(2N)^2
=\frac{8N^3+6}{7}+8N^2r.
\]

After division by \(2n\), these are exactly the expectations in the theorem.

**4. Phase weak limits.** Set \(t_n=n/N\). The period-\(2N\) mass is \(2r/(2n)=(t_n-1)/t_n\), located at \(2N/n=2/t_n\). The mass from period \(N/2^k\) equals \((N/2^k)/(2n)=2^{-k}/(2t_n)\), at \((N/2^k)/n=2^{-k}/t_n\), for \(k=0,\ldots,K\). The remaining all-zero-word mass is \(1/(2n)\) at \(1/n\). The tails of these geometric weights are uniformly summable and hence the laws converge weakly to the displayed \(\nu_t\). Both endpoint laws agree: the atom at \(1\) at \(t=2\) is precisely the leading dyadic atom at \(t=1\), and the other atoms reindex.

**5. Sharp extrema and full cluster sets.** Integration gives the first and second normalized moments

\[
m(t)=\frac{2}{t}-\frac{4}{3t^2},\qquad
q(t)=\frac{4}{t^2}-\frac{24}{7t^3}.
\]

Their difference \(q(t)-m(t)^2\) gives the variance profile. Since

\[
m'(t)=\frac{8-6t}{3t^3},
\]

\(m\) is strictly increasing on \([1,4/3]\) and strictly decreasing on \([4/3,2]\), attaining \(m(1)=m(2)=2/3\) and \(m(4/3)=3/4\). For every \(t\in[1,2]\), choose integers \(n_K\in[2^K,2^{K+1})\) with \(n_K/2^K\to t\); for \(t=2\), approach from below. Every integer sequence has a subsequence with a convergent phase in the compact interval \([1,2]\). Therefore the cluster set of the normalized means equals the full interval between these extrema. In particular no single limit law exists, since for \(1<t<2\), \(\nu_t\) places positive mass above \(1\), whereas \(\nu_1\) is supported in \([0,1]\).

## Verification

The standalone pure-Python checker `verify.py` explicitly constructs every periodic-cylinder word for each \(1\le n\le110\), compares the complete least-period histogram with the formula, tests \(p(n)=2n\), and checks both exact moment sums. This is finite reproducibility support; the argument above proves the infinite statements independently. Run `python verify.py` with Python 3.9 or later; no third-party modules are required.

## Relationship to prior work

Ville Salo's *Periodic points and residual finiteness of automorphism groups of subshifts* (arXiv:2603.16591v1, publicly submitted 17 March 2026) develops qualitative implications of density or failure of density of periodic configurations, including automorphism-group properties. The present theorem resolves a different, quantitative question: how large the shortest periodic *cylinder* extension period is across all words of each length, in one canonical countable and densely periodic example. Qualitative periodic-point density implies only existence of a finite period for each word; it does not imply the exact histogram, the phase-dependent weak limits, or the sharp mean oscillation.

Ilkka Törmä's *On countable SFT covers of sparse multidimensional shift spaces* (Theoretical Computer Science, 2026, DOI 10.1016/j.tcs.2026.115755) studies sparse marker configurations and countability/covering properties. Its gap-width conditions and covers do not compute this union-of-dyadic-periodic-orbits language or its cylinder penetration statistic. Other exact complexity and periodic-orbit enumeration results in the literature do not provide the asserted histogram for this particular shift; the period distribution is not a formal consequence of the language-size identity.

## Limitations

This theorem is for a specifically defined countable, reducible, nonmixing binary subshift; it is not a universal asymptotic law for densely periodic subshifts. The sample distribution is uniform over **distinct length-\(n\) words**; no assertion is made about sampling from an invariant measure, about physical recurrence times, or about automorphism groups. Log-periodic nonconvergence is proved for this canonical dyadic sparse model, not for arbitrary lacunary period sets. Originality was assessed against retrieved primary sources and a mathematical-results database, not independently certified; unindexed work on countable symbolic shifts remains a priority risk.

## References

1. Ville Salo, *Periodic points and residual finiteness of automorphism groups of subshifts*, arXiv:2603.16591v1, 17 March 2026, https://arxiv.org/abs/2603.16591 .
2. Ilkka Törmä, *On countable SFT covers of sparse multidimensional shift spaces*, Theoretical Computer Science 1066 (2026), article 115755, https://doi.org/10.1016/j.tcs.2026.115755 .
