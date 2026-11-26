# Boundary-dominated spine–leaf covariance in random binary search trees

## Finding
Let \(\mathcal T_n\) be a binary search tree obtained by inserting \(n\ge2\) distinct keys in uniformly random order. Let \(T_n\) count the vertices of its left spine (the search path to its minimum key), \(J_n\) count its *internal* leaves (vertices having no children), and \(I_{n,j}\) indicate that the vertex whose key has rank \(j\in\{1,\ldots,n\}\) is an internal leaf.

**Theorem (rankwise boundary–bulk law).** For every \(n\ge2\),
\[
\operatorname{Cov}(T_n,I_{n,j})=
\begin{cases}
\tfrac14,&j=1,\\
-\dfrac{2}{3j(j-1)(j+1)},&2\le j\le n-1,\\
-\dfrac{1}{2n(n-1)},&j=n.
\end{cases}
\]
Consequently,
\[
\boxed{\operatorname{Cov}(T_n,J_n)=\frac{(n-2)(n+1)}{12n(n-1)}.}
\]
The global covariance is strictly positive for every \(n\ge3\), although the covariance with *every* interior-rank leaf indicator and with the largest-rank leaf indicator is strictly negative. It approaches \(1/12\) as \(n\to\infty\).

A second aspect of the same dependence law is that the conditional regression is **not monotone**. For every \(n\ge3\), with \(H_r=\sum_{i=1}^r 1/i\),
\[
\begin{aligned}
\mathbb E[J_n\mid T_n=1]&=n/3,\\
\mathbb E[J_n\mid T_n=2]&=\frac n3+\frac{5n^2-15n+12}{6(n-2)(n-1)H_{n-1}},\\
\mathbb E[J_n\mid T_n=n]&=1.
\end{aligned}
\]
Thus the mean first rises from spine length one to two and is smaller again at the longest possible spine, despite the strictly positive aggregate covariance.

## Assumptions and scope
The key ranks are \(1,\ldots,n\); insertion priorities \(U_1,\ldots,U_n\) are independent continuous uniform random variables on \((0,1)\), and keys are inserted in increasing order of priority. Every subtree with no internal vertices is excluded when counting internal leaves. All statements are exact at finite \(n\), with the stated ranges; the case \(n=2\) has zero global covariance. The notation \(H_r\) denotes a finite harmonic number, with \(H_0=0\). No statement of independence, stochastic monotonicity, or asymptotic joint normality is implied.

## Proof
**Priority representation.** Write
\[
A_i=\mathbf1\{U_i=\min(U_1,\ldots,U_i)\}.
\]
A key of rank \(i\) lies on the left spine exactly when it was inserted before all smaller keys. Hence \(T_n=\sum_{i=1}^n A_i\), \(A_1=1\), and \(\mathbb E A_i=1/i\).

Set \(B_j=I_{n,j}\). A key with interior rank \(j\) is an internal leaf exactly when both adjacent ranks were inserted earlier, so
\[
B_j=\mathbf1\{U_j>\max(U_{j-1},U_{j+1})\},\qquad 2\le j\le n-1.
\]
At the endpoints, \(B_1=\mathbf1\{U_1>U_2\}\) and \(B_n=\mathbf1\{U_n>U_{n-1}\}\). Thus interior leaf probabilities are \(1/3\) and endpoint leaf probabilities are \(1/2\).

**Locality and the interior formula.** For an interior \(j\), \(A_i\) and \(B_j\) are independent if \(i<j-1\), because they use disjoint priorities. They are also independent if \(i>j+1\), because the position of the minimum among the first \(i\) priorities is independent of the relative order among the first \(i-1\) priorities. Therefore only \(i=j-1,j,j+1\) contribute. Conditioning on \(A_{j-1}=1\), the random variable \(U_{j-1}\) is the minimum of \(j-1\) independent uniforms, whose second moment is \(2/[j(j+1)]\). Conditional on its value \(u\), the probability of \(B_j=1\) is \((1-u^2)/2\). Consequently,
\[
\operatorname{Cov}(A_{j-1},B_j)=\frac1{j-1}\left(\frac16-\frac1{j(j+1)}\right).
\]
Here the formula also holds at \(j=2\): \(A_1\) is constant, and the expression vanishes. The event \(A_j=1\) contradicts \(B_j=1\), giving \(\operatorname{Cov}(A_j,B_j)=-1/(3j)\). Conditional on \(A_{j+1}=1\), priorities \(U_{j-1}\) and \(U_j\) are exchangeable above the common minimum; the chance of \(B_j\) is \(1/2\). This gives \(\operatorname{Cov}(A_{j+1},B_j)=1/[6(j+1)]\). Adding these three terms and simplifying proves
\[
\operatorname{Cov}(T_n,B_j)=-\frac2{3j(j-1)(j+1)}.
\]

