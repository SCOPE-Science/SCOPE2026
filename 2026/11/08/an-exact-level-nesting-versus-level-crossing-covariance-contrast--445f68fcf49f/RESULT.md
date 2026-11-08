# An exact level–nesting versus level–crossing covariance contrast for uniform set partitions

## Finding

Let \(\Pi_n\) be uniform on the \(B_n\) partitions of \([n]=\{1,\ldots,n\}\), for every integer \(n\ge2\). Connect consecutive members of each block by an arc. Write \(L_n\) for the number of *level arcs* \((i,i+1)\), and \(C_n\), respectively \(N_n\), for the number of unordered pairs of arcs with four distinct endpoints in crossing or nesting order. Then

\[
\boxed{\operatorname{Cov}(L_n,N_n)-\operatorname{Cov}(L_n,C_n)
=n+3-2\frac{B_{n+1}}{B_n}.}
\]

The difference vanishes for \(n=2,3\), is strictly positive for all \(n\ge4\), and satisfies
\[\frac{\operatorname{Cov}(L_n,N_n)-\operatorname{Cov}(L_n,C_n)}{n}\longrightarrow1.\]
The individual crossing and nesting pair counts are equidistributed, so the theorem distinguishes their *dependence on a third natural statistic*, not their marginal distributions.

## Assumptions and scope

A set partition \(\pi\) of \([n]\) has blocks of distinct integers. For each block \(a_1<\cdots<a_r\), its arcs are \((a_j,a_{j+1})\), \(1\le j<r\). Two arcs \((a,b)\) and \((c,d)\) cross if \(a<c<b<d\) or \(c<a<d<b\), and nest if \(a<c<d<b\) or \(c<a<b<d\); touching endpoints count as neither. A level arc is \((i,i+1)\). \(B_m\) denotes the number of all partitions of \([m]\), with \(B_0=1\). The underlying law assigns probability \(B_n^{-1}\) to each partition, with no restriction on block count.

Define the dimension index
\[d(\pi)=\sum_{(a,b)\in\operatorname{Arc}(\pi)}(b-a-1)=\sum_{A\text{ block}}(\max A-\min A+1)-m,\]
for a partition of \([m]\). Every summand is nonnegative.

## Proof

**Step 1: equal crossing and nesting means.** The 2-crossing and 2-nesting *pair counts* (not maximum crossing or nesting sizes) are equidistributed on all partitions of each fixed size by Kasraoui and Zeng [1]. Consequently, \(\mathbb E[N_n-C_n]=0\) for all \(n\). Hence the covariance difference in the theorem equals \(\mathbb E[L_n(N_n-C_n)]\).

