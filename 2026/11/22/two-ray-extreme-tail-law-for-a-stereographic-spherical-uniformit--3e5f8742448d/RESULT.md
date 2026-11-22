# Two-ray extreme-tail law for a stereographic spherical uniformity statistic

## Finding

Let \(n\ge 2\) and let \(X_1,\ldots,X_n\) be independent, area-uniform points on the ordinary unit two-sphere \(\mathbb S^2\). For distinct indices set \(\Theta_{ij}=\arccos(X_i\cdot X_j)\) and \(Z_{ij}=\cot(\Theta_{ij}/2)\). For any fixed \(a\in[-1,1]\), define the centered, untruncated stereographic statistic of Fernández-de-Marcos and García-Portugués by

\[
T_n(a)=\frac2n\sum_{i<j}\left(Z_{ij}+\frac{a}{Z_{ij}}\right)-\frac{\pi(n-1)}2(1+a).
\]

The following are *fixed-sample* extremes, with \(n\) held constant while the threshold \(x\to\infty\). Write \(c_n=2(n-1)/n\), \(a_+=\max\{a,0\}\), and \(a_-=\max\{-a,0\}\). Then

\[
\boxed{\lim_{x\to\infty}x^2\Pr\{T_n(a)>x\}=c_n(1+a_+^2),\qquad
\lim_{x\to\infty}x^2\Pr\{T_n(a)<-x\}=c_na_-^2.}
\]

More strongly, for every integer \(k\ge1\) and every *fixed* list \(a_1,\ldots,a_k\in[-1,1]\), let \(\boldsymbol T_n=(T_n(a_1),\ldots,T_n(a_k))\), \(\boldsymbol1=(1,\ldots,1)\), and \(\boldsymbol a=(a_1,\ldots,a_k)\). For all continuous compactly supported functions \(f\) on \(\mathbb R^k\setminus\{0\}\),

\[
\boxed{\lim_{x\to\infty}x^2\mathbb E[f(\boldsymbol T_n/x)]
=c_n\int_0^\infty\!\frac{2\,dr}{r^3}\{f(r\boldsymbol1)+f(r\boldsymbol a)\}.}
\]

Terms with \(r\boldsymbol a=0\) contribute zero because \(f\) vanishes near the origin. The limiting extreme-tail measure thus lies on exactly the collision and antipodal rays, except when those rays coincide or the latter is absent. Consequently, for every \(0<p<2\), \(\mathbb E|T_n(a)|^p<\infty\), while \(\mathbb E|T_n(a)|^p=\infty\) for all \(p\ge2\). Its truncated second moment satisfies

\[
\mathbb E\big[T_n(a)^2\mathbf1\{|T_n(a)|\le x\}\big]
\sim\frac{4(n-1)}n(1+a^2)\log x.
\]

If \(q_{n,a}(1-\varepsilon)\) denotes any standard upper \((1-\varepsilon)\)-quantile, then

\[
q_{n,a}(1-\varepsilon)\sim\left(\frac{2(n-1)(1+a_+^2)}{n\varepsilon}\right)^{1/2},\qquad\varepsilon\downarrow0.
\]

These statements are not claims about a joint limit in \(n\) and the threshold.

## Assumptions and scope

The null distribution is exactly independent and uniform on \(\mathbb S^2\); the sample size is any fixed integer \(n\ge2\); the parameter \(a\in[-1,1]\) is deterministic, with no estimation or selection from the observations. All pair angles belong to \((0,\pi)\) almost surely, so all displayed sample statistics are finite almost surely. The vector formulation permits repeated parameter values. Its mode of convergence is vague convergence of measures on \(\mathbb R^k\setminus\{0\}\), tested against continuous compactly supported \(f\). The original paper's additive normalization and its \(2/n\) factor are retained exactly.

## Proof

**Step 1: exact one-pair law.** For independent uniform points \(X,Y\) on \(\mathbb S^2\), the dot product \(U=X\cdot Y\) is uniform on \([-1,1]\). Writing \(Z=\sqrt{(1+U)/(1-U)}\), one obtains, for \(z>0\),

\[
F_Z(z)=\Pr\{Z\le z\}=\frac{z^2}{1+z^2},\quad
\Pr\{Z>z\}=\frac1{1+z^2},\quad
f_Z(z)=\frac{2z}{(1+z^2)^2}.
\]

The reciprocal \(1/Z\) has the same law as \(Z\), and \(\mathbb EZ=\mathbb E(1/Z)=\pi/2\), by direct integration. Therefore the stated centering makes \(\mathbb ET_n(a)=0\). For any finite parameter vector, \((Z+a_j/Z)_{j=1}^k\) has two separate order-two tail mechanisms: \(Z\to\infty\) produces the ray \(\boldsymbol1\) and \(Z\to0\) produces \(\boldsymbol a\). Substitution in the exact distribution shows that the corresponding one-pair vague tail measure is

\[
\int_0^\infty 2r^{-3}\{\delta_{r\boldsymbol1}+\delta_{r\boldsymbol a}\}\,dr.
\]

**Step 2: independence sufficient for a single extreme pair.** For any two *distinct* unordered pairs of indices, the associated \(Z\)'s are independent. If the pairs are disjoint this follows from independent observations. If the pairs share an index, condition on the common point. The other two observations are independent and uniform, and rotational invariance makes each conditional \(Z\) law the same \(F_Z\), independent of the conditioning point. Thus independence also holds unconditionally. Full mutual independence of all pair variables is *not* asserted.

Consequently, with \(N=\binom n2\), each fixed pairwise-kernel vector \(Y_e=(Z_e+a_j/Z_e)_j\) satisfies \(\Pr\{\|Y_e\|>t\}=O(t^{-2})\), and for distinct pairs \(e\ne f\),

