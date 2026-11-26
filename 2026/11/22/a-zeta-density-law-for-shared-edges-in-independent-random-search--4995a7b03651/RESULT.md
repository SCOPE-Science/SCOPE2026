# A zeta-density law for shared edges in independent random search trees

## Finding

Let \(T_n^{(1)}\) and \(T_n^{(2)}\) be independent binary search trees produced by inserting the ordered keys \(1,\ldots,n\) in independent uniformly random permutations. Let \(E(T)\) consist of unordered pairs of key labels joined by a **direct parent–child edge**, and set \(H_n=|E(T_n^{(1)})\cap E(T_n^{(2)})|\). For every integer \(n\ge2\), the probability of an undirected edge \(\{i,j\}\), for \(1\le i<j\le n\) and \(d=j-i\), is exactly

\[
q_{n;i,j}=\frac{1}{d(d+1)}+\frac{1}{2(n-i)(n-i+1)}+\frac{1}{2(j-1)j}.
\]

Consequently the common-edge expectation is exactly \(\sum_{i<j}q_{n;i,j}^{2}\), and

\[
\mathbb E H_n=\left(\frac{\pi^2}{3}-3\right)n+\frac{5\pi^2}{12}-3+O(n^{-1}),
\qquad
\frac{H_n}{n}\longrightarrow \frac{\pi^2}{3}-3
\quad\text{in }L^1.
\]

The limiting proportion of shared direct edges is approximately \(0.289868133696\), despite the two insertion orders being independent. The result concerns key-labelled **parent–child edges**, not common subtree shapes, ancestor pairs, or common sets of keys.

## Assumptions and scope

The key set is the deterministic ordered set \(\{1,\ldots,n\}\). Each tree is formed by ordinary binary-search-tree insertion without rotations. The two insertion permutations are independent and uniform. Equivalently, assign independent continuous uniform priorities \(U_i^{(a)}\) to the keys for each sample \(a\in\{1,2\}\), with smaller priority inserted earlier. All equalities at finite \(n\) are exact, including at the boundary keys. No assertion is made about a tree selected uniformly from Catalan shapes or a uniformly labelled Cayley tree.

## Proof

**1. Exact direct-edge kernel.** In the Cartesian/minimum-priority representation, the parent of a nonroot key \(j\) is the nearer lower-priority key on either side having the *larger* of the two lower priorities; missing-side candidates are ignored. Fix \(i<j\), put \(d=j-i\), and condition on \(U_i=u<U_j=v\). For \(i\) to be the parent of \(j\), all \(d-1\) interior priorities must exceed \(v\). The first priority below \(v\) on the right of \(j\), if present, must be below \(u\). With \(n-j\) right-hand keys, the conditional probability of this last requirement is

\[
\frac uv+\left(1-\frac uv\right)(1-v)^{n-j}.
\]

Integrating over \(0<u<v<1\) gives

\[
\Pr(i\text{ is parent of }j)
=\int_0^1\frac v2(1-v)^{d-1}\bigl[1+(1-v)^{n-j}\bigr]dv
=\frac1{2d(d+1)}+\frac1{2(n-i)(n-i+1)}.
\]

By reflecting the key order,

\[
\Pr(j\text{ is parent of }i)
=\frac1{2d(d+1)}+\frac1{2(j-1)j}.
\]

The two orientations are disjoint. Their sum is \(q_{n;i,j}\). Independence of the two sampled trees gives the exact common-edge expectation.

**2. Asymptotic expectation with its boundary correction.** Write \(a_d=1/[d(d+1)]\), \(b_s=1/[s(s+1)]\), \(s=n-i\), and \(t=j-1\). Expansion of the square and reflection of the key order give the exact identity

\[
\begin{aligned}
\mathbb E H_n={}&\sum_{d=1}^{n-1}(n-d)a_d^2
+2\sum_{s=1}^{n-1}\frac{1}{(s+1)^2}
+\frac12\sum_{s=1}^{n-1}s b_s^2\\
&+\frac12\sum_{\substack{1\le s,t\le n-1\\s+t\ge n}}b_s b_t.
\end{aligned}
\]

Here \(\sum_{d\ge1}a_d^2=2\zeta(2)-3\), \(\sum_{d\ge1}d a_d^2=2-\zeta(2)\), and \(\sum_{s\ge1}s b_s^2=2-\zeta(2)\). The final double sum is \(O(n^{-1})\): when \(s+t\ge n\), at least one index is at least \(n/2\), and the tail of \(\sum_s b_s\) is \(O(n^{-1})\). The other truncated series have errors \(O(n^{-1})\) or smaller. Therefore

\[
\mathbb E H_n=n(2\zeta(2)-3)+\frac52\zeta(2)-3+O(n^{-1}),
\]

and \(\zeta(2)=\pi^2/6\) yields the displayed expansion.

