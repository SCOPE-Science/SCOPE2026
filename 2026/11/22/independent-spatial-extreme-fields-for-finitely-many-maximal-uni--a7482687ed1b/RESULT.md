# Independent spatial extreme fields for finitely many maximal uniform spacings

## Finding
Let \(U_1,\ldots,U_n\) be independent uniform points of \([0,1]\). Write \(U_{0:n}=0\), \(U_{n+1:n}=1\) and \(U_{1:n}<\cdots<U_{n:n}\) for their order statistics. For each fixed integer \(K\ge 1\) and \(1\le k\le K\), put
\[
b_{n,k}=\log n+(k-1)\log\log n-\log((k-1)!),\qquad n\ge3,
\]
\[
\Xi_{n,k}=\sum_{i=0}^{n+1-k}\delta_{\big(i/n,\ n(U_{i+k:n}-U_{i:n})-b_{n,k}\big)}.
\]
As \(n\to\infty\), the \(K\) point processes jointly converge in the vague topology on \([0,1]\times\mathbb R\) to **mutually independent** Poisson point processes, each with intensity \(dt\,e^{-x}\,dx\). In particular, if
\[
M_n^{(k)}=\max_{0\le i\le n+1-k}(U_{i+k:n}-U_{i:n}),
\]
then for all \(x_1,\dots,x_K\in\mathbb R\),
\[
\lim_{n\to\infty}\Pr\left\{nM_n^{(k)}-b_{n,k}\le x_k\text{ for all }1\le k\le K\right\}
=\exp\left(-\sum_{k=1}^{K}e^{-x_k}\right).
\]
Furthermore, the rescaled location of a maximizing \(k\)-spacing (the index of its left endpoint divided by \(n\)) is asymptotically uniform on \([0,1]\); jointly across \(k\), these locations and the centered maxima are independent in the limit. The same location conclusion holds using the original coordinate \(U_{i:n}\) in place of \(i/n\).

## Assumptions and scope
All points are independent and exactly uniform on a fixed interval. The number \(K\) of window lengths is finite and fixed before \(n\to\infty\), and every \(k\) is a fixed positive integer. The ordinary endpoint spacings are included. The maximum is almost surely unique for each \(k\); arbitrary deterministic tie-breaking would also be harmless. Vague convergence is understood on the locally compact space \([0,1]\times\mathbb R\), with finite intensity on each compact strip in height. This is a **joint** theorem: individually convergent Gumbel marginals alone do not establish independence across lengths or spatial convergence.

## Proof
**1. Exponential representation and normalization.** Let \(E_1,\ldots,E_{n+1}\) be independent mean-one exponentials, \(T=\sum_{j=1}^{n+1}E_j\), and \(W_{i,k}=\sum_{j=i+1}^{i+k}E_j\). The complete vector of uniform spacings has the distribution of \((E_j/T)_{j=1}^{n+1}\). The unnormalized family at length \(k\) therefore has marks \(W_{i,k}-b_{n,k}\). As \(n/T-1=O_{\Pr}(n^{-1/2})\) and \(\max_{j\le n+1}E_j=O_{\Pr}(\log n)\), uniformly across all \(i\) and \(k\le K\),
\[
\left|\frac{n}{T}W_{i,k}-W_{i,k}\right|
\le K\left|\frac nT-1\right|\max_j E_j=o_{\Pr}(1).
\]
Also \(\max_{0\le i\le n+1}|U_{i:n}-i/n|=o_{\Pr}(1)\) (with the obvious endpoint convention), so the location parametrizations agree asymptotically.

**2. One-window probability.** Since \(W_{i,k}\) has a \(\operatorname{Gamma}(k,1)\) law,
\[
\Pr(W_{i,k}>z)=e^{-z}\sum_{j=0}^{k-1}\frac{z^j}{j!}
\quad(z>0),\qquad
n\Pr(W_{i,k}>b_{n,k}+x)\longrightarrow e^{-x}.
\]
Consequently the normalized marks in any fixed bounded height interval have asymptotic probability equal to the integral of \(e^{-x}dx\), divided by \(n\).

