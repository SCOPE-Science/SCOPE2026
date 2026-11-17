# Pairwise orthogonality without independence in random recursive-tree descendant sizes

## Finding
Let \(T_n\) be the uniform random recursive tree on birth labels \(1,\ldots,n\). Write \(S_i(n)\) for the number of vertices in the complete fringe subtree rooted at label \(i\), **including** \(i\). For every integer \(n\ge2\) and every two distinct labels \(1\le i<j\le n\),
\[
\mathbb E[S_i(n)S_j(n)]=\frac{n^2}{ij},\qquad
\operatorname{Cov}(S_i(n),S_j(n))=0.
\]
This pairwise orthogonality is not independence. Whenever \(n\ge4\) and \(2\le i<j<n\),
\[
\operatorname{Cov}\!\left(\mathbf1_{\{S_i(n)=1\}},\mathbf1_{\{S_j(n)=1\}}\right)
=-\frac{(i-1)(n-j)}{(n-1)^2(n-2)}<0.
\]
Thus every pair of nonconstant descendant-size variables \(S_i(n),S_j(n)\) is dependent, despite its zero covariance. The covariance matrix of \((S_2(n),\ldots,S_{n-1}(n))\) is exactly diagonal and positive definite.

For \(1\le i\le n\), the diagonal variances are
\[
\operatorname{Var}(S_i(n))=\frac{n(n-i)(i-1)}{i^2(i+1)}.
\]
If \(P_n\) denotes the total depth of all vertices, with root depth zero, the orthogonality gives the **exact variance decomposition**
\[
P_n+n=\sum_{i=1}^n S_i(n),\qquad
\operatorname{Var}(P_n)=\sum_{i=1}^n\operatorname{Var}(S_i(n))
=n^2\bigl(2-H_n^{(2)}\bigr)-nH_n,
\]
where \(H_n=\sum_{k=1}^n 1/k\) and \(H_n^{(2)}=\sum_{k=1}^n 1/k^2\). In particular, \(\operatorname{Var}(P_n)/n^2\to2-\pi^2/6\). The one-point variances and the total-path-length variance formula are classical; the joint orthogonality and its explicit contrast with dependence are the statement assessed here.

## Assumptions and scope
The model starts with vertex \(1\). For each \(k=2,\ldots,n\), vertex \(k\) chooses its parent independently and uniformly from \(\{1,\ldots,k-1\}\); equivalently each of the \((n-1)!\) recursive trees has equal probability. Descendants are oriented away from root \(1\); a vertex is its own descendant. The theorem requires no limit and covers the boundary cases \(i=1\), \(j=n\), \(n=2\) (where one or both sizes can be deterministic). The strict dependence statement concerns precisely the nondegenerate cases \(2\le i<j<n\).

## Proof
For \(k\ge i\), write \(S_i(k)\) for the evolving subtree size. The next vertex chooses a parent within that subtree with conditional probability \(S_i(k)/k\). Thus
\[
\mathbb E[S_i(k+1)\mid T_k]=(1+1/k)S_i(k),\qquad \mathbb E S_i(k)=k/i,
\]
using the initial condition \(S_i(i)=1\).

Fix \(i<j\), and let \(A\) indicate that vertex \(j\) belongs to the subtree rooted at \(i\). Since \(j\) attaches uniformly and \(\mathbb E S_i(j-1)=(j-1)/i\), we have \(\mathbb P(A=1)=1/i\). Descendant sets of two vertices are either nested or disjoint. In particular, their intersection at time \(k\ge j\) has cardinality \(A S_j(k)\), since the ancestry indicator \(A\) never changes. Conditional on \(T_k\), put \(\Delta_i=S_i(k+1)-S_i(k)\) and similarly \(\Delta_j\). Then
\[
\mathbb E\Delta_i=\frac{S_i(k)}k,\quad
\mathbb E\Delta_j=\frac{S_j(k)}k,\quad
\mathbb E[\Delta_i\Delta_j]=\frac{A S_j(k)}k.
\]
Therefore
\[
\mathbb E[S_i(k+1)S_j(k+1)\mid T_k]
=\left(1+\frac2k\right)S_i(k)S_j(k)+\frac{A S_j(k)}k.
\]
The future evolution of the subtree born at \(j\), conditional on *any* past tree and on \(A\), has mean \(k/j\). Consequently \(\mathbb E[A S_j(k)]=k/(ij)\). At time \(j\), \(S_j(j)=1\) and
\[
\mathbb E[S_i(j)S_j(j)]=j/i=j^2/(ij).
\]
Inductively, if \(\mathbb E[S_i(k)S_j(k)]=k^2/(ij)\), then the preceding conditional product identity gives
\[
\mathbb E[S_i(k+1)S_j(k+1)]
=\frac{k^2+2k+1}{ij}=\frac{(k+1)^2}{ij}.
\]
This proves the mixed-moment and covariance assertions for every \(k\ge j\).

