# Boundary covariance and cyclic orthogonality for fixed points and consecutive permutation patterns

## Finding

Let \(\pi\) be uniform on permutations of \(\{1,\ldots,n\}\). For any integer \(2\le m\le n\) and any permutation pattern \(\sigma\in S_m\), write \(F=\sum_{i=1}^{n}\mathbf1\{\pi_i=i\}\) and let \(T_\sigma\) be the number of *linear consecutive* windows whose relative-order pattern is \(\sigma\). Let \(T_\sigma^{\mathrm{cyc}}\) count the analogous \(n\) cyclic windows, allowing wrap-around but requiring \(m\le n\).

The complete fixed-point-versus-window covariance is local: it vanishes unless the fixed-point location belongs to the window, and then it depends on \(\sigma\) only through the rank at the marked location. The resulting linear covariance obeys an explicit nonnegative boundary-penalty formula. **Among all \(m!\) length-\(m\) patterns, the increasing pattern \((1,2,\ldots,m)\) uniquely maximizes \(\operatorname{Cov}(F,T_\sigma)\)**, for every \(n\ge m\ge2\), with maximum
\[
\operatorname{Cov}(F,T_{(1,2,\ldots,m)})=\frac{m-1}{n(m-1)!}.
\]
By contrast, every cyclic pattern count is exactly uncorrelated with fixed-point count:
\[
\operatorname{Cov}(F,T_\sigma^{\mathrm{cyc}})=0
\quad\text{for all }n\ge m\ge2,\ \sigma\in S_m.
\]
This is covariance-zero, not an assertion of independence.

For the first nontrivial order \(m=3\), the six linear covariances are

| Pattern \(\sigma\) | \(\operatorname{Cov}(F,T_\sigma)\) |
| --- | --- |
| \(123\) | \(1/n\) |
| \(132\), \(213\) | \((n-3)/(2n(n-1))\) |
| \(231\), \(312\) | \(-1/(2n)\) |
| \(321\) | \(-(n-3)/(n(n-1))\) |

For \(n=3,4\), the minimum is shared by \(231\) and \(312\); at \(n=5\), \(321\) joins them; and for every \(n\ge6\), \(321\) is the unique minimizer.

## Assumptions and scope

Indices are \(1\)-based. For any tuple of distinct numbers, its *pattern* is the unique permutation with the same strict pairwise order comparisons. A linear window starts at \(j\in\{1,\ldots,n-m+1\}\). A cyclic window starts at any \(j\in\{1,\ldots,n\}\), with indices reduced modulo \(n\); values retain their ordinary order \(1<\cdots<n\). All probabilities refer to a uniform permutation, not an Ewens, Mallows, or pattern-avoiding distribution. Define \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\) for \(0\le b\le a\), and \(\binom a b=0\) when \(b<0\) or \(b>a\).

## Proof

**1. One fixed point and one window.** Put \(I_i=\mathbf1\{\pi_i=i\}\) and \(A_{j,\sigma}=\mathbf1\{\operatorname{pat}(\pi_j,\ldots,\pi_{j+m-1})=\sigma\}\). We have \(\mathbb EI_i=1/n\), \(\mathbb EA_{j,\sigma}=1/m!\). Conditioning on \(I_i=1\), if \(i\notin\{j,\ldots,j+m-1\}\), the \(m\) remaining values in that window are exchangeable, hence the conditional probability is still \(1/m!\), so the covariance is zero.

Otherwise let \(r=i-j+1\in\{1,\ldots,m\}\), \(k=\sigma(r)\). In the other \(m-1\) positions, the \(k-1\) values below \(i\) and the \(m-k\) values above \(i\) must be chosen. Each selection has exactly one placement realizing \(\sigma\), out of the \((n-1)_{\underline{m-1}}\) possible ordered distinct fillings. Consequently
\[
\operatorname{Cov}(I_i,A_{j,\sigma})=\frac1n\left[
\frac{\binom{i-1}{k-1}\binom{n-i}{m-k}}{(n-1)_{\underline{m-1}}}-\frac1{m!}
\right].\tag{1}
\]
This proves the local rank-only kernel for every \(m,n\).

**2. Exact boundary penalty.** For \(1\le r,k\le m\) define the explicitly nonnegative integer
\[
B_{r,k}(n,m)=
\sum_{i=1}^{r-1}\binom{i-1}{k-1}\binom{n-i}{m-k}
+\sum_{i=n-m+r+1}^{n}\binom{i-1}{k-1}\binom{n-i}{m-k}.
\tag{2}
\]
For each \(r\), summing over linear starts makes the marked fixed-point location traverse exactly \(r,r+1,\ldots,n-m+r\). The elementary order-statistic version of Vandermonde's identity states
\[
\sum_{i=1}^{n}\binom{i-1}{k-1}\binom{n-i}{m-k}=\binom nm.
\tag{3}
\]
Indeed both sides count \(m\)-subsets by their \(k\)-th smallest member. Since \(\binom nm/(n-1)_{\underline{m-1}}=n/m!\), summing (1) over all linear windows and all fixed-point indices gives
\[
\boxed{\operatorname{Cov}(F,T_\sigma)=
\frac{m-1}{n(m-1)!}
-\frac{\sum_{r=1}^{m}B_{r,\sigma(r)}(n,m)}{n(n-1)_{\underline{m-1}}}.}\tag{4}
\]

