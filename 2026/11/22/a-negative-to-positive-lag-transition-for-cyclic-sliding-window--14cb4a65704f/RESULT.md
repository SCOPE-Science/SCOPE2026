# A negative-to-positive lag transition for cyclic sliding-window maxima

## Finding
For each integer \(k\ge2\), let \(X_0,\ldots,X_{n-1}\) be independent identically distributed real random variables with a common continuous law on a circle, where \(n\ge2k+2\). Write \(W_i\) for the *index* of the unique maximum among \(X_i,\ldots,X_{i+k-1}\), with indices read modulo \(n\). Put \(I_i=\mathbf1\{W_i\ne W_{i+1}\}\), and \(T_{n,k}=\sum_{i=0}^{n-1}I_i\). The latter also counts the distinct sample indices that appear as maximizers of the cyclic width-\(k\) windows.

The exact lag covariance of adjacent-window changes has a unique sign reversal:
\[
\operatorname{Cov}(I_i,I_{i+d})=
\begin{cases}
-\dfrac{4d}{(k+1)^2(k+d+1)},&1\le d<k,\\[4pt]
\dfrac{(k-1)^2}{(k+1)^2(2k+1)},&d=k,\\[4pt]
0,&k<d<n-k,
\end{cases}
\]
with remaining lags obtained by \(d\leftrightarrow n-d\). In particular, every shorter positive lag is *negatively* correlated, but at lag exactly \(k\) the covariance becomes *strictly positive*.

The count has exact mean and variance
\[
\mathbb ET_{n,k}=\frac{2n}{k+1},\qquad
\operatorname{Var}(T_{n,k})=nv_k,
\]
where, setting \(H_m=\sum_{j=1}^{m}j^{-1}\),
\[
v_k=\frac2{k+1}-\frac{4(2k+1)}{(k+1)^2}
+\frac8{k+1}(H_{2k+1}-H_{k+1})+\frac2{2k+1}.
\]
For all \(k\ge2\), \(v_k>\frac{2k(k-1)}{3(k+1)^2(2k+1)}>0\). Moreover, \(kv_k\to8\log2-5\) as \(k\to\infty\). For each *fixed* \(k\ge2\), as \(n\to\infty\),
\[
\frac{T_{n,k}-2n/(k+1)}{\sqrt{nv_k}}\ \xrightarrow{d}\ N(0,1).
\]
The original contribution assessed here is the complete *position-resolved change-indicator covariance*, its sign reversal, and the cyclic exact variance; no priority is claimed for the earlier-known linear total-count distribution.

## Assumptions and scope
The observations are independent and identically distributed with a continuous real-valued common law, so all maxima are almost surely unique and their relative order is uniform. The sample lies on a labeled cycle of length \(n\); window width \(k\) is an integer satisfying \(k\ge2\) and \(n\ge2k+2\). The central limit theorem holds at each fixed \(k\) as \(n\to\infty\), not uniformly over growing widths. The transition concerns *index changes*, not equality of maximum values when ties can occur; it does not cover nonidentically distributed or dependent observations.

## Proof
For a window shift from \(i\) to \(i+1\), a change occurs exactly if the largest observation of the union \(\{i,\ldots,i+k\}\) lies at one of its two ends. This establishes \(\mathbb EI_i=2/(k+1)\). For any fixed index \(j\), all the width-\(k\) windows won by \(j\) form one contiguous interval in cyclic window-start order: if \(j\) wins two windows, it beats each competitor in their union and hence wins all intermediate windows containing \(j\). Thus every distinct winning index contributes one transition, proving the count interpretation.

For a lag \(1\le d\le k\), the unions of the two adjacent-window pairs are \(A=\{0,\ldots,k\}\) and \(B=\{d,\ldots,d+k\}\). Their union comprises \(k+d+1\) distinct observations. To have \(I_0=I_d=1\), the maximum of \(A\) must be at \(0\) or \(k\), while that of \(B\) must be at \(d\) or \(d+k\). For \(d<k\), the choice \((k,d)\) is impossible, because its two distinct vertices belong to the intersection and would have to exceed each other. Of the remaining choices, \((0,d)\) and \((k,d+k)\) each have probability \(1/[(k+1)(k+d+1)]\): the first chosen end must be the global maximum in the union and the other must be maximal among the remaining points of its window. Choice \((0,d+k)\) has twice that probability, according to which end is greatest in the union. Hence for \(1\le d<k\),
\[
\Pr(I_0=I_d=1)=\frac{4}{(k+1)(k+d+1)}.
\]
When \(d=k\), the previously incompatible interior choices coincide at vertex \(k\); their additional joint probability is \(1/(2k+1)\), as vertex \(k\) must be greatest throughout the union. Therefore
\[
\Pr(I_0=I_k=1)=\frac4{(k+1)(2k+1)}+\frac1{2k+1}.
\]
Subtracting \((2/(k+1))^2\) yields exactly the displayed covariance kernel. If \(k<d<n-k\), the two length-\(k+1\) determining intervals are disjoint, implying independence. The other lags follow by stationarity and reversing the pair.

