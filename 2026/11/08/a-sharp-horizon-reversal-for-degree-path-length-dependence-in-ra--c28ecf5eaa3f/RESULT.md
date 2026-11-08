# A sharp horizon reversal for degree–path-length dependence in random recursive trees

## Finding

In a uniform random recursive tree on \(n\ge2\) vertices labeled by arrival time, let \(D_{n,i}\) be the number of children of vertex \(i\), and let \(T_n=\sum_{v=1}^n d(1,v)\) be total root-to-vertex path length. The parent \(P_j\) of vertex \(j\ge2\) is uniform on \(\{1,\ldots,j-1\}\), independently over \(j\). Define \(H_m=\sum_{k=1}^m1/k\) and \(H_m^{(2)}=\sum_{k=1}^m1/k^2\), with \(H_0=H_0^{(2)}=0\).

For every \(1\le i\le n\), the *exact labeled degree/path-length covariance* is
\[
\boxed{\operatorname{Cov}(D_{n,i},T_n)=n\sum_{j=i+1}^n\frac{H_{i-1}+1-H_{j-1}}{j(j-1)}
=\frac{n(i-1)}{i^2}+H_n-H_{i-1}-1-n(H_n^{(2)}-H_i^{(2)}).}
\tag{1}
\]
The empty sum for \(i=n\) is zero. For the root \(i=1\), the covariance is negative for \(n\ge3\) (and zero for \(n=2\)), recovering the known root-degree phenomenon. For **every nonroot label \(i\ge2\)**, however, the sign depends on how long tree growth continues:

* At the first possible stage, \(n=i+1\), the covariance is strictly positive.
* As \(n\) increases, the covariance is positive, then may be zero at a single integer order, then is strictly negative for all sufficiently large \(n\). The transition is unique: there is an integer \(N_i>i+1\) such that the covariance is positive for \(i<n<N_i\), nonpositive at \(N_i\), and strictly negative for \(n>N_i\).
* The threshold has a sharp large-label scale:
\[
\boxed{\lim_{i\to\infty}\frac{N_i}{i^2\log i}=2.}
\tag{2}
\]
In the double scaling \(n/(i^2\log i)\to c>0\), the unnormalised sum \(S_{n,i}:=\operatorname{Cov}(D_{n,i},T_n)/n\) satisfies
\[
\boxed{i^2S_{n,i}\longrightarrow\frac1c-\frac12.}
\tag{3}
\]
This shows how a fixed nonroot vertex initially correlates positively with search cost but eventually correlates negatively when sufficiently many later descendants have had opportunities to appear. The crossover is at a quadratic-logarithmic observation horizon in the marked birth label.

## Assumptions and scope

The model is the standard uniform recursive tree: for each \(j\ge2\), the parent \(P_j\) is chosen independently and uniformly among the earlier birth labels. All depths count edges from root \(1\), all degrees are *outdegrees*, and the random variables are observed in the same tree. Equation (1) holds for all integers \(n\ge2\), \(1\le i\le n\). The unique-transition statement holds separately for each fixed \(i\ge2\); it allows equality to zero at at most one integer horizon and does not assert a closed formula for \(N_i\). Equations (2)–(3) concern positive integer sequences with \(i\to\infty\) and \(n>i\). No analogous statement is asserted for weighted attachments.

## Proof

**1. The effect of a single attachment.** For \(i<j\le n\), put \(A_{j,i}=\mathbf1\{P_j=i\}\). The outdegree is \(D_{n,i}=\sum_{j=i+1}^n A_{j,i}\). Couple two recursive trees using identical parent choices except for the parent of \(j\). The set of descendants of vertex \(j\), including \(j\), depends only on future parent choices and is unchanged when this parent edge is replaced. Let \(S_{j,n}\) be the final descendant-subtree size. Standard uniform-attachment growth gives \(\mathbb E S_{j,n}=n/j\), independent of the pre-\(j\) tree and \(P_j\).

The change in total path length caused by moving the parent of \(j\) from \(q\) to \(r\) is exactly \(S_{j,n}(d(1,r)-d(1,q))\). Consequently, using independence of future attachments,
\[
\mathbb E[T_n\mid P_j=i]-\mathbb E T_n
=\frac nj\left(\mathbb E d(1,i)-\frac1{j-1}\sum_{q=1}^{j-1}\mathbb E d(1,q)\right).
\tag{4}
\]
In a recursive tree, \(\mathbb E d(1,q)=H_{q-1}\), and the expected total path length at time \(j-1\) equals \((j-1)(H_{j-1}-1)\). Thus (4) equals \((n/j)(H_{i-1}+1-H_{j-1})\).

**2. The local and total covariance.** For an event \(B\) and integrable \(X\), \(\operatorname{Cov}(\mathbf1_B,X)=\mathbb P(B)[\mathbb E(X\mid B)-\mathbb EX]\). Since \(\mathbb P(P_j=i)=1/(j-1)\),
\[
\boxed{\operatorname{Cov}(A_{j,i},T_n)=\frac{n(H_{i-1}+1-H_{j-1})}{j(j-1)}.}
\tag{5}
\]
Sum over \(j=i+1,\ldots,n\) to get the first equality in (1). The finite identity
\[
\frac{H_{j-1}}{j(j-1)}=\frac{H_{j-1}}{j-1}-\frac{H_j}{j}+\frac1{j^2}
\tag{6}
\]
telescopes to the second equality. In particular, the \(i=1\) formula becomes \(H_n-1-n(H_n^{(2)}-1)\), negative for \(n\ge3\), consistently with the known root case. For \(i=n\), the outdegree is deterministically zero.

