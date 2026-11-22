# A sharp mode count with almost-equal price peaks in exponential-mixture markets

## Finding

**Theorem.** Let \(n\geq1\) be an integer, let \(0<\lambda_1<\cdots<\lambda_n\), and let \(w_j>0\) with \(\sum_{j=1}^{n}w_j=1\). For a single zero-cost product sold at the nonnegative uniform price \(p\), suppose segment \(j\) purchases with probability \(e^{-\lambda_j p}\). Its expected revenue is
\[
R(p)=p\sum_{j=1}^{n}w_j e^{-\lambda_jp},\qquad p\geq0.
\]
Then \(R\) has at most \(n\) strict local maxima on \((0,\infty)\). This bound is sharp **with near-equal peaks**: for every \(n\geq1\) and \(\varepsilon>0\), there are such rates and weights with exactly \(n\) distinct nondegenerate local maxima whose largest and smallest revenue values differ by a factor less than \(1+\varepsilon\). The parameter choices persist as \(n\) local maxima under sufficiently small perturbations of rates and weights (without claiming that near-equal ratios are invariant under a fixed arbitrary perturbation).

An explicit simultaneous construction takes any sufficiently large integer \(L\geq400\) and the \(n\) rates \(\lambda_j=L^j\), \(j=0,\ldots,n-1\), with weights \(w_j=L^j/W\) where \(W=\sum_{k=0}^{n-1}L^k\). Each local maximum lies in the disjoint price window
\[
I_j=\left(\frac1{2L^j},\frac3{2L^j}\right).
\]
Writing \(H_j\) for its revenue and defining
\[
\Delta_L=\frac{3}{2(L-1)}+\frac{e^{-L/4}}{2(1-e^{-L/4})},
\]
we prove the uniform, dimension-free bounds
\[
\frac1{eW}\le H_j\le\frac{1/e+\Delta_L}{W},\qquad
\frac{\max_j H_j}{\min_j H_j}\le1+e\Delta_L.
\]
At \(L=400\), this upper bound is less than \(1.011\), for **every** \(n\). Letting \(L\) grow establishes the arbitrary-\(\varepsilon\) assertion.

## Assumptions and scope

There is exactly one price and one market period, no capacity restriction, no price discrimination, no fixed or marginal costs, and a unit mass of buyers. Segment weights are strictly positive and sum to one; buyers' willingness-to-pay survival functions are exponential with strictly distinct positive rates. The theorem is deterministic expected-revenue optimization, not a probabilistic statement about realized finite-sample sales. A local maximum means a strict two-sided local maximum at an interior positive price; *nondegenerate* means the revenue's second derivative is strictly negative there. The sharpness statement quantifies independently over every finite integer \(n\) and every \(\varepsilon>0\), and does not claim that every choice of rates and weights has \(n\) maxima. The weak inequalities in the displayed height bound remain true at finite \(L\); the strict target \(1+\varepsilon\) follows by choosing \(L\) with \(e\Delta_L<\varepsilon\).

## Proof

**A. General zero-count lemma.** A nonzero real exponential polynomial
\[
F(p)=\sum_{j=1}^{m}(a_j+b_jp)e^{-\mu_jp}
\]
with distinct real exponents \(\mu_j\) has at most \(2m-1\) real zeros **counted with multiplicity**. To prove this, first discard any identically zero terms. When \(m=1\), multiplication by a nowhere-zero exponential leaves one nonzero affine polynomial, which has at most one zero. Assume the statement through \(m-1\) and multiply \(F\) by \(e^{\mu_1p}\), writing
\[
G(p)=(a_1+b_1p)+\sum_{j=2}^{m}(a_j+b_jp)e^{-(\mu_j-\mu_1)p}.
\]
The second derivative \(G''\) has at most \(m-1\) distinct exponential modes, still each with an affine coefficient, so by induction it has at most \(2m-3\) zeros if nonzero. Generalized Rolle's theorem, including multiplicities, says that a twice-differentiable function with \(N\) zeros counted with multiplicity has a second derivative with at least \(N-2\) zeros. Thus \(N\le 2m-1\). If \(G''\equiv0\), then the nonzero \(G\) is affine and has at most one zero. This completes induction; multiplication by a positive exponential preserves all zero multiplicities. The same argument applies on any finite interval, and hence on the whole real line by selecting a finite interval containing any hypothetical excess of zeros.