**3. Law of large numbers.** Extend both independent priority arrays to all integer keys. Each key almost surely has a lower-priority key on either side, so the same nearest-lower-priority rule defines a stationary infinite Cartesian parent graph (every vertex has one parent and at most two children). The event that \(i\) and \(i+d\) are adjacent in this graph has probability \(a_d\): the two boundary terms in the finite kernel vanish when both endpoints are infinitely far from the boundary.

Let \(Y_i\) be the number of edges \(\{i,j\}\) with \(j>i\) shared by these two infinite graphs. Then \(0\le Y_i\le3\), the process is an ergodic factor of independent identically distributed priority sequences, and \(\mathbb E Y_i=\sum_{d\ge1}a_d^2=2\zeta(2)-3\). The ergodic theorem, with boundedness, yields \(n^{-1}\sum_{i=1}^nY_i\to2\zeta(2)-3\) in \(L^1\).

Restriction of the infinite priority arrays to \(\{1,\ldots,n\}\) cannot destroy an edge whose two endpoints remain present: the nearest-lower-priority parent criterion shows that deleting keys outside the interval can create direct edges but cannot destroy a direct edge between retained keys. The expected number of extra finite direct edges in **one** sample equals

\[
\sum_{i<j}(q_{n;i,j}-a_{j-i})=\sum_{s=1}^{n-1}\frac1{s+1}=\mathcal H_n-1,
\]

where \(\mathcal H_n=\sum_{r=1}^n 1/r\) is the harmonic number. The common finite-edge count exceeds the common infinite-edge count restricted to \(\{1,\ldots,n\}\) by a nonnegative quantity. Every edge in this difference must be extra in at least one of the two samples, so this quantity is bounded by the **sum** of the two single-sample extra-edge counts, with expectation \(2(\mathcal H_n-1)\). Also the expected number of common infinite edges starting in \(\{1,\ldots,n\}\) and ending to its right is at most

\[
\sum_{d\ge1}d a_d^2=2-\zeta(2).
\]

It follows that

\[
\mathbb E\left|\frac{H_n}{n}-\frac1n\sum_{i=1}^nY_i\right|
\le\frac{2(\mathcal H_n-1)+2-\zeta(2)}{n}\longrightarrow0.
\]

Combining this estimate with the ergodic limit proves the stated \(L^1\) convergence.

## Verification

The standalone Python 3 checker `check.py` reconstructs both directed parent–child edge frequencies by exhaustive enumeration of **all** insertion permutations for each \(2\le n\le7\), compares every oriented edge frequency to the two rational formulas above, and independently checks the finite common-edge expectation. It also checks the finite square expansion exactly at six additional sizes, and three controlled numerical comparisons with the asymptotic expansion. A local replay produced `PASS 133 exact-or-controlled assertions`. These finite checks support, but do not replace, the analytic proof of the infinite limit.

## Relationship to prior work

Seidel and Aragon's *Randomized Search Trees* supplies the priority/ancestor framework; its ancestor probability \(1/(d+1)\) is not the present **direct-parent** probability. Holmgren and Janson's 2014 analysis treats local fringe-tree counts in single random search trees and their limit laws, not the overlap of corresponding key-labelled parent edges of independent trees. Chu and Cleary's study of common edges uses **uniform Catalan rooted binary trees with leaf-interval edges** and reports a different limiting common-edge fraction of approximately \(0.092958\); neither the sampled distribution nor the edge definition matches this result. Independent uniform Cayley-tree edge-overlap theorems concern another tree ensemble. No priority claim is made against unexamined literature or a general theorem that might imply the calculation.

## Limitations

The result does not give a central limit theorem or variance for \(H_n\), does not extend to correlated insertion orders or biased priorities, and does not cover unlabeled shape overlap. The convergence asserted for \(H_n/n\) is in \(L^1\); no almost-sure limit for independently reconstructed finite pairs is asserted. Historical priority remains subject to examination of other treap literature.

## References

1. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, first public version 26 June 2014, https://arxiv.org/abs/1406.6883 . Primary MSC2010 60C05.
2. R. Seidel and C. R. Aragon, *Randomized Search Trees*, Algorithmica 16 (1996), 464–497, https://doi.org/10.1007/BF01940876 ; authorized author-text mirror https://rtheunissen.github.io/bst/docs/references/1996_seidel_aragon.pdf .
3. T. Chu and S. Cleary, *Expected Conflicts in Pairs of Rooted Binary Trees*, Involve 6 (2013); DOI https://doi.org/10.2140/involve.2013.6.323 , full text https://msp.org/involve/2013/6-3/involve-v6-n3-p05-p.pdf .
4. M. Bóna, F. Burghart, and S. Wagner, *On the Intersection of Pairs of Trees*, first public version 30 January 2025, https://arxiv.org/abs/2501.18570 .