**3. Unique horizon sign reversal.** Fix \(i\ge2\), and divide (1) by \(n\). Define
\[
S_{n,i}=\sum_{j=i+1}^n\frac{H_{i-1}+1-H_{j-1}}{j(j-1)}.
\tag{7}
\]
Its first term is \((1-1/i)/(i(i+1))>0\). Since \(H_{j-1}\) increases strictly in \(j\), the increments \(S_{n,i}-S_{n-1,i}\) start positive and then become strictly negative, with at most one zero increment. The infinite series has the exact limit
\[
S_{\infty,i}=\frac{i-1}{i^2}-\sum_{j=i+1}^{\infty}\frac1{j^2}<0,
\tag{8}
\]
because \(\sum_{j=i+1}^\infty j^{-2}>\int_{i+1}^\infty x^{-2}\,dx=1/(i+1)>(i-1)/i^2\). Thus the positive partial sums eventually cross zero while decreasing, and cannot cross back. Define \(N_i:=\min\{n>i:S_{n,i}\le0\}\). This exists and proves the unique-transition assertion. Note that \(S_{n,i}\) and \(\operatorname{Cov}(D_{n,i},T_n)=nS_{n,i}\) have identical signs since \(n>0\).

**4. Quadratic-logarithmic transition scale.** Expanding the tail of the inverse-square series gives
\[
S_{\infty,i}=-\frac1{2i^2}+O(i^{-3})
\qquad(i\to\infty).
\tag{9}
\]
From (1) and (8),
\[
S_{n,i}-S_{\infty,i}=\frac{H_n-H_{i-1}-1}{n}+\sum_{j=n+1}^{\infty}\frac1{j^2}
=\frac{H_n-H_{i-1}}n+O(n^{-2}).
\tag{10}
\]
For any fixed \(c>0\), setting \(n=\lfloor c i^2\log i\rfloor\) gives \(H_n-H_{i-1}=\log(n/i)+O(1/i)=\log i+O(\log\log i)\). Therefore (9)–(10) yield
\[
i^2 S_{n,i}=\frac1c-\frac12+o(1).
\]
The same expansion applies if \(n/(i^2\log i)\to c\), proving (3). The unique sign reversal from Step 3 implies that for any \(c_-<2<c_+\), and all sufficiently large \(i\), the threshold lies between \(c_-i^2\log i\) and \(c_+i^2\log i\). Letting \(c_-\uparrow2\) and \(c_+\downarrow2\) proves (2).

## Verification

The accompanying `verify.py` is standalone Python standard-library code. Running `python verify.py` exhaustively enumerates all recursive-tree parent sequences through \(n=9\), computes \(\operatorname{Cov}(D_{n,i},T_n)\) by direct exact-rational averaging, and compares those values against *both* representations in (1) for every label. It also tests the zero sum over labels, because the total outdegree equals \(n-1\) deterministically. A separate numerical grid of birth labels up to \(69\) checks that the partial-sum signs switch at most once and eventually turn negative. The program completed with 120 exact-enumeration/analytic and numerical threshold assertions passed. The all-size theorem is proved above, not inferred from the finite checks.

## Relationship to prior work

Dobrow and Fill (1999) develop the uniform recursive tree's total path-length moments and its independent-parent construction, without a labeled degree/path-length covariance. A later root-specific theorem establishes that attachments directly to the root shorten total path length and supplies exactly the special case \(i=1\) of (5). Neither prior statement gives the nonroot positive-to-negative horizon reversal or the sharp transition (2).

Lodewijks (2022, revised 2023) studies the joint degrees, depths, birth labels, and graph distances of individual recursive-tree vertices and a finite number of them. The inspected full-text introduction and main results do not sum over the depths of *all* vertices to obtain the mixed total-path-length covariance, and do not give a degree-dependent observation-horizon threshold. Earlier degree-distribution papers (e.g., Janson 2004/2005) study covariance among degree-count statistics rather than a marked vertex's degree against total path length. These settings are related but not statement-equivalent.

The general path-length/leaf-number study of Lundblad and Wagner (2026) focuses on external path length and average leaf distance rather than marked vertex outdegree, and does not state (2). Related finite-moment identities might be obtainable by extensions of their generating-function methods, which is a residual historical-coverage risk. Searches for birth-label degree/path-length covariance and its horizon sign reversal did not locate a prior theorem. No uniqueness of historical priority is asserted.

## Limitations

The result uses independent, uniform attachment. Weighted or preferential recursive trees would have different expected subtree sizes and parent-depth averages. The finding is about covariance, not the joint distribution, stochastic domination or nonlinear association. The integer transition \(N_i\) is characterized uniquely but not given by a closed elementary expression; its leading asymptotic is proved. A broader multivariate generating-function or degree-depth theorem could implicitly imply (1) after further summation, but the checked papers do not provide the sharp nonroot reversal classification and scale as a stated result.

## References

1. R. P. Dobrow and J. A. Fill, “Total Path Length for Random Recursive Trees,” *Combinatorics, Probability and Computing* **8** (1999), 317–333, DOI: https://doi.org/10.1017/S0963548399003855; publicly dated 1999-07-01.
2. B. Lodewijks, “On joint properties of vertices with a given degree or label in the random recursive tree,” arXiv:2204.09032, first posted 2022-04-19; *Electronic Journal of Probability* **27** (2022), article 145. https://arxiv.org/abs/2204.09032. This is later supporting literature, not the archive source anchor.
3. S. Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* **26** (2005), 69–83, DOI: https://doi.org/10.1002/rsa.20046; publicly dated 2004-11-16.
4. J. Lundblad and S. Wagner, “Path Length and External Path Length in Random Trees,” *LIPIcs AofA* **381** (2026), article 2, DOI: https://doi.org/10.4230/LIPIcs.AofA.2026.2; published 2026-07-13. Later supporting literature only.