**3. Distinct overlapping windows are asymptotically negligible.** Consider two distinct length-\(k\) and length-\(\ell\) windows that share exactly \(h\ge1\) exponential variables. Write their sums as \(G_h+H_{k-h}\) and \(G_h+H'_{\ell-h}\), where all three terms are independent and a shape-zero gamma variable is zero. For thresholds \(a=b_{n,k}+x\), \(b=b_{n,\ell}+y\), both exceedance events imply
\[
G_h+\frac{H_{k-h}+H'_{\ell-h}}2>\frac{a+b}2=:z.
\]
The final summand \(R=(H_{k-h}+H'_{\ell-h})/2\) satisfies \(\mathbb E e^R=2^{k+\ell-2h}<\infty\). Splitting according to \(R\le z\) or \(R>z\), and using the elementary gamma-tail estimate, gives, for fixed window sizes,
\[
\Pr(G_h+R>z)\le C_{k,\ell,h}e^{-z}(1+z)^{h-1}.
\]
For fixed bounded \(x,y\), this is
\[
O\!\left(\frac1n(\log n)^{h-(k+\ell)/2}\right)
=O\!\left(\frac1{n\sqrt{\log n}}\right).
\]
Indeed, since the two supports are not identical, \(2h\le k+\ell-1\); the exponent is at most \(-1/2\). For disjoint supports the corresponding windows are exactly independent. The same estimates apply to events specifying a mark in any bounded height interval, since these are bounded by the corresponding lower-threshold exceedance events.

**4. Mixed factorial moments.** Consider finitely many pairwise disjoint space-height rectangles separately marked by window length and form any fixed mixed factorial moment of their point counts. In the expansion over indexed windows, group each chosen window together with every other selected window whose exponential supports overlap. A tuple with \(c\) support-connected components has \(O(n^c)\) possible placements, where the implied constant depends only on the fixed total moment order and \(K\). Different components involve disjoint exponential families and are independent. A singleton component has joint event probability \(O(n^{-1})\); a component of at least two distinct windows has probability at most the bound from step 3, \(O(1/(n\sqrt{\log n}))\). Therefore the total contribution of all tuples having any overlap is \(O((\log n)^{-1/2})\). For tuples with pairwise disjoint supports, factorization is exact, and the admissible start positions form Riemann sums; their limits are products of the rectangle intensity measures. Thus every mixed factorial moment converges to that of **independent** Poisson counts. Their exponential moment determinacy, together with finite-dimensional tightness, proves convergence of the marked point process. Approximation by disjoint rectangles extends the claim to the vague topology.

**5. Maxima and locations.** The intensity of exceedance points above height \(x\) is \(e^{-x}\); the Poisson void probability gives the stated independent Gumbel law. The expected number of points above height \(R\) is asymptotically \(e^{-R}\), ruling out escape to \(+\infty\); Poisson void probabilities at large negative thresholds rule out escape to \(-\infty\) for the maximal point. Uniqueness of each limiting highest point and the product intensity identify its location as uniform and independent of its height and all other length-labelled fields. Continuous mapping then gives the joint maximum-location statement.

## Verification
Run `python3 checks/verify.py` with the Python 3 standard library. Its 529 deterministic assertions verify gamma-tail identities and derivatives, the strict half-logarithm loss in every overlapping-window type through length eight, exact analytic formulas for three small overlapping-window configurations, decreasing numerical rare-pair rates, one-window tail normalization, and finite exhaustive counts of disjoint windows. These tests check finite ingredients rather than certifying the infinite point-process theorem; steps 3–5 above provide the asymptotic argument.

## Relationship to prior work
Mijatović and Vysotsky (arXiv:1508.00944, initially public 2015-08-05; subsequently published 2016) establish the marginal maximal \(k\)-spacing Gumbel theorem for each fixed \(k\). Their proof uses Watson's 1954 theorem for a **single** stationary \(m\)-dependent sequence; their asymptotic independence observation concerns the parity-separated length-two windows, not windows of different lengths. This finding instead establishes a simultaneous independent, spatially marked Poisson limit for an arbitrary finite family of **different** fixed \(k\)-spacing lengths. Dembo and Karlin's 1992 \(r\)-scan Poisson approximation, and Roos's 1993 compound-Poisson work on extreme spacings, are close methodological precedents. Their accessible abstracts do not resolve the precise cross-length marked-field claim; the complete articles were not available for a definitive historical comparison. Published mathematical-finding searches covering multi-length maximal spacings, sliding Gamma windows, joint Gumbel maxima and spatial Poisson fields found no directly equivalent or dominating assertion. This is a best-knowledge priority assessment, not proof of worldwide novelty.

## Limitations
The limit is for fixed \(K\), not a sequence of growing window lengths, and for exact uniform observations. It does not assert finite-sample independence, a quantitative process-level error rate, or a result for arbitrary parent densities. A general earlier marked extreme-process theorem may imply this result after verification of its overlap hypotheses; historical priority therefore remains subject to an independent literature audit.

## References
- A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944v1 (2015-08-05), https://arxiv.org/abs/1508.00944; *Advances in Applied Probability* 48A (2016), 235–238.
- G. S. Watson, *Extreme values in samples from m-dependent stationary stochastic processes*, *Annals of Mathematical Statistics* 25 (1954), 798–800.
- A. Dembo and S. Karlin, *Poisson approximations for r-scan processes*, *Annals of Applied Probability* 2 (1992), DOI:10.1214/aoap/1177005707.
- B. Roos, *Compound Poisson approximations for the numbers of extreme spacings*, *Journal of Applied Probability* (1993), DOI:10.2307/1427795.
