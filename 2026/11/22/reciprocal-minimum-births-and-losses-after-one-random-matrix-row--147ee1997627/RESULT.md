# Reciprocal-minimum births and losses after one random-matrix row deletion

## Finding

Let \(X=(X_{ij})_{0\le i,j<n}\) be an \(n\)-by-\(n\) matrix of independent identically distributed atomless real entries, \(n\ge2\). An entry is a **reciprocal minimum** when it is the unique minimum in both its row and its column. Delete row \(0\), leaving the other entries unchanged. Let \(L_n\) be the number of reciprocal minima destroyed by deletion, and \(A_n\) the number of reciprocal minima newly created among the remaining entries. Then \(L_n\in\{0,1\}\) and

\[
\begin{aligned}
\mathbb E L_n&=\frac{n}{2n-1},\\
\mathbb E A_n&=\frac{n}{2(2n-1)},\\
\mathbb E(L_nA_n)&=\frac{n}{2(3n-2)}+\frac{n}{8(2n-1)},\\
\operatorname{Cov}(L_n,A_n)&=\frac{n(10n^2-15n+6)}{8(2n-1)^2(3n-2)}>0.
\end{aligned}
\]

For \(0\le s,t\le1\), the **joint** probability generating functions converge:

\[
\lim_{n\to\infty}\mathbb E\bigl[s^{L_n}t^{A_n}\bigr]
=s e^{(t-1)/4}+(1-s)\int_0^1(1-u)e^{(t-1)u^2/4}\,du.
\]

In particular \(L_n\) converges to \(\operatorname{Bernoulli}(1/2)\), \(A_n\) converges to \(\operatorname{Poisson}(1/4)\), but they are not independent. Their covariance converges to \(5/48\). The two limiting conditional arrival means are highly unequal:

\[
\lim_{n\to\infty}\mathbb E[A_n\mid L_n=1]=\frac{11}{24},\qquad
\lim_{n\to\infty}\mathbb E[A_n\mid L_n=0]=\frac{1}{24}.
\]

The resulting count difference between the smaller and original matrices is exactly \(A_n-L_n\). Its limiting variance is \(7/24\), and its limiting mean is \(-1/4\).

## Assumptions and scope

All \(n^2\) entries have one common continuous, atomless distribution and are independent. Row deletion is deterministic (row \(0\)); by row exchangeability this is the law of uniformly choosing a row independently of the matrix. All statements are distribution-free under strictly increasing transformations of the entries. There are no statements about correlated costs, ties, or deletion of more than one row. The limiting statements let the number of rows and columns both equal \(n\) and grow together. Reciprocal minima remaining in surviving rows cannot be destroyed, because deletion never introduces a smaller competitor; only a reciprocal minimum in the deleted row can be lost.

## Proof

**1. Exact losses and arrivals.** Use the probability-integral transform and then a strictly increasing map to independent \(\operatorname{Exp}(1)\) entries, preserving every comparison. Let \(U_j=X_{0j}\) and let \(Y_j=\min_{1\le i<n}X_{ij}\), with \(R_j\) the unique row achieving this latter minimum. Independently across columns, \(U_j\sim\operatorname{Exp}(1)\), \(Y_j\sim\operatorname{Exp}(n-1)\), and \(R_j\) is uniform among the \(n-1\) surviving rows. The deletion destroys a reciprocal minimum exactly when the smallest \(U_j\) is smaller than its corresponding \(Y_j\). Its probability is

\[
n\int_0^\infty e^{-nu}e^{-(n-1)u}\,du=\frac{n}{2n-1}.
\]

An arrival in column \(j\) requires \(U_j<Y_j\) and that \(Y_j\) be the minimum of surviving row \(R_j\) as well. Given \(Y_j=y\), its remaining \(n-1\) row entries are independent exponentials, so the latter probability is \(e^{-(n-1)y}\). Therefore

\[
\mathbb P(\text{arrival in column }j)
=(n-1)\int_0^\infty e^{-2(n-1)y}(1-e^{-y})\,dy
=\frac1{2(2n-1)}.
\]

Summing over columns gives the arrival expectation. At most one loss is possible, since a row has a unique minimum.

**2. The mixed finite moment.** Partition \(\mathbb E(L_n A_n)\) into an arrival in the same column \(i\) as the deleted reciprocal minimum and an arrival in a distinct column \(j\). The same-column probability, summed over all \(i\), is

\[
n\cdot\frac{n-1}{n}\left(\frac1{2(n-1)}-\frac1{3n-2}\right)=\frac{n}{2(3n-2)}.
\]

For distinct \(i,j\), put \(x=U_i\), \(z=U_j\), \(y=Y_j\). Necessary comparisons give \(0<x<z<y\). Summing over the \(n-1\) choices of \(R_j\), integrating all independent exponential competitors, and observing that the entry in row \(R_j\) and column \(i\) is constrained by both events, gives

\[
\mathbb P(\text{loss at }i,\text{ arrival at }j)
=(n-1)\int_{0<x<z<y}e^{-(2n-3)x-z-(2n-2)y}\,dx\,dz\,dy
=\frac1{8(n-1)(2n-1)}.
\]

There are \(n(n-1)\) ordered pairs. Adding the two contributions proves the displayed mixed moment. Subtracting the product of the means and factoring yields the strictly positive covariance (the numerator polynomial \(10n^2-15n+6\) has negative discriminant).