For the contrast with independence, \(S_i(n)=1\) exactly when no later entrant ever chooses \(i\) as its direct parent. For \(2\le i<j<n\), independent parent choices and elementary telescoping yield
\[
\mathbb P(S_i(n)=1)=\frac{i-1}{n-1},\quad
\mathbb P(S_j(n)=1)=\frac{j-1}{n-1},
\]
\[
\mathbb P(S_i(n)=1,S_j(n)=1)
=\prod_{k=i+1}^{j}\frac{k-2}{k-1}
 \prod_{k=j+1}^{n}\frac{k-3}{k-1}
=\frac{(i-1)(j-2)}{(n-1)(n-2)}.
\]
Subtracting the product of the marginals proves the strictly negative displayed covariance, which precludes independence of the two subtree sizes.

For the diagonal, after birth \(i\) the counts \((S_i(k),k-S_i(k))\) follow a two-color Pólya urn with initial counts \((1,i-1)\). Hence \(S_i(n)-1\) is beta-binomial with \(n-i\) draws and parameters \((1,i-1)\), giving the claimed variance for \(i\ge2\); the formula also gives zero for the deterministic root \(i=1\).

Every vertex of depth \(d\) belongs to precisely \(d+1\) rooted fringe subtrees, establishing \(P_n+n=\sum_iS_i(n)\). Summing the pairwise-zero covariances yields the variance decomposition. Finally, use
\[
\frac{i-1}{i^2(i+1)}=\frac2i-\frac1{i^2}-\frac2{i+1},\quad
\frac{i-1}{i(i+1)}=-\frac1i+\frac2{i+1}
\]
to evaluate the diagonal variance sum exactly as \(n^2(2-H_n^{(2)})-nH_n\).

## Verification
The accompanying `check.py` independently enumerates all recursive trees of orders \(2\) through \(9\), tests the mixed moments, individual variances, strict leaf-indicator covariance, and path-length variance with exact rational arithmetic. It reports 336 successful assertions across 46,233 equally weighted trees. This finite enumeration is a corroboration of the preceding all-size induction, not a substitute for it. Run with `python3 check.py` using only Python's standard library.

## Relationship to prior work
Kuba and Panholzer (2006) determine the *one-label* descendant-size distributions and factorial moments in classes of increasing trees, explicitly including ordinary recursive trees. Their full paper does not state the joint covariance of two distinct birth-labelled subtree sizes. Mahmoud and Smythe (1991) similarly analyze one fixed rooted subtree's size and leaf count. Feng and Mahmoud (2010) analyze counts of prescribed unlabeled fringe subtree shapes rather than mixed moments of specified birth labels. These one-point and aggregate results furnish the background and diagonal moments, but do not directly assert the joint zero-covariance statement or strict dependence of every nonconstant pair. The path-length variance expression is already known; the variance *decomposition into mutually orthogonal labeled-subtree sizes* is the explanatory consequence. No historical uniqueness or priority certification is claimed.

## Limitations
The orthogonality concerns the uniform-recursive-tree model and **linear** covariance of birth-labelled subtree sizes; it does not assert independence, uncorrelatedness of arbitrary functions of these sizes, corresponding results in nonuniform or preferential-attachment trees, or a new derivation of the previously known one-point distributions. Literature retrieval cannot exclude implicit treatment in older multivariate-urn or branching-process formulations.

## References
- Markus Kuba and Alois Panholzer, *Descendants in Increasing Trees*, Electronic Journal of Combinatorics 13 (2006), R8, published 2006-01-25. https://doi.org/10.37236/1034 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r8/pdf/
- Hosam M. Mahmoud and R. T. Smythe, *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, Annals of Applied Probability 1 (1991), 406–418. https://doi.org/10.1214/aoap/1177005874
- Qunqiang Feng and Hosam M. Mahmoud, *On the Variety of Shapes on the Fringe of a Random Recursive Tree*, Journal of Applied Probability 47 (2010), 191–200. https://doi.org/10.1239/jap/1269610825 ; full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BF796C423230F49705548FC5A487F003/S0021900200006483a.pdf/on-the-variety-of-shapes-on-the-fringe-of-a-random-recursive-tree.pdf
