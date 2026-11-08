# Sharp matching-deletion stability for two-way additive least squares

## Finding
Fix an integer \(n\ge3\). Let \(E_{n,r}=\{(i,j):1\le i,j\le n\}\setminus\{(s,s):1\le s\le r\}\), where \(0\le r\le n\). On the real functions on this observed-cell set, let \(P_{n,r}\) be the orthogonal projection, for the uniform counting inner product, onto the restrictions of additive two-way functions \(g(i,j)=a_i+b_j\). Then
\[
\boxed{\|P_{n,r}\|_{\ell^\infty(E_{n,r})\to\ell^\infty(E_{n,r})}=
\begin{cases}
3-\frac4n+\frac{2(n-2)}{n\,[n(n-2)+r]},&0\le r<n,\\[3pt]
3-\frac4n,&r=n.
\end{cases}}
\]
For \(r<n\), precisely the observed cells with **both indices outside** \(\{1,\ldots,r\}\) have maximal absolute projection-kernel row sums. For \(r=n\), every observed cell is maximizing. Each maximizing row yields all real norm-one data attaining the operator norm: the data must equal a common overall sign times the sign of that row at every nonzero kernel entry (values at any zero entries are arbitrary within the unit interval).

The norm strictly decreases with each additional deletion of a cell on the matching. For \(0\le r\le n-2\), with \(T_r=n(n-2)+r\),
\[
\|P_{n,r}\|-\|P_{n,r+1}\|=\frac{2(n-2)}{nT_r(T_r+1)}.
\]
The last deletion has the larger drop
\[
\|P_{n,n-1}\|-\|P_{n,n}\|=\frac{2(n-2)}{n(n^2-n-1)},
\]
which is exactly \((n+1)(n-2)\) times the preceding decrement. Thus the last missing matched cell gives a disproportionate stability improvement. The sharp negative fitted value for data in \([0,1]\), over all observed target cells, is \((\|P_{n,r}\|-1)/2\).

## Assumptions and scope
The table is square with \(n\) levels for each factor; all observed cells have equal positive weight. The missing cells are any matching of size \(r\): independent permutations of the row and column labels bring it to the displayed diagonal matching. The additive model includes constants; parameterization \(a_i+b_j\) has one redundancy, but fitted cell values and the orthogonal projection are unique. The bipartite observation graph remains connected when \(n\ge3\), including the full crown graph at \(r=n\). The norm is on **observed cells only**, not extrapolations to absent cells, and it is the norm of this fixed least-squares projector, not the infimum over arbitrary projections.

## Proof
Put \(T=n(n-2)+r\). For the full table, the row-and-column projection has kernel
\[
H^0_{(i,j),(k,l)}=\frac{\mathbf1_{i=k}+\mathbf1_{j=l}}n-\frac1{n^2}.
\]
Let \(D=\{(s,s):1\le s\le r\}\) and write \(E=E_{n,r}\). The deleted principal block of \(H^0\) is \(H^0_{DD}=(2/n)I_r-(1/n^2)J_r\). Deletion of observations from a full-column-rank design, followed by the Sherman--Morrison--Woodbury inverse identity, gives the **exact** observed hat matrix
\[
H=H^0_{EE}+H^0_{ED}(I_r-H^0_{DD})^{-1}H^0_{DE}.
\]
This is justified by taking the usual \(2n-1\) independent additive-model columns; the Gram matrix after deletion is invertible because the observation graph is connected. Since \(n\ge3\),
\[
(I_r-H^0_{DD})^{-1}=\frac{n}{n-2}I_r-\frac{n}{(n-2)T}J_r.
\]
For \(e=(i,j)\) let \(u_e(s)=(\mathbf1_{i=s}+\mathbf1_{j=s})/n-1/n^2\) for \(1\le s\le r\). Consequently, for all observed \(e,f\),
\[
H_{ef}=H^0_{ef}+\frac{n}{n-2}\sum_{s=1}^r u_e(s)u_f(s)-\frac{n}{(n-2)T}\left(\sum_{s=1}^r u_e(s)\right)\left(\sum_{s=1}^r u_f(s)\right).
\tag{1}
\]
This formula is valid also at \(r=0\), with empty sums. Because constants belong to the additive model, \(\sum_fH_{ef}=1\), and hence
\[
\sum_f|H_{ef}|=1+2\sum_{f:H_{ef}<0}|H_{ef}|.
\tag{2}
\]