**3. Marked Poisson limit.** Write \(x_j=nU_j\), \(y_j=nY_j\). Because columns are independent, the point process \(\sum_{j=1}^n\delta_{(x_j,y_j)}\) converges locally to a Poisson point process on \((0,\infty)^2\) with intensity \(dx\,e^{-y}dy\): each column has joint density \(n^{-1}e^{-x/n}\cdot(n-1)n^{-1}e^{-(n-1)y/n}\), and there are \(n\) columns. For points with \(x<y\), the associated surviving row's other entries exceed \(y/n\) with conditional probability \(e^{-(n-1)y/n}\to e^{-y}\).

These row-minimum marks are asymptotically independent on every bounded \((x,y)\) rectangle. Indeed, a bounded region contains only a tight number of candidate columns; their minimizing surviving rows are independent uniform labels and hence distinct with probability tending to one. Conditional on the finite set of selected columns and their column minima, the entries of these distinct rows in nonselected columns are independent. The entries at crossings with other selected columns are conditioned by their column minima, but their probabilities of being below one of the bounded thresholds are \(O(1/n)\), so removing these crossings changes no mark with probability tending to one. Thus marks converge jointly to independent Bernoulli variables of success probability \(e^{-y}\). For any \(M>0\), the expected number of candidate columns with \(x_j>M\) is at most \(e^{-M+o(1)}\), and the probability that the smallest \(x_j\) exceeds \(M\) is also \(e^{-M}\). This supplies the truncation needed for convergence of all arrival and loss counts, not merely local point processes.

After integrating out \(y>x\), the arrival marks form a one-dimensional Poisson process in the \(x\) coordinate with rate

\[
\int_x^\infty e^{-y}e^{-y}\,dy=\tfrac12e^{-2x}.
\]

The first \(x\) of the underlying rate-one Poisson process, call it \(X_*\), is \(\operatorname{Exp}(1)\). Its indicator of \(y>X_*\) is the loss indicator. Given \(X_*=x\), the first point has probability \(e^{-x}\) of producing a loss and probability \(\frac12e^{-2x}\) of producing both a loss and an arrival. All later arrivals are independent Poisson with mean \(\frac14e^{-2x}\). The conditional generating factor for the first point is

\[
1-e^{-x}+s\bigl(e^{-x}-\tfrac12e^{-2x}\bigr)+st\tfrac12e^{-2x}.
\]

Integrating this against the density \(e^{-x}\,dx\), multiplying by \(\exp((t-1)e^{-2x}/4)\) for future arrivals, and substituting \(u=e^{-x}\) gives the announced generating function. Its \(s=1\) specialization is \(e^{(t-1)/4}\), since the integrand becomes the derivative of \(u e^{(t-1)u^2/4}\). Its \(t=1\) specialization is \((1+s)/2\). Differentiation at \((1,1)\) gives \(\mathbb E(LA)=11/48\), and hence the limiting conditional means and covariance. The second factorial moments of \(A_n\) are uniformly bounded: for different columns, an arrival requires \(U_j<Y_j\), independent events each of probability \(1/n\). In fact every fixed factorial moment is bounded by one; this justifies convergence of the first two count moments and the stated variance of the difference.

## Verification

The accompanying standalone `check.py` uses exact integer permutation enumeration of all \(4!\) cost ranks for \(n=2\) and all \(9!\) cost ranks for \(n=3\), reconstructing the loss and arrival counts without invoking the integral formulas. It checks all three exact moments, and verifies marginal generating-function identities by deterministic quadrature. It also verifies the factored covariance and limiting moment arithmetic. Execute `python3 check.py` with a standard Python 3 interpreter. These tests do not replace the general exponential-integral and point-process arguments above.

## Relationship to prior work

Trendtel, Ünlü and Dzhafarov (2010) treat the probability that all row minima and column minima form a reciprocal matching, a different all-or-nothing property. Dzhafarov, Ünlü, Trendtel and Colonius (2011) derive the full one-matrix distribution of the number of violations of reciprocal matching; single-matrix counts do not specify a coupled before/after deletion law. Pittel and Weishaar (1999) study nearest-neighbor bipartite random graphs; their abstract addresses matching and connectivity rather than a one-row removal joint law. The current result analyzes the *same matrix coupled with its deletion submatrix* and resolves the joint loss/arrival law, including an explicit dependence that cannot be recovered from either marginal. The 1999 and 2011 articles could not be read completely, so a historical-priority qualification is retained.

## Limitations

The construction is for a single deleted row in a square independent continuous cost matrix, not multiple deletions, sparse matrices, geometric dependencies, adversarial row selection or general exchangeable arrays. The Poisson-limit proof is asymptotic; it gives no quantitative total-variation rate. The attached code checks finite cases and numerical identities, not every point-process inference. Full-text historical comparison remains incomplete for the 1999 nearest-neighbor graph article and the 2011 violations-of-regular-minimality article; their abstracts and available metadata were inspected, but their complete contents were not certified as non-covering.

## References

1. B. Pittel and R. S. Weishaar, “The random bipartite nearest neighbor graphs,” *Random Structures & Algorithms* 15 (1999), 279–310. First published 1999-10-20. DOI: https://doi.org/10.1002/(SICI)1098-2418(199910/12)15:3/4%3C279::AID-RSA6%3E3.0.CO;2-J.
2. M. Trendtel, A. Ünlü and E. N. Dzhafarov, “Matrices Satisfying Regular Minimality,” *Frontiers in Psychology* 1 (2010), 211. Published 2010-12-02. DOI: https://doi.org/10.3389/fpsyg.2010.00211.
3. E. N. Dzhafarov, A. Ünlü, M. Trendtel and H. Colonius, “Matrices with a given number of violations of Regular Minimality,” *Journal of Mathematical Psychology* 55 (2011), 240–250. DOI: https://doi.org/10.1016/j.jmp.2010.12.002.