For \(k=r\), both tails in (2) vanish: the lower tail cannot have \(k-1\) smaller values and the upper tail cannot have \(m-k\) greater values. For \(k<r\), the lower-tail summand at \(i=k\) equals \(\binom{n-k}{m-k}>0\); for \(k>r\), the upper-tail summand at \(i=n-m+k\) equals \(\binom{n-m+k-1}{k-1}>0\). Hence
\[
B_{r,k}(n,m)=0\iff k=r,
\]
for every \(n\ge m\). Equation (4) then proves the claimed upper bound and the strict uniqueness of its increasing-pattern maximizer.

**3. Closing the windows into a circle.** For fixed offset \(r\), as the cyclic window start traverses all \(n\) positions, its \(r\)-th marked index traverses every \(i\in\{1,\ldots,n\}\) once. Equation (1), valid unchanged for wrapped windows, and the *complete* sum (3) show that the sum of conditional probability deviations is \(n/m!-n/m!=0\). Summing over \(r\) yields \(\operatorname{Cov}(F,T_\sigma^{\mathrm{cyc}})=0\).

**4. Length-three classification.** Inserting \(m=3\) into (4), evaluating the three finite sums in (2), and simplifying yields the six formulas in the Finding section. For comparison of the negative candidates, the difference between the \(321\) covariance and that of \(231\) is \((5-n)/(2n(n-1))\), giving the exact minimizer threshold and its tie at \(n=5\).

## Verification

The standalone `verify.py` (Python standard library, no external data or packages) checks exact finite samples and the analytic identities. Run `python verify.py` in the directory containing this document. It independently enumerates permutations through \(n=7\), all length-2 through length-4 patterns allowed at those orders, both linear and cyclic windows, and all fixed-point locations; it also checks the binomial identities, boundary-penalty strictness, and six-pattern table over a larger parameter grid. The delivered checker passed 13,254 exact assertions. Exhaustive checks at finite \(n\) are corroboration; (1)–(4) are the all-parameter proof.

## Relationship to prior work

Foata and Han's *Fix-Mahonian Calculus III* (2007) gives joint enumeration involving fixed points, descents, excedances and major index, but does not state the rank-anchored all-length consecutive-pattern kernel. Elizalde and Noy's *Consecutive patterns in permutations: clusters and generating functions* (2012 conference proceedings; online article lists 2011) develops generating functions for occurrences and avoidance of consecutive patterns, without a fixed-point variable in the displayed generating function. Billey, Burdzy and Sagan (2012) enumerate peak sets, again without jointly fixing an absolute-position fixed point. Fulman, Kim and Lee (2019) study peaks in conjugacy classes, which supplies stronger cycle-structure context but not a position-resolved kernel for arbitrary consecutive patterns. A published fixed-point-versus-descent localization result establishes the length-two counterpart of the present statement; the claim here concerns all \(m\ge3\), the strict pattern extremizer and the cyclic orthogonality theorem. The length-two case is included in the formulas for completeness, not as a separately novel result.

## Limitations

The theorem concerns covariances only; zero covariance does not imply probabilistic independence. It applies to uniformly sampled permutations and not arbitrary nonuniform permutation laws. It does not classify the minimizing pattern for each general \(m\ge4\), nor provide higher mixed moments. Broad permutation-statistic generating functions may implicitly contain special cases of the formulas; the literature comparison is not a proof of first priority. Independent verification by an external mathematician has not occurred.

## References

1. D. Foata and G.-N. Han, *Fix-Mahonian Calculus III: A Quadruple Distribution*, arXiv:math/0703454v1, 15 March 2007, https://arxiv.org/abs/math/0703454.
2. S. Elizalde and M. Noy, *Consecutive patterns in permutations: clusters and generating functions*, DMTCS Proceedings AR (2012), https://doi.org/10.46298/dmtcs.3036.
3. S. Billey, K. Burdzy and B. Sagan, *Permutations with given peak set*, arXiv:1209.0693v1, 4 September 2012, https://arxiv.org/abs/1209.0693.
4. J. Fulman, G. B. Kim and S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class*, arXiv:1902.00978v1, 3 February 2019, https://arxiv.org/abs/1902.00978.