For the model,
\[
R'(p)=\sum_{j=1}^{n}w_j(1-\lambda_jp)e^{-\lambda_jp}.
\]
It is not identically zero because \(R'(0)=1\). Thus it has at most \(2n-1\) zeros counted with multiplicity. If there were \(n+1\) strict interior local maxima, the extreme-value theorem and strictness near each maximum would require an interior stationary minimum between each successive pair, giving at least \(2n+1\) distinct derivative zeros, a contradiction. Therefore there are at most \(n\) interior strict maxima.

**B. Signs creating the maximum possible number of peaks.** Use the announced geometric rates and, until the last step, omit the common positive normalizer \(W\). Set
\[
S(p)=p\sum_{k=0}^{n-1}L^k e^{-L^kp},\quad
S'(p)=\sum_{k=0}^{n-1}L^k(1-L^kp)e^{-L^kp}.
\]
At the right endpoint \(p=3/(2L^j)\), the term \(k=j\) equals \(-L^je^{-3/2}/2\); terms \(k>j\) are negative; and terms \(k<j\) are positive, each strictly smaller than \(L^k\). Their total is less than \(L^j/(L-1)\). Hence
\[
S'\left(\frac3{2L^j}\right)
<L^j\left[-\frac{e^{-3/2}}2+\frac1{L-1}\right]<0
\]
for \(L\geq400\).

At the left endpoint \(p=1/(2L^j)\), the own term is \(+L^je^{-1/2}/2\), and every slower-rate term is positive. For a faster rate \(k=j+m\), \(m\ge1\), its negative contribution in absolute value is at most
\[
\frac{L^j}{2}(L^m)^2 e^{-L^m/2}
\le\frac{L^j}{2}e^{-L^m/4}.
\]
The last inequality follows from \(2\log t\le t/4\) for \(t\ge400\). Since \(L^m\ge mL\), the sum of such terms is bounded by \(L^je^{-L/4}/[2(1-e^{-L/4})]\). It is smaller than the own positive term, giving
\[
S'\left(\frac1{2L^j}\right)>0.
\]
Consequently there is a strict interior maximizer in each \(I_j\). These intervals are disjoint since \(L>3\). Between successive windows the derivative has to change from negative to positive, creating at least \(n-1\) other zeros. There are therefore at least \(2n-1\) distinct zeros of \(S'\), while Part A allows at most \(2n-1\), including multiplicity. Hence all zeros are simple, the \(n\) windows contain exactly one stationary maximum each, all maxima have strictly negative second derivative, and there are no additional extrema. Dividing \(S\) by \(W\) preserves this classification. Simple zeros persist under sufficiently small coefficient and rate perturbations by continuity and the implicit-function theorem; each fixed \(n\) admits an open neighborhood of parameters maintaining \(n\) strict maxima (and Part A precludes further maxima).

**C. Almost-equal heights, uniformly in the number of segments.** For each \(j\), the point \(p=1/L^j\in I_j\) yields its own revenue contribution exactly \(1/e\) in \(S\), so the peak \(M_j=\max_{p\in I_j}S(p)\) is at least \(1/e\). For every \(p\in I_j\), the own term \(L^jp e^{-L^jp}\) is at most \(1/e\). Slower-rate terms collectively satisfy
\[
\sum_{k<j}pL^k e^{-L^kp}\le \sum_{m\ge1}\frac{3}{2L^m}
=\frac3{2(L-1)}.
\]
For faster rates, \(L^kp\ge L^{k-j}/2\ge200\). As \(u e^{-u}\) decreases for \(u\ge1\), each faster contribution is at most \((L^m/2)e^{-L^m/2}\), bounded by \(e^{-L^m/4}/2\) using \(\log t\le t/4\) for \(t\ge400\). Summing over \(m\ge1\) and using \(L^m\ge mL\) bounds the sum by \(e^{-L/4}/[2(1-e^{-L/4})]\). Thus
\[
1/e\le M_j\le1/e+\Delta_L
\]
for every \(j\) and \(n\). Finally \(H_j=M_j/W\), so the revenue ratio is at most \(1+e\Delta_L\). Since \(\Delta_L\to0\) as \(L\to\infty\), the ratio can be arbitrarily close to one. This completes the theorem.

## Verification

The accompanying standalone standard-library `verify.py` evaluates the announced derivative signs, brackets each peak in the prescribed window for \(n=1,\ldots,8\) at \(L=400\), tests the stated height bounds, and explores 1,200 other randomly generated heterogeneous-rate markets on a numerical grid. It reports **1,693 finite assertions passed**. For an illustrative three-segment market, the unnormalized rate coefficients are \((1,400,160000)\); the three local maxima occur near \(1\), \(0.002517\), and \(0.000006293\), all near the unnormalized revenue \(1/e\), with the exact revenue scaling factor \(W=160401\). To reproduce the calculation run `python3 verify.py` in the directory containing the two files. The zero-count lemma and the all-\(n\) existence and height properties are **proved analytically**, not inferred from the finite checks.

## Relationship to prior work

Kunz and Crone (2014), particularly their survey section on exponential demand curves, give direct retail-pricing motivation. Aksoy-Pierson, Allon and Federgruen (2013) demonstrate the importance of nonquasiconcavity for heterogeneous multinomial-logit pricing, but their model and competitive objectives are distinct. Hetrakul and Cirillo (2014) examine latent-class choice and railway pricing with seat allocations; the inspected model is not this hyperexponential single-price curve. Published published-finding corpus work on the **two-exponential** market proves a sharp two-mode bifurcation and global-price switch; the present result agrees with its \(n=2\) cap, does not replace its two-class parameter phase diagram, and adds an all-\(n\) sharp cap and all-\(n\) near-equal construction. Another published published-finding corpus result constructs arbitrarily many local optima for a **finite-mixture logit** model with common price sensitivity. Its different purchase-law family gives neither the exponential-mixture upper bound nor the near-equal-height property. The exponential-polynomial zero-count lemma is a classical extended-Chebyshev-system technique; originality is asserted only for its motivated combined application and sharp height construction, not for the lemma itself. Exact theorem priority remains provisional in the broader historical mixture-pricing and exponential-polynomial literature.

## Limitations

The construction's rate ratios and segment weights can be extremely dispersed, so near-equal theoretical maxima may be hard to resolve from finite noisy data. The result says at most \(n\) interior *strict* local maxima; it does not claim \(n\) global maxima or enumerate globally optimal posted prices, or derive an efficient stable algorithm for empirical optimization. It does not cover positive marginal costs, non-exponential valuations, correlated demand shocks, capacity constraints, multiple products, dynamic prices, or alternative demand normalization. The near-equality is an existence construction, not a universal conclusion for arbitrary markets. Historical originality has not been independently certified; broad analytic mixture literature may contain equivalent formulations.

## References

1. M. Aksoy-Pierson, G. Allon, and A. Federgruen, “Price Competition Under Mixed Multinomial Logit Demand Functions,” *Management Science* 59(8), 1817–1835, first published online 2013-04-22. DOI: https://doi.org/10.1287/mnsc.1120.1664. Author-hosted full text: https://tuck.dartmouth.edu/uploads/content/SSRN-id2405684.pdf.
2. T. P. Kunz and S. F. Crone, “Demand models for the static retail price optimization problem – A Revenue Management perspective,” *SCOR*, first public 2014-08-06. DOI: https://doi.org/10.4230/OASIcs.SCOR.2014.101. Full text: https://drops.dagstuhl.de/storage/01oasics/oasics-vol037-scor2014/OASIcs.SCOR.2014.101/OASIcs.SCOR.2014.101.pdf.
3. P. Hetrakul and C. Cirillo, “A latent class choice based model system for railway optimal pricing and seat allocation,” *Transportation Research Part E* 61 (2014), 68–83. DOI: https://doi.org/10.1016/j.tre.2013.10.005. Author full text: https://cinziacirillo.weebly.com/uploads/5/3/6/0/53607733/tre-hc14.pdf.
4. “Sharp two-segment price bifurcation and discontinuous optimal uniform pricing,” published-finding corpus published record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-two-segment-price-bifurcation-and-discontinuous-optimal-un--7b04ad2cc534.
5. “Arbitrarily many local price optima in a one-product common-slope logit mixture,” published-finding corpus published record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arbitrarily-many-local-price-optima-in-a-one-product-common-slop--408fceb9bc2a.
