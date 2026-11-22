# A birthday-scale Poisson law and exact saturation count for cyclic multinomial roughness

## Finding

Let \(n\ge 3\) and \(N\ge 1\). Draw \(N\) independent uniform categories from a labelled cycle of \(n\) categories, with counts \((X_1,\ldots,X_n)\) and \(X_{n+1}=X_1\). Define the cyclic discrete total variation and its *deficit from the largest possible value* by
\[
D_{n,N}=\sum_{i=1}^{n}|X_i-X_{i+1}|,
\qquad
T_{n,N}=N-\frac12D_{n,N}=\sum_{i=1}^{n}\min(X_i,X_{i+1}).
\]
The deficit takes nonnegative integer values. Set \(\lambda_{n,N}=N(N-1)/n\). For total-variation *distance between probability laws* defined as \(d_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|\),
\[
\boxed{
 d_{\mathrm{TV}}\!\left(\mathcal L(T_{n,N}),\operatorname{Poisson}(\lambda_{n,N})\right)
 \le \min\!\left\{1,\frac{N(N-1)(9N-16)}{n^2}\right\}.}
\]
For \(N=1\), both laws are the point mass at zero. At all positive integer sizes, there is also an exact finite formula for saturation:
\[
\boxed{
 \Pr(D_{n,N}=2N)
 =\frac{1}{n^N}\sum_{k=1}^{\min(N,\lfloor n/2\rfloor)}
 \frac{n}{n-k}\binom{n-k}{k}\,k!\,\left\{\!\begin{matrix}N\\k\end{matrix}\!\right\}.}
\]
Here the braces are Stirling numbers of the second kind; each displayed term is integral despite its rational-looking prefactor.

Consequently, as \(n\to\infty\):

- If \(N/\sqrt n\to c\in[0,\infty)\), then \(T_{n,N}\Rightarrow\operatorname{Poisson}(c^2)\), and \(\Pr(D_{n,N}=2N)\to e^{-c^2}\).
- If \(N/\sqrt n\to\infty\), with no upper restriction on \(N\), then \(\Pr(D_{n,N}=2N)\to0\).
- If \(\sqrt n\ll N\ll n^{2/3}\), then \((T_{n,N}-\lambda_{n,N})/\sqrt{\lambda_{n,N}}\Rightarrow \mathcal N(0,1)\). More generally, in the entire \(N=o(n^{2/3})\) range, the displayed finite Poisson comparison holds with error tending to zero, whether or not its Poisson parameter diverges.

The maximum-roughness event therefore has a sharp birthday-paradox onset at sample size of order \(\sqrt n\). The law of the *deficit* exhibits an explicitly controlled Poisson-to-Gaussian crossover.

## Assumptions and scope

Sampling is with replacement, uniform over the vertices of a simple cycle. The cycle is labelled, counts are not constrained to be distinct, and \(n\ge3\) excludes double counting of an edge in the two-vertex multigraph. The exact law and inequality hold for every finite \(n\ge3\) and every \(N\ge1\). The source article gives the cyclic statistic and its moment theory; the saturation and sparse, jointly growing sample/bin limits here concern different observables and asymptotic regimes.

The expression \(D_{n,N}=2N-2T_{n,N}\) is a deterministic identity. The upper bound \(2N\) is attained precisely when the set of occupied vertices is an independent set in the cycle; repeated observations at an occupied vertex are allowed.

## Proof

**Step 1 (deficit identity).** For nonnegative integers \(a,b\), \(|a-b|=a+b-2\min(a,b)\). Summing over cycle edges counts each occupancy twice and gives exactly \(T_{n,N}=\sum_i\min(X_i,X_{i+1})\). Thus \(D_{n,N}=2N\) if and only if no adjacent vertices are both occupied.