**Endpoints and summation.** At rank one, \(B_1=A_2\). All other \(A_i\) have zero covariance with \(B_1\), by the same relative-order independence, so \(\operatorname{Cov}(T_n,B_1)=\operatorname{Var}(A_2)=1/4\). At rank \(n\), only \(A_{n-1}\) and \(A_n\) may contribute. Their covariances with \(B_n\) are respectively \((n-2)/[2n(n-1)]\) and \(-1/(2n)\), so the endpoint covariance equals \(-1/[2n(n-1)]\).

The elementary telescoping identity
\[
\sum_{j=2}^{n-1}\frac1{j(j-1)(j+1)}=\frac14-\frac1{2n(n-1)}
\]
(including the empty sum at \(n=2\)) now gives
\[
\operatorname{Cov}(T_n,J_n)=\frac14-\frac23\left(\frac14-\frac1{2n(n-1)}\right)-\frac1{2n(n-1)}=\frac{(n-2)(n+1)}{12n(n-1)}.
\]

**Conditional-regression comparison.** Let \(a_{n,k}=[u^k]\mathbb E[u^{T_n}]\) and \(b_{n,k}=[u^k]\mathbb E[u^{T_n}J_n]\). The root is uniform among the \(n\) ranks, and the two subtrees are independent standard random binary search trees conditional on their sizes. The left-spine recursion implies
\[
\mathbb E[u^{T_n}]=\frac{u(u+1)\cdots(u+n-1)}{n!},\quad a_{n,1}=\frac1n,\quad a_{n,2}=\frac{H_{n-1}}n.
\]
For the leaf mean write \(\ell_0=0\), \(\ell_1=1\), and \(\ell_r=(r+1)/3\) for \(r\ge2\). For \(n\ge2\), with \(b_{0,k}=0\) and \(b_{1,1}=1\), conditioning on the left-subtree size gives the exact polynomial recurrence
\[
 n\mathbb E[u^{T_n}J_n]
 =u\sum_{s=0}^{n-1}\left(\mathbb E[u^{T_s}J_s]+\ell_{n-1-s}\mathbb E[u^{T_s}]\right).
\]
Coefficient extraction gives \(b_{n,1}=1/3\) for \(n\ge3\) and
\[
 b_{n,2}=\frac{H_{n-3}}3+\frac{3/2+1/(n-2)}n \qquad(n\ge3).
\]
Dividing by \(a_{n,1}\) and \(a_{n,2}\) gives the first two conditional means stated above. The correction to \(n/3\) at \(T_n=2\) is strictly positive since \(5n^2-15n+12>0\) for \(n\ge3\). The event \(T_n=n\) means the insertion permutation is strictly decreasing in key rank; the resulting search tree is a chain and has exactly one internal leaf. This establishes nonmonotonicity.

## Verification
Run `python verify.py` with Python 3 and only its standard library. The verifier exhaustively enumerates all \(\sum_{n=2}^8 n! = 46232\) insertion permutations for \(2\le n\le8\), compares every rankwise covariance with the stated rational law and compares the three conditional regressions for \(n\ge3\). It independently checks rational telescoping and regression expressions through \(n=1000\). Its expected final message records 2069 passed exact-rational comparisons. Enumeration checks only finite orders; the analytic argument above establishes the universally quantified claims.

## Relationship to prior work
Holmgren and Janson (2014), particularly their priority representation and Section 8.1, give the underlying random-search-tree model and internal-leaf marginal moments. They study fringe-function counts, not covariance with the extreme-key search spine. Drmota and Hwang (2005) investigate covariances of counts *at two depth levels*, and Martínez and Roura (1998) develop random-search-tree splitting/algorithmic distributions; those statements concern distinct observables and do not directly imply the rankwise boundary–bulk law. The present formulas additionally distinguish leaf indicators by their *key rank*, not their depth. Closely related results in record-process or pattern-count literature might encode the same local law in another form; no claim of exhaustive historical priority is made.

## Limitations
The dependence is second-order; positive covariance does not entail positive association, monotone regression, or independence in the limit. The local formula covers internal leaf counts only, not the \(n+1\) external null pointers sometimes called leaves in algorithmic literature. The conditional regression is displayed at three spine lengths, not fully classified for all intermediate lengths. Some older literature about permutation records and binary-search-tree fringe statistics could implicitly contain these identities; priority requires independent assessment.

## References
1. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883, first publicly submitted 2014-06-26, https://arxiv.org/abs/1406.6883.
2. M. Drmota and H.-K. Hwang, *Profiles of Random Trees: Correlation and Width of Random Recursive Trees and Binary Search Trees*, Advances in Applied Probability 37 (2005), 321–341, https://www.geometrie.tuwien.ac.at/drmota/correlation.pdf.
3. C. Martínez and S. Roura, *Randomized Binary Search Trees*, Journal of the ACM 45 (1998), 288–323, https://www.cs.upc.edu/~conrado/research/papers/jacm-mr98.pdf.