The possible evaluation rows have three symmetry types: U (neither index deleted), M (exactly one index deleted), and B (both indices deleted; the latter row is observed only when the two indices differ). **U** occurs for \(r<n\). Substitution of \(u_e(s)=-1/n^2\) into (1) gives, for a U row \(e=(i,j)\),
\[
H_{(i,j),(k,l)}=\frac{\mathbf1_{i=k}+\mathbf1_{j=l}}n-\frac{n-2+\mathbf1_{k\le r}+\mathbf1_{l\le r}}{nT}.
\tag{3}
\]
It is strictly positive when \(k=i\) or \(l=j\) and strictly negative otherwise. The negative entries have total magnitude
\[
N_U=\frac{(n-2)((n-1)^2+r)}{nT}=\frac{n-2}{n}+\frac{n-2}{nT}.
\tag{4}
\]
The count uses \((n-1)^2-r\) allowable pairs with neither index matching and a further \(2r(n-2)\) in the weighted marked-index terms.

For **M**, label the distinguished deleted index \(I\), the distinguished undeleted index \(J\), the other deleted indices \(M'\), and the other undeleted indices \(U'\). The negative entries of (1), classified by the class of the row index and column index of \(f\), are exactly
\[
(M',I),\ (M',M'),\ (M',U'),\ (J,M'),\ (J,U'),\ (U',M'),\ (U',U').
\]
Here pairs with identical deleted indices are omitted and empty classes contribute zero. Substitution and summation give
\[
N_U-N_M=\frac{r^2-nr+n^2-3n+3}{n(n-2)T}
=\frac{(r-n/2)^2+3(n-2)^2/4}{n(n-2)T}>0.
\tag{5}
\]
For **B**, choose two distinct marked indices \(I,K\); with \(M'\) the other marked indices and \(U'\) all unmarked indices, the negative entry classes are
\[
(K,M'),\ (K,U'),\ (M',I),\ (M',M'),\ (M',U'),\ (U',I),\ (U',M'),\ (U',U').
\]
Their exact negative mass is \(N_B=(n-2)/n\). The sign assertions in the last two classifications follow directly from (1), using \(3\le n\), \(1\le r\le n\), and only nonempty row classes. In particular the potentially limiting M-row positive entry indexed by a different marked row and distinguished unmarked column has numerator \(n(n-2)(n-3)+r(n-2)-1\), positive whenever that class occurs; the reversed marked-pair B-entry has numerator \(n(n-4)+2r\), positive when the B class occurs. All other signs are immediate after collecting nonnegative terms.

Thus U exceeds M strictly by (5), and U exceeds B by \(N_U-N_B=(n-2)/(nT)>0\) whenever U exists. If \(r=n\), only B rows exist, all with negative mass \((n-2)/n\). Applying (2) proves the asserted norm and all maximizing rows. The strict deletion and final-jump identities follow by subtraction; the \([0,1]\) positivity defect follows by selecting exactly those data with negative kernel coefficients at a maximizing row. Equality in the absolute row-sum triangle inequality gives the sign classification of norming inputs.

## Verification
The companion `verify_crown.py` is self-contained Python 3 code using only standard-library exact fractions. It directly constructs independent full-rank additive regression matrices, computes the Gram inverse by rational elimination, and checks every surviving row against the closed formulas for all \(3\le n\le6\) and \(0\le r\le n\) (22 designs; 466 observed-cell rows). The checker does **not** use (1) to construct its projection matrices. This finite computation is a consistency check, not a proof for unbounded \(n\); the universal proof is the exact inverse and the three analytic sign-class sums above.

## Relationship to prior work
Electrical-network projection and edge leverage identities were established in the graph-sparsification literature, including Spielman--Srivastava (2008) and Drineas--Mahoney (2010). The identity \(H=BL^+B^\mathsf T\), up to edge orientation and weighting, is background. The present result concerns a different sharp quantity, the **absolute row sum** of the additive-model projector after a matching deletion, and provides its exact values, all norming rows and the unequal successive decrements. The published foundational sources do not claim this all-dimensional matching-deletion extremizer classification. It is possible that an older experiment-design hat-matrix calculation implicitly supplies equivalent special cases; the priority claim is qualified accordingly.

## Limitations
No statement is made about nonmatching deletion patterns, nonuniform cell weights, rectangular tables with unequal side lengths, statistical risk under stochastic noise, or the minimum norm among all nonorthogonal projections. The exact endpoint \(r=n\) requires \(n\ge3\); at \(n=2\) deleting a full matching disconnects the graph. An independently performed mathematical audit has not been obtained; the scientific conclusions and literature comparison are limited to the materials and arguments described here.

## References
- D. A. Spielman and N. Srivastava, *Graph Sparsification by Effective Resistances*, arXiv:0803.0929v1 (first posted 2008-03-06), especially the edge-space projection identity and its spectral role. https://arxiv.org/abs/0803.0929
- P. Drineas and M. W. Mahoney, *Effective Resistances, Statistical Leverage, and Applications to Linear Equation Solving*, arXiv:1005.3097v1 (first posted 2010-05-18), Sections 3.1–3.2 for statistical leverage and incidence projection. https://arxiv.org/html/1005.3097v1