**Step 2 (exact saturation coefficient).** A cyclic independent vertex set of cardinality \(k\) can be chosen in
\[
 A(n,k)=\frac{n}{n-k}\binom{n-k}{k}
\]
ways, for \(1\le k\le\lfloor n/2\rfloor\). One proof counts cyclic binary strings with \(k\) isolated ones: the \(k\) positive gaps between ones sum to \(n-k\), giving \(n\binom{n-k-1}{k-1}/k=A(n,k)\). For each such support, the number of onto maps from the \(N\) labelled observations to its \(k\) vertices is \(k!\left\{\!\begin{smallmatrix}N\\k\end{smallmatrix}\!\right\}\). Dividing the sum by \(n^N\) yields the exact formula, with no asymptotic approximation.

**Step 3 (pair proxy and coupling).** Write the original sampled vertices as independent uniform \(Z_1,\ldots,Z_N\). Define
\[
 U_{n,N}=\sum_{1\le a<b\le N}\mathbf1\{Z_a\text{ and }Z_b\text{ lie at adjacent vertices of the cycle}\}.
\]
Counting pairs by occupancy gives \(U_{n,N}=\sum_i X_iX_{i+1}\). Consequently \(T_{n,N}\le U_{n,N}\) deterministically. Equality holds unless at least one edge has occupied endpoint counts not both equal to one. Such a mismatch requires three distinct sampled observations, two at one vertex and a third at a neighboring vertex. For each selection of the doubled unordered pair and a distinct third observation, either orientation is possible with combined probability \(2/n^2\). A union bound gives
\[
 \Pr(T_{n,N}\ne U_{n,N})
 \le 2\binom N2\frac{N-2}{n^2}
 =\frac{N(N-1)(N-2)}{n^2}.
\]
The same bound holds for \(\mathbb E(U_{n,N}-T_{n,N})\) using \(ab-\min(a,b)\le\binom a2b+a\binom b2\), and multinomial factorial moments.

**Step 4 (quantitative Poisson approximation).** The \(\binom N2\) indicators defining \(U_{n,N}\) have marginal probability \(p=2/n\) and mean \(\lambda_{n,N}=\binom N2p=N(N-1)/n\). In the dependency graph, a pair-indexed indicator has \(2N-3\) neighbors including itself, and \(2N-4\) distinct overlapping pair-indicators. For any two distinct pairs sharing one sampled observation, conditional independence given that observation and cyclic regularity give joint success probability \(p^2=4/n^2\). Disjoint pair indicators are independent from the entire collection outside this neighborhood. Thus the coefficients of the Arratia–Goldstein–Gordon Chen–Stein theorem are
\[
 b_1=\binom N2(2N-3)\frac4{n^2},\qquad
 b_2=\binom N2(2N-4)\frac4{n^2},\qquad b_3=0.
\]
Their Theorem 1, read in the present standard definition of \(d_{\mathrm{TV}}\) (one half of the norm used in that article), gives \(d_{\mathrm{TV}}(\mathcal L(U_{n,N}),\operatorname{Poisson}(\lambda_{n,N}))\le b_1+b_2\). Triangle inequality and the coupling bound give
\[
 d_{\mathrm{TV}}(\mathcal L(T_{n,N}),\operatorname{Poisson}(\lambda_{n,N}))
 \le\frac{N(N-1)[(N-2)+2(4N-7)]}{n^2}
 =\frac{N(N-1)(9N-16)}{n^2}.
\]
The trivial ceiling of one completes the finite bound. The theorem requiring positive Poisson mean is applied only for \(N\ge2\); \(N=1\) is immediate.

**Step 5 (all claimed regimes and threshold sharpness).** When \(N=o(n^{2/3})\), the right-hand error tends to zero. If \(N/\sqrt n\to c<\infty\), the Poisson parameter converges to \(c^2\), proving the asserted limit and saturation probability. If \(\sqrt n\ll N\ll n^{2/3}\), then \(\lambda_{n,N}\to\infty\), and the ordinary Poisson central limit theorem, combined with total-variation convergence under measurable normalization, proves the Gaussian limit. Finally, adding an observation can only increase every occupancy count and hence \(T_{n,N}\). For an arbitrary sequence \(N/\sqrt n\to\infty\), let \(M=\min\{N,\lfloor n^{7/12}\rfloor\}\). Then \(M/\sqrt n\to\infty\) and \(M=o(n^{2/3})\). The preceding Poisson comparison yields \(\Pr(T_{n,M}=0)\to0\); monotonicity gives \(\Pr(T_{n,N}=0)\le\Pr(T_{n,M}=0)\to0\). No further claims about the full law outside the stated approximation window are made.

