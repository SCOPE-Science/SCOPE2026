# A square-root birth-age crossover in recursive-tree degree–path-length dependence

## Finding

In a uniform random recursive tree on the arrival labels \(1,\ldots,n\), write \(D_{n,i}\) for the number of children of vertex \(i\) and \(L_n\) for the sum of the root-to-vertex edge distances. For every \(n\ge3\) and \(1\le i\le n\), their exact covariance is

\[
C_{n,i}:=\operatorname{Cov}(D_{n,i},L_n)
=\frac ni-1-n\sum_{k=i}^{n-1}\frac1{k^2}+H_{n-1}-H_{i-1},
\tag{1}
\]

where \(H_m=\sum_{k=1}^m k^{-1}\) and empty sums are zero. Moreover,

\[
C_{n,i+1}-C_{n,i}=\frac{n-i(i+1)}{i^2(i+1)},\qquad 1\le i<n.
\tag{2}
\]

Consequently, the covariance is strictly negative at the root, strictly positive at the penultimate arrival, and is unimodal as a function of arrival rank (allowing a single equal pair at the peak). There is exactly one negative-to-nonnegative crossing among the nonterminal birth ranks, and at most one zero there. More precisely, define \(k_n\) as the smallest \(i\in\{2,\ldots,n-1\}\) for which \(C_{n,i}\ge0\). Then all ranks before \(k_n\) have negative covariance, all ranks after \(k_n\) but before \(n\) have strictly positive covariance, and \(C_{n,n}=0\).

This exact finite-size transition takes place at the *mesoscopic* scale

\[
\boxed{\displaystyle k_n\sim \sqrt{\frac{n}{\log n}}\quad(n\to\infty).}
\tag{3}
\]

In fact, for every fixed \(c>0\), putting \(i_n=\lfloor c\sqrt{n/\log n}\rfloor\) for sufficiently large \(n\) gives

\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{C_{n,i_n}}{\log n}
=\frac12\left(1-\frac1{c^2}\right).}
\tag{4}
\]

The finding also resolves the local response to one incoming child. For every \(1\le i<j\le n\),

\[
\boxed{\displaystyle
\operatorname{Cov}\bigl({\bf1}\{P_j=i\},L_n\bigr)
=\frac{n}{j(j-1)}\bigl(1+H_{i-1}-H_{j-1}\bigr).}
\tag{5}
\]

Thus one parent attachment can increase or decrease expected total path length according to its arrival and parent labels, while the aggregate offspring–path-length dependence switches sign at a completely different scale.

## Assumptions and scope

Start with vertex \(1\) as root. Independently for every \(2\le j\le n\), vertex \(j\) chooses its parent \(P_j\) uniformly in \(\{1,\ldots,j-1\}\). Define \(\operatorname{depth}(1)=0\) and \(\operatorname{depth}(j)=1+\operatorname{depth}(P_j)\). Set \(L_n=\sum_{v=1}^n\operatorname{depth}(v)\) and \(D_{n,i}=\sum_{j=i+1}^n {\bf1}\{P_j=i\}\). Covariances are population covariances under this finite probability law. Formulae include the root and the deterministic zero offspring count at \(i=n\), with no regularity hypothesis beyond independent uniform attachment.

## Proof

**Local response.** Fix \(1\le i<j\le n\). Let \(S_{j,n}\) count vertices in the final descendant subtree rooted at \(j\), including \(j\). The set of descendants of \(j\) is unaffected by the choice of \(P_j\); it depends only on later parent choices, which are independent of \(P_j\) and the pre-arrival tree. By the urn-type subtree-size recursion, when the entire tree has \(t\) vertices, an existing subtree of size \(s\) receives the next vertex with probability \(s/t\). Starting with size one at time \(j\), this yields

\[
\mathbb E S_{j,n}=n/j.
\tag{6}
\]

If the parent of \(j\) is varied while every other parent choice is held fixed, precisely the vertices in this subtree shift depth by the same amount. Therefore the part of \(L_n\) that depends on \(P_j\) is

\[
S_{j,n}\bigl(1+\operatorname{depth}(P_j)\bigr).
\tag{7}
\]

The remaining part of \(L_n\) does not depend on \(P_j\). Independently of future attachment choices, the standard recursive-depth recursion gives \(\mathbb E\operatorname{depth}(r)=H_{r-1}\) for each \(r\ge1\). Consequently,

\[
\mathbb E\operatorname{depth}(P_j)
=\frac1{j-1}\sum_{r=1}^{j-1}H_{r-1}=H_{j-1}-1.
\tag{8}
\]

For the Bernoulli indicator \(A_{ij}={\bf1}\{P_j=i\}\), use \(\mathbb P(A_{ij}=1)=1/(j-1)\), (6)–(8), and independence to obtain

\[
\begin{aligned}
\operatorname{Cov}(A_{ij},L_n)
&=\frac1{j-1}\bigl(\mathbb E[L_n\mid P_j=i]-\mathbb E L_n\bigr)\\
&=\frac{n}{j(j-1)}\bigl(H_{i-1}-(H_{j-1}-1)\bigr),
\end{aligned}
\]

which is (5), including the degenerate case \(j=2\).

**Summation.** By linearity of covariance and the definition of \(D_{n,i}\),

\[
C_{n,i}=n\sum_{j=i+1}^n
\frac{1+H_{i-1}-H_{j-1}}{j(j-1)}.
\tag{9}
\]