**Step 2: contract a marked adjacent arc.** Fix \(i\in\{1,\ldots,n-1\}\). Set partitions of \([n]\) containing the arc \((i,i+1)\) correspond bijectively to partitions \(\rho\) of \([n-1]\) by deleting vertex \(i+1\) and subtracting one from larger labels. Because \(i,i+1\) are consecutive integers in the same block, \((i,i+1)\) is automatically an arc. Under contraction, the relative positions of preexisting arcs preserve crossing and nesting pairs. The newly inserted level arc cannot cross any arc, since no integer lies strictly between its endpoints. It is nested within exactly those arcs \((a,b)\in\operatorname{Arc}(\rho)\) for which \(a<i<b\). Put
\[h_i(\rho)=\#\{(a,b)\in\operatorname{Arc}(\rho):a<i<b\}.\]
Thus for \(X=N-C\), \(X(\pi)=X(\rho)+h_i(\rho)\). Summing over each marked level arc gives
\[
\sum_{\pi\in\mathcal P([n])}L(\pi)X(\pi)
=\sum_{i=1}^{n-1}\sum_{\rho\in\mathcal P([n-1])}
\bigl(X(\rho)+h_i(\rho)\bigr).
\]
The first term vanishes by Step 1. Each arc \((a,b)\) is counted in \(h_i\) at exactly \(b-a-1\) integers \(i\), whence \(\sum_{i=1}^{n-1}h_i(\rho)=d(\rho)\). Consequently,
\[
\operatorname{Cov}(L_n,N_n)-\operatorname{Cov}(L_n,C_n)
=\frac{1}{B_n}\sum_{\rho\in\mathcal P([n-1])}d(\rho).
\tag{1}
\]

**Step 3: calculate the dimension sum.** Set \(D_m=\sum_{\rho\in\mathcal P([m])}d(\rho)\). Let \(K(\rho)\) be the number of blocks, and, for each cut \(j\in\{1,\ldots,m-1\}\), let \(T_j(\rho)\) count blocks meeting both sides of the cut. Counting each block's span shows
\[d(\rho)=\sum_{j=1}^{m-1}T_j(\rho)+K(\rho)-m.\]
The aggregate number of blocks is \(\sum_{\rho}K(\rho)=B_{m+1}-B_m\), by marking one block. For each cut \(j\), the total number of blocks contained entirely to its left is \(\sum_{s=1}^j\binom{j}{s}B_{m-s}\), and the analogous expression holds on the right. Thus, using the hockey-stick binomial identity,
\[
D_m=mB_{m+1}-2mB_m-2\sum_{s=1}^{m-1}\binom{m}{s+1}B_{m-s}.
\]
The Bell recurrence implies
\[\sum_{s=1}^{m-1}\binom{m}{s+1}B_{m-s}=B_{m+2}-2B_{m+1}-mB_m.\]
Therefore
\[\boxed{D_m=(m+4)B_{m+1}-2B_{m+2}.}\tag{2}\]
This independently reconstructs the dimension-index identity recorded in [2]. Substitute \(m=n-1\) from (2) into (1) to obtain the asserted covariance difference for every \(n\ge2\).

**Step 4: signs and scale.** Each \(d(\rho)\) is nonnegative. All dimensions vanish if \(m\le2\); for every \(m\ge3\), the partition containing the block \(\{1,3\}\) (with remaining elements singleton) has strictly positive dimension. Equation (1) therefore proves the exact zero and positivity classification. Finally the classical Bell-ratio estimate \(B_{n+1}/B_n=O(n/\log n)\) [2] gives a difference of \(n+o(n)\).

## Verification

Run `python VERIFY.py` using Python's standard library. The verifier carries out exact integer/rational calculations: enumeration of all \(B_n\) partitions through \(n=8\), checks of the covariance identity and dimension aggregate, exhaustive marked-arc contraction checks, and Bell-cut recurrence checks up to size \(60\). The replayed standalone verifier reports **13,141 exact checks passed**. This finite verification tests the formulas and contraction mechanism; the four proof steps establish the results for all integer \(n\ge2\).

For example, the covariance gaps for \(n=2,3,4,5,6,7\) are, respectively, \(0,0,1/15,5/26,73/203,490/877\), and every value agrees with the formula.

## Relationship to prior work

Kasraoui and Zeng [1] establish equidistribution of two-arc crossing and nesting *counts*, which gives only \(\mathbb E[N_n-C_n]=0\), not an equality of their mixed moments with \(L_n\). Chern, Diaconis, Kane and Rhoades [2] identify levels, crossing counts and the dimension index as set-partition statistics; their general shifted-Bell moment theory does not specify this mixed covariance contrast, while their published dimension sum is used here and also derived independently. Poznanović and Yan [3] study subtree distributions of two-edge crossing/nesting counts rather than dependence on the local adjacent-arc count. The companion limit-theorem paper [4] studies marginal normal limits for crossings, levels and dimension. The present argument identifies the extra nesting contribution under contraction and converts it to an exact Bell-ratio covariance gap.

## Limitations

The theorem concerns the *difference* of two covariances, not closed formulas for the individual covariances. It does not imply independence or any sign for either individual covariance. It uses uniform set partitions of labeled points and counts of crossing/nesting *pairs*, not distributions conditioned on a fixed number of blocks or the maximal crossing/nesting cardinalities. Historical-priority uncertainty remains because other enumeration frameworks may implicitly encode the joint moments. The identity is not independently audited.

## References

[1] A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions* (2006), arXiv:math/0601081, https://arxiv.org/abs/math/0601081.

[2] B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Closed expressions for averages of set partition statistics* (first posted 2013), arXiv:1304.4309, https://arxiv.org/abs/1304.4309.

[3] S. Poznanović and C. Yan, *Crossings and Nestings of Two Edges in Set Partitions* (2007), arXiv:0710.1816, https://arxiv.org/abs/0710.1816.

[4] B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Central Limit Theorems for some Set Partition Statistics* (2015), arXiv:1502.00938, https://arxiv.org/abs/1502.00938.
