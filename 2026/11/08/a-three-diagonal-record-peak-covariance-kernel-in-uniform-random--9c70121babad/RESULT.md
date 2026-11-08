# A three-diagonal record–peak covariance kernel in uniform random permutations

## Finding

Let \(\pi\) be uniform on \(S_n\), where \(n\ge3\). Write
\[
R_i=\mathbf1\{\pi_i=\max(\pi_1,\ldots,\pi_i)\},\qquad
P_j=\mathbf1\{\pi_{j-1}<\pi_j>\pi_{j+1}\},
\]
for \(1\le i\le n\) and \(2\le j\le n-1\). The exact cross-covariance kernel is
\[
\boxed{\operatorname{Cov}(R_i,P_j)=
\begin{cases}
\dfrac{2-j}{3(j-1)(j+1)},&i=j-1,\\[3pt]
\dfrac{2j-1}{3j(j+1)},&i=j,\\[3pt]
-\dfrac1{3(j+1)},&i=j+1,\\[3pt]
0,&\text{otherwise}.
\end{cases}}
\]
Thus the full \(n\)-by-\((n-2)\) matrix has only three diagonals. For each eligible peak position, a precise cancellation gives
\[
\boxed{\operatorname{Cov}\left(\sum_{i=1}^nR_i,P_j\right)
=\frac1{3j(j-1)(j+1)}>0.}
\]
The total number of records \(R=\sum_iR_i\) and the number of interior peaks \(P=\sum_{j=2}^{n-1}P_j\) satisfy
\[
\operatorname{Cov}(R,P)=\frac{(n-2)(n+1)}{12n(n-1)}
\xrightarrow[n\to\infty]{}\frac1{12}.
\]
The central contribution is the **position-resolved sparse kernel**, not a claim of novelty for the aggregate count covariance, which can be recovered from previously established joint generating functions.

## Assumptions and scope

All \(n!\) permutations have equal probability. Records are strict left-to-right maxima, counting position one. Peaks are strictly interior local maxima, so neither endpoint is a peak. The formula holds for all integers \(n\ge3\), every \(i\in\{1,\ldots,n\}\), and every \(j\in\{2,\ldots,n-1\}\). Ties never occur.

## Proof

Represent \(\pi\) by the relative ranks of independent continuous identically distributed observations \(X_1,\ldots,X_n\). The record event at \(i\) has probability \(1/i\), and each interior peak has probability \(1/3\).

**Case \(i\le j-2\).** The record event is measurable with respect to \(X_1,\ldots,X_i\), whereas the peak event uses only \(X_{j-1},X_j,X_{j+1}\). These sets are disjoint, giving zero covariance.

**Case \(i\ge j+2\).** Conditional on the unordered multiset \(\{X_1,\ldots,X_{i-1}\}\), the relative ordering of the first \(i-1\) observations is uniform and independent of \(X_i\). In particular, the peak event at \(j\) depends only on this ordering, while the probability that \(X_i\) exceeds its maximum is a function only of the unordered values. Hence the events are independent, giving zero covariance. This is the rank-order independence step that produces all distant zero entries.

**Case \(i=j-1\).** Two successive upper-record events have probability \(1/((j-1)j)\). Given both records, \(X_j\) is the largest of the first \(j\) observations, and exchangeability gives \(\Pr(X_{j+1}<X_j\mid R_{j-1}=R_j=1)=j/(j+1)\). Therefore
\[
\Pr(R_{j-1}=1,P_j=1)=\frac1{(j-1)(j+1)}.
\]
Subtracting \(\Pr(R_{j-1}=1)\Pr(P_j=1)=1/[3(j-1)]\) gives \((2-j)/[3(j-1)(j+1)]\).

**Case \(i=j\).** A record at \(j\) forces \(X_{j-1}<X_j\), and its next neighbor is smaller with probability \(j/(j+1)\). Hence \(\Pr(R_j=P_j=1)=1/(j+1)\). Subtracting \(1/(3j)\) gives \((2j-1)/[3j(j+1)]\).

**Case \(i=j+1\).** A peak at \(j\) implies \(X_{j+1}<X_j\), so \(R_{j+1}=1\) is impossible. Consequently the covariance equals \(-1/[3(j+1)]\).

These cases exhaust every \((i,j)\) and prove the full kernel. Adding its three nonzero possibilities yields
\[
\frac{2-j}{3(j-1)(j+1)}+
\frac{2j-1}{3j(j+1)}-
\frac1{3(j+1)}
=\frac1{3j(j-1)(j+1)}.
\]
Finally, the identity
\[
\frac1{j(j-1)(j+1)}=\frac12\left(\frac1{j(j-1)}-\frac1{j(j+1)}\right)
\]
telescopes over \(j=2,\ldots,n-1\), giving the displayed finite-order covariance and limit.

## Verification

The accompanying standalone `verify_record_peak.py` enumerates every permutation for each \(n\in\{3,\ldots,8\}\), computes all record and peak indicators, and compares every joint moment and covariance against the claimed rational kernel. It also checks all column sums and the full covariance. The replay passed **160 exact rational assertions**. This finite check is auxiliary: the five-case independence and rank argument proves the theorem for all \(n\ge3\).

## Relationship to prior work

Gnedin (2006) studies record statistics and coherent random permutations. Billey–Burdzy–Sagan (2012) establish exact enumeration of peak sets. Their accessible full texts supply the relevant classical objects but do not state the position-by-position record–peak covariance kernel.

Ji (2023) obtains a joint generating function that includes peak and left-to-right-maxima **total counts**, building on older Euler–Stirling generating functions. That stronger coverage dominates any claim to novelty for the *aggregate* covariance \(\operatorname{Cov}(R,P)\), which is presented here only as a consequence and consistency check. Her generating function tracks numbers of peaks and records, not the individual positions \(i,j\), and therefore does not imply the three-diagonal position-resolved covariance matrix without additional positional information.

Other published position-resolved covariance formulas for inversion indicators or fixed points versus descent indicators involve different events. A peak is a conjunction of adjacent comparisons, not a linear combination of descent indicators, so those formulas do not directly imply the present kernel.

## Limitations

This is a second-order covariance statement only, not conditional independence of all records and peaks nor a higher-cumulant classification. The zero cross-covariance outside the three diagonals is in fact pairwise independence for the indicated events, but the complete vectors remain dependent. The aggregate total-count identity is not independently novel given existing generating functions. Research on position-marked peak–record generating functions could implicitly contain the same kernel; this is a residual historical-priority risk. No independent audit has occurred.

## References

1. A. Gnedin, “Coherent random permutations with record statistics,” arXiv:math/0611538, submitted 2006-11-17, https://arxiv.org/html/math/0611538v1.
2. S. Billey, K. Burdzy, and B. Sagan, “Permutations with given peak set,” arXiv:1209.0693, submitted 2012-09-04, https://arxiv.org/html/1209.0693v1.
3. K. Q. Ji, “The \((\alpha,\beta)\)-Eulerian Polynomials and Descent-Stirling Statistics on Permutations,” arXiv:2310.01053, submitted 2023-10-02, https://arxiv.org/abs/2310.01053.
4. Y. Dong, Z. Lin, and Q. Pan, “A \(q\)-analog of the Stirling–Eulerian Polynomials,” arXiv:2404.09777, submitted 2024-04-15, https://arxiv.org/abs/2404.09777.