Expand \(H_{j-1}-H_{i-1}=\sum_{k=i}^{j-1}1/k\), interchange the two finite sums, and use \(\sum_{j=k+1}^n[j(j-1)]^{-1}=1/k-1/n\). This gives

\[
\begin{aligned}
C_{n,i}
&=n\left(\frac1i-\frac1n\right)
-n\sum_{k=i}^{n-1}\frac1k\left(\frac1k-\frac1n\right)\\
&=\frac ni-1-n\sum_{k=i}^{n-1}\frac1{k^2}
+H_{n-1}-H_{i-1},
\end{aligned}
\]

proving (1). Subtracting successive expressions gives (2).

**One crossing.** For the root, every term in (9) is nonpositive, and every term with \(j\ge3\) is strictly negative; hence \(C_{n,1}<0\) for \(n\ge3\). For \(i=n-1\), equation (5) yields \(C_{n,n-1}=(n-2)/(n-1)^2>0\). And \(C_{n,n}=0\). Equation (2) shows that \(C_{n,i}\) increases until the integer neighborhood of \(\sqrt n\), and then decreases, with at most one zero difference. Since its decreasing tail ends at zero and its penultimate value is positive, the negative-to-nonnegative crossing can only occur on the increasing side. It is unique and has the stated sign pattern.

**Sharp mesoscopic scale.** Euler–Maclaurin summation, or elementary integral bounds with one trapezoidal correction, yields uniformly for \(i\to\infty\) and \(i\le n\),

\[
\sum_{k=i}^{n-1}\frac1{k^2}
=\frac1i-\frac1n+\frac1{2i^2}-\frac1{2n^2}
+O(i^{-3}),
\tag{10}
\]

while \(H_{n-1}-H_{i-1}=\log(n/i)+O(i^{-1})\). Substitution into (1) gives

\[
C_{n,i}=\log(n/i)-\frac{n}{2i^2}
+O\!\left(\frac{n}{i^3}+\frac1i+\frac1n\right).
\tag{11}
\]

At \(i=\lfloor c\sqrt{n/\log n}\rfloor\), the remainder in (11) is \(o(1)\), \(\log(n/i)=(\log n)/2+O(\log\log n)\), and \(n/(2i^2)=(\log n)/(2c^2)+o(1)\). Dividing by \(\log n\) proves (4). Fixing any \(c<1\) and any \(c>1\), formula (4) gives eventually opposite signs at the corresponding two ranks; uniqueness of the finite sign crossing therefore proves (3).

## Verification

The standalone file `verify_path_degree.py` independently enumerates all \((n-1)!\) recursive parent vectors for each \(3\le n\le9\) and uses exact rational arithmetic to compare every applicable local covariance (5) and global covariance (1). It separately verifies the finite summation formula, the telescoping difference (2), the sign pattern, and the conservation identity \(\sum_i C_{n,i}=0\) across \(3\le n\le150\). Numerical diagnostics at larger sizes test the asymptotic normalization (4). Running `python verify_path_degree.py` reports `VERIFY_OK 12134 exact/diagnostic assertions`. The infinite statements are consequences of the displayed proof, not finite enumeration.

## Relationship to prior work

Eslava (2016) and Lodewijks (first posted 2022) study the joint behavior of degrees and individual vertex depths of recursive trees; these are different from covariance of a *prescribed vertex's offspring count* with the *entire tree's total path length*. Dobrow and Fill (1999) study the total path-length statistic itself. A published result on root attachments establishes the \(i=1\) specialization of (5) and its stronger stochastic-order consequence; that root case is explicitly prior and is **not** the new contribution here. The new assertion is the complete birth-rank profile, the single sign boundary for \(i\ge2\), and its nontrivial \(\sqrt{n/\log n}\) scaling.

The fixed-label offspring–leaf covariance law also has a birth-rank sign transition, but its second statistic and its macroscopic transition scale are different. Neither its formula nor the root-only path-length result entails the present nonroot covariance law by specialization; nonetheless, the local coupling argument is close to the earlier root-only method and this is a material originality limitation.

## Limitations

The theorem concerns *covariance*, not stochastic monotonicity of total path length given the entire offspring count of a nonroot vertex. It uses independent uniform parent selection; unequal attachment weights generally change both the average depth of the selected parent and the descendant growth factor. The critical scale is an asymptotic first-order equivalent, not a closed-form integer threshold at every order. Earlier bivariate generating-function work may encode the same mixed moments under different notation, which is a remaining historical-priority risk.

## References

1. L. Eslava, “Depth of vertices with high degree in random recursive trees,” arXiv:1611.07466, first publicly posted 2016-11-22, https://arxiv.org/abs/1611.07466. Primary classification 60C05.
2. B. Lodewijks, “On joint properties of vertices with a given degree or label in the random recursive tree,” arXiv:2204.09032, first publicly posted 2022-04-19, https://arxiv.org/abs/2204.09032.
3. R. P. Dobrow and J. A. Fill, “Total Path Length for Random Recursive Trees,” *Combinatorics, Probability and Computing* 8 (1999), 317–333, https://doi.org/10.1017/S0963548399003855.
4. “Root attachments have an exact negative path-length profile in random recursive trees,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba.
5. M. Drmota and H.-K. Hwang, “Profiles of random trees: correlation and width of random recursive trees and binary search trees,” *Advances in Applied Probability* 37 (2005), 321–341, https://doi.org/10.1239/aap/1118858628 (level-size correlations; different observables).