## Verification

The standalone `verify.py` performs exhaustive labelled-sample enumeration at \(36\) pairs of finite cycle lengths and sample sizes (\(3\le n\le8\), \(1\le N\le6\)). It checks the exact deficit identity, nonnegative pair-proxy gap, zero-deficit Stirling/independent-set numerator, the exact pair-proxy mean, the triple-error bound and a multinomial-factorial-moment upper bound. It passed \(1{,}556{,}964\) counted assertions/arithmetic checks when executed from the standalone package. Those checks do **not** establish the all-size theorem or the infinite limits, which follow from the written proof and the cited Chen–Stein theorem. Reproduce with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Banić and Elezović, *Discrete total variation under the multinomial, Part 5: cyclic total variation* (arXiv:2611.14735v1, first public 10 November 2026), supply the cyclic statistic and establish its finite-sample covariance-block identities and large-sample fixed-bin variance expansions. Their §1–§3 and remarks on the remaining variance-monotonicity question were inspected. They do not state a Poisson law for the deficit under the jointly sparse \(N\asymp\sqrt n\) scaling or count the event \(D_{n,N}=2N\) by independent cyclic supports. Part 1 (arXiv:2610.13366v1) gives expectation identities, and mentions fixed-sample sparse asymptotics treated elsewhere; that priority possibility is noted below.

Arratia, Goldstein and Gordon, *Poisson Approximation and the Chen–Stein Method*, *Statistical Science* 5 (1990), 403–434, supply the **classical general theorem for locally dependent pair counts**, and discuss birthday coincidences in §4.1. This result is an essential cited premise and **not** claimed as new. The new, statistic-specific mathematical step is coupling the cyclic variation deficit to the adjacent-pair count by a controlled triple-occupancy error and deriving the exact finite independent-set/Stirling saturation formula. The general birthday theorem alone does not state those identities or the histogram-deficit conclusion.

A published result titled *Conditioning removes a leading variance term from multinomial histogram roughness* concerns \(N/n\to\lambda>0\) and a variance coefficient, with sparse-load **sequential** asymptotics. That regime and conclusion do not entail the full deficit distribution when \(N\asymp\sqrt n\). Only its publicly available summary was accessible for comparison; this is a priority limitation, not a claim of exhaustive inspection.

## Limitations

The Poisson total-variation bound is explicit but not claimed optimal, and it becomes uninformative when \(N\) is not \(o(n^{2/3})\). The Gaussian assertion is restricted to a proper subrange of growing sample sizes. The sharp threshold result outside that subrange concerns only the event of attaining maximal cyclic variation, not the full deficit law. Classical generalized-birthday and independent-set enumerations provide powerful antecedents; a historical equivalent in occupancy literature may exist. One earlier publication mentions a separate treatment of fixed-sample sparse asymptotics without identifying its full scope here. The contribution is a self-contained statistic-specific distributional and exact enumerative theorem, not a new general Chen–Stein method. No independent review has been performed.

## References

1. Nikola Banić and Neven Elezović, *Discrete total variation under the multinomial, Part 5: cyclic total variation*, arXiv:2611.14735v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14735.
2. Nikola Banić and Neven Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1 (first public 2026-10-09), https://arxiv.org/abs/2610.13366.
3. Richard Arratia, Larry Goldstein and Louis Gordon, *Poisson Approximation and the Chen–Stein Method*, *Statistical Science* 5 (1990), 403–434, https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/pacs-1.pdf.
4. *Conditioning removes a leading variance term from multinomial histogram roughness*, published result and synopsis at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conditioning-removes-a-leading-variance-term-from-multinomial-hi--e29f4fd136bb.
5. John E. Connett, *When are there too many collisions? Variants of the birthday problem*, *Communications in Statistics—Theory and Methods* 53 (2024), 4487–4497, https://doi.org/10.1080/03610926.2023.2184186. Its available abstract supplies a broad background comparison, not a verified negative full-text result.
