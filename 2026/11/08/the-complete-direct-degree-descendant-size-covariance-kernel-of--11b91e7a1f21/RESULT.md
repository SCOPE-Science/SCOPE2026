# The complete direct-degree–descendant-size covariance kernel of random recursive trees

## Finding

Choose a uniformly random recursive rooted tree on labels \(1,\ldots,n\) by making each new vertex \(t+1\) attach independently to a uniformly chosen parent in \(\{1,\ldots,t\}\). Let \(D_i\) be the number of **direct children** of vertex \(i\), and let \(S_j\) be the number of vertices in the entire rooted subtree of \(j\), including \(j\). For every integer \(n\ge2\) and all \(1\le i,j\le n\),

\[
\operatorname{Cov}(D_i,S_j)=
\begin{cases}
-\dfrac{n-j}{j^2},&i<j,\\[3pt]
\dfrac{(n-j)(j-1)}{j^2},&i=j,\\[3pt]
0,&i>j.
\end{cases}
\]

Consequently every nontrivial column \(2\le j<n\) has equal strictly negative entries for all older labels \(i<j\), one strictly positive diagonal entry, and zero entries for all younger labels \(i>j\). The entire first column and final column vanish. The positive diagonal entry equals the absolute sum of the preceding negative entries.

## Assumptions and scope

The vertex labels are insertion times, not an exchangeable relabeling. Each parent choice is independent and uniform among older labels. \(D_i\) counts **immediate** offspring; \(S_j\) counts all descendants plus the vertex itself. Covariance uses the uniform distribution over the \((n-1)!\) possible parent-choice sequences. The formula applies to every finite \(n\ge2\), without asymptotic assumptions.

## Proof

Write \(\mathcal F_t\) for all parent choices through time \(t\), \(S_j(t)\) for the size of the subtree of \(j\) at time \(t\), and, for \(t\ge i\), \(B_{i,t}=\mathbf1\{\text{vertex }t+1\text{ chooses parent }i\}\). Then \(D_i=\sum_{t=i}^{n-1}B_{i,t}\).

For \(t\ge j\), the next vertex joins the subtree of \(j\) with conditional probability \(S_j(t)/t\), so

\[
\mathbb E[S_j(t+1)\mid\mathcal F_t]=(1+t^{-1})S_j(t),\quad
\mathbb E S_j(t)=t/j,\quad
\mathbb E[S_j(n)\mid\mathcal F_{t+1}]=\frac n{t+1}S_j(t+1).
\]

For \(t<j\), the expected final subtree size \(\mathbb E[S_j(n)\mid\mathcal F_t]=n/j\) is deterministic: the later parent choices generate the subtree of vertex \(j\) without dependence on earlier parent choices. Hence \(\operatorname{Cov}(B_{i,t},S_j(n))=0\) for \(t<j\).

For \(t\ge\max\{i,j\}\), put \(p_{ij}=\mathbb P(i\text{ lies in the rooted subtree of }j\text{ at time }t)\). This probability is independent of \(t\) once both vertices exist. By increasing labels, \(p_{ij}=0\) when \(i<j\), and \(p_{jj}=1\). If \(i>j\), vertex \(i\) enters the subtree of \(j\) with probability \(\mathbb E S_j(i-1)/(i-1)=1/j\); so \(p_{ij}=1/j\) in this case.

Given \(\mathcal F_t\), the new parent is uniform. For \(t\ge\max\{i,j\}\), since \(S_j(t+1)=S_j(t)+\mathbf1\{\text{new parent lies in subtree of }j\}\),

\[
\mathbb E[B_{i,t}S_j(t+1)\mid\mathcal F_t]
=\frac{S_j(t)+\mathbf1\{i\text{ in subtree of }j\}}t.
\]

Combining this with \(\mathbb E B_{i,t}=1/t\), \(\mathbb E S_j(t+1)=(t+1)/j\), and the preceding conditional-mean identity gives

\[
\operatorname{Cov}(B_{i,t},S_j(n))
=\frac{n}{t(t+1)}\left(p_{ij}-\frac1j\right).
\]

Summing over the allowed insertion steps and using the telescoping identity
\[
\sum_{t=m}^{n-1}\frac1{t(t+1)}=\frac1m-\frac1n
\]
proves the three claimed cases. For \(i<j\), the sum begins at \(j\), giving \(-(n-j)/j^2\); for \(i=j\), it produces \((n-j)(j-1)/j^2\); for \(i>j\), every summand vanishes. This also proves both boundary columns. The equality of negative predecessor contributions precisely balances the diagonal contribution, consistent with the deterministic identity \(\sum_{i=1}^{n}D_i=n-1\).

## Verification

The included standalone Python 3 checker `verify_degree_subtree.py` uses only the standard library. Run `python3 verify_degree_subtree.py`. It enumerates all \((n-1)!\) parent sequences for each \(2\le n\le9\), computes exact rational covariances for all ordered pairs \((i,j)\), and compares them with the piecewise formula; it also checks the expected direct-degree profile and column-sum conservation through \(n=109\). The observed replay was `PASS 6322 exact checks; all recursive trees with <=9 nodes enumerated`. These finite checks are corroboration; the proof above establishes the infinite family.

## Relationship to prior work

Kuba and Panholzer (2006) determine the descendant-size distribution in increasing trees. Their 2007 study develops birth-indexed vertex-degree laws, and their 2009 descendant analysis supplies joint distributions of descendant sizes for two chosen vertices. The present statistic instead pairs one vertex's **direct** child count with a possibly different vertex's full descendant count. Marginal degree or descendant formulas, or a bivariate descendant-count distribution alone, do not determine the direct-degree–descendant covariance matrix without additional joint information. Earlier general increasing-tree methods may nevertheless imply the displayed kernel after further specialization, which remains an explicit priority risk.

## Limitations

This result is specific to the uniform recursive-tree attachment rule, rather than general preferential or weight-biased attachment; it gives second mixed moments, not a complete joint distribution or independence for \(i>j\). Zero covariance must not be interpreted as independence. Historical priority has been checked against the named primary texts and published-record searches but is not conclusively established by search absence. Independent mathematical audit has not been performed.

## References

- M. Kuba and A. Panholzer, *Descendants in Increasing Trees*, Electronic Journal of Combinatorics (public 25 January 2006), https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r8.
- M. Kuba and A. Panholzer, *On the degree distribution of the nodes in increasing trees*, Journal of Combinatorial Theory, Series A 114 (2007), 597–618, doi:10.1016/j.jcta.2006.08.003; author PDF https://www.dmg.tuwien.ac.at/kuba/nodedegree3.pdf.
- M. Kuba and A. Panholzer, *A combinatorial approach for analyzing the number of descendants in increasing trees and related parameters*, Quaestiones Mathematicae 32 (2009), 91–117; author preprint https://www.dmg.tuwien.ac.at/kuba/preprintcombdesc.pdf.
