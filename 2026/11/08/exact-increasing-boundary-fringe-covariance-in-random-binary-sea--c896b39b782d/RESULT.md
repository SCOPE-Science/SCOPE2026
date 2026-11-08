# Exact increasing boundary–fringe covariance in random binary search trees

## Finding
Consider the ordinary binary search tree formed by inserting a uniformly random permutation of \(n\) distinct totally ordered keys. Write \(L_n\) for the number of nonempty vertices along the leftmost path from the root to the minimum key (both endpoints counted), and \(Z_n\) for the number of ordinary childless vertices (internal leaves). For every integer \(n\ge2\),
\[
\operatorname{Cov}(L_n,Z_n)=\begin{cases}
0,&n=2,\\
\dfrac{(n-2)(n+1)}{12n(n-1)},&n\ge3.
\end{cases}
\]
The covariance is strictly positive for every \(n\ge3\), increases strictly with \(n\) for \(n\ge3\), and converges to \(1/12\). More precisely,
\[
\operatorname{Cov}(L_n,Z_n)-\operatorname{Cov}(L_{n-1},Z_{n-1})
=\frac1{3n(n-1)(n-2)}\quad(n\ge4).
\]
This is a boundary-to-global-fringe dependence law: the expected cost of locating the smallest key and the total number of terminal records have a positive, size-stable covariance even though their standardized correlation vanishes.

## Assumptions and scope
For every integer \(n\ge0\), keys are inserted independently of their values in a uniform random ordering; equivalently, the root key has uniform rank in \(\{1,\ldots,n\}\), and conditional on this rank the left and right subtrees are independent random BSTs of their respective sizes. A subtree of size zero is empty, with both statistics defined as zero. For a singleton, \(L_1=Z_1=1\). An ordinary internal leaf has zero nonempty children, not an external null child; a BST has exactly \(n+1\) external null positions, and counting those would be deterministic.

## Proof
Let \(K\) denote the number of keys in the root's left subtree. For \(n\ge2\), conditional on \(K=k\), with independent copies of subtree statistics,
\[
L_n=1+L_k^{(\mathrm{left})},\qquad
Z_n=Z_k^{(\mathrm{left})}+Z_{n-1-k}^{(\mathrm{right})}.
\]
The singleton has one ordinary leaf, so the above decomposition is used only for \(n\ge2\). Write \(a_n=\mathbb E L_n\), \(b_n=\mathbb E Z_n\), and \(v_n=\operatorname{Cov}(L_n,Z_n)\), with \(a_0=b_0=v_0=0\), \(a_1=b_1=1\), and \(v_1=0\). Averaging over uniform \(K\) gives
\[
a_n=1+\frac1n\sum_{k=0}^{n-1}a_k=H_n,\qquad
b_n=\frac2n\sum_{k=0}^{n-1}b_k=\frac{n+1}{3}\quad(n\ge2),
\]
where \(H_k=\sum_{j=1}^k1/j\) and \(H_0=0\). The leaf recurrence holds for \(n\ge2\) and starts from \(b_1=1\).

By the law of total covariance and conditional independence of the two subtrees,
\[
v_n=\frac1n\sum_{k=0}^{n-1}v_k+
\operatorname{Cov}_{K}\bigl(H_K,b_K+b_{n-1-K}\bigr),\qquad n\ge2.
\]
For \(n\ge3\) and every \(0\le k\le n-1\), the exceptional singleton and empty-subtree cases are encoded exactly by
\[
b_k+b_{n-1-k}=\frac{n+1}{3}+
\frac{{\bf1}_{\{k=1\}}+{\bf1}_{\{k=n-2\}}-{\bf1}_{\{k=0\}}-{\bf1}_{\{k=n-1\}}}{3}.
\]
The two positive indicators coincide when \(n=3\); both contributions must be retained. The corrections sum to zero over uniform \(K\), hence
\[
\operatorname{Cov}_{K}(H_K,b_K+b_{n-1-K})
=\frac{H_1+H_{n-2}-H_0-H_{n-1}}{3n}
=\frac{n-2}{3n(n-1)}.
\]
Thus, with \(v_2=0\),
\[
v_n=\frac1n\sum_{k=0}^{n-1}v_k+\frac{n-2}{3n(n-1)},\quad n\ge3.
\]
The case \(n=3\) yields \(v_3=1/18\). Subtracting the recurrence at successive sizes for \(n\ge4\) gives
\[
v_n-v_{n-1}=\frac1{3n(n-1)(n-2)}.
\]
Indeed, multiplying the recurrence by \(n\) and using the \(n-1\) recurrence leads to \(n(v_n-v_{n-1})=(n-2)/[3(n-1)]-(n-3)/[3(n-2)]\). Summing the increments from \(v_3\), or direct substitution, gives \(v_n=(n-2)(n+1)/[12n(n-1)]\) for all \(n\ge3\). Positivity, monotonicity and the limit follow.

Additionally \(\operatorname{Var}(L_n)=H_n-\sum_{j=1}^n1/j^2\) by the independent-record representation, and the standard fringe-leaf calculation gives \(\operatorname{Var}(Z_n)=2(n+1)/45\) for \(n\ge4\). Consequently
\[
\operatorname{Corr}(L_n,Z_n)\sim
\frac{\sqrt{45/2}}{12\sqrt{n\log n}}.
\]

## Verification
Run `python bst_spine_leaf_checker.py` with Python 3 standard library only. The checker constructs the exact rational moments from independent-subtree recurrences through \(n=300\) and independently enumerates all \(n!\) insertion orders for \(1\le n\le8\). It checks the tree statistics against records and permutation peaks, the exact formula and all successive increments. The check reported `PASS: 47438 exact assertions; n<=8 permutation exhaustive, n<=300 rational recurrence`. Those finite calculations corroborate but do not replace the proof above.

## Relationship to prior work
Holmgren and Janson, *Limit laws for functions of fringe trees for binary search trees and recursive trees*, first public arXiv version June 26, 2014, treats ordinary BST fringe-size-one counts and supplies their exact marginal mean and variance. It studies additive fringe functionals but does not state the mixed covariance with a distinguished extreme-key root-to-leaf path. Bóna and Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, arXiv first public version December 8, 2014, studies distances to leaves across the tree, rather than the extreme-key spine and its joint covariance with terminal vertices. The boundary-path statistic is not a fixed-size fringe sum, so their marginal results do not directly imply the mixed law. Earlier record/peak joint-enumeration results could conceivably yield the same formula after translation; historical priority is not independently certified.

## Limitations
The claim applies to uniform-permutation ordinary BSTs only, not uniformly chosen Catalan-shaped binary trees or deterministic insertion sequences. Leaf means are for ordinary childless vertices, not external null positions. Zero correlation asymptotically does not establish independence. Literature searches and inspected primary works do not establish exhaustive historical priority; general permutation peak–record methods may implicitly encompass the covariance.

## References
1. C. Holmgren and S. Janson, *Limit laws for functions of fringe trees for binary search trees and recursive trees*, arXiv:1406.6883v1, June 26, 2014, https://arxiv.org/html/1406.6883v1 .
2. M. Bóna and B. Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, arXiv:1412.2796v1, December 8, 2014, https://arxiv.org/abs/1412.2796 .
