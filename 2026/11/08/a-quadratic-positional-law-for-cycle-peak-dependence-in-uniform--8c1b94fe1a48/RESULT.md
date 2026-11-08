# A quadratic positional law for cycle–peak dependence in uniform permutations

## Finding
Let \(\Pi\) be uniform on the symmetric group \(S_n\), \(n\ge3\), and let \(C\) be its total number of cycles, including fixed points. For every three positions \(1\le i<j<k\le n\), set \(A_{i,j,k}=\mathbf 1\{\Pi(i)<\Pi(j)>\Pi(k)\}\). Then
\[
\operatorname{Cov}(C,A_{i,j,k})=\frac{-3i^2+9i+6j^2-18j-3k^2+9k+2}{6n(n-1)(n-2)}. \tag{1}
\]
Thus the numerator is independent of the ambient permutation size. For consecutive positions \(i=j-1\) and \(k=j+1\), the covariance is \(-2/[3n(n-1)(n-2)]\) for every interior \(j\). In contrast, for positions \((1,n-1,n)\), the numerator is \(3n^2-21n+32\), positive for every \(n\ge5\). For \(n=3,4\), every admissible triple has negative covariance; hence \(n=5\) is the smallest order at which both covariance signs occur. At \(n=5\), the triple \((1,4,5)\) has covariance \(1/180\). In the separated family \((1,n-1,n)\), the covariance is asymptotic to \(1/(2n)\), whereas any consecutive peak has covariance asymptotic to \(-2/(3n^3)\).

## Assumptions and scope
The permutation is uniform on all \(n!\) bijections \(\{1,\ldots,n\}\to\{1,\ldots,n\}\), with positions and values labeled by the same ordered set. Cycles refer to the action of this bijection, rather than runs or ascents of the one-line notation. The three positions are arbitrary and need not be consecutive. No asymptotic approximation is used in (1). An inequality of the form \(\Pi(i)<\Pi(j)>\Pi(k)\) uses strict comparisons, automatic because the values are distinct. Since three sampled values have all six relative orders equally often, \(\mathbb E A_{i,j,k}=1/3\).

## Proof
Write \(H_m=\sum_{t=1}^m1/t\), with \(H_0=0\). The following finite partial-permutation identity is useful: prescribe the three distinct images \(\Pi(i)=a\), \(\Pi(j)=b\), \(\Pi(k)=c\). View these assignments as three directed edges on the labeled set. Because they form a partial injection, each component is a directed path or a closed directed cycle. Let \(r\) be the number of closed directed cycles already present among the prescribed edges. Contract each directed path, and delete the forced cycles. The remaining unconstrained completion is bijective to a permutation of \(n-3\) residual objects, and the total number of cycles in each completion is \(r\) plus the cycle count of the residual permutation. Consequently
\[
\mathbb E[C\mid\Pi(i)=a,\Pi(j)=b,\Pi(k)=c]=H_{n-3}+r. \tag{2}
\]
This is an exact identity for all \(n\ge3\), including \(n=3\), when the residual permutation is empty. The standard expected cycle count identity is \(\mathbb E C=H_n\).

To evaluate \(\mathbb E[r A_{i,j,k}]\), sum over the \((n)_3=n(n-1)(n-2)\) ordered distinct image triples. By additivity of the forced-cycle count, count fixed points, transpositions, and 3-cycles separately; overlapping prescribed cycles cannot occur in a partial injection.

A fixed point at \(i\) is compatible with the peak precisely when \(b=t>i\) and \(c<t\), \(c\ne i\). The number of compatible triples is \(\sum_{t=i+1}^{n}(t-2)=(n-i)(n+i-3)/2\). A fixed point at \(j\) allows exactly \((j-1)(j-2)\) ordered choices of \(a,c<j\). A fixed point at \(k\) contributes \((n-k)(n+k-3)/2\) image triples by the corresponding right-hand comparison.

Of the three possible transpositions among the prescribed positions, \((i\ j)\) is incompatible with the central peak, \((i\ k)\) contributes \(n-k\) image triples, and \((j\ k)\) contributes \(k-2\). Of the two 3-cycles, only \(i\mapsto j\mapsto k\mapsto i\) is compatible, and contributes one triple. Their combined contribution is \((n-k)+(k-2)+1=n-1\). Therefore
\[
\mathbb E[r A_{i,j,k}]=\frac{\frac12(n-i)(n+i-3)+(j-1)(j-2)+\frac12(n-k)(n+k-3)+n-1}{n(n-1)(n-2)}. \tag{3}
\]
By (2), \(\mathbb E[C A_{i,j,k}]=H_{n-3}/3+\mathbb E[r A_{i,j,k}]\). Subtract \(H_n/3\) and use \(H_n-H_{n-3}=1/(n-2)+1/(n-1)+1/n\). Simplifying gives (1).

For consecutive positions, substitute \(i=j-1\), \(k=j+1\); the numerator in (1) is \(-4\). At \((1,n-1,n)\), it becomes \(3n^2-21n+32\), positive for every integer \(n\ge5\). For \(n=3,4\), direct substitution over respectively one and four possible triples gives only negative numerators (the maximum is \(-4\)); the first positive numerator is \(2\) at \((n,i,j,k)=(5,1,4,5)\). Hence the claimed boundary is exact.

## Verification
Run `python3 verify.py` with Python 3. The script independently enumerates all permutations through \(n=8\), computes exact rational covariances for every triple, verifies the partial-injection conditional cycle lemma for every triple prescription through \(n=6\), and checks the first-positive-sign boundary. It reports `VERIFY_OK 3237 exact assertions`. These finite checks corroborate the all-\(n\) algebraic proof, and do not replace it. No random simulation or numerical approximation is required.

## Relationship to prior work
Fulman, Kim, and Lee (arXiv:1902.00978, first public February 3, 2019) analyze total consecutive peak counts in uniform permutations and fixed conjugacy classes, using cycle-type generating functions. Gessel and Zhuang (arXiv:2001.00654, first public January 2, 2020), especially Section 7.1, develop joint formulas for global peak, descent, and cycle-type statistics. Those results encompass the aggregate consecutive-peak context, which is not claimed as new here. Equation (1) instead concerns any explicitly indexed nonconsecutive three-position comparison and its covariance with total cycles. The quadratic positional profile, its positive/negative sign coexistence, and the sharp \(n=5\) boundary are the additional claims. An existing full descent-set/cycle-type formula can encode consecutive-index peak events, but a comparison of nonadjacent permutation values is not determined by the descent set. General permutation pattern-density limit theorems likewise do not give this finite positional law. The proof uses a direct partial-injection contraction, not a restatement of a global peak enumerator.

## Limitations
Only a single triple-comparison indicator and the total number of cycles are analyzed; joint distributions, higher-order cumulants, nonuniform permutation measures, and peak-conditioned cycle distributions are not determined. Historical priority is not established exhaustively: an equivalent nonconsecutive positional formula could occur in older pattern/cycle enumeration literature outside the inspected texts.

## References
- J. Fulman, G. B. Kim, S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class of* \(S_n\), arXiv:1902.00978, 2019. https://arxiv.org/abs/1902.00978
- I. M. Gessel, Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654, 2020. https://arxiv.org/html/2001.00654v2