\[
\Pr\{\|Y_e\|>\eta t,\ \|Y_f\|>\eta t\}=O_\eta(t^{-4})
\]

for every \(\eta>0\). To prove the finite-sum vague limit, first fix a compactly supported continuous test function whose support has positive distance from the origin. Choose a small fixed separation threshold so that if all \(N\) vectors are below it after scaling, the test function vanishes. The probability of two vectors exceeding any smaller fixed threshold is \(O(t^{-4})\). On the remaining event, at most one vector is significant, and the sum of the other scaled vectors can be made arbitrarily small by reducing that threshold. Uniform continuity, plus a bound on the \(t^2\)-scaled probability that the significant vector exceeds the fixed separation threshold, makes the resulting expectation error arbitrarily small. Hence the tail measure of this *finite* pair sum is the sum of its individual tail measures. This argument uses neither unproved mutual independence nor a sample-size asymptotic theorem.

**Step 3: normalization and the two rays.** Each kernel is multiplied by \(2/n\); multiplying an index-two regularly varying vector by \(2/n\) multiplies its tail measure by \((2/n)^2\). There are \(N=n(n-1)/2\) pairs, so the overall multiplier is \(N(2/n)^2=2(n-1)/n=c_n\). The additive deterministic centering, divided by the extreme threshold, tends to zero and has no effect. This proves the displayed vector tail formula.

**Step 4: scalar tails and consequences.** For the scalar coordinate \(a\), the first ray points to \(+\infty\). The second contributes to the upper tail if and only if \(a>0\), with factor \(a^2\), and to the lower tail if and only if \(a<0\), again with factor \(a^2\). Integrating \(2r^{-3}\) above the appropriate ray threshold gives both displayed constants. For \(a\ge0\), \(T_n(a)\) is bounded below, and the lower-tail constant is zero. The combined absolute-tail constant is \(c_n(1+a^2)>0\); the tail-integral identity for moments proves finiteness precisely below order two. Finally,

\[
\mathbb E[T^2\mathbf1\{|T|\le x\}]
=2\int_0^x t\Pr\{|T|>t\}\,dt-x^2\Pr\{|T|>x\}
\]

and the order-two absolute-tail law give the logarithmic asymptotic. Regular-variation inversion of the positive tail gives the upper-quantile formula. No inference about finite-\(x\) relative error is required.

## Verification

The accompanying `checker.py` numerically integrates the exact one-pair density, checks the asymptotic constants using the *exact* one-pair tail formulas for seven parameter values at three thresholds, and independently simulates the fixed \(n=3\) spherical statistic at two large thresholds for three parameters. With its specified random seed it passes 64 checks. These are reproducibility and arithmetic sanity checks, not substitutes for the tail-measure proof. The argument proves an infinite-threshold limit for every fixed sample size; the simulation checks only finitely many settings.

## Relationship to prior work

Fernández-de-Marcos and García-Portugués (2024, arXiv:2405.13531, first posted 2024-05-22), Equation (2), introduce exactly this stereographic statistic, its parameter range and centering. Their Sections 3--5 and Appendix analyze Gegenbauer coefficients, the conventional null asymptotics for dimensions at least three, and test power; their discussion notes that on the two-sphere the untruncated statistic has infinite variance. They do not give the finite-sample *two-sided* extreme-tail constants, the joint two-ray measure, the logarithmic truncated-second-moment coefficient, or an extreme-quantile law here. The previous infinite-variance observation is not asserted as new.

Fernández-de-Marcos and García-Portugués (2023, arXiv:2304.04519, first posted 2023-04-10) analyze smooth-maximum and Poisson-kernel spherical tests, whose kernels are bounded at fixed tuning parameters; their exact null moments do not imply the singular stereographic extreme-tail law. Published and research-record searches were also compared against general heavy-tail U-statistic literature, spherical distance-tail results, and earlier work on this same statistic's *growing-sample* Gaussian normalization. A growing-\(n\) weak limit is not a fixed-\(n\), threshold-to-infinity tail theorem. The possibility of an earlier equivalent calculation in a broader regular-variation framework is not excluded by failed keyword searches.

## Limitations

The result treats the fixed \(n\), extreme-threshold regime only. It does not give a uniform approximation when \(n\to\infty\), finite-significance-level error bounds, optimal test power, nuisance-parameter effects, dependent observations, dimensions other than two, or independently certified historical priority. The null distribution is exactly uniform, and \(a\) is not data adaptive. Each individual realization is finite, even though the second moment is infinite. The second ray may coincide with the first or disappear for special parameter lists; "exactly two distinct rays" is not claimed universally.

## References

1. Fernández-de-Marcos, A. and García-Portugués, E. (2024). *A stereographic test of spherical uniformity*. Statistics & Probability Letters **215**, 110218. Earliest verified public preprint: 2024-05-22, https://arxiv.org/abs/2405.13531 ; https://doi.org/10.1016/j.spl.2024.110218.
2. Fernández-de-Marcos, A. and García-Portugués, E. (2023). *On new omnibus tests of uniformity on the hypersphere*. TEST **32**, 1508--1529. Public preprint: 2023-04-10, https://arxiv.org/abs/2304.04519 ; https://doi.org/10.1007/s11749-023-00882-x.
3. Bakhshizadeh, M. (2023). *Exponential tail bounds and Large Deviation Principle for Heavy-Tailed U-Statistics*. https://arxiv.org/abs/2301.11563. Its growing-sample large-deviation setting differs from the exact fixed-sample tail coefficients here.