Since \(n\ge2k+2\), each site has exactly two distinct partners at each circular separation \(1,\ldots,k\). Summing covariance over all ordered pairs gives
\[
\operatorname{Var}(T_{n,k})=n\left(\frac{2(k-1)}{(k+1)^2}+2\sum_{d=1}^{k-1}\frac{-4d}{(k+1)^2(k+d+1)}+\frac{2(k-1)^2}{(k+1)^2(2k+1)}\right).
\]
Evaluating the harmonic sum gives the stated \(v_k\). The \(k\) reciprocals in \(H_{2k+1}-H_{k+1}\) have denominators with arithmetic mean \(3(k+1)/2\), so strict Jensen inequality gives
\(H_{2k+1}-H_{k+1}>2k/[3(k+1)]\) for \(k\ge2\). Inserting this bound produces the stated strict positive lower bound. The asymptotic \(kv_k\to8\log2-5\) follows from the harmonic-number expansion.

For fixed \(k\), on a linear sequence the indicators depend on \(k+1\) consecutive independent observations and hence form a stationary, bounded, \(k\)-dependent process. Split into large blocks separated by gaps of length \(k\), apply the elementary independent-block central limit theorem, and let block size grow sufficiently slowly; the positive long-run variance is exactly \(v_k\). The linear and cyclic sums differ by at most \(O(k)\) terms, which is negligible after normalization by \(\sqrt n\). This proves the stated cyclic CLT.

## Verification
The independent-implementation standalone script `verify.py` enumerates every relative ordering of the \(k+d+1\) observations determining the joint pair event for \(2\le k\le4\), \(1\le d\le k\). It also enumerates all entire cyclic permutations for \((k,n)=(2,7),(3,8),(4,9)\), checking exact rational means and variances. Symbolic rational tests confirm both variance formula representations and the covariance sign classification for \(2\le k\le14\). The script reports 76 passed assertions. This finite enumeration is a cross-check only; the general law and CLT are proved above.

## Relationship to prior work
Austin, Fagen, Lehrer, and Penney (1957) already gave the distribution of the number of locally maximal elements generated by sliding windows in a *linear* sample. In particular the linear total-count expectation \((2n-k+1)/(k+1)\) is known. This result does **not** claim the count object or its linear full distribution as new. The new comparison is the all-lag covariance of the constituent change indicators in a *cyclic* sample, including the reversal from negative short-lag dependence to a positive full-window lag, which is not determined merely by a scalar marginal total-count law. Alon and Feldheim (2014) establish general uniform bounds for runs in finite-range sliding-window processes, rather than the stated exact rank-specific covariance kernel. Earlier linear distribution results could imply portions of the aggregate moments; the position-resolved kernel is the central distinct claim.

## Limitations
The 1957 original paper's full text was not available for a conclusive page-by-page priority comparison; a faithful published mathematical restatement was inspected instead. Thus the exact lag-resolved result should undergo independent historical-priority review before any publication claim. The statements apply only to continuous iid inputs, fixed integer window widths for the CLT, and cycles with \(n\ge2k+2\). The script checks finitely many sizes and cannot establish the general theorem or independence under different sampling models.

## References
1. J. P. Austin, R. E. Fagen, M. A. Lehrer and W. F. Penney, *The Distribution of the Number of Locally Maximal Elements in a Random Sample*, Annals of Mathematical Statistics **28** (1957), 786–790. https://doi.org/10.1214/aoms/1177706893 . Accessible expository statement: https://www.theoremoftheday.org/Statistics/PermLocalMax/TotDPermLocalMax.pdf .
2. N. Alon and O. N. Feldheim, *A note on general sliding window processes*, 2014, arXiv:1402.1975, https://arxiv.org/abs/1402.1975 ; published in *Electronic Communications in Probability* **19** (2014), https://doi.org/10.1214/ECP.v19-3341 .
